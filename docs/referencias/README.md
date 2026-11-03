# Referências para manutenção

Fontes úteis ao currículo, à leitura por ATS e à publicação.
Cópias integrais de normas não acompanham o repositório.

## Europass

Consulta e cópias: 15/10/2026.
Fonte: União Europeia / Comissão Europeia / Europass.

O perfil Europass reúne experiências, formação e competências para produzir currículos selecionados conforme a candidatura.
As orientações oficiais recomendam destacar experiências relevantes, usar linguagem clara, revisar o texto e apresentar a experiência em ordem cronológica inversa.
Mantenha os currículos gerais V3 como acervo completo e prepare versões direcionadas quando a oportunidade exigir outro foco.

Os PDFs V3 são documentos próprios, não exportações do editor Europass.
O uso do Europass não comprova reconhecimento de diploma, equivalência profissional ou compatibilidade universal com ATS.
A página de criação de CV sugere fotografia; as condições da vaga e do destino orientam essa decisão.

### Cópias oficiais

As páginas HTML preservam as respostas recebidas dos sites oficiais.
Os recursos externos, como imagens e folhas de estilo, não foram espelhados.
O [manifesto](europass/manifesto.json) registra URLs, títulos, datas, tamanhos e hashes SHA-256.

| Documento | Cópia local | Fonte oficial |
| --- | --- | --- |
| Criar o CV, português | [HTML](europass-fontes/criar-cv-pt.html) | [Europass](https://europass.europa.eu/pt/create-europass-cv) |
| Criar o CV, inglês | [HTML](europass-fontes/criar-cv-en.html) | [Europass](https://europass.europa.eu/en/create-europass-cv) |
| Perfil, português | [HTML](europass-fontes/perfil-pt.html) | [Europass](https://europass.europa.eu/pt/ferramentas-europass/o-perfil-europass) |
| Perfil, inglês | [HTML](europass-fontes/perfil-en.html) | [Europass](https://europass.europa.eu/en/europass-tools/europass-profile) |
| Perguntas frequentes | [HTML](europass-fontes/perguntas-frequentes-en.html) | [Europass](https://europass.europa.eu/en/faq) |
| Preencher o perfil | [HTML](europass-fontes/preencher-perfil-en.html) | [Europass](https://europass.europa.eu/en/how-complete-my-europass-profile) |
| Aviso legal da Comissão | [HTML](europass-fontes/aviso-legal-comissao-europeia.html) | [Comissão Europeia](https://commission.europa.eu/legal-notice_en) |
| Aviso legal ligado pelo Europass | [HTML](europass-fontes/aviso-legal-uniao-europeia.html) | [União Europeia](https://european-union.europa.eu/legal-notice_en) |

© União Europeia, 1995–2026. Os avisos legais identificam a licença CC BY 4.0, salvo exceções e direitos de terceiros.
As cópias HTML não foram editadas.
Preserve a atribuição e os avisos recebidos; não incorpore as cópias ao site publicado.

## ATS

Revisão: 15/10/2026.
ATS identifica sistemas de acompanhamento de candidaturas; o parser extrai e organiza os dados do currículo.
Extrair texto, identificar campos, comparar requisitos e selecionar candidatos são etapas diferentes.

### Escolher o arquivo

1. Confira formatos e limites do portal da vaga.
2. Prefira a versão de uma coluna quando não houver outra exigência.
3. Use a versão com coluna lateral quando a apresentação visual for adequada.
4. Envie PDF com texto selecionável ou o DOCX solicitado.
5. Preserve nome e contatos no corpo principal.

A documentação da Greenhouse identifica tabelas, colunas, cabeçalhos, rodapés, caixas de texto e documentos em imagem como causas de extração incompleta.
O limite de 2,5 MB pertence à Greenhouse, não a todos os ATS.
Os PDFs V3 usam texto selecionável e têm menos de 250 KB cada.
Fonte: [Greenhouse — Unsuccessful resume parse](https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse).

### Escrever e conferir

1. Use títulos claros e sequência consistente.
2. Preserve cargos, empresas, instituições e datas verdadeiros.
3. Relacione competências a atividades ou projetos concretos.
4. Use termos da vaga apenas quando correspondam à experiência declarada.
5. Identifique formação em andamento e conteúdos previstos.
6. Preserve níveis como aprendiz, N1 e N1/N2.
7. Diferencie sua contribuição do trabalho da equipe.
8. Confira o DOCX e o PDF finais, a ordem de leitura e a paginação.
9. Copie o texto do PDF para um editor simples e confira nome, contatos, empresas, cargos, datas e formação.
10. Verifique se todos os cursos aparecem uma única vez na versão geral.

Para extrair texto localmente, use `pdftotext -layout curriculo.pdf curriculo.txt` quando disponível.
Esse procedimento confere leitura; não reproduz a classificação de um ATS proprietário.
Uma versão direcionada pode selecionar cursos e experiências diferentes do currículo geral.

### Limites dos ensaios

Os ensaios de 13 e 14/10/2026 executaram rotinas públicas sobre entradas textuais derivadas do HTML.
Houve recuperação parcial de campos e falsos positivos; o resultado variou conforme parser, idioma, entrada e versão.
O cvats recuperou experiências e graduação no ensaio dedicado ao bloco estruturado, mas não executou a leitura de PDF nem a aplicação completa.

As rotinas consultadas foram [Resume-parser](https://github.com/Sihamkassim/Resume-parser), [resume-parser](https://github.com/Praveenkanna16/resume-parser) e [cvats-app](https://github.com/rntxbr/cvats-app).
Os commits, entradas, saídas e licenças estão preservados no arquivo histórico local e no histórico Git anterior à reorganização.
O commit de referência é `56f6430f296f24048fed4327ab68b9708ffb928d`.

Os 312 fragmentos conferidos em cada V3 demonstram preservação do conteúdo entre DOCX e PDF.
Eles não demonstram leitura por Gupy, Sólides, Greenhouse ou outro serviço proprietário.
As instruções e aliases do bloco oculto não controlam as regras de um parser determinístico.

As capturas de ATS usadas na análise foram arquivadas em `_arquivo/site-curriculo-portfolio/2026-11-03/referencias-ats-local/`.

## ASD-STE100

O PDF da ASD-STE100 não acompanha clones do Git.
Consulte a origem no [manifesto](asd-ste100/manifesto.json) antes de citar uma edição.
O [guia de redação](../guia-de-redacao.md) adapta princípios de clareza; não é tradução oficial nem certificação STE.

## Repertório técnico local

A base técnica foi arquivada em 03/11/2026 em `_arquivo/site-curriculo-portfolio/2026-11-03/repertorio-tecnico-site/` (67 MB).
O catálogo e o índice permanecem em `repertorio-tecnico-site/` como registro.
As citações históricas em [Padrões técnicos](../historico/padroes-tecnicos.md) usam o caminho antigo.

## Fontes externas

| Assunto | Referência |
| --- | --- |
| HTML | [WHATWG HTML Living Standard](https://html.spec.whatwg.org/) |
| Acessibilidade | [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) |
| Compatibilidade CSS | [Baseline](https://web.dev/baseline) |
| Etiquetas de idioma | [RFC 5646](https://www.rfc-editor.org/rfc/rfc5646.html) |
| GitHub Pages | [Documentação oficial](https://docs.github.com/en/pages) |
| Competências | [SFIA e NICE](../competencias.md) |
| Currículos atuais | [PDFs V3](../curriculos/v3/README.md) |

As cópias integrais anteriores de normas, bases de competências, código de terceiros e relatórios estão no arquivo local descrito em [Histórico](../historico/historico.md).
Consulte a fonte oficial antes de aplicar uma edição mais recente.
O SFIA é consultado na biblioteca principal; não há cópia local versionada.
