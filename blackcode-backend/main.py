from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
from router.chat import router

app = FastAPI(title="BlackCode Legal Chatbot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Tighten this in production
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")

# Serve React static assets
current_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.abspath(os.path.join(current_dir, "..", "blackcode-frontend", "build"))
static_dir = os.path.join(build_dir, "static")

if os.path.exists(build_dir):
    if os.path.exists(static_dir):
        app.mount("/static", StaticFiles(directory=static_dir), name="static")

    @app.get("/{catchall:path}")
    def serve_react(catchall: str):
        # Do not catch API or Docs requests
        if catchall.startswith("api") or catchall.startswith("docs") or catchall.startswith("openapi.json"):
            return {"error": "Not Found"}
        
        # Check if the requested path is a real file (like /lady_justice.png)
        file_path = os.path.join(build_dir, catchall)
        if os.path.exists(file_path) and os.path.isfile(file_path):
            return FileResponse(file_path)
            
        return FileResponse(os.path.join(build_dir, "index.html"))

    @app.get("/")
    def read_root():
        return FileResponse(os.path.join(build_dir, "index.html"))
else:
    @app.get("/")
    def root():
        return {"status": "BlackCode Legal API is live 🟢 (Frontend build not found)"}