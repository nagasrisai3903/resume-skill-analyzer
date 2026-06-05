from rest_framework import serializers
from .models import ResumeAnalysis


class ResumeAnalysisSerializer(serializers.ModelSerializer):
    matched_skills_list = serializers.SerializerMethodField()
    missing_skills_list = serializers.SerializerMethodField()
    roadmap_list = serializers.SerializerMethodField()

    class Meta:
        model = ResumeAnalysis
        fields = '__all__'

    def get_matched_skills_list(self, obj):
        if not obj.matched_skills:
            return []
        return [skill.strip() for skill in obj.matched_skills.split(',')]

    def get_missing_skills_list(self, obj):
        if not obj.missing_skills:
            return []
        return [skill.strip() for skill in obj.missing_skills.split(',')]

    def get_roadmap_list(self, obj):
        if not obj.roadmap:
            return []
        return [item.strip() for item in obj.roadmap.split('|')]