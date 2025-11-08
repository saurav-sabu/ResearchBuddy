from services.arxiv_service import fetch_arxiv_papers

def get_articles(query: str):
    # Fetch documents from the arXiv service based on the provided query
    docs = fetch_arxiv_papers(query)
    papers = []

    # Iterate through each document to extract relevant metadata
    for doc in docs:
        metadata = doc.metadata
       
        papers.append({
            # Extract the title of the paper
            "title": metadata.get("Title"),
            # Extract the authors of the paper, defaulting to an empty list if not found
            "authors": metadata.get("Authors"),
            # Extract the publication date of the paper
            "published": metadata.get("Published")
        })

    print(papers)

    # Return the list of papers with their metadata
    return papers