========================
# Part 1: Data Loading and Basic Exploration
# ========================
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st

# Load dataset
df = pd.read_csv("metadata.csv")

# Examine structure
print("First 5 rows:")
print(df.head())
print("\nDataFrame shape (rows, cols):", df.shape)
print("\nData types:")
print(df.dtypes)
print("\nMissing values per column:")
print(df.isnull().sum())
print("\nBasic stats for numeric columns:")
print(df.describe())

# ========================
# Part 2: Data Cleaning and Preparation
# ========================

# Handle missing values: drop rows without title or publish_time
df = df.dropna(subset=["title", "publish_time"])

# Convert date column to datetime
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")

# Extract year
df["year"] = df["publish_time"].dt.year

# Create new column: abstract word count
df["abstract_word_count"] = df["abstract"].fillna("").apply(lambda x: len(x.split()))

# ========================
# Part 3: Data Analysis and Visualization
# ========================

# Publications per year
year_counts = df["year"].value_counts().sort_index()
plt.figure(figsize=(8,5))
plt.bar(year_counts.index, year_counts.values)
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Number of Papers")
plt.tight_layout()
plt.savefig("publications_by_year.png")
plt.close()

# Top journals
top_journals = df["journal"].value_counts().head(10)
plt.figure(figsize=(8,5))
top_journals.plot(kind="bar")
plt.title("Top Journals Publishing COVID-19 Research")
plt.xlabel("Journal")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("top_journals.png")
plt.close()

# Word frequency in titles (WordCloud)
titles = " ".join(df["title"].dropna().astype(str))
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(titles)
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.tight_layout()
plt.savefig("title_wordcloud.png")
plt.close()

# ========================
# Part 4: Streamlit Application
# ========================
def run_streamlit():
    st.title("CORD-19 Data Explorer")
    st.write("Simple exploration of COVID-19 research papers")

    # Year filter
    min_year, max_year = int(df["year"].min()), int(df["year"].max())
    year_range = st.slider("Select year range", min_year, max_year, (2020, 2021))

    filtered = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

    # Show data sample
    st.write("Sample of filtered data:")
    st.dataframe(filtered[["title", "journal", "year"]].head(10))

    # Show plots
    st.subheader("Publications by Year")
    st.image("publications_by_year.png")

    st.subheader("Top Journals")
    st.image("top_journals.png")

    st.subheader("WordCloud of Titles")
    st.image("title_wordcloud.png")

# Uncomment below to run Streamlit app directly
# run_streamlit()

# ========================
# Part 5: Documentation and Reflection
# ========================

Reflection:
- Learned how to load, clean, and explore large datasets.
- Practiced handling missing data and date conversions.
- Created basic plots and a wordcloud.
- Built an interactive Streamlit app for exploration.
Challenges:
- Handling missing values without losing too much data.
- Working with large dataset sizes in memory.
