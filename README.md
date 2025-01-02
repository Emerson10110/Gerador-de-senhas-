
---

# 🔐 Gerador de Senhas Fortes

Um projeto em Python para gerar senhas seguras, customizáveis e difíceis de quebrar! As senhas podem incluir uma combinação de letras maiúsculas, letras minúsculas, números e caracteres especiais, atendendo a diferentes níveis de segurança.

## ⚙️ Funcionalidades:

- **Comprimento Personalizável** 📏: Escolha o comprimento da sua senha.
- **Opções de Caracteres** 🔠🔢: Personalize para incluir letras maiúsculas, minúsculas, números e/ou caracteres especiais.
- **Simples e Eficiente** 🖥️: Fácil de usar e adaptar a qualquer necessidade de segurança.

## 🚀 Começando

### ✅ Pré-requisitos:

Para rodar este projeto, você precisa ter:
- **Python 3.x** instalado.

### 📥 Instalação:

1. Clone o repositório para sua máquina local:
   ```bash
   git clone https://github.com/Emerson10110/gerador-de-senhas-.git
   cd gerador-de-senhas-
   ```

2. Pronto! Agora você já pode executar o script.

## 🎉 Uso

Para usar o gerador de senhas, execute o script **`gerador_de_senhas.py`** diretamente:
```bash
python gerador_de_senhas.py
```

### Exemplo de Uso:

Abaixo um exemplo simples de como gerar uma senha usando o módulo `gerador_de_senhas`:

```python
# Importa o módulo gerador
from gerador_de_senhas import gerar_senha

# Gera uma senha com 12 caracteres
senha = gerar_senha(tamanho=12)
print(f'Sua senha forte gerada é: {senha}')
```

### 🔧 Personalização:

Você pode configurar o gerador de senhas ajustando os parâmetros diretamente na função `gerar_senha` no arquivo `gerador_de_senhas.py`. Aqui estão os parâmetros disponíveis:

- `tamanho` _(int)_: Define o comprimento da senha (padrão: 12).
- `incluir_maiusculas` _(bool)_: Inclui letras maiúsculas se `True`.
- `incluir_minusculas` _(bool)_: Inclui letras minúsculas se `True`.
- `incluir_numeros` _(bool)_: Inclui números se `True`.
- `incluir_especiais` _(bool)_: Inclui caracteres especiais se `True`.

#### Exemplo de Customização:

```python
# Exemplo de função personalizada
def gerar_senha(tamanho=16, incluir_maiusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_especiais=True):
    ...
```

## 💡 Exemplos de Configurações

1. **Senha com 8 caracteres, apenas letras e números:**
   ```python
   senha = gerar_senha(tamanho=8, incluir_especiais=False)
   ```

2. **Senha de 20 caracteres com letras, números e símbolos:**
   ```python
   senha = gerar_senha(tamanho=20)
   ```

## 🤝 Contribuições

Contribuições são sempre bem-vindas! Se você tiver sugestões ou encontrar algum problema, por favor, abra uma **issue** ou envie um **pull request**. 💡

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.

## 📬 Contato

Para mais informações, dúvidas ou sugestões, entre em contato: [the.emerson.araujo@gmail.com](mailto:the.emerson.araujo@gmail.com)

---
