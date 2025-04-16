# AI SCREENER RESUME

## Overview

The **Job Matching & Analysis System** matches job titles with resume titles based on semantic similarity using NLP and Word Embeddings. It also categorizes roles into **Tech** and **Non-Tech**, analyzes job demand trends, skill frequencies, and visualizes key insights.

---

## Key Features

### 1. Text Cleaning & Preprocessing
- Utilizes **NLTK** for advanced text preprocessing.
- Key Steps:
  - Lowercasing
  - Removing punctuation
  - Tokenization
  - Stopword removal
  - Lemmatization

### 2. Fuzzy Matching
- Leverages `fuzzywuzzy` for approximate string matching between resume and job titles.
- Features:
  - Strict-to-relaxed threshold matching
  - Handles minor typos and phrasing variations

### 3. Word Embedding with Word2Vec
- Embeds job descriptions and resumes using **Google's pre-trained Word2Vec** model via `gensim`.
- Captures semantic relationships for better match accuracy.

### 4. Cosine Similarity
- Calculates **cosine similarity** between embedded vectors.
- Helps determine how closely a resume matches a job title semantically.

### 5. Job Demand Analysis
- Analyzes frequency distribution of job titles.
- Categorizes job roles into:
  - Tech Roles (e.g., Software Engineer, Data Scientist)
  - Non-Tech Roles (e.g., HR Manager, Sales Executive)

### 6. Visualization
- Scatter plot of:
  - Resume length vs. similarity score
  - Reveals insights into content quality and job match strength

### 7. Skill Frequency Analysis
- Extracts skills from resume content.
- Displays most frequently mentioned abilities.

---

## Prerequisites

Before running the system, install the following dependencies:

```bash
pip install pandas nltk fuzzywuzzy[speedup] gensim matplotlib

```

---

## Sample Screenshots

### 1. Top 10 Job Titles with Strongest Resume Matches:

![image](https://github.com/user-attachments/assets/75dcff09-7421-45e6-9003-b6e88521bef8)

### 2. Job Titles with the Highest Demand (Based on Job Posting Frequency) AND Top 10 Tech Jobs in Demand:

![image](https://github.com/user-attachments/assets/04bd8099-26d8-45ed-bafc-18a8a96f50c6)

### 3. Resume Length vs. Similarity Score:

![image](https://github.com/user-attachments/assets/bd5b0cb7-e9e4-46d3-b14f-2c86ead6985b)

### 4. Count how often each skill appears in the resumes:

![image](https://github.com/user-attachments/assets/cdde2d2a-5b3c-44c5-ace5-31015d0229f2)

## Credits
- Developed by: Sushant Singh Gautam


