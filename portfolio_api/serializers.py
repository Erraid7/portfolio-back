from rest_framework import serializers
from .models import Profile, HomeContent, Project, SkillCategory, ExperienceEntry, ContactMessage


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "name", "role", "photo_url", "school", "speciality",
            "school_years", "location", "seeking", "email", "phone",
            "github", "linkedin", "bio", "journey", "interests",
        ]
        # Frontend expects camelCase-ish keys like "photoUrl" -- handled in
        # the view layer (§6) by renaming keys after serialization, so the
        # serializer itself can stay Pythonic (snake_case).


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id", "slug", "name", "role", "pinned", "summary",
            "bullets", "stack", "media", "links", "docs_markdown",
        ]


class SkillCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillCategory
        fields = ["key", "label", "items"]

    def to_representation(self, instance):
        # Frontend expects {"id": ..., "label": ..., "items": [...]}
        data = super().to_representation(instance)
        data["id"] = data.pop("key")
        return data


class ExperienceEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceEntry
        fields = ["role", "org", "period", "bullets"]


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]