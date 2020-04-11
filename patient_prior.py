import pandas as pd

def calScore(name,age,gender,height,weight,spo2,heartrate,resprate,bodyt,cough,soret,breathdif,tiredness,pregnant,preexist):
    gender = gender.strip()
    pregnant = pregnant.strip()
    preexist = preexist.strip()
        
   
    body_mass_index = 0.0
    death_rate_age = 0.0
    bmi_weight = 0.0
    death_rate_gender = 0.0
    death_rate_heartrate = 0.0
    death_rate_resprate = 0.0

    if pregnant == "Yes":
        death_rate_preg=6.0
    else:
        death_rate_preg=0.0
    #print("The death_rate_preg is " + str(death_rate_preg))
        
    if preexist == "Yes":
        death_rate_preexisting=6.0
    else:
        death_rate_preexisting=0.0
    #print("The death_rate_preexisting is " + str(death_rate_preexisting))
    height = height * 0.393701
    weight = weight*2.20462
    body_mass_index = (weight * 703) / (height ** 2)
    if body_mass_index < 18.5:
        bmi_weight=.05
    elif body_mass_index < 24.9:
        bmi_weight=0
    elif body_mass_index > 25.0 and body_mass_index < 28.9:
        bmi_weight=.07
    elif body_mass_index > 28.9 and body_mass_index < 34.9:
        bmi_weight=.08
    elif body_mass_index > 34.9 and body_mass_index < 39.9:
        bmi_weight=.09
    else:
        bmi_weight=1.0
    #print("A person with a BMI of " + str(body_mass_index ))
    #print("The BMI weight is " + str(bmi_weight))
    if age < 9:
        death_rate_age=0.0
    elif age < 39:
        death_rate_age=1.0
    elif age < 49:
        death_rate_age=3.0
    elif age < 59:
        death_rate_age=3.0
    elif age < 69:
        death_rate_age=6.0
    elif age < 79:
        death_rate_age=7.0
    else:
        death_rate_age=10.0
    #print("The death_rate_age is " + str(death_rate_age))
    if gender == "Male":
        death_rate_gender=6.0
    else:
        death_rate_gender=4.0
    #print("The death_rate_gender is " + str(death_rate_gender))
    #athletes have heart rate of 40(implies good functioning of heart)
    #less than 40 is abnormal
    if heartrate < 40:
        death_rate_heartrate=5.0
    elif heartrate <60 and heartrate > 40:
        death_rate_heartrate=0.0
    elif heartrate > 60 and heartrate < 100 :
        death_rate_heartrate=0.0
    elif heartrate > 100 :
        death_rate_heartrate=5.0
    #print("The death_rate_heartrate is " + str(death_rate_heartrate))
    #given more imporance to respiratory rate
    if resprate < 10:
        death_rate_resprate=10.0
    elif resprate < 12:
        death_rate_resprate=9.0
    elif resprate > 12 and resprate < 20 :
        death_rate_resprate=0.0
    elif resprate > 20 and resprate < 25 :
        death_rate_resprate=5.0
    elif resprate > 25 and resprate < 27 :
        death_rate_resprate=9.0
    elif resprate > 27 :
        death_rate_resprate=10.0
        #print("The death_rate_resprate is " + str(death_rate_resprate))
    if spo2 < 90:
        death_rate_spo=7.0
    elif spo2 >90 and spo2 <100:
        death_rate_spo=0.0
    else:
        death_rate_spo=7.0
        #print("The death_rate_spo is " + str(death_rate_spo))
    if bodyt < 97:
        death_rate_temp=1.0
    elif bodyt >97 and bodyt <97.7:
        death_rate_temp=0.0
    elif bodyt >97.7 and bodyt <100.5:
        death_rate_temp=3.0
    else:
        death_rate_temp=6.0
        #print("The death_rate_temp is " + str(death_rate_temp))
    if cough == 0:
        death_rate_cough=0.0
    elif cough == 1:
        death_rate_cough=1.0
    elif cough == 2:
        death_rate_cough=2.0
    elif cough == 3:
        death_rate_cough=3.0
    elif cough == 4:
        death_rate_cough=4.0
    elif cough == 5:
        death_rate_cough=5.0
    elif cough == 6:
        death_rate_cough=6.0
    elif cough == 7:
        death_rate_cough=7.0
    elif cough == 8:
        death_rate_cough=8.0
    elif cough == 9:
        death_rate_cough=9.0
    else:
        death_rate_cough=10.0
        #print("The death_rate_cough is " + str(death_rate_cough))
    if soret == 0:
        death_rate_throat=0.0
    elif soret == 1:
        death_rate_throat=1.0
    elif soret == 2:
         death_rate_throat=2.0
    elif soret == 3:
        death_rate_throat=3.0
    elif soret == 4:
        death_rate_throat=4.0
    elif soret == 5:
        death_rate_throat=5.0
    elif soret == 6:
        death_rate_throat=6.0
    elif soret == 7:
        death_rate_throat=7.0
    elif soret == 8:
        death_rate_throat=8.0
    elif soret == 9:
        death_rate_throat=9.0
    else:
        death_rate_throat=10.0
    #print("The death_rate_throat is " + str(death_rate_throat))
    if breathdif == 0:
        death_rate_breath=0.0
    elif breathdif == 1:
        death_rate_breath=1.0
    elif breathdif == 2:
        death_rate_breath=2.0
    elif breathdif == 3:
        death_rate_breath=3.0
    elif breathdif == 4:
        death_rate_breath=4.0
    elif breathdif == 5:
        death_rate_breath=5.0
    elif breathdif == 6:
        death_rate_breath=6.0
    elif breathdif == 7:
        death_rate_breath=7.0
    elif breathdif == 8:
        death_rate_breath=8.0
    elif breathdif == 9:
        death_rate_breath=9.0
    else:
        death_rate_breath=10.0
    #print("The death_rate_breath is " + str(death_rate_breath))
    if tiredness == 0:
        death_rate_tired=0.0
    elif tiredness == 1:
        death_rate_tired=1.0
    elif tiredness == 2:
        death_rate_tired=2.0
    elif tiredness == 3:
        death_rate_tired=3.0
    elif tiredness == 4:
        death_rate_tired=4.0
    elif tiredness == 5:
        death_rate_tired=5.0
    elif tiredness == 6:
        death_rate_tired=6.0
    elif tiredness == 7:
        death_rate_tired=7.0
    elif tiredness == 8:
        death_rate_tired=8.0
    elif tiredness == 9:
        death_rate_tired=9.0
    else:
        death_rate_tired=10.0
    #print("The death_rate_tired is " + str(death_rate_tired))
    score = death_rate_tired+death_rate_breath+death_rate_throat+death_rate_cough+death_rate_temp+death_rate_spo+death_rate_resprate+death_rate_heartrate+death_rate_gender+death_rate_age+bmi_weight+death_rate_preexisting+death_rate_preg
    return score
