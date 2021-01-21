from io import BytesIO
import numpy as np
import tensorflow as tf
from PIL import Image
from tensorflow.keras.applications.imagenet_utils import decode_predictions

# 是否指定模型 model or None
model = None

# 函式: 讀取模型
def load_model():
    model = tf.keras.applications.MobileNetV2(weights="imagenet")
    print("Model loaded")
    return model

# 函式: 讀取讀片
# 範例 file=@cat02.png;type=image/png
def read_imagefile(file) -> Image.Image:
    # 內存讀取二進制數據, 轉為圖片
    image = Image.open(BytesIO(file))
    return image

# 函式: 預測圖片
# 範例 image from Image.open(BytesIO(file)) or Image.open(localfile)
def predict(image: Image.Image):
    # 取取模型
    global model
    if model is None:
        model = load_model()
    
    # 影像處理
    image = np.asarray(image.resize((224, 224)))[..., :3]
    image = np.expand_dims(image, 0)
    image = image / 127.5 - 1.0
    
    # 預測結果輸出
    result = decode_predictions(model.predict(image), 2)[0]
    
    # 輸出結果渲染
    response = []
    for i, res in enumerate(result):
        resp = {}
        resp["class"] = res[1]
        resp["confidence"] = f"{res[2]*100:0.2f} %"

        response.append(resp)

    return response




'''
# 直接執行
image = Image.open(('/var/www/html/github/tensorflow-fastapi-starter-pack/cat02.png'))
prediction = predict(image)
print(prediction)
'''