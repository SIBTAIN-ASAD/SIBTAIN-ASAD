"""Render the verified toolkit as aligned, borderless columns, with mobile reflow."""
from pathlib import Path
from html import escape
import ast,json,math,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
# Read the shared data without running the old badge generator.
tree=ast.parse((ROOT/'scripts/generate_toolkit.py').read_text())
groups=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='groups' for t in n.targets))
logos=json.loads((ROOT/'scripts/tool_logos.json').read_text())
for dark in [True,False]:
 theme='dark' if dark else 'light';bg='#0d1117' if dark else '#ffffff';fg='#d8e2ed' if dark else '#283342';muted='#8fa0b2' if dark else '#627083';line='#263340' if dark else '#d8e0e8'
 for mobile in [False,True]:
  W=360 if mobile else 720;groupW=360 if mobile else 348
  positions=[];y=0
  if mobile:
   for group in groups:
    h=30+math.ceil(len(group[3])/2)*21+8;positions.append((group,0,y));y+=h
  else:
   for i in range(0,len(groups),2):
    pair=groups[i:i+2];h=30+max(math.ceil(len(g[3])/2) for g in pair)*21+14
    positions.extend((g,j*372,y) for j,g in enumerate(pair));y+=h
  parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{y}" viewBox="0 0 {W} {y}"><rect width="{W}" height="{y}" fill="{bg}"/>']
  for (key,title,c,tools),x,y0 in positions:
   if not dark:c='#0969da'
   parts.append(f'<rect x="{x+2}" y="{y0+5}" width="3" height="13" rx="1" fill="{c}"/><text x="{x+14}" y="{y0+16}" fill="{fg}" font-family="Arial,sans-serif" font-size="14" font-weight="600">{escape(title)}</text>')
   parts.append(f'<path d="M{x+2} {y0+23}H{x+groupW-10}" stroke="{line}"/>')
   for i,tool in enumerate(tools):
    tx=x+4+(i%2)*(groupW/2);ty=y0+32+(i//2)*21
    name=logos.get(tool)
    if name:
     svg=ET.parse(ROOT/'assets/logos'/f'{name}.svg').getroot()
     paths=''.join(ET.tostring(ch,encoding='unicode') for ch in svg if ch.tag.endswith('path'))
     parts.append(f'<g transform="translate({tx} {ty}) scale(.58333)" fill="{c}">{paths}</g>')
    else:
     parts.append(f'<path d="M{tx+5} {ty+2}L{tx+1} {ty+7}L{tx+5} {ty+12}M{tx+9} {ty+2}L{tx+13} {ty+7}L{tx+9} {ty+12}" fill="none" stroke="{muted}" stroke-width="1.2"/>')
    parts.append(f'<text x="{tx+21}" y="{ty+11}" fill="{fg}" font-family="Arial,sans-serif" font-size="12">{escape(tool)}</text>')
  parts.append('</svg>');(ROOT/'assets'/f'toolkit-matrix{"-mobile" if mobile else ""}-{theme}.svg').write_text(''.join(parts))
print('Rendered all',sum(len(g[3]) for g in groups),'tools in eight aligned groups.')
