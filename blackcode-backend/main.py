from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router.chat import router

app = FastAPI(title="BlackCode Legal Chatbot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Tighten this in production
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"status": "BlackCode Legal API is live 🟢"}