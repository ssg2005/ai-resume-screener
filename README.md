# Job Matching & Analysis System

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
