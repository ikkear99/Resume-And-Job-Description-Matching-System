from logging import error
from flask import jsonify
from flask import Flask, request
from flask_cors import CORS

import os

from process import process

import json

UPLOAD_FOLDER = 'uploaded_files'
if not os.path.exists(UPLOAD_FOLDER): os.makedirs(UPLOAD_FOLDER)

app = Flask(__name__)
cors = CORS(app, resources={r"/cv": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/cv', methods=['GET', 'POST'])
def all_cv():
    api_json = {}
    if request.method == 'POST':
        resume_dir = "web_app/server/data_test_matching/Resumes/"
        job_desc_dir = "web_app/server/data_test_matching/JobDesc/"

        # get data from form
        cv_data = request.files.getlist('cvFile')
        jd_data = request.files.getlist('jdFile')
        jd_index = int(request.form.get('jdIndex'))
        
        # extract all file in cv_data
        dir_name_cv = ""
        for file in cv_data:
            filename = file.filename
            filename = resume_dir + filename
            dir_name_cv = os.path.dirname(filename)
            print("=============================", dir_name_cv, "=========================================")

            if not os.path.exists(os.path.dirname(filename)):
                try:
                    os.makedirs(os.path.dirname(filename))
                except (error):
                    print(error)

            f = open(filename, 'wb')
            text = file.read()
            f.write(text)

        resume_dir = dir_name_cv + "/"
            

        # extract all file in jd_data
        dir_name_jd = ""
        for file in jd_data:
            filename = file.filename
            filename = job_desc_dir + filename
            dir_name_jd = os.path.dirname(filename)
            print("=============================", dir_name_jd, "=========================================")
            
            if not os.path.exists(os.path.dirname(filename)):
                try:
                    os.makedirs(os.path.dirname(filename))
                except (error):
                    print(error)

            f = open(filename, 'wb')
            text = file.read()
            f.write(text)

        job_desc_dir = dir_name_jd + "/"
    
        print("=============================", job_desc_dir, "=========================================")
        model_path = './model/model-1_best_version1.h5'

        # Compute score and get ranking of CVs
        result = process(resume_dir, job_desc_dir, model_path, jd_index)
        print("DOneeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        data_array = result.to_numpy()
        
        cv = []
        for item in data_array:
            cv_info = {
                'name': item[0],
                'sentences': item[1],
                'score': item[6],
                'ranking': item[7],
            }
            cv.append(cv_info)

        api_json['cv'] = cv

        with open('db.txt', 'w') as outfile:
            json.dump(api_json, outfile)
        
    with open('db.txt') as json_file:
        api_json = json.load(json_file)

    return jsonify(api_json)

# def create_dir(dir):
#     if not os.path.exists(dir):
#         os.makedirs(dir)
#     else:
#         print("Directory already existed : ", dir)
#     return dir


app.run("0.0.0.0", port=5000)
