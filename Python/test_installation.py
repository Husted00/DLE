import requests
import pandas as pd

# Parametre
år = 2025
måned_dag = "11-24"  # fx
prisklasse = "DK1"   # eller "DK2"

url = f"https://www.elprisenligenu.dk/api/v1/prices/{år}/{måned_dag}_{prisklasse}.json"
resp = requests.get(url)
resp.raise_for_status()
data = resp.json()

# Lav DataFrame
df = pd.DataFrame(data)

# Konverter tid til pæn datetime (hvis nødvendigt)
df['time_start'] = pd.to_datetime(df['time_start'])
df['time_end'] = pd.to_datetime(df['time_end'])

# Vælg kolonner
df2 = df[['time_start', 'time_end', 'DKK_per_kWh', 'EUR_per_kWh']]

# Gem til CSV
df2.to_csv("elspot.csv", index=False)



