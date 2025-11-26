# %% 1
import pandas as pd

data = pd.read_csv('elspot.csv')

data["område"] = "DK1"
print(data.head())


print("Gennemsnitspris:", data['DKK_per_kWh'].mean())
print("Mindste pris:", data['DKK_per_kWh'].min())
print("Højeste pris:", data['DKK_per_kWh'].max())

# %%

# %% høj pris
import pandas as pd

data = pd.read_csv('elspot.csv')
