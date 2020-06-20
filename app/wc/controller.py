
import os
from flask import Flask, Blueprint, render_template, request, send_file,send_from_directory
from app.wc.wd_cloud import image_wordcloud

mod_wc = Blueprint('wc', 'wc', url_prefix='/wc')
APP_ROOT=os.path.dirname(os.path.abspath(__file__))

@mod_wc.route('/upload',methods = ['GET', 'POST'])
def upload_file():
   return render_template('upload.html')
	
@mod_wc.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      filename=f.filename+".jpeg"
      target=os.path.join(APP_ROOT,'image')
      print(target)
      destination=os.path.join(target,filename)
      print(destination)
      image_wordcloud(str(f.getvalue()),destination)
      return render_template('index.html',image_name=filename)
        
@mod_wc.route('/index/<filename>')       
def index(filename):
    return send_from_directory("image",filename)

@mod_wc.route('/')
@mod_wc.route('/home')
def home_page():
    return render_template('index.html')