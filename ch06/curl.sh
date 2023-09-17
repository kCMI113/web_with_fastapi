#!/bin/bash

### get all
curl -X 'GET' \
'http://127.0.0.1:8000/event/' \
-H 'accept: application/json' \


# ### get one
# curl -X 'GET' \
# 'http://127.0.0.1:8000/event/3' \
# -H 'accept: application/json' \

# ### add event
# curl -X 'POST' \
# 'http://127.0.0.1:8000/event/new' \
# -H 'accept: application/json' \
# -H 'Content-Type: application/json' \
# -d '{
#     "id": 3,
#     "title": "FastAPI Book Launch",
#     "image": "https: //linktomyimage.com/image.png",
#     "description": "We will be discussing the contents of the FastAPI book in this event.Ensure to come with your own copy to win gifts!",
#     "tags": ["python", "fastapi", "book", "launch"], 
#     "location": "Google Meet"
# }'

# ### del one 
# curl -X 'DELETE' \
# 'http://127.0.0.1:8000/event/2' \
# -H 'accept: application/json'

# ### del all 
# curl -X 'DELETE' \
# 'http://127.0.0.1:8000/event/' \
# -H 'accept: application/json'




# ### signup
# curl -X 'POST' \
# 'http://127.0.0.1:8000/user/signup' \
# -H 'accept: application/json' \
# -H 'Content-Type: application/json' \
# -d '{
#     "email": "test@eamil.com",
#     "password": "pass123",
#     "username": "zanni"
# }'

# ### signin_wrong
# curl -X 'POST' \
# 'http://127.0.0.1:8000/user/signin' \
# -H 'accept: application/json' \
# -H 'Content-Type: application/json' \
# -d '{
#     "email": "test@eamil.com",
#     "password": "pass1d23"
# }'

# ### signin
# curl -X 'POST' \
# 'http://127.0.0.1:8000/user/signin' \
# -H 'accept: application/json' \
# -H 'Content-Type: application/json' \
# -d '{
#     "email": "test@eamil.com",
#     "password": "pass123"
# }'


# curl -X 'PUT' \
# 'http://127.0.0.1:8000/todo/1' \
# -H 'accept: application/json' \
# -H 'Content-Type: application/json' \
# -d '{
#     "item": "changed11"
# }'

# curl -X 'DELETE' \
# 'http://127.0.0.1:8000/todo/1' \
# -H 'accept: application/json'


