import requests
from tokens import token

def update_repo(url):
    headers = {"Authorization": f'token {token}'}
    body = {"description": "I know Python Requests!"}
    response = requests.patch(url, headers=headers, json=body)
    print(f'Response status code: {response.status_code}')
    return response.json()


if __name__ == '__main__':
    url = 'https://api.github.com/repos/angelkokudev/repo-created-with-api'

    repo = update_repo(url)
    assert repo['description'] == 'I know Python Requests!'
