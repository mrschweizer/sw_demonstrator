import serial
import time
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from matplotlib.colors import LogNorm
import numpy as np
import time
from scipy.signal import spectrogram
from scipy.signal import resample
from scipy.interpolate import interp1d

arduino = serial.Serial(port='COM7', baudrate=57600, timeout=.1)
print('start')
time.sleep(2)
mag = np.empty(5000, dtype=int)
t = np.empty(mag.shape)

timepoint = 0
t0 = time.time()
print(t0)
for i ,(m, tau) in enumerate(zip(mag, t)):
    try:
        dat = int(arduino.readline())
        # if i == 0:
        #    y0 = dat
        mag[i] = dat
        t[i] = time.time() - t0
        print(dat)
    except ValueError:
        dat = None
        print('Fail')
print('Fertig')
mag = mag - mag[0]
arduino.close()
#print(mag)
fig, (line_ax) = plt.subplots()
#line_ax.set_ylim(-50, 50)
line_ax.set_ylabel('Field')
line_ax.set_xlabel('time')
plt.plot(t, mag)
plt.show()