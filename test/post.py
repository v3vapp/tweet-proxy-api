from fastapi import FastAPI, File, UploadFile
from typing import List

app = FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(file: bytes = File(...)):
    with open("/home/daiki/Dropbox/v3v/tweet-proxy-api/files/test.png", "wb") as f:
        f.write(file)
    return {"status": "success"}

@app.post("/uploadfiles/")
async def create_upload_files(files: List[bytes] = File(...)):
    for i, file in enumerate(files):
        with open(f"/home/daiki/Dropbox/v3v/tweet-proxy-api/files/image{i}.png", "wb") as f:
            f.write(file)
    return {"filenames": [f"image{i}.png" for i in range(len(files))]}