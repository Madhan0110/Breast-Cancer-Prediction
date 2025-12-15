# import pickle
# import streamlit as st

# # Load model
# with open("wbc_model.sav", "rb") as file:
#     model = pickle.load(file)

# st.title('Breast Cancer Prediction App')

# # Input fields
# # diagnosis = st.selectbox('Diagnosis (0 = Benign, 1 = Malignant)', [0, 1])

# radius_mean = st.text_input('Radius Mean')
# texture_mean = st.text_input('Texture Mean')
# perimeter_mean = st.text_input('Perimeter Mean')
# area_mean = st.text_input('Area Mean')
# smoothness_mean = st.text_input('Smoothness Mean')
# compactness_mean = st.text_input('Compactness Mean')
# concavity_mean = st.text_input('Concavity Mean')
# concave_points_mean = st.text_input('Concave Points Mean')
# symmetry_mean = st.text_input('Symmetry Mean')
# fractal_dimension_mean = st.text_input('Fractal Dimension Mean')

# radius_se = st.text_input('Radius SE')
# texture_se = st.text_input('Texture SE')
# perimeter_se = st.text_input('Perimeter SE')
# area_se = st.text_input('Area SE')
# smoothness_se = st.text_input('Smoothness SE')
# compactness_se = st.text_input('Compactness SE')
# concavity_se = st.text_input('Concavity SE')
# concave_points_se = st.text_input('Concave Points SE')
# symmetry_se = st.text_input('Symmetry SE')
# fractal_dimension_se = st.text_input('Fractal Dimension SE')

# radius_worst = st.text_input('Radius Worst')
# texture_worst = st.text_input('Texture Worst')
# perimeter_worst = st.text_input('Perimeter Worst')
# area_worst = st.text_input('Area Worst')
# smoothness_worst = st.text_input('Smoothness Worst')
# compactness_worst = st.text_input('Compactness Worst')
# concavity_worst = st.text_input('Concavity Worst')
# concave_points_worst = st.text_input('Concave Points Worst')
# symmetry_worst = st.text_input('Symmetry Worst')
# fractal_dimension_worst = st.text_input('Fractal Dimension Worst')

# # Prediction button
# if st.button('Cancer Test Result'):

#     def safe_float(val):
#         try:
#             return float(val)
#         except:
#             return None

#     user_input = [

#         safe_float(radius_mean),
#         safe_float(texture_mean),
#         safe_float(perimeter_mean),
#         safe_float(area_mean),
#         safe_float(smoothness_mean),
#         safe_float(compactness_mean),
#         safe_float(concavity_mean),
#         safe_float(concave_points_mean),
#         safe_float(symmetry_mean),
#         safe_float(fractal_dimension_mean),
#         safe_float(radius_se),
#         safe_float(texture_se),
#         safe_float(perimeter_se),
#         safe_float(area_se),
#         safe_float(smoothness_se),
#         safe_float(compactness_se),
#         safe_float(concavity_se),
#         safe_float(concave_points_se),
#         safe_float(symmetry_se),
#         safe_float(fractal_dimension_se),
#         safe_float(radius_worst),
#         safe_float(texture_worst),
#         safe_float(perimeter_worst),
#         safe_float(area_worst),
#         safe_float(smoothness_worst),
#         safe_float(compactness_worst),
#         safe_float(concavity_worst),
#         safe_float(concave_points_worst),
#         safe_float(symmetry_worst),
#         safe_float(fractal_dimension_worst)
#     ]

#     if None in user_input:
#         st.write("⚠️ Please enter valid numeric values")
#     else:
#         prediction = model.predict([user_input])

#         if prediction[0] == 1:
#             st.error('Malignant Tumor Detected – Consult a Doctor Immediately')
#         else:
#             st.success('Benign Tumor – No Cancer Detected')


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


