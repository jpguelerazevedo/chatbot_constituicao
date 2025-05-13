Perguntas e Respostas sobre a Constituição Brasileira
Este projeto utiliza modelos de linguagem e processamento de linguagem natural (NLP) para responder perguntas com base no texto da Constituição Federal do Brasil. 
A aplicação identifica os trechos mais relevantes relacionados à pergunta e gera uma resposta utilizando um modelo pré-treinado em português.

🚀 Tecnologias Utilizadas
Python
Transformers (Hugging Face)
Sentence-Transformers
PyTorch

📦 Instalação
1. Clone o repositório:
git clone https://github.com/seu-usuario/perguntas-constituicao.git
cd perguntas-constituicao

3. Instale as dependências:
pip install -r requirements.txt

📄 Pré-requisitos
Certifique-se de ter um arquivo chamado constituicao.txt na mesma pasta do script, contendo o texto da Constituição Federal em formato .txt, com os artigos numerados no padrão:

Art. 1º Esta Constituição estabelece...
Art. 2º São Poderes da União...
...

⚙️ Como funciona
Carregamento dos modelos:
paraphrase-multilingual-MiniLM-L12-v2 para busca semântica.
pierreguillou/bert-base-cased-squad-v1.1-portuguese para perguntas e respostas.

Extração de trechos:
O texto é dividido em trechos por artigos usando expressões regulares.

Busca semântica:
Os trechos mais similares à pergunta são selecionados com base em embeddings.

Geração da resposta:
A pergunta é respondida com base no contexto mais relevante.

▶️ Como usar
Execute o script:
python nome_do_arquivo.py

Digite uma pergunta quando solicitado.  Exemplo:
Pergunte algo sobre a Constituição (ou digite 'sair' para encerrar): Quem é igual perante a lei?

A aplicação irá:
Mostrar os trechos mais relevantes.
Gerar uma resposta com base neles.
Exibir o grau de confiabilidade da resposta.

❓ Exemplo de uso
Pergunte algo sobre a Constituição (ou digite 'sair' para encerrar): O que é cláusula pétrea?
1. Similaridade: 0.89
Art. 60...
...
Resposta: As cláusulas pétreas são disposições constitucionais que não podem ser abolidas por emenda.
Confiabilidade: 0.85

📌 Observações
O modelo pierreguillou/bert-base-cased-squad-v1.1-portuguese foi treinado especificamente para tarefas de QA em português.
O sistema pode ser adaptado para outros textos jurídicos ou documentos.

📜 Licença
Este projeto é open-source, licenciado sob a MIT License.
