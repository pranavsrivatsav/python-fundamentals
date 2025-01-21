from fastapi import FastAPI, Path

app = FastAPI()  # Create a fast api object

students = [
    {"student_id": 1, "name": "Alice", "age": 20},
    {"student_id": 2, "name": "Bob", "age": 21},
    {"student_id": 3, "name": "Charlie", "age": 22},
    {"student_id": 4, "name": "David", "age": 23},
    {"student_id": 5, "name": "Eve", "age": 24},
]

# Print the toy array of students
for student in students:
    print(student)


# creating a get endpoint
@app.get("/")
def index():
    return {"Hello": "World"}


# path parameter endpoint example
@app.get("/getStudent/{student_id}")
def getStudentById(
    student_id: int = Path(description="Student ID is Mandatory", lt=5, gt=0)
):
    return students[int(student_id) - 1]
