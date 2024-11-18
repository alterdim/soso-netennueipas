import streamlit as st
import requests

def get_cat_fact():
    url = "https://catfact.ninja/fact"
    return requests.get(url).json()["fact"]

st.title("🎈 My new app")
st.write(
    "Soline ne doit pas s'ennuyer !!! Non non non !!"
)

if st.button('Dis moi quelque chose que je ne sais pas'):
   st.write(get_cat_fact())
