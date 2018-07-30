import requests


class RepoInfo:
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def __str__(self):
        return f'RepoInfo({self.name}, {self.url})'

    def to_tuple(self):
        return (self.name, self.url)


class GithubService:
    def __init__(self, token):
        self.token = token

    # TODO: add error handling and retries
    def authenticated_get(self, url):
        return requests.get(url, headers={'Authorization': f'token {self.token}'}).json()

    def get_user(self):
        return self.authenticated_get('https://api.github.com/user')

    def get_user_repos_with_retries(self, offset):
        url = f'https://api.github.com/user/repos?per_page=100&page={offset}'
        return self.authenticated_get(url).json()

    def get_user_repos(self):
        def loop(acc, offset):
            repos = self.get_user_repos_with_retries(offset)
            if not repos:
                return acc
            else:
                my_repos = list(map(lambda repo: RepoInfo(repo['full_name'], repo['html_url']), repos))
                return loop(acc + my_repos, offset + 1)

        return loop([], 1)
