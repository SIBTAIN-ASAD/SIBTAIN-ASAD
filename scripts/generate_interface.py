"""Original geometric profile UI: themed section rails, links and project diagrams."""
from pathlib import Path
from html import escape
OUT=Path(__file__).resolve().parents[1]/'assets'
sections=[('oss','01','Open source','#bc8cff','#8250df'),('build','02','Selected projects','#58cde8','#087d98'),('career','03','Experience','#79b8ff','#0969da'),('activity','04','GitHub activity','#56d4a2','#16794d'),('tools','05','Technologies & tools','#e3b341','#986800')]
for theme in ['dark','light']:
 dark=theme=='dark';bg='#0d1117' if dark else '#ffffff';surface='#161b22' if dark else '#f6f8fa';fg='#e6edf3' if dark else '#1f2328';border='#303d4c' if dark else '#d1d9e0';muted='#8b9eb0' if dark else '#576579'
 for slug,num,title,dc,lc in sections:
  c=dc if dark else lc
  for mobile in [False,True]:
   W=360 if mobile else 720;h=48
   s=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}" role="img" aria-label="{escape(title)}"><defs><linearGradient id="g"><stop stop-color="{c}"/><stop offset=".55" stop-color="{'#b6a1e8' if dark else '#8250df'}"/><stop offset="1" stop-color="{c}" stop-opacity=".1"/></linearGradient></defs><style>@media(prefers-reduced-motion:reduce){{.signal{{display:none}}}}</style><path d="M1 34V12L9 4H35V34Z" fill="{surface}" stroke="{border}"/><path d="M1 22V12L9 4H19" fill="none" stroke="{c}"/><text x="10" y="24" fill="{c}" font-family="monospace" font-size="12">{num}</text><text x="47" y="25" fill="{fg}" font-family="Arial,sans-serif" font-size="18" font-weight="600">{escape(title)}</text><path d="M1 42H{W-13}L{W-1} 30" fill="none" stroke="url(#g)"/><path d="M{W-30} 10H{W-12}M{W-22} 17H{W-4}" stroke="{c}" stroke-width="1" opacity=".6"/>'''
   if not mobile:
    s+=f'<path d="M400 23H440L449 14H478L487 23H580L589 14H639" stroke="{border}" fill="none"/><circle cx="449" cy="14" r="2" fill="{c}"/><circle cx="589" cy="14" r="2" fill="{c}"/>'
   s+=f'<circle class="signal" cx="1" cy="42" r="1.5" fill="{c}" opacity=".75"><animate attributeName="cx" values="1;{W-15};{W-15}" dur="9s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;.9;.9;0" dur="9s" repeatCount="indefinite"/></circle></svg>'
   (OUT/f'interface-{slug}{"-mobile" if mobile else ""}-{theme}.svg').write_text(s)
 for slug,label,w,c in [('portfolio','Portfolio ↗',112,'#58cde8'),('linkedin','LinkedIn ↗',106,'#79b8ff'),('repos','Repositories ↗',136,'#bc8cff'),('prs','View merged PRs ↗',164,'#bc8cff'),('background','Full background ↗',156,'#79b8ff')]:
  c=c if dark else '#0969da'
  (OUT/f'action-{slug}-{theme}.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="32"><defs><linearGradient id="g"><stop stop-color="{surface}"/><stop offset="1" stop-color="{bg}"/></linearGradient></defs><path d="M.5 .5H{w-9}L{w-.5} 9V31.5H.5Z" fill="url(#g)" stroke="{border}"/><path d="M.5 9V.5H17M{w-17} 31.5H{w-.5}V23" fill="none" stroke="{c}"/><text x="12" y="21" fill="{fg}" font-family="Arial,sans-serif" font-size="12" font-weight="600">{label}</text></svg>')
 for slug,labels,c in [('spotter',['ROUTE','FUEL DATA','PLANNER'],'#58cde8' if dark else '#087d98'),('portfolio',['REACT','3D SCENE','MOTION'],'#bc8cff' if dark else '#8250df')]:
  # Narrow enough to stay legible in a mobile README; a diagram, not a content card.
  s=f'<svg xmlns="http://www.w3.org/2000/svg" width="360" height="46" viewBox="0 0 360 46"><path d="M12 23H347" stroke="{border}"/><path d="M114 23H140M230 23H254" stroke="{c}" stroke-width="1"/>'
  for i,label in enumerate(labels):
   x=2+i*120
   s+=f'<path d="M{x} 7H{x+99}L{x+108} 16V38H{x}Z" fill="{surface}" stroke="{border}"/><path d="M{x} 18V7H{x+16}" stroke="{c}" fill="none"/><text x="{x+13}" y="26" fill="{c}" font-family="monospace" font-size="11">{label}</text>'
  s+='</svg>';(OUT/f'project-flow-{slug}-{theme}.svg').write_text(s)
