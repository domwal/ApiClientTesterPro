import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog
import requests
import json
import os
from datetime import datetime
import threading


class ApiClientApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ApiClient Tester Pro - Testador de API")
        self.root.geometry("1200x700")
        self.root.configure(bg='#f0f0f0')
        
        # Variáveis
        self.history = []
        self.collections = {}
        self.current_collection = None
        self.collections_file = "collections.json"
        
        # Carregar collections salvas
        self.load_collections()
        
        self.setup_ui()
        
    def setup_ui(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Título
        title_label = ttk.Label(main_frame, text="ApiClient Tester Pro", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Frame para requisição
        request_frame = ttk.LabelFrame(main_frame, text="Requisição", padding="10")
        request_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        request_frame.columnconfigure(1, weight=1)
        
        # Método HTTP
        ttk.Label(request_frame, text="Método:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        self.method_var = tk.StringVar(value="GET")
        method_combo = ttk.Combobox(request_frame, textvariable=self.method_var, 
                                   values=["GET", "POST", "PUT", "DELETE", "PATCH"], 
                                   state="readonly", width=10)
        method_combo.grid(row=0, column=1, sticky=tk.W, padx=(0, 10))
        
        # URL
        ttk.Label(request_frame, text="URL:").grid(row=0, column=2, sticky=tk.W, padx=(10, 10))
        self.url_var = tk.StringVar()
        url_entry = ttk.Entry(request_frame, textvariable=self.url_var, width=50)
        url_entry.grid(row=0, column=3, sticky=(tk.W, tk.E), padx=(0, 10))
        request_frame.columnconfigure(3, weight=1)
        
        # Botão Enviar
        send_button = ttk.Button(request_frame, text="Enviar", command=self.send_request)
        send_button.grid(row=0, column=4, padx=(10, 0))
        
        # Notebook para abas
        notebook = ttk.Notebook(request_frame)
        notebook.grid(row=1, column=0, columnspan=5, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(20, 0))
        
        # Aba Headers
        headers_frame = ttk.Frame(notebook)
        notebook.add(headers_frame, text="Headers")
        
        # Frame para adicionar headers
        add_header_frame = ttk.LabelFrame(headers_frame, text="Adicionar Header", padding="10")
        add_header_frame.pack(fill=tk.X, padx=10, pady=(10, 5))
        
        # Configurar grid
        add_header_frame.columnconfigure(1, weight=1)
        add_header_frame.columnconfigure(3, weight=1)
        
        # Tipo de header
        ttk.Label(add_header_frame, text="Tipo:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
        self.header_type_var = tk.StringVar()
        self.header_type_combo = ttk.Combobox(add_header_frame, textvariable=self.header_type_var, 
                                             state="readonly", width=20)
        self.header_type_combo.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 10))
        self.header_type_combo.bind('<<ComboboxSelected>>', self.on_header_type_selected)
        
        # Valor do header
        ttk.Label(add_header_frame, text="Valor:").grid(row=0, column=2, sticky=tk.W, padx=(0, 5))
        self.header_value_var = tk.StringVar()
        self.header_value_combo = ttk.Combobox(add_header_frame, textvariable=self.header_value_var, 
                                              width=30)
        self.header_value_combo.grid(row=0, column=3, sticky=(tk.W, tk.E), padx=(0, 10))
        
        # Botão adicionar
        add_button = ttk.Button(add_header_frame, text="Adicionar", command=self.add_header)
        add_button.grid(row=0, column=4, padx=(5, 0))
        
        # Frame para headers ativos
        active_headers_frame = ttk.LabelFrame(headers_frame, text="Headers Ativos (duplo clique para editar)", padding="10")
        active_headers_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Treeview para mostrar headers
        columns = ('Header', 'Valor')
        self.headers_tree = ttk.Treeview(active_headers_frame, columns=columns, show='headings', height=8)
        self.headers_tree.heading('Header', text='Header')
        self.headers_tree.heading('Valor', text='Valor')
        self.headers_tree.column('Header', width=200)
        self.headers_tree.column('Valor', width=300)
        
        # Scrollbar para treeview
        tree_scrollbar = ttk.Scrollbar(active_headers_frame, orient=tk.VERTICAL, command=self.headers_tree.yview)
        self.headers_tree.configure(yscrollcommand=tree_scrollbar.set)
        
        self.headers_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tree_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Adicionar evento de duplo clique para editar
        self.headers_tree.bind('<Double-1>', self.edit_header)
        
        # Botões para gerenciar headers
        header_buttons_frame = ttk.Frame(active_headers_frame)
        header_buttons_frame.pack(fill=tk.X, pady=(10, 0))
        
        ttk.Button(header_buttons_frame, text="Editar Selecionado", command=self.edit_selected_header).pack(fill=tk.X, pady=(0, 5))
        ttk.Button(header_buttons_frame, text="Remover Selecionado", command=self.remove_header).pack(fill=tk.X, pady=(0, 5))
        ttk.Button(header_buttons_frame, text="Limpar Todos", command=self.clear_headers).pack(fill=tk.X)
        
        # Inicializar dados dos headers
        self.setup_header_data()
        
        # Aba Body
        body_frame = ttk.Frame(notebook)
        notebook.add(body_frame, text="Body")
        
        # Body
        ttk.Label(body_frame, text="Body da Requisição").pack(anchor=tk.W, pady=(10, 5))
        self.body_text = scrolledtext.ScrolledText(body_frame, height=6, width=80)
        self.body_text.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Frame para resposta
        response_frame = ttk.LabelFrame(main_frame, text="Resposta", padding="10")
        response_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(10, 0))
        response_frame.columnconfigure(0, weight=1)
        response_frame.rowconfigure(1, weight=1)
        
        # Status da resposta
        self.status_label = ttk.Label(response_frame, text="Status: -", font=("Arial", 10, "bold"))
        self.status_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 10))
        
        # Resposta
        self.response_text = scrolledtext.ScrolledText(response_frame, height=15, width=80)
        self.response_text.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Frame para histórico e collections
        right_frame = ttk.Frame(main_frame)
        right_frame.grid(row=1, column=3, rowspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(10, 0))
        right_frame.columnconfigure(0, weight=1)
        right_frame.rowconfigure(2, weight=1)
        
        # Collections
        collections_frame = ttk.LabelFrame(right_frame, text="Collections", padding="10")
        collections_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        collections_frame.columnconfigure(0, weight=1)
        
        # Botões de collections
        collections_buttons_frame = ttk.Frame(collections_frame)
        collections_buttons_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        collections_buttons_frame.columnconfigure(0, weight=1)
        collections_buttons_frame.columnconfigure(1, weight=1)
        collections_buttons_frame.columnconfigure(2, weight=1)
        
        new_collection_button = ttk.Button(collections_buttons_frame, text="Nova", command=self.new_collection)
        new_collection_button.grid(row=0, column=0, padx=(0, 3), sticky=(tk.W, tk.E))
        
        save_request_button = ttk.Button(collections_buttons_frame, text="Salvar Req.", command=self.save_request_to_collection)
        save_request_button.grid(row=0, column=1, padx=(3, 3), sticky=(tk.W, tk.E))
        
        delete_collection_button = ttk.Button(collections_buttons_frame, text="Deletar", command=self.delete_collection)
        delete_collection_button.grid(row=0, column=2, padx=(3, 0), sticky=(tk.W, tk.E))
        
        # Dropdown de collections
        ttk.Label(collections_frame, text="Collection Atual:").grid(row=1, column=0, sticky=tk.W, pady=(0, 5))
        self.collection_var = tk.StringVar()
        self.collection_combo = ttk.Combobox(collections_frame, textvariable=self.collection_var, state="readonly", width=25)
        self.collection_combo.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        self.collection_combo.bind('<<ComboboxSelected>>', self.on_collection_selected)
        
        # Lista de requisições da collection
        ttk.Label(collections_frame, text="Requisições:").grid(row=3, column=0, sticky=tk.W, pady=(0, 5))
        self.requests_listbox = tk.Listbox(collections_frame, height=8)
        self.requests_listbox.grid(row=4, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        self.requests_listbox.bind('<Double-1>', self.load_request_from_collection)
        
        # Botões de gerenciamento
        collection_mgmt_frame = ttk.Frame(collections_frame)
        collection_mgmt_frame.grid(row=5, column=0, sticky=(tk.W, tk.E))
        collection_mgmt_frame.columnconfigure(0, weight=1)
        collection_mgmt_frame.columnconfigure(1, weight=1)
        collection_mgmt_frame.columnconfigure(2, weight=1)
        
        delete_req_button = ttk.Button(collection_mgmt_frame, text="Del. Req.", command=self.delete_request_from_collection)
        delete_req_button.grid(row=0, column=0, padx=(0, 3), sticky=(tk.W, tk.E))
        
        import_button = ttk.Button(collection_mgmt_frame, text="Importar", command=self.import_collection)
        import_button.grid(row=0, column=1, padx=(3, 3), sticky=(tk.W, tk.E))
        
        export_button = ttk.Button(collection_mgmt_frame, text="Exportar", command=self.export_collection)
        export_button.grid(row=0, column=2, padx=(3, 0), sticky=(tk.W, tk.E))
        
        # Frame para histórico
        history_frame = ttk.LabelFrame(right_frame, text="Histórico", padding="10")
        history_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(10, 0))
        history_frame.columnconfigure(0, weight=1)
        history_frame.rowconfigure(1, weight=1)
        
        # Botão limpar histórico
        clear_button = ttk.Button(history_frame, text="Limpar Histórico", command=self.clear_history)
        clear_button.grid(row=0, column=0, pady=(0, 10))
        
        # Lista do histórico
        self.history_listbox = tk.Listbox(history_frame, height=8)
        self.history_listbox.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.history_listbox.bind('<Double-1>', self.load_from_history)
        
        # Scrollbar para histórico
        history_scrollbar = ttk.Scrollbar(history_frame, orient=tk.VERTICAL, command=self.history_listbox.yview)
        history_scrollbar.grid(row=1, column=1, sticky=(tk.N, tk.S))
        self.history_listbox.configure(yscrollcommand=history_scrollbar.set)
        
        # Configurar redimensionamento
        main_frame.rowconfigure(2, weight=1)
        main_frame.columnconfigure(2, weight=1)
        
        # Atualizar collections na inicialização
        self.update_collections_combo()
    
    def setup_header_data(self):
        """Configura os dados de headers comuns"""
        self.header_data = {
            "Content-Type": [
                "application/json",
                "application/xml",
                "application/x-www-form-urlencoded",
                "text/plain",
                "text/html",
                "text/xml",
                "multipart/form-data",
                "application/octet-stream"
            ],
            "Authorization": [
                "Bearer TOKEN_AQUI",
                "Basic dXNlcjpwYXNz",
                "API-Key SUA_API_KEY",
                "Token TOKEN_AQUI",
                "OAuth OAUTH_TOKEN"
            ],
            "Accept": [
                "application/json",
                "application/xml",
                "text/html",
                "text/plain",
                "*/*"
            ],
            "User-Agent": [
                "ApiClient-Tester-Pro/1.0",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                "ApiClientRuntime/7.0",
                "curl/7.68.0",
                "SeuApp/1.0"
            ],
            "Cache-Control": [
                "no-cache",
                "no-store",
                "max-age=0",
                "public, max-age=31536000",
                "private"
            ],
            "Access-Control-Allow-Origin": [
                "*",
                "https://localhost:3000",
                "https://seudominio.com"
            ],
            "X-API-Key": [
                "SUA_API_KEY_AQUI"
            ],
            "X-Custom-Header": [
                "valor_personalizado"
            ],
            "Cookie": [
                "session=abc123; token=xyz789"
            ],
            "Referer": [
                "https://seusite.com",
                "https://localhost:3000"
            ]
        }
        
        # Configurar combobox de tipos
        header_types = list(self.header_data.keys())
        self.header_type_combo['values'] = header_types
        
        # Adicionar headers padrão
        self.add_default_headers()
    
    def add_default_headers(self):
        """Adiciona headers padrão"""
        default_headers = [
            ("Content-Type", "application/json"),
            ("User-Agent", "ApiClient-Tester-Pro/1.0")
        ]
        
        for header, value in default_headers:
            self.headers_tree.insert('', 'end', values=(header, value))
    
    def on_header_type_selected(self, event):
        """Quando um tipo de header é selecionado"""
        selected_type = self.header_type_var.get()
        if selected_type in self.header_data:
            values = self.header_data[selected_type]
            self.header_value_combo['values'] = values
            if values:
                self.header_value_var.set(values[0])  # Selecionar primeiro valor
        else:
            self.header_value_combo['values'] = []
            self.header_value_var.set("")
    
    def add_header(self):
        """Adiciona um header à lista"""
        header_type = self.header_type_var.get().strip()
        header_value = self.header_value_var.get().strip()
        
        if not header_type:
            messagebox.showwarning("Aviso", "Selecione um tipo de header!")
            return
        
        if not header_value:
            messagebox.showwarning("Aviso", "Digite um valor para o header!")
            return
        
        # Verificar se header já existe
        for item in self.headers_tree.get_children():
            existing_header = self.headers_tree.item(item)['values'][0]
            if existing_header.lower() == header_type.lower():
                if messagebox.askyesno("Header Existente", 
                                      f"O header '{header_type}' já existe.\nDeseja substituir?"):
                    self.headers_tree.delete(item)
                    break
                else:
                    return
        
        # Adicionar header
        self.headers_tree.insert('', 'end', values=(header_type, header_value))
        
        # Limpar campos
        self.header_type_var.set("")
        self.header_value_var.set("")
        self.header_value_combo['values'] = []
    
    def edit_header(self, event):
        """Edita um header existente"""
        selected_item = self.headers_tree.selection()
        if not selected_item:
            return
        
        item = selected_item[0]
        header_data = self.headers_tree.item(item)['values']
        if not header_data:
            return
        
        header_name = header_data[0]
        header_value = header_data[1]
        
        # Dialog para editar header
        dialog = EditHeaderDialog(self.root, header_name, header_value, self.header_data)
        if dialog.result:
            new_header = dialog.result['header']
            new_value = dialog.result['value']
            
            # Verificar se o novo header já existe (exceto o atual)
            for other_item in self.headers_tree.get_children():
                if other_item != item:
                    existing_header = self.headers_tree.item(other_item)['values'][0]
                    if existing_header.lower() == new_header.lower():
                        if messagebox.askyesno("Header Existente", 
                                              f"O header '{new_header}' já existe.\nDeseja substituir ambos?"):
                            self.headers_tree.delete(other_item)
                            break
                        else:
                            return
            
            # Atualizar o header
            self.headers_tree.item(item, values=(new_header, new_value))
    
    def edit_selected_header(self):
        """Edita o header selecionado via botão"""
        selected_item = self.headers_tree.selection()
        if not selected_item:
            messagebox.showwarning("Aviso", "Selecione um header para editar!")
            return
        
        # Simular evento de duplo clique
        self.edit_header(None)
    
    def remove_header(self):
        """Remove o header selecionado"""
        selected_item = self.headers_tree.selection()
        if not selected_item:
            messagebox.showwarning("Aviso", "Selecione um header para remover!")
            return
        
        for item in selected_item:
            self.headers_tree.delete(item)
    
    def clear_headers(self):
        """Remove todos os headers"""
        if messagebox.askyesno("Confirmar", "Remover todos os headers?"):
            for item in self.headers_tree.get_children():
                self.headers_tree.delete(item)
    
    def get_headers_dict(self):
        """Retorna os headers como dicionário"""
        headers = {}
        for item in self.headers_tree.get_children():
            header, value = self.headers_tree.item(item)['values']
            headers[header] = value
        return headers
    
    def set_headers_from_dict(self, headers_dict):
        """Define headers a partir de um dicionário"""
        # Limpar headers existentes
        for item in self.headers_tree.get_children():
            self.headers_tree.delete(item)
        
        # Adicionar novos headers
        for header, value in headers_dict.items():
            self.headers_tree.insert('', 'end', values=(header, value))
        
    def parse_headers(self, headers_text=None):
        """Converte os headers em um dicionário (compatibilidade com método antigo)"""
        if headers_text:
            # Método antigo para compatibilidade
            headers = {}
            lines = headers_text.strip().split('\n')
            for line in lines:
                if ':' in line and line.strip():
                    key, value = line.split(':', 1)
                    headers[key.strip()] = value.strip()
            return headers
        else:
            # Novo método usando TreeView
            return self.get_headers_dict()
    
    def send_request(self):
        """Envia a requisição HTTP"""
        url = self.url_var.get().strip()
        if not url:
            messagebox.showerror("Erro", "Por favor, insira uma URL válida")
            return
            
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
            self.url_var.set(url)
        
        # Executar em thread separada para não travar a interface
        thread = threading.Thread(target=self._execute_request, args=(url,))
        thread.daemon = True
        thread.start()
    
    def _execute_request(self, url):
        """Executa a requisição em thread separada"""
        try:
            method = self.method_var.get()
            body_text = self.body_text.get("1.0", tk.END).strip()
            
            # Usar novo sistema de headers
            headers = self.get_headers_dict()
            
            # Preparar dados do body
            data = None
            if body_text and method in ['POST', 'PUT', 'PATCH']:
                try:
                    # Tentar interpretar como JSON
                    data = json.loads(body_text)
                except json.JSONDecodeError:
                    # Se não for JSON válido, enviar como texto
                    data = body_text
            
            # Fazer a requisição
            start_time = datetime.now()
            
            if method == 'GET':
                response = requests.get(url, headers=headers, timeout=30)
            elif method == 'POST':
                if isinstance(data, dict):
                    response = requests.post(url, json=data, headers=headers, timeout=30)
                else:
                    response = requests.post(url, data=data, headers=headers, timeout=30)
            elif method == 'PUT':
                if isinstance(data, dict):
                    response = requests.put(url, json=data, headers=headers, timeout=30)
                else:
                    response = requests.put(url, data=data, headers=headers, timeout=30)
            elif method == 'DELETE':
                response = requests.delete(url, headers=headers, timeout=30)
            elif method == 'PATCH':
                if isinstance(data, dict):
                    response = requests.patch(url, json=data, headers=headers, timeout=30)
                else:
                    response = requests.patch(url, data=data, headers=headers, timeout=30)
            
            end_time = datetime.now()
            response_time = (end_time - start_time).total_seconds() * 1000
            
            # Atualizar interface na thread principal
            self.root.after(0, self._update_response, response, response_time, url, method)
            
        except requests.exceptions.RequestException as e:
            self.root.after(0, self._show_error, f"Erro na requisição: {str(e)}")
        except Exception as e:
            self.root.after(0, self._show_error, f"Erro inesperado: {str(e)}")
    
    def _update_response(self, response, response_time, url, method):
        """Atualiza a interface com a resposta"""
        # Status
        status_text = f"Status: {response.status_code} {response.reason} | Tempo: {response_time:.2f}ms"
        if response.status_code < 300:
            status_color = "green"
        elif response.status_code < 400:
            status_color = "orange"
        else:
            status_color = "red"
        
        self.status_label.configure(text=status_text, foreground=status_color)
        
        # Resposta
        self.response_text.delete("1.0", tk.END)
        
        # Headers da resposta
        response_content = "=== HEADERS DA RESPOSTA ===\n"
        for key, value in response.headers.items():
            response_content += f"{key}: {value}\n"
        
        response_content += "\n=== BODY DA RESPOSTA ===\n"
        
        # Tentar formatar como JSON
        try:
            content_type = response.headers.get('content-type', '').lower()
            if 'application/json' in content_type:
                json_data = response.json()
                response_content += json.dumps(json_data, indent=2, ensure_ascii=False)
            else:
                response_content += response.text
        except:
            response_content += response.text
        
        self.response_text.insert("1.0", response_content)
        
        # Adicionar ao histórico
        self.add_to_history(method, url, response.status_code, response_time)
    
    def _show_error(self, error_message):
        """Mostra erro na interface"""
        self.status_label.configure(text=f"Erro: {error_message}", foreground="red")
        self.response_text.delete("1.0", tk.END)
        self.response_text.insert("1.0", f"Erro: {error_message}")
    
    def add_to_history(self, method, url, status_code, response_time):
        """Adiciona requisição ao histórico"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        history_item = {
            'method': method,
            'url': url,
            'status': status_code,
            'time': response_time,
            'timestamp': timestamp
        }
        
        self.history.append(history_item)
        
        # Atualizar listbox
        display_text = f"{timestamp} {method} {status_code}"
        self.history_listbox.insert(0, display_text)
        
        # Limitar histórico a 50 itens
        if len(self.history) > 50:
            self.history.pop()
            self.history_listbox.delete(tk.END)
    
    def load_from_history(self, event):
        """Carrega requisição do histórico"""
        selection = self.history_listbox.curselection()
        if selection:
            index = selection[0]
            if index < len(self.history):
                item = self.history[index]
                self.method_var.set(item['method'])
                self.url_var.set(item['url'])
                
                # Limpar headers e adicionar apenas Content-Type padrão
                self.clear_headers()
                self.add_default_headers()
    
    def clear_history(self):
        """Limpa o histórico"""
        self.history.clear()
        self.history_listbox.delete(0, tk.END)
    
    # Métodos para Collections
    def load_collections(self):
        """Carrega collections do arquivo JSON"""
        try:
            if os.path.exists(self.collections_file):
                with open(self.collections_file, 'r', encoding='utf-8') as f:
                    self.collections = json.load(f)
        except Exception as e:
            print(f"Erro ao carregar collections: {e}")
            self.collections = {}
    
    def save_collections(self):
        """Salva collections no arquivo JSON"""
        try:
            with open(self.collections_file, 'w', encoding='utf-8') as f:
                json.dump(self.collections, f, indent=2, ensure_ascii=False)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar collections: {e}")
    
    def update_collections_combo(self):
        """Atualiza o combobox de collections"""
        collection_names = list(self.collections.keys())
        self.collection_combo['values'] = collection_names
        
        # Se a collection atual não existe mais, selecionar a primeira disponível
        if self.current_collection not in collection_names:
            if collection_names:
                self.current_collection = collection_names[0]
                self.collection_var.set(self.current_collection)
            else:
                self.current_collection = None
                self.collection_var.set("")
        
        # Se não há collection atual mas há collections disponíveis, selecionar a primeira
        elif not self.current_collection and collection_names:
            self.current_collection = collection_names[0]
            self.collection_var.set(self.current_collection)
        
        self.update_requests_list()
    
    def new_collection(self):
        """Cria uma nova collection"""
        dialog = CollectionDialog(self.root, "Nova Collection")
        if dialog.result:
            name = dialog.result['name']
            description = dialog.result['description']
            
            if name in self.collections:
                messagebox.showerror("Erro", "Já existe uma collection com esse nome!")
                return
            
            self.collections[name] = {
                'name': name,
                'description': description,
                'requests': [],
                'created': datetime.now().isoformat()
            }
            
            self.current_collection = name
            self.collection_var.set(name)
            self.update_collections_combo()
            self.update_requests_list()
            self.save_collections()
            
            messagebox.showinfo("Sucesso", f"Collection '{name}' criada com sucesso!")
    
    def save_request_to_collection(self):
        """Salva a requisição atual em uma collection"""
        if not self.current_collection:
            messagebox.showwarning("Aviso", "Selecione ou crie uma collection primeiro!")
            return
        
        url = self.url_var.get().strip()
        if not url:
            messagebox.showwarning("Aviso", "Configure uma URL antes de salvar!")
            return
        
        # Dialog para nome da requisição
        dialog = RequestNameDialog(self.root)
        if not dialog.result:
            return
        
        request_name = dialog.result
        method = self.method_var.get()
        headers_dict = self.get_headers_dict()
        body_text = self.body_text.get("1.0", tk.END).strip()
        
        request_data = {
            'name': request_name,
            'method': method,
            'url': url,
            'headers': headers_dict,  # Agora salva como dicionário
            'body': body_text,
            'created': datetime.now().isoformat()
        }
        
        self.collections[self.current_collection]['requests'].append(request_data)
        self.update_requests_list()
        self.save_collections()
        
        messagebox.showinfo("Sucesso", f"Requisição '{request_name}' salva na collection!")
    
    def on_collection_selected(self, event):
        """Quando uma collection é selecionada"""
        self.current_collection = self.collection_var.get()
        self.update_requests_list()
    
    def update_requests_list(self):
        """Atualiza a lista de requisições da collection atual"""
        self.requests_listbox.delete(0, tk.END)
        if self.current_collection and self.current_collection in self.collections:
            requests_list = self.collections[self.current_collection]['requests']
            for req in requests_list:
                display_text = f"{req['method']} - {req['name']}"
                self.requests_listbox.insert(tk.END, display_text)
    
    def load_request_from_collection(self, event):
        """Carrega uma requisição da collection"""
        selection = self.requests_listbox.curselection()
        if selection and self.current_collection:
            index = selection[0]
            requests_list = self.collections[self.current_collection]['requests']
            if index < len(requests_list):
                req = requests_list[index]
                
                self.method_var.set(req['method'])
                self.url_var.set(req['url'])
                
                # Carregar headers
                headers = req.get('headers', {})
                if isinstance(headers, str):
                    # Compatibilidade com formato antigo
                    headers_dict = self.parse_headers(headers)
                    self.set_headers_from_dict(headers_dict)
                else:
                    # Formato novo (dicionário)
                    self.set_headers_from_dict(headers)
                
                self.body_text.delete("1.0", tk.END)
                self.body_text.insert("1.0", req['body'])
    
    def delete_request_from_collection(self):
        """Deleta uma requisição da collection"""
        selection = self.requests_listbox.curselection()
        if not selection:
            messagebox.showwarning("Aviso", "Selecione uma requisição para deletar!")
            return
        
        if not self.current_collection:
            return
        
        index = selection[0]
        requests_list = self.collections[self.current_collection]['requests']
        if index < len(requests_list):
            req_name = requests_list[index]['name']
            
            if messagebox.askyesno("Confirmar", f"Deletar requisição '{req_name}'?"):
                del requests_list[index]
                self.update_requests_list()
                self.save_collections()
                messagebox.showinfo("Sucesso", "Requisição deletada!")
    
    def export_collection(self):
        """Exporta uma collection para arquivo JSON"""
        if not self.current_collection:
            messagebox.showwarning("Aviso", "Selecione uma collection para exportar!")
            return
        
        filename = filedialog.asksaveasfilename(
            title="Exportar Collection",
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
            initialfile=f"{self.current_collection}.json"
        )
        
        if filename:
            try:
                collection_data = self.collections[self.current_collection]
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(collection_data, f, indent=2, ensure_ascii=False)
                messagebox.showinfo("Sucesso", f"Collection exportada para {filename}")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao exportar: {e}")
    
    def delete_collection(self):
        """Deleta uma collection inteira"""
        if not self.current_collection:
            messagebox.showwarning("Aviso", "Selecione uma collection para deletar!")
            return
        
        collection_name = self.current_collection
        
        # Confirmação dupla para evitar deletar por acidente
        if not messagebox.askyesno("Confirmar Exclusão", 
                                  f"Tem certeza que deseja deletar a collection '{collection_name}'?\n\n"
                                  f"Esta ação não pode ser desfeita!\n"
                                  f"Todas as requisições desta collection serão perdidas."):
            return
        
        # Segunda confirmação
        if not messagebox.askyesno("Confirmação Final", 
                                  f"ÚLTIMA CONFIRMAÇÃO:\n\n"
                                  f"Deletar permanentemente a collection '{collection_name}'?"):
            return
        
        try:
            # Remover a collection
            del self.collections[collection_name]
            
            # Resetar collection atual
            self.current_collection = None
            self.collection_var.set("")
            
            # Atualizar interface
            self.update_collections_combo()
            self.update_requests_list()
            
            # Salvar mudanças
            self.save_collections()
            
            messagebox.showinfo("Sucesso", f"Collection '{collection_name}' foi deletada com sucesso!")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao deletar collection: {e}")
    
    def import_collection(self):
        """Importa uma collection de arquivo JSON"""
        filename = filedialog.askopenfilename(
            title="Importar Collection",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if not filename:
            return
        
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                collection_data = json.load(f)
            
            # Validar estrutura básica
            if not isinstance(collection_data, dict) or 'name' not in collection_data:
                messagebox.showerror("Erro", "Arquivo não é uma collection válida!")
                return
            
            collection_name = collection_data['name']
            
            # Verificar se já existe
            if collection_name in self.collections:
                if not messagebox.askyesno("Collection Existente", 
                                          f"Já existe uma collection chamada '{collection_name}'.\n"
                                          f"Deseja substituir?"):
                    return
            
            # Importar collection
            self.collections[collection_name] = collection_data
            self.current_collection = collection_name
            self.collection_var.set(collection_name)
            
            # Atualizar interface
            self.update_collections_combo()
            self.update_requests_list()
            
            # Salvar mudanças
            self.save_collections()
            
            messagebox.showinfo("Sucesso", f"Collection '{collection_name}' importada com sucesso!")
            
        except json.JSONDecodeError:
            messagebox.showerror("Erro", "Arquivo JSON inválido!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao importar collection: {e}")


class CollectionDialog:
    def __init__(self, parent, title):
        self.result = None
        
        # Criar janela
        self.dialog = tk.Toplevel(parent)
        self.dialog.title(title)
        self.dialog.geometry("450x300")
        self.dialog.minsize(400, 280)
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        # Centralizar janela
        self.dialog.geometry("+%d+%d" % (parent.winfo_rootx() + 50, parent.winfo_rooty() + 50))
        
        # Frame principal
        main_frame = ttk.Frame(self.dialog, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Nome
        ttk.Label(main_frame, text="Nome da Collection:").pack(anchor=tk.W, pady=(0, 5))
        self.name_var = tk.StringVar()
        self.name_entry = ttk.Entry(main_frame, textvariable=self.name_var, width=45)
        self.name_entry.pack(fill=tk.X, pady=(0, 15))
        self.name_entry.focus()
        
        # Descrição
        ttk.Label(main_frame, text="Descrição (opcional):").pack(anchor=tk.W, pady=(0, 5))
        self.description_text = scrolledtext.ScrolledText(main_frame, height=6, width=45)
        self.description_text.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        # Botões
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Usar grid para melhor controle dos botões
        buttons_frame.columnconfigure(0, weight=1)
        
        cancel_button = ttk.Button(buttons_frame, text="Cancelar", command=self.cancel)
        cancel_button.grid(row=0, column=1, padx=(5, 0), sticky="e")
        
        create_button = ttk.Button(buttons_frame, text="Criar", command=self.ok)
        create_button.grid(row=0, column=2, padx=(10, 0), sticky="e")
        
        # Bind Enter
        self.dialog.bind('<Return>', lambda e: self.ok())
        self.dialog.bind('<Escape>', lambda e: self.cancel())
        
        # Aguardar resultado
        self.dialog.wait_window()
    
    def ok(self):
        name = self.name_var.get().strip()
        if not name:
            messagebox.showerror("Erro", "Nome da collection é obrigatório!")
            return
        
        description = self.description_text.get("1.0", tk.END).strip()
        
        self.result = {
            'name': name,
            'description': description
        }
        self.dialog.destroy()
    
    def cancel(self):
        self.dialog.destroy()


class RequestNameDialog:
    def __init__(self, parent):
        self.result = None
        
        # Criar janela
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Nome da Requisição")
        self.dialog.geometry("400x180")
        self.dialog.minsize(350, 160)
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        # Centralizar janela
        self.dialog.geometry("+%d+%d" % (parent.winfo_rootx() + 100, parent.winfo_rooty() + 100))
        
        # Frame principal
        main_frame = ttk.Frame(self.dialog, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Nome
        ttk.Label(main_frame, text="Nome da Requisição:").pack(anchor=tk.W, pady=(0, 10))
        self.name_var = tk.StringVar()
        self.name_entry = ttk.Entry(main_frame, textvariable=self.name_var, width=40)
        self.name_entry.pack(fill=tk.X, pady=(0, 30))
        self.name_entry.focus()
        
        # Botões
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Usar grid para melhor controle dos botões
        buttons_frame.columnconfigure(0, weight=1)
        
        cancel_button = ttk.Button(buttons_frame, text="Cancelar", command=self.cancel)
        cancel_button.grid(row=0, column=1, padx=(5, 0), sticky="e")
        
        save_button = ttk.Button(buttons_frame, text="Salvar", command=self.ok)
        save_button.grid(row=0, column=2, padx=(10, 0), sticky="e")
        
        # Bind Enter
        self.dialog.bind('<Return>', lambda e: self.ok())
        self.dialog.bind('<Escape>', lambda e: self.cancel())
        
        # Aguardar resultado
        self.dialog.wait_window()
    
    def ok(self):
        name = self.name_var.get().strip()
        if not name:
            messagebox.showerror("Erro", "Nome da requisição é obrigatório!")
            return
        
        self.result = name
        self.dialog.destroy()
    
    def cancel(self):
        self.dialog.destroy()


class EditHeaderDialog:
    def __init__(self, parent, header_name, header_value, header_data):
        self.result = None
        self.header_data = header_data
        
        # Criar janela
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Editar Header")
        self.dialog.geometry("450x200")
        self.dialog.minsize(400, 180)
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        # Centralizar janela
        self.dialog.geometry("+%d+%d" % (parent.winfo_rootx() + 100, parent.winfo_rooty() + 100))
        
        # Frame principal
        main_frame = ttk.Frame(self.dialog, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        ttk.Label(main_frame, text="Header:").grid(row=0, column=0, sticky=tk.W, pady=(0, 10))
        self.header_var = tk.StringVar(value=header_name)
        self.header_combo = ttk.Combobox(main_frame, textvariable=self.header_var, width=25)
        self.header_combo.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(10, 0), pady=(0, 10))
        self.header_combo['values'] = list(header_data.keys())
        self.header_combo.bind('<<ComboboxSelected>>', self.on_header_selected)
        
        # Valor
        ttk.Label(main_frame, text="Valor:").grid(row=1, column=0, sticky=tk.W, pady=(0, 20))
        self.value_var = tk.StringVar(value=header_value)
        self.value_combo = ttk.Combobox(main_frame, textvariable=self.value_var, width=40)
        self.value_combo.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(10, 0), pady=(0, 20))
        
        # Configurar valores iniciais
        if header_name in header_data:
            self.value_combo['values'] = header_data[header_name]
        
        # Configurar grid
        main_frame.columnconfigure(1, weight=1)
        
        # Botões
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 0))
        buttons_frame.columnconfigure(0, weight=1)
        
        cancel_button = ttk.Button(buttons_frame, text="Cancelar", command=self.cancel)
        cancel_button.grid(row=0, column=1, padx=(5, 0), sticky="e")
        
        save_button = ttk.Button(buttons_frame, text="Salvar", command=self.ok)
        save_button.grid(row=0, column=2, padx=(10, 0), sticky="e")
        
        # Bind Enter e Escape
        self.dialog.bind('<Return>', lambda e: self.ok())
        self.dialog.bind('<Escape>', lambda e: self.cancel())
        
        # Focar no campo valor
        self.value_combo.focus()
        
        # Aguardar resultado
        self.dialog.wait_window()
    
    def on_header_selected(self, event):
        """Quando um header é selecionado"""
        selected_header = self.header_var.get()
        if selected_header in self.header_data:
            values = self.header_data[selected_header]
            self.value_combo['values'] = values
            if values:
                self.value_var.set(values[0])
        else:
            self.value_combo['values'] = []
    
    def ok(self):
        header = self.header_var.get().strip()
        value = self.value_var.get().strip()
        
        if not header:
            messagebox.showerror("Erro", "Header é obrigatório!")
            return
        
        if not value:
            messagebox.showerror("Erro", "Valor é obrigatório!")
            return
        
        self.result = {
            'header': header,
            'value': value
        }
        self.dialog.destroy()
    
    def cancel(self):
        self.dialog.destroy()


def main():
    root = tk.Tk()
    app = ApiClientApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
