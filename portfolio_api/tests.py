from functools import cache

from django.test import TestCase

# Create your tests here.
from django.core.cache import cache
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Project


class ProjectEndpointTests(APITestCase):
    def setUp(self):
        Project.objects.create(slug="test-project", name="Test", role="Dev", pinned=True)

    def test_list_returns_200(self):
        res = self.client.get("/api/projects/")
        self.assertEqual(res.status_code, 200)

    def test_detail_404_for_missing_id(self):
        res = self.client.get("/api/projects/9999/")
        self.assertEqual(res.status_code, 404)
        self.assertIn("error", res.json()["data"])


class LoginJokeEndpointTests(APITestCase):
    def setUp(self):
        cache.clear()
    
    def test_returns_401(self):
        res = self.client.post("/api/auth/login/")
        self.assertEqual(res.status_code, 401)

    def test_rate_limits_after_three_attempts(self):
        for _ in range(3):
            self.client.post("/api/auth/login/")
        res = self.client.post("/api/auth/login/")
        self.assertEqual(res.status_code, 429)