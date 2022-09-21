import streamlit as st


def show():
    with open('README.md') as fin:
        st.markdown(fin.read())
