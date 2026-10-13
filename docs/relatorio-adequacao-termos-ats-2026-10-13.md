# Adequação dos termos ATS nos cinco idiomas

Data: 13 de outubro de 2026.
Base: commit cc0cb6d, após a sincronização dos cinco idiomas.
O responsável autorizou aplicar a adequação dos termos nesta etapa.

## Resultado

Os cinco currículos usam nomes mais explícitos para atividades e ferramentas já confirmadas.
A redação preserva as variantes pt-BR, pt-PT, inglês, es-419 e es-ES.
Os títulos oficiais dos cursos permanecem no idioma original.

A adequação abrange introdução, metadados, competências e a descrição da gestão do SGCS.
Galeria e agradecimentos mantêm o conteúdo da versão sincronizada.
As 15 páginas foram incluídas na verificação de navegação e apresentação.

O [registro de alterações](referencias/ats/adequacao-terminologia-2026-10-13.json) contém textos anteriores, textos novos, contextos e justificativas.
Ele também registra identificadores das fontes e hashes das entradas e dos cinco currículos.
As 107 entradas são operações de revisão, com repetições entre idiomas.
Elas não representam uma quantidade de competências.

## Critérios e fontes

A revisão priorizou correspondências já examinadas semanticamente, definições oficiais e declarações do responsável.
Os nomes foram adaptados à gramática local.
Uma adaptação editorial não foi apresentada como sinônimo confirmado por um fornecedor.

| Conceito | pt-BR | pt-PT | Inglês | Espanhol |
| --- | --- | --- | --- | --- |
| Ativos | Gestão de ativos de TI | Gestão de ativos de TI | IT asset management | Gestión de activos de TI |
| Atendimento | Resolução de incidentes e escalonamento de chamados | Resolução de incidentes e escalonamento de pedidos de assistência | Incident resolution and ticket escalation | Resolución de incidentes y escalamiento de tickets, es-419. Escalado de tickets, es-ES |
| Hardware | Manutenção de hardware de computadores e periféricos | Manutenção de hardware de computadores e periféricos | Computer hardware and peripheral maintenance | Mantenimiento de hardware de computadoras y periféricos, es-419. Ordenadores, es-ES |
| Documentação | Documentação técnica e manuais de usuário | Documentação técnica e manuais de utilizador | Technical and user documentation | Documentación técnica y manuales de usuario |
| Colaboração | Ferramentas colaborativas online | Ferramentas colaborativas online | Online collaborative tools | Herramientas colaborativas en línea |
| Liderança no SGCS | Liderança de equipe | Liderança de equipa | Team leadership | Liderazgo de equipo |

