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

@app.get('/api/employee')
def get_employee():
    id_input = request.json.get('employeeId')
    result = run_statement("CALL get_employee(?)",[id_input])
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
    if result == None:
        return "Success"
    else:
        "Something went wrong"

@app.post('/api/employee')
def post_employee():
    name = request.json.get('name')
    hourly_wage = request.json.get('hourlyWage')
    result = run_statement("CALL post_employee(?,?)" [name, hourly_wage])
    if result == None:
        return "Success"
    else:
        "Something went wrong"

@app.patch('/api/item')
def patch_item():
    quantity = request.json.get('quantity')
    id = request.json.get('itemId')
    result = run_statement("CALL patch_item(?,?)" [quantity, id])
    if result == None:
        return "Success"
    else:
        "Something went wrong"

@app.patch('/api/employee')
def patch_employee():
    hourly_wage = request.json.get('hourlyWage')
    id = request.json.get('employeeId')
    result = run_statement("CALL patch_employee(?,?)" [hourly_wage, id])
    if result == None:
        return "Success"
    else:
        "Something went wrong"

@app.delete('/api/item')
def delete_item():
    id = request.json.get('itemId')
    result = run_statement("CAll delete_item(?)", [id])
    if result == None:
        return "Success"
    else:
        "Something went wrong"

@app.delete('/api/employee')
def delete_empoyee():
    id = request.json.get('employeeId')
    result = run_statement("CAll delete_employee(?)", [id])
    if result == None:
        return "Success"
    else:
        "Something went wrong"






app.run(debug = True)
# This is what runs our application