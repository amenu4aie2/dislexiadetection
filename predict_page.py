import streamlit as st
from PIL import Image
from keras.models import load_model
from keras.preprocessing.image import load_img
from keras.preprocessing.image import image
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16
import numpy as np


def load_image(image):
    image = Image.open(image)
    kkpp = image.save("dolls.png")
    return image


def main():
    st.title("File Upload Tutorial")

    menu = ["Image"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Image":
        st.subheader("Image")

    image = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])
    if image is not None:

        # To See details
        file_details = {"filename": image.name, "filetype": image.type,
                        "filesize": image.size}
        st.write(file_details)

# To View Uploaded Image
        st.image(load_image(image), width=224)

        model = load_model('model_saved.h5')

        img = load_img(
            r"C:\Users\cody\Downloads\studies\hackahon\dolls.png", target_size=(224, 224))
        img = np.array(img)

        img = img/255
        img = img.reshape(-1, 224, 224, 3)
        label = (model.predict(img) < 0.4).astype(np.int32)

        st.write(
            "Predicted Class (0 - Non-dyslexia , 1- Dyslexia): ", label[0][0])


main()
