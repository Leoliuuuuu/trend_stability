import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

# Load data
data = pd.read_csv('YS-DI-012_piperazine.csv')  # Replace with your actual file
time = data['time']
measurements = data['area']

smoothed = savgol_filter(measurements, window_length=(len(time)-1), polyorder=2)

residuals = []
rss = 0
rmse = 0

for i in range(len(smoothed)):
    residuals.append(smoothed[i] - measurements[i])
    rss += residuals[i] ** 2
mean = sum(residuals)/len(residuals)

for i in range(len(residuals)):
    rmse += (residuals[i]-mean)**2/len(residuals)
rmse = rmse**0.5
rmse = rmse *100
print(f"Residual Sum of Squares (RSS): {rss}")

print(f"Root Mean Square Error (RMSE): {rmse} %")

plt.figure(figsize=(10, 5))
plt.plot(time, measurements, label='Original', alpha=0.6)
plt.plot(time, smoothed, label='Smoothed', color='green')
plt.xlabel('Time (h)')
plt.ylabel('Measurement')
plt.title('Original vs Smoothed Reaction Trend')
plt.legend()
plt.show()