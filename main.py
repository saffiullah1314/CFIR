import streamlit as st
import numpy as np
from PIL import Image, ImageOps
import tensorflow as tf
import requests, os, json
from io import BytesIO
import gdown

st.set_page_config(page_title="CIFAR-10 Classifier", layout="wide", page_icon="🤖")


st.markdown("""
<style>
    .reportview-container { font-family: 'Segoe UI', Tahoma, sans-serif; }
    .stButton>button { border-radius: 10px; }
    .big-title { font-size:28px; font-weight:600; }
    .subtle { color: #6c757d; font-size:14px; }
</style>
""", unsafe_allow_html=True)


MODEL_PATH = "model_final.h5"
CLASSES_PATH = "classes.json"

def download_if_needed(url, out_path):
    if url and not os.path.exists(out_path):
        
        gdown.download(url, out_path, quiet=False)


@st.cache_resource
def load_model():
    model = tf.keras.models.load_model(MODEL_PATH)
    if os.path.exists(CLASSES_PATH):
        with open(CLASSES_PATH,'r') as f:
            classes = json.load(f)
    else:
        classes = ['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck']
    return model, classes

model, class_names = load_model()

def preprocess_image(img: Image.Image, target_size=(32,32)):
    img = img.convert('RGB')
    img = ImageOps.fit(img, target_size, Image.Resampling.LANCZOS)
    arr = np.array(img).astype('float32') / 255.0
    arr = np.expand_dims(arr, 0)  # batch dim
    return arr


col1, col2 = st.columns([2,1])
with col1:
    st.markdown('<div class="big-title">CIFAR-10 Image Classifier</div>', unsafe_allow_html=True)
    st.write("Upload an image or use your camera. Model predicts class with probabilities.")

    uploaded = st.file_uploader("Upload image", type=["png","jpg","jpeg"])
    camera_img = st.camera_input("Or take a photo (mobile/desktop)")

    img = None
    if uploaded:
        img = Image.open(uploaded)
    elif camera_img:
        img = Image.open(camera_img)

    if img is not None:
        st.image(img, caption="Input image", use_column_width=True)
        inp = preprocess_image(img)
        preds = model.predict(inp)[0]
        top_idx = np.argsort(preds)[::-1][:3]
        st.subheader("Predictions")
        for i, idx in enumerate(top_idx):
            st.write(f"**{i+1}. {class_names[idx]}** — {preds[idx]*100:.2f}%")
            st.progress(float(preds[idx]))
    else:
        st.write("Upload an example image to see predictions.")

with col2:
    st.sidebar.title("About")
    st.sidebar.markdown("**Model:** Trained on CIFAR-10 (Colab).")
    st.sidebar.markdown("**How to use:** Upload 1 image (32x32 resized).")
    st.sidebar.markdown("**Notes:** Make sure model_final.h5 is in repo or MODEL_PUBLIC_URL is set for download.")

# Optional: show example gallery (from repo assets)
st.markdown("---")
st.write("Sample gallery")
samples = ["assets/dog.jpg","assets/cat.jpg"]  # add to repo
gallery = st.columns(len(samples))
for i, path in enumerate(samples):
    try:
        gallery[i].image(path, use_column_width=True)
    except:
        pass
