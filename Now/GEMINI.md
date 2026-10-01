# Automated Detection of Cardiac Arrhythmia using Deep Learning (Production Ready)

## Project Overview
This project implements an automated, production-ready system for detecting **cardiac arrhythmia** from ECG signal data using deep learning models — specifically **LSTM** and **CNN**. 

The application has been heavily upgraded to include a **Doctor-Friendly, Tabbed GUI** that handles not only model training and evaluation, but also **single-patient clinical predictions**, **PDF report generation**, and **SQLite-based patient history logging**.

The dataset used is the **MIT-BIH Arrhythmia Dataset**, classifying ECG records into **7 distinct cardiac conditions**.

---

## 🚀 What's New in the Production Version (v2.0 & v3.0)

### 🏥 Doctor-Friendly Features (v2.0)
- **Tabbed Interface:** Separated "Model Training" and "Patient Prediction" workflows.
- **Doctor Parameters Panel:** Sliders to adjust PCA components, LSTM units, Dropout Rate, Epochs, and Batch Size on the fly.
- **Patient Clinical Form:** Input fields for Name, Age, Gender, Symptoms, Medications, BP, and Doctor Notes.
- **Real-Time Confidence Charts:** Matplotlib horizontal bar charts embedded directly in the UI showing probability for all 7 conditions.
- **Automated PDF Reports:** Generates a highly polished, printable HTML/PDF report combining clinical notes and ML confidence scores.
- **SQLite Patient Database:** Automatically logs all predictions, vitals, and diagnoses into `patient_history.db` with a built-in UI viewer.

### 🧠 Advanced ML Architecture Upgrades (v3.0)
To ensure the model is highly robust for clinical use, the core ML pipeline was completely rebuilt for scalability and accuracy:
- **Ensemble Learning (Flexibility):** Doctors can now select `Ensemble (Best)` in the prediction UI. This runs the patient's ECG through both the Deep LSTM and CNN simultaneously and averages their probabilities to provide the highest possible diagnostic accuracy.
- **Class Balancing (Accuracy):** Medical data is highly imbalanced (mostly "Normal" patients). The training pipeline now uses `sklearn.utils.class_weight` to mathematically penalize the model for missing rare conditions (like Myocardial Infarction), drastically improving True Positive sensitivity for fatal conditions.
- **Early Stopping & Checkpointing (Scalability):** The model uses `keras.callbacks.EarlyStopping` to stop training the moment validation accuracy peaks (patience=15) and automatically restores the best weights, preventing overfitting and saving training time.
- **Deep Architecture (Accuracy):** The LSTM was upgraded to a 2-layer Deep LSTM structure, and both LSTM and CNN received heavy `Dropout` layers to regularize the networks, ensuring they memorize actual clinical patterns rather than overfitting on test data.

---

## Project Structure
```text
project-root/
│
├── Main.py                  # Main application entry point (Tabbed GUI + ML + DB pipeline)
├── requirements.txt         # Python dependencies 
├── run.bat                  # Windows batch script to launch the app
├── GEMINI.md                # Project documentation
│
├── patient_history.db       # SQLite database logging all patient diagnoses (Auto-generated)
├── patient_report.html      # Printable clinical report (Auto-generated per patient)
├── output.html              # Model performance comparison table
│
├── Dataset/
│   └── arrhythmia.csv       # MIT-BIH Arrhythmia Dataset (279 features)
│
└── model/                   # Saved models
    ├── pca.txt                  # Saved PCA transformation object
    ├── lstm_model.json          # LSTM architecture
    ├── lstm_model_weights.h5    # LSTM trained weights
    ├── lstm_history.pckl        # LSTM training history
    ├── cnn_model.json           # CNN architecture
    ├── cnn_model_weights.h5     # CNN trained weights
    └── cnn_history.pckl         # CNN training history
```

---

## Application Workflow

### Tab 1: Model Training & Evaluation
1. **Adjust Parameters:** Use the sidebar sliders to tune hyper-parameters before training.
2. **Upload & Preprocess:** Load `arrhythmia.csv`. Preprocessing fills missing values, normalizes, applies PCA (and saves it to disk), and splits the data.
3. **Train Models:** Run Deep LSTM and Deep CNN. The models utilize Early Stopping and Dynamic Class Balancing. If models exist on disk, they load instantly unless the "Force Retrain" checkbox is ticked.
4. **Evaluate:** Generate training loss/accuracy graphs and performance tables comparing Accuracy, Precision, Recall, F-Score, Sensitivity, and Specificity.

### Tab 2: Patient Prediction & Diagnosis
1. **Clinical Data Entry:** The doctor fills out the patient's vitals, ID, and clinical notes.
2. **Model Selection:** The doctor selects whether to predict using LSTM, CNN, or Ensemble (Best).
3. **Predict:** Click "Predict on Test Patient" to process an ECG sample through the trained models.
4. **Analyze Results:** The UI displays the predicted diagnosis, an uncertainty warning if confidence is <60%, and a bar chart of all 7 condition probabilities.
5. **Generate Report:** Creates and opens a printable `patient_report.html` tailored for medical records.
6. **View History:** Opens a spreadsheet view of the `patient_history.db` SQLite database showing all past predictions.

---

## Setup & Installation

### Prerequisites
- Python 3.6–3.8 (recommended for TensorFlow 1.14 compatibility)
- Windows OS (for `run.bat`)

### Install Dependencies
```bash
pip install numpy==1.19.2 pandas==0.25.3 matplotlib==3.1.1
pip install keras==2.3.1 tensorflow==1.14.0 h5py==2.10.0
pip install protobuf==3.16.0 scikit-learn==0.22.2.post1 seaborn==0.10.1
```

## Authors & Context
Developed as a production-grade implementation of deep learning-based cardiac arrhythmia detection, bridging the gap between raw machine learning scripts and an interactive, usable medical tool.
