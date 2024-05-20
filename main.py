import streamlit as st
import pandas as pd

name=st.text_input("enter your name:")
fname=st.text_input("enter your father name: ")
adr=st.text_area("enter the addrss: ")
classdata=st.selectbox("enter your class:",(1,2,3,4,5,6,7))
button=st.button("done")
if button:
    st.markdown(f"""
    name: {name}
    father name: {fname}
     address :{adr}
    class:{classdata}""")