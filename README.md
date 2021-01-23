### 安裝
```
conda create --name fastapi python=3.8
conda activate fastapi
git clone https://github.com/c00cjz00/fastapi_uploadimg.git
cd fastapi_uploadimg
pip install --upgrade -r requirements.txt
```
### 執行
```
python main.py
or
python fomr2.py
```
或
```
uvicorn main:app  --host 0.0.0.0 --port 9999
or
uvicorn fomr2:app  --host 0.0.0.0 --port 9999
```
### 瀏覽
```
http://$IP:9999
```

Editor: Allen Chuang
