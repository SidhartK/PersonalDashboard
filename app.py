 # Importing required packages
import streamlit as st
import pandas as pd

import todo
import todo2


st.title('Personal Dashboard')

PAGES = {
    "To-Do List": todo,
    "Second To-Do List": todo2,
    }


st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]

page.app()