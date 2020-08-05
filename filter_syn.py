import sys
import math 
import numpy as np
import matplotlib.pyplot as plt 

f0=0
bw=0
N=0
tz=[]
RL=0
Q=0
def inputs(f0,b,n,r,q):
    f0=f0
    bw=bw 
    N=n
    for i in range(N-2):
        t=input()
        tz.append(t) 
    RL=r 
    Q=q 
f1=f0-bw
f2=f0+bw 

def poly_form():
    xx=[]
    yy=-[]
    UN1=[1,-1/tz(0)]
    VN1=np.sqrt(1-1/tz(0)**2)
    UN=[]
    VN=[] 
    for k in range(1,N):
        P=[1,-1/tz(k)]
        UN_PT1=np.convolve(UN1,P)
        Q=[np.sqrt(1-1/tz(k)**2),0,-np.sqrt(1-1/tz(k)**2)]
        UN_PT2=np.convolve(VN1,Q)
        for m in range(len(UN_PT1)):
            UN.append(UN_PT1(m)+UN_PT2(m))
        VN_PT1=np.convolve(VN1,P)
        VN_PT2=[np.sqrt(1-1/tz(k)**2)*a for a in UN1]
        for m in range(len(VN_PT1)):
            VN.append(VN_PT1(m)+VN_PT2(m))
        UN1=UN 
        VN1=VN 

    Ui=UN 
