import streamlit as st
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import os

# ------------------------------------------------
# 🔍 Model info with paths and class names
# ------------------------------------------------
model_info = {
    "Chest X-Ray": {
        "path": "trained_models/chest_xray_model.pth",
        "classes": ["Normal", "Pneumonia"]
    },
    "Brain MRI": {
        "path": "trained_models/brain_mri_model.pth",
        "classes": ["Glioma", "Meningioma", "No Tumor", "Pituitary"]
    },
    "CT Scan": {
        "path": "trained_models/CR_scan_model.pth",
        "classes": ["Adenocarcinoma", "Large Cell Carcinoma", "Normal", "Squamous Cell Carcinoma"]
    },
    "Ultrasound": {
        "path": "trained_models/Ultrasound_model.pth",
        "classes": ["Benign", "Malignant","Normal"]
    },
    "Bone X-Ray": {
        "path": "trained_models/bone_xray_model.pth",
        "classes": ["Fracture","Normal"]
    }
}

# ------------------------------------------------
# 🧩 Model Loading Function
# ------------------------------------------------
def load_model(model_path, num_classes):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = models.resnet50(pretrained=False)
    model.fc = nn.Linear(model.fc.in_features, num_classes)
    model = model.to(device)

    if not os.path.exists(model_path):
        st.error(f"❌ Model not found at: {model_path}")
        return None, device

    checkpoint = torch.load(model_path, map_location=device)

    # Handle cases where the checkpoint is wrapped inside "model" key
    if isinstance(checkpoint, dict) and "model" in checkpoint:
        checkpoint = checkpoint["model"]

    # Remove "model." prefix if it exists
    new_state_dict = {}
    for k, v in checkpoint.items():
        new_k = k.replace("model.", "")
        new_state_dict[new_k] = v

    model.load_state_dict(new_state_dict, strict=False)
    model.eval()
    return model, device


# ------------------------------------------------
# 🧾 Image Preprocessing Transform
# ------------------------------------------------
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])
])

# ------------------------------------------------
# 🌐 Streamlit UI
# ------------------------------------------------
st.set_page_config(page_title="🩺 Medical Image Classifier", layout="centered")

st.title("🩻 Medical Image Classifier")
st.write("Upload an image and select its type to classify using the correct trained model.")

# Dropdown to select image type
image_type = st.selectbox("Select Image Type", list(model_info.keys()))

# File uploader
uploaded_file = st.file_uploader("Upload Medical Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    model_path = model_info[image_type]["path"]
    class_names = model_info[image_type]["classes"]

    st.info(f"🔍 Loading {image_type} Model...")
    model, device = load_model(model_path, len(class_names))

    if model is not None:
        # Preprocess image
        img_tensor = transform(image).unsqueeze(0).to(device)

        # Predict
        with torch.no_grad():
            outputs = model(img_tensor)
            _, preds = torch.max(outputs, 1)
            predicted_label = class_names[preds.item()]

        st.success(f"✅ **Predicted Class:** {predicted_label}")


