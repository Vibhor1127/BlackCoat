from pydantic import BaseModel

class ChatRequest(BaseModel):
    query: str

class SourceCard(BaseModel):
    title: str
    court_or_source: str
    year: str
    case_1: str
    case_1_year: str
    case_1_holding: str
    case_2: str
    case_2_year: str
    case_2_holding: str
    status: str
    provision_id: str

class ChatResponse(BaseModel):
    answer: str
    sources: list[SourceCard]