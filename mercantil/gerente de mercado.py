import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk


class MercantilApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mercantil | Lista de compras")
        self.geometry("900x600")
        self.minsize(760, 500)

        self.adicionar_produtos = {}
        self.compras = {}

        self._criar_menu()
        self._criar_interface()

    def _criar_menu(self):
        barra_menu = tk.Menu(self)

        menu_arquivo = tk.Menu(barra_menu, tearoff=False)
        menu_arquivo.add_command(label="Salvar compra", command=self.salvar_compras)
        menu_arquivo.add_separator()
        menu_arquivo.add_command(label="Sair", command=self.destroy)
        barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)

        menu_produtos = tk.Menu(barra_menu, tearoff=False)
        menu_produtos.add_command(
            label="Novo produto", command=self._focar_nome_produto
        )
        menu_produtos.add_command(
            label="Remover produto selecionado", command=self.remover_produto
        )
        barra_menu.add_cascade(label="Produtos", menu=menu_produtos)

        menu_compra = tk.Menu(barra_menu, tearoff=False)
        menu_compra.add_command(
            label="Adicionar produto selecionado", command=self.adicionar_a_compra
        )
        menu_compra.add_command(
            label="Remover item selecionado", command=self.remover_da_compra
        )
        menu_compra.add_command(label="Limpar compra", command=self.limpar_compra)
        barra_menu.add_cascade(label="Compra", menu=menu_compra)

        self.config(menu=barra_menu)

    def _criar_interface(self):
        principal = ttk.Frame(self, padding=18)
        principal.pack(fill="both", expand=True)
        principal.columnconfigure(0, weight=1)
        principal.rowconfigure(2, weight=1)

        ttk.Label(
            principal, text="Mercantil", font=("Segoe UI", 20, "bold")
        ).grid(row=0, column=0, sticky="w")
        ttk.Label(
            principal,
            text="Cadastre produtos e monte sua lista de compras.",
        ).grid(row=1, column=0, sticky="w", pady=(2, 14))

        formulario = ttk.LabelFrame(
            principal, text="Cadastro de produto", padding=12
        )
        formulario.grid(row=2, column=0, sticky="new")
        formulario.columnconfigure(1, weight=1)

        ttk.Label(formulario, text="Produto").grid(row=0, column=0, sticky="w")
        self.nome_produto = ttk.Entry(formulario)
        self.nome_produto.grid(row=1, column=0, sticky="ew", padx=(0, 12))
        self.nome_produto.bind("<Return>", self._adicionar_com_enter)

        ttk.Label(formulario, text="Preço (R$)").grid(row=0, column=1, sticky="w")
        self.preco_produto = ttk.Entry(formulario, width=16)
        self.preco_produto.grid(row=1, column=1, sticky="ew", padx=(0, 12))
        self.preco_produto.bind("<Return>", self._adicionar_com_enter)

        ttk.Button(
            formulario, text="Adicionar produto", command=self.adicionar_produto
        ).grid(row=1, column=2, sticky="ew")

        listas = ttk.Frame(principal)
        listas.grid(row=3, column=0, sticky="nsew", pady=(14, 0))
        principal.rowconfigure(3, weight=1)
        listas.columnconfigure(0, weight=1)
        listas.columnconfigure(2, weight=1)
        listas.rowconfigure(0, weight=1)

        quadro_catalogo = ttk.LabelFrame(listas, text="Produtos", padding=8)
        quadro_catalogo.grid(row=0, column=0, sticky="nsew")
        quadro_catalogo.columnconfigure(0, weight=1)
        quadro_catalogo.rowconfigure(0, weight=1)
        self.lista_produtos = self._criar_tabela(quadro_catalogo)
        self.lista_produtos.bind("<Double-1>", self._adicionar_com_duplo_clique)

        acoes = ttk.Frame(listas, padding=(10, 34))
        acoes.grid(row=0, column=1, sticky="ns")
        ttk.Button(
            acoes, text="Adicionar  →", command=self.adicionar_a_compra
        ).pack(fill="x", pady=(0, 8))
        ttk.Button(
            acoes, text="←  Remover", command=self.remover_da_compra
        ).pack(fill="x")

        quadro_compra = ttk.LabelFrame(listas, text="Lista de compras", padding=8)
        quadro_compra.grid(row=0, column=2, sticky="nsew")
        quadro_compra.columnconfigure(0, weight=1)
        quadro_compra.rowconfigure(0, weight=1)
        self.lista_compra = self._criar_tabela(quadro_compra)

        resumo = ttk.Frame(principal)
        resumo.grid(row=4, column=0, sticky="ew", pady=(14, 0))
        resumo.columnconfigure(0, weight=1)
        self.total_label = ttk.Label(
            resumo, text="Total: R$ 0,00", font=("Segoe UI", 13, "bold")
        )
        self.total_label.grid(row=0, column=0, sticky="w")
        ttk.Button(
            resumo, text="Salvar lista em TXT", command=self.salvar_compras
        ).grid(row=0, column=1, sticky="e")

        self.status = tk.StringVar(value="Pronto")
        ttk.Label(self, textvariable=self.status, anchor="w", padding=(12, 6)).pack(
            fill="x", side="bottom"
        )

    def _criar_tabela(self, pai):
        tabela = ttk.Treeview(
            pai, columns=("produto", "preco"), show="headings", selectmode="browse"
        )
        tabela.heading("produto", text="Produto")
        tabela.heading("preco", text="Preço")
        tabela.column("produto", anchor="w", width=180)
        tabela.column("preco", anchor="e", width=95)
        barra = ttk.Scrollbar(pai, orient="vertical", command=tabela.yview)
        tabela.configure(yscrollcommand=barra.set)
        tabela.grid(row=0, column=0, sticky="nsew")
        barra.grid(row=0, column=1, sticky="ns")
        return tabela

    def _focar_nome_produto(self):
        self.nome_produto.focus_set()

    def _adicionar_com_enter(self, _evento):
        self.adicionar_produto()

    def _adicionar_com_duplo_clique(self, _evento):
        self.adicionar_a_compra()

    def adicionar_produto(self):
        nome = self.nome_produto.get().strip()
        valor = self.preco_produto.get().strip().replace(",", ".")

        if not nome:
            messagebox.showwarning("Produto", "Digite o nome do produto.")
            self.nome_produto.focus_set()
            return

        try:
            preco = float(valor)
        except ValueError:
            messagebox.showerror("Preço inválido", "Digite um preço numérico.")
            self.preco_produto.focus_set()
            return

        if preco < 0:
            messagebox.showerror("Preço inválido", "O preço não pode ser negativo.")
            self.preco_produto.focus_set()
            return

        if nome in self.adicionar_produtos and not messagebox.askyesno(
            "Produto já cadastrado", f"Atualizar o preço de {nome}?"
        ):
            return

        self.adicionar_produtos[nome] = preco
        if nome in self.compras:
            self.compras[nome] = preco

        self.nome_produto.delete(0, tk.END)
        self.preco_produto.delete(0, tk.END)
        self._atualizar_tabelas()
        self.nome_produto.focus_set()
        self.status.set(f"{nome} cadastrado.")

    def adicionar_a_compra(self):
        selecao = self.lista_produtos.selection()
        if not selecao:
            messagebox.showinfo("Lista de compras", "Selecione um produto do catálogo.")
            return

        nome = selecao[0]
        self.compras[nome] = self.adicionar_produtos[nome]
        self._atualizar_tabelas()
        self.status.set(f"{nome} adicionado à compra.")

    def remover_produto(self):
        selecao = self.lista_produtos.selection()
        if not selecao:
            messagebox.showinfo("Produtos", "Selecione um produto do catálogo.")
            return

        nome = selecao[0]
        del self.adicionar_produtos[nome]
        self._atualizar_tabelas()
        self.status.set(f"{nome} removido do catálogo.")

    def remover_da_compra(self):
        selecao = self.lista_compra.selection()
        if not selecao:
            messagebox.showinfo("Lista de compras", "Selecione um item da compra.")
            return

        nome = selecao[0]
        del self.compras[nome]
        self._atualizar_tabelas()
        self.status.set(f"{nome} removido da compra.")

    def limpar_compra(self):
        if not self.compras:
            return
        if messagebox.askyesno("Limpar compra", "Remover todos os itens da compra?"):
            self.compras.clear()
            self._atualizar_tabelas()
            self.status.set("Lista de compras limpa.")

    def _atualizar_tabelas(self):
        for tabela, produtos in (
            (self.lista_produtos, self.adicionar_produtos),
            (self.lista_compra, self.compras),
        ):
            tabela.delete(*tabela.get_children())
            for nome, preco in sorted(produtos.items()):
                tabela.insert(
                    "", "end", iid=nome, values=(nome, f"R$ {preco:.2f}")
                )

        total = sum(self.compras.values())
        self.total_label.config(text=f"Total: R$ {total:.2f}")

    def salvar_compras(self):
        if not self.compras:
            messagebox.showwarning(
                "Lista vazia", "Adicione produtos à compra antes de salvar."
            )
            return

        caminho = Path(__file__).with_name("compras.txt")
        total = sum(self.compras.values())

        try:
            with caminho.open("w", encoding="utf-8") as arquivo:
                arquivo.write("Lista de compras\n")
                for nome, preco in self.compras.items():
                    arquivo.write(f"{nome} - R$ {preco:.2f}\n")
                arquivo.write(f"Total: R$ {total:.2f}\n")
        except OSError as erro:
            messagebox.showerror("Erro ao salvar", str(erro))
            return

        self.status.set(f"Lista salva em {caminho}")
        messagebox.showinfo("Lista salva", f"Arquivo salvo em:\n{caminho}")


if __name__ == "__main__":
    app = MercantilApp()
    app.mainloop()