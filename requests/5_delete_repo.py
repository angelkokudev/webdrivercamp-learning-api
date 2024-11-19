import requests

def delete_repo(url):
    token = ""
    headers = {"Authorization": f'token {token}'}
    response = requests.delete(url, headers=headers)
    print(f'Response status code: {response.status_code}')
    return response


if __name__ == "__main__":
    url = f'https://api.github.com/repos/angelkokudev/repo-created-with-api'

    delete_repo(url)
