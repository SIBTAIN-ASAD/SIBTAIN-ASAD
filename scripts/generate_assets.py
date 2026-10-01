"""Generate a compact, transparent GitHub profile animation.
Requires Pillow. Uses Arial on macOS or DejaVu Sans on Linux.
PROFILE_FONT_DIR can override the macOS font directory.
"""
from pathlib import Path
import os
from PIL import Image, ImageDraw, ImageFont, ImageChops

OUT = Path(__file__).resolve().parents[1] / 'assets'
OUT.mkdir(exist_ok=True)
root = Path(os.environ.get('PROFILE_FONT_DIR', '/System/Library/Fonts/Supplemental'))
path = root / 'Arial.ttf'
font = ImageFont.truetype(str(path) if path.exists() else 'DejaVuSans.ttf', 32)
W, H = 1000, 86
phrases = ['Building thoughtful interfaces.', 'Designing dependable APIs.', 'Exploring AI and open source.']
for theme, fg in [('dark', '#9198a1'), ('light', '#59636e')]:
    frames = []
    for frame in range(144):
        # Reserve a unique flat color for transparent pixels in the GIF palette.
        im = Image.new('RGB', (W, H), '#ff00ff')
        d = ImageDraw.Draw(im)
        phase = frame % 48
        phrase = phrases[frame // 48]
        count = min(len(phrase), int(phase * 1.2))
        d.text((0, 23), '> ', font=font, fill='#3fb950')
        d.text((36, 23), phrase[:count], font=font, fill=fg)
        if phase % 12 < 7:
            x = 40 + d.textlength(phrase[:count], font=font)
            d.rectangle((x, 27, x+3, 56), fill='#3fb950')
        # A small branch graph carries a moving signal; no enclosing card.
        color = '#30363d' if theme == 'dark' else '#d1d9e0'
        d.line([(720,43),(775,43),(815,20),(880,20),(930,43),(985,43)],fill=color,width=3)
        d.line([(775,43),(815,67),(880,67),(930,43)],fill=color,width=3)
        for x,y in [(720,43),(815,20),(880,67),(985,43)]:
            d.ellipse((x-6,y-6,x+6,y+6),fill='#3fb950')
        f=(frame%48)/48
        x=720+265*f
        y=43 if x<775 or x>930 else (43-(x-775)*23/40 if x<815 else (20 if x<880 else 20+(x-880)*23/50))
        d.ellipse((x-4,y-4,x+4,y+4),fill='#58a6ff' if theme=='dark' else '#0969da')
        pal=im.quantize(colors=254,dither=Image.Dither.NONE)
        index=pal.getpixel((W-1,0))
        pal.info['transparency']=index
        frames.append(pal)
    frames[0].save(OUT/f'activity-{theme}.gif',save_all=True,append_images=frames[1:],duration=80,loop=0,disposal=2,optimize=False)
    static=frames[30].convert('RGBA')
    static.save(OUT/f'activity-{theme}.png')
    check=Image.open(OUT/f'activity-{theme}.gif')
    assert check.n_frames == 144 and check.info['loop'] == 0
    check.seek(30)
    assert check.convert('RGBA').getpixel((999,0))[3] == 0
    print(theme, round((OUT/f'activity-{theme}.gif').stat().st_size/1024), 'KB; 144 frames; transparent background')
