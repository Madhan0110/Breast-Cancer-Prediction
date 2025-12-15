import pickle
import streamlit as st

# Load model
with open("wbc_model.sav", "rb") as file:
    model = pickle.load(file)

st.title('Breast Cancer Prediction App')

col1, col2 = st.columns(2)

with col1:
    radius_mean = st.number_input('Radius Mean')
    perimeter_mean = st.number_input('Perimeter Mean')
    smoothness_mean = st.number_input('Smoothness Mean')
    concavity_mean = st.number_input('Concavity Mean')
    symmetry_mean = st.number_input('Symmetry Mean')

    radius_se = st.number_input('Radius SE')
    perimeter_se = st.number_input('Perimeter SE')
    smoothness_se = st.number_input('Smoothness SE')
    concavity_se = st.number_input('Concavity SE')
    symmetry_se = st.number_input('Symmetry SE')

    radius_worst = st.number_input('Radius Worst')
    perimeter_worst = st.number_input('Perimeter Worst')
    smoothness_worst = st.number_input('Smoothness Worst')
    concavity_worst = st.number_input('Concavity Worst')
    symmetry_worst = st.number_input('Symmetry Worst')

with col2:
    texture_mean = st.number_input('Texture Mean')
    area_mean = st.number_input('Area Mean')
    compactness_mean = st.number_input('Compactness Mean')
    concave_points_mean = st.number_input('Concave Points Mean')
    fractal_dimension_mean = st.number_input('Fractal Dimension Mean')

    texture_se = st.number_input('Texture SE')
    area_se = st.number_input('Area SE')
    compactness_se = st.number_input('Compactness SE')
    concave_points_se = st.number_input('Concave Points SE')
    fractal_dimension_se = st.number_input('Fractal Dimension SE')

    texture_worst = st.number_input('Texture Worst')
    area_worst = st.number_input('Area Worst')
    compactness_worst = st.number_input('Compactness Worst')
    concave_points_worst = st.number_input('Concave Points Worst')
    fractal_dimension_worst = st.number_input('Fractal Dimension Worst')

# Prediction
if st.button('Cancer Test Result'):

    user_input = [
        radius_mean, texture_mean, perimeter_mean, area_mean,
        smoothness_mean, compactness_mean, concavity_mean,
        concave_points_mean, symmetry_mean, fractal_dimension_mean,

        radius_se, texture_se, perimeter_se, area_se,
        smoothness_se, compactness_se, concavity_se,
        concave_points_se, symmetry_se, fractal_dimension_se,

        radius_worst, texture_worst, perimeter_worst, area_worst,
        smoothness_worst, compactness_worst, concavity_worst,
        concave_points_worst, symmetry_worst, fractal_dimension_worst
    ]

    prediction = model.predict([user_input])

    if prediction[0] == 1:
        st.error('Malignant Tumor Detected – Consult a Doctor Immediately')
    else:
        st.success('Benign Tumor – No Cancer Detected')




