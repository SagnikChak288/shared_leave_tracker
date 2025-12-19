import streamlit as st

def home():
    st.subheader("Select Date Interval")
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date")
        
        st.write("People on Leave:")
        # Placeholder for displaying people on leave
        st.write("Sagnik Chakraborty")
        st.write("Debango De")
        
        st.write("\n")
        st.markdown("<b>Total People on Leave:</b> 2", unsafe_allow_html=True)
        
    with col2:
        end_date = st.date_input("End Date")
        
        st.write("People working:")
        # Placeholder for displaying people working
        st.write("Kush Kumar")
        st.write("Manshi Sinha")
        
        st.write("\n")
        st.markdown("<b>Total People on Leave:</b> 2", unsafe_allow_html=True)
        
    