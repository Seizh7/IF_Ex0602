#!/usr/bin/env python3
# coding: utf8

# Fonctions importées
import streamlit as st
import json
import pandas as pd



# function to add to JSON
def read_json(filename):
    with open(filename, 'r') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
    return file_data

if __name__ == '__main__':
    st.title("Exercice 6.2")

    json_data = read_json("fr-esr-principaux-etablissements-enseignement-superieur.json")
    
    lat = []
    lon = []
    noms = []

    for item in json_data:
        if type(item['coordonnees']) == dict:
            noms.append(item['uo_lib'])
            lat.append(item['coordonnees']['lat'])
            lon.append(item['coordonnees']['lon'])

    map_data = pd.DataFrame({'ecoles' : noms, 'lat' : lat, 'lon' : lon})


    st.write("Principaux etablissements de l'enseignement superieur français")
    # affiche la carte
    st.map(map_data)
