# ApiClient Tester Pro

Um aplicativo GUI em Python que oferece funcionalidades profissionais para teste de APIs REST, similar ao Postman.

## Funcionalidades

- **Métodos HTTP**: Suporte para GET, POST, PUT, DELETE e PATCH
- **Headers Intuitivos**: Interface visual com dropdown de tipos e valores sugeridos
- **Body de Requisição**: Envie dados JSON ou texto no body da requisição
- **Visualização de Resposta**: Veja os headers e body da resposta formatados
- **Collections**: Organize e salve grupos de requisições relacionadas
- **Gerenciamento Completo**: Criar, deletar, importar e exportar collections
- **Persistência**: Collections são salvas automaticamente em arquivo JSON
- **Exportação**: Exporte collections para compartilhar ou fazer backup
- **Histórico**: Mantenha um histórico das últimas 50 requisições
- **Interface Intuitiva**: Interface gráfica amigável usando tkinter

## Instalação

1. Certifique-se de ter Python 3.6+ instalado
2. Clone ou baixe este projeto
3. Crie e ative um ambiente virtual:
   ```bash
   # Criar ambiente virtual
   python -m venv venv
   
   # Ativar no Windows (PowerShell)
   .\venv\Scripts\Activate.ps1
   
   # Ativar no Windows (CMD)
   .\venv\Scripts\activate.bat
   
   # Ativar no Linux/Mac
   source venv/bin/activate
   ```
4. Instale as dependências:
   ```bash
   pip install requests
   ```

## Como Usar

### Opção 1: Usando os scripts prontos
- **Windows**: Execute `run.bat` ou `run.ps1`
- Estes scripts automaticamente ativam o ambiente virtual e executam o app

### Opção 2: Manual
1. Ative o ambiente virtual:
   ```bash
   # Windows PowerShell
   .\venv\Scripts\Activate.ps1
   
   # Windows CMD
   .\venv\Scripts\activate.bat
   ```

2. Execute o aplicativo:
   ```bash
   python app.py
   ```

2. **Fazendo uma Requisição**:
   - Selecione o método HTTP (GET, POST, PUT, DELETE, PATCH)
   - Digite a URL da API
   - Configure headers na aba "Headers" usando os dropdowns intuitivos
   - Se necessário, adicione dados na aba "Body" 
   - Clique em "Enviar"

3. **Usando Collections**:
   - Clique em "Nova" para criar uma collection
   - Configure uma requisição e clique em "Salvar Req." para salvar
   - Selecione collections no dropdown para trocar entre elas
   - Clique duas vezes em uma requisição salva para carregá-la
   - Use "Deletar" para remover collections inteiras (com confirmação dupla)
   - Use "Exportar"/"Importar" para compartilhar collections

4. **Visualizando a Resposta**:
   - O status da resposta aparecerá com código de status e tempo de resposta
   - Headers e body da resposta são exibidos na área de resposta
   - Respostas JSON são automaticamente formatadas

5. **Usando o Histórico**:
   - Todas as requisições ficam salvas no histórico
   - Clique duas vezes em um item do histórico para recarregar a requisição
   - Use "Limpar Histórico" para limpar a lista

## Exemplos de Uso

### Requisição GET Simples
- Método: GET
- URL: `https://jsonplaceholder.typicode.com/posts/1`
- Headers: (padrão)

### Requisição POST com JSON
- Método: POST
- URL: `https://jsonplaceholder.typicode.com/posts`
- Headers: `Content-Type:application/json`
- Body:
  ```json
  {
    "title": "Meu Post",
    "body": "Conteúdo do post",
    "userId": 1
  }
  ```

### Testando API Local
- Método: GET
- URL: `http://localhost:3000/api/users`
- Headers: `Authorization:Bearer seu_token_aqui`

## Recursos Técnicos

- **Interface**: tkinter (biblioteca padrão do Python)
- **Requisições HTTP**: biblioteca `requests`
- **Threading**: Requisições executadas em threads separadas para não travar a interface
- **Persistência**: Collections salvas em arquivo JSON local
- **Formatação JSON**: Respostas JSON são automaticamente formatadas
- **Tratamento de Erros**: Erros de rede e de parsing são tratados adequadamente

## Características da Interface

- **Área de Requisição**: Configure método, URL, headers e body
- **Abas Organizadas**: Headers e Body em abas separadas para melhor organização
- **Collections**: Painel dedicado para organizar e gerenciar groups de requisições
- **Área de Resposta**: Visualização clara do status, headers e body da resposta
- **Painel de Histórico**: Lista lateral com histórico de requisições
- **Redimensionável**: Interface se adapta ao redimensionamento da janela

## Limitações

- Histórico limitado a 50 requisições (para performance)
- Timeout padrão de 30 segundos para requisições
- Não suporta upload de arquivos (pode ser adicionado futuramente)
- Não salva dados entre sessões (histórico é perdido ao fechar o app)

## Possíveis Melhorias Futuras

- Salvar/carregar coleções de requisições
- Suporte a autenticação OAuth
- Upload de arquivos
- Temas dark/light
- Export de requisições/respostas
- Variáveis de ambiente
- Testes automatizados
