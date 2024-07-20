import os
from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI

from lib.dynamic_module import load_module_from_code
import lib.prompts as prompts

app = FastAPI()

origins = [
    "http://localhost:5173"
]

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

@app.post("/uploadcode")
async def upload_code(file: UploadFile = File(...)):
    content = await file.read()

    # do something to the code
    source_code = content.decode("utf-8")
    new_module = load_module_from_code(source_code)
    try:
        return new_module.say_hi()
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