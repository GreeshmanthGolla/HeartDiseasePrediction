from flask import Flask, render_template, request,jsonify,app,url_for,redirect
import pickle
import numpy as np
import warnings

app = Flask(__name__)
#modl = pickle.load('modl.pkl','rb')
with open ('modl.pkl','rb') as file:
   modl=pickle.load(file)

@app.route('/')
def home():
   return render_template('index.html')
  
@app.route('/predict', methods=['POST','GET'])
def predict():
    # Get the feature values from the form
    
    print(request.form)
    int_features=[float(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=modl.predict(final)
    #output='(0:{1}f)'.format(prediction[0][1],2)
  
    

    # Make a prediction using the loaded model
   

    # Render the prediction result
    if(prediction==0):
    #return render_template('result.html', prediction=prediction)
     return render_template('resultfail.html',prediction=prediction);
     
    else :
       return render_template('resultsucess.html',prediction=prediction);
    
 
 

if __name__ == '__main__':
    app.run(debug=True)
