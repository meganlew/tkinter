import numpy as np

def M0toMw(M0):
    return (np.log10(M0) - 9.05)/1.5;

def MwtoM0(Mw):
    return 10.0**(1.5*Mw+9.05)

def M0tofc(M0,dSig=3.0*1.0e6,kBrune=0.38,Vs=3000.0):
    return kBrune*Vs*np.power(((16.0/7.0)*dSig/M0),(1.0/3.0))

def MwtoRW(Mw,author='wellscoppersmith',faulttype='All'):
    return 10.0**(-1.01 + 0.32*Mw)

def MwtoRLD(Mw,author='wellscoppersmith',faulttype='All'):
    return 10.0**(-2.44 + 0.59*Mw)

def MwtoRA(Mw,author='wellscoppersmith',faulttype='All'):
    return 10.0**(-3.49 + 0.91*Mw)



