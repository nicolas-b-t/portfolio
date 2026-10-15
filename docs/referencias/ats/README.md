# ATS: instruções para preparar e conferir currículos

Revisão: 15 de outubro de 2026.
ATS identifica sistemas de acompanhamento de candidaturas. O parser é o componente que extrai e organiza os dados do currículo.
Extrair texto, identificar campos, comparar requisitos e selecionar candidatos são etapas diferentes.

## Escolher o arquivo

1. Confira os formatos e limites informados pelo portal da vaga.
2. Prefira a versão de uma coluna quando não houver outra exigência.
3. Use a versão com coluna lateral quando a apresentação visual for adequada ao destinatário.
4. Envie um PDF com texto selecionável ou o DOCX solicitado pelo portal.
5. Preserve nome e contatos no corpo principal do documento.

A documentação da Greenhouse identifica tabelas, colunas, cabeçalhos, rodapés, caixas de texto e documentos em imagem como possíveis causas de extração incompleta.
Ela também informa um limite de 2,5 MB para seu parser. Esse limite pertence à Greenhouse, não a todos os ATS.
Os PDFs V3 usam texto selecionável e têm menos de 250 KB cada.

Fonte: [Greenhouse — Unsuccessful resume parse](https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse), consultada em 15 de outubro de 2026.

## Escrever o conteúdo

1. Apresente títulos de seção claros e uma sequência consistente.
2. Preserve cargos, empresas, instituições e datas verdadeiros.
3. Relacione competências a atividades ou projetos concretos.
4. Use termos da vaga somente quando correspondam à experiência declarada.
5. Identifique formação em andamento e conteúdos previstos da graduação.
6. Preserve níveis como aprendiz, N1 e N1/N2.
7. Diferencie sua contribuição do trabalho da equipe.

Não transforme nomes de catálogos, requisitos de vagas ou coincidências de palavras em qualificações pessoais.
Um catálogo como ESCO descreve conceitos. Ele não é uma lista universal de palavras que garantem aprovação.

## Conferir antes do envio

1. Abra o DOCX e o PDF finais.
2. Confira a ordem de leitura e a paginação.
3. Copie o texto do PDF para um editor simples.
4. Confira nome, contatos, empresas, cargos, datas e formação.
5. Confira nomes oficiais dos cursos, instituições, datas e cargas horárias.
6. Verifique se os 17 cursos aparecem uma única vez na versão geral.
7. Revise os campos preenchidos automaticamente pelo portal.
8. Corrija os campos que o portal interpretar incorretamente.

Para extrair texto localmente, use `pdftotext -layout curriculo.pdf curriculo.txt` quando a ferramenta estiver disponível.
Esse procedimento confere leitura. Ele não reproduz a classificação ou a decisão de um ATS proprietário.
Para uma versão direcionada, a seleção de cursos e experiências pode diferir do currículo geral.

## Limites dos ensaios do projeto

Os ensaios de 13 e 14 de outubro executaram rotinas públicas sobre entradas textuais derivadas do HTML.
Houve recuperação parcial de campos e falsos positivos. O resultado variou conforme parser, idioma, entrada e versão.
O cvats recuperou experiências e graduação em um ensaio dedicado ao bloco estruturado.
Esse ensaio não executou sua leitura de PDF nem a aplicação completa.

As rotinas consultadas foram [Resume-parser](https://github.com/Sihamkassim/Resume-parser), [resume-parser](https://github.com/Praveenkanna16/resume-parser) e [cvats-app](https://github.com/rntxbr/cvats-app).
Os commits, as entradas, as saídas e as licenças estão preservados no arquivo histórico local e no histórico Git anterior à reorganização.
O commit de referência para recuperar a documentação anterior é `56f6430f296f24048fed4327ab68b9708ffb928d`.

Os 312 fragmentos conferidos em cada V3 demonstram preservação do conteúdo entre DOCX e PDF.
Eles não demonstram leitura por Gupy, Sólides, Greenhouse ou outro serviço proprietário.
Não foi realizado novo teste de candidatura, pontuação ou seleção nesta reorganização.

As instruções e os aliases do bloco oculto do site não controlam as regras de um parser determinístico.
As traduções das listas de tags não declaram fluência nos respectivos idiomas.

Para organização e seleção do conteúdo, consulte as [diretrizes Europass](../europass/README.md).
