import json,sys
def M(id,who,x,at=0,say=None,tf=None,cara='neutral',gesto=None,label=None,flip=False,w=270,y=47,bub='up',bw=420,bfs=34,**k):
    e={"id":id,"type":"mono","who":who,"x":x,"y":y,"w":w,"at":at,"habla":bool(say),"cara":cara}
    if say: e.update(say=say,tf=tf or [0.15,1],bub=bub,bw=bw,bfs=bfs)
    if gesto: e['gesto']=gesto
    if label: e['label']=label
    if flip: e.update(flip=True,mira='l')
    e.update(k);return e
def H(t,id='h1'): return {"id":id,"type":"headline","text":t,"x":50,"y":20,"w":920}
def C(id,t,at=0,y=20): return {"id":id,"type":"card","text":t,"x":50,"y":y,"w":920,"at":at}
def CAP(id,n,t,at=0): return {"id":id,"type":"cap","n":n,"text":t,"at":at}
def ST(id,t,at,y=22,color='red',rot=-5): return {"id":id,"type":"stamp","text":t,"color":color,"x":50,"y":y,"rot":rot,"at":at}
def P(id,kind,x=50,y=44,w=500,at=0,**k): e={"id":id,"type":"prop","kind":kind,"x":x,"y":y,"w":w,"at":at};e.update(k);return e
def MESA(): return P('mesa','mesa',y=60,w=900,text='THE WILD PROJECT')
def FIN(q,stamp,hide): return {"clause":-1,"segments":[{"text":q+" Comenta y síguenos.","show":[M('tu9','tu',50,y=44,w=290,cara='duda',gesto='manos'),ST('fol',stamp,1,y=62,color='ink',rot=-4)],"hide":hide}]}
def build(id,tag,src,caption,portada,labels,scenes):
    for sc in scenes:
        for sg in sc['segments']:
            if any(e['type']=='headline' for e in sg['show']):
                for e in sg['show']:
                    if e['type']=='mono' and e.get('say') and e.get('bub','up')=='up': e['bub']='l' if e['x']>55 else 'r'
    g={"id":id,"brand":"Politízate Hoy","formato":"minuto","tono":"normal","clauses":len(labels)-1,"clauseLabels":labels,
       "header":{"tag":tag,"source":src},"caption":caption,"portada":portada,"scenes":scenes}
    json.dump(g,open(f'/home/claude/politi/guiones/{id}.json','w'),ensure_ascii=False,indent=1)
    t=' '.join(s['text'] for sc in scenes for s in sc['segments']);print(id,len(t));print(t)
