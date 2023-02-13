Este projeto fullstack foi criado a partir do template de Djavue do @huogerac. 
A proposta é possibilitar o compartilhamento de pontos turísticos ao redor do mundo, por diferentes usuários.
Para uma apresentação mais detalhada, acesse: 
[Link](https://youtu.be/IH5UgG_9DII)
Para poder acessar o projeto na sua máquina, você precisa de algumas ferramentas instaladas:   
# Requisitos (requirements):
- [Install docker](https://docs.docker.com/install/)
- Learn [Python](https://docs.python.org/3/tutorial/) and [Django](https://docs.djangoproject.com/en/2.0/intro/tutorial01/)
- Learn [vue.js](vuejs.org)
- Learn [Nuxt.js](https://nuxtjs.org/)
- Get familiar with [Vuetify.js](vuetifyjs.com/) components

# Rodar localmente (running locally):
```
    $ cd search_turism
    $ docker-compose build
    $ docker-compose up -d backend frontend
```
Depois de fazer o build e iniciar todos containers, fazendo um docker ps é possível ver que temos os seguintes serviços rodando:

```
$ docker ps
CONTAINER ID   IMAGE                  COMMAND                 NAMES
fc70d0d24a71   front-search_turism    "docker-entrypoint.s…"   search_turism_frontend_1
54bc3e4bc3d7   nginx                  "/docker-entrypoint.…"   search_turism_nginx_1
9bf5f32dfd3e   postgres:13.3-alpine   "docker-entrypoint.s…"   search_turism_postgres_1
```
Para acessar os serviços, utilize as URLs abaixo:

[http://localhost] para acessar o frontend
[http://localhost/api] para acessar diretamente alguma rota da API
[http://localhost/admin] para acessar o Django admin
