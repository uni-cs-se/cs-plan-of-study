import json

from fastapi import FastAPI

app = FastAPI()

desiredcourses = {'CS1520': ['CS1800'], 'CS1800': ['CS1130', 'CS1160', 'CS1510'] , 'CS2530': ['CS1510', 'CS1520', 'CS1800'], 'CS3730': ['CS2530'], 'CS3530': ['CS1520', 'CS1800']}

@app.get("/desiredcourses/{course_id}")
def read_root(course_id):
    return json.dumps(desiredcourses[course_id])