import requests
from pprint import pprint


def create_repo(url):
    token = ""
    headers = {'Authorization': f'token {token}'}
    body = {
        "name": "repo-created-with-api",
        "private": True,
        "has_wiki": False
    }
    response = requests.post(url, headers=headers, json=body)
    print(f'Response status code: {response.status_code}')
    return response.json()


if __name__ == '__main__':
    url = 'https://api.github.com/user/repos'

    repo = create_repo(url)
    pprint(repo)
