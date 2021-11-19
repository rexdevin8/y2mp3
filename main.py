from fastapi import FastAPI
from fastapi.responses import FileResponse
from download import Download
from pathlib import Path
import uvicorn
import os

app = FastAPI()

directory = os.getcwd()
path = os.path.join(directory,"Download")
print(path)

@app.get("/ymp3/")
async def ytsearch(link: str):
    download = Download.getaudio(link,)
    pathfile = os.path.join(directory,download)
    print(pathfile)
    print(download)
    paths = sorted(Path(path).iterdir(), key=os.path.getmtime)
    actpath = paths[0]
    print("path is"+str(paths[0]))
    return FileResponse(actpath, media_type="audio/mpeg",filename=download)
