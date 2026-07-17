import requests

response_posts = requests.get("https://jsonplaceholder.typicode.com/posts/")
print(f"Response status code: {response_posts.status_code}")
response_users = requests.get("https://jsonplaceholder.typicode.com/users/")
print(f"Response status code: {response_users.status_code}")

users = response_users.json()
posts = (response_posts.json())

#print how many post 
print(f"Number of posts: {len(posts)}")

# print title of first and last post
print(f"First post: {posts[0]['title']}")
print(f"Last post: {posts[-1]['title']}")

#qui is in title of posts and list first 3
qui_titles = [post['title'] for post in posts if 'qui' in post['title'].lower()]
print(f"Count with 'qui' in title: {len(qui_titles)}")
print(f"First 3 titles with 'qui': {qui_titles[:3]}")

#count how many posts each user has made
user_post_count = {}
for post in posts:
    user_id = post['userId']
    user_post_count[user_id] = user_post_count.get(user_id, 0) + 1

for user_id, count in sorted(user_post_count.items()):
    print(f"User {user_id}: {count} posts")
