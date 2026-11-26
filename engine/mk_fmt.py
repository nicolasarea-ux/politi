"""Formatos copiados (f1 plató, f2 amarillo, f3 oscuro-ley, f4 ilustrado, f5 versus, f6 collage).
fmt(id, estilo, segs=[(texto, [elementos])], fecha, cover_tit, fuente, tags, cta_txt)
Elementos: dicts con k=por|big|stat|emo|tape|card|podios|hemi|vs|pill|pan|bars|mono, x,y en %, at=índice de palabra."""
import json
def E(k,**kw): kw['k']=k; kw.setdefault('at',0); return kw
def fmt(id,estilo,segs,fecha,cover_tit,fuente,tags='',portada=None):
    out=[{"text":t,"show":els,"hide":[]} for t,els in segs]
    voz=' '.join(s[0] for s in segs)
    cap=f"""{cover_tit} 👀

{voz}

Fuente: {fuente}
#elecciones #29N #espana #politica {tags}"""
    g={"id":id,"brand":"Politízate Hoy","formato":"minuto","tono":"normal","clauses":0,"clauseLabels":[""],"header":{"tag":"","source":fuente},
       "caption":cap,"portada":portada or {"estilo":"nueva","titulo":cover_tit},"scenes":[{"clause":0,"segments":out}],"fechaPub":fecha,"estilo":estilo}
    json.dump(g,open(f'/home/claude/politi/guiones/{id}.json','w'),ensure_ascii=False,indent=1)
    return voz
