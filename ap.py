
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 10:59:14 2020

@author: PRAYAG
"""

from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('carprice.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index1.html')

@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        symboling = int(request.form['symboling'])
        carheight=float(request.form['carheight'])
        wheelbase=float(request.form['wheelbase'])
        enginesize = int(request.form['enginesize'])
        boreratio=float(request.form['boreratio'])
        horsepower = int(request.form['horsepower'])
        carlength=float(request.form['carlength'])
        carwidth=float(request.form['carwidth'])
        peakrpm = int(request.form['peakrpm'])
        stroke=float(request.form['stroke'])
        doornumber=request.form['doornumber']
        if(doornumber=='two'):
            doornumber_two=1
        else:
            doornumber_two=0
        fueltype=request.form['fueltype']
        if(fueltype=='gas'):
            fueltype_gas=1
        else:
            fueltype_gas=0
        aspiration=request.form['aspiration']
        if(aspiration=='turbo'):
            aspiration_turbo=1
        else:
            aspiration_turbo=0
        carbody=request.form['carbody']
        if(carbody=='convertible'):
            carbody_hardtop=0
            carbody_hatchback=0
            carbody_sedan=0
            carbody_wagon=0
        elif(carbody=='hatchback'):
            carbody_hardtop=0
            carbody_hatchback=1
            carbody_sedan=0
            carbody_wagon=0
        elif(carbody=='sedan'):
             carbody_hardtop=0
             carbody_hatchback=0
             carbody_sedan=1
             carbody_wagon=0
        elif(carbody=='wagon'):
            carbody_hardtop=0
            carbody_hatchback=0
            carbody_sedan=0
            carbody_wagon=1   
        else:
            carbody_hardtop=1
            carbody_hatchback=0
            carbody_sedan=0
            carbody_wagon=0
        drivewheel=request.form['drivewheel']
        if(drivewheel=='rwd'):
             drivewheel_rwd=1
             drivewheel_fwd=0
        elif(drivewheel=='fwd'):
            drivewheel_rwd=0
            drivewheel_fwd=1
        else:
            drivewheel_rwd=0
            drivewheel_fwd=0
        cylindernumber=request.form['cylindernumber']
        if(cylindernumber=='five'):
            cylindernumber_five =1
            cylindernumber_four=0
            cylindernumber_six=0
            cylindernumber_three=0
            cylindernumber_twelve=0
            cylindernumber_two=0
        elif(cylindernumber=='four'):
            cylindernumber_five =0
            cylindernumber_four=1
            cylindernumber_six=0
            cylindernumber_three=0
            cylindernumber_twelve=0
            cylindernumber_two=0
        elif(cylindernumber=='six'):
            cylindernumber_five =0
            cylindernumber_four=0
            cylindernumber_six=1
            cylindernumber_three=0
            cylindernumber_twelve=0
            cylindernumber_two=0
        elif(cylindernumber=='three'):
            cylindernumber_five =0
            cylindernumber_four=0
            cylindernumber_six=0
            cylindernumber_three=1
            cylindernumber_twelve=0
            cylindernumber_two=0
        elif(cylindernumber=='twelve'):
            cylindernumber_five =0
            cylindernumber_four=0
            cylindernumber_six=0
            cylindernumber_three=0
            cylindernumber_twelve=1
            cylindernumber_two=0
        elif(cylindernumber=='two'):
            cylindernumber_five =0
            cylindernumber_four=0
            cylindernumber_six=0
            cylindernumber_three=0
            cylindernumber_twelve=0
            cylindernumber_two=1
        else:
            cylindernumber_five=0
            cylindernumber_four=0
            cylindernumber_six=0
            cylindernumber_three=0
            cylindernumber_twelve=0
            cylindernumber_two=0
        enginelocation=request.form['enginelocation']
        if(enginelocation=='rear'):
            enginelocation_rear=1
        else:
            enginelocation_rear=0
        fuelsystem=request.form['fuelsystem']
        if(fuelsystem=='2bbl'):
            fuelsystem_2bbl=1
            fuelsystem_4bbl=0
            fuelsystem_mpfi=0
            fuelsystem_mfi=0
            fuelsystem_spdi=0
            fuelsystem_spfi=0
            fuelsystem_idi=0
        elif(fuelsystem=='4bbl'):
            fuelsystem_2bbl=0
            fuelsystem_4bbl=1
            fuelsystem_mpfi=0
            fuelsystem_mfi=0
            fuelsystem_spdi=0
            fuelsystem_spfi=0
            fuelsystem_idi=0
        elif(fuelsystem=='mpfi'):
            fuelsystem_2bbl=0
            fuelsystem_4bbl=0
            fuelsystem_mpfi=1
            fuelsystem_mfi=0
            fuelsystem_spdi=0
            fuelsystem_spfi=0
            fuelsystem_idi=0
        elif(fuelsystem=='mfi'):
            fuelsystem_2bbl=0
            fuelsystem_4bbl=0
            fuelsystem_mpfi=0
            fuelsystem_mfi=1
            fuelsystem_spdi=0
            fuelsystem_spfi=0
            fuelsystem_idi=0
        elif(fuelsystem=='spdi'):
            fuelsystem_2bbl=0
            fuelsystem_4bbl=0
            fuelsystem_mpfi=0
            fuelsystem_mfi=0
            fuelsystem_spdi=1
            fuelsystem_spfi=0
            fuelsystem_idi=0
        elif(fuelsystem=='spfi'):
            fuelsystem_2bbl=0
            fuelsystem_4bbl=0
            fuelsystem_mpfi=0
            fuelsystem_mfi=0
            fuelsystem_spdi=0
            fuelsystem_spfi=1
            fuelsystem_idi=0
        elif(fuelsystem=='idi'):
            fuelsystem_2bbl=0
            fuelsystem_4bbl=0
            fuelsystem_mpfi=0
            fuelsystem_mfi=0
            fuelsystem_spdi=0
            fuelsystem_spfi=0
            fuelsystem_idi=1
        else:
            fuelsystem_2bbl=0
            fuelsystem_4bbl=0
            fuelsystem_mpfi=0
            fuelsystem_mfi=0
            fuelsystem_spdi=0
            fuelsystem_spfi=0
            fuelsystem_idi=0
        prediction=model.predict([[symboling,carheight,wheelbase,enginesize,boreratio,horsepower,carlength,carwidth,peakrpm,stroke,doornumber_two,fueltype_gas,aspiration_turbo,carbody_hardtop,carbody_hatchback,carbody_sedan,carbody_wagon,drivewheel_fwd,drivewheel_rwd,cylindernumber_five,cylindernumber_four,cylindernumber_six,cylindernumber_three,cylindernumber_twelve,cylindernumber_two,enginelocation_rear,fuelsystem_2bbl,fuelsystem_4bbl,fuelsystem_idi,fuelsystem_mfi,fuelsystem_mpfi,fuelsystem_spdi,fuelsystem_spfi]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index1.html',prediction_text="Sorry Incorrect input")
        else:
            return render_template('index1.html',prediction_text="Car Price is Rs. {}".format(output))
    else:
        return render_template('index1.html')

if __name__=="__main__":
    app.run(debug=True)

