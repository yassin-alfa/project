from flask import Flask, jsonify

app = Flask(name)

employees = [
    {'id': 1, 'firstName': 'messi', 'lastName': 'Doe', 'emailId': 'johndoe@example.com'},
    {'id': 2, 'firstName': 'neymar', 'lastName': 'Smith', 'emailId': 'janesmith@example.com'},
    {'id': 3, 'firstName': 'benzema', 'lastName': 'Johnson', 'emailId': 'bobjohnson@example.com'}
]



@app.route('/api/v1/employees', methods=['GET'])
def get_all_employees():
    return jsonify(employees)



@app.route('/api/v1/employees/<int:id>', methods=['GET'])
def get_employee_by_id(id):
    employee = next((emp for emp in employees if emp['id'] == id), None)
    if employee:
        return jsonify(employee)
    else:
        return jsonify({'error': 'Employee not found'}), 404



@app.route('/api/v1/employees', methods=['POST'])
def create_employee():
    global employees
    if not request.json or 'firstName' not in request.json or 'lastName' not in request.json or 'emailId' not in request.json:
        return jsonify({'error': 'The request must contain firstName, lastName, and emailId fields'}), 400
    employee = {
        'id': len(employees) + 1,
        'firstName': request.json['firstName'],
        'lastName': request.json['lastName'],
        'emailId': request.json['emailId']
    }
    employees.append(employee)
    return make_response(jsonify({'message': 'Employee created successfully'}), 201)



@app.route('/api/v1/employees/<int:id>', methods=['DELETE'])
def delete_employee_by_id(id):
    global employees
    employees = [emp for emp in employees if emp['id'] != id]
    return '', 204



@app.route('/api/v1/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    global employees
    employee = next((emp for emp in employees if emp['id'] == id), None)
    if not employee:
        return jsonify({'error': 'Employee not found'}), 404
    if not request.json:
        return jsonify({'error': 'The request must contain data in JSON format'}), 400
    if 'firstName' in request.json:
        employee['firstName'] = request.json['firstName']
    if 'lastName' in request.json:
        employee['lastName'] = request.json['lastName']
    if 'emailId' in request.json:
        employee['emailId'] = request.json['emailId']
    return make_response(jsonify({'message': 'Employee updated successfully'}), 200)



if name == 'main':
    app.run(debug=True)
