# ResumeSkill Analyzer

ResumeSkill Analyzer is a full-stack web application that compares a resume with a job description and shows how well the resume matches the required skills.

The user can upload a resume PDF, paste a job description, and get a match score, matched skills, missing skills, and a suggested learning roadmap.

## Features

- Upload resume PDF
- Paste job description
- Extract text from resume
- Detect skills from resume and job description
- Calculate resume match score
- Show matched skills
- Show missing skills
- Suggest learning roadmap
- Store previous analysis history
- Download analysis report
- Copy report to clipboard
- Modern black theme user interface

## Tech Stack

Frontend:
- React
- JavaScript
- CSS
- Vite

Backend:
- Python
- Django
- Django REST Framework
- PyMuPDF

Database:
- SQLite

## Project Workflow

1. User uploads a resume PDF.
2. User pastes a job description.
3. Backend extracts text from the resume.
4. Skills are detected from both resume and job description.
5. Both skill sets are compared.
6. Match score is calculated.
7. Matched skills, missing skills, and roadmap are displayed.
8. User can download or copy the analysis report.
9. Previous analysis reports are shown in the history dashboard.

## Screenshots

### Home Page

![Home Page](assets/screenshots/01-home-page.png)

### Resume Analysis Result

![Analysis Result](assets/screenshots/02-analysis-result.png)

### History Dashboard

![History Dashboard](assets/screenshots/03-history-dashboard.png)

### Download Report Feature

![Download Report](assets/screenshots/04-download-report.png)

### Django REST API

![API History](assets/screenshots/05-api-history.png)

## API Endpoints

Analyze resume:

```http
POST http://127.0.0.1:8000/api/analyze/