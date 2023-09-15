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
from flask import Flask, jsonify, request, session
from pymongo import MongoClient
from bson.json_util import dumps
from flask_cors import CORS
import bcrypt
import jwt
import datetime

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
users_coll = db['users']
filter_coll = db['filter']

# JWT secret key (you should change this to a more secure value)
JWT_SECRET_KEY = "1234567890"


# Helper function to validate JWT token
def validate_token(token):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return {"message": "Token has expired"}, 401
    except jwt.InvalidTokenError:
        return {"message": "Invalid token"}, 401


@app.route('/', methods=['GET'])
def say_hello():
    # Get the JWT token from the request headers
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"message": "Authorization token required"}), 401

    # Validate the token
    payload = validate_token(token)
    if "message" in payload:
        return jsonify(payload), 401

    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    skip = (page - 1) * per_page

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
    # Get the JWT token from the request headers
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"message": "Authorization token required"}), 401

    # Validate the token
    payload = validate_token(token)
    if "message" in payload:
        return jsonify(payload), 401

    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    skip = (page - 1) * per_page

    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    skip = (page - 1) * per_page

    data = subjects_coll.find().skip(skip).limit(per_page)
    return dumps(data)


@app.route('/categories', methods=['GET'])
def get_categories():
    # Get the JWT token from the request headers
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"message": "Authorization token required"}), 401

    # Validate the token
    payload = validate_token(token)
    if "message" in payload:
        return jsonify(payload), 401

    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    skip = (page - 1) * per_page

    data = categories_coll.find()
    return dumps(data)


@app.route('/exams', methods=['GET'])
def get_exams():
    # Get the JWT token from the request headers
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"message": "Authorization token required"}), 401

    # Validate the token
    payload = validate_token(token)
    if "message" in payload:
        return jsonify(payload), 401

    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    skip = (page - 1) * per_page

    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    skip = (page - 1) * per_page

    data = exams_coll.find().skip(skip).limit(per_page)
    return dumps(data)


@app.route('/getQuestionsByExamId/<string:exam_id>', methods=['GET'])
def get_questions_for_exam_id(exam_id):
    # Get the JWT token from the request headers
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"message": "Authorization token required"}), 401

    # Validate the token
    payload = validate_token(token)
    if "message" in payload:
        return jsonify(payload), 401

    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    skip = (page - 1) * per_page

    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    skip = (page - 1) * per_page

    data = questions_coll.find({"exam_id": exam_id}).skip(skip).limit(per_page)
    return dumps(data)


@app.route('/student/<int:student_id>', methods=['GET'])
def get_student(student_id):
    # Get the JWT token from the request headers
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"message": "Authorization token required"}), 401

    # Validate the token
    payload = validate_token(token)
    if "message" in payload:
        return jsonify(payload), 401

    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    skip = (page - 1) * per_page

    student = collection.find_one({"id": student_id})
    if student:
        return dumps(student)
    else:
        return jsonify({"message": "Student not found."}), 404


@app.route('/questions/<int:questions_id>', methods=['GET'])
def get_question_for_id(questions_id):
    # Get the JWT token from the request headers
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"message": "Authorization token required"}), 401

    # Validate the token
    payload = validate_token(token)
    if "message" in payload:
        return jsonify(payload), 401

    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    skip = (page - 1) * per_page

    question = questions_coll.find_one({"id": questions_id})
    if question:
        return dumps(question)
    else:
        return jsonify({"message": "Question not found."}), 404


@app.route('/questions', methods=['POST'])  # Change method to POST for search requests
def get_questions():
    # Get the JWT token from the request headers
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"message": "Authorization token required"}), 401

    # Validate the token
    payload = validate_token(token)
    if "message" in payload:
        return jsonify(payload), 401

    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    skip = (page - 1) * per_page

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
        elif prop_name == "search_term":
            search_filter["en.value"] = {"$regex": re.compile(value, re.IGNORECASE)}
        else:
            search_filter[prop_name] = value

    # Use the search filter in the find query
    data = questions_coll.find(search_filter).skip(skip).limit(per_page)

    return dumps(data)


@app.route('/filters', methods=['POST'])  # Change method to POST for search requests
def get_filters():
    # Get the JWT token from the request headers
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"message": "Authorization token required"}), 401

    # Validate the token
    payload = validate_token(token)
    if "message" in payload:
        return jsonify(payload), 401

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
        elif prop_name == "search_term":
            search_filter["en.value"] = {"$regex": re.compile(value, re.IGNORECASE)}
        else:
            search_filter[prop_name] = value

    # Use the search filter in the find query
    data = filter_coll.find({})

    return dumps(data)


# User Signup
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check if the username already exists in the database
    if users_coll.find_one({'username': username}):
        return jsonify({"message": "Username already exists"}), 400

    # Hash the password before storing it in the database
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Insert the new user into the users collection
    users_coll.insert_one({'username': username, 'password': hashed_password})

    return jsonify({"message": "User registered successfully"}), 201


# User Login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Retrieve the user from the database based on the given username
    user = users_coll.find_one({'username': username})

    if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
        # Generate JWT token with 2-day validity
        token = jwt.encode({'username': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(days=2)},
                           JWT_SECRET_KEY, algorithm='HS256')
        return jsonify({"message": "Login successful", "token": token}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401


if __name__ == '__main__':
    app.run()
