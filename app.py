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

st.set_page_config(layout="wide")

st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

image = Image.open('adidas-logo.jpg')

# Create two columns (summing to 1.0 for proper layout)
col1, col2 = st.columns([0.1, 0.9])  # Adjusted to sum to 1.0

with col1:
    st.image(image,width=100)

html_title = """
    <style>
    .title-test {
        font-weight: bold;
        padding: 5px;
        border-radius: 6px;
    }
    </style>

<center><h1 class="title-test">Adidas Interactive Sales Dashboard</h1></center>
"""

with col2:
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

