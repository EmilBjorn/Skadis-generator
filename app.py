"""
Streamlit app wrapper for svg_generator.py
"""

import streamlit as st
import svg_generator as sg

# Initialization
landscape = False
width = 200
height = 300
stepsize = 20

# Title
st.title('IKEA Skådis SVG Generator')

col1, col2 = st.columns([0.3, 0.7], gap='medium')

# Column 1
# width = col1.slider('Width', 100, 1000, 300, step=stepsize, format="%d mm")
# height = col1.slider('Height', 100, 1000, 300, step=stepsize, format="%d mm")
landscape = col1.toggle('Landscape', False)

# Download Button

# Column 2
canvas = sg.draw(width, height, landscape=landscape, trim=False)
col2.image(str(canvas))
