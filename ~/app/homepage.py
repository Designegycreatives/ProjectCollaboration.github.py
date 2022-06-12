import streamlit as st



st.header("Loan Prediction App ")
st.sidebar.markdown("💳 Home Page")

expander_1 = st.sidebar.expander("PLEASE READ BEFORE YOU BEGIN")
expander_1.markdown("""<b>This App</b> has been designed out of passion to 
make <b>business intelligence</b> simple, easy, and efficient for business owners
with <b>no business analysis experience</b>. """, unsafe_allow_html=True)
