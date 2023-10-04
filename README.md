# Desafio sistema de gerenciamento de tarefas (To-Do List)
Repositório para ser usado pelos candidatos à vaga de Desenvolvedor Júnior Backend Liferay da Simplify

## Descrição
- Desenvolva uma aplicação web utilizando uma linguagem de programação e um framework de sua escolha. A aplicação deve consistir em um sistema de gerenciamento de tarefas, onde os usuários podem criar, visualizar, editar e excluir tarefas.

## Requisitos
- Usar banco de dados
- Campos mínimos da entidade de tarefa
    - Nome
    - Descrição
    - Realizado
    - Prioridade
- Criar CRUD de tarefas

## Instruções
- Fazer um fork do repositório para sua conta pessoal do git
- Trabalhar utilizando commits
- Documentar como executar sua aplicação
- Descrever as funcionalidades do software

## Utilização
Necessário Docker instalado.

Foram compiladas as instruções necessárias em um arquivo "makefile", podendo usare o projeto utilizando os passoa:
1. Clonar o repositório
2. Criar a imagem (irá resultar na imagem "micro_python:1.0.0"): ```make build ```
3. Subir os container (através do docker compose): ```make up```
4. [Opcional] Baixar os containers: ````make down```

## Estrutura
Há três serviços parametrizados no arquivo "docker-compose.yml" sendo eles:
- api: API utilizando o framework FastAPI (Python)
- db: contêm o banco de dados PostgreSQL
- adminer: explorador de banco de dados (PHP) 

Ao serem criados os containers, os mesmos podem ser acessados através das URLs:
- api: localhost:8000/docs (documentação no Swagger, gerado pelo FastAPI)

![api](https://github.com/digitalesch/desafio-junior-backend-simplify/assets/3438852/4d6ff5b9-6c54-42a0-8ef7-525869f2da9a)

- db: utilizando a string de conexão "postgresql://postgres:example@db:5000/postgres" ou pelo próximo serviço

![db3](https://github.com/digitalesch/desafio-junior-backend-simplify/assets/3438852/7e9c01b2-fe34-4bfb-a26b-fa225516e522)

- adminer: localhost:9000

![db](https://github.com/digitalesch/desafio-junior-backend-simplify/assets/3438852/98f80f4f-d72e-4f91-bb7e-756eb3157fa5)
![db_2](https://github.com/digitalesch/desafio-junior-backend-simplify/assets/3438852/0c5231fa-a092-4619-afea-b054e50e380f)

  
