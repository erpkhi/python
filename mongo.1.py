from flask import Flask, jsonify, request,render_template , url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("member.html")
   
app.run(debug=True ,port=5000)
