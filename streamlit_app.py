import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('ia.png'))

st.header('Ircham Ali, M.Kom')

st.info('Web Developer and Informatics Lecturer')

icon_size = 20

st_button('youtube', 'https://www.youtube.com/channel/UCsqZalj5sdMDX2yUoeLMkXw', 'Unusia Labs', icon_size)
st_button('medium', 'https://broirham.medium.com/', 'Read my Blogs', icon_size)
st_button('instagram', 'https://instagram.com/bro_irham/', 'Folloe me on Instagram', icon_size)
st_button('twitter', 'https://twitter.com/bro_irham/', 'Follow me on Twitter', icon_size)
st_button('facebook', 'https://facebook.com/dosenirham/', 'Follow me on Facebook', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/ircham-ali/', 'Follow me on LinkedIn', icon_size)

