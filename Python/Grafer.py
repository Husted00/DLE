# %% El pris
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('elspot.csv')

# Konverter tid til datetime
data['time_start'] = pd.to_datetime(data['time_start'])

x = data['time_start']
y = data['DKK_per_kWh']

plt.plot(x, y, color='r', marker='o')
plt.title('Elpris')
plt.xlabel('Tid')
plt.ylabel('Pris (DKK/kWh)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# %%

