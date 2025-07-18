from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()

# Cross-Origin Resource Sharing (CORS)
# essential to prevent random web pages from calling our API via a user's browser
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],            # for dev purposes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# mounting the browsers extension's source to the src/ directory
app.mount(
    "/static",
    StaticFiles(directory="../extension", html=True),
    name="static"
)

# serve popup.html at root to build out popup UI
@app.get("/")
async def serve_popup():
    return FileResponse("../extension/popup.html")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
