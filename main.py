# from boto3 import resources
# from flask import Flask, jsonify
# from pymongo import MongoClient
# from bson.json_util import dumps
# from flask_cors import CORS
#
# app = Flask(__name__)
#
# CORS(app)
# cors = CORS(app, resources={
#     r"/*" : {
#         "origins": "*"
#     }
# })
#
# # Establish a connection to MongoDB
# client = MongoClient("mongodb+srv://anupamsoni27:Mystuff8358%401@india-01.kwer3ek.mongodb.net/")
# db = client['students']
# collection = db['studentsList']
# subjects_coll = db['subjects']
# exams_coll = db["exams"]
#
#
# @app.route('/', methods=['GET'])
# def say_hello():
#     return jsonify({"m": "Welcome to student api"})
#
#
# @app.route('/students', methods=['GET'])
# def get_students():
#     data = collection.find()
#     return dumps(data)
#
#
# @app.route('/subjects', methods=['GET'])
# def get_subjects():
#     data = subjects_coll.find()
#     return dumps(data)
#
# @app.route('/exams', methods=['GET'])
# def get_exams():
#     data = exams_coll.find()
#     return dumps(data)
#
#
#
# @app.route('/student/<int:student_id>', methods=['GET'])
# def get_student(student_id):
#     print(student_id)
#     student = collection.find_one({"id": student_id})
#     if student:
#         return dumps(student)
#     else:
#         return jsonify({"message": "Student not found."}), 404
#
#
# if __name__ == '__main__':
#     app.run()


from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.json_util import dumps
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
cors = CORS(app, resources={
    r"/*" : {
        "origins": "*"
    }
})

# Establish a connection to MongoDB
client = MongoClient("mongodb+srv://anupamsoni27:Mystuff8358%401@india-01.kwer3ek.mongodb.net/")
db = client['students']
collection = db['studentsList']
subjects_coll = db['subjects']
exams_coll = db["exams"]

@app.route('/', methods=['GET'])
def say_hello():
    return jsonify({"m": "Welcome to student api"})

@app.route('/students', methods=['GET'])
def get_students():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    skip = (page - 1) * per_page

    data = collection.find().skip(skip).limit(per_page)
    return dumps(data)

@app.route('/subjects', methods=['GET'])
def get_subjects():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    skip = (page - 1) * per_page

    data = subjects_coll.find().skip(skip).limit(per_page)
    return dumps(data)

@app.route('/exams', methods=['GET'])
def get_exams():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    skip = (page - 1) * per_page

    data = exams_coll.find().skip(skip).limit(per_page)
    return dumps(data)

@app.route('/student/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = collection.find_one({"id": student_id})
    if student:
        return dumps(student)
    else:
        return jsonify({"message": "Student not found."}), 404

if __name__ == '__main__':
    app.run()
