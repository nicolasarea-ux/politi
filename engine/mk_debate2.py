"""Reels post-debate. items: lista de
  ("sanchez"|"feijoo", "cita literal", "texto narrador antes (opcional)")
  ("narr", "texto narrador", "SELLO opcional")
Primer segmento = gancho (hook) con titular."""
import json,sys;sys.path.insert(0,'engine')
from mk_guion import *
NOM={'sanchez':'Sánchez','feijoo':'Feijóo'}
def base(i,cs='serio',cf='serio'):
    return [M(f'sB{i}','sanchez',27,y=44,cara=cs,gesto='manos'),M(f'fB{i}','feijoo',73,y=44,cara=cf,gesto='manos',flip=True)]
def reel(id,titulo,hook,items,fecha,pregunta,cover_rojo,fuente,extra_cap='',tags='',cara_hook=('serio','serio')):
    segs=[{"text":hook,"show":[H(titulo)]+base(0,*cara_hook)+[ATRILES(text='19-N')],"hide":[]}]
    prev=['h1','sB0','fB0']
    for i,it in enumerate(items,1):
        w=it[0]
        if w=='narr':
            sh=base(i,'duda','duda')+([ST(f'st{i}',it[2],0,y=29,color='red')] if len(it)>2 and it[2] else [])
            segs.append({"text":it[1],"show":sh,"hide":prev});prev=[f'sB{i}',f'fB{i}']+([f'st{i}'] if len(it)>2 and it[2] else []);continue
        q=it[1];pre=(it[2]+' ') if len(it)>2 and it[2] else f'{NOM[w]}: '
        o='feijoo' if w=='sanchez' else 'sanchez'
        tk=M(f'{w[0]}{i}',w,27 if w=='sanchez' else 73,y=44,flip=(w=='feijoo'),say=f'«{q}»',bub='up',bw=520,bfs=38,cara='enfadado' if i%2==0 else 'serio',gesto='senala' if i%2==0 else 'manos')
        ot=M(f'{o[0]}{i}',o,27 if o=='sanchez' else 73,y=44,flip=(o=='feijoo'),cara='duda' if i%2 else 'serio',gesto='brazos' if i%2 else 'manos')
        segs.append({"text":pre+q+('' if q[-1] in '.?!…' else '.'),"show":[tk,ot],"hide":prev});prev=[f's{i}',f'f{i}']
    fin={"text":f"{pregunta} Comenta Sánchez o Feijóo. Quedan diez días: síguenos para no perderte nada.","show":[ST('fol','¿TÚ QUÉ DICES?',0,y=29,color='red')]+base(99,'duda','duda'),"hide":prev}
    def lin(it): return (f"🗣️ {NOM[it[0]]}: «{it[1]}»" if it[0]!='narr' else f"▶️ {it[1]}")
    cap=f"""{titulo.replace('*','')} 👀 #CaraACara

{hook}
"""+"\n".join(lin(it) for it in items)+f"""
{extra_cap}
👇 {pregunta} Comenta SÁNCHEZ o FEIJÓO.
⏳ Quedan 10 días para el 29-N. Síguenos: cada día, lo más fuerte de la campaña.

Fuente: {fuente}
#debate #caraacara #sanchez #feijoo #debateelectoral #elecciones #29N {tags}"""
    build(id,'CARA A CARA · 19-N',f'Fuente: {fuente}',cap,{"serie":"CARA A CARA","titulo":titulo,"mini":{"rojo":cover_rojo},"cartel":True},["EL MOMENTO","TU VOTO"],[{"clause":0,"segments":segs},{"clause":-1,"segments":[fin]}])
    g=json.load(open(f'guiones/{id}.json'));g['fechaPub']=fecha;g['trial']=True
    json.dump(g,open(f'guiones/{id}.json','w'),ensure_ascii=False,indent=1)
    return ' '.join(t.split('|')[-1] for sc in g['scenes'] for s in sc['segments'] for t in s['text'].split())
