### 安裝
conda create --name webserver -c pytorch -c fastai fastai==1.0.61 torchvision==0.7 ipykernel 
conda create --name fastapi python=3.8
conda activate fastapi
git clone https://github.com/c00cjz00/fastapi_uploadimg.git
cd fastapi_uploadimg
pip install --upgrade -r requirements.txt

### 執行
python main.py
或
uvicorn predictImg:app  --host 0.0.0.0 --port 9001
### 瀏覽
http://$IP:9999

