from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError

app = Flask(_name_)

# In-memory storage for employees (replace with database in production)
employees = {}


@app.route('/employee', methods=['POST'])
def create_employee():
    try:
        data = request.json
        required_keys = ['name', 'email', 'age', 'gender', 'phoneNo', 'addressDetails', 'workExperience', 'qualifications', 'projects', 'photo']
        for key in required_keys:
            if key not in data:
                raise BadRequest('Invalid body request')

        email = data['email']
        if email in employees:
            return jsonify({"message": "Employee already exists", "success": False}), 200

        # Validate data types (you can add more validations)
        if not isinstance(data['age'], int):
            raise BadRequest('Invalid data type for age')

        # Add the employee
        employees[email] = data

        return jsonify({"message": "Employee created successfully", "regid": email, "success": True}), 200

    except BadRequest as e:
        return jsonify({"message": str(e), "success": False}), 400
    except Exception as e:
        return jsonify({"message": "Employee creation failed", "success": False}), 500


@app.route('/employee/<string:email>', methods=['PUT'])
def update_employee(email):
    try:
        if email not in employees:
            raise NotFound('No employee found with this email')

        data = request.json
        # Update employee data (you can add more validations)
        employees[email] = data

        return jsonify({"message": "Employee details updated successfully", "success": True}), 200

    except NotFound as e:
        return jsonify({"message": str(e), "success": False}), 404
    except Exception as e:
        return jsonify({"message": "Employee updation failed", "success": False}), 500


@app.route('/employee/<string:email>', methods=['DELETE'])
def delete_employee(email):
    try:
        if email not in employees:
            raise NotFound('No employee found with this email')

        # Delete the employee
        del employees[email]

        return jsonify({"message": "Employee deleted successfully", "success": True}), 200

    except NotFound as e:
        return jsonify({"message": str(e), "success": False}), 404
    except Exception as e:
        return jsonify({"message": "Employee deletion failed", "success": False}), 500


@app.route('/employees', methods=['GET'])
def get_employees():
    try:
        regid = request.args.get('regid')
        if regid:
            # Return a specific employee
            if regid in employees:
                return jsonify({"message": "Employee details found", "success": True, "employees": [employees[regid]]}), 200
            else:
                raise NotFound('No employee found with this email')
        else:
            # Return all employees
            return jsonify({"message": "Employee details found", "success": True, "employees": list(employees.values())}), 200

    except NotFound as e:
        return jsonify({"message": str(e), "success": False, "employees": []}), 404
    except Exception as e:
        return jsonify({"message": "Internal Server Error", "success": False}), 500


if _name_ == '_main_':
    app.run(debug=True)