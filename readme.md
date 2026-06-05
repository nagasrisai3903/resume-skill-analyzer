# ResumeSkill Analyzer

ResumeSkill Analyzer is a full-stack resume and job description matching platform built using Django REST Framework and React.

It allows users to upload a resume PDF, paste a job description, and instantly get a resume match score, matched skills, missing skills, suggested learning roadmap, and downloadable analysis report.

## Features

- Resume PDF upload
- Job description input
- Resume text extraction using Python
- Skill extraction from resume and job description
- Resume match score calculation
- Matched skills analysis
- Missing skills analysis
- Personalized learning roadmap
- Analysis history dashboard
- Average score and best score tracking
- Downloadable text report
- Copy report to clipboard
- Sample job descriptions for testing
- Modern black theme UI

## Tech Stack

### Frontend
- React
- JavaScript
- CSS
- Vite

### Backend
- Python
- Django
- Django REST Framework
- PyMuPDF
- SQLite

## Project Workflow

1. User uploads resume PDF.
2. User pastes a job description.
3. Backend extracts text from the resume.
4. Backend detects technical skills from resume and job description.
5. System compares both skill sets.
6. Match score is calculated.
7. Matched skills, missing skills, and roadmap are displayed.
8. User can download or copy the analysis report.
9. Previous analysis reports are shown in history dashboard.

## API Endpoints

### Analyze Resume

```http
POST http://127.0.0.1:8000/api/analyze/