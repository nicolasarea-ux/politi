"""Estilo CINE: escenas a sangre (cielo/noche/día/rojo/duelo), subtítulo arriba, overlays limpios.
segs: [(texto, [elementos], escena)]  escena: None(atardecer) | 'noche' | 'dia' | 'rojo' | 'duelo'"""
import json,sys;sys.path.insert(0,'engine')
from mk_guion import *
def mono(id,who,x=50,y=72,w=300,say=None,cara='serio',gesto='manos',**k):
    return M(id,who,x,y=y,w=w,say=say,cara=cara,gesto=gesto,flip=(who=='feijoo' and x>=50),bub='up',bw=600,bfs=40,**k)
def BIG(id,n,t='',color='',y=84): return P(id,'big',y=y,w=1000,n=n,text=t,color=color)
def HEMI(id,parts,line=None,y=50): return P(id,'hemi',y=y,w=1060,parts=parts,line=line)
def EDI(id,y=58,w=860,luz=True): return P(id,'edificio',y=y,w=w,luz=luz)
def XM(id,y=55,w=420): return P(id,'xmark',y=y,w=w)
def MED(id,l1,l2=None,f=1,y=70): return P(id,'medida',y=y,w=800,l1=l1,l2=l2,f=f)
def SELLO(id,t,y=60): return ST(id,t,0,y=y,color='red',rot=-8)
def cine(id,segs,fecha,cta,cover_tit,cover_rojo,fuente,tags='',dias='siete'):
    out=[];prev=[]
    for k,sg in enumerate(segs):
        t,sh=sg[0],sg[1];bg=sg[2] if len(sg)>2 else None
        o={"text":t,"show":sh,"hide":prev}
        if bg:o['bg']=bg
        out.append(o);prev=[e['id'] for e in sh]
    fin={"bg":"duelo","text":f"{cta} Síguenos: quedan {dias} días.","show":[mono('sF','sanchez',28,66,330,cara='duda'),mono('fF','feijoo',72,66,330,cara='duda'),BIG('bF','¿TÚ QUÉ DICES?','',y=40)],"hide":prev}
    voz=' '.join(s[0] for s in segs)
    cap=f"""{cover_tit.replace('*','')} 👀

{voz}

👇 {cta}
⏳ Quedan {dias} días para el 29-N. Síguenos: cada día, la campaña explicada.

Fuente: {fuente}
#elecciones #29N #espana #politica {tags}"""
    build(id,'CAMPAÑA 29-N',f'Fuente: {fuente}',cap,{"serie":"29-N","titulo":cover_tit,"mini":{"rojo":cover_rojo},"cartel":True},["","",""],[{"clause":0,"segments":out},{"clause":-1,"segments":[fin]}])
    g=json.load(open(f'guiones/{id}.json'));g['fechaPub']=fecha;g['estilo']='cine'
    json.dump(g,open(f'guiones/{id}.json','w'),ensure_ascii=False,indent=1)
    return ' '.join(t.split('|')[-1] for sc in g['scenes'] for s in sc['segments'] for t in s['text'].split())
