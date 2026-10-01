"""Generate fine-line neon artwork for the GitHub profile. Requires Pillow.
Motion is pre-rendered for README compatibility; no scripts or external services.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
from html import escape
import math
OUT=Path(__file__).resolve().parents[1]/'assets';OUT.mkdir(exist_ok=True)
W,H,S=1000,250,2

def font(n,mono=False):
 p=Path('/System/Library/Fonts/SFNSMono.ttf') if mono else Path('/System/Library/Fonts/Supplemental/Arial.ttf')
 return ImageFont.truetype(str(p) if p.exists() else ('DejaVuSansMono.ttf' if mono else 'DejaVuSans.ttf'),n*S)
def line(d,points,color,width=1):d.line([(round(x*S),round(y*S)) for x,y in points],fill=color,width=max(1,round(width*S)),joint='curve')
def text(d,xy,s,n,color,mono=False):d.text((xy[0]*S,xy[1]*S),s,font=font(n,mono),fill=color)
def project(v,t):
 x,y,z=v
 xx=x*math.cos(t)+z*math.sin(t);zz=-x*math.sin(t)+z*math.cos(t)
 return (790+xx*89,126+(y*.92+zz*.28)*89,zz)
for theme in ['dark','light']:
 dark=theme=='dark'
 bg='#0d1117' if dark else '#ffffff';fg='#e6edf3' if dark else '#1f2328';muted='#8b949e' if dark else '#59636e'
 cyan='#67e8f9' if dark else '#007f99';violet='#b9a3ff' if dark else '#7848bc'
 faint='#233642' if dark else '#dae5e9'
 frames=[]
 for f in range(96):
  t=2*math.pi*f/96
  im=Image.new('RGB',(W*S,H*S),bg);d=ImageDraw.Draw(im)
  # Open corner brackets and hairline accents, without a filled panel.
  for pts in [[(0,30),(0,1),(31,1)],[(969,1),(999,1),(999,30)],[(0,220),(0,249),(31,249)],[(969,249),(999,249),(999,220)]]:line(d,pts,faint,.6)
  text(d,(22,20),'WEB ENGINEERING / AI EXPLORATION',14,muted,True)
  text(d,(20,66),'From interface',39,fg)
  text(d,(20,111),'to intelligence.',39,fg)
  text(d,(22,183),'TYPESCRIPT  /  PYTHON  /  OPEN SOURCE',13,muted,True)
  line(d,[(23,223),(250,223),(265,211),(480,211)],faint,.7)
  # A moving pin-light, with a short fading trail, follows the lower trace.
  x=23+(f/96)*215
  line(d,[(max(23,x-36),223),(x,223)],cyan,.8)
  bright=Image.new('RGB',im.size);b=ImageDraw.Draw(bright)
  # Thin rotating wireframe: latitude arcs and meridians form an abstract AI core.
  for j in range(1,7):
   lat=math.pi*j/7
   pts=[project((math.sin(lat)*math.cos(a),math.cos(lat),math.sin(lat)*math.sin(a)),t) for a in [k*2*math.pi/100 for k in range(101)]]
   for a,c in zip(pts,pts[1:]):
    col=cyan if (a[2]+c[2])/2>0 else faint
    line(d,[a[:2],c[:2]],col,.8 if col==cyan else .4)
    if dark and col==cyan:line(b,[a[:2],c[:2]],'#125263',.45)
  for j in range(8):
   lon=j*math.pi/4
   pts=[project((math.sin(a)*math.cos(lon),math.cos(a),math.sin(a)*math.sin(lon)),t) for a in [k*math.pi/90 for k in range(91)]]
   for a,c in zip(pts,pts[1:]):
    line(d,[a[:2],c[:2]],violet if a[2]>0 else faint,.8 if a[2]>0 else .4)
    if dark and a[2]>0:line(b,[a[:2],c[:2]],'#403159',.45)
  # Circuit leads with tiny packet lights.
  paths=[[(606,63),(668,63),(690,85),(710,85)],[(875,80),(909,46),(977,46)],[(690,171),(658,203),(597,203)],[(872,176),(903,207),(972,207)]]
  for n,path in enumerate(paths):
   line(d,path,faint,.7)
   lengths=[math.dist(a,c) for a,c in zip(path,path[1:])];dist=((f/96+n*.23)%1)*sum(lengths)
   for i,length in enumerate(lengths):
    if dist<=length:
     a,c=path[i],path[i+1];v=dist/length;px=a[0]+v*(c[0]-a[0]);py=a[1]+v*(c[1]-a[1]);break
    dist-=length
   b.ellipse(((px-2)*S,(py-2)*S,(px+2)*S,(py+2)*S),fill=cyan if n%2==0 else violet)
   d.ellipse(((px-1)*S,(py-1)*S,(px+1)*S,(py+1)*S),fill=cyan if n%2==0 else violet)
  # Glow belongs to the small light sources, never the typography.
  if dark:
   glow=bright.filter(ImageFilter.GaussianBlur(4*S))
   im=ImageChops.add(im,glow)
   im=ImageChops.add(im,bright.filter(ImageFilter.GaussianBlur(1.1*S)))
  frames.append(im.resize((W,H),Image.Resampling.LANCZOS))
 palette=Image.new('RGB',(W,H*4))
 for n in range(4):palette.paste(frames[n*24],(0,n*H))
 palette=palette.quantize(colors=192)
 quant=[im.quantize(palette=palette,dither=Image.Dither.NONE) for im in frames]
 quant[0].save(OUT/f'neon-core-{theme}.gif',save_all=True,append_images=quant[1:],duration=80,loop=0,optimize=True,disposal=1)
 frames[24].save(OUT/f'neon-core-{theme}.png')
 print(theme,(OUT/f'neon-core-{theme}.gif').stat().st_size//1024,'KB')

# Fine outlined badges, using theme-aware text and no opaque background.
badges=[('typescript','TS','TypeScript'),('python','Py','Python'),('react','R','React'),('django','Dj','Django'),('postgresql','Pg','PostgreSQL'),('docker','D','Docker'),('pytorch','AI','PyTorch'),('merged','PR','Merged')]
for slug,icon,label in badges:
 width=54+len(label)*7
 svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="28" role="img" aria-label="{escape(label)}"><style>.label{{fill:#59636e}}.accent{{fill:#007f99}}@media(prefers-color-scheme:dark){{.label{{fill:#c9d1d9}}.accent{{fill:#67e8f9}}}}</style><defs><linearGradient id="g"><stop stop-color="#22b8cf"/><stop offset="1" stop-color="#a78bfa"/></linearGradient></defs><path d="M7 .5H{width-1}V20L{width-8} 27.5H.5V7Z" fill="none" stroke="url(#g)" stroke-opacity=".55" stroke-width=".7"/><path d="M34 5V23" stroke="#818b98" stroke-opacity=".4" stroke-width=".6"/><text x="17" y="18" text-anchor="middle" class="accent" font-family="monospace" font-size="11">{icon}</text><text x="44" y="18" class="label" font-family="Arial,sans-serif" font-size="12">{label}</text></svg>'''
 (OUT/f'neon-{slug}.svg').write_text(svg)
# Minimal circuit rules join the native GitHub sections visually.
for name,label in [('work','01 / SELECTED WORK'),('contributions','02 / OPEN SOURCE'),('toolkit','03 / ENGINEERING TOOLKIT'),('connect','04 / CONNECT')]:
 svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="32" viewBox="0 0 1000 32" role="img" aria-label="{label}"><defs><linearGradient id="g"><stop stop-color="#22b8cf"/><stop offset=".6" stop-color="#a78bfa"/><stop offset="1" stop-color="#818b98" stop-opacity=".15"/></linearGradient></defs><text x="0" y="21" fill="#818b98" font-family="monospace" font-size="14" letter-spacing="2">{label}</text><path d="M270 17H490L500 7H705L715 17H999" stroke="url(#g)" stroke-width=".75" fill="none"/><circle cx="500" cy="7" r="1.6" fill="#67e8f9"/><path d="M980 12L985 17L980 22" fill="none" stroke="#a78bfa" stroke-width=".7"/></svg>'''
 (OUT/f'neon-{name}.svg').write_text(svg)
# Small line illustrations for the native project cards.
for name in ['route','interface']:
 shape='<path d="M8 58H47L73 20H110L138 54H181L211 8H275"/>' if name=='route' else '<path d="M8 15H275V66H8ZM8 26H275M19 20H21M26 20H28M19 38H88M19 46H66M19 54H77M193 33L177 45L193 57M224 33L240 45L224 57M213 32L204 59"/>'
 svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="284" height="76" viewBox="0 0 284 76" role="img" aria-label="{'Route planning circuit' if name=='route' else 'Interface wireframe'}"><defs><linearGradient id="g"><stop stop-color="#22b8cf"/><stop offset="1" stop-color="#a78bfa"/></linearGradient></defs><g stroke="url(#g)" stroke-width=".8" fill="none" stroke-linejoin="round">{shape}</g></svg>'''
 (OUT/f'neon-{name}.svg').write_text(svg)
