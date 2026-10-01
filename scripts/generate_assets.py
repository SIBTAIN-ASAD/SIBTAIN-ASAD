"""Generate GitHub-themed profile artwork; requires Pillow.
Arial/SF Mono on macOS; DejaVu Sans/Mono on Linux.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math
from html import escape
OUT=Path(__file__).resolve().parents[1]/'assets'
OUT.mkdir(exist_ok=True)
def font(size,mono=False,bold=False):
 p=Path('/System/Library/Fonts/SFNSMono.ttf') if mono else Path('/System/Library/Fonts/Supplemental')/('Arial Bold.ttf' if bold else 'Arial.ttf')
 fallback='DejaVuSansMono.ttf' if mono else ('DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf')
 return ImageFont.truetype(str(p) if p.exists() else fallback,size)
W,H=1000,302
for theme in ['dark','light']:
 dark=theme=='dark'
 bg='#0d1117' if dark else '#ffffff'; panel='#151b23' if dark else '#f6f8fa'
 border='#3d444d' if dark else '#d1d9e0'; fg='#f0f6fc' if dark else '#1f2328'
 muted='#9198a1' if dark else '#59636e'; blue='#79c0ff' if dark else '#0550ae'
 green='#3fb950' if dark else '#1a7f37'; purple='#d2a8ff' if dark else '#8250df'
 frames=[]
 for f in range(120):
  im=Image.new('RGB',(W,H),bg); d=ImageDraw.Draw(im)
  d.rounded_rectangle((1,1,998,300),radius=12,fill=bg,outline=border,width=2)
  d.rounded_rectangle((2,2,997,51),radius=11,fill=panel)
  d.rectangle((2,28,997,51),fill=panel)
  d.line((1,51,998,51),fill=border,width=1)
  d.line((624,51,624,301),fill=border,width=1)
  d.text((23,16),'<>  engineer.ts',font=font(19,mono=True),fill=fg)
  d.line((19,50,214,50),fill='#f78166',width=3)
  d.text((648,17),'BRANCHING OUT',font=font(17,mono=True),fill=muted)
  lines=[('const engineer = {',purple),('  name: "Sibtain Asad",',blue),('  stack: ["TypeScript", "Python"],',fg),('  focus: ["Web", "APIs", "AI"],',fg),('  mindset: "Always exploring"',green),('};',purple)]
  # The first line is always readable; remaining lines are typed, then held.
  budget=20+int(f*3)
  for i,(line,col) in enumerate(lines):
   visible=line[:max(0,budget)];budget-=len(line)
   d.text((21,78+i*32),str(i+1),font=font(18,mono=True),fill=muted)
   d.text((54,76+i*32),visible,font=font(21,mono=True),fill=col)
   if len(visible)<len(line) and budget+len(line)>=0 and f%12<7:
    x=54+d.textlength(visible,font=font(21,mono=True));d.rectangle((x+2,79+i*32,x+4,98+i*32),fill=fg)
  # Branch graph, with an animated signal along the path.
  pts=[(670,211),(729,211),(777,123),(833,123),(885,211),(954,211)]
  d.line([(670,211),(954,211)],fill=border,width=4)
  d.line(pts,fill=purple,width=4,joint='curve')
  for x,y in [(670,211),(729,211),(777,123),(833,123),(885,211),(954,211)]:
   d.ellipse((x-7,y-7,x+7,y+7),fill=bg,outline=green if y==211 else purple,width=3)
  d.text((671,251),'BUILD',font=font(15,mono=True),fill=muted)
  d.text((764,86),'EXPLORE',font=font(15,mono=True),fill=muted)
  d.text((864,251),'CONTRIBUTE',font=font(15,mono=True),fill=muted)
  lengths=[math.dist(a,b) for a,b in zip(pts,pts[1:])];dist=(f%60)/60*sum(lengths)
  for i,length in enumerate(lengths):
   if dist<=length:
    a,b=pts[i],pts[i+1];v=dist/length;x=a[0]+v*(b[0]-a[0]);y=a[1]+v*(b[1]-a[1]);break
   dist-=length
  d.ellipse((x-5,y-5,x+5,y+5),fill=blue)
  frames.append(im)
 palette=frames[80].quantize(colors=128)
 quant=[im.quantize(palette=palette,dither=Image.Dither.NONE) for im in frames]
 quant[0].save(OUT/f'engineering-{theme}.gif',save_all=True,append_images=quant[1:],duration=80,loop=0,optimize=True,disposal=1)
 frames[80].save(OUT/f'engineering-{theme}.png')
 print(theme,(OUT/f'engineering-{theme}.gif').stat().st_size//1024,'KB')
# Familiar flat badges. Fixed colors are deliberate for legibility in either theme.
badges=[('typescript','TS','TypeScript','#3178c6'),('python','Py','Python','#3572a5'),('react','⚛','React','#087ea4'),('django','Dj','Django','#237249'),('postgresql','Pg','PostgreSQL','#4169a1'),('docker','D','Docker','#0969da'),('pytorch','AI','PyTorch','#b83c20'),('merged','↳','Merged','#8250df')]
for slug,icon,label,color in badges:
 width=54+len(label)*7
 svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="28" role="img" aria-label="{escape(label)}"><rect width="{width}" height="28" rx="6" fill="#24292f"/><path d="M6 0H34V28H6Q0 28 0 22V6Q0 0 6 0" fill="{color}"/><text x="17" y="18" text-anchor="middle" fill="white" font-family="Arial,sans-serif" font-size="12" font-weight="700">{escape(icon)}</text><text x="44" y="18" fill="white" font-family="Arial,sans-serif" font-size="12">{escape(label)}</text></svg>'''
 (OUT/f'{slug}.svg').write_text(svg)
