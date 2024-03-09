import os
import sys
os.path.dirname(sys.executable)

import streamlit as st
import pickle
import numpy as np
import pandas as pd
import joblib
loaded_model = pickle.load(open("Algorithms/trained_model.pickle", "rb"))
def Stress_prediction(input_data):
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,5)

    prediction = loaded_model.predict(input_data_reshaped)

    if (prediction[0] == 3):
        return 'The person has kind of stress but not much'
    elif(prediction[0] < 3):
        return 'The person is not stressful'
    elif(prediction[0] > 3):
        return 'The person is highly stressful'
def main ():
    st.title('Stress Levelini Olc')

    Sleep_quality =       st.select_slider('Kindly Rate your Sleep Quality 😴',[1,2,3,4,5])
    Headaches_frequency = st.select_slider('How many times a week do you suffer headaches 🤕?',[1,2,3,4,5])
    Academic_success    = st.select_slider('How would you rate you academic performance 👩‍🎓?',[1,2,3,4,5])
    Academic_load       = st.select_slider('How would you rate ur academic load',[1,2,3,4,5])
    Doing_sports        = st.select_slider('How many times a week you practice extracurricular activities 🎾?',[1,2,3,4,5])

    Stress_level = ''


    if st.button('Stress Level Olc!'):
         Stress_level = Stress_prediction([Sleep_quality, Headaches_frequency, Academic_success, Academic_load, Doing_sports])

    st.success(Stress_level)
    

if __name__ == '__main__':
    main()