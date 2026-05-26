import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Hollywood Movie Analytics",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Hollywood Movie Analytics Dashboard")

# ---------------------------
# Dataset
# ---------------------------
data = {
    "Movie": [
        "Inception", "Interstellar", "Titanic", "Avengers: Endgame",
        "Joker", "Avatar", "The Dark Knight", "Frozen",
        "Toy Story", "Gladiator"
    ],
    "Genre": [
        "Sci-Fi", "Sci-Fi", "Romance", "Action",
        "Drama", "Sci-Fi", "Action", "Animation",
        "Animation", "Action"
    ],
    "Rating": [8.8, 8.6, 7.8, 8.4, 8.5, 7.9, 9.0, 7.5, 8.3, 8.5],
    "Votes": [
        2000000, 1800000, 1100000, 2500000,
        1200000, 1300000, 2300000, 900000,
        1000000, 1400000
    ],
    "Year": [2010, 2014, 1997, 2019, 2019, 2009, 2008, 2013, 1995, 2000]
}

df = pd.DataFrame(data)

# ---------------------------
# Sidebar Filters
# ---------------------------
st.sidebar.header("Filters")

selected_genre = st.sidebar.multiselect(
    "Select Genre",
    df["Genre"].unique(),
    default=df["Genre"].unique()
)

filtered_df = df[df["Genre"].isin(selected_genre)]

# ---------------------------
# Dataset Display
# ---------------------------
st.subheader("📋 Dataset")
st.dataframe(filtered_df, use_container_width=True)

# ---------------------------
# KPIs
# ---------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Movies", len(filtered_df))
col2.metric("Average Rating", round(filtered_df["Rating"].mean(), 2))
col3.metric("Highest Rating", filtered_df["Rating"].max())

# ---------------------------
# Analysis
# ---------------------------
st.subheader("📊 Analysis")

with st.expander("Top Rated Movies"):
    st.dataframe(
        filtered_df.sort_values(
            by="Rating",
            ascending=False
        )
    )

with st.expander("Movies per Genre"):
    st.write(filtered_df["Genre"].value_counts())

with st.expander("Average Rating by Genre"):
    st.write(
        filtered_df.groupby("Genre")["Rating"].mean()
    )

with st.expander("Movies with Rating > 8"):
    st.dataframe(filtered_df[filtered_df["Rating"] > 8])

# ---------------------------
# Dashboard
# ---------------------------
fig = make_subplots(
    rows=2,
    cols=2,
    specs=[
        [{"type": "xy"}, {"type": "domain"}],
        [{"type": "xy"}, {"type": "xy"}]
    ],
    subplot_titles=(
        "Movie Ratings",
        "Genre Distribution",
        "Votes vs Rating",
        "Correlation Heatmap"
    )
)

# Bar Chart
fig.add_trace(
    go.Bar(
        x=filtered_df["Movie"],
        y=filtered_df["Rating"],
        name="Ratings"
    ),
    row=1,
    col=1
)

# Pie Chart
genre_counts = filtered_df["Genre"].value_counts()

fig.add_trace(
    go.Pie(
        labels=genre_counts.index,
        values=genre_counts.values
    ),
    row=1,
    col=2
)

# Scatter Plot
fig.add_trace(
    go.Scatter(
        x=filtered_df["Votes"],
        y=filtered_df["Rating"],
        mode="markers+text",
        text=filtered_df["Movie"],
        textposition="top center"
    ),
    row=2,
    col=1
)

# Heatmap
corr = filtered_df[["Rating", "Votes", "Year"]].corr()

fig.add_trace(
    go.Heatmap(
        z=corr.values,
        x=corr.columns,
        y=corr.columns
    ),
    row=2,
    col=2
)

fig.update_layout(
    height=800,
    title="🎬 Hollywood Movie Analytics Dashboard",
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------
# Highest Voted Movie
# ---------------------------
st.subheader("🏆 Highest Voted Movie")

highest_voted = filtered_df.loc[
    filtered_df["Votes"].idxmax()
]

st.write(highest_voted)