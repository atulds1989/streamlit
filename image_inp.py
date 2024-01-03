import streamlit as st
from PIL import Image
import cv2, numpy as np
st.title("Upload an image as an input")

image_file = st.file_uploader(r"C:\Users\hp\OneDrive\Pictures\Screenshots\asura.jpg", type="jpg")

# if image_file is not None:
#     img1 = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), 1)
#     img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
#     st.image(img1, caption="input image.", use_column_width=True)
#     st.write(img1)
    

    

# if image_file is not None:
#     img2 = Image.open(image_file)
#     st.image(img2, caption="input image.", use_column_width=True)
    

