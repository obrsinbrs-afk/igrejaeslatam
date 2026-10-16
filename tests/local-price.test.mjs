import test from 'node:test';
import assert from 'node:assert/strict';
import { getLocalQuote, makeQuote, showLocalPrice } from '../dist/assets/local-price.mjs';

const now = Date.UTC(2026, 9, 16, 15);
const rates = {
  result: 'success', base_code: 'USD',
  time_last_update_unix: (now - 3600000) / 1000,
  time_next_update_unix: (now + 7200000) / 1000,
  rates: { USD: 1, COP: 4000, MXN: 20, BRL: 5, CLP: 1000, PEN: 4, EUR: 0.9 },
};
const storage = () => {
  const map = new Map();
  return { getItem: key => map.get(key), setItem: (key, value) => map.set(key, value), map };
};
const response = data => ({ ok: true, json: async () => data });

test('IP country selects COP despite another browser language; amount includes code and Spanish name', async () => {
  const geoStorage = storage();
  const quote = await getLocalQuote(9.9, {
    now, geoStorage, rateStorage: null,
    fetcher: async url => response(url.includes('geojs') ? { country: 'CO', ip: '203.0.113.1' } : rates),
  });
  assert.equal(quote.currency, 'COP');
  assert.equal(quote.amount, 39600);
  assert.match(quote.text, /COP/);
  assert.match(quote.text, /39[.,]600/);
  assert.match(quote.text, /pesos colombianos/);
  assert.ok(!JSON.stringify([...geoStorage.map]).includes('203.0.113.1'));
});

test('LATAM currencies convert from the same USD 9.90 offer', () => {
  for (const [country, currency, expected] of [
    ['MX', 'MXN', 198], ['BR', 'BRL', 49.5], ['CL', 'CLP', 9900], ['PE', 'PEN', 39.6],
  ]) {
    const quote = makeQuote(country, rates.rates, 9.9);
    assert.equal(quote.currency, currency);
    assert.ok(Math.abs(quote.amount - expected) < 0.000001);
  }
});

test('dollarized countries do not require an FX request', async () => {
  for (const country of ['EC', 'US', 'SV']) {
    let requests = 0;
    const quote = await getLocalQuote(9.9, {
      now, geoStorage: null, rateStorage: null,
      fetcher: async () => { requests++; return response({ country }); },
    });
    assert.equal(quote.currency, 'USD');
    assert.equal(quote.amount, 9.9);
    assert.equal(requests, 1);
  }
});

test('fresh country/rate caches prevent repeat requests; expired rates are refreshed', async () => {
  const geoStorage = storage(), rateStorage = storage();
  let requests = 0;
  const fetcher = async url => {
    requests++;
    return response(url.includes('geojs') ? { country: 'CO' } : rates);
  };
  await getLocalQuote(9.9, { now, geoStorage, rateStorage, fetcher });
  assert.equal(requests, 2);
  await getLocalQuote(9.9, { now: now + 60000, geoStorage, rateStorage, fetcher });
  assert.equal(requests, 2);
  const saved = JSON.parse(rateStorage.getItem('brote-usd-rates-v1'));
  assert.equal(saved.expires, rates.time_next_update_unix * 1000);
  rateStorage.setItem('brote-usd-rates-v1', JSON.stringify({ ...saved, expires: now - 1 }));
  await getLocalQuote(9.9, { now, geoStorage, rateStorage, fetcher });
  assert.equal(requests, 3);
});

test('blocked browser storage does not prevent an accurate conversion', async () => {
  const blocked = { getItem() { throw Error(); }, setItem() { throw Error(); } };
  const quote = await getLocalQuote(9.9, {
    now, geoStorage: blocked, rateStorage: blocked,
    fetcher: async url => response(url.includes('geojs') ? { country: 'CO' } : rates),
  });
  assert.equal(quote.amount, 39600);
});

test('unknown countries, failed providers and invalid rates never produce a fabricated quote', async () => {
  await assert.rejects(getLocalQuote(9.9, { now, geoStorage: null, rateStorage: null, fetcher: async () => response({ country: 'XX' }) }));
  await assert.rejects(getLocalQuote(9.9, { now, geoStorage: null, rateStorage: null, fetcher: async () => ({ ok: false }) }));
  assert.throws(() => makeQuote('CO', { COP: 0 }, 9.9));
  assert.throws(() => makeQuote('CO', { COP: '4000' }, 9.9));
  assert.throws(() => makeQuote('CO', { COP: NaN }, 9.9));
  const old = { ...rates, time_next_update_unix: (now - 1000) / 1000 };
  await assert.rejects(getLocalQuote(9.9, {
    now, geoStorage: null, rateStorage: null,
    fetcher: async url => response(url.includes('geojs') ? { country: 'CO' } : old),
  }));
});

test('network failure clears the loading text and keeps an explicit USD fallback', async () => {
  const target = { textContent: 'Calculando…', dataset: {} };
  const doc = {
    querySelectorAll: selector => selector === '[data-local-price]' ? [target] : [],
    querySelector: () => ({ dataset: { offerUsd: '9.90' } }),
  };
  await showLocalPrice(doc, { now, geoStorage: null, rateStorage: null, fetcher: async () => { throw Error('offline'); } });
  assert.equal(target.dataset.priceState, 'unavailable');
  assert.match(target.textContent, /USD/);
  assert.doesNotMatch(target.textContent, /Calculando|COP/);
});
