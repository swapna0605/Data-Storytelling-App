import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Netflix Data Storytelling",
    layout="wide"
)

st.title("📖 Netflix Data Storytelling App")

df = pd.read_csv("netflix.csv")

df.drop_duplicates(inplace=True)
df.fillna("Unknown", inplace=True)

# Introduction

st.header("🎬 Introduction")

st.write("""
Netflix is one of the largest streaming platforms in the world.

This project explores Netflix's Movies and TV Shows dataset
to uncover trends, patterns, and insights about content
distribution across countries, genres, and years.
""")

# Dataset Overview

st.header("📊 Dataset Overview")

st.write("Total Records:", df.shape[0])
st.write("Total Columns:", df.shape[1])

st.dataframe(df.head())

# EDA

st.header("🔍 Exploratory Data Analysis")

# Visualization 1

type_count = df["type"].value_counts()

fig1 = px.pie(
    names=type_count.index,
    values=type_count.values,
    title="Movies vs TV Shows Distribution"
)

st.plotly_chart(fig1, use_container_width=True)

st.subheader("💡 Insight 1")

st.write("""
Netflix contains significantly more Movies than TV Shows,
showing a stronger focus on movie content.
""")

# Visualization 2

country_count = (
    df[df["country"] != "Unknown"]["country"]
    .value_counts()
    .head(10)
)

fig2 = px.bar(
    x=country_count.index,
    y=country_count.values,
    title="Top 10 Content Producing Countries"
)

st.plotly_chart(fig2, use_container_width=True)

st.subheader("💡 Insight 2")

st.write("""
The United States dominates Netflix content production,
followed by India and the United Kingdom.
""")

# Visualization 3

df["date_added"] = pd.to_datetime(
    df["date_added"],
    errors="coerce"
)

df["year_added"] = df["date_added"].dt.year

year_count = df["year_added"].value_counts().sort_index()

fig3 = px.line(
    x=year_count.index,
    y=year_count.values,
    title="Content Added Over Years"
)

st.plotly_chart(fig3, use_container_width=True)

st.subheader("💡 Insight 3")

st.write("""
Netflix experienced rapid content growth after 2015,
indicating aggressive expansion of its content library.
""")

# Recommendations

st.header("📌 Recommendations")

st.write("""
1. Increase investment in international content.

2. Expand TV Show production.

3. Focus on popular genres.

4. Improve regional content diversity.
""")

# Conclusion

st.header("✅ Conclusion")

st.write("""
This analysis reveals that Netflix is highly movie-oriented,
with strong contributions from the United States and
significant growth in content additions over recent years.

The insights highlight opportunities for further
international expansion and content diversification.
""")