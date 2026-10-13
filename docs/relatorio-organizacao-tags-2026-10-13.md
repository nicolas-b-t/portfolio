# Organização das tags nos cinco idiomas

Data: 13 de outubro de 2026.
Base: commit 87f445f, após a adequação dos termos ATS.
O responsável autorizou consolidar conceitos, separar tecnologias e remover descritores e repetições.

## Resultado

Cada tag apresenta uma tecnologia, competência ou qualificação.
Nomes oficiais e identificadores permanecem como unidades.
As três categorias principais foram preservadas nos cinco currículos.

As ferramentas de colaboração foram integradas em gestão e produtividade.
Microsoft Office, LibreOffice, Git, GitHub, GitHub Actions, GitHub Pages, HTML e CSS aparecem em tags separadas.
ERP, PDV, NF-e e NFC-e também foram separados.
O apoio Help Desk foi acrescentado com o nível N1, conforme a experiência já descrita.

Os descritores das tags ficaram restritos a suporte técnico, fusão de fibra e inglês.
Foram retirados uso online, formação complementar, formação introdutória, fundamentos e nativo.
Os títulos e os dados dos cursos continuam a indicar o contexto da formação.
A experiência orientada de trabalho em altura foi transferida para a descrição profissional.

Condução foi dividida em carros, motos e CNH AB.
Uma frase explica que a CNH AB é uma habilitação brasileira.
As traduções não converteram essa qualificação em categorias estrangeiras.
Ferramentas de campo substitui a enumeração de ferramentas.
Organização de materiais substitui preparação de materiais e a tag genérica organização.

O [registro da organização](referencias/ats/organizacao-tags-2026-10-13.json) contém decisões, justificativas, hashes e contagens por idioma.
Os nomes foram adaptados a pt-BR, pt-PT, inglês, es-419 e es-ES.

## Consolidações e limites

| Tag consolidada | Conteúdo abrangido | Evidência ou limite preservado |
| --- | --- | --- |
| Gestão financeira | Fluxo de caixa e capitalização | Cursos e respectivos títulos oficiais |
| Inteligência artificial | Ética em IA e aprendizado de máquina | Formação em fundamentos. Desenvolvimento com agentes permanece no projeto pessoal |
| Cabeamento | SC/APC e RJ45 | Conectores citados na experiência |
| Configuração de redes | ONU, ONT e roteadores | Instalação e configurações descritas na RealFort |
| Testes de fibra óptica | OTDR, power meter e VFL | A experiência mantém apoio ao diagnóstico por OTDR |
| Redes sem fio | Rádio, Wi-Fi e mesh | Tecnologias citadas na experiência. PoE permanece separado |
| Documentação técnica | Manuais de usuário e POPs | Autoria e documentos descritos no suporte hospitalar |
| Manutenção de hardware | Computadores, periféricos e impressoras | Equipamentos e atividades descritos na experiência |
| Ferramentas de campo | Ferramentas elétricas, pneumáticas e clivador | Nenhuma qualificação técnica nova |
| Organização de materiais | Preparação e organização dos materiais | Não equivale à gestão completa de logística |
| Comunicação | Comunicação e orientação de usuários | Orientação descrita na experiência profissional |
| Adaptabilidade | Aprendizado e adaptação | Mantém o alcance da competência social anterior |

As consolidações usam atividades já declaradas.
Elas não demonstram equivalência lexical reconhecida por todo ATS.
Os detalhes profissionais continuam nas descrições, quando necessários para compreender a atividade.
O registro anterior preserva os termos específicos retirados das tags.

## Separações e repetições

Planejamento e indicadores foram separados.
Resolução de incidentes e escalonamento de chamados foram separados.
Comunicação e negociação foram separados no contexto da formação.
Redes e sistemas operacionais também foram separados.
Prototipação e MVP foram separados no SGCS.
Entrevistas e questionários passaram a ocupar tags distintas.

Cada rótulo aparece uma única vez na seção principal de competências.
GitHub deixou de aparecer simultaneamente nas listas de colaboração e web dessa seção.
As tags do portfólio que repetiam tecnologias já descritas no texto foram retiradas.
Gestão de projetos e Trello deixaram de repetir a descrição e o título da gestão do SGCS.

Quatro rótulos reaparecem em contextos distintos.
Documentação técnica permanece nas competências e na participação pessoal no Optigrow.
Essa ocorrência preserva a distinção entre o trabalho do responsável e o desenvolvimento realizado por Rodrigo.
Comunicação, gestão financeira e trabalho em equipe permanecem também no contexto da formação em andamento.
Essas ocorrências não foram tratadas como duplicações acidentais.

