from langchain_community.document_loaders import ArxivLoader

def fetch_arxiv_papers(query: str, max_results: int = 3):
    """
    Fetches research papers from arXiv based on a search query.
    
    Args:
        query (str): Search query string to find relevant papers
        max_results (int): Maximum number of papers to retrieve (default: 3)
    
    Returns:
        list: List of document objects containing paper information, or empty list if error occurs
    """
    try:
        # Initialize ArxivLoader with search query and result limit
        loader = ArxivLoader(query=query, max_results=max_results)
        # Load and fetch the documents
        docs = loader.load()

        if not docs:
            print("⚠️ No papers found for this query.")
            return []
            
        return docs
    
    except Exception as e:
        # Handle any errors during the fetch operation
        print(f"❌ Error fetching from arXiv: {e}")
        return []