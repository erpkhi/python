from flask import Flask, jsonify, request,render_template , url_for , \
redirect, session
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'UserInfo'
app.config['MONGO_URI'] = 'mongodb://test:test@ds117878.mlab.com:17878/erpkhi'
mongo = PyMongo(app)

@app.route('/<page>', methods=['GET', 'POST'])
def index(page):
    return render_template("index.html",msg=page)
    # student = []
    # records = mongo.db.test.find()
    # for urecords in records:
    #     student.append({'name':urecords['names']})
    
    # return jsonify({'salni':student})
    # #return 'immi'
@app.route('/signin',methods=['GET', 'POST'] )
def index1():
    UserID=request.form["UserID"]
    password=request.form['password']
    msg=signins(UserID,password)
    #return msg
    return  render_template('index.html', msg=msg)
@app.route('/signup')
def signup():
    return render_template('signup.html')
# def signin():
#     msg='Invalid User or password'
#     chkuser=mongo.db.UserInfo
#     UserID=request.form["UserID"]
#     password=request.form['password']
#     #lst=[]
#     userIDPassword=chkuser.find({'UserID':UserID, 'pass':password})
#     for signInInfo  in userIDPassword:
#         if signInInfo['UserID']==UserID and signInInfo['pass']==password:
#             msg= UserID +' is log in '
#         else:
#             pass
            
#     return  render_template('index.html', msg=msg)

    #return jsonify({'salni':lst})
    #return userIDPassword[0]
    # if lst==userID:
    #     msg='You are log in '
    # else:
    #     msg='Invalid User or password'
    # return  render_template('index.html',msg=msg)


@app.route('/add', methods=['GET', 'POST'])
def add():

    # chkuser1=mongo.db.UserInfo
    # chkuser1.insert({'UserID':'zafar','pass':'1234'})
    # chkuser1.insert({'UserID':'Imran','pass':'123'})
    # chkuser1.insert({'UserID':'Asad','pass':'456'})
    
    return render_template('index.html',msg='user added') 

def signins(UserID,password):
    msg='Invalid User or password'
    chkuser=mongo.db.UserInfo
      
    userIDPassword=chkuser.find({'UserID':UserID, 'pass':password})
    for signInInfo  in userIDPassword:
        if signInInfo['UserID']==UserID:
            #if signInInfo['UserID']==UserID and signInInfo['pass']==password:
            if signInInfo['pass']==password:
                msg= UserID 
        else:
            msg='chaged again2'
            pass
               
    return msg      
    #return   render_template('index.html', msg=msg , msg1='sfsdfs')    

def userExist():
    return('ths is abc funtion')    

app.run(debug=True ,port=5000)
