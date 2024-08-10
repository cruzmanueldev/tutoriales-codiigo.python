import requests

def method_get():
    base_url = "https://jsonplaceholder.typicode.com/todos/1"

    response = requests.get(base_url)
    result = response.json()

    print(result)


def method_post():
    base_url = "https://jsonplaceholder.typicode.com/posts"

    data = {
        'title' : 'requests',
        'body'  : 'codiigo.python',
        'userId': 1
    }

    response = requests.post(base_url, json=data)
    result = response.json()

    print(result)

method_get()
method_post()