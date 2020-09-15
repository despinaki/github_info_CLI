###################   --REQUIREMENTS---   ###########################
# Create a CLI with an Object Oriented design
# On starting the app, User is asked for their GitHub username
# A request is made to https://api.github.com/users/<username>/repos
# API data is turned into instances of Repository class
# User is shown a numbered list their repos by name
# User can input a number to see more details on the corresponding repository
import requests

class Repository():
    def __init__(self, reponame):
        self.reponame=reponame
    
    def show_details(self, name, private, forks_count, stargazers_count, created_at, updated_at):
        print(f'{name} has {forks_count} fork(s)')
        print(f'{name} has {stargazers_count} stargazer(s)')
        print(f'Is {name} private? >{private}')
        print(f'{name} was created on {created_at} and last updated on{updated_at}')

def get_github_info():
    global username
    global response
    global resp
    
    username = input('Please enter your GitHub username \n')
    response = requests.get(f'https://api.github.com/users/{username}/repos')
    resp=response.json()

    get_list()


def get_list():
    counter = 0
    for x in resp:
        counter += 1
        for attr, val in x.items():
            if attr=='name':
                print(f'{counter} - {val}')
    get_details()

def get_details():
    repo_choice = input('Choose a repo by repo number to view more details\n')
    try:
        choice = resp[int(repo_choice)-1]
        user_repo=Repository(choice['name'])
        user_repo.show_details(choice['name'], choice['private'], choice['forks_count'], choice['stargazers_count'], choice['created_at'], choice['updated_at'])
    except:
        print(f'The number must be between 1 and {len(resp)}')
        get_list()

    def yes_or_no():
        yes_no_answer = input('wanna choose another one? Enter Y or N \n')
        if yes_no_answer.lower() == 'y':
            get_list()
        elif yes_no_answer.lower() == 'n':
            exit()
        else:
            print('Please enter Y or N')
            yes_or_no()

    yes_or_no()

get_github_info()    
