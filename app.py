import streamlit as st
from src.parser import extract_text
from src.matcher import rank_resumes

st.set_page_config(page_title='AI Resume Screening System', page_icon='📄', layout='wide')
st.title('📄 AI Resume Screening System')
st.caption('NLP-based resume screening using TF-IDF, cosine similarity, and skill matching.')

job_description = st.text_area('Paste Job Description', height=250)
files = st.file_uploader('Upload resumes (PDF, DOCX, TXT)', type=['pdf','docx','txt'], accept_multiple_files=True)

if st.button('Screen Resumes', type='primary'):
    if not job_description.strip(): st.error('Please enter a job description.'); st.stop()
    if not files: st.error('Please upload at least one resume.'); st.stop()
    resumes=[]
    for f in files:
        text=extract_text(f)
        if text.strip(): resumes.append({'filename':f.name,'text':text})
    results=rank_resumes(job_description,resumes)
    st.subheader('Candidate Ranking')
    st.dataframe([{'Rank':i+1,'Resume':r['filename'],'Overall Match':f"{r['overall_score']:.1f}%",'Text Similarity':f"{r['text_similarity']:.1f}%",'Skill Match':f"{r['skill_score']:.1f}%"} for i,r in enumerate(results)],use_container_width=True,hide_index=True)
    for i,r in enumerate(results,1):
        with st.expander(f"#{i} {r['filename']} — {r['overall_score']:.1f}%"):
            st.write('**Matched skills:**', ', '.join(r['matched_skills']) or 'None')
            st.write('**Missing skills:**', ', '.join(r['missing_skills']) or 'None')
