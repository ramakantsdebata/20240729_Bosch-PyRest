import seaborn as sns
import matplotlib.pyplot as plt
import pickle

fileName = 'tips.pkl'

df = sns.load_dataset('tips')
print(df.head())
sns.scatterplot(data=df, x='total_bill', y='tip')
plt.show()

with open(fileName, "wb") as file:
    pickle.dump(df, file)

## Retrieve the data

with open(fileName, "rb") as file:
    df2 = pickle.load(file)

sns.scatterplot(data=df2, x='total_bill', y='tip')
plt.show()
