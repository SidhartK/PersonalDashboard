 # Importing required packages
import streamlit as st
from st_ant_tree import st_ant_tree
import pandas as pd

# import todo
# import todo2


st.title('Personal Dashboard')
st.subheader("A simple and elegant checkbox tree for Streamlit.")

tree_data = [
    {
    "value": "parent 1",
    "title": "Parent 1",
    "children": 
        [
            {"value": "child 1",
            "title": "Child 1"},
            {"value": "child 2",
            "title": "Child 2"},
        ]
    },
    {
    "value": "parent 2",
    "title": """<i> <b style="color:green">Parent 2</b> </i>""",
    }
]

return_select = st_ant_tree(tree_data, treeCheckable=False, multiple=False, treeLine=False)
print("\n\n\n\n", return_select)
# PAGES = {
#     "To-Do List": todo,
#     "Second To-Do List": todo2,
#     }


# st.sidebar.title('Navigation')
# selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# page = PAGES[selection]

# page.app()