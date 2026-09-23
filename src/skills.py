import re
SKILLS={'python','sql','pandas','numpy','matplotlib','seaborn','scikit-learn','sklearn','machine learning','deep learning','tensorflow','pytorch','nlp','natural language processing','nltk','spacy','tf-idf','postgresql','mysql','mongodb','git','github','streamlit','fastapi','flask','docker','jupyter','statistics','probability','hypothesis testing','feature engineering','model evaluation','rest api'}

def extract_skills(text):
    t=text.lower(); found=set()
    for s in SKILLS:
        if re.search(r'(?<![a-z0-9])'+re.escape(s)+r'(?![a-z0-9])',t): found.add(s)
    return found
