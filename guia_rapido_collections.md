# Guia Rápido - Collections

## 🚀 Como Começar com Collections

### 1. **Primeira Vez**
   - Abra o aplicativo
   - Você verá collections de exemplo já carregadas
   - Selecione "Exemplo - JSONPlaceholder" no dropdown

### 2. **Testando Requisições Prontas**
   - Clique duas vezes em "Listar Todos os Posts"
   - Clique em "Enviar" para testar
   - Experimente outras requisições da lista

### 3. **Criando Sua Primeira Collection**
   ```
   1. Clique em "Nova Collection"
   2. Nome: "Meus Testes"
   3. Descrição: "Collection para meus testes de API"
   4. Clique "Criar"
   ```

### 4. **Salvando Requisições**
   ```
   1. Configure uma requisição (URL, método, etc.)
   2. Clique em "Salvar Req."
   3. Digite um nome: "Login API"
   4. Pronto! Requisição salva na collection
   ```

### 5. **Deletando Collections**
   ```
   1. Selecione a collection que deseja remover
   2. Clique em "Deletar" (botão vermelho)
   3. Confirme duas vezes (segurança)
   4. Collection e todas suas requisições serão removidas
   ```

### 6. **Importar/Exportar Collections**
   ```
   EXPORTAR:
   1. Selecione a collection
   2. Clique "Exportar"
   3. Escolha local e nome do arquivo
   
   IMPORTAR:
   1. Clique "Importar"
   2. Selecione arquivo .json
   3. Collection será adicionada ao app
   ```

## 📋 Fluxo de Trabalho

```
1. CRIAR COLLECTION
   ↓
2. CONFIGURAR REQUISIÇÃO
   ↓
3. SALVAR NA COLLECTION
   ↓
4. REPETIR PARA OUTRAS REQUISIÇÕES
   ↓
5. USAR QUANDO NECESSÁRIO
   ↓
6. EXPORTAR PARA BACKUP (opcional)
   ↓
7. DELETAR SE NÃO PRECISAR MAIS
```

## 🎯 Casos de Uso Comuns

### **Desenvolvimento de API**
- Crie collection "Projeto X - Dev"
- Salve todas as requisições do projeto
- Teste conforme desenvolve

### **Testes de Integração**
- Collection "Testes E2E"
- Sequência de requisições de um fluxo
- Login → Buscar → Criar → Atualizar → Deletar

### **Diferentes Ambientes**
- "API - Local" (localhost:3000)
- "API - Homologação" (test.api.com)
- "API - Produção" (api.com)

### **Por Funcionalidade**
- "Autenticação" (login, logout, refresh)
- "Usuários" (CRUD de usuários)
- "Produtos" (CRUD de produtos)

## 🔧 Dicas Úteis

### **Gerenciamento Seguro**
- ⚠️ **Deletar Collection**: Confirmação dupla para evitar acidentes
- 💾 **Sempre Exporte**: Faça backup antes de deletar
- 🔄 **Importe Facilmente**: Compartilhe collections via arquivos JSON

### **Nomenclatura**
- ✅ "Login com Email"
- ✅ "Buscar Usuário por ID"
- ✅ "Criar Produto - Admin"
- ❌ "teste1", "req2", "api"

### **Organização**
- Use collections por contexto
- Mantenha requisições relacionadas juntas
- Exporte collections importantes

### **Headers Reutilizáveis**
```
Content-Type:application/json
Authorization:Bearer seu_token
User-Agent:SeuApp/1.0
```

## 📁 Arquivos Gerados

- **`collections.json`** - Todas suas collections
- **`NomeCollection.json`** - Collections exportadas

## ⚡ Atalhos e Botões

### **Botões Principais**
- **Nova** - Criar nova collection
- **Salvar Req.** - Salvar requisição atual
- **Deletar** - ⚠️ Remover collection inteira

### **Botões de Gerenciamento**
- **Del. Req.** - Deletar requisição específica
- **Importar** - Carregar collection de arquivo
- **Exportar** - Salvar collection em arquivo

### **Ações Rápidas**
- **Duplo-clique** na requisição = Carrega nos campos
- **Enter** nos dialogs = Confirma
- **Escape** nos dialogs = Cancela

## 🎉 Exemplo Prático

### Criando Collection para API de Blog

1. **Nova Collection**: "Blog API - Local"
2. **Salvar Requisições**:
   - GET `/posts` → "Listar Posts"
   - GET `/posts/1` → "Ver Post"
   - POST `/posts` → "Criar Post"
   - PUT `/posts/1` → "Editar Post"
   - DELETE `/posts/1` → "Deletar Post"

3. **Usar**: Selecione no dropdown e teste!

## 🚨 Lembrete Importante

- Collections são salvas automaticamente
- Use "Exportar" para backup
- Requisições ficam organizadas por collection
- Histórico continua separado das collections
