"""Reels con estructura de historia: gancho -> giro -> escalada -> remate -> pregunta.
segs: [(texto_voz, [elementos])]; el último segmento (CTA) se añade solo."""
import json,sys;sys.path.insert(0,'engine')
from mk_guion import *
def mono(id,who,x=50,y=50,w=430,say=None,cara='serio',gesto='manos',**k):
    return M(id,who,x,y=y,w=w,say=say,cara=cara,gesto=gesto,flip=(who=='feijoo' and x>=50),bub='up',bw=640,bfs=44,**k)
def DUEL(id,t,f,s,sub='',**k): return P(id,'duelo',y=46,w=960,text=t,f=f,s=s,sub=sub,**k)
def TELE(id,t,fs=90,y=44,sub=None): e=P(id,'tele',y=y,w=760,text=t,fs=fs); e.update({'sub':sub} if sub else {}); return e
def DOC(id,kick,t,sello,y=45): return P(id,'doc',y=y,w=640,kicker=kick,text=t,sello=sello,st=0.9)
def FL(id,t,bg='ink',size=170): return P(id,'cifra',y=50,w=940,n=t,text='',bg=bg,fs=min(size,150))
def CF(id,n,t,bg='ink',fs=230,y=44): return P(id,'cifra',y=y,w=940,n=n,text=t,bg=bg,fs=fs)
def DUO(i,cs='serio',cf='serio',atr=True,y=52,w=320):
    return [mono(f's{i}','sanchez',27,y,w,cara=cs),mono(f'f{i}','feijoo',73,y,w,cara=cf)]+([ATRILES(text='19-N')] if atr else [])
def story(id,titulo,segs,fecha,cta,cover_rojo,fuente,tags='',dias='nueve',caption_extra=''):
    out=[];prev=[]
    for k,(t,sh) in enumerate(segs):
        if k==0: sh=[H(titulo)]+sh
        out.append({"text":t,"show":sh,"hide":prev});prev=[e['id'] for e in sh]
    fin={"text":f"{cta} Síguenos: quedan {dias} días.","show":[ST('fol','¿TÚ QUÉ DICES?',0,y=29,color='red')]+DUO(99,'duda','duda'),"hide":prev}
    voz=' '.join(s[0] for s in segs)
    cap=f"""{titulo.replace('*','')} 👀

{voz}

👇 {cta}
⏳ Quedan {dias} días para el 29-N. Síguenos: cada día, lo más fuerte de la campaña.
{caption_extra}
Fuente: {fuente}
#elecciones #29N #sanchez #feijoo #debate {tags}"""
    build(id,'CAMPAÑA 29-N',f'Fuente: {fuente}',cap,{"serie":"CARA A CARA","titulo":titulo,"mini":{"rojo":cover_rojo},"cartel":True},["EL GANCHO","EL GIRO","TU VOTO"],[{"clause":0,"segments":out},{"clause":-1,"segments":[fin]}])
    g=json.load(open(f'guiones/{id}.json'));g['fechaPub']=fecha
    json.dump(g,open(f'guiones/{id}.json','w'),ensure_ascii=False,indent=1)
    return ' '.join(t.split('|')[-1] for sc in g['scenes'] for s in sc['segments'] for t in s['text'].split())
