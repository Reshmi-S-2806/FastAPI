from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
import os
from dotenv import load_dotenv
import urllib.parse

load_dotenv()  # Load environment variables from .env file

username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")
cluster = os.getenv("MONGO_CLUSTER")

app = FastAPI()

# Connect to MongoDB locally
MONGO_URL = f"mongodb+srv://{username}:{urllib.parse.quote(password)}@{cluster}/?appName=Cluster0"
client = MongoClient(MONGO_URL)
db = client["library_management"]
students_collection = db["students"]

class Address(BaseModel):
    city: str
    country: str

class Student(BaseModel):
    name: str
    age: int
    address: Address

@app.post("/students", status_code=201)
async def create_student(student: Student):
    result = students_collection.insert_one(student.model_dump())
    return {"id": str(result.inserted_id)}

@app.get("/students", response_model=list[Student])
async def list_students(country: str = None, age: int = None):
    query = {}
    if country:
        query["address.country"] = country
    if age:
        query["age"] = {"$gte": age}
    students = list(students_collection.find(query, {"_id": 0}))
    return students

@app.get("/students/{id}", response_model=Student)
async def get_student(id: str):
    student = students_collection.find_one({"_id": ObjectId(id)}, {"_id": 0})
    if student:
        return student
    else:
        raise HTTPException(status_code=404, detail="Student not found")

@app.patch("/students/{id}", status_code=204)
async def update_student(id: str, student: Student):
    updated_student = student.model_dump(exclude_unset=True)
    result = students_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": updated_student})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    else:
        return

@app.delete("/students/{id}", status_code=200)
async def delete_student(id: str):
    result = students_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    else:
        return {"message": "Student deleted successfully"}
