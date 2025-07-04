from fastapi import FastAPI
import json

app = FastAPI()

def laod_data():
    with open('patients.json', 'r') as f:
       data =  json.load(f)

@app.get("/")
def create():
    return{'message':'Patient management api'}

@app.get("/about")
def about():
    return{'message':'A fully functional api to manage the patient records'}

@app.get("/view")
def view():
    data = laod_data()

    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str):
    data = laod_data()

    if patient_id in data:
         return data[patient_id]
    return {'error':'patient not found'}


