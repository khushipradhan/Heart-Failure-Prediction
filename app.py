
from flask import Flask,render_template,request
import pickle
import numpy as np
model=pickle.load(open('model.pkl','rb'))
app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict_heartfailure():
    anaemia=int(request.form.get('anaemia'))
    diabetes = int( request.form.get('diabetes'))
    ejection_fraction=int (request.form.get('ejection_fraction'))
    high_blood_pressure = int( request.form.get('high_blood_pressure'))
    serum_creatinine = float(request.form.get('serum_creatinine'))
    serum_sodium =int( request.form.get('serum_sodium'))
    sex = int(request.form.get('sex'))
    smoking = int(request.form.get('smoking'))
    time=int( request.form.get('time'))

    result=model.predict(np.array([ anaemia,diabetes,ejection_fraction,high_blood_pressure,serum_creatinine,serum_sodium,sex,smoking,time]).reshape(1,9))
    if result[0]==1:
        result='Heart Failure'
    else:
        result='No Heart Failure'
    return render_template('index.html',result=result )
app.run(debug=True)
if __name__== '__ main__':
    app.run(debug=True)