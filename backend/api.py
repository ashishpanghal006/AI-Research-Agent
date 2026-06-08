from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

from graph.workflow import graph

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class ResearchRequest(BaseModel):
    query: str


@app.get("/")
def home():
    return {"message": "AI Research Agent Running"}


@app.post("/research")
def research(data: ResearchRequest):
    try:
        result = graph.invoke(
            {
                "query": data.query
            }
        )
    
    except Exception as e:
        return {"error": str(e)}

    return {
        "query": data.query,
        "plan": result["plan"],
        "analysis": result["analysis"],
        "report": result["report"],
        "sources": result["sources"]
    }