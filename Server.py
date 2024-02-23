
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db



# Fetch the service account key JSON file contents
cred = credentials.Certificate('care-alert.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://care-alert-ef06f-default-rtdb.firebaseio.com"
})

ref = db.reference('/patients')

def setAlert(pCode):
    ref.set({
        pCode:{
            'alert':False
        }
    })

def setVitals(pCode):
    ref.set({
        pCode:{
            'heart-rate':0,
            'spo2':0,
            'breathRate':0,
            'temperature':0,
        }
    })

def sendAlert(pCode):
    ref.update({
        pCode:{
            'alert':True  
        }
    })
    print('Alert Sent')

def sendVitals(pCode,heartRate,spo2,breathRate,temperature):
    ref.update(
        {
            pCode:{
                'heart-rate':heartRate,
                'spo2':spo2,
                'breathRate':breathRate,
                'temperature':temperature,
            }
        }
    )