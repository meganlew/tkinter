import numpy as np


def Triangle(t,t0=0.0,w=1.0):
    tm1 = np.sin(np.pi*w*(t-t0))
    tm2 = np.sin(3.0*np.pi*w*(t-t0))/9.0
    tm3 = np.sin(5.0*np.pi*w*(t-t0))/25.0
    tm4 = np.sin(7.0*np.pi*w*(t-t0))/49.0
    if ((t>t0) & (t<t0+1.0/w)):
        ff = 16.0*w/np.pi**2*(tm1-tm2+tm3-tm4)
    else:
        ff = 0.0
    return ff;


def BruneSmoothed(t,t0=0.0,w=1.0):
    
    tau0 = 2.31
    wtt0 = w*(t-t0)
    if t<t0:
        ff = 0.0
    elif ((wtt0 >= 0.0) and (wtt0<tau0)):
        ff = 1 - np.exp(-wtt0)* (1.0 + wtt0 + 0.5*wtt0**2 
                - 1.5/tau0*wtt0**3 + 1.5/tau0**2*wtt0**4 -0.5/tau0**3*wtt0**5)
    elif (wtt0>=tau0):
        ff = 1.0 - np.exp(-wtt0)*(1.0+wtt0)

    return ff;

def Liu(t,t0=0.0,w=1.0):
    tt = t
    pi = np.pi
    tau = 2*pi/w
    tau1 = 0.13*tau
    tau2 = tau-tau1
    Cc = pi/(1.4*tau1*pi + 1.2*tau1 + 0.3*tau2*pi)
    tt0 = tt-t0
    if tt<t0:
        ff = 0.0
    elif ((tt>=t0) and (tt<=tau1+t0)):
        ff = Cc*(0.7*tt0 + 1.2/pi*tau1 - 1.2/pi*tau1*np.cos(pi*tt0/2.0/tau1)
                -0.7/pi*tau1*np.sin(pi*tt0/tau1))
    elif ((tt>tau1+t0) and (tt<=2*tau1+t0)):
        ff = Cc*(tt0-0.3*tau1+1.2/pi*tau1 - 0.7*tau1/pi*np.sin(pi*tt0/tau1)
                + 0.3/pi*tau2*np.sin(pi*(tt0-tau1)/tau2))
    elif ((tt>2*tau1+t0) and (tt<=tau+t0)):
        ff = Cc*(0.3*tt0+1.1*tau1+1.2/pi*tau1 + 0.3/pi*tau2*np.sin(pi*(tt0-tau1)/tau2))
    elif (tt>tau+t0):
        ff = 1.0
    return ff;

