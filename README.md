## How to Run

pip install -r requirements.txt
streamlit run obesity_dashboard.py

# 📊 Obesity Analysis Dashboard

## 📖 Overview

The **Obesity Dashboard** is an interactive web application designed to visualize and analyze data related to obesity levels, body mass index (BMI), and contributing lifestyle factors (such as diet, physical activity, and transportation).

This tool aims to provide actionable insights into health trends, helping users understand the correlation between daily habits and obesity classifications.

## ✨ Key Features

- **Interactive Visualizations**: Dynamic charts and graphs showing obesity distribution by age, gender, and region.
- **Factor Analysis**: deep-dive into how variables like *eating habits*, *physical activity frequency*, and *technology usage* impact weight categories.
- **Data Filtering**: Filter data by specific demographics or risk factors.
- **Responsive Design**: Optimized for viewing on both desktop and mobile devices.

## 🛠️ Tech Stack

This project is built using the following technologies:

- **Language**: Python
- **Data Processing**: Pandas / NumPy
- **Visualization**: Plotly / Matplotlib / Seaborn 

## 📂 Project Structure

```bash
obesity-dashboard/
├── data/                  # Dataset files
├── src/                   # Source code for the dashboard
│   ├── components/        # Reusable UI components
│   └── utils/             # Helper functions and data processing
├── app.py                 # Main application entry point
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
└── .gitignore             # Files to ignore in version control
