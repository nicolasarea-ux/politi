import cv2,numpy as np,sys
def toon(src,dst,k=8):
    im=cv2.imread(src,cv2.IMREAD_UNCHANGED)
    if im.shape[2]==3: im=np.dstack([im,np.full(im.shape[:2],255,np.uint8)])
    rgb=im[:,:,:3].copy();a=im[:,:,3]
    h,w=a.shape;sc=600/max(h,w);rgb=cv2.resize(rgb,(int(w*sc),int(h*sc)),interpolation=cv2.INTER_AREA);a=cv2.resize(a,(int(w*sc),int(h*sc)))
    sm=rgb
    for _ in range(8): sm=cv2.bilateralFilter(sm,9,35,7)
    hsv=cv2.cvtColor(sm,cv2.COLOR_BGR2HSV).astype(np.float32);hsv[...,1]*=1.18;hsv[...,2]=np.clip(hsv[...,2]*1.08+8,0,255);sm=cv2.cvtColor(hsv.clip(0,255).astype(np.uint8),cv2.COLOR_HSV2BGR)
    Z=sm.reshape(-1,3).astype(np.float32);m=(a.reshape(-1)>128)
    crit=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,20,1.0)
    _,lab,cen=cv2.kmeans(Z[m],k,None,crit,3,cv2.KMEANS_PP_CENTERS)
    out=Z.copy();out[m]=cen[lab.flatten()];q=out.reshape(sm.shape).astype(np.uint8)
    q=cv2.medianBlur(q,5)
    g=cv2.cvtColor(sm,cv2.COLOR_BGR2GRAY);g=cv2.medianBlur(g,7)
    ed=cv2.adaptiveThreshold(g,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,13,6)
    ed=cv2.morphologyEx(ed,cv2.MORPH_OPEN,np.ones((2,2),np.uint8))
    ink=np.array([61,33,20],np.uint8)
    q[ed==0]=(q[ed==0]*0.35+ink*0.65).astype(np.uint8)
    # contorno grueso
    am=(a>128).astype(np.uint8)*255
    dil=cv2.dilate(am,np.ones((9,9),np.uint8))
    outl=(dil>0)&(am==0)
    res=np.dstack([q,am]);res[outl]=[61,33,20,255]
    cv2.imwrite(dst,res)
for n in sys.argv[2:]: toon(f'fotos/{n}_head.png',f'{sys.argv[1]}/{n}_toon.png')
