# Projeto Avaliacao LLM

## Como Executar o Código

1. **Clone o repositório:**
    ```bash
    git clone https://github.com/ArturMSilva/projeto-avaliacao-llm.git
    cd projeto-avaliacao-llm
    ```

2. **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Execute o código:**
    ```bash
    python main.py
    ```

4. **Ao executar:**

    O vscode irá perguntar se quer inciar um ambiente virtual, clique em "Yes" e aguarde a instalação das dependências, caso não tenha as extensões do python, siga o passo a passo abaixo.

5. **Configurações necessárias:**

   - ✅ **Verifique a versão do Python:**  
     ```bash
     python --version  # Deve mostrar 3.8 ou superior
     ```

   - 🔌 **Extensão Python (se necessário):**  
     > *Siga caso não tenha a extensão instalada:*  
     > 1. Abra o VS Code  
     > 2. Clique no ícone de extensões (🔎)  
     > 3. Busque por **"Python"**  
     > 4. Instale a extensão oficial da Microsoft

## Estrutura do Projeto

- `main.py`: Arquivo principal para execução do código.
- `requirements.txt`: Lista de dependências do projeto.
- `README.md`: Este arquivo.

## Configurando .env

Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis de ambiente:

```env
GROQ_LLM_API_KEY="sua chave api da groqCloud"

GROQ_QWEN_API_KEY="sua chave api da groqCloud"

GOOGLE_API_KEY="sua chave api do gemini"
```

## Como Obter Chaves API Gratuitas da GroqCloud e Gemini

Neste tutorial, você aprenderá a obter chaves API gratuitas para:
1. **GroqCloud** (serviço de IA com modelos como Llama 3 e Mixtral)
2. **Gemini** (IA do Google, anteriormente conhecido como Bard)

## 1. Obter Chave API da GroqCloud (Grátis)

### Passo a Passo:
1. **Acesse o Site**:  
   Vá para [GroqCloud](https://console.groq.com/login).

2. **Cadastre-se**:  
   - Clique em "Sign Up"  
   - Use e-mail, Google ou GitHub para criar conta gratuita.

3. **Verificação de E-mail**:  
   Confirme seu e-mail através do link enviado pela Groq.

4. **Acesse a Dashboard**:  
   Após login, vá para [API Keys](https://console.groq.com/keys).

5. **Crie uma Chave**:  
   - Clique em "Create API Key"  
   - Nomeie sua chave (ex: "meu-projeto")  
   - Copie a chave gerada (⚠️ **Salve em local seguro!**)

---

## 2. Obter Chave API do Gemini (Google AI Studio - Grátis)

### Passo a Passo:
1. **Acesse o Google AI Studio**:  
   Vá para [Google AI Studio](https://aistudio.google.com/).

2. **Faça Login**:  
   Use sua conta Google (Gmail).

3. **Crie uma Chave**:  
   - No menu lateral, clique em "Get API Key"  
   - Selecione "Create API Key in new project"  
   - Copie a chave exibida (🔑 **Não compartilhe!**)

