import streamlit as st
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as mp
import plotly.express as px
from PIL import Image
import plotly.gragh_objects as go

# Reading the data from Excel file
df = pd.read_excel("Adidas.xlsx")

# Set page configuration
st.set_page_config(layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    div.block-container {padding-top: 1rem;}
    .title-test {
        font-weight: bold;
        padding: 5px;
        border-radius: 6px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Define HTML title with custom styling
html_title = """
<center><h1 class="title-test">Adidas Interactive Sales Dashboard</h1></center>
"""

# Load and display the image
image_path = "Adidas-logo.jpg"  # Ensure this file is in the same directory as app.py or provide the full path

# Create two columns (summing to 1.0 for proper layout)
col1, col2 = st.columns([0.1, 0.9])  # Adjusted to sum to 1.0

with col1:
    st.markdown(html_title, unsafe_allow_html=True)

with col2:
    col3, col4, col5 = st.columns([0.1, 0.45, 0.45])

    with col3:
        box_date = datetime.datetime.now().strftime("%d %b %Y")
        st.write(f"**Last updated by:** [in {box_date}]")

with col4:
    fig = px.bar(df, x="Retailer", y="TotalSales", labels={"TotalSales": "Total Sales ($)"},
                 title="Total Sales by Retailer", hover_data=["TotalSales"],
                 template="gridon", height=500)
    st.plotly_chart(fig, use_container_width=True)

view1, dwn1, view2, dwn2 = st.columns([0.15, 0.20, 0.20, 0.26])

with view1:
    expander = st.expander("Retailer wise Sales")
    data = df[["Retailer", "TotalSales"]].groupby(by="Retailer")["TotalSales"].sum()
    expander.write(data)

