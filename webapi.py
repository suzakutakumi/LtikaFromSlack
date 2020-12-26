from flask import Flask
app = Flask(__name__)
Lflg=False

@app.route("/H")
def High():
    global Lflg
    Lflg=True
    return "1"
@app.route("/L")
def Low():
    global Lflg
    Lflg=False
    return "1"

@app.route("/Stat")
def Stat():
    global Lflg
    return "H" if Lflg else "L"

if __name__ == "__main__":
    app.run(debug=False,host="0.0.0.0",port=8080)
