import os
import asyncio
from dotenv import load_dotenv
load_dotenv()
import spacy
from sentence_transformers import SentenceTransformer
from backend.services.resume_analyzer import analyze_full_resume

def main():
    print("Loading models...")
    nlp = spacy.load("en_core_web_md")
    embedder = SentenceTransformer("all-MiniLM-L6-v2")
    
    resume_text = "I am a software engineer with 5 years of Python experience."
    job_desc = "Looking for a Python software engineer."
    
    print("Analyzing...")
    res = analyze_full_resume(resume_text, nlp, embedder, job_desc)
    print("Result:", res)

if __name__ == "__main__":
    main()
