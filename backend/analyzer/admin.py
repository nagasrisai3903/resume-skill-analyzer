from django.contrib import admin
from .models import ResumeAnalysis


@admin.register(ResumeAnalysis)
class ResumeAnalysisAdmin(admin.ModelAdmin):
    list_display = ('id', 'match_score', 'created_at')
    search_fields = ('job_description', 'matched_skills', 'missing_skills')
    list_filter = ('created_at',)