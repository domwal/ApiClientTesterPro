# Collections - Guia de Uso

## O que são Collections?

Collections são grupos organizados de requisições HTTP que permitem:
- Organizar requisições relacionadas
- Salvar e reutilizar requisições
- Compartilhar grupos de testes
- Exportar collections para outros desenvolvedores

## Como Usar Collections

### 1. Criar uma Nova Collection
1. Clique em "Nova Collection"
2. Digite o nome (ex: "API de Usuários")
3. Adicione uma descrição opcional
4. Clique em "Criar"

### 2. Salvar Requisições
1. Configure sua requisição (método, URL, headers, body)
2. Clique em "Salvar Req."
3. Digite um nome descritivo para a requisição
4. A requisição será salva na collection atual

### 3. Usar Requisições Salvas
1. Selecione uma collection no dropdown
2. Clique duas vezes em uma requisição da lista
3. A requisição será carregada nos campos

### 4. Gerenciar Collections
- **Deletar Requisição**: Selecione e clique em "Deletar Req."
- **Exportar**: Clique em "Exportar" para salvar a collection em arquivo JSON

## Exemplos de Collections

### Collection: "JSONPlaceholder API"
**Descrição**: Testes da API pública JSONPlaceholder

**Requisições:**
1. **Listar Posts**
   - Método: GET
   - URL: https://jsonplaceholder.typicode.com/posts
   - Headers: Content-Type:application/json

2. **Criar Post**
   - Método: POST
   - URL: https://jsonplaceholder.typicode.com/posts
   - Headers: Content-Type:application/json
   - Body:
   ```json
   {
     "title": "Meu Post",
     "body": "Conteúdo do post",
     "userId": 1
   }
   ```

3. **Buscar Post**
   - Método: GET
   - URL: https://jsonplaceholder.typicode.com/posts/1
   - Headers: Content-Type:application/json

4. **Atualizar Post**
   - Método: PUT
   - URL: https://jsonplaceholder.typicode.com/posts/1
   - Headers: Content-Type:application/json
   - Body:
   ```json
   {
     "id": 1,
     "title": "Post Atualizado",
     "body": "Novo conteúdo",
     "userId": 1
   }
   ```

5. **Deletar Post**
   - Método: DELETE
   - URL: https://jsonplaceholder.typicode.com/posts/1

### Collection: "API Local - Desenvolvimento"
**Descrição**: Testes do ambiente de desenvolvimento local

**Requisições:**
1. **Login**
   - Método: POST
   - URL: http://localhost:3000/api/auth/login
   - Headers: Content-Type:application/json
   - Body:
   ```json
   {
     "email": "admin@test.com",
     "password": "123456"
   }
   ```

2. **Listar Usuários**
   - Método: GET
   - URL: http://localhost:3000/api/users
   - Headers: 
   ```
   Content-Type:application/json
   Authorization:Bearer SEU_TOKEN_AQUI
   ```

3. **Criar Usuário**
   - Método: POST
   - URL: http://localhost:3000/api/users
   - Headers:
   ```
   Content-Type:application/json
   Authorization:Bearer SEU_TOKEN_AQUI
   ```
   - Body:
   ```json
   {
     "name": "João Silva",
     "email": "joao@test.com",
     "role": "user"
   }
   ```

### Collection: "Testes de API Externa"
**Descrição**: Testes com APIs de terceiros

**Requisições:**
1. **CEP - ViaCEP**
   - Método: GET
   - URL: https://viacep.com.br/ws/01310-100/json/

2. **Clima - OpenWeather**
   - Método: GET
   - URL: https://api.openweathermap.org/data/2.5/weather?q=São Paulo&appid=SUA_API_KEY

3. **GitHub - Repositórios**
   - Método: GET
   - URL: https://api.github.com/users/octocat/repos
   - Headers: User-Agent:MeuApp/1.0

## Dicas para Organizar Collections

### 1. Nomenclatura Clara
- Use nomes descritivos: "API Usuários - Produção"
- Inclua ambiente: "Local", "Desenvolvimento", "Produção"
- Agrupe por funcionalidade: "Autenticação", "CRUD Produtos"

### 2. Organização por Contexto
- **Por Ambiente**: Dev, Test, Prod
- **Por Módulo**: Usuários, Produtos, Pedidos
- **Por Fluxo**: Onboarding, Checkout, Relatórios

### 3. Documentação
- Use descrições nas collections
- Nomeie requisições de forma clara
- Mantenha headers organizados

### 4. Versionamento
- Exporte collections importantes
- Mantenha backups
- Use controle de versão se necessário

## Fluxo de Trabalho Sugerido

1. **Desenvolvimento**:
   - Crie collection "Projeto X - Dev"
   - Adicione requisições conforme desenvolve
   - Teste endpoints locais

2. **Teste**:
   - Duplique para "Projeto X - Test"
   - Ajuste URLs para ambiente de teste
   - Execute testes de integração

3. **Produção**:
   - Crie "Projeto X - Prod"
   - Configure URLs de produção
   - Use para troubleshooting

4. **Compartilhamento**:
   - Exporte collections importantes
   - Compartilhe com equipe
   - Documente casos de uso
