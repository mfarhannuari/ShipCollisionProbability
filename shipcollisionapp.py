import pickle

import numpy as np
import streamlit as st

st.title("Ship Collision Probability Prediction app")
model = pickle.load(open("model.pkl", "rb"))

Daylight = st.number_input("Daylight")
Inexperience = st.number_input("Inexperience")
NumberOfCrew = st.number_input("NumberOfCrew")
UnderstandingOfShipCharacteristic = st.number_input("UnderstandingOfShipCharacteristic")
UnderstandingOfWaterCondition = st.number_input("UnderstandingOfWaterCondition")
DualTask = st.number_input("DualTask")
VisualObservation = st.number_input("VisualObservation")
Master = st.number_input("Master")
ShipCommunication = st.number_input("ShipCommunication")
Pilot = st.number_input("Pilot")
CrewCompetence = st.number_input("CrewCompetence")
Uncertain = st.number_input("Uncertain")
Fatigue = st.number_input("Fatigue")
CrewHealth = st.number_input("CrewHealth")
NavcomEquipment = st.number_input("NavcomEquipment")
NavcomUtilized = st.number_input("NavcomUtilized")
UnderstandingofNavcomSign = st.number_input("UnderstandingofNavcomSign")
Manuveurability = st.number_imput("Manuveurability")
DecisionMaking = st.number_input("DecisionMaking")
GoodSeamanship = st.number_input("GoodSeamanship")
PreventiveTiming = st.number_input("PreventiveTiming")
TechnicalFailure = st.number_input("TechnicalFailure")
btn = st.button("predict")

if btn:
    pred = model.predict(np.array([Daylight,Inexperience,NumberOfCrew,UnderstandingOfShipCharacteristic,UnderstandingOfWaterCondition,DualTask,VisualObservation,Master,ShipCommunication,Pilot,CrewCompetence,Uncertain,Fatigue,CrewHealth,NavcomEquipment,NavcomUtilized,UnderstandingOfNavcomSign,Manuveurability,DecisionMaking,GoodSeamanship,PreventiveTiming,TechnicalFailure]).reshape(1,0))
    st.write(f"Your Ship will have: {pred}" )