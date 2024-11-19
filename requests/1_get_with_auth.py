import requests


def get_with_auth(url):
    token = ""
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    print(f'Response status code: {response.status_code}')
    data = response.json()
    num_of_repos = len(data)
    return num_of_repos, response.headers


if __name__ == "__main__":
    url = "https://api.github.com/user/repos"

    num_of_repos, headers = get_with_auth(url)

    print(f"Total Repos: {num_of_repos}")
    print(f"Response headers: {headers}")
