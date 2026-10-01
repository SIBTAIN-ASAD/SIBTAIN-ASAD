"""Generate the profile's original UI artwork and animation.
Requires Pillow and NumPy. Set PROFILE_FONT_DIR to a directory containing
Arial.ttf and Arial Bold.ttf, or let the script use DejaVu Sans on Linux.
"""
from pathlib import Path
import math, os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

OUT = Path(__file__).resolve().parents[1] / 'assets'
OUT.mkdir(exist_ok=True)
W = 1100
FONT_DIR = Path(os.environ.get('PROFILE_FONT_DIR', '/System/Library/Fonts/Supplemental'))
def font(n, bold=False):
    p = FONT_DIR / ('Arial Bold.ttf' if bold else 'Arial.ttf')
    return ImageFont.truetype(str(p) if p.exists() else ('DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf'), n)
WHITE = '#F2F3FF'; MUTED = '#A3AAC8'; CYAN = '#6CE9EF'; PURPLE = '#B99AFF'
def text(d, xy, s, size=20, fill=WHITE, bold=False):
    d.text(xy, s, font=font(size, bold), fill=fill)
def base(h):
    y,x = np.mgrid[0:h,0:W]
    a = np.exp(-((x-850)**2/140000 + (y-h*.4)**2/90000))
    b = np.exp(-((x-80)**2/160000 + (y-h)**2/85000))
    arr = np.stack([10+22*a+4*b,13+13*a+9*b,26+45*a+12*b],axis=2).astype('uint8')
    im=Image.fromarray(arr)
    d=ImageDraw.Draw(im)
    d.rounded_rectangle((1,1,W-2,h-2), radius=24, outline='#34364F', width=2)
    return im

def chip(d,x,y,label,color=PURPLE):
    w=int(d.textlength(label,font=font(16)))+26
    d.rounded_rectangle((x,y,x+w,y+32),radius=10, fill='#1C2038',outline='#363A55')
    text(d,(x+13,y+7),label,16,color)
    return x+w+10

# Hero: continuously rotating 3D sphere, orbiting signals and a typing terminal.
H=510
bg=base(H)
d=ImageDraw.Draw(bg)
for x in range(650,W,28):
    for y in range(30,H-30,28): d.ellipse((x,y,x+1,y+1),fill='#37344D')
d.rounded_rectangle((42,34,355,67),radius=16,fill='#22203D',outline='#514574')
d.ellipse((55,46,63,54),fill=CYAN)
text(d,(76,42),'SOFTWARE ENGINEER  /  LAHORE',14,PURPLE,True)
text(d,(42,107),'Muhammad',47,WHITE,True)
text(d,(39,159),'Sibtain Asad',72,WHITE,True)
text(d,(44,254),'Building across the stack.',29,WHITE,True)
text(d,(44,298),'Interfaces. APIs. AI experiments.',21,MUTED)
x=44
for label in ['TYPESCRIPT','PYTHON','REACT','DJANGO']: x=chip(d,x,343,label)
d.rounded_rectangle((42,408,650,476),radius=13,fill='#0C1020',outline='#343B54')
text(d,(62,431),'>',22,CYAN,True)
text(d,(766,451),'CODE  /  CONNECT  /  CREATE',14,MUTED)
points=[]
for j in range(1,20):
    lat=math.pi*j/20
    count=max(8,round(44*math.sin(lat)))
    for k in range(count):
        lon=2*math.pi*k/count
        points.append((math.sin(lat)*math.cos(lon),math.cos(lat),math.sin(lat)*math.sin(lon)))
