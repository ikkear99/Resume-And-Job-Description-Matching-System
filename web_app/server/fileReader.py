import textract as tx
import Cleaner
import tf_idf
from knowledge_model import *

resume_names = os.listdir(resume_dir)
job_description_names = os.listdir(job_desc_dir)

document = []

def read_resumes(list_of_resumes, resume_directory, model_path):
    placeholder = []
    for res in list_of_resumes:
        knowledge = read_pdf_resumes(resume_directory + res, model_path)
        temp = []
        temp.append(res)

        # knowledge = tx.process(knowledge, encoding='ascii')
        knowledge.encode('ascii', 'replace')
        # knowledge = str(knowledge, 'utf-8')
        # knowledge.decode('utf-8', 'ignore')

        temp.append(knowledge)
        placeholder.append(temp)
    return placeholder



def get_cleaned_words(document):
    for i in range(len(document)):
        raw = Cleaner.Cleaner(document[i][1])
        document[i].append(" ".join(raw[0]))
        document[i].append(" ".join(raw[1]))
        document[i].append(" ".join(raw[2]))
        sentence = tf_idf.do_tfidf(document[i][3].split(" "))
        document[i].append(sentence)
    return document

def create_resume(resume_names, resume_dir, model_path):
    document = read_resumes(resume_names, resume_dir, model_path)

    Doc = get_cleaned_words(document)

    Database = pd.DataFrame(document, columns=[
                            "Name", "Context", "Cleaned", "Selective", "Selective_Reduced", "TF_Based"])

    return Database


def read_jobdescriptions(job_description_names, job_desc_dir):
    placeholder = []
    for tes in job_description_names:
        temp = []
        temp.append(tes)
        text = tx.process(job_desc_dir+tes, encoding='ascii')
        text = str(text, 'utf-8')
        temp.append(text)
        placeholder.append(temp)
    return placeholder


def create_job(job_description_names, job_desc_dir):
    job_document = read_jobdescriptions(job_description_names, job_desc_dir)

    Jd = get_cleaned_words(job_document)

    jd_database = pd.DataFrame(Jd, columns=[
                               "Name", "Context", "Cleaned", "Selective", "Selective_Reduced", "TF_Based"])

    return jd_database

