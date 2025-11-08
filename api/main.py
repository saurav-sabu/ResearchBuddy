from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from services.arxiv_service import fetch_arxiv_papers
from core.article_fetcher import get_articles
from core.summarizer import summarize_research_papers

app = FastAPI(
    title="ResearchBuddy API",
    description="An AI-powered research paper discovery and summarization API using Google Gemini",
    version="1.0.0"
)

class SearchRequest(BaseModel):
    query: str = Field(description="Topic or paper title to search for")



class SummaryRequest(BaseModel):
    query: str = Field(description="Generate summary for particular topic")


@app.get("/")
def home():
    return {"message": "Welcome to ResearchBuddy API 🚀"}


@app.post("/search")
def search_papers(request:SearchRequest):
    """
    Fetch relevant research papers from arXiv.
    """
    try:
        papers = get_articles(request.query)
        if not papers:
            raise HTTPException(status_code=404, detail="No papers found.")
        return {"count": len(papers), "papers": papers}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search error: {str(e)}")
    

@app.post("/summarize")
def summarize_paper(request: SummaryRequest):
    """
    Summarize a selected research paper using Google Gemini.
    """
    try:
        # Fetch arXiv documents
        docs = fetch_arxiv_papers(request.query)

        print(docs)
        
        if not docs:
            raise HTTPException(status_code=404, detail="No papers found for this query.")

        summary = summarize_research_papers(docs)

        return {
            "summary": summary
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Summarization error: {str(e)}")