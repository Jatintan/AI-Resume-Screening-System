from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .preprocessing import clean_text
from .skills import extract_skills

def rank_resumes(job_description,resumes):
    texts=[clean_text(job_description)]+[clean_text(r['text']) for r in resumes]
    matrix=TfidfVectorizer(stop_words='english',ngram_range=(1,2)).fit_transform(texts)
    sims=cosine_similarity(matrix[0:1],matrix[1:]).flatten()
    job_skills=extract_skills(job_description); out=[]
    for r,sim in zip(resumes,sims):
        skills=extract_skills(r['text']); matched=sorted(job_skills & skills); missing=sorted(job_skills-skills)
        skill_score=(len(matched)/len(job_skills)*100) if job_skills else 0
        text_score=float(sim*100); overall=.70*text_score+.30*skill_score
        out.append({'filename':r['filename'],'overall_score':overall,'text_similarity':text_score,'skill_score':skill_score,'matched_skills':matched,'missing_skills':missing})
    return sorted(out,key=lambda x:x['overall_score'],reverse=True)
