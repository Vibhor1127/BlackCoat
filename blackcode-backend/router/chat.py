from fastapi import APIRouter, HTTPException
from models.schemas import ChatRequest, ChatResponse, SourceCard
from services.retriever import retrieve_top_k
from services.gemini import get_gemini_answer

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    # Retrieve top matching laws/judgments
    contexts = retrieve_top_k(request.query, k=3)

    # Get Gemini's simple-language answer grounded in context
    answer = get_gemini_answer(request.query, contexts)

    # Build source cards for UI
    sources = [
        SourceCard(
            title=c['title'],
            court_or_source=c['court_or_source'],
            year=c['year'],
            case_1=c['case_1'],
            case_1_year=c['case_1_year'],
            case_1_holding=c['case_1_holding'],
            case_2=c['case_2'],
            case_2_year=c['case_2_year'],
            case_2_holding=c['case_2_holding'],
            status=c['status'],
            provision_id=c['provision_id'],
        )
        for c in contexts
    ]

    return ChatResponse(answer=answer, sources=sources)