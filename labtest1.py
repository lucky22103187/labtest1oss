import scipy as sp
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt



traffic_data = np.arange(0,1440)
arr = np.random.randint(60 , 120 , size = (len(traffic_data)))
random_noise = np.random.randint(len(traffic_data)*20)

traffic_data = traffic_data + random_noise

print(traffic_data[:10])
b, a = signal.butter(6,0.05, btype = 'low')
smooth_noise = signal.filtfilt(b, a, traffic_data)

print(smooth_noise[:10])



for i in traffic_data:
    avg_vech = np.arange(np.mean(i))

print(avg_vech[:10])


time = 0
interval = 60

plt.figure(figsize = (10,10))
plt.plot(time ,traffic_data, label = "noisy data")

plt.scatter(time , avg_vech , label = "average data" , marker='.',markersize = 4)





