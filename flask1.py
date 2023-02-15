from flask import Flask, jsonify, request

app = Flask(__name__)
employees = [
    {'id': 1, 'firstName': 'John', 'lastName': 'Doe', 'emailId': 'johndoe@example.com'},
    {'id': 2, 'firstName': 'Jane', 'lastName': 'Smith', 'emailId': 'janesmith@example.com'},
    {'id': 3, 'firstName': 'Bob', 'lastName': 'Johnson', 'emailId': 'bobjohnson@example.com'}
]

@app.route('/get', methods=['GET'])
def get_employees():
    return jsonify(employees)

@app.route('/employees', methods=['POST'])
def create_employee():
    data = request.get_json()
    new_employee = {
        'id': len(employees) + 1,
        'firstName': data['firstName'],
        'lastName': data['lastName'],
        'emailId': data['emailId']
    }
    employees.append(new_employee)
    return jsonify(new_employee)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
