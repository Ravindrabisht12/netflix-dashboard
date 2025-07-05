import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/netflix_titles.csv')

# --- Plot 1: Content Type Distribution ---
df['type'].value_counts().plot(kind='bar')
plt.title('Content Type Distribution')
plt.xlabel('X - Type')
plt.ylabel('Y - Count')
st.pyplot(plt.gcf())
plt.clf()

# --- Plot 2: Titles Added Per Year ---
df['release_year'].value_counts().sort_index().plot(kind='line')
plt.title('Titles by Release Year')
plt.xlabel('Year')
plt.ylabel('Count')
st.pyplot(plt.gcf())
plt.clf()

# --- Plot 3: Top 10 Countries ---
df['country'].dropna().str.split(', ').explode().value_counts().head(10).plot(kind='barh')
plt.title('Top 10 Countries by Number of Titles')
plt.xlabel('Count')
plt.ylabel('Country')
st.pyplot(plt.gcf())
plt.clf()

# --- Plot 4: Top 10 Genres ---
df['listed_in'].str.split(', ').explode().value_counts().head(10).plot(kind='bar')
plt.title('Top 10 Genres')
plt.xlabel('Genre')
plt.ylabel('Count')
st.pyplot(plt.gcf())
plt.clf()

# --- Plot 5: Rating Distribution ---
df['rating'].value_counts().plot(kind="bar")
plt.title("Rating")
plt.xlabel('Rating')
plt.ylabel('Count')
st.pyplot(plt.gcf())
plt.clf()

# --- Streamlit's Own Chart ---
st.subheader("Content Type Distribution (Streamlit Native Chart)")
st.bar_chart(df['type'].value_counts())
