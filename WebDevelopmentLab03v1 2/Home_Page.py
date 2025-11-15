import streamlit as st
import creativeApi

st.title("Web Development Lab03")

st.header("CS 1301")
st.subheader("Team 17, Web Development - Section E")
st.subheader("George Ejike, Chris Hernandez")

st.sidebar.title("Menu")
page = st.sidebar.radio(
    "Go to:",
    ["Home", "API Page", "Part 2"]
)

if page == "Home":
    st.write("""
    Welcome to our Streamlit Web Development Lab03 app! You can navigate between the pages using the sidebar to the left. 
    The following pages are:

    1. **API Page** – PokeAPI API & interactive graphs  
    2. **Part 2** – Additional content  
    """)

elif page == "API Page":
    creativeApi.dataStuff()

elif page == "Part 2":
    st.header("Part 2")
    st.write("Soon to be updated.")

else:
    None
