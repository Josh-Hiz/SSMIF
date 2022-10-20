import pandas as pd 
from pandas import DataFrame
from flask import Flask, render_template

netflix = pd.read_csv("netflix.csv")

app = Flask(__name__)

df = pd.read_csv('netflix.csv')
df.to_csv('netflix.csv', index=None)

@app.route('/')
@app.route('/table')
def table():
    
    #Convert to html
    return render_template('table.html', tables=[netflix.to_html()], titles=[''])

if __name__ == "__main__":
    
    app.run(host="localhost", port=int("5050"))