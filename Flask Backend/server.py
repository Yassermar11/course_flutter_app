from flask import Flask, jsonify, request, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

courses = []


@app.route('/courses', methods=['GET'])
def get_courses():
    return jsonify(courses)

@app.route('/courses', methods=['POST'])
def create_course():
    if not request.json:
        return jsonify({"error": "Request must be JSON"}), 400

    required_fields = ['title', 'code', 'description', 'ects']
    if not all(field in request.json for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    new_course = request.json
    new_course["id"] = str(len(courses) + 1)
    courses.append(new_course)

    return jsonify(new_course), 201

@app.route('/courses/<id>', methods=['PUT'])
def update_course(id):
    course = next((c for c in courses if c["id"] == id), None)
    if not course:
        return jsonify({"error": "Course not found"}), 404
    course.update(request.json)
    return jsonify(course)

@app.route('/courses/<id>', methods=['DELETE'])
def delete_course(id):
    global courses
    courses = [c for c in courses if c["id"] != id]
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3400, debug=True)
