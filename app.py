#  Importing Libraries
import numpy as np # Math manipulation
import cv2 as cv # Computer vision
import matplotlib.pyplot as plt # View
# import skimage.io as io # Image manipulation
import pandas as pd
import streamlit as st
from PIL import Image, ImageOps

import morphology as pm 
import auxiliars as ps
import watershed as pw

st.set_option('deprecation.showPyplotGlobalUse', False)

# Constantes

KERNEL_TYPES = ['Rect', 'Ellipse', 'Cross']
IMAGENS = ['flower','bloodcells', 'chickparts', 'coins', 'cookies', 'j', 'leaf', 'potatoes']
OPERATIONS = ['Erosão', 'Dilatação', 'Opening', 'Closing', 'Gradient', 'Tophat']

# Start

with st.sidebar:
    # img = st.selectbox('Selecionar Imagem:', IMAGENS)

    page = st.selectbox('Página', ['Morfologia Matemática', 'Segmentação'])
    
    if page == 'Morfologia Matemática':

        img = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

        # operations = st.multiselect('Escolha as operações para aplicar (Na ordem de preferência): ', OPERATIONS)
        operation = st.selectbox('Escolha a operação para aplicar: ', OPERATIONS)
        st.write('Criar Kernel')
        kernel_type = st.selectbox('Formato', KERNEL_TYPES) 
        col1, col2 = st.columns(2)
        with col1:
            linhas = st.slider('Número de Linhas', 0, 20, 1)
            n_iterations =  st.number_input('Número de iterações: ', 1, 50, 1, 1)
        with col2:
            colunas = st.slider('Número de colunas', 0, 20, 1)

        aplicar = st.button('Aplicar')

    elif page == 'Segmentação':
        
        img = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

        aplicar = st.button('Aplicar')

if page == 'Morfologia Matemática':    

    st.title('Aplicações Operações de Morfologia Matemática')

    if img is not None:
        st.image(img)
        im = Image.open(img)
        image = np.array(im)
        # image = cv.imread(f'images/{img}.jpg', 0)
        # st.image(f'images/{img}.jpg')

    if aplicar:
        kernel = pm.get_kernel(kernel_type, (linhas, colunas))
        result = pm.applyOperation(image, operation, kernel, n_iterations)
        image = Image.fromarray(result)
        st.image(image, caption=f"Imagem com {operation} - {kernel_type} ({linhas}, {colunas}) {n_iterations}x")

        im_bytes = ps.imgToByte(image)

        btn = st.download_button(
            label="Baixar",
            data = im_bytes,
            file_name="Example.png",
            mime="image/png"
        )    

elif page == 'Segmentação':

    st.title('Segmentação')

    if img is not None:
        im = Image.open(img)
        gray = ImageOps.grayscale(im)
        im_array = np.array(gray)

    if aplicar:
        img = pw.watershed_with_markers(im_array)
        img = Image.fromarray(img)

        plt.imshow(img)
        st.pyplot()