from typing import Dict

import pytest

from api_client import APIMangacollect


class TestAPIMangacollect:

    @pytest.fixture
    def api(self):
        # Instantiate the APIMangacollect class with your credentials
        return APIMangacollect(username='shooter.dev@gmail.com', password='Shooteroot59')

    def test_get_collection(self, api):
        collection = api.get_collection()

        assert isinstance(collection, dict)

    def test_get_collection_by_user(self, api):
        collection = api.get_collection('shooterdev')

        assert isinstance(collection, dict)

    def test_get_all_series(self, api):
        items = api.get_all_series()

        assert isinstance(items, list)

        for item in items:
            assert isinstance(item, dict)

    def test_get_all_jobs(self, api):
        items = api.get_all_jobs()

        assert isinstance(items, list)

        for item in items:
            assert isinstance(item, dict)

    def test_get_all_authors(self, api):
        items = api.get_all_authors()

        assert isinstance(items, list)

        for item in items:
            assert isinstance(item, dict)

    def test_get_all_publishers(self, api):
        items = api.get_all_publishers()

        assert isinstance(items, list)

        for item in items:
            assert isinstance(item, dict)

    def test_get_news(self, api):
        item = api.get_news()

        assert isinstance(item, Dict)

        for item_volume in item['volumes']:
            assert isinstance(item_volume, dict)

        for item_edition in item['editions']:
            assert isinstance(item_edition, dict)

        for item_serie in item['series']:
            assert isinstance(item_serie, dict)

        for item_boxe in item['boxes']:
            assert isinstance(item_boxe, dict)

        for item_box_edition in item['box_editions']:
            assert isinstance(item_box_edition, dict)

        for item_box_volume in item['box_volumes']:
            assert isinstance(item_box_volume, dict)

    def test_get_planning(self, api):
        item = api.get_planning()

        assert isinstance(item, Dict)

        for item_volume in item['volumes']:
            assert isinstance(item_volume, dict)

        for item_edition in item['editions']:
            assert isinstance(item_edition, dict)

        for item_serie in item['series']:
            assert isinstance(item_serie, dict)

        for item_boxe in item['boxes']:
            assert isinstance(item_boxe, dict)

        for item_box_edition in item['box_editions']:
            assert isinstance(item_box_edition, dict)

        for item_box_volume in item['box_volumes']:
            assert isinstance(item_box_volume, dict)

    def test_get_planning_month(self, api):
        item = api.get_planning('2020', '11')

        assert isinstance(item, Dict)

        for item_volume in item['volumes']:
            assert isinstance(item_volume, dict)

        for item_edition in item['editions']:
            assert isinstance(item_edition, dict)

        for item_serie in item['series']:
            assert isinstance(item_serie, dict)

        for item_boxe in item['boxes']:
            assert isinstance(item_boxe, dict)

        for item_box_edition in item['box_editions']:
            assert isinstance(item_box_edition, dict)

        for item_box_volume in item['box_volumes']:
            assert isinstance(item_box_volume, dict)

    def test_get_edition(self, api):
        item = api.get_edition('333eb14c-5f0a-4130-99fe-d2842cd06349')

        assert isinstance(item, Dict)

        for item_edition in item['editions']:
            assert isinstance(item_edition, dict)

        assert isinstance(item['publisher'], dict)

        assert isinstance(item['serie'], dict)

        assert isinstance(item['genre'], dict)

        for item_volume in item['volumes']:
            assert isinstance(item_volume, dict)

    def test_get_serie(self, api):
        item = api.get_serie('a320ac19-4318-4471-9e4e-eb017f4584d5')

        assert isinstance(item, Dict)

        assert isinstance(item['serie'], dict)

        assert isinstance(item['genre'], dict)

        for item_kind in item['kinds']:
            assert isinstance(item_kind, dict)

        for item_task in item['tasks']:
            assert isinstance(item_task, dict)

        for item_job in item['jobs']:
            assert isinstance(item_job, dict)

        for item_author in item['authors']:
            assert isinstance(item_author, dict)

        for item_edition in item['editions']:
            assert isinstance(item_edition, dict)

        assert isinstance(item['publisher'], dict)

        for item_volume in item['volumes']:
            assert isinstance(item_volume, dict)

        for item_box_edition in item['box_editions']:
            assert isinstance(item_box_edition, dict)

        for item_boxe in item['boxes']:
            assert isinstance(item_boxe, dict)

        for item_box_volume in item['box_volumes']:
            assert isinstance(item_box_volume, dict)

    def test_get_author(self, api):
        item = api.get_author('edad2d63-cc34-42b8-9bc2-ca9e210b670d')

        assert isinstance(item, Dict)

        assert isinstance(item['author'], dict)

        for item_task in item['tasks']:
            assert isinstance(item_task, dict)

        for item_job in item['jobs']:
            assert isinstance(item_job, dict)

        for item_serie in item['series']:
            assert isinstance(item_serie, dict)

        for item_edition in item['editions']:
            assert isinstance(item_edition, dict)

        for item_volume in item['volumes']:
            assert isinstance(item_volume, dict)
