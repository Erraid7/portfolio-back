from django.db import models


class Profile(models.Model):
    """Singleton -- there's only ever one row. Powers /api/about."""
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    photo_url = models.URLField(blank=True, default="")
    school = models.CharField(max_length=300)
    speciality = models.CharField(max_length=200, blank=True, default="")
    school_years = models.CharField(max_length=100, blank=True, default="")
    location = models.CharField(max_length=200, blank=True, default="")
    seeking = models.CharField(max_length=200, blank=True, default="")
    email = models.EmailField(blank=True, default="")
    phone = models.CharField(max_length=50, blank=True, default="")
    github = models.URLField(blank=True, default="")
    linkedin = models.URLField(blank=True, default="")

    # JSONField stores a Python list/dict directly as JSON in Postgres --
    # perfect for things like a list of paragraphs where you don't need to
    # query into individual items.
    bio = models.JSONField(default=list)         # list[str]
    journey = models.JSONField(default=list)      # list[str]
    interests = models.JSONField(default=list)    # list[str]

    def __str__(self):
        return self.name


class HomeContent(models.Model):
    """Singleton -- powers the static parts of /api/home (tagline, steps).
    Stats are computed live in the view, not stored here -- see §6."""
    tagline = models.TextField()
    how_to_use = models.JSONField(default=list)  # list[str]

    def __str__(self):
        return "Home content"


class Project(models.Model):
    PLATFORM_CHOICES = [
        ("web", "Web"),
        ("mobile", "Mobile"),
        ("desktop", "Desktop"),
        ("cli", "CLI / pipeline"),
    ]

    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=300)
    pinned = models.BooleanField(default=False)
    summary = models.TextField()
    bullets = models.JSONField(default=list)      # list[str]
    stack = models.JSONField(default=list)         # list[str]
    platform = models.CharField(
        max_length=20, choices=PLATFORM_CHOICES, default="web"
    )

    # Matches the frontend's MediaItem[] shape exactly:
    # [{ "type": "image", "src": "...", "alt": "..." }, ...]
    media = models.JSONField(default=list)

    # Matches the frontend's `links` shape exactly:
    # { "live": {"available": bool, "url": str|null, "reason": str|null}, ... }
    links = models.JSONField(default=dict)

    docs_markdown = models.TextField(blank=True, default="")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name


class SkillCategory(models.Model):
    key = models.SlugField(unique=True)   # "frontend", "backend", ...
    label = models.CharField(max_length=100)
    items = models.JSONField(default=list)  # list[str]
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.label


class ExperienceEntry(models.Model):
    role = models.CharField(max_length=200)
    org = models.CharField(max_length=200)
    period = models.CharField(max_length=100)   # e.g. "2025 -- Present"
    bullets = models.JSONField(default=list)
    is_current = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.role} @ {self.org}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} <{self.email}>"