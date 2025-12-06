## 📁 Repository Structure

├── data/

│   └── breast_cancer_data.csv

├── notebooks/

│   └── Breast_Cancer_Prediction.ipynb

├── src/

│   ├── preprocess.py

│   ├── train_model.py

│   └── evaluate.py

├── models/

│   └── final_model.pkl

├── README.md

└── requirements.txt



## 🧬 Breast Cancer Prediction using Machine Learning
A machine learning project that predicts whether a tumor is benign or malignant using the Breast Cancer Wisconsin Dataset.
This repository includes data preprocessing, exploratory data analysis (EDA), model training, evaluation, and deployment.

## 📌 Project Overview

Early detection of breast cancer significantly increases survival rates.
This project uses machine learning algorithms to classify tumors based on medical diagnostic features.

1. The workflow includes:

2. Data preprocessing

3. Exploratory data analysis (EDA)

4. Feature engineering

5. Model building (Multiple ML algorithms)

6. Model evaluation

## 🧪 Dataset

The dataset used is the Breast Cancer Wisconsin Diagnostic Dataset, which contains:

 569 samples
 30 numeric diagnostic features
 #### Classification label:

      0 → Malignant
      1 → Benign

You can download the dataset directly from:

    1. Scikit-learn datasets module, or

   2.  UCI Machine Learning Repository

## 🛠️ Technologies Used

1. Python 3.8+
2. Pandas, NumPy
3. Matplotlib, Seaborn
4. Scikit-learn
5. Jupyter Notebook
6. Flask / Streamlit for deployment

### ⚙️ Modeling Approach

### Models trained in the project:

1. Logistic Regression
2. Random Forest Classifier
3. Support Vector Machine (SVM)
4. Gradient Boosting
5. K-Nearest Neighbors (KNN)
   ### Performance metrics evaluated:
1. Accuracy
2. Precision
3. Recall
4. F1-score
5. ROC-AUC
