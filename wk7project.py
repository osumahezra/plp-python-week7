import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv(r"PYTHON CLASS\plp-python-week7\owid-covid-data.csv")
df = pd.DataFrame(df)
print(df.info())
print(df.isnull().sum())
dfAf = df[df['location'].isin(['Nigeria', 'Kenya', 'Uganda', 'Tanzania', 'South Africa'])]
print(dfAf.head())
print(dfAf.info())
dfAf = dfAf.dropna(axis=1, thresh=6300)
dfAf = dfAf.dropna()
dfAf['date'] = pd.to_datetime(dfAf['date'])

print(dfAf.shape)
print(dfAf.head(10))
print(dfAf.info())


plt.figure(figsize=(10, 5))
sns.lineplot(x='date', y='total_cases', data=dfAf[dfAf['location'] == 'Nigeria'], label='Nigeria')
plt.title('Time Series Data of Total Cases')
plt.xlabel('Date')
plt.ylabel('Total Case')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
sns.lineplot(x='date', y='total_cases', data=dfAf[dfAf['location'] == 'Kenya'], label='Kenya')
plt.title('Time Series Data of Total Cases')
plt.xlabel('Date')
plt.ylabel('Total Case')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
sns.lineplot(x='date', y='total_deaths', data=dfAf)
plt.title('Time Series Data of Total Deaths')
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
sns.lineplot(x='date', y='new_cases', data=dfAf, hue='location')
plt.title('Time Series Data of New Cases')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.grid(True)
plt.tight_layout()
plt.show()

dfAf['death_rate'] = dfAf['total_deaths'] / dfAf['total_cases']
print(dfAf.info())

(dfAf.groupby('location')['total_cases'].mean()).plot(x='location', y='total_cases', kind='bar', legend=False, color='salmon')
plt.title('Bar chat of Total Cases')
plt.ylabel('Total Cases(mean)')
plt.tight_layout()
plt.show()


