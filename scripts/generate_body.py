"""Render the profile body with a shared light/dark design system. Requires Pillow."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math
OUT=Path(__file__).resolve().parents[1]/'assets';S=2;W=960

def f(n,b=False):
 p=Path('/System/Library/Fonts/Supplemental')/('Arial Bold.ttf' if b else 'Arial.ttf')
 return ImageFont.truetype(str(p) if p.exists() else ('DejaVuSans-Bold.ttf' if b else 'DejaVuSans.ttf'),n*S)
for theme in ['dark','light']:
 bg='#0d1117' if theme=='dark' else '#ffffff';surface='#111820' if theme=='dark' else '#f6f8fa'
 fg='#e6edf3' if theme=='dark' else '#1f2328';muted='#98a5b3' if theme=='dark' else '#59636e'
 border='#2a3642' if theme=='dark' else '#d1d9e0';accent='#7fcce0' if theme=='dark' else '#096f8a';violet='#b9a7e0' if theme=='dark' else '#7352a1'
 def make(h):
  im=Image.new('RGB',(W*S,h*S),bg);return im,ImageDraw.Draw(im)
 def txt(d,x,y,t,n=24,color=None,b=False):d.text((x*S,y*S),t,font=f(n,b),fill=color or fg)
 def line(d,pts,color=None,w=1):d.line([(x*S,y*S) for x,y in pts],fill=color or border,width=max(1,int(w*S)))
 def box(d,x,y,w,h,fill=None):
  fill=fill or surface
  d.rounded_rectangle((x*S,y*S,(x+w)*S,(y+h)*S),radius=10*S,fill=fill,outline=border,width=S)
 def label(d,n,t):txt(d,24,22,n,18,accent);txt(d,74,20,t,22,muted);line(d,[(24,63),(936,63)])
 def save(im,name):im.save(OUT/f'{name}-ui-{theme}.png',optimize=True)
 im,d=make(790);label(d,'01','PROFESSIONAL EXPERIENCE')
 roles=[('NavForward','Senior Software Engineer','JUN 2025 — PRESENT','Backend architecture & distributed data pipelines'),('Turing','Software Engineer','JUN — DEC 2025','LLM training, agent evaluation & scoring pipelines'),('Devsinc','Software Engineer','NOV 2023 — JUN 2025','Enterprise applications & frontend architecture'),('i2c','Associate Software Engineer','SEP — NOV 2023','Production operations, releases & monitoring')]
 line(d,[(40,107),(40,658)],border)
 for i,(company,role,date,desc) in enumerate(roles):
  y=92+i*171
  d.ellipse(((40-5)*S,(y+21-5)*S,(40+5)*S,(y+21+5)*S),fill=bg,outline=accent,width=2*S)
  txt(d,77,y,company,35,b=True);txt(d,77,y+48,role,25)
  txt(d,77,y+87,desc,23,muted)
  txt(d,600,y+9,date,17,accent)
  if i<3:line(d,[(77,y+141),(934,y+141)])
 txt(d,77,750,'Earlier roles and freelance work are detailed below.',19,muted)
 save(im,'career')
 # Professional practice panels form a coherent three-row editorial layout.
 im,d=make(435);label(d,'02','SELECTED PROFESSIONAL WORK')
 for i,(name,org,scope) in enumerate([('Legal data intelligence','NAVFORWARD','Django / Selenium / Celery / Redis'),('Healthcare referral workflows','DEVSINC','React / TypeScript / enterprise integrations'),('AI-agent evaluation','TURING','Evaluation datasets / scoring / prompt refinement')]):
  y=88+i*113;txt(d,25,y,org,16,accent);txt(d,25,y+28,name,28,b=True);txt(d,25,y+66,scope,21,muted)
  if i<2:line(d,[(25,y+99),(935,y+99)])
 save(im,'professional-work')
 for name,num,title,sub,desc,tech in [('spotter','03.1','Spotter','Route planning & fuel optimization',['US routes, fuel prices, and vehicle constraints.','Separate services. Injectable clients. Automated tests.'],'PYTHON / DJANGO REST / GEOJSON / DOCKER'),('portfolio','03.2','SAM Portfolio','My experience, projects & code',['A React interface with 3D visuals and motion.','TypeScript components and structured project content.'],'TYPESCRIPT / REACT / THREE.JS / TAILWIND')]:
  im,d=make(370);box(d,1,1,958,368);txt(d,29,23,num,18,accent);txt(d,99,23,'SELECTED PROJECT',18,muted)
  txt(d,29,72,title,48,b=True);txt(d,30,136,sub,25)
  for j,t in enumerate(desc):txt(d,30,190+j*31,t,21,muted)
  line(d,[(30,286),(931,286)]);txt(d,30,317,tech,18,accent)
  if name=='spotter':
   for j in range(7):line(d,[(705+j*29,65),(685+j*29,243)],border,.5)
   for j in range(5):line(d,[(699,82+j*33),(931,103+j*33)],border,.5)
   pts=[(707,212),(752,173),(787,187),(834,114),(870,130),(921,76)]
   line(d,pts,accent,1)
   for x,y in pts:d.ellipse(((x-3)*S,(y-3)*S,(x+3)*S,(y+3)*S),fill=surface,outline=accent,width=S)
  else:
   for j in range(14):
    pts=[(700+k*2.1,145+(j-6.5)*7+26*math.sin(k/100*math.pi*2+j*.045)) for k in range(101)]
    line(d,pts,accent if j%3==0 else border,.6)
  save(im,name+'-panel')
 for slug,org,title,desc,num in [('airflow','APACHE AIRFLOW','Async datetime sensor fix','Resolved DAG parsing failures for templated targets.','#72659'),('django','DJANGO-STUBS','Mutable request typing','Preserved request subclass inference in typed tests.','#3642'),('gaia','AMD GAIA','Telegram media feedback','Made unsupported uploads explicit; added a regression test.','#3263')]:
  im,d=make(194);box(d,1,1,958,192)
  txt(d,26,22,org,18,accent);txt(d,737,22,'MERGED  /  '+num,16,violet)
  txt(d,26,61,title,32,b=True);txt(d,26,119,desc,23,muted)
  line(d,[(921,86),(935,86),(929,80)],accent);line(d,[(935,86),(929,92)],accent)
  save(im,'contribution-'+slug)
 im,d=make(510);label(d,'05','TECHNICAL BACKGROUND')
 groups=[('Frontend',['TypeScript / JavaScript','React / Next.js / Tailwind CSS','Three.js']),('Backend & data',['Python / Django / FastAPI','Django REST Framework','PostgreSQL / Redis']),('Infrastructure',['Docker / GitHub Actions','AWS / Azure / Google Cloud']),('Machine learning',['PyTorch / TensorFlow','Reinforcement learning'])]
 for i,(title,lines) in enumerate(groups):
  x=24+(i%2)*472;y=88+(i//2)*205;box(d,x,y,440,181)
  txt(d,x+19,y+17,title,28,b=True)
  for j,t in enumerate(lines):txt(d,x+19,y+65+j*29,t,21,muted)
  line(d,[(x+19,y+49),(x+74,y+49)],accent)
 save(im,'skills-panel')
print('Generated themed career, project, contribution and skills panels at 2x resolution.')
# Mobile layouts use fewer columns and larger relative type.
for theme in ['dark','light']:
 bg='#0d1117' if theme=='dark' else '#ffffff';fg='#e6edf3' if theme=='dark' else '#1f2328';muted='#98a5b3' if theme=='dark' else '#59636e';border='#2a3642' if theme=='dark' else '#d1d9e0';accent='#7fcce0' if theme=='dark' else '#096f8a'
 surface='#111c29' if theme=='dark' else '#f6f8fa'
 def mobile(h):
  im=Image.new('RGB',(600*S,h*S),bg);return im,ImageDraw.Draw(im)
 def wrap(d,s,x,y,width=536,n=22):
  words=s.split();line='';rows=[]
  for word in words:
   candidate=(line+' '+word).strip()
   if d.textlength(candidate,font=f(n))>width*S:rows.append(line);line=word
   else:line=candidate
  if line:rows.append(line)
  for i,t in enumerate(rows):txt(d,x,y+i*(n+9),t,n,muted)
 im,d=mobile(925);txt(d,18,15,'01 / PROFESSIONAL EXPERIENCE',20,accent)
 for i,(company,role,date,desc) in enumerate(roles):
  y=65+i*211;box(d,38,y-8,555,198);line(d,[(22,y+17),(22,y+213)],border)
  d.ellipse((17*S,(y+12)*S,27*S,(y+22)*S),fill=accent)
  txt(d,49,y,company,34,b=True);txt(d,49,y+45,role,23)
  txt(d,49,y+81,date,18,accent);wrap(d,desc,49,y+118,510)
 save(im,'career-mobile')
 for name,title,sub,desc,tech in [('spotter','Spotter','Route planning & fuel optimization','US routes and fuel recommendations. Testable services and injectable clients.','Python / Django REST / Docker'),('portfolio','SAM Portfolio','My experience, projects & code','React, 3D visuals and motion. TypeScript components and structured content.','TypeScript / React / Three.js')]:
  im,d=mobile(330);box(d,1,1,598,328);txt(d,19,17,'SELECTED PROJECT',18,accent);txt(d,18,60,title,44,b=True);txt(d,20,119,sub,23)
  wrap(d,desc,20,166);line(d,[(20,268),(580,268)]);txt(d,20,293,tech,20,accent);save(im,name+'-panel-mobile')
 im,d=mobile(470);txt(d,20,14,'02 / SELECTED PROFESSIONAL WORK',19,accent)
 for i,(name,org,scope) in enumerate([('Legal data intelligence','NAVFORWARD','Django / Selenium / Celery / Redis'),('Healthcare referral workflows','DEVSINC','React / TypeScript / integrations'),('AI-agent evaluation','TURING','Datasets / scoring / prompt refinement')]):
  y=70+i*133;box(d,5,y-7,590,120);txt(d,20,y,org,17,accent);txt(d,20,y+31,name,28,b=True);txt(d,20,y+73,scope,21,muted);line(d,[(20,y+114),(580,y+114)])
 save(im,'professional-work-mobile')
 for slug,org,title,desc,num in [('airflow','APACHE AIRFLOW','Async datetime sensor fix','Resolved DAG parsing failures for templated targets.','#72659'),('django','DJANGO-STUBS','Mutable request typing','Preserved request subclass inference in typed tests.','#3642'),('gaia','AMD GAIA','Telegram media feedback','Made unsupported uploads explicit; added a regression test.','#3263')]:
  im,d=mobile(214);box(d,1,1,598,212);txt(d,20,18,org,19,accent);txt(d,420,21,'MERGED',16,muted);txt(d,20,61,title,29,b=True);wrap(d,desc,20,113);save(im,'contribution-'+slug+'-mobile')
 im,d=mobile(760);txt(d,20,15,'05 / TECHNICAL BACKGROUND',20,accent)
 for i,(title,lines) in enumerate(groups):
  y=68+i*170;box(d,5,y-7,590,160);txt(d,20,y,title,30,b=True);line(d,[(20,y+44),(570,y+44)])
  for j,t in enumerate(lines):txt(d,20,y+60+j*29,t,23,muted)
 save(im,'skills-panel-mobile')
