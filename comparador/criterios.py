PROMPT_AVALIACAO = """
Analise as respostas a seguir com base nos seguintes critérios:  

1. **Clareza**: A resposta é compreensível, bem estruturada e de fácil leitura?  
2. **Relevância**: A resposta está alinhada com a pergunta e fornece informações úteis?  
3. **Precisão**: A resposta contém informações corretas, bem fundamentadas e verificáveis?  
4. **Concisão**: A resposta é direta ao ponto, evitando informações desnecessárias ou redundantes?  
5. **Criatividade**: A resposta apresenta uma abordagem inovadora ou diferenciada?  

**Respostas a serem avaliadas:**  
- **Resposta 1 (Qwen):** {resposta_qwen}  
- **Resposta 2 (Llama):** {resposta_llama}  
- **Resposta 3 (Gemini):** {resposta_gemini}  

### **Instruções para avaliação:**  
- Para cada resposta, forneça uma análise detalhada destacando seus pontos fortes e fracos com base nos critérios acima.  
- Seja objetivo e imparcial na avaliação.  
- Leve em conta que sua própria avaliação também está sendo julgada pela qualidade da análise.  

### **Formato de saída esperado:**  

Após as análises individuais, forneça um ranking final das respostas, ordenando-as da melhor para a pior, no seguinte formato JSON:  

```json  
{{  
    "ranking": ["modelo_melhor", "modelo_segundo", "modelo_pior"]  
}}  

"""