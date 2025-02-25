import streamlit as st
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as mp

# reading the data from excel file
df = pd.read_excel("Adidas.xlsx")
st.set_page_config(page_title="Adidas Dashboard", page_icon=":bar_chart:", layout="wide")
st.markdown('<style>div.block-container{padding-top:1rem;}<style>', unsafe_allow_html=True)
image_path = "adidas-logo.jpg"  # Ensure this file is in the same directory as your app.py or provide the full path
st.image(image_path, width=100)  # Display the image with a width of 100 pixels

col1, col2 = st.columns([0.8, 0.9])
with col1:
  
  <html title="">

    <style>
    .title-test {
        font-weight: bold;
        padding: 5px;
        border-radius: 6px;
    }
</style>

<center><h1 class="title-test">Adidas Interactive Sales Dashboard</h1></center>
  
with col2:
    st.markdown(html_title, unsafe_allow_html=True)

col3, col4, col5 = st.columns([0.1, 0.45, 0.45])

with col3:
    box_date = str(datetime.datetime.now().strftime("%d %b %Y"))
    st.write(f"Last updated by: [in {box_date}]")
