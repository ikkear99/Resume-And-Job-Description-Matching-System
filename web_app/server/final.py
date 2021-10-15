import Similar
from fileReader import *
import pandas as pd

resume_dir = "data_test_matching/Resumes/"
job_desc_dir = "data_test_matching/JobDesc/"
model_path = "model\model-1_best_version1.h5"

Resumes =  create_resume(resume_names, resume_dir)
Jobs =  create_job(job_description_names, job_desc_dir)

#################################### SCORE CALCULATION ################################
def calculate_scores(resumes, job_description):
    scores = []
    for x in range(resumes.shape[0]):
        score = Similar.match(resumes['TF_Based'][x], job_description['TF_Based'][index])
        scores.append(score)
    return scores

Resumes['Scores'] = calculate_scores(Resumes, Jobs)

Ranked_resumes = Resumes.sort_values(by=['Scores'], ascending=False).reset_index(drop=True)

Ranked_resumes['Rank'] = pd.DataFrame([i for i in range(1, len(Ranked_resumes['Scores'])+1)])

rank = pd.DataFrame((np.array(Ranked_resumes.Rank), Ranked_resumes.Name, np.array(Ranked_resumes.Scores)), columns=['Rank', 'Name', 'Score'])

rank.to_csv('Ranked_resumes.csv')
rank.to_json('Ranked_resumes.json')