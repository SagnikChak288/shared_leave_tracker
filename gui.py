import streamlit as st
from streamlit_option_menu import option_menu

from Section.home import home

def gui():
    # --------------SETTINGS--------------
    page_title = "Leave Tracker"
    page_icon = ":material/task_alt:"

    # --------------INITIALIZE--------------
    st.set_page_config(page_title=page_title, page_icon=page_icon, 
                    layout="wide", initial_sidebar_state="auto", menu_items=None)



    # ---------------UI------------------
    st.title(f"{page_icon} {page_title}")
    st.divider()
    
    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",
            options=["Home", "Add Leave", "Leave Status", "Admin"],
            icons=["house", "file-earmark-plus", "clipboard-check", "shield-lock"],
            menu_icon="cast",
            default_index=0,
        )
        
    if selected == "Home":
        home()

