import streamlit as st




st.header("Loan Prediction App ")
st.sidebar.markdown("💳 Home Page")

st.sidebar.image("image_1.png", use_column_width=True)

expander_1 = st.expander("PLEASE READ BEFORE YOU BEGIN")
expander_1.markdown("""<b>This App</b> Can Predict Which Customer Can 
<b>Repay Or Default On Their Loans</b>. """, unsafe_allow_html=True)