A ESCO liga rótulos portugueses, ingleses e espanhóis pela mesma URI.
Isso permite examinar o conceito antes de escolher a expressão regional.
A classificação distingue conhecimento de habilidade e apresenta definições e nomes alternativos.
Consulte a [descrição oficial da ESCO](https://esco.ec.europa.eu/en/classification/skills).

O recorte Sólides sustenta referências específicas a suporte N1/N2 e manutenção de impressoras.
Os IDs 2064833 e 1890998 permanecem no [arquivo das vagas públicas](referencias/ats/solides/registros-publicos.json).
Os requisitos dessas vagas não foram convertidos em competências pessoais.

O dicionário O*NET fornece nomes como Microsoft Excel, Microsoft Office, LibreOffice e Microsoft Teams.
As [declarações do responsável](fontes/competencias-declaradas.json) sustentam o uso dos produtos acrescentados.
A [referência ocupacional de suporte](https://www.onetonline.org/link/summary/15-1232.00) foi consultada como contexto.
Ela não substitui a evidência pessoal nem atribui todas as atividades da ocupação ao responsável.

## Aplicações e restrições

- Excel e Office passam a usar os nomes Microsoft Excel e Microsoft Office.
- LibreOffice e Office 365 aparecem com base nas declarações. Office 365 preserva a indicação de uso online.
- Canva, GitHub, Google Drive, Microsoft Teams, OneDrive e Trello aparecem no contexto de colaboração da equipe.
- A descrição restringe acessos, permissões, sincronização, versões e cópias de segurança ao ambiente da equipe.
- A manutenção de impressoras e os procedimentos operacionais padrão aparecem como atividades específicas do suporte.
- Inteligência artificial recebe o nome completo. IA, aprendizado de máquina, JavaScript e Python preservam o contexto de fundamentos.
- Fluxo de caixa e gestão financeira indicam formação complementar. Melhoria de processos indica formação introdutória.
- Liderança de equipe permanece no SGCS acadêmico, com MVP em desenvolvimento.
- A identificação de requisitos em espanhol permanece atribuída à equipe.
- Modelação de processos e prototipagem corrigem a redação pt-PT.

Gestão de projetos, modelagem de dados e trabalho em equipe já tinham nomes adequados.
Esses conceitos foram preservados nas respectivas variantes.
Não houve substituição geral de termos técnicos específicos por categorias mais amplas.

Não foram acrescentados PMO, FP&A, pandas, Java, administração corporativa em nuvem ou gestão completa de incidentes.
GitHub Actions e GitHub Pages continuam ligados à publicação descrita no projeto.
Fusão de fibra óptica mantém a condição de aprendiz.
Trabalho em altura mantém a experiência orientada.
A formação superior permanece em andamento.
Os dados e as qualificações brasileiras permanecem preservados.

## Verificação

A inspeção estrutural examinou 16 páginas HTML, incluindo a escolha de idioma.
Ela confirmou caminhos relativos, âncoras, lang e hreflang, sem scripts ou eventos JavaScript.
As duas cópias de cursos preservam os 17 títulos, instituições, datas e cargas horárias de cada currículo.
O conteúdo factual dos empregos foi comparado com a versão anterior e permanece igual.

Os cinco CSS permanecem iguais à versão anterior e entre si.
SHA-256: b0baa10b43187f8a376f350f8e28b8a96f18273fb6a21ad667cfb8acb2a6cff7.
O [resultado estrutural](estrutura-adequacao-ats-2026-10-13.json) registra essas verificações.
Também foram conferidos 141 links locais na documentação atualizada, sem destinos ausentes.
Os clones completos continuam excluídos, conforme git check-ignore.

O Nu HTML Checker 26.10.12 foi executado localmente nos cinco currículos.
Ele não encontrou erros e apresentou 110 avisos sobre role=list em listas nativas.
Esse atributo foi preservado conforme a decisão de compatibilidade documentada.
O [resultado HTML](validacao-html-adequacao-ats-2026-10-13.json) preserva as mensagens do validador.

O Chromium 151.0.7922.34 examinou as 15 páginas com JavaScript desativado.
Os testes abrangeram larguras de 320 e 1280 pixels, texto a 200%, espaçamento ampliado e temas claro e escuro.
Não houve transbordamento horizontal nem falhas de carregamento nos cenários examinados.
O link de salto e o controle de cursos funcionaram por teclado, com foco visível nos cinco currículos.
O [registro do navegador](verificacao-adequacao-ats-2026-10-13.json) preserva os resultados.

A impressão foi examinada com o controle de cursos fechado e aberto.
Em ambos os estados, somente a cópia de impressão apresentou os 17 títulos.
Cada PDF de inspeção contém os 17 cursos uma única vez.
O ensaio A4, com margens de 12 mm, produziu nove páginas por idioma.
O [registro de impressão](impressao-adequacao-ats-2026-10-13.json) preserva as contagens.

As imagens em [evidencias-adequacao-ats-2026-10-13/](evidencias-adequacao-ats-2026-10-13/) registram a apresentação examinada.
Foram inspecionadas as competências dos cinco idiomas, amostras estreitas e as folhas de contato da impressão.
Os PDFs de inspeção e os scripts temporários foram removidos após a revisão.
git diff --check não encontrou problemas.

## Limites

As fontes não demonstram um cadastro universal de palavras-chave usado por todos os ATS.
Os cadastros e as classificações fornecem referências de nomenclatura.
Os guias editoriais complementares não foram usados para ampliar as competências.

Nenhum currículo foi enviado a um serviço externo de avaliação.
Nenhum parser ATS ou processo real de seleção foi testado.
A revisão não promete pontuação, aprovação ou aumento de convites para entrevistas.
As verificações automáticas não demonstram conformidade integral com WCAG ou STE.
O ensaio utilizou um navegador. Não abrange todos os motores, leitores de tela ou impressoras.
A ampliação de texto foi testada. O zoom nativo da interface do navegador não foi automatizado.
A paginação pode variar conforme o navegador, as fontes, o papel e as margens escolhidas.

O [relatório de análise anterior](referencias/ats/analise-palavras-chave-2026-10-13.md) permanece como registro da versão examinada.
Seus CSVs e hashes não foram atualizados para representar o texto novo.
O registro de adequação documenta a passagem entre as duas versões.
