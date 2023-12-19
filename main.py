import streamlit as st
from PIL import Image
import sklearn

img = Image.open ('assets/photo.jpg')
new_size = img.resize ((250,250))
st.sidebar.image(new_size)


st.title("Portofolio")
st.header("Perkenalan", divider='rainbow')
st.text("""Mahasiswa S1 Teknologi Informasi di Institut Teknologi Tangerang Selatan. 
Berpengalaman sebagai pengembang website yang memiliki minat dan keterampilan di 
bidang Programming. Saya percaya dapat bekerjasama dan bersikap professional. 
Serta, berkomitmen untuk pengembangan diri dan terus belajar agar dapat 
meningkatkan keterampilan dan pengetahuan saya.""")
