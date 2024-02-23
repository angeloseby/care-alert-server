
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from VItalDetection import heart_rate_stream,respiration_rate_stream,temperature_stream,spO2_stream


# Fetch the service account key JSON file contents
cred = credentials.Certificate('care-alert.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://care-alert-ef06f-default-rtdb.firebaseio.com"
})

ref = db.reference('/patients')

def sendAlert(pCode):
    ref.set({
        pCode:{
            'alert':True  
        }
    })
    print('Alert Sent')

