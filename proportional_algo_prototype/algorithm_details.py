import streamlit as st


def show():
    st.markdown(open('README.md').read())
