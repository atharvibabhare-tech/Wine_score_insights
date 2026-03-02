import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

st.title("🍷 Wine Rating Data Analysis Dashboard")

# Upload file
uploaded_file = st.file_uploader("Upload Wine Dataset (CSV or Excel)", type=["csv","xlsx"])

if uploaded_file is not None:
    
    # Read file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    
    # Fill missing values
    df = df.fillna(0)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # Total wines per type
    st.subheader("📊 Total Wines per Type")
    totals = df.drop("points", axis=1).sum()
    fig1, ax1 = plt.subplots()
    ax1.bar(totals.index, totals.values, color="purple")
    plt.xticks(rotation=45)
    st.pyplot(fig1)

    # Line chart
    st.subheader("📈 Wine Rating Distribution")
    fig2, ax2 = plt.subplots()
    for col in df.columns[1:]:
        ax2.plot(df["points"], df[col], marker='o', label=col)
    ax2.legend()
    ax2.set_xlabel("Rating Points")
    ax2.set_ylabel("Number of Wines")
    st.pyplot(fig2)

    # Premium segment
    st.subheader("🔥 Premium Wines (90+ Ratings)")
    premium = df[df["points"] >= 90]
    premium_totals = premium.drop("points", axis=1).sum()
    fig3, ax3 = plt.subplots()
    ax3.bar(premium_totals.index, premium_totals.values, color="darkred")
    plt.xticks(rotation=45)
    st.pyplot(fig3)

else:
    st.info("Please upload a wine dataset to begin analysis.")
