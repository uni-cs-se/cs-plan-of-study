import json

from fastapi import FastAPI

app = FastAPI()

universities = ["Univeristy of Northern Iowa", "University of Iowa", "University of Iowa State"]

course_lists = {'000': ['CS1', 'CS2', 'C3'], '001': ['CS1', 'CS2', 'CS3'], '002': ['CS1', 'CS2', 'CS3']  }
@app.get("/courses/{university_id}")
def read_root(university_id):
    return json.dumps(course_lists[university_id])