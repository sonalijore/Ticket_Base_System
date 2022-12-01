from flask import Flask,render_template,request,redirect
import pymysql

app=Flask('__name__')  #creating an object of Flask class

@app.route('/')
def index():
    try:
        db=pymysql.connect(host="localhost", user="root",password="saijore@6132",database="train_info")
        cu=db.cursor()
        q="select * from train"
        cu.execute(q)
        data=cu.fetchall()
        return render_template('reservation.html',d=data) 
    except Exception as e:
        return "Error"
    

@app.route('/create' )
def create():
    return render_template('form.html')

@app.route('/store', methods=['POST'] )
def store():
    n=request.form['n']
    a=request.form['a']
    s=request.form['s']
    dst=request.form['dst']
    p=request.form['p']
    
    try:
        db=pymysql.connect(host="localhost", user="root",password="saijore@6132",database="train_info")
        cu=db.cursor()
        q="insert into train (NAME,AGE,SOURCE,DESTINATION,PRICE) values('{}','{}','{}','{}','{}')".format(n,a,s,dst,p)
        cu.execute(q)
        db.commit()
        return redirect('/')  
    except Exception as e:
               return "Error"
        
        
@app.route('/delete/<rid>')
def delete(rid):
        try:
            db=pymysql.connect(host="localhost", user="root",password="saijore@6132",database="train_info")
            cu=db.cursor()
            q="delete from train where Sr='{}'".format(rid)
            cu.execute(q)
            db.commit()
            return redirect('/')
        except Exception as e:
            return ("error")
                
@app.route('/edit/<rid>')
def edit(rid): 
    try:
        db=pymysql.connect(host="localhost", user="root",password="saijore@6132",database="train_info")
        cu=db.cursor()
        q="select * from train where Sr='{}'".format(rid)
        cu.execute(q)
        data=cu.fetchone()
        return render_template('editform.html',d=data) 
    except Exception as e:
        return "Error"
    
@app.route('/update/<rid>',methods=['POST'])
def update(rid): 
        un=request.form['n']
        ua=request.form['a']
        us=request.form['s']
        udst=request.form['dst']
        up=request.form['p']
        
        try:
            db=pymysql.connect(host="localhost", user="root", password="saijore@6132", database="train_info")
            cu=db.cursor()
            q="update train set name='{}',age='{}',source='{}',destination='{}',price='{}' where Sr='{}'".format(un,ua,us,udst,up,rid)
            cu.execute(q)
            db.commit()
            return redirect('/')

        except Exception as e:
            return("Error")
    
    
app.run(debug=True)

