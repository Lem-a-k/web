from requests import get, post


# print(post('http://localhost:5000/api/news',
#            json={'title': 'Заголовок',
#                  'content': 'Текст новости',
#                  'user_id': 1,
#                  'is_private': False}).json())

# print(get('http://localhost:5000/api/news').json())
print(get('http://localhost:5000/api/v2/news/3').json())