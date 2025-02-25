import streamlit as st
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as mp

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
image_path = "adidas-logo.jpg"  # Ensure this file is in the same directory as app.py or provide the full path
try:
    st.image(image_path, width=100, caption="Adidas Logo")  # Display the image with a width of 100 pixels
except FileNotFoundError:
    st.error("Image file 'adidas-logo.jpg' not found. Please check the file path or upload the image.")

# Create two columns (summing to 1.0 for proper layout)
col1, col2 = st.columns([0.5, 0.5])  # Adjusted to sum to 1.0

with col1:
    st.markdown(html_title, unsafe_allow_html=True)

with col2:
    col3, col4, col5 = st.columns([0.1, 0.45, 0.45])

    with col3:
        box_date = datetime.datetime.now().strftime("%d %b %Y")
        st.write(f"**Last updated by:** [in {box_date}]")

# You can add more content (e.g., data analysis, charts) using df here
