import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

st.write("[![Star](https://img.shields.io/github/stars/irchamali.svg?logo=github&style=social)](https://github.com/irchamali)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('ia.png'))

st.header('Ircham Ali, M.Kom.')

st.info('System Analyst, Web Designer, and Informatics Lecturer')

icon_size = 20

st_button('linkedin', 'https://www.linkedin.com/in/ircham-ali/', 'Follow me on LinkedIn', icon_size)
st_button('youtube', 'https://www.youtube.com/@unusialabs', 'Subscribe our YouTube', icon_size)
st_button('medium', 'https://irchamali.medium.com/', 'Read my Medium Blogs', icon_size)
st_button('instagram', 'https://instagram.com/irchamali_/', 'Follow me on Instagram', icon_size)
st_button('twitter', 'https://twitter.com/irchamxyz/', 'Follow me on Twitter', icon_size)
st_button('facebook', 'https://facebook.com/dosenirham/', 'Follow me on Facebook', icon_size)

