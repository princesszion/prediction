import streamlit as st 
import pandas as pd
import numpy as np
from prediction import predict

st.title('Player Ratings')
st.markdown('Enter proposed values to predict player rating')

st.header('Player Features')
col1, col2, col3, col4 = st.columns(4)
with col1:
    movement_reactions = st.number_input('movement_reactions')
    mentality_composure = st.number_input('mentality_composure')
    passing   = st.number_input('passing')
    potential = st.number_input('potential')
    dribbling = st.number_input('dribbling')
    wage_eur = st.number_input('wage_eur')
    power_shot_power = st.number_input('power_shot_power')
    value_eur = st.number_input('value_eur')
    release_clause_eur = st.number_input('release_clause_eur')
    attacking_short_passing = st.number_input('attacking_short_passing')
    skill_long_passing = st.number_input('skill_long_passing')
with col2:
    rcm = st.number_input('rcm')
    #rs= st.number_input('rs')
    lcm = st.number_input('lcm')
    cm = st.number_input('cm')
    ram = st.number_input('ram')
    cam = st.number_input('cam')
    st = st.number_input('st')
    #rdm = st.number_input('rdm')
    #rdm = st.slider('rdm', 10, 50, 100)
with col3:
  #  cdm = st.number_input('cdm')
  #  ldm = st.number_input('ldm')
    lf = st.number_input('lf')
    cf = st.number_input('cf')
    lm = st.number_input('lm')
    rm = st.number_input('rm')
    rwb = st.number_input('rwb')
    lwb = st.number_input('lwb')
    rw = st.number_input('rw')
    lw = st.number_input('lw')

with col4:
    physic = st.number_input('physic')
    ls = st.number_input('ls')
    international_reputation = st.number_input('international_reputation')
    mentality_aggression = st.number_input('mentality_aggressionmentality_aggression')
    #dribbling = st.slider( 'dribbling',10, 50, 100)
    attacking_crossing = st.number_input('attacking_crossing')
    skill_ball_control = st.number_input('skill_ball_control')
    age = st.number_input('age')
    shooting = st.number_input('shooting')
    skill_curve = st.number_input('skill_curve')
    power_long_shots = st.number_input('power_long_shots')
    mentality_vision = st.number_input('mentality_vision')


    if st.button("Predict Player"):
        result = predict(np.array([[movement_reactions,
 mentality_composure,
 passing,
 potential,
 dribbling,
 wage_eur,
 power_shot_power,
 value_eur,
 release_clause_eur,
 mentality_vision,
 attacking_short_passing,
 skill_long_passing,
 physic,
 ls,
 international_reputation,
 skill_ball_control,
 age,
 shooting,
 skill_curve,
 power_long_shots,
 attacking_crossing,
 rcm,
 lcm,
 cm,
 ram,
 cam,
 st,
 #rs,
 #rdm,
 #cdm,
 #ldm,
 lf,
 cf,
 lm,
 rm,
 rwb,
 lwb,
 rw,
 lw,
 mentality_aggression]]))
        st.text(result[0])
