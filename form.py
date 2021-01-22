# 載入uvicorn, 網頁服務器
import uvicorn

# 載入fastapi, 功能api框架
from fastapi import FastAPI, File, UploadFile, Request, Form

# 載入Jinja2Templates, 網頁框架
from fastapi.templating import Jinja2Templates

# 載入starlette, 功能 Restful api
from starlette.responses import RedirectResponse

# 載入  application/components/prediction/serve_model.py 之 Def:  predict, read_imagefile
from serve_model import predict, read_imagefile

#from src.model import spell_number


# 描述 app 
app_desc = """<h2>Try this app by uploading any image with `predict/image`</h2>
"""

# 定義 app FastAPI()
app = FastAPI(title='Tensorflow FastAPI Starter Pack', description=app_desc)

# 網頁範本
templates = Jinja2Templates(directory='webTemplates/')

# 家目錄 /
@app.get("/", include_in_schema=False)
async def index(request: Request):
    # 開啟網頁templates/form3.html
    return templates.TemplateResponse('form.html', context={'request': request})

# 目錄 /predict/image, POST
# 檔案上傳函式, 採用 UploadFile
@app.post("/")
async def predict_api(request: Request, usr: str = Form(...), age: int = Form(...), file: UploadFile = File(...)):
    # 帶入參數
    usr = usr
    age = age
    filename = file.filename

    # 許可圖片格式
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    # 圖片格式判定, 中斷返回下列訊息
    if not extension:
        predictionMessage = "Image must be jpg or png format!"
    else:
        # 圖片讀取, 啟動等待作業
        image = read_imagefile(await file.read())
        # 圖片預測函式
        predictionMessage = predict(image)
    return templates.TemplateResponse('form.html', context={'request': request, 'usr': usr, 'age': age, 'filename': filename, 'prediction': predictionMessage})

    
# Python 直接執行 python main.py
# 或  uvicorn main:app  --host 0.0.0.0 --port 9999
if __name__ == "__main__":
    #uvicorn.run(app, debug=True)
    uvicorn.run(app, port=9999, host='0.0.0.0')
