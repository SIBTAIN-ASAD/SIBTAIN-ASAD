"""Render repository-owned contribution cards using the GitHub calendar API."""
import argparse,json,os,urllib.request
from datetime import date,datetime,timedelta
from zoneinfo import ZoneInfo
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]/'assets'
QUERY='query { user(login:"SIBTAIN-ASAD") { contributionsCollection { contributionCalendar { totalContributions weeks { contributionDays { date contributionCount } } } } } }'
def metrics(days,today):
 counts={date.fromisoformat(d['date']):d['contributionCount'] for d in days if date.fromisoformat(d['date'])<=today}
 end=today if counts.get(today,0) else today-timedelta(days=1)
 current=0
 while counts.get(end,0)>0:current+=1;end-=timedelta(days=1)
 longest=run=0;prev=None
 for day,count in sorted(counts.items()):
  run=(run+1 if prev==day-timedelta(days=1) else 1) if count else 0
  longest=max(longest,run);prev=day
 return current,longest

def render(calendar,today):
 days=[d for week in calendar['weeks'] for d in week['contributionDays']]
 current,longest=metrics(days,today)
 for dark in [True,False]:
  bg='#0d1117' if dark else '#ffffff';panel='#161b22' if dark else '#f6f8fa';border='#303d4c' if dark else '#d1d9e0';fg='#e6edf3' if dark else '#1f2328';muted='#98a8b9' if dark else '#59636e'
  colors=['#79b8ff','#56d4a2','#bc8cff'] if dark else ['#0969da','#16794d','#8250df']
  for mobile in [False,True]:
   W=360 if mobile else 720;H=206 if mobile else 210
   s=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="6" fill="{panel}" stroke="{border}"/>']
   s.append(f'<path d="M1 25V7L7 1H38M{W-38} {H-1}H{W-7}L{W-1} {H-7}V{H-25}" fill="none" stroke="{colors[0]}" stroke-width="1"/><path d="M40 1H{W//2}" stroke="{colors[2]}" stroke-opacity=".4"/>')
   def text(x,y,t,size=12,color=muted,weight=400):s.append(f'<text x="{x}" y="{y}" fill="{color}" font-family="Arial,sans-serif" font-size="{size}" font-weight="{weight}">{t}</text>')
   text(16,25,'GITHUB ACTIVITY',11,fg,600);text(16,43,'Past year · updated '+today.isoformat()+' PKT',10)
   labels=['Contributions','Current streak','Longest streak']
   for i,(label,num) in enumerate(zip(labels,[calendar['totalContributions'],current,longest])):
    x=16+i*((W-24)/3)
    text(x,87,str(num),32,colors[i],600);text(x,109,label,10 if mobile else 12)
    text(x,126,'past year' if i==0 else ('days · PKT' if i==1 else 'days · past year'),9)
    if i<2:s.append(f'<path d="M{x+(W-24)/3-12} 61V128" stroke="{border}"/>')
   text(16,151,'RECENT 12 WEEKS',9)
   recent=days[-84:];gap=(W-32)/84
   for i,day in enumerate(recent):
    count=day['contributionCount'];opacity=0.25 if not count else min(1,.4+count/20)
    s.append(f'<rect x="{16+i*gap:.2f}" y="160" width="{max(1,gap-1):.2f}" height="14" rx="1" fill="{colors[1] if count else border}" opacity="{opacity}"/>')
   text(16,194,'Calendar contributions · today may still be in progress',9)
   s.append('</svg>');(OUT/f'activity{"-mobile" if mobile else ""}-{"dark" if dark else "light"}.svg').write_text(''.join(s))
 return {'contributions':calendar['totalContributions'],'current_streak':current,'longest_streak_past_year':longest,'updated':str(today)}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--input');args=p.parse_args()
 if args.input:data=json.loads(Path(args.input).read_text())
 else:
  req=urllib.request.Request('https://api.github.com/graphql',data=json.dumps({'query':QUERY}).encode(),headers={'Authorization':'Bearer '+os.environ['GH_TOKEN'],'Content-Type':'application/json'})
  with urllib.request.urlopen(req,timeout=30) as response:data=json.load(response)
 if data.get('errors'):raise RuntimeError(data['errors'])
 print(json.dumps(render(data['data']['user']['contributionsCollection']['contributionCalendar'],datetime.now(ZoneInfo('Asia/Karachi')).date())))
