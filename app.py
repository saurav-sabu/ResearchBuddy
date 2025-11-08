import streamlit as st
from services.arxiv_service import fetch_arxiv_papers
from core.article_fetcher import get_articles
from core.summarizer import summarize_research_papers
import time

# Streamlit Page Setup
st.set_page_config(
    page_title="ResearchBuddy - AI Research Paper Summarizer",
    page_icon="📚",
    layout="wide"
)

# Custom CSS for a polished UI
st.markdown("""
<style>
    .main-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #2E86C1;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        text-align: center;
        font-size: 1.1rem;
        color: #555;
        margin-bottom: 2rem;
    }
    .paper-card {
        background-color: #f9f9f9;
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #ddd;
        margin-bottom: 1rem;
        transition: all 0.3s ease-in-out;
    }
    .paper-card:hover {
        background-color: #f1f8ff;
        border-color: #2E86C1;
        transform: scale(1.01);
    }
</style>
""", unsafe_allow_html=True)

# Title and Description
st.markdown('<div class="main-title">📚 ResearchBuddy</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered academic assistant that finds and summarizes research papers from arXiv using Gemini</div>', unsafe_allow_html=True)

# --- Search Section ---
query = st.text_input("🔍 Enter a research paper title or topic:", placeholder="e.g., Attention Is All You Need")

if st.button("Search Papers"):
    if query.strip() == "":
        st.warning("Please enter a valid research paper title or topic.")
    else:
        with st.spinner("🔎 Fetching relevant papers from arXiv..."):
            papers = get_articles(query)
            time.sleep(1.5)

        if len(papers) == 0:
            st.error("No relevant papers found. Try a different query.")
        else:
            st.success(f"Found {len(papers)} related papers.")
            
            # --- Display Paper List ---
            st.markdown("### 🧾 Available Papers")
            selected_paper = st.radio(
                "Select a paper to summarize:",
                options=[f"{i+1}. {p['title']}" for i, p in enumerate(papers)],
                index=0
            )

            chosen_index = int(selected_paper.split(".")[0]) - 1
            chosen_paper = papers[chosen_index]

            with st.expander("📄 Paper Details"):
                st.write(f"**Title:** {chosen_paper['title']}")
                st.write(f"**Authors:** {chosen_paper['authors']}")
                st.write(f"**Published:** {chosen_paper['published']}")
            

            # --- Summarization Button ---
            if st.button("🧠 Generate Summary"):
                with st.spinner("Generating AI summary using Gemini..."):
                    try:
                        docs = fetch_arxiv_papers(query)
                        summary = summarize_research_papers(docs[chosen_index])
                        st.subheader("📘 Summary")
                        st.write(summary)
                        st.success("✅ Summary generated successfully!")
                    except Exception as e:
                        st.error(f"⚠️ An error occurred: {e}")
