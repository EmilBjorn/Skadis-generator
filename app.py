import streamlit as st
import svg_generator as sg

st.title('IKEA Skådis SVG Generator')

sg.WIDTH = st.slider('Width', 100, 1000, 300)
togglelabel = 'Landscape' if sg.LANDSCAPE else 'Portrait'
sg.LANDSCAPE = st.toggle(togglelabel, False)

canvas = sg.draw()

st.image(str(canvas))
