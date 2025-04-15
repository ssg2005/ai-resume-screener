# Job Matching & Analysis System

## Overview

This system aims to match job titles with resumes based on textual similarity and categorize them into tech and non-tech roles. It processes job descriptions and resume titles, calculates cosine similarity between them using pre-trained word embeddings (Word2Vec), and categorizes job roles based on specific keywords. It also provides insights into job demand, resume length, and skill analysis.

## Key Features

1. **Text Cleaning**: Cleans job titles, job descriptions, and resume titles using natural language processing (NLP) techniques, including tokenization, lemmatization, and stopword removal.
   
2. **Fuzzy Matching**: Matches resumes with job titles based on textual similarity, initially using fuzzy matching and gradually applying relaxed matching thresholds.

3. **Word Embedding Calculation**: Computes word embeddings for both resumes and job titles using Google's pre-trained Word2Vec model to capture semantic relationships.

4. **Cosine Similarity**: Calculates the cosine similarity between resume titles and job titles, helping to assess the degree of relevance between them.

5. **Job Demand Analysis**: Analyzes the frequency of job titles to identify the most common job postings and determine demand in tech and non-tech roles.

6. **Visualization**: Plots a scatter plot of resume length versus similarity score to identify any correlations between content length and job match strength.

7. **Skill Frequency Analysis**: Analyzes the skills (abilities) mentioned in resumes, identifying the most frequently mentioned skills.

## Prerequisites

Before running the code, ensure the following packages are installed:

```bash
pip install pandas nltk fuzzywuzzy gensim matplotlib
