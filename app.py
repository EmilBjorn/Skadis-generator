"""
Streamlit app wrapper for svg_generator.py
"""

import streamlit as st
import svg_generator as sg

# Initialization
width = 200
height = 300
stepsize = 20
landscape = False
if 'numberinputwidth' not in st.session_state:
    st.session_state.numberinputwidth = width
if 'numberinputheight' not in st.session_state:
    st.session_state.numberinputheight = height
if 'sliderwidth' not in st.session_state:
    st.session_state.sliderwidth = width
if 'sliderheight' not in st.session_state:
    st.session_state.sliderheight = height

# Title
st.title('IKEA Skådis SVG Generator')


def sliderwidth():
    st.session_state.sliderwidth = st.session_state.numberinputwidth


def numberinputwidth():
    st.session_state.numberinputwidth = st.session_state.sliderwidth


def sliderheight():
    st.session_state.sliderheight = st.session_state.numberinputheight


def numberinputheight():
    st.session_state.numberinputheight = st.session_state.sliderheight


col1, col2 = st.columns([0.3, 0.7], gap='medium')
# Column 1
with col1:
    width = st.slider('Width',
                      min_value=40,
                      max_value=1000,
                      value=width,
                      step=stepsize,
                      format="%d mm",
                      key='sliderwidth',
                      on_change=numberinputwidth)
    width = st.number_input('Width',
                            min_value=40,
                            max_value=None,
                            value=width,
                            step=20,
                            key="numberinputwidth",
                            on_change=sliderwidth,
                            label_visibility='collapsed')
    height = st.slider('Height',
                       min_value=40,
                       max_value=1000,
                       value=height,
                       step=stepsize,
                       format="%d mm",
                       key='sliderheight',
                       on_change=numberinputheight)
    height = st.number_input('Height',
                             min_value=40,
                             max_value=None,
                             value=height,
                             step=20,
                             label_visibility='collapsed',
                             key="numberinputheight",
                             on_change=sliderheight)
    landscape = st.toggle('Rotate file', False)
    canvas = sg.draw(width=st.session_state.numberinputwidth,
                     height=st.session_state.numberinputheight,
                     landscape=landscape,
                     trim=False)

    # Download Button
    st.download_button(
        label='Download SVG',
        data=str(canvas),
        file_name=
        f"IKEA_Skådis_{width}x{height}_{'Landscape' if landscape else 'Portrait'}.svg"
    )
# Column 2
with col2:
    st.image(str(canvas), use_column_width=True)
