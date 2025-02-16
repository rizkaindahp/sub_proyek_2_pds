
# Mengimpor library yang diperlukan
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load('model/student_rf_model.pkl')
scaler = joblib.load('model/scaler.pkl')


# Mengatur konfigurasi halaman Streamlit
st.set_page_config(page_title="Predict Student Dropout/Enroll/Graduated)", page_icon=":sushi:")

# Function to make predictions
def predict_status(inputs):
    # Convert inputs to numpy array and reshape
    input_array = np.array(inputs).reshape(1, -1)
    input_array = scaler.transform(input_array)
    prediction = model.predict(input_array)
    return prediction

# Menampilkan judul halaman
st.title("Prediksi Status Siswa")


# Membuat tab untuk single prediction dan multi-prediction
tab1, = st.tabs(["Prediksi"])

# Bagian Predict
with tab1:
    st.sidebar.header("**User Input** Sidebar")

    # Input fields for user to input data
    curr_units_2nd_sem_appr = st.sidebar.number_input('Curricular Units 2nd Semester Approved', min_value=0, max_value=30, value=15)
    curr_units_2nd_sem_grade = st.sidebar.number_input('Curricular Units 2nd Semester Grade', min_value=0, max_value=20, value=15)
    curr_units_1st_sem_appr = st.sidebar.number_input('Curricular Units 1st Semester Approved', min_value=0, max_value=30, value=15)
    curr_units_1st_sem_grade = st.sidebar.number_input('Curricular Units 1st Semester Grade', min_value=0, max_value=20, value=15)
    tuition_fees_up_to_date = st.sidebar.selectbox('Tuition Fees Up to Date', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
    scholarship_holder = st.sidebar.selectbox('Scholarship Holder', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
    curr_units_2nd_sem_enrolled = st.sidebar.number_input('Curricular Units 2nd Semester Enrolled', min_value=0, max_value=30, value=20)
    curr_units_1st_sem_enrolled = st.sidebar.number_input('Curricular Units 1st Semester Enrolled', min_value=0, max_value=30, value=20)
    admission_grade = st.sidebar.slider('Admission Grade', min_value=0.0, max_value=200.0, value=5.0, step=0.1)
    displaced = st.sidebar.selectbox('Displaced', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')


    # Map the inputs to the format expected by the model
    input_data = [
        curr_units_2nd_sem_appr,
        curr_units_2nd_sem_grade,
        curr_units_1st_sem_appr,
        curr_units_1st_sem_grade,
        tuition_fees_up_to_date,
        scholarship_holder,
        curr_units_2nd_sem_enrolled,
        curr_units_1st_sem_enrolled,
        admission_grade,
        displaced
    ]

    predict_btn = st.button("**Prediksi**", type="primary")

    # Button for prediction
    if predict_btn:
        prediction = predict_status(input_data)

        # The prediction will be a 1D array or 2D array depending on model
        status_dict = {
            0: 'Dropout',
            1: 'Enrolled',
            2: 'Graduate'
        }

        # Check if prediction is 1D or 2D and adjust accordingly
        if prediction.ndim == 1:
            predicted_status_index = np.argmax(prediction)
        else:
            predicted_status_index = np.argmax(prediction, axis=1)[0]

        predicted_status = status_dict[predicted_status_index]

        # Menampilkan hasil prediksi dengan format yang lebih jelas
        st.write("")
        st.subheader("Hasil Prediksi:")
        st.success(f"📈 **{predicted_status}**")
        # st.write(predicted_status)


    