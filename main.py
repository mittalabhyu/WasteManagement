# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:35:01 2020

@author: HP
"""

from flask import Flask, render_template,request,session,redirect
from flask_pymongo import PyMongo
from pymongo import MongoClient
from datetime import datetime




app = Flask(__name__)
client=MongoClient("mongodb+srv://mittalabhyu:Mittal@cluster0.ocodw.mongodb.net/wms?retryWrites=true&w=majority")
db=client.get_database('wms')

app.secret_key='super-secret-key'
@app.route("/")
def home():
    
   
    return render_template('index.html')
@app.route("/about")
def about():
    
   
    return render_template('about.html')
@app.route("/public")
def public():
    
   
    return render_template('public.html',flag=0,k5=[])
@app.route("/track", methods=['GET','POST'])
def track(): 
    if request.method=='POST':
        username=request.form.get('mobileno')
        qq=db.ward
        k5=list(qq.find({"mobile":username}))
        if(len(k5)!=0 ):
            
            return render_template('public.html',flag=1,k5=k5)
    return render_template('public.html',flag=0,k5=[])
    
@app.route("/complaint", methods=['GET','POST'])
def complaint(): 
    if request.method=='POST':
        name=request.form.get('username')
        email=request.form.get('email')
        ward=request.form.get('ward')
        mob=request.form.get('mobileno')
        city=request.form.get('city')
        img=request.form.get('file1')
        complain=request.form.get('Complain')
        status="Pending"
        date=datetime.now()
        dic={"name":name,"email":email,"city":city,"ward":ward,"mobile":mob,"complain":complain,"status":status,"image":img,"date":date}
        qq=db.ward
        qw=db.head
        dw={"ward":ward,"city":city}
        li=list(qw.find(dw))
        nn=li[0]["complains"]
        no=nn+1
        dq={"complains":no}
        qw.update_one({"complains":nn},{'$set':dq})
        qq.insert_one(dic)
            
        
    return render_template('public.html',flag=0,k5=[])
@app.route("/officials")
def officials():
    
    return render_template('official.html')
@app.route("/dashboard")
def dashboard():
    
   
    return render_template('login.html')
@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/dashboard')
@app.route("/logouth")
def logouth():
    session.pop('user')
    return redirect('/officials')
@app.route("/logoutw")
def logoutw():
    session.pop('user')
    return redirect('/officials')
@app.route("/login", methods=['GET','POST'])
def login(): 
    if request.method=='POST':
        username=request.form.get('uname')
        userpass=request.form.get('pass')
        if( username=="admin@up" and userpass == "Password@1"):
            session['user']=username
            rt=db.admin
            k3=list(rt.find())
            return render_template('dashboard.html',k3=k3)
    
    return render_template('login.html')
@app.route("/head", methods=['GET','POST'])
def loginhead(): 
    if request.method=='POST':
        username=request.form.get('uname')
        userpass=request.form.get('pass')
        aa=db.admin
        ab=db.head
        k1=list(aa.find({"email":username}))
        
        if( len(k1)!=0 and userpass == k1[0]["password"]):
            session['user']=username
            k3=list(ab.find({"city":k1[0]["city"]}))
            return render_template('head.html',k1=k1,k3=k3)
    
    return render_template('official.html')
@app.route("/ward", methods=['GET','POST'])
def loginward(): 
    if request.method=='POST':
        username=request.form.get('uname')
        userpass=request.form.get('pass')
        ab=db.head
        ac=db.ward
        k2=list(ab.find({"email":username}))
       
       
        if( len(k2)!=0 and userpass == k2[0]["password"]):
            session['user']=username
            hh={"city":k2[0]["city"],"ward":k2[0]["ward"]}
            k4=list(ac.find(hh))
            return render_template('ward.html',k2=k2,k4=k4)
    
    return render_template('official.html')
@app.route("/update", methods=['GET','POST'])
def update(): 
    ss=db.head
    sa=db.ward
    dw={"ward":ward,"city":city}
    li=list(qw.find(dw))
    nn=li[0]["complains"]
    no=nn+1
    dq={"complains":no}
    qw.update_one({"complains":nn},{'$set':dq})
    qq.insert_one(dic)
    return render_template('ward.html')


