import streamlit as st

st.title("Cricbuzz Analytics - Dashboard")
st.write("Cricbuzz Analytics - Get match Information")

#x = st.slider("Select a range of values", 0, 100, (25, 75))

##st.write(f"You selected range: {x[0]} to {x[1]}")
##st.write("Cricbuzz Analytics - Get match Information")
##x = st.slider("Select a range of values", 0, 100, (25, 75))
##st.write(f"You selected range: {x[0]} to {x[1]}") 

x = st.text_input("Enter your name", key="name")
st.write(f"Hello, {x}!")

print(f"Hello, {x}!")

enable = st.checkbox("Enable camera")
picture = st.camera_input("Take your picture", disabled=not enable)

if picture:
    st.image(picture)