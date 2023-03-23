# Recipe App API
Django REST API project using TDD, Docker and GitHub actions.

This project manages different recipies posted by different users.
In this project,
- Only verified users are able to post.
- The posted recipe can only be updated by its user.

# Technologies used
- Django REST framework
- Docker/ Docker-compose
- GitHub Actions

# How to use
Use the following command to run the server
```
sudo docker-compose up -d
```
The API will be available at http://127.0.0.1:8000.

Use http://127.0.0.1:8000/api/docs to use the swagger.
