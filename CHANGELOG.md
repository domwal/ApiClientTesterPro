# Changelog - ApiClient Tester Pro

## Versão 1.3 - Interface de Headers Renovada (09/09/2025)

### 🎨 Nova Interface de Headers
- **Dropdown de Tipos**: Seleção visual de tipos de headers comuns
- **Valores Sugeridos**: Lista de valores apropriados para cada tipo de header
- **Interface TreeView**: Lista organizada dos headers ativos
- **Gerenciamento Visual**: Botões para adicionar, remover e limpar headers

### 📋 Headers Pré-configurados
- **Content-Type**: 8 tipos comuns (JSON, XML, Form, etc.)
- **Authorization**: 4 métodos (Bearer, Basic, API-Key, Token)
- **Accept**: 5 tipos de resposta aceitos
- **User-Agent**: 5 user agents comuns
- **Cache-Control**: 5 opções de cache
- **Headers Personalizados**: X-API-Key, X-Custom-Header, Cookie, etc.

### 🔄 Compatibilidade
- **Retrocompatibilidade**: Collections antigas são automaticamente convertidas
- **Novo Formato**: Headers salvos como objeto estruturado
- **Migração Transparente**: Conversão automática do formato texto para visual

### ✨ Melhorias de UX
- **Prevenção de Duplicatas**: Sistema pergunta antes de substituir headers existentes
- **Headers Padrão**: Content-Type e User-Agent adicionados automaticamente
- **Validação**: Interface previne erros de digitação
- **Personalização**: Valores podem ser editados mesmo após seleção

---

## Versão 1.2 - Melhorias na Interface (09/09/2025)

### 🔧 Correções de Interface
- **Janela "Nova Collection"**: Aumentada de 400x250 para 450x300 pixels
- **Janela "Nome da Requisição"**: Aumentada de 350x150 para 400x180 pixels
- **Tamanho mínimo**: Adicionado minsize() para evitar janelas muito pequenas
- **Layout dos botões**: Melhorado usando grid() ao invés de pack() para melhor posicionamento
- **Espaçamento**: Ajustado padding e margem dos botões para evitar sobreposição

### ✨ Melhorias Visuais
- **Campos de entrada**: Aumentados para melhor usabilidade
- **Botões**: Alinhamento consistente à direita
- **Espaçamento**: Margens adequadas entre elementos
- **Responsividade**: Janelas redimensionáveis com tamanho mínimo definido

### 🎯 Antes vs Depois
**Antes:**
- Botões cortados ou mal posicionados
- Janelas muito pequenas
- Layout inconsistente

**Depois:**
- Todos os botões visíveis e bem posicionados
- Tamanhos adequados para o conteúdo
- Layout profissional e consistente

### 💡 Detalhes Técnicos
- Uso de `minsize()` para definir tamanho mínimo das janelas
- Substituição de `pack(side=tk.RIGHT)` por `grid()` para melhor controle
- Ajuste de padding e espaçamento entre elementos
- Aumento da largura dos campos de entrada

---

## Versão 1.1 - Collections Completas (09/09/2025)

### 🆕 Novas Funcionalidades
- **Deletar Collections**: Remover collections inteiras com confirmação dupla
- **Importar Collections**: Carregar collections de arquivos JSON
- **Gerenciamento Aprimorado**: Interface completa para CRUD de collections

### 🛡️ Segurança
- Confirmação dupla para deletar collections
- Proteção contra perda acidental de dados
- Validação de arquivos de importação

---

## Versão 1.0 - Lançamento Inicial (09/09/2025)

### 🚀 Funcionalidades Principais
- **Requisições HTTP**: GET, POST, PUT, DELETE, PATCH
- **Collections**: Organização de requisições em grupos
- **Headers e Body**: Configuração completa de requisições
- **Histórico**: Últimas 50 requisições
- **Exportação**: Salvar collections em JSON
- **Interface GUI**: tkinter com layout profissional
