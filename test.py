import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict

st.title('Player Ratings')
st.markdown('Enter proposed values to predict player rating')

st.header('Player Features')
col1, col2 = st.columns(2)
with col1:
    movement_reactions = st.slider('movement_reactions', 10, 50, 100)
    mentality_composure = st.slider('mentality_composure', 10, 50, 100)
    passing   = st.slider('passing', 10, 50, 100)
    potential = st.slider('potential', 10, 50, 100)
    dribbling = st.slider( 'dribbling',10, 50, 100)
    wage_eur = st.slider('wage_eur', 10, 50, 100)
    power_shot_power = st.slider( 'power_shot_power',10, 50, 100)
    value_eur = st.slider('value_eur',10, 50, 100)
    release_clause_eur = st.slider('release_clause_eur', 10, 50, 100)
    attacking_short_passing = st.slider('attacking_short_passing', 10, 50, 100)
    skill_long_passing = st.slider('skill_long_passing', 10, 50, 100)
    rcm = st.slider('rcm', 10, 50, 100)
    lcm = st.slider('lcm', 10, 50, 100)
    cm = st.slider('cm', 10, 50, 100)
    ram = st.slider('ram', 10, 50, 100)
    cam = st.slider('cam', 10, 50, 100)
    st = st.slider('st', 10, 50, 100)
    rs = st.slider('rs', 10, 50, 100)
    rdm = st.slider('rdm', 10, 50, 100)
    cdm = st.slider('cdm', 10, 50, 100)
    ldm = st.slider('ldm', 10, 50, 100)
    lf = st.slider('lf', 10, 50, 100)
    cf = st.slider('cf', 10, 50, 100)
    lm = st.slider('lm', 10, 50, 100)
    rm = st.slider('rm', 10, 50, 100)
    rwb = st.slider('rwb', 10, 50, 100)
    lwb = st.slider('lwb', 10, 50, 100)
    rw = st.slider('rw', 10, 50, 100)
    lw = st.slider('lw', 10, 50, 100)


with col2:
    physic = st.slider('physic', 10, 50, 100)
    ls = st.slider('ls', 10, 50, 100)
    international_reputation = st.slider('international_reputation', 10, 50, 100)
    mentality_aggression = st.slider('mentality_aggression', 10, 50, 100)
    #dribbling = st.slider( 'dribbling',10, 50, 100)
    attacking_crossing = st.slider('attacking_crossing', 10, 50, 100)
    skill_ball_control = st.slider( 'skill_ball_control',10, 50, 100)
    age = st.slider('age',10, 50, 100)
    shooting = st.slider('shooting ', 10, 50, 100)
    skill_curve = st.slider('skill_curve', 10, 50, 100)
    power_long_shots = st.slider('power_long_shots', 10, 50, 100)
    mentality_vision = st.slider('mentality_vision', 10, 50, 100)


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
 rs,
 rdm,
 cdm,
 ldm,
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
