from io import StringIO
from pathlib import Path

import pandas as pd
import pytest
from django.conf import settings
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.fixture(scope="module")
def media_file():
    fn = Path(settings.MEDIA_ROOT) / "test.txt"
    if not fn.exists():
        fn.parent.mkdir(parents=True, exist_ok=True)
        fn.write_text("hello\n")


@pytest.mark.django_db
class TestAdminDashboardViewSet:
    def test_permissions(self):
        client = APIClient()

        # failure - not admin
        assert client.login(username="pm@hawcproject.org", password="pw") is True
        url = reverse("api:admin_dashboard-media")
        resp = client.get(url)
        assert resp.status_code == 403

        # success - admin
        assert client.login(username="admin@hawcproject.org", password="pw") is True
        url = reverse("api:admin_dashboard-media")
        resp = client.get(url)
        assert resp.status_code == 200

    def test_media_report(self, media_file):
        client = APIClient()
        # check that media report successfully returns a csv header
        assert client.login(username="admin@hawcproject.org", password="pw") is True
        url = reverse("api:admin_dashboard-media") + "?format=csv"
        resp = client.get(url)
        assert resp.status_code == 200
        header = resp.content.decode().split("\n")[0]
        assert header == "name,extension,full_path,hash,uri,media_preview,size_mb,created,modified"


@pytest.mark.django_db
class TestAdminDiagnosticViewSet:
    def test_throttle(self):
        client = APIClient()

        # failure - not admin
        assert client.login(username="pm@hawcproject.org", password="pw") is True
        url = reverse("api:diagnostic-throttle")
        resp = client.get(url)
        assert resp.status_code == 403

        # success - admin
        assert client.login(username="admin@hawcproject.org", password="pw") is True
        url = reverse("api:diagnostic-throttle")
        for i in range(5):
            resp = client.get(url)
            assert "identity" in resp.data

        # success- throttled (>5/min)
        resp = client.get(url)
        assert resp.status_code == 429


@pytest.mark.django_db
class TestReportsViewSet:
    def test_assessment_values(self):
        client = APIClient()
        url = reverse("api:admin_reports-values")

        resp = client.get(url)
        assert resp.status_code == 403

        assert client.login(username="admin@hawcproject.org", password="pw") is True
        resp = client.get(url)
        assert resp.status_code == 200
        df = pd.read_json(StringIO(resp.content.decode()))
        assert df.shape == (3, 33)
