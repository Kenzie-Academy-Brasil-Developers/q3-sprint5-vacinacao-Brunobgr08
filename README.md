<h1 align="center">
  <img alt="Kenzie" title="Kenzie Academy Brasil" src="https://kenzie.com.br/_next/image?url=%2Fimages%2Flogo.png&w=256&q=75" width="100px" />
</h1>

<h1 align="center">
  Vacinação - API
</h1>

<p align = "center">
Este é o backend da atividade Vacinação - Uma database onde é possível cadastrar vacinas, juntamente informações  da pessoa vacinada e visualizar estes registros. O objetivo dessa aplicação é trazer praticidade para controle de vacinação, seja em uma instituição ou para controle particular/individual.
</p>

<p align="center">
  <a href="#endpoints">Endpoints</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</p>

## **Endpoints**

A API tem um total de 2 endpoints, sendo relacionados a vacinas - podendo cadastrar e visualizar os registros das mesmas.<br/>

#### Por se tratar de uma aplicação simples, as rotas não requerem autenticação

O url base da API é https://budgets-management.herokuapp.com

<h2 align ='center'> Listando Vacinas </h2>

Nesse endpoint podemos ver as vacinas já cadastrados na plataforma. Aqui conseguimos ver as vacinas, dados da pessoa vacinada, datas e unidade de aplicação da vacina.
Na API podemos acessar a lista dessa forma:

`GET /vaccinations - FORMATO DA RESPOSTA - STATUS 200`

```json
[
  {
    "cpf": "81276557183",
    "name": "chrystian",
    "first_shot_date": "Thu, 21 Apr 2022 21:19:00 GMT",
    "second_shot_date": "Wed, 20 Jul 2022 21:19:00 GMT",
    "vaccine_name": "pfizer",
    "health_unit_name": "santa rita"
  },
  {
    "cpf": "85754688794",
    "name": "miguel lopes",
    "first_shot_date": "Thu, 21 Apr 2022 22:46:50 GMT",
    "second_shot_date": "Wed, 20 Jul 2022 22:46:50 GMT",
    "vaccine_name": "pfizer",
    "health_unit_name": "santa casa"
  },
  {
    "cpf": "65127943658",
    "name": "thais de souza",
    "first_shot_date": "Thu, 21 Apr 2022 22:46:50 GMT",
    "second_shot_date": "Wed, 20 Jul 2022 22:46:50 GMT",
    "vaccine_name": "fiocruz",
    "health_unit_name": "santa casa"
  },
  {
    "cpf": "54223598971",
    "name": "diego torres",
    "first_shot_date": "Thu, 21 Apr 2022 22:46:50 GMT",
    "second_shot_date": "Wed, 20 Jul 2022 22:46:50 GMT",
    "vaccine_name": "fiocruz",
    "health_unit_name": "posto jk"
  }
]
```

<h2 align ='center'> Cadastro de Vacinas </h2>

`POST /vaccinations - FORMATO DA REQUISIÇÃO`

```json
{
  "cpf": "54223598971",
  "name": "Diego Torres",
  "vaccine_name": "FioCruz",
  "health_unit_name": "Posto JK"
}
```

Caso dê tudo certo, a resposta será assim:

`POST /vaccinations - FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "cpf": "54223598971",
  "name": "diego torres",
  "first_shot_date": "Thu, 21 Apr 2022 22:46:50 GMT",
  "second_shot_date": "Wed, 20 Jul 2022 22:46:50 GMT",
  "vaccine_name": "fiocruz",
  "health_unit_name": "posto jk"
}
```

<h3 align ='center'> Possíveis erros no Cadastro </h3>

No exemplo a requisição foi feita faltando o campo "health_unit_name".
Caso você acabe errando e mandando algum campo errado ou faltando, a resposta de erro será assim:

`POST /vaccinations - FORMATO DA REQUISIÇÃO`

```json
{
  "cpf": "54223598971",
  "name": "Diego Torres",
  "vaccine_name": "FioCruz"
}
```

`POST /vaccinations - `
` FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "required_keys": ["cpf", "name", "vaccine_name", "health_unit_name"],
  "sended_keys": ["cpf", "name", "vaccine_name"]
}
```

CPF já cadastrado:
Não são aceitos CPF's repetidos no cadastro.
O retorno para este tipo de requisição será a seguinte:

`POST /vaccinations - `
` FORMATO DA RESPOSTA - STATUS 409`

```json
{
  "error": "This CPF already exists in database"
}
```

Tipos de dados inválidos.
No exemplo, a requisição foi feita faltando o campo "cpf" como "inteiro" (Integer).

`POST /vaccinations - FORMATO DA REQUISIÇÃO`

```json
{
  "cpf": 54223598971,
  "name": "Diego Torres",
  "vaccine_name": "FioCruz",
  "health_unit_name": "Posto JK"
}
```

`POST /vaccinations - `
` FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "error": "wrong type data for key 'cpf'",
  "expected": "string",
  "received": "integer"
}
```
