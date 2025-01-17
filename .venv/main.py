import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

# Load data
data = pd.read_csv('shimdazu_piperazine.csv')  # Replace with your actual file
time = data['time']
measurements = data['area']

smoothed = savgol_filter(measurements, window_length=5, polyorder=2)

plt.figure(figsize=(10, 5))
plt.plot(time, measurements, label='Original', alpha=0.6)
plt.plot(time, smoothed, label='Smoothed', color='green')
plt.xlabel('Time (min)')
plt.ylabel('Measurement')
plt.title('Original vs Smoothed Reaction Trend')
plt.legend()
plt.show()