# Dependencies
import streamlit as st
import os

def stop():
    """
    Stop the Streamlit app and close the browser tab.
    """
    os.kill(os.getpid(), 9)

st.title("Hello, World!")
if st.button("Stop"):
    stop()

