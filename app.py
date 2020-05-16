from flask import Flask, render_template, request
from pandas import read_csv
import matplotlib.pyplot as plt
from plotly.utils import PlotlyJSONEncoder
import bokeh
import json
import numpy as np
from io import StringIO

data = read_csv('./veri/covid.csv')
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hist():
  img = StringIO()
  x = data['country']
  y = data['cases']
  plt.plot(x,y)
  plt.savefig(img, format='png')
  plt.close()
  img.seek(0)
  plot_url = base64.b64encode(img.getvalue())
  return render_template('index.html', plot_url=plot_url)

@app.route('/')
def home():
  return render_template('index.html')

if __name__ == '__main__':
  app.run()
