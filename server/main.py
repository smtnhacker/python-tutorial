import os
from dotenv import load_dotenv

load_dotenv()

import uvicorn
from fastapi import FastAPI, File, UploadFile, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI

from lib.dynamic_module import load_module_from_code
import lib.prompts as prompts
import lib.auth as auth

app = FastAPI()

origins = [
    "http://localhost:5173",
    "https://python-tutorial-client.onrender.com"
]

if CLIENT_HOST := os.environ.get("CLIENT_HOST", ""):
    origins.append(CLIENT_HOST)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

openai_client = OpenAI()

@app.get("/")
def home():
    return "API is working"

@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    # Here you can process the file
    content = await file.read()
    return JSONResponse(content={"filename": file.filename, "content": content.decode("utf-8")})

class User(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(user: User):
    user_id = auth.authenticate_user(user.username, user.password)
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return {
        "userId": user_id
    }

@app.get("/io")
def gen_io_testcase():
    try:
        message = openai_client.chat.completions.create(
            temperature=0.6,
            top_p=1,    
            messages=[
                {
                    "role": "user",
                    "content": prompts.gen_io_testcase()
                }
            ],
            model="gpt-4o-mini"
        )

        res = message.choices[0].message.content
        if res.startswith("```plaintext"):
            res = res.split("\n")[1:-1]

        lines = res.split("\n")
        print(lines[0])
        if len(lines) == 1:
            return JSONResponse(content={"testcase": res, "answer": "None Given"})
        else:
            return JSONResponse(content={"testcase": lines[0], "answer": "\n".join(lines[1:])})
    except Exception as e:
        return e

@app.post("/ask_question")
async def ask_question(file: UploadFile = File(...)):
    content = await file.read()

    # do something to the code
    source_code = content.decode("utf-8")
    new_module = load_module_from_code(source_code)
    try:
        question = new_module.ask_question()
        message = openai_client.chat.completions.create(
            temperature=1,
            messages=[
                {
                    "role": "user",
                    "content": prompts.gen_question(question)
                }
            ],
            model="gpt-4o-mini"
        )

        return message.choices[0].message.content
    except Exception as e:
        return e

if __name__ == "__main__":
    PORT = os.environ.get("PORT", 8000)
    uvicorn.run(app, host="0.0.0.0", port=PORT)