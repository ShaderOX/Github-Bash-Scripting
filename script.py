from github import Github
import os
import sys

if __name__ == "__main__":
    try:
        project_name = sys.argv[1].strip()
        project_description = sys.argv[2].strip()
        project_visibility = sys.argv[2].strip()

        g = Github(os.getenv('github_token'))
        user = g.get_user()
        username = user.login

        new_repo = user.create_repo(name=project_name,
                                    private=False if project_description == 'f' else True,
                                    description=project_description)

        print(new_repo.ssh_url)
    except Exception as e:
        pass
