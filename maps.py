import streamlit as st
import pandas as pd

st.title("Addis Abeba Inistitute of Technology GIS Assignemnt ")
st.title("Abel Tadesse ATE 1359 11 ")
point = st.selectbox("Select Map Point ", ('Meskel Square', 'Addis Abeba Stadium', 'Mexico','Elilly Hotel','hyatt Regency', 'Gihon Hotel', 'Dembel City Center','Flamingo', 'Ahadu Bank Main Branch'))
if point == 'Meskel Square':
    coordinate = pd.DataFrame(
        {
    'lat':[9.01029],
     'lon': [38.76142]}

    )
    st.map(coordinate, zoom=15.2)
elif point == ('Addis Abeba Stadium'):
    coordinate = pd.DataFrame(
        {
    'lat':[9.01373],
     'lon': [38.75627]}

    )
    st.map(coordinate, zoom=15.2)
elif point == ('Mexico'):
    coordinate = pd.DataFrame(
        {
    'lat':[9.01034],
     'lon': [38.74605]}

    )
    st.map(coordinate, zoom=15.2)
elif point == ('Elilly Hotel'):
    coordinate = pd.DataFrame(
        {
    'lat':[9.01483

],
     'lon': [38.76893

]}
    )
    st.map(coordinate, zoom=15.2)
elif point == ('hyatt Regency'):
    coordinate = pd.DataFrame(
        {
    'lat':[9.01004],
     'lon': [38.76403]}
    )
    st.map(coordinate, zoom=15.2)
elif point == ('Gihon Hotel'):
    coordinate = pd.DataFrame(
        {
    'lat':[9.01407
],
     'lon': [38.76004
]}
    )
    st.map(coordinate, zoom=15.2)
elif point == ('Dembel City Center'):
    coordinate = pd.DataFrame(
        {
    'lat':[9.00516
],
     'lon': [38.76738
]}
    )
    st.map(coordinate, zoom=15.2)
elif point == ('Flamingo'):
    coordinate = pd.DataFrame(
        {
    'lat':[9.00897
],
     'lon': [38.76422
]}
    )
    st.map(coordinate, zoom=15.2)
elif point == ('Ahadu Bank Main Branch'):
    coordinate = pd.DataFrame(
        {
    'lat':[9.00911
],
     'lon': [38.76477
]}
    )
    st.map(coordinate, zoom=15.2)
elif point == (''):
    coordinate = pd.DataFrame(
        {
    'lat':[],
     'lon': []}
    )
    st.map(coordinate, zoom=15.2)
else:
    coordinate = pd.DataFrame(
        {
    'lat':[9.01029],
     'lon': [38.76142]}

    )
    st.map(coordinate, zoom=15.2)
