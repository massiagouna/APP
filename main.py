import streamlit as st
import pandas as pd
import pickle as pkl
from streamlit_option_menu import option_menu




st.write('''
# App Simple pour la prévision des prix
Cette application prédit le prix de fleur
''')

st.sidebar.header("Les parametres d'entrée")

def user_input():


    MDVP_Fo=st.sidebar.slider('entrez la valeur1',-2,2,0)

    MDVP_Fhi=st.sidebar.slider('entrez la valeur2',-2,2,0)

    MDVP_Flo=st.sidebar.slider('entrez la valeur3',-2,2,0)

    MDVP_Jitter_1=st.sidebar.slider('entrez la valeur4',-2,2,0)
    MDVP_Jitter_2=st.sidebar.slider('entrez la valeur5',-2,2,0)

    MDVP_RAP=st.sidebar.slider('entrez la valeur6',-2,2,0)

    MDVP_PPQ=st.sidebar.slider('entrez la valeur7',-2,2,0)

    Jitter_DDP=st.sidebar.slider('entrez la valeur8',-2,2,0)

    MDVP_Shimmer=st.sidebar.slider('entrez la valeur9',-2,2,0)

    MDVP_Shimmer2=st.sidebar.slider('entrez la valeur10',-2,2,0)

    Shimmer_APQ3=st.sidebar.slider('entrez la valeur11',-2,20)

    Shimmer_APQ5=st.sidebar.slider('entrez la valeur12',-2,2,0)

    MDVP_APQ=st.sidebar.slider('entrez la valeur13',-2,2,0)

    Shimmer_DDA=st.sidebar.slider('entrez la valeur14',-1000,1000,0)

    NHR=st.sidebar.slider('entrez la valeur15',-1000,1000,0)

    HNR=st.sidebar.slider('entrez la valeur16',-1000,1000,0)

    RPDE=st.sidebar.slider('entrez la valeur17',-1000,1000,0)

    DFA=st.sidebar.slider('entrez la valeur18',-1000,1000,0)

    spread1=st.sidebar.slider('entrez la valeur19',-1000,1000,0)

    spread2=st.sidebar.slider('entrez la valeur20',-1000,1000,0)

    D2=st.sidebar.slider('entrez la valeur21',-1000,1000,0)

    PPE=st.sidebar.slider('entrez la valeur22',-1000,1000,0)


    data={

    'MDVP_Fo '  :  MDVP_Fo,
    'MDVP_Fhi'  :  MDVP_Fhi,
    'MDVP_Flo'  :  MDVP_Flo,
    'MDVP_Jitter_1 '  :  MDVP_Jitter_1,
    'MDVP_Jitter_2 ': MDVP_Jitter_2,
    'MDVP_RAP'      :   MDVP_RAP,
    'MDVP_PPQ'      :  MDVP_PPQ,
    'Jitter_DDP ': Jitter_DDP,

    'MDVP_Shimmer'   : MDVP_Shimmer,
    'MDVP_Shimmer2': MDVP_Shimmer2,
    'Shimmer_APQ3'  :  Shimmer_APQ3,
    'Shimmer_APQ5'  : Shimmer_APQ5,
    'MDVP_APQ '     :  MDVP_APQ,
    'Shimmer_DDA'  :  Shimmer_DDA,
    'NHR'         :   NHR,
    'HNR '        :   HNR,
    'RPDE '       :   RPDE,
    'DFA'         :   DFA,
    'spread1'        :   spread1,
    'spread2'        :   spread2,
    'D2'          :   D2,
    'PPE '        :   PPE
    }
    pred_parametres = pd.DataFrame(data, index=[0])
    return pred_parametres


daf=user_input()

st.subheader('on veut trouver la catégorie de cette fleur')
st.write(daf)
diabetes_model = pkl.load(open(r"C:\Users\HP\Downloads\projet_geek\web_app_ml_streamlit1-main\modelBS.pkl", 'rb') )

st.title('Heart Disease Prediction using ML')

col1, col2, col3 = st.columns(3)

with col1:
    age = st.text_input('Age')

with col2:
    sex = st.text_input('Sex')

with col3:
    cp = st.text_input('Chest Pain types')

with col1:
    trestbps = st.text_input('Resting Blood Pressure')

with col2:
    chol = st.text_input('Serum Cholestoral in mg/dl')

with col3:
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

with col1:
    restecg = st.text_input('Resting Electrocardiographic results')

with col2:
    thalach = st.text_input('Maximum Heart Rate achieved')

with col3:
    exang = st.text_input('Exercise Induced Angina')

with col1:
    oldpeak = st.text_input('ST depression induced by exercise')

with col2:
    slope = st.text_input('Slope of the peak exercise ST segment')

with col3:
    ca = st.text_input('Major vessels colored by flourosopy')

with col1:
    thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

