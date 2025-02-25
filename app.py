import streamlit as st
import pandas as pd
import datetime
import numpy as np
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go

# reading the data from excel file
df = pd.read_excel("Adidas.xlsx")
st.set_page_config(page_title="Adidas Dashboard", page_icon=":bar_chart:", layout="wide")
st.title("Adidas Dashboard")
st.markdown('<style>div.block-container{padding-top:1rem;}<style>', unsafe_allow_html=True)
image = image.open('adidas-logo.jpg')

