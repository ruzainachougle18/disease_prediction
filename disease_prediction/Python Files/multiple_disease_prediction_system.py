#Importing the dependencies

import pickle
import streamlit as st 
from streamlit_option_menu import option_menu

#Diabetes Prediction Page
def diabetes_prediction(diabetes_model):
    #PAGE Title
    st.title('Diabetes Prediction')

    #Getting input data from the user

    #Columns for input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure')
        
    with col1:
        SkinThickness = st.text_input('Skin Thickness')
        
    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Prediction Function')
    
    with col2:
        Age = st.text_input('Age')

    #Prediction
    diabetes_diagnosis = ''

    #Creating a button for Prediction
    if st.button('Diabetes Test Result'):

        diabetes_predicted = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, 
                                              Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if (diabetes_predicted[0] == 0): 
            diabetes_diagnosis = 'The person is Not Diabetic.'
        else:
            diabetes_diagnosis = 'The person is Diabetic.'
        
    st.success(diabetes_diagnosis)    


#Heart Disease Prediciton Page
def heart_disease_prediction(heart_disease_model):
    #Page Title
    st.title('Heart Disease Prediction')
    
    #Getting input data from the user
    
    #Columns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Age = st.text_input('Age')
        
    with col2:
        Sex = st.text_input('Gender')
        
    with col3:
        CP = st.text_input('Chest Pain Type')
        
    with col1:
        Trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        Chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        FBS = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        Restecg = st.text_input('Resting Electrocardiographic Results')
        
    with col2:
        Thalach = st.text_input('Maximum Heart Rate Achieved')
        
    with col3:
        Exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        Oldpeak = st.text_input('ST Depression Induced by Exercise')
        
    with col2:
        Slope = st.text_input('Slope of the Peak Exercise ST Segment')
        
    with col3:
        CA = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        Thal = st.text_input('Defect Type')

    #Code for prediction
    heart_disease_diagnosis = ''
    
    #Creating a button for prediction
    if st.button('Heart Disease Test Result'):
    
        heart_disease_predicted = heart_disease_model.predict([[Age,Sex,CP,Trestbps,Chol,FBS,Restecg,Thalach,Exang,Oldpeak,Slope,CA,Thal]])           
        
        if (heart_disease_predicted[0] == 1):
          heart_disease_diagnosis = 'The person is having heart disease'
        else:
          heart_disease_diagnosis = 'The person does not have any heart disease'
          
        print(heart_disease_diagnosis)
        
    st.success(heart_disease_diagnosis)        



    #Code for prediction
    parkinsons_diagnosis = ''
    
    #Creating a button for prediction
    if st.button('Parkinsons Test Result'):
    
        parkinsons_predicted = parkinsons_model.predict([[Fo, Fhi, Flo, Jitter_Perc, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, 
                                                                      APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])           
        
        if (parkinsons_predicted[0] == 0):
          parkinsons_diagnosis = 'The person is Healthy.\n'
        else:
          parkinsons_diagnosis = 'The person is Parkinson\'s Positive.\n'
        
    st.success(parkinsons_diagnosis)
    

def main():
    #Loading the saved model
    diabetes_model = pickle.load(open('C:/Users/ruzai/Desktop/multiple_disease_prediction_using_ml/Python Files/diabetes_trained_model.sav', 'rb'))
    heart_disease_model = pickle.load(open('C:/Users/ruzai/Desktop/multiple_disease_prediction_using_ml/Python Files/heart_disease_trained_model.sav', 'rb'))
    parkinsons_model = pickle.load(open('C:/Users/ruzai/Desktop/multiple_disease_prediction_using_ml/Python Files/parkinsons_disease_trained_model.sav', 'rb'))
        
    #Sidebar for navigation
    with st.sidebar:
        selected = option_menu('Multiple disease Prediction System',
                               ['Diabetes Prediction',
                                'Heart Disease Prediction',
                                'Parkinsons Prediction'],
                               icons = ['activity', 'heart', 'person', 'gender-female'],
                               default_index = 0)
    
    if(selected == 'Diabetes Prediction'):
        diabetes_prediction(diabetes_model)
        
    if (selected == 'Heart Disease Prediction'):
        heart_disease_prediction(heart_disease_model)
    
    if (selected == 'Parkinsons Prediction'):
        parkinsons_prediction(parkinsons_disease_model)

if __name__ == '__main__':
    
    main()
    
