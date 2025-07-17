import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Obesity Data Analysis Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and intro
st.title("📊 Obesity Data Analysis Dashboard")
st.markdown("""
Welcome to the interactive dashboard analyzing factors influencing obesity.
Use the sidebar to filter the dataset and explore patterns related to physical activity, eating habits, technology use, and more.
""")

# Load data with cache
@st.cache_data
def load_data():
    return pd.read_csv("ObesityDataSet_raw_and_data_sinthetic.csv")

df = load_data()

# Sidebar filters
st.sidebar.header("🔍 Filter Options")

# Gender filter
gender_options = st.sidebar.multiselect(
    "Select Gender(s):",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

# Age filter
age_range = st.sidebar.slider(
    "Select Age Range:",
    min_value=int(df["Age"].min()),
    max_value=int(df["Age"].max()),
    value=(int(df["Age"].min()), int(df["Age"].max()))
)

# Filtered data
filtered_df = df[
    (df["Gender"].isin(gender_options)) &
    (df["Age"] >= age_range[0]) &
    (df["Age"] <= age_range[1])
]

# Tabs for layout
tab1, tab2, tab3 = st.tabs([
    "📈 Obesity Distribution",
    "🏃 Physical Activity",
    "🍔 Food & Tech Habits"
])

# --- Tab 1: Obesity Distribution ---
with tab1:
    st.subheader("Obesity Level by Gender")
    fig1, ax1 = plt.subplots()
    sns.countplot(data=filtered_df, x="NObeyesdad", hue="Gender", ax=ax1)
    ax1.set_title("Obesity Category Distribution by Gender")
    ax1.set_xlabel("Obesity Category")
    ax1.set_ylabel("Count")
    plt.xticks(rotation=45)
    st.pyplot(fig1)

    st.subheader("Age Distribution by Obesity Level")
    fig2, ax2 = plt.subplots()
    sns.boxplot(data=filtered_df, x="NObeyesdad", y="Age", ax=ax2)
    ax2.set_title("Age vs. Obesity Level")
    ax2.set_xlabel("Obesity Category")
    ax2.set_ylabel("Age")
    plt.xticks(rotation=45)
    st.pyplot(fig2)

# --- Tab 2: Physical Activity ---
with tab2:
    st.subheader("Physical Activity Distribution by Obesity Level")
    fig3, ax3 = plt.subplots()
    sns.boxplot(data=filtered_df, x="NObeyesdad", y="FAF", ax=ax3)
    ax3.set_title("FAF (Physical Activity Frequency) across Obesity Categories")
    ax3.set_xlabel("Obesity Category")
    ax3.set_ylabel("FAF - Frequency of Physical Activity")
    plt.xticks(rotation=45)
    st.pyplot(fig3)

    st.subheader("Alcohol Consumption (CALC) by Obesity")
    fig4, ax4 = plt.subplots()
    sns.countplot(data=filtered_df, x="CALC", hue="NObeyesdad", ax=ax4)
    ax4.set_title("Alcohol Consumption Frequency by Obesity Category")
    ax4.set_xlabel("CALC (Alcohol Consumption)")
    plt.xticks(rotation=45)
    st.pyplot(fig4)


# --- Tab 3: Food & Tech Habits ---
with tab3:
    st.subheader("High Caloric Food Consumption")
    fig5, ax5 = plt.subplots()
    sns.countplot(data=filtered_df, x="CAEC", hue="Gender", ax=ax5)
    ax5.set_title("Frequency of Eating High Caloric Food")
    ax5.set_xlabel("CAEC (Meal Frequency)")
    plt.xticks(rotation=45)
    st.pyplot(fig5)

    st.subheader("Technology Usage by Gender and Obesity")
    fig6, ax6 = plt.subplots()
    sns.violinplot(data=filtered_df, x="Gender", y="TUE", hue="NObeyesdad", ax=ax6)
    ax6.set_title("Technology Use (TUE) by Gender and Obesity Category")
    st.pyplot(fig6)


# Footer
st.markdown("---")
st.caption("Created for Summer 2025 Final Project — Streamlit Bonus")