from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/alfat', methods=['GET'])
def get_employees():
    employees = [
        {'id': 1, 'firstName': 'Raouf', 'lastName': 'Doe', 'emailId': 'johndoe@example.com'},
        {'id': 2, 'firstName': 'Amine', 'lastName': 'Smith', 'emailId': 'janesmith@example.com'},
        {'id': 3, 'firstName': 'Bob', 'lastName': 'Johnson', 'emailId': 'bobjohnson@example.com'}
    ]
    return jsonify(employees)

if __name__ == '__main__':
    app.run(debug=True, port=8080)