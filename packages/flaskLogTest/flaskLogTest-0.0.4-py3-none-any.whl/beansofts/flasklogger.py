import json
from lib2to3.pgen2 import token
import string
from textwrap import wrap
from traceback import print_tb
from flask import jsonify,request
from werkzeug.security import check_password_hash,generate_password_hash
import socket
import geocoder
import os
import pika
import time
import jwt
from functools import wraps
def channelInfo(usrInfo):
    #!/usr/bin/env python
    #establishig a connection
    # convertion of the data to string
    usrInfo=json.dumps(usrInfo)
    url = os.environ.get('CLOUDAMQP_URL', 'amqps://tnmldbri:STSB8LTzIx8PRW8sgaiAslc0iCocUvXe@puffin.rmq2.cloudamqp.com/tnmldbri')
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel() # start a channel
    channel.queue_declare(queue='leon') # Declare a queue
    channel.basic_publish(exchange='',
                        routing_key='hello',
                        body=usrInfo) #collection of data
    # print(" [x] Sent 'Hello World!'")
    connection.close()
    # authentiocation decroraor

def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        # token=request.args.get("token")
        header = request.headers.get('Authorization')
        _, token = header.split()
        # decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms='HS256')
        # print(decoded)
        if not token:
            return jsonify({'message':'denied'}),401#missing token
        try:
            data=jwt.decode(token.app.config['SECRET KEY'])
            print(data)
           
            # print(data)
        except:
            return jsonify({'message':'denied'}),401 #invalid token
        return "hello"
    return decorated













def registerUser(f):
    def wrapper(*args,**kwargs):
        if request.method=="POST":
            contents=request.get_json() #user data
            contents["datafield"]="register"
            #appending Keys
            contents["API_KEY"]="false"
            contents["SECRET_KEY"]="false"


            # acquire user ip adress
            ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
            # appending ip
            contents["ip"]=ip_addr
            contents['url']=request.host
            #user location
            location=geocoder.ip(ip_addr)
            city=location.city
            coordinates=location.latlng
            location=f"{city}-{coordinates}"
            contents["location"]=location
            channelInfo(contents)



            # print("hello")
            
        return "hello"
    return wrapper

        











# login decorator
def login(f):
    def login_wrapper(*args,**kwargs):
        loginCredentials=["password","username","password","phone number","email"]
        if request.method=="POST":
            contents=request.get_json()
            foundCredentials=[]
            for key,value in contents.items():
                if key in loginCredentials:
                    foundCredentials.append(key)
                if len(foundCredentials)==0:
                    return f" credentials requirend to login {loginCredentials}"
            # contents['url']=request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
            ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
            contents["ip"]=ip_addr
            contents['url']=request.host
            # time and confiruation
            from datetime import datetime,timezone,timedelta
            import re
            now = datetime.now(timezone.utc)
            current_time = now.strftime("%H:%M:%S")
            hours=int(current_time[:2])+3
            cur=re.sub(current_time[:2],str(hours),current_time)
            # print(hours)
            # print(type(current_time))
            # kenyan_time_diff=timedelta(hours=3)
            # datetime.time()
            # print(datetime.time())
            # datetime(now)+kenyan_time_diff
            # current_time+=kenyan_time_diff
            contents["log_tim"]=cur
            contents["datafield"]="logins"
            # print(cur)
            # print("hello martin")
            channelInfo(contents)
            # check very password
            return jsonify(contents)
            
            # return "hello world"

        return "login"
        

    return login_wrapper
def addKeys(f):
    def wrapper_key():
        if request.method=="POST":
            contents=request.get_json()
            contents['url']=request.host
            contents["datafield"]="apikey_add"
            
            #indentify the user
            SECRET_KEY='leonApllication'

            token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoibWFydGlubGVvbnRlY2gyM0BnbWFpbC5jb20iLCJleHAiOjE2NTczNjIyODh9.UEbaSzK0Q1nViYlX-ocHUejnlwVexNgM3z_ESPe1R0I"
            token=jwt.decode(token,SECRET_KEY)
            userEmail=token['user']
            # appending user data
            contents["user"]=userEmail

            # channeling user data
            channelInfo(contents)


            return jsonify(contents)
        
            

    return wrapper_key


            


            

