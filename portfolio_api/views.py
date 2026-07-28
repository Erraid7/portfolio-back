from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.cache import cache
from django.utils import timezone

from .models import Profile, HomeContent, Project, SkillCategory, ExperienceEntry
from .serializers import (
    ProfileSerializer, ProjectSerializer,
    SkillCategorySerializer, ExperienceEntrySerializer, ContactMessageSerializer,
)
from .envelope import envelope


def _camel_profile(data: dict) -> dict:
    return {
        **data,
        "photoUrl": data.pop("photo_url"),
        "schoolYears": data.pop("school_years"),
    }


@api_view(["GET"])
def home_view(request):
    content = HomeContent.objects.first()
    profile = Profile.objects.first()

    total_projects = Project.objects.count()
    live_deployments = sum(
        1 for p in Project.objects.all() if p.links.get("live", {}).get("available")
    )
    platforms = Project.objects.values_list("platform", flat=True).distinct().count()
    tech_count = sum(len(c.items) for c in SkillCategory.objects.all())

    assert profile is not None
    assert content is not None
    data = {
        "name": profile.name,
        "role": profile.role,
        "photoUrl": profile.photo_url,
        "status": f"{profile.role} · {profile.seeking}",
        "tagline": content.tagline,
        "stats": [
            {"value": str(total_projects), "label": "projects shipped"},
            {"value": str(live_deployments), "label": "live deployments"},
            {"value": str(platforms), "label": "platforms — web, mobile, desktop"},
            {"value": f"{tech_count}+", "label": "technologies across the stack"},
        ],
        "howToUse": content.how_to_use,
    }
    return envelope(data)


@api_view(["GET"])
def about_view(request):
    profile = Profile.objects.first()
    data = _camel_profile(ProfileSerializer(profile).data) # type: ignore
    return envelope(data)


@api_view(["GET"])
def projects_list_view(request):
    projects = Project.objects.all()
    data = ProjectSerializer(projects, many=True).data
    tests = [
        {"label": "status is 200", "pass": True},
        {"label": "returns array", "pass": True},
        {"label": f"{projects.count()} projects present", "pass": projects.count() == 7},
    ]
    return envelope(data, tests=tests)


@api_view(["GET"])
def project_detail_view(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return envelope(
            {"error": f"No project with id {pk}."},
            status=404, status_text="Not Found",
        )
    data = ProjectSerializer(project).data
    tests = [
        {"label": "status is 200", "pass": True},
        {"label": "has field 'stack'", "pass": isinstance(project.stack, list)},
        {"label": "has field 'links'", "pass": bool(project.links)},
    ]
    return envelope(data, tests=tests)


@api_view(["GET"])
def skills_view(request):
    categories = SkillCategory.objects.all()
    data = SkillCategorySerializer(categories, many=True).data
    return envelope(data)


@api_view(["GET"])
def experience_view(request):
    entries = ExperienceEntry.objects.all()
    data = {"experience": ExperienceEntrySerializer(entries, many=True).data}
    return envelope(data)


@api_view(["POST"])
def contact_view(request):
    serializer = ContactMessageSerializer(data=request.data)
    if not serializer.is_valid():
        return envelope(
            {"error": "name, email, and message are required."},
            status=400, status_text="Bad Request",
        )
    serializer.save()
    return envelope(
        {"queued": True, "receivedAt": timezone.now().isoformat()},
        status=202, status_text="Accepted",
    )


# --- The joke endpoint -------------------------------------------------
# Always 401s. Escalates to 429 after 3 rapid attempts from the same IP,
# tracked via Django's cache (in-memory by default -- resets on restart,
# which is fine, this mirrors the original mock's in-memory Map exactly).
WINDOW_SECONDS = 10
LIMIT = 3


@api_view(["POST"])
def login_view(request):
    ip = request.META.get("HTTP_X_FORWARDED_FOR", request.META.get("REMOTE_ADDR", "anon"))
    cache_key = f"login-attempts:{ip}"
    attempts = cache.get(cache_key, 0) + 1
    cache.set(cache_key, attempts, timeout=WINDOW_SECONDS)

    if attempts > LIMIT:
        return envelope(
            {"error": "Too many attempts — try again in a few seconds."},
            status=429, status_text="Too Many Requests",
        )
    return envelope(
        {"error": "Nice try — this one needs an actual offer letter."},
        status=401, status_text="Unauthorized",
    )