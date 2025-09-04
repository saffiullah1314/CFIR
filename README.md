# 🖼️ CIFAR-10 Image Classifier (Deep Learning + Streamlit)

This is a **Deep Learning project** built using **TensorFlow/Keras** and deployed with **Streamlit**.  
The model is trained on the **CIFAR-10 dataset** (60,000 images, 10 classes) and can classify images into categories like **airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck**.

🚀 **Live Demo**: [Click Here to Try!](https://cfir7z.streamlit.app/)

---

## 📌 Features
- Upload an image OR capture live photo using your webcam.
- Model resizes image to `32x32` before prediction.
- Shows **Top-3 predictions with confidence bars**.
- Displays probability distribution for all 10 classes.
- Fully responsive **Dark Theme UI** with CSS animations and styled cards.
- Ready-to-deploy using **Streamlit Cloud**.

---

## 📂 Project Structure
CIFAR10-Image-Classifier/
│
├── app.py # Streamlit application
├── model_final.h5 # Trained CNN model
├── classes.json # CIFAR-10 class names
├── requirements.txt # Dependencies
└── README.md # Documentation

---

## ⚙️ Installation & Usage

### 🔹 1. Clone the repository
```bash
git clone https://github.com/YOUR-USERNAME/CIFAR10-Image-Classifier.git
cd CIFAR10-Image-Classifier
```
### 🔹 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```
### 🔹 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 🔹 4. Run the Streamlit app locally
```bash
streamlit run app.py
```
Now open 👉 **http://localhost:8501 in your browser.**

### 🧠 Model Training
- Dataset: CIFAR-10 (32x32 images, 10 classes)

- Model: Convolutional Neural Network (CNN)

- Training Environment: Google Colab (GPU)

- Optimizer: Adam

- Loss: Categorical Crossentropy

- Accuracy achieved: ~80%

- Trained model saved as model_final.h5.
---
### ☁️ Deployment (Streamlit Cloud)
- Push your project to GitHub.

- Go to Streamlit Cloud.

- Click **New app** → connect your GitHub repo.
- Repo: https://github.com/saffiullah1314/CFIR
- Branch: main
- File: app.py

 ---
 
## Predictions

- 🙌 Author
- 👨‍💻 Developed by Safi Ullah
**Passionate Full Stack Developer & ML Enthusiast**

🔗 Connect with me: LinkedIn | GitHub

⭐ Support
If you like this project, give it a star ⭐ on GitHub — it really motivates me!

