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

arduino = serial.Serial(port='COM5', baudrate=9600, timeout=.1)



fig, (line_ax, spec_ax) = plt.subplots(1, 2)
line, = line_ax.plot([0])

i_fft = 128
repeat = 64


line_ax.set_ylim(-50, 50)
line_ax.set_xlim(0, 10)
# spec_ax.set_xlim(0,10)
spec_ax.set_ylim(1, i_fft//2)
# ax.update({'autoscale_on': True})

xdata, ydata = [0], [0]

spect = np.zeros((i_fft, 32))
# spect[...] = np.NaN
spect_plot = spec_ax.imshow(spect, norm=LogNorm(16, 2000), aspect='auto')



def run(data):
    i = len(ydata)
    print(i)
    if i >= i_fft and (i % repeat) == 0:
        spect[:, i//repeat] = np.abs(np.fft.fft(ydata[i-i_fft: i], axis=0))
        spect_plot.set_data(spect)
    line.set_data(xdata, ydata)
    return line, spect_plot

def gen_data():
    timepoint = 0
    t0 = time.time()
    while timepoint <= 10:
        try:
            dat = int(arduino.readline())
            if timepoint == 0:
                y0 = dat
            timepoint = time.time() - t0
            xdata.append(timepoint)
            ydata.append(dat - y0)
        except ValueError:
            dat = None
        yield xdata, ydata



ani = anim.FuncAnimation(fig, run, gen_data, interval=0, blit=True, repeat=False)
print(ydata)
plt.show(block=True)




exit()
try:
    pass
    # ip = interp1d(tdata, ydata)
    # t_iterp = np.linspace(min(tdata), max(tdata), len(tdata))
    # y_interp = ip(t_iterp)
    # inter_line.set_data(t_iterp, y_interp)
except ValueError:
    pass