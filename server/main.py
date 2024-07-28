import os
import random
from dotenv import load_dotenv

import cases.find_intersection

load_dotenv()

import io
import uvicorn
from fastapi import FastAPI, Response, File, UploadFile, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import matplotlib.pyplot as plt

from lib.dynamic_module import load_module_from_code
import lib.prompts as prompts
import lib.auth as auth
import cases

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

testcases_cache = set()
MAX_IO_CACHE_SIZE = os.environ.get("MAX_IO_CACHE_SIZE", 30)

@app.get("/io")
def gen_io_testcase():
    if len(testcases_cache) >= MAX_IO_CACHE_SIZE:
        print("Getting from cache")
        res = random.choice(list(testcases_cache))
    else:
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
            testcases_cache.add(res)
        except Exception as e:
            return e

    if res.startswith("```plaintext"):
        res = res.split("\n")[1:-1]

    lines = res.split("\n")
    print(lines[0])
    if len(lines) == 1:
        return JSONResponse(content={"testcase": res, "answer": "None Given"})
    else:
        return JSONResponse(content={"testcase": lines[0], "answer": "\n".join(lines[1:])})

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

@app.post("/generate_graph", responses={200: {"content": {"image/png": {}}}}, response_class=Response)
async def generate_graph(file: UploadFile = File(...)):
    content = await file.read()

    source_code = content.decode("utf-8")
    new_module = load_module_from_code(source_code)
    try:
        xrange = list(range(1,100))
        yrange = [new_module.compute_y(x) for x in xrange]
        plt.figure()
        plt.plot(xrange, yrange)
        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        return Response(content=buf.getvalue(), media_type="image/png")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Server cannot run code: {e}",
            headers={"WWW-Authenticate": "Bearer"}
        ) 

@app.post("/find_intersection")
async def find_intersection(file: UploadFile = File(...)):
    content = await file.read()

    source_code = content.decode("utf-8")
    new_module = load_module_from_code(source_code)
    try:
        scores = { "bc": 0, "ca": 0, "x": 0, "y": 0, "total_cases": 0, "AC": 0 }
        for testcase in cases.find_intersection.testcases:
            print(testcase)
            line1 = testcase.line1
            line2 = testcase.line2

            a1 = line1.a
            b1 = line1.b
            c1 = line1.c
            a2 = line2.a
            b2 = line2.b
            c2 = line2.c

            try:
                answers = testcase.get_answers()
                print("answers", answers)
                scores["total_cases"] += 1
            except Exception as e:
                print(e)
                continue

            try:
                bc = new_module.get_bc(b1, c1, b2, c2)
                if bc == answers["bc"]:
                    scores["bc"] += 1
            except Exception as e:
                pass

            try:
                ca = new_module.get_ca(c1, a1, c2, a2)
                if ca == answers["ca"]:
                    scores["ca"] += 1
            except Exception as e:
                pass

            try:
                x = new_module.get_x(a1, b1, c1, a2, b2, c2)
                if abs(x - answers["x"]) < 1e-6:
                    scores["x"] += 1
            except Exception as e:
                pass

            try:
                y = new_module.get_y(a1, b1, c1, a2, b2, c2)
                if abs(y - answers["y"]) < 1e-6:
                    scores["y"] += 1
            except Exception as e:
                pass

            try:
                x = new_module.get_x(a1, b1, c1, a2, b2, c2)
                y = new_module.get_y(a1, b1, c1, a2, b2, c2)
                print(f"Expected ({answers['x']}, {answers['y']}). Got ({x}, {y})")
                if abs(x - answers["x"]) < 1e-6 and abs(y - answers["y"]) < 1e-6:
                    scores["AC"] += 1
            except Exception as e:
                pass
            
        print(scores, flush=True)
        return JSONResponse(content=scores)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Server cannot run code: {e}",
            headers={"WWW-Authenticate": "Bearer"}
        )

if __name__ == "__main__":
    PORT = os.environ.get("PORT", 8000)
    uvicorn.run(app, host="0.0.0.0", port=PORT)