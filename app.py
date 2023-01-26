import streamlit as st
import qrcode
import PIL
from PIL import Image


def criar_qrcode():
    if codigo == "":
        st.error("Código Inválido")
        pass
    else:
        img_qrcode = qrcode.make(codigo)
        img_qrcode.save("qrcode.png")
        img_qrcode_final = st.image("qrcode.png", width=300)

logo = st.image("logo_mcdonalds.png", width=100)
titulo = st.title('QRCode 4 Pickup')
codigo = st.text_input("", max_chars=5, placeholder=("Introduz o Código do Pedido"))
btn_criar = st.button("Criar QRCode", on_click=criar_qrcode)
