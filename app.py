from flask import Flask,render_template,redirect,request
import pandas as pd
from patient_prior import *
import speech_recognition as sr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/patientPrioritizer')
def patientPrioritizer():
    return render_template("Patient Prioritizer.html")
    
@app.route('/editPatient',methods=["GET","POST"])
def editPatient():
    if request.method == "POST":
        name = request.form.get("inp_name")
        age = request.form.get("age")
        gender = request.form.get("gender")
        height = request.form.get("height")
        weight = request.form.get("weight")
        spo2 = request.form.get("spo2")
        heartrate = request.form.get("heart")
        resprate = request.form.get("resp")
        bodyt = request.form.get("body")
        cough = request.form.get("cough")
        soret = request.form.get("sore")
        breathdif = request.form.get("breath")
        tiredness = request.form.get("tiredness")
        pregnant = request.form.get("pregnant")
        preexist = request.form.get("preex")

        height = float(height)
        weight = float(weight)
        heightOrig = height
        weightOrig = weight
        age = int(age)
        heartrate = int(heartrate)
        resprate = int(resprate)
        spo2 = float(spo2)
        bodyt = float(bodyt)
        cough = int(cough)
        soret = int(soret)
        tiredness = int(tiredness)
        breathdif = int(breathdif)
        
        score = calScore(name,age,gender,height,weight,spo2,heartrate,resprate,bodyt,cough,soret,breathdif,tiredness,pregnant,preexist)        

        data = [[name,age,gender,heightOrig,weightOrig,heartrate,resprate,spo2,bodyt,cough,soret,breathdif,tiredness,pregnant,preexist,score]] 

        
        df_orig = pd.read_csv('data.csv')
        df_new = pd.DataFrame(data,columns=df_orig.columns)
        
        df_orig.drop(df_orig[df_orig['name'] == data[0][0]].index, inplace = True)

        df_latest = df_orig.append(df_new)
        #raise Exception(df_latest)
        #raise Exception(name,age,gender,height,weight,spo2,heartrate,resprate,bodyt,cough,soret,breathdif,tiredness,pregnant, preexist,score)
        df_latest.to_csv('data.csv', header=True,index=False)
        return render_template("Patient Prioritizer.html")
        
    else:
        return render_template("edit.html")
@app.route('/searchPatient',methods=["GET", "POST"])
def searchPatient():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        age = int(age)
        name = name.strip()
        name = name.lower()
      
    
        df = pd.read_csv('data.csv')
      
        df["name_match"] = None
       
        for i in df.index:
            name_orignal = df.loc[i]["name"]
            df.iloc[i:i+1,16:17] = name_orignal.lower()
     
        dat = df[(df["name_match"]==name) & (df["age"]==age)]
       
        dat.drop(["name_match"],axis=1,inplace=True)
        dat.reset_index(drop=True)
        df.drop(["name_match"],axis=1,inplace=True)
        result_pt = dat.to_dict(orient='records')
        if len(result_pt)==0:
            return render_template("noRes.html")

        result_pt_send = result_pt[0]
        result_pt_send["Height"] = result_pt_send["Height (cm)"]
        del result_pt_send["Height (cm)"]
        result_pt_send["Weight"] = result_pt_send["Weight (kg)"]
        del result_pt_send["Weight (kg)"]
        result_pt_send["Resp"] = result_pt_send["Respiratory Rate "]
        del result_pt_send["Respiratory Rate "]
        result_pt_send["Spo2"] = result_pt_send["SPO2 (%age)"]
        del result_pt_send["SPO2 (%age)"]
        result_pt_send["Sore"] = result_pt_send["Sore Throat"]
        del result_pt_send["Sore Throat"]
        result_pt_send["Breath"] = result_pt_send["Breathing difficulty"]
        del result_pt_send["Breathing difficulty"]
        result_pt_send["preex"] = result_pt_send["Pre-existing Condition"]
        del result_pt_send["Pre-existing Condition"]
        result_pt_send["Body"] = result_pt_send["Body temp"]
        del result_pt_send["Body temp"]
        result_pt_send["Heart"] = result_pt_send["Heart Rate (bpm)"]
        del result_pt_send["Heart Rate (bpm)"]
        #raise Exception(result_pt_send)
        return render_template("edit.html",result_pt_send = result_pt_send)
    else:
        return render_template("searchPatient.html")


@app.route('/addPatient',methods=["GET", "POST"])
def addPatient():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        gender = request.form.get("gender")
        height = request.form.get("height")
        weight = request.form.get("weight")
        spo2 = request.form.get("spo2")
        heartrate = request.form.get("heartrate")
        resprate = request.form.get("resprate")
        bodyt = request.form.get("bodyt")
        cough = request.form.get("cough")
        soret = request.form.get("soreth")
        breathdif = request.form.get("breatheDif")
        tiredness = request.form.get("tiredness")
        pregnant = request.form.get("pregnant")
        preexist = request.form.get("preexist")

        #following code calculates score
        height = float(height)
        weight = float(weight)
        heightOrig = height
        weightOrig = weight
        age = int(age)
        heartrate = int(heartrate)
        resprate = int(resprate)
        spo2 = float(spo2)
        bodyt = float(bodyt)
        cough = int(cough)
        soret = int(soret)
        tiredness = int(tiredness)
        breathdif = int(breathdif)
        

        score = calScore(name,age,gender,height,weight,spo2,heartrate,resprate,bodyt,cough,soret,breathdif,tiredness,pregnant,preexist)
        
        #following part enters the data into database
        
        
        data = [[name,age,gender,heightOrig,weightOrig,heartrate,resprate,spo2,bodyt,cough,soret,breathdif,tiredness,pregnant,preexist,score]] 
        df = pd.DataFrame(data)
        df.to_csv('data.csv', mode='a', header=False,index=False)
        return render_template("Patient Prioritizer.html")
    else:
        return render_template("Add Patient.html")

@app.route('/viewPatients')
def viewPatients():
    res = pd.read_csv('data.csv')
    res_s = res.sort_values('Score',ascending = False)
    res_s = res_s.reset_index(drop=True)
    final = res_s[['name','Score']].to_dict(orient='records')
    length = len(final)
    return render_template("View Patients.html",final=final,length=length)

if __name__ == "__main__":
    app.run(debug=True)
