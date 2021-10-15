import gensim
import gensim.corpora as corpora
import streamlit as st
import Similar
from fileReader import *


def process(resume_dir, job_desc_dir, model_path, jdIndex):

    print(".............................................", jdIndex)

    resume_names = os.listdir(resume_dir)
    job_description_names = os.listdir(job_desc_dir)
    Resumes = create_resume(resume_names, resume_dir, model_path)
    Jobs = create_job(job_description_names, job_desc_dir)

    # chose the Job Description
    index = jdIndex

    #################################### SCORE CALCULATION ################################
    @st.cache()
    def calculate_scores(resumes, job_description):
        scores = []
        for x in range(resumes.shape[0]):
            score = Similar.match(
                resumes['TF_Based'][x], job_description['TF_Based'][index])
            scores.append(score)
        return scores


    Resumes['Scores'] = calculate_scores(Resumes, Jobs)

    Ranked_resumes = Resumes.sort_values(
        by=['Scores'], ascending=False).reset_index(drop=True)

    Ranked_resumes['Rank'] = pd.DataFrame(
        [i for i in range(1, len(Ranked_resumes['Scores'])+1)])

    ############################################ TF-IDF Code ###################################
    @st.cache()
    def get_list_of_words(document):
        Document = []

        for a in document:
            raw = a.split(" ")
            Document.append(raw)

        return Document


    document = get_list_of_words(Resumes['Cleaned'])

    id2word = corpora.Dictionary(document)
    corpus = [id2word.doc2bow(text) for text in document]


    lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=id2word, num_topics=6, random_state=100,
                                                update_every=3, chunksize=100, passes=50, alpha='auto', per_word_topics=True)

    return Ranked_resumes

