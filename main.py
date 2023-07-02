from flask import Flask, jsonify
from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)

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
    data = collection.find()
    return dumps(data)


@app.route('/subjects', methods=['GET'])
def get_subjects():
    data = subjects_coll.find()
    return dumps(data)

@app.route('/exams', methods=['GET'])
def get_exams():
    data = exams_coll.find()
    return dumps(data)



@app.route('/student/<int:student_id>', methods=['GET'])
def get_student(student_id):
    print(student_id)
    student = collection.find_one({"id": student_id})
    if student:
        return dumps(student)
    else:
        return jsonify({"message": "Student not found."}), 404


if __name__ == '__main__':
    app.run()
