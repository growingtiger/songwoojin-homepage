#!/usr/bin/env python3
"""data/papers.json → public/index.html 의 PAPERS:LIST 블록을 다시 생성한다.
사용: python3 tools/build_papers.py
"""
import json, html, re, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
papers = json.load(open(ROOT/'data/papers.json', encoding='utf-8'))
JMAP = {'Korean J. Vet. Serv':'Korean J Vet Serv','Veterinary Sciences':'Vet Sci',
        'Journal of Feline Medicine and Surgery Open Reports':'JFMS Open Rep','Sci Rep':'Sci Rep'}
ME = ('Song WJ','Song W','Song W-J')
def esc(x): return html.escape(x, quote=False)
def authors(p):
    out=[]
    for a in p['authors']:
        a2 = 'Song WJ' if a in ME else a
        out.append(f'<strong>{esc(a2)}</strong>' if a in ME else esc(a2))
    return ', '.join(out)
def cite(p):
    j = JMAP.get(p['journal'], p['journal'])
    v = p.get('volume',''); i = p.get('issue',''); pg = p.get('pages','')
    s = f'<i>{esc(j)}</i> {p["year"]}'
    if v: s += f';{esc(v)}'
    if i: s += f'({esc(i)})'
    if pg: s += f':{esc(pg)}'
    return s
by = {}
for p in papers: by.setdefault(p['year'], []).append(p)
blocks=[]
for y in sorted(by, reverse=True):
    ps = by[y]
    nf = sum(1 for p in ps if p['role']=='first'); nl = sum(1 for p in ps if p['role']=='last')
    lead = []
    if nf: lead.append(f'제1저자 {nf}')
    if nl: lead.append(f'교신저자 {nl}')
    c = f'{len(ps)}편' + (f' · {" · ".join(lead)}' if lead else '')
    openattr = ' open' if y >= 2025 else ''
    items=[]
    for p in ps:
        cls = f' class="{p["role"]}"' if p['role'] in ('first','last') else ''
        items.append(
            f'        <li{cls}><b class="t"><a href="https://doi.org/{esc(p["doi"])}" target="_blank" rel="noopener">{esc(p["title"])}</a></b>'
            f'<span class="a">{authors(p)}</span><br><span class="j">{cite(p)} · <a href="https://doi.org/{esc(p["doi"])}" target="_blank" rel="noopener">doi:{esc(p["doi"])}</a></span></li>')
    blocks.append(f'    <details class="pubyr"{openattr}>\n      <summary><span class="y">{y}</span><span class="c">{c}</span><span class="o"></span></summary>\n      <ul class="pub">\n' + '\n'.join(items) + '\n      </ul>\n    </details>')
block = '\n'.join(blocks)
idx = ROOT/'public/index.html'
s = idx.read_text(encoding='utf-8')
s = re.sub(r'(<!-- PAPERS:LIST:START -->\n).*?(<!-- PAPERS:LIST:END -->)', lambda m: m.group(1)+block+'\n'+m.group(2), s, flags=re.S)
idx.write_text(s, encoding='utf-8')
print(f'{len(papers)} papers written into index.html')
