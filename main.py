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
import re

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
questions_coll = db["questions"]
categories_coll = db["categories"]

@app.route('/', methods=['GET'])
def say_hello():
    return jsonify({"m": "Welcome to student api"})


# @app.route('/questions', methods=['GET'])
# def get_questions():
#     page = int(request.args.get('page', 1))
#     per_page = int(request.args.get('per_page', 10))
#     skip = (page - 1) * per_page
#
#     data = questions_coll.find({"course": "MPPSC"}).skip(skip).limit(per_page)
#     return dumps(data)


@app.route('/subjects', methods=['GET'])
def get_subjects():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    skip = (page - 1) * per_page

    data = subjects_coll.find().skip(skip).limit(per_page)
    return dumps(data)


@app.route('/categories', methods=['GET'])
def get_categories():
    data = categories_coll.find()
    return dumps(data)


@app.route('/exams', methods=['GET'])
def get_exams():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    skip = (page - 1) * per_page

    data = exams_coll.find().skip(skip).limit(per_page)
    return dumps(data)


@app.route('/getQuestionsByExamId/<string:exam_id>', methods=['GET'])
def get_questions_for_exam_id(exam_id):
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    skip = (page - 1) * per_page

    data = questions_coll.find({"exam_id": exam_id}).skip(skip).limit(per_page)
    return dumps(data)


@app.route('/student/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = collection.find_one({"id": student_id})
    if student:
        return dumps(student)
    else:
        return jsonify({"message": "Student not found."}), 404


@app.route('/questions/<int:questions_id>', methods=['GET'])
def get_question_for_id(questions_id):
    question = questions_coll.find_one({"id": questions_id})
    if question:
        return dumps(question)
    else:
        return jsonify({"message": "Question not found."}), 404


@app.route('/questions', methods=['POST'])  # Change method to POST for search requests
def get_questions():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    skip = (page - 1) * per_page

    # Get the search data from the request payload using request.get_json(force=True)
    data = request.get_json(force=True)

    # Check if the data is a dictionary and contains the "data" key
    if not isinstance(data, dict) or "data" not in data:
        return jsonify({"message": "Invalid request payload. 'data' key is missing."}), 400

    # Create a filter based on the search data
    search_filter = {}
    for item in data["data"]:
        prop_name = item["propertyName"]
        value = item["value"]

        # Use regex to perform a case-insensitive search for tags and globalConcept
        if prop_name in ["tags", "globalConcept"]:
            search_filter[prop_name] = {"$regex": re.compile(value, re.IGNORECASE)}
        else:
            search_filter[prop_name] = value

    # Use the search filter in the find query
    data = questions_coll.find(search_filter).skip(skip).limit(per_page)

    return dumps(data)


if __name__ == '__main__':
    app.run()
