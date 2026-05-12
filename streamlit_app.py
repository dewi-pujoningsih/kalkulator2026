import streamlit as st

st.title("🎈 Kalkulator 2027")
st.header("Aplikasi Operasi Aritmatika", divider=True)
number1 = st.number_input("Masukkan angka 1")
number2 = st.number_input("Masukkan angka 2")
tambah,kurang,bagi,kali=st.columns(4)
if tambah.button("+"):
    st.subheader(f"{number1}+{number2}={number1+number2}")
elif kurang.button("-"):
   st.subheader(f"{number1}-{number2}={number1-number2}")
elif bagi.button(":"):
   st.subheader(f"{number1}/{number2}={number1/number2}")
elif kurang.button("x"):
   st.subheader(f"{number1}x{number2}={number1*number2}")
if st.button("reset"):
    st.rerun()
