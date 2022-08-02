import numpy as np
import SourceParameters as src
import SourceTimeFunctions as stf
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import integrate


def ellipseSource(Mw, \
				  visualize2D, \
				  visualize3D, \
				  writeFileAscii, \
				  writeFileSW4, \
				  vrup=3000.0):


	# should get these from GUI eventually
	strike = 0.0
	dip = 90.0
	rake = 180.0
	centroidX = 0.0
	centroidY = 0.0
	centroidZ = -10000.0
	aspectRatio = 2.0
	#vrup = 3000.0
	hypoX = 0.0
	hypoZ = -10000.0
	dx = 50


	M0 = src.MwtoM0(Mw)
	fc0 = src.M0tofc(M0)
	RA = src.MwtoRA(Mw)

	###calculate ellipse major (A) and minor (B) axes in km of slipping area of the fault
	###where ellipse area RA = pi*A*B, B=A*aspectRatio
	ellA = np.sqrt(aspectRatio * RA / np.pi)
	ellB = ellA / aspectRatio

	###convert to meters
	ellA = ellA * 1000.0
	ellB = ellB * 1000.0

	###define the extent of the domain
	extentStk = 2.0 * ellA
	extentDip = 2.0 * ellB

	###discretize fault surface
	xx = np.arange(-extentStk, extentStk, dx)
	zz = np.arange(-extentDip, extentDip, dx) + centroidZ
	nx = len(xx)
	nz = len(zz)
	XX, ZZ = np.meshgrid(xx, zz)

	xxx = np.reshape(XX, (nx * nz))
	zzz = np.reshape(ZZ, (nx * nz))
	nsp = len(zzz)

	###evaluate ellipse function, which == 1 on the ellipse, < 1 inside, >1 outside
	ellps = ((xxx - centroidX) / ellA) ** 2 + ((zzz - centroidZ) / ellB) ** 2
	slip0 = np.zeros(nsp)

	###smoothly taper the amount of fault slip from 1 to 0 around the edge of the ellipse
	tap1 = 1.25
	tap0 = 0.75
	slip0[np.where(ellps >= tap1)[0]] = 0.0
	slip0[np.where(ellps < tap0)[0]] = 1.0
	iwheretap = np.where((ellps <= tap1) & (ellps > tap0))[0]
	slip0[iwheretap] = 0.5 + 0.5 * np.cos(np.pi / (tap1 - tap0) * (ellps[iwheretap] + 0.25))

	###setup source time functions for each sub fault
	dSigMax = 3.0 * 1.0e6
	kBrune = 0.38
	Vs = 3000.0
	dSigFault = dSigMax * slip0
	dt = 0.005
	tt = np.arange(0, 10.0, dt)
	nt = len(tt)
	ff = np.fft.fftshift(np.fft.fftfreq(nt, d=dt))
	v1 = np.zeros(nt)

	###get source time function for equivalent point source
	# for kk in np.arange(nt):
	#    v1[kk] = stf.Triangle(tt[kk],w=src.M0tofc(M0))
	# v1 = np.gradient(M0*integrate.cumtrapz(v1,dx=dt),dt)
	# g1 = np.fft.fftshift(np.abs(np.fft.fft(v1)))

	###get rupture time
	rupdist = np.sqrt((xxx - hypoX) ** 2 + (zzz - hypoZ) ** 2)
	trup = rupdist / vrup

	###scale fault slip to seismic moment
	m0Fault = M0 * slip0 / np.sum(slip0)

	# vFault = np.zeros(nt)
	# for isp in np.arange(nsp):
	#    if slip0[isp] <= 0.0:
	#	continue
	#   vtmp = np.zeros(len(vFault))
	#   sffc = src.M0tofc(m0Fault[isp],dSig=dSigFault[isp])
	#   for kk in np.arange(nt):
	#	vtmp[kk] = stf.Triangle(tt[kk],t0=trup[isp],w=sffc)
	#    vtmp = np.gradient(m0Fault[isp]*integrate.cumtrapz(vtmp,dx=dt),dt)
	#    vFault[:-1] = vFault[:-1]+vtmp



	maxm0 = np.max(m0Fault)
	minm0 = np.min(m0Fault)
	maxtrup = np.max(trup)
	mintrup = np.min(trup)




	slip02d = np.reshape(slip0, (nz, nx))
	trup2d = np.reshape(trup, (nz, nx))
	rupdist2d = np.reshape(rupdist, (nz, nx))
	dSigFault2d = np.reshape(dSigFault, (nz, nx))
	m0Fault2d = np.reshape(m0Fault, (nz, nx))



	xx = xx/1000.0
	zz = zz/1000.0
	#plot 2d images
	if visualize2D == True:
		hh = plt.figure(1,figsize=(9,5))
		hh.tight_layout()
		ax00 = plt.subplot2grid((2,2),(0,0))
		ax01 = plt.subplot2grid((2,2),(0,1))
		ax10 = plt.subplot2grid((2,2),(1,0))
		#ax11 = plt.subplot2grid((2,2),(1,1))        
		im00 = ax00.imshow(m0Fault2d,origin='lower',extent=(xx[0],xx[-1],zz[0],zz[-1]),cmap='inferno')
		im01 = ax01.imshow(dSigFault2d,origin='lower',extent=(xx[0],xx[-1],zz[0],zz[-1]),cmap='Oranges')
		im10 = ax10.imshow(trup2d,origin='lower',extent=(xx[0],xx[-1],zz[0],zz[-1]),cmap='viridis')

		fontsize0=9
		ax00.set_xlabel('along strike distance (km)',fontsize=fontsize0)
		ax00.set_ylabel('dip distance (km)',fontsize=fontsize0)
		ax00.set_title('Seismic moment (M0)')
		hh.colorbar(im00,ax=ax00,label='N*m')

		ax01.set_xlabel('along strike distance (km)',fontsize=fontsize0)
		ax01.set_ylabel('dip distance (km)',fontsize=fontsize0)
		ax01.set_title('Stress drop')
		hh.colorbar(im01,ax=ax01,label='MPa')

		ax10.set_xlabel('along strike distance (km)',fontsize=fontsize0)
		ax10.set_ylabel('dip distance (km)',fontsize=fontsize0)
		ax10.set_title('Rupture time')
		hh.colorbar(im10,ax=ax10,label='seconds')
		plt.show()



	##plot 3d images
	if visualize3D == True:
		cmapinferno = plt.cm.inferno(np.arange(256))
		cmapGreys = plt.cm.Greys(np.arange(256))
		ax3d = plt.subplot2grid((1,1),(0,0),projection='3d')
		for ix in np.arange(0,nx,2):
			for iz in np.arange(0,nz,2):
				if slip02d[iz,ix]==0:
					continue
				icolorm0 = int(255*(m0Fault2d[iz,ix]-minm0)/(maxm0-minm0))
				icolorm0 = np.min((icolorm0,255))
				icolorm0 = np.max((icolorm0,0))
				ax3d.scatter(XX[iz,ix],0,ZZ[iz,ix],'o',color=cmapGreys[icolorm0,:])
		plt.show()



	##write file
	if writeFileAscii == True:
		saveFileName = 'subfaults.txt'
		datW = np.column_stack((xxx,zzz,m0Fault,trup))
		np.savetxt(saveFileName,datW)




	##write file in format for SW4 input
	if writeFileSW4 == True:
		f = open('subfaultsSW4.txt','w')
		for ix in np.arange(0,nx,2):
			for iz in np.arange(0,nz,2):
				if slip02d[iz,ix]==0:
					continue
				subfaultM0 = m0Fault2d[iz,ix]
				subfaultfc = src.M0tofc(subfaultM0,dSig=dSigFault2d[iz,ix])
				subfaultx = XX[iz,ix]
				subfaultz = ZZ[iz,ix]
				subfaulttrup = trup2d[iz,ix]
				string0 = 'source x=' + '{:.4f}'.format(subfaultx) + \
						  ' y=' + '{:.4f}'.format(0) + ' z=' + '{:.4f}'.format(subfaultz) + \
						  ' m0=' + '{:.4e}'.format(subfaultM0) + ' strike=' + '{:.2f}'.format(strike) + \
						  ' dip=' + '{:.2f}'.format(dip) + ' rake=' + '{:.2f}'.format(rake) + \
						  ' type=Triangle freq=' + '{:.4f}'.format(subfaultfc) + ' t0=' + '{:.4f}'.format(subfaulttrup)
				f.write(string0 + '\n')
		f.close()



ellipseSource(4.5,True,True,True,True)










