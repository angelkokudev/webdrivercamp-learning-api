import requests


def get_created_repo(url):
    token = ""
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    print(f'Response status code: {response.status_code}')
    repo = response.json()
    assert repo['has_wiki'] == False
    assert repo['private'] == True
    assert repo['name'] == 'repo-created-with-api'
    assert repo['owner']['login'] == 'angelkokudev'


if __name__ == "__main__":
    url = "https://api.github.com/repos/angelkokudev/repo-created-with-api"

    get_created_repo(url)
