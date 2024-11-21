# Middlewares

__Middleware__ - це програмний компонент, який знаходиться між точкою входження додатку (наприклад, мережевим запитом) та основною бізнес-логікою цього додатку. Він діє як проміжний обробник, виконуючи певні дії або перевірки перед тим, як запит досягне основної логіки обробки або після виконання цієї логіки, але перед тим, як відповідь буде повернута користувачу.

## Dependency
### Встановлення залежностей

`pip install -f requrements.txt`
### Запуск доданку

`uvicorn main:app `


## Documentation

- [Base Middlewares](https://fastapi.tiangolo.com/tutorial/middleware/?h=midd)
- [Advanced Middlewares](https://fastapi.tiangolo.com/advanced/middleware/)