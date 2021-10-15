# Resume-Job-And-Description-Matching-System

------------------------------------------

This is an AI system that allows to select the most potential CVs for a corresponding job description

## *This is the system pipeline*

![Alt text](https://github.com/ikkear99/Resume-Job-And-Description-Matching-System/blob/Master/web_app/Images/pipeline.png "a title")

---------------------------

## *Dataset*

- Using CV and JD data from BAP software company (PDF, img, docs)
- Category: Information Technology
- Number of CV: 350
- Number of JD: 15

## *Description:*

### *Convert and cleaning data*

- Using NLTK and Spacy library
- Convert PDF, image, docs to text

### *Extract the candidate's knowledge contained in the CV*

- Using GGnew free train model to word embedding 

- Using TCN model(Acc~92%)

Model Accuracy

![Alt text](https://github.com/ikkear99/Resume-Job-And-Description-Matching-System/blob/Master/web_app/Images/result1.png "Model Accuracy")

Result classification 

![Alt text](https://github.com/ikkear99/Resume-Job-And-Description-Matching-System/blob/Master/web_app/Images/result2.png "Model classification result")

### *Calculate similarity between CV and JD*

Similarity Measures

![Alt text](https://github.com/ikkear99/Resume-Job-And-Description-Matching-System/blob/Master/web_app/Images/Similarity_Measures.png "Similarity Measures")


- Using 4 Algorithm: 

  - Jaccard Coefficient 
  - Sorensen Dice 
  - Cosine Similarity
  - Overlap Coefficient

## *My Result*

- My website:

![Alt text](https://github.com/ikkear99/Resume-Job-And-Description-Matching-System/blob/Master/web_app/Images/view_page_2.png "My website")

- Score Ranking

![Alt text](https://github.com/ikkear99/Resume-Job-And-Description-Matching-System/blob/Master/web_app/Images/view_page.png "Table score ranking")
