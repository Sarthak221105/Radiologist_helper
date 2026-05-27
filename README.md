# 🩺 Radiologist Helper

Radiologist Helper is a modern web application built with **Streamlit** and **PyTorch** designed to assist radiologists and healthcare professionals. It classifies different types of medical body scans as **Normal** or **Abnormal** (or specific pathologies depending on the scan type).

---

## 🩻 Detection Capabilities

The application supports the following body scan types:

| Scan Type | Model | Classes Detected |
| :--- | :--- | :--- |
| 🦴 **Bone X-Ray** | ResNet50 | Normal, Fracture |
| 🧠 **Brain MRI** | ResNet50 | Glioma, Meningioma, No Tumor, Pituitary |
| 🔬 **CT Scan** | ResNet50 | Adenocarcinoma, Large Cell Carcinoma, Normal, Squamous Cell Carcinoma |
| 📡 **Ultrasound** | ResNet50 | Benign, Malignant, Normal |
| 🫁 **Chest X-Ray** | ResNet50 | Normal, Pneumonia |

---

## 🚀 Getting Started

### Prerequisites
* Python 3.10 or higher
* Docker (Optional, for containerized execution)

### Option 1: Local Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Sarthak221105/Radiologist_helper.git
   cd Radiologist_helper
   ```

2. **Create and Activate a Virtual Environment:**
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure Model Checkpoints are Present:**
   Make sure your trained model files (`.pth`) are placed in the `trained_models/` directory:
   * `trained_models/chest_xray_model.pth`
   * `trained_models/brain_mri_model.pth`
   * `trained_models/CR_scan_model.pth`
   * `trained_models/Ultrasound_model.pth`
   * `trained_models/bone_xray_model.pth`

5. **Run the Streamlit App:**
   ```bash
   streamlit run app.py
   ```
   Open your browser and navigate to `http://localhost:8501`.

---

## 🐳 Option 2: Docker Installation

We provide an optimized Docker setup running on CPU-only PyTorch to minimize container size.

### Using Docker Compose (Recommended)
Build and start the application in the background:
```bash
docker compose up --build
```
Access the application at `http://localhost:8501`.

### Using Docker CLI
1. **Build the Docker Image:**
   ```bash
   docker build -t radiologist-helper -f docker/Dockerfile .
   ```
2. **Run the Container:**
   ```bash
   docker run -p 8501:8501 --name radiologist_helper_app radiologist-helper
   ```

---

## 📂 Project Structure

```text
Radiologist_helper/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python package dependencies
├── docker/
│   └── Dockerfile          # Optimized CPU-only Docker configuration
├── docker-compose.yml      # Docker Compose configuration
├── .dockerignore           # Files ignored by Docker daemon
├── trained_models/         # Directory containing trained PyTorch models (.pth)
├── models/                 # Jupyter Notebooks for model training
└── demo/                   # UI screenshot and demo assets
```

---

## ⚠️ Medical Disclaimer

**This application is for educational, research, and screening support purposes only. It is NOT a substitute for professional medical diagnosis, advice, or treatment.** Always consult with a qualified healthcare professional before making any medical decisions.
