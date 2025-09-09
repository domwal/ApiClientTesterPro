# 🚀 Como Executar o ApiClient Tester Pro

## ⚡ Execução Rápida

### **Opção 1: Scripts Automáticos**
```bash
# Windows
.\run.bat

# PowerShell
.\run.ps1
```

### **Opção 2: Manual**
```bash
# Ativar ambiente virtual
.\venv\Scripts\Activate.ps1

# Executar aplicativo
python app.py
```

## 📁 Estrutura de Arquivos

```
📁 ApiClient Tester Pro/
├── 🚀 app.py                     # Aplicativo principal
├── 📋 collections.json            # Collections salvas
├── 📝 requirements.txt            # Dependências
├── 🏃 run.bat / run.ps1           # Scripts de execução
├── 📖 README.md                   # Documentação principal
├── ℹ️ SOBRE.md                     # Informações do app
├── 📚 guia_headers.md             # Guia de headers
├── ⚡ guia_rapido_collections.md   # Guia rápido
├── 💡 exemplos.md                 # Exemplos de uso
├── 📅 CHANGELOG.md                # Histórico de versões
└── 📁 venv/                       # Ambiente virtual
```

## 🎯 Primeira Execução

1. **Execute** o aplicativo usando `run.bat`
2. **Explore** as collections de exemplo já incluídas
3. **Teste** uma requisição simples (ex: JSONPlaceholder)
4. **Crie** sua primeira collection personalizada

## 💡 Dicas Rápidas

- **Headers**: Use os dropdowns para configurar facilmente
- **Collections**: Organize suas requisições por projeto
- **Histórico**: Acesse rapidamente requisições anteriores
- **Export**: Faça backup das collections importantes

## 🆘 Problemas Comuns

### **Erro de Dependência**
```bash
pip install requests
```

### **Ambiente Virtual**
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install requests
```

### **Permissão PowerShell**
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

**ApiClient Tester Pro** está pronto para uso! 🎉
