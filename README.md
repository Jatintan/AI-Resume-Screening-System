# AI Resume Screening System

Portfolio project for screening resumes against a job description using explainable NLP/ML techniques.

## Features
- PDF, DOCX and TXT resume upload
- TF-IDF text representation
- Cosine similarity
- Transparent skill matching
- Candidate ranking
- Streamlit web interface

## Tech Stack
Python, Streamlit, scikit-learn, Pandas, NumPy, pypdf, python-docx, TF-IDF, cosine similarity.

## Local setup
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

## Scoring
Overall match = 70% text similarity + 30% skill match.

## Privacy
Do not commit real candidate resumes or personal information to GitHub. The `data/resumes/` folder is ignored by Git.

## License
MIT License. Copyright (c) 2026 Jatin Tanwar.


