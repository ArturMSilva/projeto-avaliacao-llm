from llms.groqcloud_qwen_client import get_qwen_response
from llms.groqcloud_llama_client import get_llama_response
from llms.google_gemini_client import get_gemini_response
from comparador.analise_respostas import comparar_respostas, processar_avaliacao


def exibir_menu():
    print("\n=== MENU ===")
    print("1. Fazer uma pergunta")
    print("2. Sair")
    return input("Escolha uma opção: ")


def main():
    while True:
        escolha = exibir_menu()
        if escolha == "1":
            mensagem = input("\nDigite sua pergunta para os modelos Qwen, Llama e Gemini: ")
            
            print("\nObtendo resposta do Qwen...")
            resposta_qwen = get_qwen_response(mensagem)
            print(resposta_qwen)
            
            print("\nObtendo resposta do Llama...")
            resposta_llama = get_llama_response(mensagem)
            print(resposta_llama)
            
            print("\nObtendo resposta do Gemini...")
            resposta_gemini = get_gemini_response(mensagem)
            print(resposta_gemini)
            
            respostas = {
                "qwen": resposta_qwen,
                "llama": resposta_llama,
                "gemini": resposta_gemini
            }
            
            print("\nIniciando processo de comparação das respostas...")
            rankings_parciais = {}
            ranking_final = comparar_respostas(respostas, rankings_parciais)
            
            if isinstance(ranking_final, dict) and "ranking_final" in ranking_final:
                print("\nRanking Final Consolidado:")
                for posicao, modelo in enumerate(ranking_final["ranking_final"], start=1):
                    print(f"{posicao}º lugar: {modelo.capitalize()}")
                
                detalhes = input("\nDeseja exibir os detalhes da avaliação? (s/n): ").strip().lower()
                if detalhes == "s":
                    for modelo_avaliador in ["qwen", "llama", "gemini"]:
                        print(f"\nDetalhes da avaliação feita por {modelo_avaliador.capitalize()}:")
                        ranking, analise_textual = processar_avaliacao(modelo_avaliador, respostas)
                        if analise_textual:
                            print(analise_textual)
                        else:
                            print("Nenhum detalhe disponível.")
            else:
                print(f"Erro ao consolidar o ranking final: {ranking_final.get('error', 'Erro desconhecido.')}")
        
        elif escolha == "2":
            print("\nSaindo do programa. Até mais!")
            break
        
        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()