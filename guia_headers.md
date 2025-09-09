# Guia de Headers - ApiClient Tester Pro

## 🎯 Nova Interface de Headers

### ✨ **Sistema Intuitivo**
A nova interface de headers oferece uma experiência muito mais amigável:

- **Dropdown de Tipos**: Selecione tipos de headers comuns
- **Valores Sugeridos**: Valores pré-definidos para cada tipo
- **Interface Visual**: Lista organizada dos headers ativos
- **Gerenciamento Fácil**: Adicionar, remover e editar headers

### 🔧 **Como Usar**

#### **1. Adicionar Header**
1. **Selecione o Tipo**: Clique no dropdown "Tipo" e escolha um header comum
2. **Escolha o Valor**: O dropdown "Valor" mostrará opções adequadas
3. **Personalize**: Você pode editar o valor ou digitar um personalizado
4. **Adicione**: Clique "Adicionar" para incluir na lista

#### **2. Gerenciar Headers**
- **Editar**: Duplo clique em um header na lista OU selecione e clique "Editar Selecionado"
- **Remover**: Selecione um header na lista e clique "Remover Selecionado"
- **Limpar Todos**: Clique "Limpar Todos" para remover todos os headers
- **Substituir**: Se adicionar um header que já existe, será perguntado se deseja substituir

### 📋 **Headers Disponíveis**

#### **Content-Type** (Tipo de Conteúdo)
- `application/json` - Para APIs REST com JSON
- `application/xml` - Para APIs XML
- `application/x-www-form-urlencoded` - Para formulários web
- `text/plain` - Texto simples
- `text/html` - HTML
- `multipart/form-data` - Para upload de arquivos

#### **Authorization** (Autenticação)
- `Bearer TOKEN_AQUI` - Tokens JWT/OAuth
- `Basic dXNlcjpwYXNz` - Autenticação básica (base64)
- `API-Key SUA_API_KEY` - Chaves de API
- `Token TOKEN_AQUI` - Tokens personalizados

#### **Accept** (Tipo de Resposta Aceita)
- `application/json` - Aceitar JSON
- `application/xml` - Aceitar XML
- `text/html` - Aceitar HTML
- `*/*` - Aceitar qualquer tipo

#### **User-Agent** (Identificação do Cliente)
- `ApiClient-Tester-Pro/1.0` - Identificação padrão
- `Mozilla/5.0 (Windows NT 10.0; Win64; x64)` - Simular navegador
- `PostmanRuntime/7.0` - Simular Postman
- `curl/7.68.0` - Simular curl
- `SeuApp/1.0` - Identificação personalizada

#### **Cache-Control** (Controle de Cache)
- `no-cache` - Não usar cache
- `no-store` - Não armazenar cache
- `max-age=0` - Cache expirado
- `public, max-age=31536000` - Cache público por 1 ano
- `private` - Cache privado

#### **Outros Headers Úteis**
- **X-API-Key**: Chaves de API personalizadas
- **X-Custom-Header**: Headers personalizados
- **Cookie**: Cookies de sessão
- **Referer**: URL de origem
- **Access-Control-Allow-Origin**: CORS

### 💡 **Exemplos Práticos**

#### **API REST com JSON**
```
Content-Type: application/json
Accept: application/json
User-Agent: ApiClient-Tester-Pro/1.0
```

#### **API com Autenticação**
```
Content-Type: application/json
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Accept: application/json
```

#### **API com Chave**
```
Content-Type: application/json
X-API-Key: sk-1234567890abcdef
Accept: application/json
```

#### **Formulário Web**
```
Content-Type: application/x-www-form-urlencoded
Accept: text/html
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
```

### 🚀 **Fluxo de Trabalho**

1. **Selecione o Tipo** no primeiro dropdown
2. **Escolha/Digite o Valor** no segundo dropdown
3. **Clique "Adicionar"** para incluir na lista
4. **Edite se necessário** - Duplo clique no header para editar
5. **Repita** para adicionar mais headers
6. **Faça a Requisição** - headers serão enviados automaticamente

### ⭐ **Vantagens da Nova Interface**

#### **Antes (Texto)**
- ❌ Formato manual: "Content-Type:application/json"
- ❌ Propenso a erros de digitação
- ❌ Difícil de lembrar headers exatos
- ❌ Sem validação ou sugestões

#### **Agora (Visual)**
- ✅ Interface intuitiva com dropdowns
- ✅ Valores pré-definidos para cada tipo
- ✅ Prevenção de erros de digitação
- ✅ Lista organizada e visual
- ✅ Fácil gerenciamento (adicionar/remover/editar)
- ✅ Edição rápida com duplo clique

### 🔄 **Compatibilidade**

- **Collections Antigas**: Automaticamente convertidas
- **Formato de Salvamento**: Headers salvos como objeto estruturado
- **Retrocompatibilidade**: Suporte a collections no formato antigo

### 🎯 **Dicas**

1. **Headers Padrão**: Content-Type e User-Agent são adicionados automaticamente
2. **Edição Rápida**: Duplo clique em qualquer header para editar rapidamente
3. **Substituição**: Se adicionar header existente, será perguntado sobre substituição
4. **Personalização**: Você pode editar valores sugeridos ou criar próprios
5. **Validação**: Interface previne headers duplicados
6. **Persistência**: Headers são salvos nas collections junto com as requisições
