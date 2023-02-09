from flask import Flask, request
import json
from dbhelpers import run_statement

app = Flask(__name__)

@app.get('/api/item')
def get_items():
    result = run_statement("CALL get_items()")
    if(type(result) == list):
        return json.dumps(result, default=str)
    else:
        return "Something went wrong!"


@app.post('/api/item')
def post_item():
    name = request.json.get('name')
    description = request.json.get('description')
    quantity = request.json.get('quantity')
    result = run_statement("CALL post_item(?,?,?)", [name, description, quantity])
    if result[0][0] == 1:
        return "Item added successfully!"
    else:
        "Something went wrong"

@app.patch('/api/item')
def patch_item():
    quantity = request.json.get('quantity')
    id = request.json.get('itemId')
    result = run_statement("CALL patch_item(?,?)" [quantity, id])
    if result [0][0] == 1:
        return "Item quantity updated successfully!"
    else:
        "Something went wrong"


@app.delete('/api/item')
def delete_item():
    id = request.json.get('itemId')
    result = run_statement("CAll delete_item(?)", [id])
    if(type(result) == list):
        if result[0][0] == 1:
            return "Item deleted successfully!"
        else:
            return "Item {} does not exist!".format(id)
    else:
        "Something went wrong"



# !.................EMPLOYEE.............


@app.get('/api/employee')
def get_employee():
    id_input = request.json.get('employeeId')
    result = run_statement("CALL get_employee(?)",[id_input])
    if(type(result) == list):
        return json.dumps(result, default=str)
    else:
        return "Something went wrong!"


@app.post('/api/employee')
def post_employee():
    name = request.json.get('name')
    hourly_wage = request.json.get('hourlyWage')
    result = run_statement("CALL post_employee(?,?)" [name, hourly_wage])
    # first field of the first array
    if result[0][0] == 1:
        return "New employee's name and hourly wage added successfully!"
    else:
        "Something went wrong"


@app.patch('/api/employee')
def patch_employee():
    hourly_wage = request.json.get('hourlyWage')
    id = request.json.get('employeeId')
    result = run_statement("CALL patch_employee(?,?)" [hourly_wage, id])
    if result[0][0] == 1:
        return "Employee's hourly wage updated successfully!"
    else:
        "Something went wrong"


@app.delete('/api/employee')
def delete_empoyee():
    id = request.json.get('employeeId')
    result = run_statement("CAll delete_employee(?)", [id])
    if(type(result) == list):
        if result[0][0] == 1:
            return "Employee deleted successfully!"
        else:
            return "Employee {} does not exist!".format(id)
    else:
        "Something went wrong"




app.run(debug = True)
# This is what runs our application