#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import pandas as pd
import flask as Flask
from flask import request
from flask import render_template
import pickle


# In[12]:


from flask import Flask

app = Flask(__name__)


# In[13]:


@app.route('/')
def home():
    return render_template('InsuranceModel.html')


# In[14]:


# prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,1)
    loaded_model = pickle.load(open("insurance_flask.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    print(result[0])
    return result[0]


# In[16]:


@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)
        if int(result) == 0:
            prediction = 'Person will not buy insurance!!!'
        else:
            prediction = 'Person will buy insurance!!!'
        return render_template("result.html", prediction = prediction)


# In[17]:


# Main function
if __name__ == "__main__":
    app.run(debug=True)
    app.config['TEMPLATES_AUTO_RELOADED'] = True

