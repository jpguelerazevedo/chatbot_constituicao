from sentence_transformers import SentenceTransformer, util
from transformers import pipeline
import os
import re

# 🔹 Modelos: busca + QA
modelo_emb = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
modelo_qa = pipeline("question-answering", model="pierreguillou/bert-base-cased-squad-v1.1-portuguese")

# 🔹 Leitura da Constituição
def obter_constituicao_do_arquivo(arquivo_path):
    if not os.path.exists(arquivo_path):
        print("Arquivo não encontrado.")
        return ""
    with open(arquivo_path, "r", encoding="utf-8") as file:
        return file.read()

# 🔹 Divide em trechos (por artigos)
def dividir_texto_em_artigos(texto):
    artigos = re.split(r"(Art\. ?\d+[^\n]*)", texto)
    trechos = []
    for i in range(1, len(artigos), 2):
        titulo = artigos[i].strip()
        conteudo = artigos[i+1].strip() if i+1 < len(artigos) else ""
        trechos.append(f"{titulo}\n{conteudo}")
    return trechos

# 🔹 Busca os trechos mais parecidos com a pergunta
def buscar_trechos_semelhantes(pergunta, trechos, modelo_emb):
    emb_pergunta = modelo_emb.encode(pergunta, convert_to_tensor=True)
    emb_trechos = modelo_emb.encode(trechos, convert_to_tensor=True)
    similaridades = util.cos_sim(emb_pergunta, emb_trechos)[0]
    
    # Ordena todos os trechos por similaridade
    indices = similaridades.argsort(descending=True)
    return [(trechos[i], similaridades[i].item()) for i in indices]

# 🔹 Gera resposta para um trecho
def responder(pergunta, contexto, modelo_qa):
    resposta = modelo_qa(question=pergunta, context=contexto)
    return resposta['answer'], resposta['score']

# 🔹 Execução principal
def executar_pergunta(pergunta):
    texto = obter_constituicao_do_arquivo("constituicao.txt")
    if not texto:
        return

    trechos = dividir_texto_em_artigos(texto)
    
    # Busca os 3 trechos mais semelhantes
    similares = buscar_trechos_semelhantes(pergunta, trechos, modelo_emb)

    # Selecionando os 3 trechos mais relevantes
    print("\nTrechos mais relevantes encontrados:\n")
    for i, (trecho, sim) in enumerate(similares[:3], 1):  # Aqui estamos pegando os 3 primeiros
        print(f"{i}. Similaridade: {sim:.2f}")
        print(trecho[:500], "...\n")

    # Junta os 3 trechos mais relevantes para formar o contexto completo
    contexto_completo = "\n\n".join([trecho for trecho, _ in similares[:3]])
    resposta, score = responder(pergunta, contexto_completo, modelo_qa)

    print("Resposta:", resposta)
    print(f"Confiabilidade: {score:.2f}")

# 🔹 Faz a pergunta

while True:
    pergunta = input("Pergunte algo sobre a Constituição (ou digite 'sair' para encerrar):")
    if pergunta.lower() in ["sair", "exit", "quit", "Sair", "Exit", "Quit"]:
        print("Encerrando o programa.")
        break
    elif not pergunta.strip():
        print("Por favor, faça uma pergunta válida.")
        continue

    # Executa a pergunta
    executar_pergunta(pergunta)
