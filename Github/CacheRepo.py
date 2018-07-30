import sqlite3


class CacheRepo:

    def __init__(self, db_path, db_name):
        self.fullPath = db_path + "/" + db_name
        # self.create_repo_info_table() # TODO: Not sure if this is working or not?
        # self.create_token_table() # TODO: Not sure if this is working or not?

    def create_token_table(self):
        conn = sqlite3.connect(self.fullPath)
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM sqlite_master WHERE type = 'table' AND name = 'token'")
        count = cur.fetchone()
        if count[0] == 0:
            cur.execute('''create table if not exists token (token text)''')
        cur.close()
        conn.close()

    def create_repo_info_table(self):
        conn = sqlite3.connect(self.fullPath)
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM sqlite_master WHERE type = 'table' AND name = 'repo_info'")
        count = cur.fetchone()
        if count[0] == 0:
            cur.execute('''create table if not exists repo_info (name text, url text)''')
        cur.close()
        conn.close()

    def fetch_token(self):
        conn = sqlite3.connect(self.fullPath)
        cur = conn.cursor()
        cur.execute("select * from token")
        token = cur.fetchone()
        conn.close()
        return token[0]

    def is_logged_in(self):
        token = self.fetch_token()
        if token:
            return True
        else:
            return False

    def insert_token(self, token):
        conn = sqlite3.connect(self.fullPath)
        cur = conn.cursor()
        cur.execute("insert into token(token) values (?)", token)
        inserted_token = cur.fetchone()
        cur.close()
        conn.close()
        return inserted_token

    '''@param repos Array of RepoInfo(name, url)'''
    def insert_repos_user_has_access_to(self, repos):
        conn = sqlite3.connect(self.fullPath)
        cur = conn.cursor()
        # TODO: Does this return anything? Would be useful
        cur.executemany("insert into repo_info(name, url) values (?, ?)", list(map(lambda repo: repo.to_tuple, repos)))
        cur.execute("select count(*) from repo_info")
        count = cur.fetchall()
        cur.close()
        conn.close()
        return count

    def fetch_all_repos(self):
        conn = sqlite3.connect(self.fullPath)
        cur = conn.cursor()
        cur.execute("select * from repo_info")
        repos = cur.fetchall()
        cur.close()
        conn.close()
        return repos
