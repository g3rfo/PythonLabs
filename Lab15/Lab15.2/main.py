import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

df = pd.read_csv(
    '2011.csv',
    sep=',',
    encoding='latin1',
    parse_dates=['Date'],
    dayfirst=True,
    index_col='Date'
)

# Дані для кожного велосипедиста окремо
df['Month'] = df.index.month
monthly_popularity = df.groupby('Month').sum()
most_popular_month = monthly_popularity.idxmax()
print(f"Популярність для кожного велосипедиста окремо: \n{most_popular_month}")

# Дані для всіх велосипедистів разом
monthly_popularity['Total'] = monthly_popularity.sum(axis=1)
most_popular_month_total = monthly_popularity['Total'].idxmax()
print(f"\nПопулярність для всіх велосипедистів разом: {most_popular_month_total}")

plot = df.drop(columns=['Month']).plot(figsize=(15, 10))
plt.show()