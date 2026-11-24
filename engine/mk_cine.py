"""Estilo CINE: escenas a sangre (cielo/noche/día/rojo/duelo), subtítulo arriba, overlays limpios.
segs: [(texto, [elementos], escena)]  escena: None(atardecer) | 'noche' | 'dia' | 'rojo' | 'duelo'"""
import json,sys;sys.path.insert(0,'engine')
from mk_guion import *
def mono(id,who,x=50,y=72,w=300,say=None,cara='serio',gesto='manos',**k):
    return M(id,who,x,y=y,w=w,say=say,cara=cara,gesto=gesto,flip=(who=='feijoo' and x>=50),bub='up',bw=600,bfs=40,**k)
def BIG(id,n,t='',color='',y=84,fs=None): return P(id,'big',y=y,w=1000,n=n,text=t,color=color,**({'fs':fs} if fs else {}))
def HEMI(id,parts,line=None,y=50): return P(id,'hemi',y=y,w=1060,parts=parts,line=line)
def EDI(id,y=58,w=860,luz=True): return P(id,'edificio',y=y,w=w,luz=luz)
def BARRAS(id,bars,t0,t1,lab='',y=50): return P(id,'barras',y=y,w=940,bars=bars,t0=t0,t1=t1,lab=lab)
def XM(id,y=55,w=420): return P(id,'xmark',y=y,w=w)
def MED(id,l1,l2=None,f=1,y=70): return P(id,'medida',y=y,w=960,l1=l1,l2=l2,f=f)
def SELLO(id,t,y=60): return ST(id,t,0,y=y,color='red',rot=-8)
import re
EMO={'vot':'🗳️','urna':'🗳️','euro':'💶','dinero':'💶','cobra':'💰','sueldo':'💰','congreso':'🏛️','escaño':'💺','encuesta':'📊','por ciento':'📊','mentira':'❌','mito':'❌','falso':'❌','silencio':'🤐','calla':'🤐','ia':'🤖','inteligencia':'🤖','tiktok':'📱','móvil':'📱','correo':'✉️','presidente':'👑','vivienda':'🏠','casa':'🏠','debate':'🎙️','canción':'🎵','barrera':'🚧','provincia':'📍','madrid':'📍','gobernar':'🏛️','mañana':'⏰','días':'⏳','partido':'🎯','nulo':'🚫','blanco':'⬜','papeleta':'📄','pacto':'🤝','pactar':'🤝','junta':'⚖️','ley':'⚖️'}
POS_T=[(15,25),(85,26)];POS_B=[(14,89),(86,88)]
def deco(t,sh,k):
    words=t.split();extra=[];used=set();n=0
    low=any(e.get('y',50)>76 for e in sh)
    POS=POS_T+([] if low else POS_B)
    for i,w in enumerate(words):
        lw=w.lower().strip('¿?¡!.,:;«»')
        num=re.match(r'^[\d.,]+(%|€)?$',lw) and any(c.isdigit() for c in lw)
        emo=next((v for kk,v in EMO.items() if lw.startswith(kk) or (' ' in kk and kk in t.lower() and lw==kk.split()[0])),None)
        if i<4 or n>=len(POS): continue
        if num and lw not in used:
            x,y=POS[n%len(POS)];txt=w.strip('¿?¡!.,:;«»')
            nx=' '.join(words[i+1:i+3]).lower()
            if nx.startswith('por ciento'): txt+=' %'
            elif i+1<len(words) and words[i+1].lower().startswith(('euro','millon','escañ','día','pag')): txt+=' '+words[i+1].strip('.,:;').upper()
            extra.append(P(f'k{k}_{n}','chip',x=x,y=y,w=360,at=i,**{'in':'left' if x<50 else 'right'},text=txt.upper(),c=['','w','b','r'][n%4],rot=[-6,5,-3,7][n%4]));used.add(lw);n+=1
        elif emo and emo not in used:
            x,y=POS[n%len(POS)]
            extra.append(P(f'k{k}_{n}','emo',x=x,y=y,w=160,at=i,text=emo,fs=110,**{'in':'left' if x<50 else 'right'}));used.add(emo);n+=1
    return sh+extra
def cine(id,segs,fecha,cta,cover_tit,cover_rojo,fuente,tags='',dias='siete',auto_fin=True,fin_show=None,fin_bg='duelo',fin_txt=None):
    out=[];prev=[]
    for k,sg in enumerate(segs):
        t,sh=sg[0],sg[1];bg=sg[2] if len(sg)>2 else None
        INS=['left','right','down','zoom','up','spin']
        for j,e in enumerate(sh):
            if j>0 and not e.get('at'): e['at']=min(3,max(len(t.split())-1,0))  # lo secundario entra cuando lo principal ya está en su sitio
            if 'in' in e: continue
            kd=e.get('kind');x,y=e.get('x',50),e.get('y',50)
            if e.get('type')=='mono': e['from']='left' if x<50 else 'right'
            elif y>=70: e['in']='down'
            elif y<=32: e['in']='up'
            elif x<40: e['in']='left'
            elif x>60: e['in']='right'
            else: e['in']=['zoom','left','right'][(k+j)%3]
        sh=deco(t,sh,k)
        o={"text":t,"show":sh,"hide":prev}
        if bg:o['bg']=bg
        out.append(o);prev=[e['id'] for e in sh]
    fin={"bg":fin_bg,"text":fin_txt if fin_txt else f"{cta} Síguenos: quedan {dias} días.","show":fin_show if fin_show is not None else [mono('sF','sanchez',28,66,330,cara='duda'),mono('fF','feijoo',72,66,330,cara='duda'),BIG('bF','¿TÚ QUÉ DICES?','',y=40)],"hide":prev}
    voz=' '.join(s[0] for s in segs)
    cap=f"""{cover_tit.replace('*','')} 👀

{voz}

👇 {cta}
⏳ Quedan {dias} días para el 29-N. Síguenos: cada día, la campaña explicada.

Fuente: {fuente}
#elecciones #29N #espana #politica {tags}"""
    if not auto_fin: out[-1]["bg"]="duelo"; out[-1]["show"]=fin["show"]
    build(id,'CAMPAÑA 29-N',f'Fuente: {fuente}',cap,{"serie":"29-N","titulo":cover_tit,"mini":{"rojo":cover_rojo},"cartel":True},["","",""],[{"clause":0,"segments":out}]+([{"clause":-1,"segments":[fin]}] if auto_fin else []))
    g=json.load(open(f'guiones/{id}.json'));g['fechaPub']=fecha;g['estilo']='cine'
    json.dump(g,open(f'guiones/{id}.json','w'),ensure_ascii=False,indent=1)
    return ' '.join(t.split('|')[-1] for sc in g['scenes'] for s in sc['segments'] for t in s['text'].split())
