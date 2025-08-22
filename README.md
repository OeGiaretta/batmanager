# 🦇 BatManager

**BatManager** é um programa com **interface gráfica (GUI)** para gerenciamento de scripts.
Com ele, você pode **incluir, alterar, executar e excluir** scripts de forma prática.
Quando um script é executado, a **saída aparece diretamente na tela principal** do programa.

---

## ✨ Funcionalidades

* ➕ **Adicionar scripts** manualmente.
* ✏️ **Alterar scripts existentes**.
* ▶️ **Executar scripts** e visualizar a saída em tempo real.
* ❌ **Excluir scripts** desnecessários.
* 🖥️ **Saída exibida direto na interface**, sem precisar abrir o terminal.

---

## 🚀 Como usar

1. Abra o **BatManager**.
2. Escolha uma das opções no menu:

   * **Incluir** → adicionar um novo script.
   * **Alterar** → editar um script salvo.
   * **Executar** → rodar o script selecionado.
   * **Excluir** → remover scripts que não serão mais usados.
3. A saída da execução será exibida na janela principal.

---

## 🛠️ Tecnologias utilizadas

* **Linguagem**: Python
* **GUI**: Tkinter (ou PyQt, dependendo da implementação)
* **Execução**: módulo `subprocess` para rodar os scripts

---

## 📂 Estrutura básica

```bash
📦 BatManager
 ┣ 📜 main.py           # Arquivo principal do programa
 ┣ 📜 scripts.db/json   # Base de dados dos scripts
 ┣ 📜 README.md         # Documentação
 ┗ 📂 assets            # Ícones e recursos visuais
```

---

## 💡 Exemplo de uso

1. Adicione um script simples:

```python
print("BatManager funcionando!")
```

2. Clique em **Executar**.
3. A saída será exibida na janela principal:

```
BatManager funcionando!
```

---

## 📌 Requisitos

* Python 3.10+
* Bibliotecas necessárias:

  * `tkinter` (ou `pyqt5`)
  * `subprocess`

Instale dependências (se houver `requirements.txt`):

```bash
pip install -r requirements.txt
```

---

## 📜 Licença

Distribuído sob a licença **MIT**.
Você pode usar, modificar e compartilhar livremente.
