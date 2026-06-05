import fitz

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import ResumeAnalysis
from .serializers import ResumeAnalysisSerializer


SKILL_KEYWORDS = [
    # Python Backend
    "python", "django", "django rest framework", "drf", "flask", "fastapi",

    # Java Backend
    "java", "spring boot", "spring", "hibernate", "microservices",

    # Frontend
    "html", "css", "javascript", "typescript", "react", "react.js",
    "angular", "vue", "bootstrap", "tailwind", "responsive design",

    # Databases
    "sql", "mysql", "postgresql", "sqlite", "mongodb", "database design",

    # APIs and Tools
    "rest api", "api", "crud", "postman", "swagger",

    # DevOps and Cloud
    "git", "github", "docker", "kubernetes", "aws", "azure", "gcp",
    "deployment", "ci/cd",

    # Auth and Security
    "authentication", "authorization", "jwt", "oauth",

    # Data Skills
    "pandas", "numpy", "data analysis", "excel", "statistics",

    # CS Fundamentals
    "oops", "object oriented programming", "problem solving",
    "dsa", "data structures", "algorithms",
]


ROADMAP_SUGGESTIONS = {
    "python": "Revise Python basics, OOP, functions, file handling, and exception handling.",
    "django": "Learn Django models, views, URLs, admin panel, and backend CRUD flow.",
    "django rest framework": "Practice serializers, API views, CRUD APIs, and authentication in DRF.",
    "drf": "Practice Django REST Framework serializers, API views, routers, and authentication.",
    "flask": "Learn Flask routing, templates, APIs, and database integration.",
    "fastapi": "Learn FastAPI routing, Pydantic models, request validation, and API documentation.",

    "java": "Learn Java basics, OOP, collections, exception handling, and JDBC.",
    "spring boot": "Learn Spring Boot controllers, services, repositories, REST APIs, and dependency injection.",
    "spring": "Understand Spring framework basics, beans, dependency injection, and MVC architecture.",
    "hibernate": "Learn ORM concepts, entity mapping, relationships, and database operations using Hibernate.",
    "microservices": "Understand service-to-service communication, API gateway, service discovery, and modular backend design.",

    "html": "Practice semantic HTML, forms, tables, and accessibility basics.",
    "css": "Practice flexbox, grid, responsive design, animations, and clean UI styling.",
    "javascript": "Revise JavaScript variables, functions, arrays, objects, DOM, promises, and ES6.",
    "typescript": "Learn TypeScript types, interfaces, functions, generics, and React integration.",
    "react": "Learn React components, props, state, hooks, forms, routing, and API integration.",
    "react.js": "Learn React components, hooks, routing, forms, and REST API integration.",
    "angular": "Learn Angular components, services, routing, forms, and HTTP client.",
    "vue": "Learn Vue components, directives, state handling, and API integration.",
    "bootstrap": "Practice Bootstrap grid, components, forms, cards, and responsive layouts.",
    "tailwind": "Practice Tailwind utility classes, layouts, spacing, colors, and responsive design.",

    "sql": "Practice SELECT, WHERE, JOIN, GROUP BY, subqueries, constraints, and indexes.",
    "mysql": "Practice MySQL queries, joins, aggregate functions, normalization, and database design.",
    "postgresql": "Practice PostgreSQL queries, relationships, constraints, indexing, and transactions.",
    "sqlite": "Practice SQLite database creation, CRUD queries, and integration with Django.",
    "mongodb": "Learn collections, documents, CRUD operations, aggregation, and schema design.",
    "database design": "Learn tables, relationships, normalization, primary keys, foreign keys, and indexes.",

    "rest api": "Practice building REST APIs using Django REST Framework and testing them with Postman.",
    "api": "Understand API request-response flow, status codes, JSON, and endpoint design.",
    "crud": "Practice create, read, update, and delete operations in full-stack projects.",
    "postman": "Use Postman to test GET, POST, PUT, DELETE APIs and request bodies.",
    "swagger": "Learn API documentation and testing using Swagger/OpenAPI.",

    "git": "Learn Git init, add, commit, branch, merge, push, and pull workflow.",
    "github": "Upload projects to GitHub with README, screenshots, commits, and clean repository structure.",
    "docker": "Learn Docker images, containers, Dockerfile, ports, and running apps in containers.",
    "kubernetes": "Understand pods, deployments, services, scaling, and container orchestration basics.",
    "aws": "Learn AWS basics such as EC2, S3, IAM, RDS, and deployment concepts.",
    "azure": "Learn Azure basics, app services, storage, and deployment concepts.",
    "gcp": "Learn GCP basics, cloud run, storage, compute, and deployment concepts.",
    "deployment": "Practice deploying frontend and backend projects using Vercel, Render, or Railway.",
    "ci/cd": "Learn automated build, test, and deployment pipelines.",

    "authentication": "Learn login, registration, password hashing, sessions, and token-based authentication.",
    "authorization": "Learn role-based access control and permissions.",
    "jwt": "Learn JWT login, access tokens, refresh tokens, and protected routes.",
    "oauth": "Understand third-party login flow using Google or GitHub OAuth.",

    "pandas": "Practice dataframes, filtering, grouping, cleaning data, and CSV processing.",
    "numpy": "Practice arrays, indexing, numerical operations, and data manipulation.",
    "data analysis": "Practice cleaning, analyzing, and summarizing datasets.",
    "excel": "Practice formulas, filtering, pivot tables, and basic reporting.",
    "statistics": "Learn mean, median, mode, variance, probability, and data interpretation.",

    "oops": "Revise classes, objects, inheritance, polymorphism, abstraction, and encapsulation.",
    "object oriented programming": "Practice OOP concepts using Python or Java examples.",
    "problem solving": "Solve daily coding problems and explain your logic clearly.",
    "dsa": "Practice arrays, strings, dictionaries, recursion, searching, sorting, stacks, and queues.",
    "data structures": "Practice arrays, linked lists, stacks, queues, trees, graphs, and hash maps.",
    "algorithms": "Practice searching, sorting, recursion, dynamic programming basics, and time complexity.",
}