frames=[]
N=96
for f in range(N):
    im=bg.copy(); draw=ImageDraw.Draw(im); t=2*math.pi*f/N
    # Elliptical orbital tracks, deliberately quiet behind the point cloud.
    draw.ellipse((696,93,1048,402),outline='#4C416F',width=1)
    draw.ellipse((678,164,1068,324),outline='#325664',width=1)
    cloud=[]
    for x,y,z in points:
        xx=x*math.cos(t)-z*math.sin(t); zz=x*math.sin(t)+z*math.cos(t)
        yy=y*.95-zz*.24; zz=y*.24+zz*.95
        cloud.append((zz,873+xx*149,249+yy*149))
    for z,x,y in sorted(cloud):
        strength=(z+1)/2
        col=tuple(int(a+(b-a)*strength) for a,b in zip((38,39,83),(126,218,250)))
        r=1+1.3*strength
        draw.ellipse((x-r,y-r,x+r,y+r),fill=col)
    glow=Image.new('RGB',im.size); gd=ImageDraw.Draw(glow)
    for k in range(3):
        a=t+k*2*math.pi/3
        px=873+193*math.cos(a); py=246+80*math.sin(a)
        gd.ellipse((px-6,py-6,px+6,py+6),fill=(85,196,228))
    im=ImageChops.add(im,glow.filter(ImageFilter.GaussianBlur(12)))
    draw=ImageDraw.Draw(im)
    for k in range(3):
        a=t+k*2*math.pi/3; px=873+193*math.cos(a); py=246+80*math.sin(a)
        draw.ellipse((px-3,py-3,px+3,py+3),fill=CYAN)
    phase=f%48
    message=['build thoughtful interfaces','engineer dependable systems'][f//48]
    n=min(len(message),int(phase*1.2))
    typed=message[:n]
    text(draw,(88,431),typed,21,'#DBDCF8')
    if phase%12<8:
        cx=88+draw.textlength(typed,font=font(21))+4
        draw.rectangle((cx,432,cx+9,453),fill=CYAN)
    frames.append(im)
# Global palette avoids flicker; retain smooth animation at a modest file size.
palette=frames[24].quantize(colors=128)
indexed=[im.quantize(palette=palette,dither=Image.Dither.NONE) for im in frames]
indexed[0].save(OUT/'profile-hero.gif',save_all=True,append_images=indexed[1:],duration=80,loop=0,optimize=True,disposal=1)
frames[24].save(OUT/'profile-hero-static.png')

def project(filename, number,title,subtitle,lines,tags,kind):
    im=base(300); d=ImageDraw.Draw(im)
    text(d,(36,28),f'{number}  /  SELECTED PROJECT',14,CYAN,True)
    text(d,(34,68),title,42,WHITE,True)
    text(d,(36,124),subtitle,21,PURPLE)
    for i,line in enumerate(lines): text(d,(36,163+i*27),line,18,MUTED)
    x=36
    for label in tags: x=chip(d,x,245,label)
    if kind=='map':
        for x in range(723,1070,38): d.line((x,36,x-42,267),fill='#28324C',width=1)
        for y in range(42,268,32): d.line((705,y,1071,y+15),fill='#28324C',width=1)
        pts=[(738,226),(790,180),(845,197),(887,126),(940,140),(1032,72)]
        d.line(pts,fill='#254C68',width=12,joint='curve');d.line(pts,fill=CYAN,width=3,joint='curve')
        for x,y in pts:
            d.ellipse((x-5,y-5,x+5,y+5),fill='#101C30',outline=CYAN,width=2)
        d.rounded_rectangle((862,205,1054,258),radius=10,fill='#172C3B',outline='#375868')
        text(d,(880,216),'ROUTE → REFUEL',16,CYAN,True)
        text(d,(722,44),'US / ROUTE PLANNER',13,MUTED)
    else:
        d.rounded_rectangle((714,38,1064,261),radius=13,fill='#0B1020',outline='#514575',width=2)
        d.line((714,67,1064,67),fill='#34304A')
        for i,c in enumerate(['#B99AFF','#6CE9EF','#56647E']):d.ellipse((728+i*15,49,734+i*15,55),fill=c)
        text(d,(741,93),'SAM',28,WHITE,True)
        text(d,(741,134),'DESIGN × ENGINEERING',12,PURPLE)
        for i,w in enumerate([95,128,75]):d.rounded_rectangle((741,169+i*13,741+w,173+i*13),radius=2,fill='#39425E')
        for r in [25,43,62]:d.ellipse((968-r,157-r,968+r,157+r),outline='#7563B2',width=2)
        d.line((920,199,1017,113),fill=CYAN,width=2)
        d.rounded_rectangle((741,224,828,241),radius=7,fill='#B99AFF')
    im.save(OUT/filename)
project('project-spotter.png','01','Spotter','Route intelligence, from API to map.', ['US driving routes and fuel-stop recommendations.','Django services, tested logic, and an interactive map.'],['PYTHON','DJANGO REST','DOCKER','PYTEST'],'map')
project('project-portfolio.png','02','SAM / Portfolio','A space for code, craft, and motion.', ['An interactive showcase of my projects and experience.','React interfaces with 3D visuals and animation.'],['TYPESCRIPT','REACT','THREE.JS','MOTION'],'web')

im=base(270);d=ImageDraw.Draw(im)
text(d,(36,24),'THE TOOLKIT',15,CYAN,True)
cols=[('01','INTERFACES',['TypeScript · React','Next.js · Tailwind CSS']),('02','BACKEND',['Python · Django','FastAPI · PostgreSQL']),('03','INFRASTRUCTURE',['Docker · GitHub Actions','AWS · Azure · GCP']),('04','AI EXPLORATION',['PyTorch · TensorFlow','Reinforcement learning'])]
for i,(n,title,lines) in enumerate(cols):
    x=25+i*270
    d.rounded_rectangle((x,66,x+245,240),radius=14,fill='#13192D',outline='#32364F')
    text(d,(x+18,84),n,26,PURPLE,True)
    text(d,(x+18,129),title,16,WHITE,True)
    for j,line in enumerate(lines):text(d,(x+18,170+j*26),line,16,MUTED)
im.save(OUT/'toolkit.png')

im=base(150);d=ImageDraw.Draw(im)
text(d,(37,30),'Good software starts with a conversation.',32,WHITE,True)
text(d,(39,85),'Engineering problems, collaborations, and open-source ideas.',20,MUTED)
d.rounded_rectangle((890,46,1057,104),radius=15,fill='#BCA4FF')
text(d,(915,64),"LET'S TALK",18,'#151326',True)
im.save(OUT/'connect.png')
print('Generated',len(frames),'animation frames.')
for p in sorted(OUT.iterdir()): print(p.name,round(p.stat().st_size/1024),'KB')
