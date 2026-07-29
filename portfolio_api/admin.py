from django.contrib import admin
from .models import Profile, HomeContent, Project, SkillCategory, ExperienceEntry, ContactMessage, Service


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["name", "role", "seeking"]
    # Profile is a singleton -- this just makes the one row easy to find.


@admin.register(HomeContent)
class HomeContentAdmin(admin.ModelAdmin):
    list_display = ["tagline"]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "role", "pinned", "platform", "created_at"]
    list_editable = ["pinned"]          # tick/untick pinned right from the list view
    list_filter = ["pinned", "platform"]
    search_fields = ["name", "slug", "summary"]
    prepopulated_fields = {"slug": ("name",)}   # auto-fills slug as you type the name
    ordering = ["id"]


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ["label", "key", "order"]
    list_editable = ["order"]
    ordering = ["order"]


@admin.register(ExperienceEntry)
class ExperienceEntryAdmin(admin.ModelAdmin):
    list_display = ["role", "org", "period", "is_current", "order"]
    list_editable = ["is_current", "order"]
    ordering = ["order"]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["title", "key", "order", "example_project"]
    list_editable = ["order"]
    prepopulated_fields = {"key": ("title",)}
    ordering = ["order"]


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "created_at", "read"]
    list_editable = ["read"]
    list_filter = ["read"]
    ordering = ["-created_at"]
    readonly_fields = ["name", "email", "message", "created_at"]  # messages are read-only, not editable