import flask
from flask import Flask, request, render_template, redirect
import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]

Credentials = ServiceAccountCredentials.from_json_keyfile_name(r"claves.json", scope)
cliente = gspread.authorize(Credentials)

sheet = cliente.open("Estacionamientos Database").sheet1
x = sheet.acell("A1").value
x = int(x)
print(x)



app = Flask(__name__)   


@app.route('/')
def inicio():
    while True:
        x = sheet.acell("A1").value
        x = int(x)
        print(x)
            
        if x==1:
            print(0)
        else:
            print(1)    

        return render_template("index.html", x=x)
        time.sleep(3)

@app.route("/Home")
def Home():
    return redirect("/")

@app.route("/SectorA")
def A():
    while True:
        x = sheet.acell("A1").value
        x = int(x)
        print(x)
            
        if x==1:
            print(0)
        else:
            print(1)    

        return render_template("A.html", x=x)
        time.sleep(3)

@app.route("/SectorB")
def B():
    return render_template("B.html")

@app.route("/SectorC")
def C():
    return render_template("C.html")

@app.route("/SectorD")
def D():
    return render_template("D.html")

@app.route("/SectorE")
def E():
    return render_template("E.html")    

@app.route("/SectorF")
def F():
    return render_template("F.html")    

if __name__ == '__main__':
    app.run(debug=True)

