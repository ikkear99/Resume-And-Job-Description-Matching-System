import pandas as pd
import os
from Extract_sentence import *
from Extract_line import *
from Extract_word import *
from pdf2text import *


def pdf2text(pdfFilename):
    # Convert pdf file to text
    text = Pdf2Text.convert(pdfFilename) # get string of text content of pdf
    cv_df = pd.DataFrame(text.split("\n"))
    return cv_df


def extract_sentence(cv_df):
    # extract all sentences from the pdf cv file
    extract_sentence = Extract_sentence()
    extract_sentence.init_data(cv_df)
    extract_sentence.normalize()
    extract_sentence.clusterSentence()
    extract_sentence.extractSentence()
    return extract_sentence.data

def extract_line(cv_df):
    # Extract all lines from the pdf cv file
    extract_line = Extract_line()
    extract_line.init_data(cv_df)
    extract_line.extract_line()
    return extract_line.data

def extract_word(cv_df):
    # Extract all words from the cv text file
    extract_word = Extract_word()
    extract_word.init_data(cv_df)
    extract_word.extract_word()
    return extract_word.data

resume_dir = "data_test_matching/Resumes"
job_desc_dir = "data_test_matching/JobDesc"
resume_names = os.listdir(resume_dir)
job_description_names = os.listdir(job_desc_dir)


def pdf2line(res):
    pdfFilename = res
    extract = pdf2text(pdfFilename)
    data = extract_line(extract)
    data.columns = ['Sentence']

    return data