## Espaço ocupado

As listas passaram de 106 para 105 tags por currículo.
As contagens incluem tecnologias, competências, qualificação e repetições em contextos distintos.
Elas não representam uma quantidade de competências pessoais.
A separação de tecnologias compensa parte das consolidações na contagem.

| Idioma | Caracteres nas tags, antes | Caracteres nas tags, depois | Altura das competências, 1280 px, antes/depois | Altura das competências, 320 px, antes/depois |
| --- | ---: | ---: | ---: | ---: |
| pt-BR | 2.433 | 1.758 | 1.572 / 1.316 px | 3.498 / 2.800 px |
| pt-PT | 2.492 | 1.781 | 1.547 / 1.385 px | 3.524 / 2.851 px |
| en | 2.290 | 1.611 | 1.529 / 1.316 px | 3.346 / 2.580 px |
| es-419 | 2.547 | 1.860 | 1.590 / 1.385 px | 3.593 / 2.982 px |
| es-ES | 2.540 | 1.854 | 1.590 / 1.385 px | 3.593 / 2.982 px |

O texto das tags diminuiu cerca de 27% a 30%, conforme o idioma.
A altura da seção diminuiu cerca de 10% a 16% em 1280 pixels.
Em 320 pixels, a redução foi de aproximadamente 17% a 23%.
As medições incluem os títulos e os textos explicativos da seção.
Os resultados dependem da largura, das fontes e do navegador.

## Verificação

A inspeção estrutural examinou as 16 páginas HTML e 62 caminhos de recursos locais.
Ela confirmou âncoras, lang, hreflang e ausência de scripts, eventos e URLs JavaScript.
Os cinco CSS permanecem iguais.
Uma regra de impressão mantém o contato no mesmo bloco.
As duas cópias de cursos mantêm os 17 títulos, instituições, datas e cargas horárias.
A contribuição pessoal no Optigrow permanece igual.
O [registro estrutural](estrutura-organizacao-tags-2026-10-13.json) preserva os resultados.
Também foram conferidos 147 links locais na documentação atualizada, sem destinos ausentes.

O Nu HTML Checker 26.10.12 não encontrou erros nos cinco currículos.
Foram mantidos 105 avisos sobre role=list, conforme a decisão anterior de compatibilidade.
O [resultado HTML](validacao-html-organizacao-tags-2026-10-13.json) preserva as mensagens.

O Chromium 151.0.7922.34 examinou os cinco currículos com JavaScript desativado.
Foram testadas larguras de 320 e 1280 pixels, texto a 200%, espaçamento ampliado e temas claro e escuro.
Não houve transbordamento horizontal nos cenários examinados.
O link de salto, o controle de cursos e a troca de idioma funcionaram por teclado.
O [registro do navegador](verificacao-organizacao-tags-2026-10-13.json) inclui as comparações de altura.

A impressão mostrou os 17 cursos uma única vez, com o controle fechado e aberto.
Cada PDF de inspeção contém os 17 títulos uma única vez.
O ensaio A4, com margens de 12 mm, manteve nove páginas antes e depois em cada idioma.
O [registro de impressão](impressao-organizacao-tags-2026-10-13.json) contém as contagens.
O título e os três links de contato ficaram juntos na mesma página em cada idioma.

As imagens em [evidencias-organizacao-tags-2026-10-13/](evidencias-organizacao-tags-2026-10-13/) registram a apresentação examinada.
Foram inspecionadas as competências nos cinco idiomas e as folhas de contato da impressão.
Os scripts, as cópias de comparação e os PDFs temporários foram removidos após a revisão.
git diff --check não encontrou problemas.

## Limites

A revisão não ampliou a experiência profissional ou os níveis de suporte.
A fusão mantém a condição de aprendiz.
O inglês mantém o nome e a pontuação do TOEIC.
A formação superior e o MVP continuam em andamento.
As atividades da equipe permanecem distintas das atividades pessoais.

Nenhum parser ATS foi executado.
A organização das tags não representa uma pontuação de seleção.
O teste utilizou um navegador e não demonstra conformidade integral com WCAG ou STE.
A ampliação de texto foi examinada. O zoom nativo do navegador não foi automatizado.
A impressão pode variar conforme o motor, as fontes, o papel e as margens.
