import io
import pandas as pd
from fastapi import FastAPI, Request, Form
from fastapi.responses import StreamingResponse
from fastapi.templating import Jinja2Templates
from app.models import date_from_cal


app = FastAPI()
templates = Jinja2Templates(directory='templates/')


@app.get("/")
async def root():
    return {"message": "Hello World"}


async def get_csv(resp: dict) -> pd.DataFrame:
    date_string = resp.get('chosen_date')
    some_data = {'a': [1,2,3], 'b': [5,5,5], 'c': [date_string, date_string, date_string]}
    df = pd.DataFrame(data=some_data)
    return df


@app.get('/downloader')
async def form_post(request: Request):
    result = 'Select a date'
    return templates.TemplateResponse('index.html', context={'request': request, 'result': result})


@app.post('/downloader')
async def form_post(request: Request, chosen_date: str = Form(...)):
    result = date_from_cal(chosen_date)
    df = await get_csv(result)
    
    response = StreamingResponse(io.StringIO(df.to_csv(index=False)), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=export.csv"
    return response