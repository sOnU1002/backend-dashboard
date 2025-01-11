import streamlit as st
import pandas as pd
import os

# Load data
data_path = './Electric_Vehicle_Population_Data.csv'

# Verify file existence
if not os.path.exists(data_path):
    raise FileNotFoundError(f"File not found: {data_path}. Please ensure the file is in the correct directory.")

# Load data
df = pd.read_csv(data_path)

# Custom CSS to style the app
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f6f9;
            color: #2c3e50;
            margin: 0;
            padding: 0;
        }
        .title {
            font-size: 4em;
            color: #2980b9;
            font-weight: bold;
            text-align: center;
            margin-top: 40px;
            margin-bottom: 40px;
        }
        .header {
            color: #34495e;
            font-size: 2.2em;
            margin-top: 40px;
            margin-bottom: 20px;
            text-align: left;
            font-weight: bold;
        }
        .metric-container {
            display: flex;
            justify-content: space-around;
            margin-top: 40px;
            margin-bottom: 40px;
            flex-wrap: wrap;
        }
        .metric {
            background-color: #ffffff;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
            width: 28%;
            text-align: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            margin-bottom: 30px;
        }
        .metric:hover {
            transform: translateY(-8px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
        }
        .metric h3 {
            font-size: 1.8em;
            color: #2980b9;
            margin-bottom: 15px;
        }
        .metric p {
            font-size: 1.6em;
            color: #34495e;
        }
        .chart {
            margin-top: 40px;
            background-color: #ffffff;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
            margin-bottom: 40px;
        }
        .chart h3 {
            font-size: 1.8em;
            color: #2980b9;
            margin-bottom: 20px;
        }
        .chart-container {
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
            margin-top: 20px;
        }
        .st-bar-chart .stChart {
            background-color: #f4f6f9;
            border-radius: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit UI setup
st.markdown('<div class="title">Electric Vehicle Population Data</div>', unsafe_allow_html=True)

# Metrics Section
st.markdown('<div class="header">Metrics</div>', unsafe_allow_html=True)
total_evs = len(df)
avg_range = df['Electric Range'].mean()
avg_msrp = df['Base MSRP'].mean()

# Display metrics in a professional layout with hover effect
st.markdown('<div class="metric-container">', unsafe_allow_html=True)

st.markdown(f"""
    <div class="metric">
        <h3>Total Electric Vehicles</h3>
        <p>{total_evs}</p>
    </div>
""", unsafe_allow_html=True)

st.markdown(f"""
    <div class="metric">
        <h3>Average Electric Range</h3>
        <p>{round(avg_range, 2)} miles</p>
    </div>
""", unsafe_allow_html=True)

st.markdown(f"""
    <div class="metric">
        <h3>Average MSRP</h3>
        <p>${round(avg_msrp, 2):,}</p>
    </div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Locations & Distribution Section
st.markdown('<div class="header">Data Distribution</div>', unsafe_allow_html=True)

# Yearly Data
yearly_data = df.groupby('Model Year').size().to_dict()
st.markdown('<div class="chart">', unsafe_allow_html=True)
st.subheader("Number of EVs by Model Year")
st.bar_chart(yearly_data)
st.markdown('</div>', unsafe_allow_html=True)

# EV Type Distribution
type_distribution = df['Electric Vehicle Type'].value_counts().to_dict()
st.markdown('<div class="chart">', unsafe_allow_html=True)
st.subheader("EV Type Distribution")
st.bar_chart(type_distribution)
st.markdown('</div>', unsafe_allow_html=True)

# Price vs Range
price_vs_range = df[['Base MSRP', 'Electric Range']].dropna()
st.markdown('<div class="chart">', unsafe_allow_html=True)
st.subheader("Price vs Electric Range")
st.line_chart(price_vs_range.set_index('Electric Range')['Base MSRP'])
st.markdown('</div>', unsafe_allow_html=True)
