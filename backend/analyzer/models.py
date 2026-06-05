from django.db import models


class ResumeAnalysis(models.Model):
    resume_file = models.FileField(upload_to='resumes/')
    job_description = models.TextField()
    match_score = models.FloatField(default=0)
    matched_skills = models.TextField(blank=True)
    missing_skills = models.TextField(blank=True)
    roadmap = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Analysis - {self.match_score}%"