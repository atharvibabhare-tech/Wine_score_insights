import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

st.set_page_config(page_title="Wine Rating Dashboard", layout="wide")

st.title("🍷 Wine Rating Data Analysis Dashboard")
st.markdown("Explore wine rating distribution and premium insights.")

# Sidebar Options
st.sidebar.header("Data Source")

option = st.sidebar.radio(
    "Choose Dataset:",
    ("Use Sample Dataset", "Upload Your Own Dataset")
)

# Load Data
if option == "Use Sample Dataset":
    df = pd.read_csv("wine_dataset.csv")
    st.success("Using built-in sample dataset")

else:
    uploaded_file = st.sidebar.file_uploader("Upload CSV or Excel", type=["csv","xlsx"])
    
    if uploaded_file is not None:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        st.success("Uploaded dataset successfully")
    else:
        st.info("Please upload a dataset from sidebar to continue.")
        st.stop()

# Data Cleaning
df = df.fillna(0)

# Layout Columns
col1, col2 = st.columns(2)

# 📊 Total Wines
with col1:
    st.subheader("Total Wines by Type")
    totals = df.drop("points", axis=1).sum().sort_values(ascending=False)
    
    fig1, ax1 = plt.subplots()
    ax1.bar(totals.index, totals.values, color="#8E44AD")
    plt.xticks(rotation=45)
    st.pyplot(fig1)

# 📈 Rating Distribution
with col2:
    st.subheader("Wine Rating Distribution")
    
    fig2, ax2 = plt.subplots()
    for col in df.columns[1:]:
        ax2.plot(df["points"], df[col], marker='o', label=col)
    
    ax2.set_xlabel("Rating Points")
    ax2.set_ylabel("Number of Wines")
    ax2.legend()
    st.pyplot(fig2)

# 🔥 Premium Segment
st.subheader("Premium Wines (90+ Ratings)")

premium = df[df["points"] >= 90]
premium_totals = premium.drop("points", axis=1).sum().sort_values(ascending=False)

fig3, ax3 = plt.subplots()
ax3.bar(premium_totals.index, premium_totals.values, color="#5B2C6F")
plt.xticks(rotation=45)
st.pyplot(fig3)

# 📊 Heatmap
st.subheader("Wine Ratings Heatmap")

fig4, ax4 = plt.subplots(figsize=(10,6))
sb.heatmap(df.set_index("points"), cmap="Purples", ax=ax4)
st.pyplot(fig4)

st.markdown("---")
st.markdown("👩‍💻 Built with Streamlit | Data Analysis by Atharvi")
