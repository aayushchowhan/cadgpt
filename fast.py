from fastapi import FastAPI, Request, Form
from starlette.responses import FileResponse,HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from openaicode import openai_prompt
import os, time



import_details="""FREECADPATH = 'C:/Program Files/FreeCAD 0.20/bin'
import sys
sys.path.append(FREECADPATH)
import FreeCAD , Part
import FreeCAD as App
"""


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
#creating a get request
@app.get("/prompt/{prompt}",response_class=HTMLResponse)
async def prompt(prompt: str,request:Request):
    file_name='_'.join(prompt.split(' '))+'.FCStd'
    #changing prompt as per FCMacro
    prompt='create a free cad Macro in python for'+prompt+' in freeCAD and save it as '+file_name
    #prompt='create a stl file for '+prompt
    #saving all details in temporary python file
    with open('x.py','w') as f: 
        f.write(import_details)
        f.write(openai_prompt(prompt=prompt))

    #running file 
    os.system('python8 x.py')

    #checking if file exisits
    return templates.TemplateResponse("index.html", {"request": request})


