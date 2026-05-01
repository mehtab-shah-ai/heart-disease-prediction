# 🫀 Heart Disease Prediction App

A machine learning web app that predicts the risk of 
heart disease based on basic medical parameters.

## 📊 Dataset
- **Source:** Heart Failure Prediction Dataset (Kaggle)
- **Size:** 918 patients
- **Features:** 11 medical parameters

## 🎯 Model Performance
| Metric    | Score  |
|-----------|--------|
| Model     | KNN Classifier |
| Input     | 11 Medical Features |
| Output    | High Risk / Low Risk |

## 🔬 Features Used
| Feature | Description |
|---------|-------------|
| Age | Patient age |
| Sex | M / F |
| ChestPainType | ATA / NAP / TA / ASY |
| RestingBP | Resting blood pressure |
| Cholesterol | Serum cholesterol |
| FastingBS | Fasting blood sugar |
| RestingECG | ECG results |
| MaxHR | Maximum heart rate |
| ExerciseAngina | Exercise induced angina |
| Oldpeak | ST depression |
| ST_Slope | Slope of peak exercise ST |

## 🛠️ Tech Stack
- **Language:** Python
- **ML Library:** Scikit-learn
- **Web App:** Streamlit
- **Data Processing:** Pandas, NumPy

## 📁 Project Structure
HEARTAPP/
├── App.py                 ← Streamlit app
├── knn_heart_model.pkl    ← Trained KNN model
├── heart_scaler.pkl       ← StandardScaler
├── heart_columns.pkl      ← Expected columns
├── requirements.txt       ← Dependencies
└── README.md
