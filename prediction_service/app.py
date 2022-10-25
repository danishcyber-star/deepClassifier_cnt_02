import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np
"""
# deep Classifier project

"""
model = tf.keras.models.load_model("C:/Users/dan7i/Downloads/FSDS_NOV_deepCNNClassifier-main/artifacts/prepare_base_model/base_model_updated.h5")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:

    image = Image.open(uploaded_file)
    img = image.resize((224,224))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0) # [batch_size, row, col, channel]
    result = model.predict(img_array) # [[0.99, 0.01], [0.99, 0.01]]

    argmax_index = np.argmax(result, axis=1) # [0, 0]
    if argmax_index[0] == 0:
        st.image(image, caption="predicted: cat")
    else:
        st.image(image, caption='predicted: dog')
      
    