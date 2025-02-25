import streamlit as st
import pandas as pd
import datetime
import numpy as np
import matplotlib as mp

# reading the data from excel file
df = pd.read_excel("Adidas.xlsx")
st.set_page_config(page_title="Adidas Dashboard", page_icon=":bar_chart:", layout="wide")
st.title("Adidas Dashboard")
st.markdown('<style>div.block-container{padding-top:1rem;}<style>', unsafe_allow_html=True)
image = image.open('adidas-logo.jpg')

col1, col2 = st.columns([0.1,0.9])
with col1
      st.image(image, width = 100)
