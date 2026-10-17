'''7. Explore the ‘Flask’ module and create a web server using Flask & Python.    '''

# S1] go to https://flask.palletsprojects.com/en/stable/ (or search flask module)
# S2} select A minimal Application under Quickstart (Scroll & find) :
# s3] copy paste that code

from flask import Flask  # type: ignore[reportMissingImports]

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#use $ flask --app hello run tp tun the app where app is the app.py name here use 
# flask --app 07_problem7 run
#or simply use 
# app.run()

#I USED THIS & THE CMD PROMPT OP:-
# PS C:\Users\Hello\OneDrive\Desktop\Skills++\PythonTechStack\chapter 13_AdvPython2\Practice set> flask --app 07_problem7 run
#  * Ignoring a call to 'app.run()' that would block the current 'flask' CLI command.
#    Only call 'app.run()' in an 'if __name__ == "__main__"' guard.
#  * Serving Flask app '07_problem7'
#  * Debug mode: off
# WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
#  * Running on http://127.0.0.1:5000
# Press CTRL+C to quit