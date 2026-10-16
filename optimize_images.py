from pathlib import Path
from PIL import Image

ROOT = Path(__file__).parent
WIDTHS = [480, 900]

def optimize_images():
    for src in sorted((ROOT/'images').glob('*.webp')):
        im = Image.open(src).convert('RGB')
        for w in WIDTHS:
            out = ROOT/'dist'/'assets'/f'{src.stem}-{w}.webp'
            im.resize((w, round(im.height*w/im.width)), Image.LANCZOS).save(out, 'WEBP', quality=78, method=6)
            print(f'{out.name}: {out.stat().st_size//1024} KB')

if __name__ == '__main__':
    optimize_images()
