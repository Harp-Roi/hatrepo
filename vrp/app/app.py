#!/usr/bin/python3
import os
from flask import Flask, flash, request, redirect, url_for, render_template, jsonify
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './uploaded/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','html','vue','gz','log','py'])

LOG_FILE='log.txt'
ENTRY_POINT_HTML = 'upload.html'

def logf(log_text):
	f_log = open(LOG_FILE,'w')
	f_log.write(str(log_text))
	f_log.close()


app = Flask(__name__,static_url_path='')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'


@app.route('/main', methods=['GET', 'POST'])
def main():
    f = open(ENTRY_POINT_HTML,'r')
    r=f.read()
    f.close()
    return str(r)

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return 'hello'
 


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

from create_db import add_user,get_files,get_users,login_user,get_departments,add_department,flush


@app.route('/flush', methods=['GET', 'POST'])
def flush_rollback():
    flush()
    
@app.route('/list_files', methods=['GET', 'POST'])
def list_files():
    print(get_files(UPLOAD_FOLDER))
    return jsonify(get_files(UPLOAD_FOLDER))

@app.route('/list_users', methods=['GET', 'POST'])
def list_users():
    print(get_users())
    return jsonify(get_users())

@app.route('/list_departments', methods=['GET', 'POST'])
def list_departments():
    print(get_departments())
    return jsonify(get_departments())


@app.route('/post_department', methods=['GET', 'POST'])
def post_department():
    print(request.form['department_id'])
    add_department(request.form['department_id'])
    return redirect(url_for('successful_load') )


@app.route('/post_test', methods=['GET', 'POST'])
def post_test():
    print(request.form['email'])
    add_user(request.form['email'],request.form['password'])
    return redirect(url_for('successful_load') )

   
@app.route('/successful_load', methods=['GET', 'POST'])
def successful_load():
    f = open(ENTRY_POINT_HTML,'r')
    r=f.read()
    f.close()
    return '''
    <!doctype html>
    <title>Thank you. Update is complete.</title>
    <h1>Thank you. Update is complete.</h1>
    <a href="/main">Go Back to Main Page</a><hr>''' + str(r)
  
@app.route('/login', methods=['GET', 'POST'])
def login():
    print(login_user(request.form['email'],request.form['password']))
    return jsonify(login_user(request.form['email'],request.form['password']))

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    print(request.method)
    print(request.files.getlist('file'))
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file_list=request.files.getlist('file')
        print("file_list: " + str(file_list))
        for file in file_list:
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):    
                filename = secure_filename(file.filename)
                print(app.config['UPLOAD_FOLDER'])
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('successful_load'))
    return redirect(url_for('successful_load'))
