# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 22:38:00 2022

@author: user
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class model_input(BaseModel):
    
    fixedacidity : float
    volatileacidity : float
    citricacid : float
    residualsugar : float
    chlorides : float
    freesulfurdioxide : float
    totalsulfurdioxide : float
    density : float
    pH : float
    sulphates : float
    alcohol : float
    
#loading the saved model
wine_model = pickle.load(open("wine_trained_model_final.sav","rb")) 

@app.post('/wine_quality_prediction')
def wine_pred(input_parameters : model_input):
    input_data = input_parameters.json()
    input_directory = json.loads(input_data)
    
    fi_acid = input_directory['fixedacidity']
    vol_acid = input_directory['volatileacidity']
    cit_acid = input_directory['citricacid']
    res_sugar = input_directory['residualsugar']
    chl = input_directory['chlorides']
    fr_dio = input_directory['freesulfurdioxide']
    ts_dio = input_directory['totalsulfurdioxide']
    den = input_directory['density']
    ph = input_directory['pH']
    sulph = input_directory['sulphates']
    alc = input_directory['alcohol']
    
    input_list = [fi_acid, vol_acid, cit_acid, res_sugar, chl, fr_dio, ts_dio, den, ph, sulph, alc]
    
    prediction = wine_model.predict([input_list])

    if (prediction[0]==3):
        return 'Very Bad Quality Wine'
    elif(prediction[0]==4):
        return 'Bad Quality Wine'
    elif(prediction[0]==5):
        return 'Normal Quality wine'
    elif(prediction[0]==6):
        return 'Good Quality Wine'
    elif(prediction[0]==7):
        return 'Best Quality'
    elif(prediction[0]>=8):
        return 'Very Good Quality Wine'    
    