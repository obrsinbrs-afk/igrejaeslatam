import { countryCurrencies } from './country-currencies.mjs';

const GEO_URL = 'https://get.geojs.io/v1/ip/country.json';
const RATES_URL = 'https://open.er-api.com/v6/latest/USD';
const GEO_KEY = 'brote-country-v1';
const RATES_KEY = 'brote-usd-rates-v1';
const DAY = 24 * 60 * 60 * 1000;
const currencyNames = {
  USD: 'dólares estadounidenses', COP: 'pesos colombianos', MXN: 'pesos mexicanos',
  ARS: 'pesos argentinos', CLP: 'pesos chilenos', PEN: 'soles peruanos',
  BRL: 'reales brasileños', BOB: 'bolivianos', VES: 'bolívares venezolanos',
  UYU: 'pesos uruguayos', PYG: 'guaraníes paraguayos', CRC: 'colones costarricenses',
  GTQ: 'quetzales guatemaltecos', HNL: 'lempiras hondureños', NIO: 'córdobas nicaragüenses',
  DOP: 'pesos dominicanos', CUP: 'pesos cubanos', PAB: 'balboas panameños',
  EUR: 'euros', CAD: 'dólares canadienses', GBP: 'libras esterlinas',
};

// Storage is optional: privacy settings must never prevent the conversion.
function readCache(storage, key, now) {
  try {
    const value = JSON.parse(storage?.getItem(key) || 'null');
    return value && Number.isFinite(value.expires) && value.expires > now ? value.data : null;
  } catch { return null; }
}

function writeCache(storage, key, data, expires) {
  try { storage?.setItem(key, JSON.stringify({ data, expires })); } catch { /* optional */ }
}

function browserStorage(name) {
  try { return globalThis[name]; } catch { return null; }
}

async function getJson(url, fetcher) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), 5500);
  try {
    const response = await fetcher(url, {
      signal: controller.signal, credentials: 'omit', referrerPolicy: 'no-referrer',
      headers: { Accept: 'application/json' },
    });
    if (!response.ok) throw new Error('Provider unavailable');
    return await response.json();
  } finally { clearTimeout(timer); }
}

export function makeQuote(country, rates, usdAmount, updatedAt = null) {
  const currency = countryCurrencies[country];
  const rate = currency === 'USD' ? 1 : rates?.[currency];
  if (!currency || !Number.isFinite(rate) || rate <= 0 || !Number.isFinite(usdAmount) || usdAmount <= 0) {
    throw new Error('No valid conversion');
  }
  const amount = usdAmount * rate;
  if (!Number.isFinite(amount) || amount <= 0) throw new Error('Invalid converted amount');
  const locale = country === 'BR' ? 'pt-BR' : `es-${country}`;
  const options = { style: 'currency', currency, currencyDisplay: 'code' };
  if (['COP', 'CLP', 'PYG'].includes(currency)) {
    options.minimumFractionDigits = 0;
    options.maximumFractionDigits = 0;
  }
  const formatted = new Intl.NumberFormat(locale, options).format(amount);
  const name = currencyNames[currency] || new Intl.DisplayNames(['es'], { type: 'currency' }).of(currency);
  return { country, currency, amount, text: `≈ ${formatted} · ${name}`, updatedAt };
}

export async function getLocalQuote(usdAmount, options = {}) {
  const fetcher = options.fetcher || globalThis.fetch.bind(globalThis);
  const geoStorage = options.geoStorage === undefined ? browserStorage('sessionStorage') : options.geoStorage;
  const rateStorage = options.rateStorage === undefined ? browserStorage('localStorage') : options.rateStorage;
  const now = options.now ?? Date.now();
  let country = readCache(geoStorage, GEO_KEY, now);
  if (typeof country !== 'string' || !countryCurrencies[country]) {
    const geo = await getJson(GEO_URL, fetcher);
    country = typeof geo.country === 'string' ? geo.country.toUpperCase() : '';
    if (!countryCurrencies[country]) throw new Error('Unknown country');
    // Discard the IP and all other fields returned by the provider.
    writeCache(geoStorage, GEO_KEY, country, now + 30 * 60 * 1000);
  }
  if (countryCurrencies[country] === 'USD') return makeQuote(country, {}, usdAmount);
  let data = readCache(rateStorage, RATES_KEY, now);
  if (!validRates(data, now)) {
    data = await getJson(RATES_URL, fetcher);
    if (!validRates(data, now)) throw new Error('Invalid exchange rates');
    const expires = Math.min(data.time_next_update_unix * 1000, now + DAY);
    // Save only the data used by the converter.
    data = {
      result: 'success', base_code: 'USD', rates: data.rates,
      time_last_update_unix: data.time_last_update_unix,
      time_next_update_unix: data.time_next_update_unix,
    };
    writeCache(rateStorage, RATES_KEY, data, expires);
  }
  return makeQuote(country, data.rates, usdAmount, data.time_last_update_unix * 1000);
}

function validRates(data, now) {
  return data?.result === 'success' && data.base_code === 'USD' && data.rates?.USD === 1 &&
    Number.isFinite(data.time_last_update_unix) && Number.isFinite(data.time_next_update_unix) &&
    data.time_next_update_unix * 1000 > now && data.time_last_update_unix * 1000 <= now + 300000 &&
    now - data.time_last_update_unix * 1000 < 2 * DAY;
}

export async function showLocalPrice(doc = document, options = {}) {
  const targets = [...doc.querySelectorAll('[data-local-price]')];
  if (!targets.length) return;
  const amount = Number(doc.querySelector('[data-offer-usd]')?.dataset.offerUsd);
  try {
    const quote = await getLocalQuote(amount, options);
    for (const target of targets) {
      target.textContent = quote.text;
      target.dataset.priceState = 'ready';
      target.dataset.currency = quote.currency;
    }
    if (quote.updatedAt) {
      const date = new Intl.DateTimeFormat('es-419', { dateStyle: 'short', timeZone: 'UTC' }).format(quote.updatedAt);
      doc.querySelectorAll('[data-rate-date]').forEach(el => {
        el.textContent = `Cotización: ${date}`;
        el.hidden = false;
      });
    }
  } catch {
    for (const target of targets) {
      target.textContent = 'Precio en USD. Consulta el equivalente local al pagar.';
      target.dataset.priceState = 'unavailable';
    }
  }
}

if (typeof document !== 'undefined') showLocalPrice();
