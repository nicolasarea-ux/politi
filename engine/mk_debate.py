"""Reels del cara a cara en directo. Uso:
python3 engine/mk_debate.py <id> '<BLOQUE>' '<json lineas [[who,"cita"],...]>' [fecha ISO] [pregunta]
who: sanchez|feijoo. Las citas, LITERALES (de directos de prensa), sin comillas."""
import json,sys;sys.path.insert(0,'engine')
from mk_guion import *
NOM={'sanchez':'Sánchez','feijoo':'Feijóo'}
def reel(id,bloque,lineas,fecha=None,pregunta='¿Quién gana este asalto?'):
    base=lambda cs,cf:[M('sA','sanchez',27,y=44,cara=cs,gesto='manos'),M('fA','feijoo',73,y=44,cara=cf,gesto='manos',flip=True)]
    segs=[{"text":f"Cara a cara, en directo. Bloque: {bloque.lower()}.","show":[H(f'*{bloque}*')]+base('serio','serio')+[ATRILES(text='EN DIRECTO')],"hide":[]}]
    prev=['h1']
    for i,(w,q) in enumerate(lineas):
        o='feijoo' if w=='sanchez' else 'sanchez'
        def mm(who,talk):
            x=27 if who=='sanchez' else 73
            k=dict(say=f'«{q}»',bub='up',bw=520,bfs=38,cara='enfadado' if i%2 else 'serio',gesto='senala' if i%2 else 'manos') if talk else dict(cara='duda' if i%2 else 'serio',gesto='brazos' if i%2 else 'manos')
            return M(f'{who[0]}{i}',who,x,y=44,flip=(who=='feijoo'),**k)
        segs.append({"text":f"{NOM[w]}: {q}","show":[mm(w,True),mm(o,False)],"hide":prev+(['sA','fA'] if i==0 else [])})
        prev=[f's{i}',f'f{i}']
    segs.append({"text":f"{pregunta} Comenta Sánchez o Feijóo. Mañana contamos los votos.","show":[ST('fol','¿QUIÉN GANA?',0,y=29,color='red')]+base('duda','duda'),"hide":prev})
    cap=f"""🔴 CARA A CARA EN DIRECTO · {bloque}

"""+"\n".join(f"{NOM[w]}: «{q}»" for w,q in lineas)+f"""

👇 {pregunta} Comenta SÁNCHEZ o FEIJÓO. Mañana contamos los votos.

Frases literales del debate de esta noche (Academia de TV, 19-N).
#debate #caraacara #sanchez #feijoo #debateelectoral #29N"""
    build(id,'CARA A CARA · DIRECTO','Debate Academia de TV, 19-N',cap,{"serie":"🔴 EN DIRECTO","titulo":f"*{bloque}*","mini":{"rojo":"¿SÁNCHEZ O FEIJÓO?"},"cartel":True},["DIRECTO","TU VOTO"],[{"clause":0,"segments":segs[:-1]},{"clause":-1,"segments":segs[-1:]}])
    g=json.load(open(f'guiones/{id}.json'));g['trial']=True
    if fecha:g['fechaPub']=fecha
    json.dump(g,open(f'guiones/{id}.json','w'),ensure_ascii=False,indent=1)
    print(' '.join(t.split('|')[-1] for sc in g['scenes'] for s in sc['segments'] for t in s['text'].split()))
if __name__=='__main__':
    a=sys.argv; reel(a[1],a[2],json.loads(a[3]),a[4] if len(a)>4 else None,a[5] if len(a)>5 else '¿Quién gana este asalto?')
