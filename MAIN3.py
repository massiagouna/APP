import streamlit as st
import numpy as np
import pandas as pd
import pickle as pkl
#import matplotlib.pyplot as plt
#from sklearn import datasets
#from sklearn.model_selection import train_test_split

#from sklearn.decomposition import PCA
#from sklearn.svm import SVC
#from sklearn.neighbors import KNeighborsClassifier
#from sklearn.ensemble import RandomForestClassifier

#from sklearn.metrics import accuracy_score


st.title('PREDICTION DES PRIX')

classifier_name = st.sidebar.selectbox(
    'Select classifier',
    ('RandomForestRegressor', 'LGBMRegressor', 'XGBRegressor')
)

########################


#fhi = st.text_input('code de la commune')
#flo = st.text_input('code de la commune')
Jitter_percent = st.text_input('nom de la commune')
Jitter_Abs = st.text_input('code de la commune')
RAP = st.text_input('type du local')
PPQ = st.text_input('surface réelle')
DDP = st.text_input('surface de terrain')
APQ = st.text_input('year')


Shimmer_dB = st.text_input('longitude')
APQ3 = st.text_input('latitude')
APQ5 = st.text_input('le département')


Shimmer = st.text_input('nombre de piece')





modellgbm = pkl.load(open(url(r'model.pkl', 'rb'))                     



if classifier_name == 'RandomForestRegressor' :
                     
                    st.title('PREDICTION DES PRIX AVEC RANDOM')
                    if st.button("cliquez pour voir le prix"):
                        prediction_random = modellgbm.predict(
                            [[ fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer_dB,
                               APQ3, APQ5,Shimmer]])
                        st.success(prediction_random)

elif classifier_name == 'LGBMRegressor' :
    st.title('PREDICTION DES PRIX AVEC LGBM')
    if st.button("cliquez pour voir le prix"):
        prediction_random = modellgbm.predict(
            [[fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer_dB,
               APQ3, APQ5,Shimmer]])
        st.success(prediction_random)


else:
    st.title('PREDICTION DES PRIX AVEC XGBOOST')
    if st.button("cliquez pour voir le prix"):
        prediction_random = modellgbm.predict(
            [[fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer_dB,
               APQ3, APQ5,Shimmer]])
        st.success(prediction_random)





