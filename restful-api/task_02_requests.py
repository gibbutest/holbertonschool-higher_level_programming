import requests
import csv

def fetch_and_print_posts():
    res = requests.get('https://jsonplaceholder.typicode.com/posts')

    print(f"Status Code: {res.status_code}")

    try:
        posts = res.json()
        for post in posts:
            print(post['title'])
    except:
        return

def fetch_and_save_posts():
    res = requests.get('https://jsonplaceholder.typicode.com/posts')

    data = []

    try:
        posts = res.json()
        for post in posts:
            data.append({'id': post['id'], 'title': post['title'], 'body': post['body']})

        fields = data[0].keys()

        with open('posts.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)

            writer.writeheader()
            writer.writerows(data)
    except:
        return
    

fetch_and_save_posts()