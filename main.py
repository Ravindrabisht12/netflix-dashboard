import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/netflix_titles.csv')
df.head()

df.isnull().sum()

df['type'].value_counts().plot(kind='bar')
plt.title('Content Type Distribution')
plt.xlabel('X - Type')
plt.ylabel('Y - Count')
plt.show()

df['release_year'].value_counts().sort_index().plot(kind='line')
plt.title('Titles Added Per Year')
plt.xlabel('Year')
plt.ylabel('Count')
plt.show()

df['country'].dropna().str.split(', ').explode().value_counts().head(10).plot(kind='barh')
plt.title('Top 10 Countries by Number of Titles')
plt.xlabel('Count')
plt.ylabel('Country')
plt.show()

df['listed_in'].str.split(', ').explode().value_counts().head(10).plot(kind='bar')
plt.title('Top 10 Genres')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.show()

df['rating'].value_counts().plot(kind="bar")
plt.title("Rating")
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show()