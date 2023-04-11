import json
from pprint import pprint
from typing import Dict, List

import requests as requests


class APIMangacollect:
    _url_api = 'https://api.mangacollec.com/'
    _client_id = '38fee110b53a75af6cc72f6fb66fa504fc6241e566788f4b2f5b21c25ba2fefb'
    _client_secret = '060658630f7d199c19ab1cf34ed4e50935c748267e318a24e048d6ab45871da2'

    def __init__(self, username, password):
        self.headers = {'User-Agent': 'Mozilla/5.0', 'Accept': 'application/json', 'Authorization': ''}
        self.username = username
        self.password = password

    def _get_token(self):
        body = {
            "client_id": self._client_id,
            'client_secret': self._client_secret,
            'grant_type': 'password',
            'password': self.password,
            'scope': '',
            'username': 'shooter.dev@gmail.com'
        }

        req = requests.post('https://api.mangacollec.com/oauth/token', headers=self.headers, data=body)

        expires_in: float = float(json.loads(req.content)["expires_in"])
        created_at: float = float(json.loads(req.content)["created_at"])
        access_token: str = json.loads(req.content)["access_token"]
        refresh_token: str = json.loads(req.content)["refresh_token"]
        return access_token

    def get_collection(self, user: str = None) -> Dict:
        headers = self.headers
        headers['Authorization'] = f'Bearer {self._get_token()}'
        headers['client_id'] = self._client_id
        headers['client_secret'] = self._client_secret

        url = ''
        if user is None:
            url = f'{self._url_api}v2/users/me/collection'
        else:
            url = f'{self._url_api}v2/user/{user}/collection'

        response = requests.get(url,headers=headers)

        if response.status_code != 200:
            print(f'ERROR: code {response.status_code}')
        else:
            return json.loads(response.content)

    def get_all_series(self) -> List:
        """
            get all series V2
            :return: list[Dict] [
                {
                    "id": str,
                    "title": str,
                    "type_id": str,
                    "adult_content": bool,
                    "editions_count": int,
                    "tasks_count": int
                },
                ...
            ]
        """
        headers = self.headers
        headers['Authorization'] = f'Bearer {self._get_token()}'
        headers['client_id'] = self._client_id
        headers['client_secret'] = self._client_secret

        url = f'{self._url_api}v2/series/'

        response = requests.get(url,headers=headers)

        data: list = []

        if response.status_code != 200:
            print(f'ERROR: code {response.status_code}')
        else:
            for item in json.loads(response.content)['series']:
                data.append(item)

            return data

    def get_all_jobs(self) -> List:
        """
        get all jobs V1
        :return: list[Dict] [
            {
                "id": str,
                "title": str
            },
            ...
        ]
        """
        headers = self.headers
        headers['Authorization'] = f'Bearer {self._get_token()}'
        headers['client_id'] = self._client_id
        headers['client_secret'] = self._client_secret

        url = f'{self._url_api}v1/jobs/'

        response = requests.get(url, headers=headers)

        data: list = []

        if response.status_code != 200:
            print(f'ERROR: code {response.status_code}')
        else:
            for item in json.loads(response.content):
                data.append(item)

            return data

    def get_all_authors(self) -> List:
        """
        get all author V2
        :return: list[Dict] [
            {
                "id": str,
                "name": str,
                "first_name": str,
                "tasks_count": int
            },
            ...
        ]
        """
        headers = self.headers
        headers['Authorization'] = f'Bearer {self._get_token()}'
        headers['client_id'] = self._client_id
        headers['client_secret'] = self._client_secret

        url = f'{self._url_api}v2/authors/'

        response = requests.get(url, headers=headers)

        data: list = []

        if response.status_code != 200:
            print(f'ERROR: code {response.status_code}')
        else:
            for item in json.loads(response.content)['authors']:
                data.append(item)

            return data

    def get_all_publishers(self) -> List:
        """
        get all publishers V2
        :return: [
            {
                "id": str,
                "name": str,
                "first_name": str,
                "tasks_count": int
            },
            ...
        ]
        """
        headers = self.headers
        headers['Authorization'] = f'Bearer {self._get_token()}'
        headers['client_id'] = self._client_id
        headers['client_secret'] = self._client_secret

        url = f'{self._url_api}v2/publishers/'

        response = requests.get(url, headers=headers)

        data: list = []

        if response.status_code != 200:
            print(f'ERROR: code {response.status_code}')
        else:
            for item in json.loads(response.content)['publishers']:
                print(item)
                data.append(item)

            return data

    def get_news(self) -> Dict:
        headers = self.headers
        headers['Authorization'] = f'Bearer {self._get_token()}'
        headers['client_id'] = self._client_id
        headers['client_secret'] = self._client_secret

        url = f'{self._url_api}v2/volumes/news'

        response = requests.get(url, headers=headers)

        data: Dict = {
            'volumes': list[Dict],
            'editions': list[Dict],
            'series': list[Dict],
            'boxes': list[Dict],
            'box_editions': list[Dict],
            'box_volumes': list[Dict],
        }

        if response.status_code != 200:
            print(f'ERROR: code {response.status_code}')
        else:
            data_json = json.loads(response.content)

            volumes: list = []
            for item in data_json['volumes']:
                volumes.append(item)

            editions: list = []
            for item in data_json['editions']:
                editions.append(item)

            series: list = []
            for item in data_json['series']:
                series.append(item)

            boxes: list = []
            for item in data_json['boxes']:
                boxes.append(item)

            box_editions: list = []
            for item in data_json['box_editions']:
                box_editions.append(item)

            box_volumes: list = []
            for item in data_json['box_volumes']:
                box_volumes.append(item)

            data['volumes'] = volumes
            data['editions'] = editions
            data['series'] = series
            data['boxes'] = boxes
            data['box_editions'] = box_editions
            data['box_volumes'] = box_volumes
            return data

    def get_planning(self, annee: str = None, month: str = None) -> Dict:
        headers = self.headers
        headers['Authorization'] = f'Bearer {self._get_token()}'
        headers['client_id'] = self._client_id
        headers['client_secret'] = self._client_secret

        if annee is not None and month is not None:
            url: str = f'{self._url_api}v2/planning?month={annee}-{month}'
        else:
            url = f'{self._url_api}v2/planning'

        response = requests.get(url, headers=headers)

        data: Dict = {
            'volumes': list[Dict],
            'editions': list[Dict],
            'series': list[Dict],
            'boxes': list[Dict],
            'box_editions': list[Dict],
            'box_volumes': list[Dict],
        }

        if response.status_code != 200:
            print(f'ERROR: code {response.status_code}')
        else:
            data_json = json.loads(response.content)

            volumes: list = []
            for item in data_json['volumes']:
                volumes.append(item)

            editions: list = []
            for item in data_json['editions']:
                editions.append(item)

            series: list = []
            for item in data_json['series']:
                series.append(item)

            boxes: list = []
            for item in data_json['boxes']:
                boxes.append(item)

            box_editions: list = []
            for item in data_json['box_editions']:
                box_editions.append(item)

            box_volumes: list = []
            for item in data_json['box_volumes']:
                box_volumes.append(item)

            data['volumes'] = volumes
            data['editions'] = editions
            data['series'] = series
            data['boxes'] = boxes
            data['box_editions'] = box_editions
            data['box_volumes'] = box_volumes
            return data

    def get_edition(self, id: str) -> Dict:
        """
        get edition V2
        :return:
        editions: list[Dict] [
            {
            "id": str,
            "title": str | None,
            "series_id": str,
            "publisher_id": str,
            "parent_edition_id": str | None,
            "volumes_count": int,
            "last_volume_number": int | None,
            "commercial_stop": bool,
            "not_finished": bool,
            "follow_editions_count": int
            },
            ...
        ],
        publisher: Dict  {
            "id": str,
            "title": str,
            "closed": bool,
            "editions_count": int,
            "no_amazon": bool
        },
        serie: Dict {
            "id": str,
            "title": str,
            "type_id": str,
            "adult_content": bool,
            "editions_count": int,
            "tasks_count": int
        },
        genre: Dict {
            "id": str,
            "title": str,
            "to_display": bool
        },
        volumes: list[Dict] [
            {
            "id": str,
            "title": str | None,
            "number": int,
            "release_date": str date | None,
            "image_url": str url | None,
            "isbn": str | None,
            "asin": str | None,
            "edition_id": str,
            "possessions_count": int,
            "not_sold": bool
            },
            ...
        ]
        """
        headers = self.headers
        headers['Authorization'] = f'Bearer {self._get_token()}'
        headers['client_id'] = self._client_id
        headers['client_secret'] = self._client_secret

        url = f'{self._url_api}v2/editions/{id}'

        response = requests.get(url, headers=headers)

        data: Dict = {
            'editions': list[Dict],
            'publisher': Dict,
            'serie': Dict,
            'genre': Dict,
            'volumes': list[Dict]
        }

        if response.status_code != 200:
            print(f'ERROR: code {response.status_code}')
        else:
            data_json = json.loads(response.content)

            editions: list = []
            for item in data_json['editions']:
                editions.append(item)

            volumes: list = []
            for item in data_json['volumes']:
                volumes.append(item)

            data['editions'] = editions
            data['publisher'] = data_json['publishers'][0]
            data['serie'] = data_json['series'][0]
            data['genre'] = data_json['types'][0]
            data['volumes'] = volumes
            return data

    def get_serie(self, id: str) -> Dict:
        headers = self.headers
        headers['Authorization'] = f'Bearer {self._get_token()}'
        headers['client_id'] = self._client_id
        headers['client_secret'] = self._client_secret

        url = f'{self._url_api}v2/series/{id}'

        response = requests.get(url, headers=headers)

        data: Dict = {
            'series': Dict,
            'types': Dict,
            'kinds': list[Dict],
            'tasks': list[Dict],
            'jobs': list[Dict],
            'authors': list[Dict],
            'editions': list[Dict],
            'publishers': Dict,
            'volumes': list[Dict],
            'box_editions': list[Dict],
            'boxes': list[Dict],
            'box_volumes': list[Dict]
        }

        if response.status_code != 200:
            print(f'ERROR: code {response.status_code}')
        else:
            data_json = json.loads(response.content)

            kinds: list = []
            for item in data_json['kinds']:
                kinds.append(item)

            tasks: list = []
            for item in data_json['tasks']:
                tasks.append(item)

            jobs: list = []
            for item in data_json['jobs']:
                jobs.append(item)

            authors: list = []
            for item in data_json['authors']:
                authors.append(item)

            editions: list = []
            for item in data_json['editions']:
                editions.append(item)

            volumes: list = []
            for item in data_json['volumes']:
                volumes.append(item)

            box_editions: list = []
            for item in data_json['box_editions']:
                box_editions.append(item)

            boxes: list = []
            for item in data_json['boxes']:
                boxes.append(item)

            box_volumes: list = []
            for item in data_json['box_volumes']:
                box_volumes.append(item)

            data['serie'] = data_json['series'][0]
            data['genre'] = data_json['types'][0]
            data['kinds'] = kinds
            data['tasks'] = tasks
            data['jobs'] = jobs
            data['authors'] = authors
            data['editions'] = editions
            data['publisher'] = data_json['publishers'][0]
            data['volumes'] = volumes
            data['box_editions'] = box_editions
            data['boxes'] = boxes
            data['box_volumes'] = box_volumes
            return data

    def get_author(self, id: str) -> Dict:
        headers = self.headers
        headers['Authorization'] = f'Bearer {self._get_token()}'
        headers['client_id'] = self._client_id
        headers['client_secret'] = self._client_secret

        url = f'{self._url_api}v2/authors/{id}'

        response = requests.get(url, headers=headers)

        data: Dict = {
            'author': Dict,
            'tasks': list[Dict],
            'jobs': list[Dict],
            'series': list[Dict],
            'editions': list[Dict],
            'volumes': list[Dict]
        }

        if response.status_code != 200:
            print(f'ERROR: code {response.status_code}')
        else:
            data_json = json.loads(response.content)

            tasks: list = []
            for item in data_json['tasks']:
                tasks.append(item)

            jobs: list = []
            for item in data_json['jobs']:
                jobs.append(item)

            series: list = []
            for item in data_json['series']:
                series.append(item)

            editions: list = []
            for item in data_json['editions']:
                editions.append(item)

            volumes: list = []
            for item in data_json['volumes']:
                volumes.append(item)

            data['author'] = data_json['authors'][0]
            data['tasks'] = tasks
            data['jobs'] = jobs
            data['series'] = series
            data['editions'] = editions
            data['volumes'] = volumes
            return data
