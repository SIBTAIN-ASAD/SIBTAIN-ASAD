"""Render compact, borderless profile sections in light and dark themes."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math
OUT=Path(__file__).resolve().parents[1]/'assets'
S=2
ROLES=[('NavForward','Senior Software Engineer','JUN 2025 — PRESENT','Backend architecture & distributed data pipelines'),('Turing','Software Engineer','JUN — DEC 2025','LLM training, agent evaluation & scoring pipelines'),('Devsinc','Software Engineer','NOV 2023 — JUN 2025','Enterprise applications & frontend architecture'),('i2c','Associate Software Engineer','SEP — NOV 2023','Production operations, releases & monitoring')]
WORK=[('Legal data intelligence','NAVFORWARD','Django / Selenium / Celery / Redis'),('Healthcare referral workflows','DEVSINC','React / TypeScript / integrations'),('AI-agent evaluation','TURING','Datasets / scoring / prompt refinement')]
CONTRIB=[('airflow','APACHE AIRFLOW','Async datetime sensor fix','Resolved DAG parsing failures for templated targets.','#72659'),('django','DJANGO-STUBS','Mutable request typing','Preserved request subclass inference in typed tests.','#3642'),('gaia','AMD GAIA','Telegram media feedback','Explicit feedback for unsupported uploads; regression coverage.','#3263')]
GROUPS=[('Frontend','TypeScript / React / Next.js / Tailwind / Three.js'),('Backend & data','Python / Django / FastAPI / PostgreSQL / Redis'),('Infrastructure','Docker / GitHub Actions / AWS / Azure / GCP'),('Machine learning','PyTorch / TensorFlow / Reinforcement learning')]
def font(n,b=False):
 p=Path('/System/Library/Fonts/Supplemental')/('Arial Bold.ttf' if b else 'Arial.ttf')
 return ImageFont.truetype(str(p),n*S)
for theme in ['dark','light']:
 bg='#0d1117' if theme=='dark' else '#ffffff';fg='#e6edf3' if theme=='dark' else '#1f2328';muted='#98a5b3' if theme=='dark' else '#59636e';rule='#253341' if theme=='dark' else '#d8e1e8';cyan='#7bd4e6' if theme=='dark' else '#096f8a';violet='#afa1d4' if theme=='dark' else '#7352a1'
 for mobile in [False,True]:
  W=600 if mobile else 960
  suffix=('-mobile' if mobile else '')+'-slim-'+theme+'.png'
  def canvas(h):
   im=Image.new('RGB',(W*S,h*S),bg);return im,ImageDraw.Draw(im)
  def text(x,y,t,n=20,c=None,b=False):d.text((x*S,y*S),t,font=font(n,b),fill=c or fg)
  def line(points,c=None,w=1):d.line([(x*S,y*S) for x,y in points],fill=c or rule,width=max(1,round(w*S)))
  def header(num,title):
   text(12,9,num,15,cyan);text(49,9,title,16,muted);line([(12,38),(W-12,38)]);line([(12,38),(60,38)],cyan)
  def save(name):im.save(OUT/(name+suffix),optimize=True)
  # Short rows with an open timeline, no enclosing surfaces.
  step=126 if mobile else 91
  im,d=canvas(56+4*step);header('01','EXPERIENCE')
  for i,(company,role,date,desc) in enumerate(ROLES):
   y=54+i*step;line([(18,y+8),(18,y+step-5)])
   d.ellipse((15*S,(y+8)*S,21*S,(y+14)*S),fill=cyan)
   text(38,y,company,25 if mobile else 23,b=True)
   if mobile:
    text(38,y+32,role,21);text(38,y+62,date,16,cyan);text(38,y+88,desc,18,muted)
   else:
    text(270,y+3,role,20);text(710,y+5,date,15,cyan);text(38,y+37,desc,19,muted)
  save('career')
  step=100 if mobile else 76
  im,d=canvas(52+3*step);header('02','PROFESSIONAL WORK')
  for i,(title,org,scope) in enumerate(WORK):
   y=53+i*step
   if mobile:
    text(12,y,org,15,cyan);text(12,y+25,title,24,b=True);text(12,y+60,scope,18,muted)
   else:
    text(12,y+4,org,15,cyan);text(184,y,title,22,b=True);text(184,y+31,scope,18,muted)
   line([(12,y+step-9),(W-12,y+step-9)])
  save('professional-work')
  for name,title,sub,tech in [('spotter','Spotter','Route planning & fuel optimization','Python / Django REST / GeoJSON / Docker'),('portfolio','SAM Portfolio','My experience, projects & code','TypeScript / React / Three.js / Tailwind')]:
   im,d=canvas(163 if mobile else 153)
   text(12,8,'SELECTED PROJECT',14,cyan);text(12,35,title,29,b=True)
   text(12,78,sub,21);text(12,114,tech,17,muted)
   # Hairline data contours on the right, kept away from the text.
   if not mobile:
    for j in range(6):
     pts=[(730+k*2,69+j*6+15*math.sin(k/100*math.pi*2+j*.2)) for k in range(101)]
     line(pts,cyan if j==2 else rule,.5)
   line([(12,146),(W-12,146)]);line([(12,146),(60,146)],cyan)
   save(name+'-panel')
  for slug,org,title,desc,num in CONTRIB:
   im,d=canvas(134 if mobile else 108)
   text(12,8,org,16,cyan);text(W-172,9,'MERGED / '+num,14,violet)
   text(12,36,title,25 if mobile else 24,b=True)
   if mobile and len(desc)>59:
    text(12,73,'Explicit feedback for unsupported uploads;',18,muted);text(12,97,'regression coverage.',18,muted)
   else:text(12,75 if mobile else 71,desc,18,muted)
   line([(12,132 if mobile else 106),(W-12,132 if mobile else 106)])
   line([(W-35,47),(W-23,47),(W-28,42)],cyan);line([(W-23,47),(W-28,52)],cyan)
   save('contribution-'+slug)
  step=74 if mobile else 51
  im,d=canvas(53+step*4);header('04','TOOLKIT')
  for i,(title,items) in enumerate(GROUPS):
   y=52+i*step;text(12,y,title,20,b=True)
   text(12 if mobile else 225,y+29 if mobile else y+1,items,18,muted)
   line([(12,y+step-9),(W-12,y+step-9)])
  save('skills-panel')
print('Generated compact profile sections.')
