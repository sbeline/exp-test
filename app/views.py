from app import app
from flask import request, url_for, redirect, render_template
from flask_api.app import FlaskAPI


@app.route('/')
def home():
   return render_template('index.html')

if __name__ == "__main__":
      app.debug = True
      app.run()
