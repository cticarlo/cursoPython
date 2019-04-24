import serial
import matplotlib.pyplot as plt
import numpy as np
import sys

def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth


ser=serial.Serial('COM3',115200);
X = np.array([], dtype=float)
Y = np.array([], dtype=float)
devPins = raw_input("Number of Terminals of DUT : ")
ser.write('S')

for x in range(0,800):
	pt=ser.readline()
	pt=pt.split(",");
	Y=np.append(Y,pt[0])
	X=np.append(X,pt[1])
	sys.stdout.write("\r" + "Acquiring Data : " + str((x+1)*100/800) + "%")
	sys.stdout.flush()

ser.close()

X = np.array(X,dtype=float)*5.7*2.5/1023
Y = np.array(Y,dtype=float)*2.5*1000/10230

V0 = X[0:99]
I0 = Y[0:99]
V1 = X[100:199]
I1 = Y[100:199]
V2 = X[200:299]
I2 = Y[200:299]
V3 = X[300:399]
I3 = Y[300:399]
V4 = X[400:499]
I4 = Y[400:499]
V5 = X[500:599]
I5 = Y[500:599]
V6 = X[600:699]
I6 = Y[600:699]
V7 = X[700:799]
I7 = Y[700:799]

#print X;
#print Y;

plt.plot(V0[4:84],smooth(I0,16)[4:84])
if(int(devPins) == 3):
	plt.plot(V1[4:84],smooth(I1,16)[4:84])
	plt.plot(V2[4:84],smooth(I2,16)[4:84])
	plt.plot(V3[4:84],smooth(I3,16)[4:84])
	plt.plot(V4[4:84],smooth(I4,16)[4:84])
	plt.plot(V5[4:84],smooth(I5,16)[4:84])
	plt.plot(V6[4:84],smooth(I6,16)[4:84])
	plt.plot(V7[4:84],smooth(I7,16)[4:84])

plt.grid()
plt.title('Device Characteristics')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (mA)')
plt.show()
print "\n\nDone !\n"