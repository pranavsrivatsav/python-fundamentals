import logging
from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI, Path, Query

# Configure logging - to use it for logging purpose - similar to console.log in js
logging.basicConfig(level=logging.INFO) 

app = FastAPI()  # Create a fast api object


# Class for student - we will use this
# Pydantic baseModel: It is used for creating data models with validation
# Below, we are validating the datamodel with the data types
class Student(BaseModel):
    student_id: int
    name: str
    age: int
    referrer: Optional[str] = None  # referrer is an optional attribute


students = [
    {"student_id": 1, "name": "Alice", "age": 20},
    {"student_id": 2, "name": "Bob", "age": 21},
    {"student_id": 3, "name": "Charlie", "age": 22},
    {"student_id": 4, "name": "David", "age": 23},
    {"student_id": 5, "name": "Eve", "age": 24},
]

#In python, optional params must come after mandatory params
def checkStudent(value, key: Optional[str] = "student_id", retIndex: Optional[bool] = False):
        logging.info(f"students in checkstudent: {students}")
        for i in range(len(students)):
            student = students[i]
            if student[key] == value:
                return student if not retIndex else i


# the @ symbol is something called as a decorator in python, similar to an annotation in Java
# It enhances the function associated with it
# creating a get endpoint
@app.get("/")
def index():
    return {"Hello": "World"}


# path parameter endpoint example
@app.get("/getStudent/{student_id}")
def getStudentById(student_id: int = Path(description="Student ID is Mandatory", gt=0)):
    studentFound = checkStudent(student_id)
    return studentFound


# query parameter endpoint example
@app.get("/getStudent")
def getStudentByName(
    name,
):  # any argument provided here, that is not obtained as a path param is assumed a query param
    studentFound = checkStudent(value=name, key="name")
    return studentFound


# post end point with request body
@app.post("/student/{student_id}")
# So in the request we are expecting a request body with a model matching the Student pydantic model
# And an optional parameter referrer
def createStudent(
    student_id: int,
    student: Student,
    referrer=Query(None, description="Referrer for the student admission"), 
    #None - makes it an optional parameter, description - will be available in the swagger docs
):
    # check if student exists
    logging.info(students)
    studentExists = checkStudent(student_id)
    logging.info(studentExists)

    # if exists throw failure
    if studentExists:
        return {"status": "failure", "message": "student already exists"}
    # else add student to the array
    else:
        # the request body is a pydantic model, we need to convert into dict before appending to students array
        student_dict = student.model_dump()

        # if referrer provided, add referrer as well into the student
        if referrer:
            student_dict["referrer"] = referrer
        
        students.append(student_dict)
        return student
    
#put method
@app.put("/student/{student_id}")
def edit_student(student_id: int, student: Student):
    student_found = checkStudent(student_id)

    if not student_found :
         return {"status": "failure", "message": "student does not exist"}

    student_dict = student.model_dump()
    students.remove(student_found)
    students.append(student_dict)
    return student_dict

#delete method
@app.delete("/student/{student_id}")
def delete_student(student_id: int):
    student_Found = checkStudent(student_id)

    if not student_Found :
         return {"status": "failure", "message": "student does not exist"}
    
    students.remove(student_Found) #unlike javascript, python is able to compare objects, find the first occurence and remove it
    logging.info(f"remaining students: {students}")
    return student_Found