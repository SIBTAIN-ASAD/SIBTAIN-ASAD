"""Render the personal masthead. Requires Pillow; no remote assets.
Typography stays still while a fine-line flow field moves at the right.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import math
OUT=Path(__file__).resolve().parents[1]/'assets';OUT.mkdir(exist_ok=True)
W,H,S=1120,280,2

def font(size,bold=False):
 p=Path('/System/Library/Fonts/Supplemental')/('Arial Bold.ttf' if bold else 'Arial.ttf')
 return ImageFont.truetype(str(p) if p.exists() else ('DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf'),size*S)
def mix(a,b,t):return tuple(round(x+(y-x)*t) for x,y in zip(a,b))
for theme in ['dark','light']:
 dark=theme=='dark';bg=(13,17,23) if dark else (255,255,255)
 fg='#f0f6fc' if dark else '#1f2328';muted='#8b949e' if dark else '#59636e'
 frames=[]
 for frame in range(80):
  phase=frame*2*math.pi/80
  im=Image.new('RGB',(W*S,H*S),bg);d=ImageDraw.Draw(im)
  # Editorial hierarchy: actual identity, with no slogan or decorative labels.
  d.text((12*S,39*S),'Muhammad',font=font(36),fill=muted)
  d.text((10*S,87*S),'Sibtain Asad',font=font(68,True),fill=fg)
  d.text((12*S,187*S),'Software Engineer',font=font(21),fill=fg)
  d.text((12*S,220*S),'Lahore, Pakistan  /  SIBTAIN-ASAD',font=font(16),fill=muted)
  # Smooth parallel data contours, with tapered ends and precise luminous cores.
  glow=Image.new('RGB',im.size);gd=ImageDraw.Draw(glow)
  for j in range(28):
   pts=[]
   for k in range(151):
    u=k/150
    x=582+u*536
    bend=math.sin(u*math.pi)
    y=140+(j-13.5)*5.6 + 45*bend*math.sin(u*math.pi*2+phase+j*.045)
    y+=23*math.sin(phase+u*math.pi)*bend*(j-13.5)/15
    pts.append((x*S,y*S))
   for k,(a,b) in enumerate(zip(pts,pts[1:])):
    u=k/150
    taper=math.sin(math.pi*u)**.65
    strength=taper*(.28+.56*(1-abs(j-13.5)/20))
    hue=mix((62,196,217),(129,156,235),j/27) if dark else mix((0,106,139),(70,83,151),j/27)
    col=mix(bg,hue,strength)
    d.line((a,b),fill=col,width=2)
   if dark and j in [5,14,23]:
    gd.line(pts,fill=(8,27,34),width=2)
  if dark:im=ImageChops.add(im,glow.filter(ImageFilter.GaussianBlur(2*S)))
  frames.append(im.resize((W,H),Image.Resampling.LANCZOS))
 palette=Image.new('RGB',(W,H*4))
 for n in range(4):palette.paste(frames[n*20],(0,n*H))
 palette=palette.quantize(colors=192)
 quant=[f.quantize(palette=palette,dither=Image.Dither.NONE) for f in frames]
 quant[0].save(OUT/f'masthead-{theme}.gif',save_all=True,append_images=quant[1:],duration=90,loop=0,optimize=True,disposal=1)
 frames[20].save(OUT/f'masthead-{theme}.png')
 print(theme,(OUT/f'masthead-{theme}.gif').stat().st_size//1024,'KB')
