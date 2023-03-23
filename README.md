# Recipe App API
<p align="center">
  <img src="https://user-images.githubusercontent.com/30208736/227306458-e400929a-701d-4593-b953-c38ab85ef3fd.png">
</p>

# Django REST API project using TDD, Docker and GitHub actions.


## Topics
- [About](About)
- [Technologies used](Technologies%20used)
- [How to use](How%20to%20use)

## About
This project manages different recipes posted by various users.
In this project,
- Only verified users are permitted to publish the recipe.
- The posted recipe can only be updated by its user.
- Nested serializers are used to generate the required results.
- Docker compose is used to manage the app and database.

## Technologies used
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)

## How to use
Use the following command to run the server
```
sudo docker-compose up -d
```
The API will be available at http://127.0.0.1:8000.

Use http://127.0.0.1:8000/api/docs to use the swagger.
