import pytest
from django.urls import reverse

from hawc.apps.animalv2 import models

from ..test_utils import check_200, check_403, generic_get_first, get_client


@pytest.mark.django_db
class TestExperimentView:
    def test_permission(self, db_keys):
        experiment = generic_get_first(models.Experiment)
        url = reverse("animalv2:experiment_detail", args=(experiment.id,))
        client = get_client()
        check_403(client, url)

        url = reverse("animalv2:experiment_update", args=(experiment.id,))
        check_403(client, url)

    def test_success(self, db_keys):
        random_experiment = generic_get_first(models.Experiment)
        url = reverse("animalv2:experiment_detail", args=(random_experiment.id,))
        client = get_client("pm")
        response = check_200(client, url)
        context_experiment = response.context["experiment"]
        assert random_experiment.id == context_experiment.id

        url = reverse("animalv2:experiment_update", args=(random_experiment.id,))
        response = check_200(client, url)