def extract_text_from_pdf(uploaded_file):
    file_bytes = uploaded_file.read()
    uploaded_file.seek(0)

    text = ""

    pdf_document = fitz.open(stream=file_bytes, filetype="pdf")

    for page in pdf_document:
        text += page.get_text()

    return text.lower()


def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILL_KEYWORDS:
        if skill.lower() in text:
            found_skills.append(skill)

    return sorted(list(set(found_skills)))


def generate_roadmap(missing_skills):
    roadmap = []

    for skill in missing_skills:
        suggestion = ROADMAP_SUGGESTIONS.get(
            skill,
            f"Learn and practice {skill} with small projects."
        )
        roadmap.append(suggestion)

    if not roadmap:
        roadmap.append(
            "Your resume matches well. Focus on projects, GitHub, interview practice, and deployment."
        )

    return roadmap


@api_view(['POST'])
def analyze_resume(request):
    resume_file = request.FILES.get('resume')
    job_description = request.data.get('job_description', '')

    if not resume_file:
        return Response(
            {"error": "Resume PDF is required."},
            status=status.HTTP_400_BAD_REQUEST
        )

    if not resume_file.name.lower().endswith(".pdf"):
        return Response(
            {"error": "Only PDF resume files are allowed."},
            status=status.HTTP_400_BAD_REQUEST
        )

    if not job_description.strip():
        return Response(
            {"error": "Job description is required."},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        resume_text = extract_text_from_pdf(resume_file)
    except Exception:
        return Response(
            {"error": "Could not read PDF. Please upload a valid resume PDF."},
            status=status.HTTP_400_BAD_REQUEST
        )

    jd_text = job_description.lower()

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    if not jd_skills:
        return Response(
            {
                "error": "No recognizable technical skills found in job description. Try adding skills like Python, Java, React, SQL, Django, Spring Boot, AWS, Docker, etc."
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    matched_skills = sorted(list(set(resume_skills).intersection(set(jd_skills))))
    missing_skills = sorted(list(set(jd_skills).difference(set(resume_skills))))

    match_score = round((len(matched_skills) / len(jd_skills)) * 100, 2)

    roadmap = generate_roadmap(missing_skills)

    analysis = ResumeAnalysis.objects.create(
        resume_file=resume_file,
        job_description=job_description,
        match_score=match_score,
        matched_skills=", ".join(matched_skills),
        missing_skills=", ".join(missing_skills),
        roadmap="|".join(roadmap)
    )

    serializer = ResumeAnalysisSerializer(analysis)

    return Response(
        {
            "message": "Resume analyzed successfully.",
            "analysis": serializer.data,
            "resume_skills": resume_skills,
            "job_description_skills": jd_skills
        },
        status=status.HTTP_201_CREATED
    )


@api_view(['GET'])
def analysis_history(request):
    analyses = ResumeAnalysis.objects.all().order_by('-created_at')
    serializer = ResumeAnalysisSerializer(analyses, many=True)
    return Response(serializer.data)