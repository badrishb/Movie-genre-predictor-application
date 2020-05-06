from flask import Flask,render_template,redirect,url_for,request,send_file,session
from forms import homef
from PIL import Image
import cgi
import numpy as np
from flask import g,request
import sqlite3

from PIL import ImageGrab 
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model,save_model

model=load_model('./genre_model(1)/genre_model')
out=''


app=Flask(__name__)
app.config['SECRET_KEY']='5791628bb0b13c6dfde280ba245'
img=[]

@app.route('/',methods=['GET','POST'])
def login():
    
    if(request.method=="POST" ):
        em=request.form['em']
        pwd=request.form['pwd']
        
        conn = sqlite3.connect('db/movie.db')
        temp=0
        x=conn.execute('''SELECT * from login ;''')
        for row in x:
            if(row[0]==em and row[1]==pwd):
                temp=1
                print(row)
            print(row[0]==em,row[1]==pwd)
        if(temp==1):
            session['username']=em
            session.modified=True
            print(session)
            
            return redirect(url_for('home'))
        
        return render_template('login-fail.html')
    else:
        if(not(session.get('username')==None)):
            print(session)
            print(session.get('username'))
            print("I'm in")
            return redirect(url_for('home'))
        
            
        return render_template("login-temp.html")
@app.route('/logout',methods=['GET','POST'])
def logout():
    session.pop('username',None)
    session.modified=True
    return redirect(url_for('login'))
@app.route('/register',methods=['GET','POST'])
def register():
    if(request.method=="POST" ):
        em=request.form['em']
        pwd=request.form['pwd']
        conn = sqlite3.connect('db/movie.db')
        x=conn.execute('''SELECT * from login ;''')
        temp=0
        for row in x:
            if(row[0]==em and row[1]==pwd):
                temp=1
                print(row)
            print(row[0]==em,row[1]==pwd)
        if(temp==1):
            return redirect(url_for('register'))
        else:
            conn.execute(
            f"INSERT INTO login VALUES ( '{em}', '{pwd}')")
            conn.commit()
            temp=0
            return redirect(url_for('login'))
    else:
        return render_template("register.html")

@app.route('/home',methods=['GET','POST'])
def home():
    # return "Welcome to my home page"
    form=homef()
    if form.validate_on_submit():
        
        filename = secure_filename(form.photo.data.filename)
        form.photo.data.save('./images/'+filename)
        global img
        img=Image.open('./images/'+filename)
        
        classes=[ 'Action', 'Adventure', 'Animation', 'Biography',
       'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy',
       'History', 'Horror', 'Music', 'Musical', 'Mystery', 'N/A', 'News',
       'Reality-TV', 'Romance', 'Sci-Fi', 'Short', 'Sport', 'Thriller', 'War',
       'Western']
  
        img=img.resize((350,350))
        img.show()
        img=np.asarray(img,dtype=np.float32)
        img=img/255
        img=img.reshape(1,350,350,3)
        print(img.shape)

        yp=model.predict(img)
        yp=np.array(yp)
        top3=(np.argsort(yp).reshape(-1,1))[::-1]
        top3=top3[:5]
        global out
        # out=str(classes)+str(yp)
        out=classes[top3[0][0]]+' '+classes[top3[1][0]]+' '+classes[top3[2][0]]+' '+classes[top3[3][0]] +' '+classes[top3[4][0]]
        print(top3)
  
        
        return redirect(url_for('success'))
    else:
        print(form.validate_on_submit())
        return render_template("home.html",form=form)
@app.route('/success',methods=['GET'])
def  success():
    global out
    return render_template("resp.html",value=out)

if __name__ =='__main__':
    
    img=Image
    app.run(port=5000,threaded=False,debug=True)
