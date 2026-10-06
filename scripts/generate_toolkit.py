"""Regenerate toolkit badges from verified profile and portfolio evidence."""
from pathlib import Path
from html import escape
import json
import xml.etree.ElementTree as ET
root=Path(__file__).resolve().parents[1]
groups=[('languages','Languages','#e3b341',['Python','JavaScript','TypeScript','C','C++','PHP','8086 Assembly']),('frontend','Frontend & motion','#58cde8',['HTML','CSS','React','Next.js','Redux Toolkit','Tailwind CSS','Material UI','Three.js','Framer Motion','GSAP','React Router']),('backend','Backend & automation','#56d4a2',['Django','Django REST','FastAPI','Express','Celery','Selenium','REST APIs']),('data','Databases & services','#bc8cff',['PostgreSQL','MySQL','MongoDB','Redis','Firebase']),('cloud','Cloud & delivery','#79b8ff',['AWS','Azure','Google Cloud','Docker','GitHub Actions','Git']),('ai','AI & machine learning','#f18fc0',['PyTorch','TensorFlow','Reinforcement learning','LLM evaluation']),('integrations','Product integrations','#e3b341',['Microsoft Dynamics','Adobe authentication','EmailJS','SendGrid']),('dev','Testing & development','#f0a66c',['pytest','Vite','ESLint','Prettier','npm','Yarn','GitHub','GeoJSON'])]
def slug(t):return t.lower().replace('++','pp').replace(' ','-').replace('&','and')
def picture(name,label,w):return f'<picture><source media="(prefers-color-scheme: dark)" srcset="./assets/{name}-dark.svg" /><img src="./assets/{name}-light.svg" alt="{escape(label)}" width="{w}" /></picture>'
logo_map=json.loads((root/'scripts/tool_logos.json').read_text())
def icon_markup(tool,color):
 name=logo_map.get(tool)
 if name:
  svg=ET.parse(root/'assets/logos'/f'{name}.svg').getroot()
  paths=''.join(ET.tostring(child,encoding='unicode') for child in svg if child.tag.endswith('path'))
  return f'<g transform="translate(9 7) scale(.667)" fill="{color}">{paths}</g>'
 # Concepts and tools without a supplied brand asset use a neutral outline glyph.
 if tool in ['8086 Assembly','LLM evaluation','Reinforcement learning']:
  return f'<g fill="none" stroke="{color}" stroke-width="1.3"><rect x="10" y="8" width="13" height="13" rx="2"/><path d="M13 5V8M20 5V8M13 21V25M20 21V25M6 11H10M23 11H27M6 18H10M23 18H27"/></g>'
 return f'<g fill="none" stroke="{color}" stroke-width="1.4"><path d="M14 9L8 15L14 21M21 9L27 15L21 21M19 7L16 23"/></g>'
parts=[]
for key,title,c,tools in groups:
 parts.append('### '+title+'\n\n<p>')
 for tool in tools:
  w=max(62,round(len(tool)*6.7+43));name='tool-logo-'+slug(tool)
  for dark in [True,False]:
   bg='#161b22' if dark else '#f6f8fa';fg='#e6edf3' if dark else '#1f2328';border='#303d4c' if dark else '#d1d9e0'
   (root/'assets'/f'{name}-{"dark" if dark else "light"}.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="30"><rect x=".5" y=".5" width="{w-1}" height="29" rx="4" fill="{bg}" stroke="{border}"/><path d="M1 8V22" stroke="{c}" stroke-width="2"/>{icon_markup(tool,c)}<text x="33" y="19" fill="{fg}" font-size="12" font-family="Arial,sans-serif">{escape(tool)}</text></svg>')
  parts.append(picture(name,tool,w)+' ')
 parts.append('</p>\n')
