import pandas as pd
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/predict", methods=['POST'])
def predict():
    inp = request.form['input']
    #inp = "ALARM CLOCK BAKELIKE RED "
    input1 = "frozenset({'"+inp+"'})"
    data = pd.read_csv("Association_result_for_online_reatil_data.csv")
    data=data[['antecedents', 'consequents']]

    data_new = data[data['antecedents'] == input1]
    finallst = list(data_new['consequents'])
    final =[]
    for each in finallst:
        p1 = each[12:][:-3]
        if "," in p1:
            lss = p1.split(", ")
            for every in lss:
                if "'" in every:
                    re_in = every.index("'")
                    every =  every[:re_in] + every[re_in+1:]
                    every.replace("'","")
                final.append(every)
        else:    
            final.append(p1)
    print(list(set(final)))
    return {"result":list(set(final))}

if __name__=="__main__":
    app.run(debug=True)

