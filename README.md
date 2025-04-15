Job Matching & Analysis System
Overview
This system aims to match job titles with resumes based on textual similarity and categorize them into tech and non-tech roles. It processes job descriptions and resume titles, calculates cosine similarity between them using pre-trained word embeddings (Word2Vec), and categorizes job roles based on specific keywords. It also provides insights into job demand, resume length, and skill analysis.

Key Features
Text Cleaning: Cleans job titles, job descriptions, and resume titles using natural language processing (NLP) techniques, including tokenization, lemmatization, and stopword removal.

Fuzzy Matching: Matches resumes with job titles based on textual similarity, initially using fuzzy matching and gradually applying relaxed matching thresholds.

Word Embedding Calculation: Computes word embeddings for both resumes and job titles using Google's pre-trained Word2Vec model to capture semantic relationships.

Cosine Similarity: Calculates the cosine similarity between resume titles and job titles, helping to assess the degree of relevance between them.

Job Demand Analysis: Analyzes the frequency of job titles to identify the most common job postings and determine demand in tech and non-tech roles.

Visualization: Plots a scatter plot of resume length versus similarity score to identify any correlations between content length and job match strength.

Skill Frequency Analysis: Analyzes the skills (abilities) mentioned in resumes, identifying the most frequently mentioned skills.

Prerequisites
Before running the code, ensure the following packages are installed:

pandas: For data manipulation.

nltk: For natural language processing (NLP).

fuzzywuzzy: For fuzzy string matching.

gensim: For word embedding calculations.

matplotlib: For plotting visualizations.

To install the necessary packages, run:

bash
Copy
Edit
pip install pandas nltk fuzzywuzzy gensim matplotlib
Dataset
Job Title and Description CSV (job_title_des.csv):

Contains job titles and descriptions to be matched with resumes.

Resume Data CSV (cleaned_final_file.csv):

Contains resumes, including job titles and other information.

Both datasets need to be pre-processed to ensure consistency and clarity for further analysis.

Step-by-Step Process
1. Data Cleaning:
Job Title & Description Cleaning:

Removes unnecessary words like "Job," "Overview," and "Excited by."

Standardizes text (e.g., capitalization).

Removes symbols and cleans job descriptions.

Saves the cleaned dataset as cleaned_job_title_des.csv.

Resume Title & Description Cleaning:

Tokenizes, lemmatizes, and removes stopwords from both job titles and job descriptions.

Cleans text using clean_text function, which removes punctuation and converts text to lowercase.

2. Fuzzy Matching:
Initial Matching:

Matches resumes with job titles using fuzzy string matching (fuzzywuzzy library).

Computes similarity scores based on string similarity.

Relaxed Matching:

Applies relaxed matching thresholds (70% and 65%) to find more matches.

3. Word Embedding Calculation:
Word2Vec Model:

Loads Google’s pre-trained Word2Vec model for word embedding calculation.

Computes the average word embeddings for both resumes and job titles.

4. Cosine Similarity Calculation:
Computes cosine similarity between resume embeddings and job title embeddings to measure how well they match.

5. Job Demand Analysis:
Analyzes job titles for both tech and non-tech roles.

Categorizes job roles as tech-related using a predefined list of tech role keywords.

Displays the most common job titles, with separate analysis for tech and non-tech roles.

6. Resume Length vs. Similarity Score:
Plots a scatter plot comparing resume length (word count) with the similarity score to investigate any correlations.

7. Skills Analysis:
Analyzes the "ability" column in resumes to find the most common skills mentioned.

Output Files
cleaned_job_title_des.csv: Cleaned job titles and descriptions.

embedded_data.csv: Dataset containing resume and job embeddings.

similarity_results.csv: Dataset with cosine similarity scores between resumes and job titles.

top_resumes_0.75.csv: Filtered dataset of resumes with similarity scores above 0.75.

cleaned_top_resumes_0.75.csv: Dataset with missing data handled.

final_merged_dataset.csv: Final dataset with job descriptions linked to resumes.

Visualizations
Resume Length vs. Similarity Score:

A scatter plot showing the relationship between the word count of resumes and their corresponding similarity scores with job titles.

Example Outputs
Top 10 Job Titles with Strongest Resume Matches:

Lists the job titles that have the highest average similarity score with resumes.

Technical vs. Non-Technical Roles:

Provides insights into the demand for tech roles versus non-tech roles based on job title frequency.

Top 10 Skills in Resumes:

Shows the most common abilities (skills) mentioned in the resumes.

Troubleshooting
If you encounter any issues with missing data, check for null values in the original dataset. These can be handled by filling them with default values or dropping the rows/columns.

If the Word2Vec model fails to load, ensure you have an internet connection and the gensim library is correctly installed.

Future Improvements
Enhanced NLP Models: Implementing advanced models like BERT or GPT for better semantic understanding.

Automated Job Recommendation: Using the similarity scores to recommend the most suitable job roles for a given resume.

Integration with ATS Systems: Extending the system to interface with Applicant Tracking Systems (ATS) for automated job matching
