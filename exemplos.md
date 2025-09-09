# Exemplos de Requisições para Testar

## APIs Públicas para Teste

### 1. JSONPlaceholder (Fake REST API)

**GET - Listar Posts**
- URL: `https://jsonplaceholder.typicode.com/posts`
- Método: GET
- Headers: `Content-Type:application/json`

**GET - Post Específico**
- URL: `https://jsonplaceholder.typicode.com/posts/1`
- Método: GET

**POST - Criar Post**
- URL: `https://jsonplaceholder.typicode.com/posts`
- Método: POST
- Headers: `Content-Type:application/json`
- Body:
```json
{
  "title": "Meu novo post",
  "body": "Este é o conteúdo do meu post",
  "userId": 1
}
```

**PUT - Atualizar Post**
- URL: `https://jsonplaceholder.typicode.com/posts/1`
- Método: PUT
- Headers: `Content-Type:application/json`
- Body:
```json
{
  "id": 1,
  "title": "Post atualizado",
  "body": "Conteúdo atualizado",
  "userId": 1
}
```

**DELETE - Deletar Post**
- URL: `https://jsonplaceholder.typicode.com/posts/1`
- Método: DELETE

### 2. httpbin.org (Serviço de teste HTTP)

**GET com Parâmetros**
- URL: `https://httpbin.org/get?param1=valor1&param2=valor2`
- Método: GET

**POST com JSON**
- URL: `https://httpbin.org/post`
- Método: POST
- Headers: `Content-Type:application/json`
- Body:
```json
{
  "nome": "João",
  "idade": 30,
  "email": "joao@email.com"
}
```

**Headers Customizados**
- URL: `https://httpbin.org/headers`
- Método: GET
- Headers: 
```
User-Agent:MeuApp/1.0
X-Custom-Header:valor-personalizado
Authorization:Bearer token123
```

### 3. ReqRes (API de teste)

**GET - Listar Usuários**
- URL: `https://reqres.in/api/users?page=2`
- Método: GET

**POST - Criar Usuário**
- URL: `https://reqres.in/api/users`
- Método: POST
- Headers: `Content-Type:application/json`
- Body:
```json
{
  "name": "morpheus",
  "job": "leader"
}
```

### 4. Cat Facts API

**GET - Fato Aleatório sobre Gatos**
- URL: `https://catfact.ninja/fact`
- Método: GET

### 5. Advice Slip API

**GET - Conselho Aleatório**
- URL: `https://api.adviceslip.com/advice`
- Método: GET

## Testando APIs Locais

Se você tiver um servidor local rodando, pode testar com:

**Servidor Local Típico**
- URL: `http://localhost:3000/api/endpoint`
- URL: `http://localhost:8080/api/users`
- URL: `http://127.0.0.1:5000/api/data`

## Dicas de Teste

1. **Comece com GET**: Use requisições GET primeiro para testar a conectividade
2. **Verifique Headers**: Sempre configure o Content-Type correto
3. **JSON Válido**: Certifique-se de que o JSON no body está válido
4. **URLs Completas**: Use URLs completas com http:// ou https://
5. **Timeouts**: Requisições têm timeout de 30 segundos
6. **Erros de CORS**: Algumas APIs podem ter restrições de CORS

## Códigos de Status HTTP Comuns

- **200**: OK - Requisição bem-sucedida
- **201**: Created - Recurso criado com sucesso
- **400**: Bad Request - Erro na requisição
- **401**: Unauthorized - Não autorizado
- **404**: Not Found - Recurso não encontrado
- **500**: Internal Server Error - Erro no servidor
