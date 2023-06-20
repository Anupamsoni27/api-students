from flask import Flask, jsonify, request

app = Flask(__name__)


# Fake student data
students = [
    {
        "id": "1001",
        "name": "Alice Smith",
        "age": 17,
        "grade": 11,
        "address": "456 Oak Avenue",
        "city": "Exampletown",
        "state": "New York",
        "country": "United States",
        "courses": [
            {
                "courseName": "Mathematics",
                "teacher": "Mr. Johnson",
                "grade": "B+"
            },
            {
                "courseName": "Science",
                "teacher": "Mrs. Adams",
                "grade": "A"
            },
            {
                "courseName": "English",
                "teacher": "Ms. Thompson",
                "grade": "A"
            }
        ]
    },
    {
        "id": "1002",
        "name": "Bob Johnson",
        "age": 16,
        "grade": 10,
        "address": "789 Elm Street",
        "city": "Exampleville",
        "state": "California",
        "country": "United States",
        "courses": [
            {
                "courseName": "Mathematics",
                "teacher": "Mr. Davis",
                "grade": "A-"
            },
            {
                "courseName": "Science",
                "teacher": "Mrs. Wilson",
                "grade": "B"
            },
            {
                "courseName": "English",
                "teacher": "Ms. Roberts",
                "grade": "B+"
            }
        ]
    }
]


@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)


@app.route('/students/<student_id>', methods=['GET'])
def get_student(student_id):
    for student in students:
        if student['id'] == student_id:
            return jsonify(student)
    return jsonify({'message': 'Student not found'})


if __name__ == '__main__':
    app.run()
