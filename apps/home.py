import streamlit as st



st.markdown("Loan Prediction App ")
st.sidebar.markdown(("💳 Home Page")


       
# Image For Page
file_ = open("image1.jpg", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
       f'<img src="data:image/gif;base64,{data_url}" alt="dashboard gif">',
       unsafe_allow_html=True
)
       
      
       
       
       
