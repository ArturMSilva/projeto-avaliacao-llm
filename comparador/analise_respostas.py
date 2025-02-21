import json

from comparador.criterios import PROMPT_AVALIACAO
from llms.groqcloud_qwen_client import get_qwen_response
from llms.groqcloud_llama_client import get_llama_response
from llms.google_gemini_client import get_gemini_response


def processar_avaliacao(modelo_avaliador, respostas):
    prompt = PROMPT_AVALIACAO.format(
        resposta_qwen=respostas["qwen"],
        resposta_llama=respostas["llama"],
        resposta_gemini=respostas["gemini"]
    )
    
    if modelo_avaliador == "qwen":
        resposta_avaliacao = get_qwen_response(prompt)
    elif modelo_avaliador == "llama":
        resposta_avaliacao = get_llama_response(prompt)
    elif modelo_avaliador == "gemini":
        resposta_avaliacao = get_gemini_response(prompt)
    else:
        raise ValueError("Modelo avaliador inválido.")
    
    if not resposta_avaliacao or not isinstance(resposta_avaliacao, str):
        print(f"Resposta inválida do modelo {modelo_avaliador}.")
        return None, None
    
    try:
        ranking = extrair_ranking(resposta_avaliacao)
        analise_textual = resposta_avaliacao
        return ranking, analise_textual
    except Exception as e:
        print(f"Erro ao processar a resposta do modelo avaliador {modelo_avaliador}: {e}")
        return None, None


def extrair_ranking(resposta_bruta):
    try:
        data = json.loads(resposta_bruta)
        if "ranking" not in data:
            raise ValueError("Campo 'ranking' não encontrado no JSON.")
        return data["ranking"]
    except json.JSONDecodeError:
        inicio = resposta_bruta.find('{')
        fim = resposta_bruta.rfind('}') + 1
        if inicio == -1 or fim == -1:
            raise ValueError("Nenhuma estrutura JSON válida encontrada.")
        json_str = resposta_bruta[inicio:fim]
        try:
            data = json.loads(json_str)
            if "ranking" not in data:
                raise ValueError("Campo 'ranking' não encontrado no JSON.")
            return data["ranking"]
        except json.JSONDecodeError:
            raise ValueError("JSON encontrado, mas inválido ou sem o campo 'ranking'.")

def comparar_respostas(respostas, rankings_parciais):
    modelos = ["qwen", "llama", "gemini"]
    for modelo in modelos:
        print(f"\nObtendo avaliação do modelo {modelo.capitalize()}...")
        
        ranking_parcial, analise_textual = processar_avaliacao(modelo, respostas)
        if not ranking_parcial:
            print(f"Avaliação do modelo {modelo} falhou. Retornando erro.")
            return {"error": f"Avaliação do modelo {modelo} falhou."}
        
        rankings_parciais[modelo] = {
            "ranking_final": ranking_parcial,
            "analise_textual": analise_textual
        }
        print(f"Avaliação do modelo {modelo} concluída com sucesso.")
    
    pontuacao_total = {}
    for avaliador, ranking_info in rankings_parciais.items():
        ranking_final = ranking_info["ranking_final"]
        
        if not isinstance(ranking_final, list) or len(ranking_final) != 3:
            print(f"Ranking inválido do avaliador {avaliador}: {ranking_final}")
            return {"error": f"Erro ao processar ranking do avaliador {avaliador}."}
        
        for i, posicao in enumerate(ranking_final):
            if isinstance(posicao, str) and posicao.lower() in modelos:
                modelo_avaliado = posicao.lower()
            else:
                try:
                    modelo_avaliado = modelos[int(posicao) - 1]
                except (ValueError, IndexError):
                    print(f"Erro ao converter posição '{posicao}' para um modelo válido.")
                    return {"error": f"Erro ao processar ranking do avaliador {avaliador}."}
            
            if modelo_avaliado not in pontuacao_total:
                pontuacao_total[modelo_avaliado] = 0
            pontuacao_total[modelo_avaliado] += 10 - i  
    
    if not pontuacao_total:
        return {"error": "Nenhum modelo foi ranqueado corretamente."}
    
    ranking_final = sorted(pontuacao_total.keys(), key=lambda x: pontuacao_total[x], reverse=True)
    return {"ranking_final": ranking_final}