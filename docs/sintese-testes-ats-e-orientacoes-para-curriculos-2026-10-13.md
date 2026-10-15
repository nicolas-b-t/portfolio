# Síntese dos testes ATS e orientações para currículos

Datas dos testes: 13 e 14 de outubro de 2026. Encerramento e consolidação: 14 de outubro de 2026.

Esta síntese reúne os testes e sua aplicação ao portfólio e a futuros currículos do responsável.
ATS identifica sistemas de acompanhamento de candidaturas.
O parser é o componente que extrai texto e organiza dados do currículo.

Os testes demonstraram leitura local do conteúdo e identificaram erros de interpretação.
Eles não demonstraram compatibilidade universal com sistemas proprietários, aprovação em vagas ou efeito sobre a seleção de candidatos.

## Estado no encerramento

A [verificação vigente](verificacao-lista-geral-tags-2026-10-14.json) descreve o HTML publicado no commit 74b186f.
As rotinas originais do cvats recuperaram as três experiências e a graduação na leitura dedicada do bloco oculto.

| Experiência | Período recuperado |
| --- | --- |
| RealFort Sistemas — Auxiliar de instalação de fibra óptica | Sem período declarado |
| Lukos Tecnologia — Técnico de suporte Help Desk | Setembro a dezembro de 2025 |
| Instituto Alpha de Saúde Integral — Técnico de suporte de TI | Abril de 2023 a junho de 2024 |

Os campos de cargo retornam aliases ingleses. Os títulos portugueses permanecem nas descrições recuperadas e no conteúdo principal.
A graduação recuperada é o Curso superior de tecnologia em Gestão da Tecnologia da Informação, na Fatec Franco da Rocha – Giuliano Cecchettini.
O registro preserva início em julho de 2024, conclusão prevista para julho de 2027 e formação em andamento.

Os dois parsers anteriores mantiveram o nome correto. O segundo recuperou as mesmas 11 tecnologias.
Eles continuam sem recuperar corretamente o conjunto de experiências e graduação.
Os testes anteriores do DOM completo e da entrada sem hidden apresentaram falhas.
O positivo não demonstra leitura de PDF, DOCX, ATS proprietário ou da aplicação completa do cvats.

O conteúdo principal contém 161 ocorrências de tags e 145 rótulos distintos.
O bloco oculto contém 170 ocorrências e 152 rótulos distintos, após acrescentar sete termos ingleses em nove ocorrências.
A [lista de consulta](../Lista_de_tags/README.md) preserva os dados públicos e as instruções de leitura.
Os 14 arquivos reservados para outros sistemas de escrita continuam vazios. A exportação curricular TXT foi preservada.

Sete registros anteriores foram reunidos no [histórico compactado](historico-ats/README.md), com conteúdo integral e hashes conferidos.
Esta síntese concentra as decisões e orientações vigentes. As seções seguintes preservam a cronologia e os limites dos ensaios.
Nenhum teste de tela ou teclado foi executado nesta interação.

## Evidências e escopo

A análise abrangeu o currículo pt-BR e sua exportação TXT.
As demais páginas e traduções permaneceram fora desta revisão de extração.
Não houve teste de apresentação, CSS, tela ou teclado.
Nenhum currículo foi enviado a um serviço externo.

| Registro | Conteúdo preservado |
| --- | --- |
| [Inventário e comparação](historico-ats/README.md#exportações-substituídas) | Todas as tags, contextos, correspondências e limites documentais |
| [Resultados da extração](historico-ats/README.md) | Saídas originais, testes de controle, casos negativos e simulação |
| [Currículo textual](historico-ats/README.md#exportações-substituídas) | Cópia UTF-8 derivada do conteúdo público, com 17 cursos únicos |
| [Manifesto dos parsers](referencias/ats/manifesto-parser-publico-2026-10-13.json) | Repositórios, commits, licenças, adaptações de carregamento e hashes |
| [Guia de uso das referências](referencias/guia-de-uso.md) | Origem dos acervos, condições de uso e recuperação das fontes |

Os resultados identificam a página pelo SHA-256 e registram o commit-base 6a96e0b.
A página recebeu alterações locais após esse commit.
Um resultado só descreve a versão, o arquivo de entrada e o parser registrados.

## Leitura, interpretação e seleção

| Etapa | O que verifica | Situação nesta análise |
| --- | --- | --- |
| Leitura | Bytes, acentos, texto, separação dos itens e ausência de perda | Conferida no HTML e no TXT |
| Identificação de campos | Nome, contatos, cargos, empresas, datas e formação | Resultados parciais nos parsers públicos |
| Normalização de termos | Nome encontrado, nome normalizado e identificador do catálogo | Comparação documental e taxonomia do segundo parser |
| Associação de contexto | Atividade pessoal, atividade da equipe, apoio e conteúdo curricular previsto | Conferida na simulação baseada no HTML |
| Correspondência com vaga | Requisitos, níveis, pesos e critérios da empresa | Não testada |
| Seleção de candidatos | Aprovação, classificação ou decisão de recrutamento | Não testada |

Preservar o texto é necessário para os campos seguintes, mas não comprova sua interpretação correta.
Um parser pode recuperar tecnologias e ainda perder cargos, instituições ou datas.
Uma instituição de curso complementar pode ser identificada sem que a graduação seja recuperada.

## Resultados consolidados

| Ensaio | Resultado observado | Limite da conclusão |
| --- | --- | --- |
| Dois leitores HTML independentes | HTMLParser e lxml extraíram as mesmas 161 tags, na mesma ordem | Leitura de HTML não representa interpretação por ATS proprietário |
| Inventário | 108 tags de habilidades, 21 conteúdos previstos da graduação e 32 tags de projetos | São 161 ocorrências e 145 rótulos distintos. A contagem não mede domínio |
| Comparação com o acervo | Seis nomes aplicados elevaram as igualdades textuais de 24 para 30 | As contagens não são taxas de compatibilidade ou aprovação |
| Primeiro parser público | Recuperou nome e e-mail após ajustar a ordem do TXT | Não reconheceu habilidades, experiências ou formação em português |
| Segundo parser público | Recuperou nome, e-mail, perfis pessoais e 11 tecnologias após refinar o TXT | Não recuperou as três experiências nem a graduação na Fatec |
| Cursos | O HTML contém duas cópias equivalentes de 17 cursos. O TXT contém uma cópia | Um leitor que ignora CSS pode recuperar 34 ocorrências do HTML |
| Simulação contextual | Preservou campos, períodos conhecidos, contextos, níveis e formação em andamento | Lê a estrutura do HTML. Não reproduz a interpretação de texto livre de um fornecedor |
| OpenCATS legado | A reprodução de cleanText perdeu caracteres não ASCII em UTF-8 | O serviço SOAP não foi chamado. O resultado se limita ao algoritmo local reproduzido |
| Código local do Odoo | Associa habilidades por skill_id | A inspeção não comprova associação automática de nomes extraídos ao cadastro |

O primeiro parser foi executado no commit 76f35bc5406276f5d7f1bfa0f8d60e2682d8df28.
O segundo foi executado no commit b35512d5fa5fc5dddd39aeaeff2df3dfa4da6746.
O manifesto registra os dois repositórios e as condições das cópias locais.

No segundo teste, dois imports de leitores PDF/DOCX foram omitidos na cópia de execução em memória.
O Node.js retirou os tipos TypeScript. As regras da rotina textual permaneceram iguais.
PDF, DOCX, servidor e frontend não foram executados.
O teste não representa a aplicação completa do fornecedor desse parser.

Os controles em inglês confirmaram que as rotinas executavam e recuperavam os exemplos esperados.
Esses controles não demonstram cobertura do português.
As falhas nos currículos pt-BR foram preservadas nos resultados.

## O que cada fonte permite concluir

| Fonte | Aplicação válida | Limite |
| --- | --- | --- |
| Odoo Recruitment 19.0 | Consultar nomes, IDs e regras do cadastro de habilidades | O acervo inclui registros iniciais e demonstrativos |
| ESCO v1.2.1 | Consultar conceitos, definições, rótulos e aliases ligados por URI | É uma classificação externa. Um conceito pode ser mais amplo que a atividade declarada |
| O*NET 31.0 | Consultar nomes de software e referências ocupacionais | Não é uma lista universal de termos aceitos por ATS |
| Sólides | Consultar nomes de hardSkills publicados em quatro vagas | Os nomes e níveis pertencem às vagas, não ao responsável |
| Nesta e ESCoE | Consultar vocabulário de pesquisa derivado de anúncios | Não constitui catálogo comercial de ATS |
| Exemplos RChilli, Textkernel e Lightcast | Examinar exemplos documentados e aliases publicados | São seis exemplos, sem consulta executada ao catálogo integral |
| Guias editoriais e AIResume Guru | Apoiar a redação e a pesquisa de nomenclaturas | Menções e termos relacionados não comprovam equivalência ou reconhecimento por um parser |
| Parsers públicos executados | Observar extração de campos nas versões e entradas registradas | Seus resultados não representam Gupy, Sólides ou outros sistemas proprietários |

Uma igualdade textual inclui apenas caixa e espaços normalizados nesta comparação.
Versões, acentos, fabricante, pontuação e palavras adicionais permanecem distintos.
Um alias só é documental quando a fonte o registra expressamente.
Uma relação editorial ou parcial conserva essa classificação.

O campo synonyms do dataset editorial inclui tecnologias relacionadas.
Ele não foi usado como conjunto automático de equivalências.
Níveis profissionais do dataset e requisitos das vagas não qualificam o responsável.

## Aplicabilidade ao portfólio

### Tecnologias e nomes

Os nomes específicos identificam produtos, equipamentos e atividades que uma categoria genérica pode omitir.
A revisão preservou tecnologias declaradas e recuperou equipamentos, conectores, ferramentas e atividades do histórico confirmado.
A ausência de um nome no acervo não demonstrou rejeição por ATS.

| Nome anterior | Nome aplicado | Evidência |
| --- | --- | --- |
| Windows | Microsoft Windows | O*NET |
| ChatGPT | OpenAI ChatGPT | O*NET |
| Apache | Apache HTTP Server | O*NET, no contexto de servidores web |
| Nginx | Nginx web server | Alias inglês ESCO de um conceito mais amplo de servidores proxy |
| Amazon Web Services (AWS) | Amazon Web Services AWS software | Rótulo da O*NET |
| Microsoft Azure | Microsoft Azure software | Rótulo da O*NET |

Os nomes anteriores e atuais produziram a mesma lista de tecnologias no segundo parser.
As seis alterações aumentaram a igualdade documental, sem ganho observado de recuperação nesse teste.
Esse resultado não sustenta acrescentar palavras a uma tag apenas para reproduzir um catálogo.
Uma mudança futura de nomenclatura deve preservar a identidade do produto e ter uma justificativa verificável.

Consultas SQL mantém o alcance da atividade declarada.
Metodologias ágeis e Scrum permanecem separados.
Windows 11 não foi convertido em Windows 11 Pro.
Nenhuma certificação Scrum Master ou competência em serviços específicos de nuvem foi inferida.

### Campos e atribuições

O currículo conserva três experiências, três projetos e a formação em andamento.
As datas da RealFort permanecem ausentes. A conclusão da graduação permanece prevista para julho de 2027.
As 21 tags acadêmicas identificam conteúdos previstos, sem comprovar aprovação individual ou prática profissional.

Fusão de fibra permanece no nível de aprendiz. A atuação com OTDR permanece de apoio ao diagnóstico.
A experiência em altura continua orientada.
N1 e N1/N2 permanecem associados aos contextos de suporte.

Rodrigo permanece identificado como principal responsável pelo desenvolvimento do Optigrow.
A aplicação e a pesquisa do SGCS permanecem atribuídas à equipe.
A gestão do projeto permanece atribuída ao responsável.
Recuperar uma tecnologia do texto não transfere uma atividade da equipe para uma pessoa.

### Exportação para leitura

O HTML permanece como fonte do currículo público.
O TXT é uma cópia derivada para conferência e uso em sistemas que aceitem esse formato.
Ele não substitui documentos oficiais ou arquivos restritos da cópia pessoal.

O TXT coloca o nome na primeira linha e os contatos pessoais antes dos links de projetos.
Essa ordem corrigiu a escolha do repositório do portfólio como perfil GitHub no segundo parser.
Sete rótulos de navegação foram retirados. As URLs pertinentes e o conteúdo profissional foram preservados.

O segundo parser interpretou C a partir da palavra Código.
O TXT refinado deixou de apresentar esse falso positivo no currículo testado.
Um teste negativo separado ainda reproduziu a falha de limite de palavra Unicode do parser.
A correção da exportação não corrigiu o algoritmo nem demonstrou ausência de todos os falsos positivos.

As duas cópias dos cursos continuam necessárias no HTML, conforme as regras do projeto.
A exportação reúne cada curso uma única vez, com título, instituição, datas, carga horária e qualificação preservados.
Tags repetidas em contextos profissionais, acadêmicos ou de projetos não foram removidas por repetição lexical.

## Procedimento para futuros currículos do responsável

As instruções seguintes derivam dos resultados locais e de verificações de integridade.
Elas não são requisitos universais dos sistemas proprietários.
O idioma e o formato aceitos devem ser confirmados para cada candidatura.

### Preparar os fatos

1. Registre as atividades realizadas e suas fontes.
2. Separe contribuições pessoais, contribuições da equipe e conteúdos acadêmicos previstos.
3. Identifique tecnologias, versões e equipamentos efetivamente usados.
4. Preserve apoio, aprendizagem, familiaridade e níveis declarados.
5. Distinga curso, certificado de participação e certificação profissional.
6. Mantenha datas desconhecidas como ausentes.
7. Identifique separadamente conclusão prevista e conclusão realizada.
8. Use os dados pessoais do próprio responsável, conforme a finalidade da candidatura.

Este projeto permanece pessoal.
As orientações metodológicas podem apoiar futuras versões, mas os dados pessoais não constituem um modelo para terceiros.

### Escolher os termos

1. Use uma tecnologia, competência ou qualificação por tag.
2. Prefira nomes específicos sustentados pela experiência ou declaração recebida.
3. Consulte a definição quando o rótulo da fonte admitir mais de um sentido.
4. Separe correspondência literal, alias documental, variante de nome e relação parcial.
5. Preserve conceitos diferentes em itens distintos.
6. Registre a fonte e a justificativa de cada mudança de nomenclatura.
7. Preserve tecnologias pertinentes sem correspondência no acervo.
8. Use termos da vaga somente quando os fatos sustentarem seu significado.

A quantidade de correspondências não é uma meta de competência ou aprovação.
Adicionar uma palavra-chave sem evidência pode alterar a interpretação do histórico.
O vocabulário da vaga serve para identificar conceitos pertinentes, sem ampliar a atuação comprovada.

### Preparar a entrada do parser

1. Confirme os formatos e idiomas aceitos pela plataforma.
2. Coloque o nome antes do resumo profissional.
3. Liste contatos pessoais antes dos links de projetos.
4. Separe o perfil pessoal dos repositórios e sites de projetos.
5. Retire comandos de navegação da cópia de candidatura.
6. Preserve acentos e identificadores técnicos em UTF-8, quando o formato admitir essa codificação.
7. Confira cada curso uma única vez na exportação.
8. Separe instituições de cursos complementares e instituições da graduação.
9. Preserve a indicação de formação em andamento.

Se a plataforma aceitar TXT, use uma exportação conferida.
Se exigir PDF ou DOCX, confira a extração do arquivo final nesse formato.
Os testes desta análise não comprovam a leitura desses formatos.
Não traduza todo o currículo apenas para satisfazer um parser limitado a cabeçalhos em inglês.

### Verificar os dados extraídos

1. Compare o nome, o e-mail e os perfis recuperados com os dados de origem.
2. Confira a associação entre cada cargo e sua empresa.
3. Confira os períodos de cada experiência.
4. Verifique a instituição e o estado da graduação.
5. Confira títulos, instituições, datas e cargas horárias dos cursos.
6. Verifique o contexto de cada tecnologia recuperada.
7. Confira se observações e limitações permaneceram associadas à atividade correta.
8. Registre omissões e dados atribuídos incorretamente.
9. Preserve as saídas antes e depois de corrigir a entrada.

Um campo ausente pode representar uma limitação do parser ou um dado não declarado.
Um campo recuperado também pode estar associado à pessoa, ao projeto ou à formação incorretos.
Nenhum desses casos deve ser convertido automaticamente em uma aprovação do teste.

### Usar controles e casos negativos

| Entrada de controle | Interpretação que deve ser rejeitada |
| --- | --- |
| JavaScript | Java, por coincidência parcial |
| PostgreSQL | SQL, apenas por conter as mesmas letras |
| GitHub | Git, apenas por coincidência parcial |
| Scrum | Scrum Master ou certificação profissional |
| Windows 11 | Edição Pro não declarada |
| Consultas SQL | SQL Server ou administração completa de bancos |
| Código, em uma frase comum | Competência na linguagem C |
| Instituição de curso complementar | Instituição da graduação |
| Conclusão prevista | Graduação concluída |
| Repositório de projeto | Perfil pessoal GitHub |
| Atividade da equipe | Atividade individual não declarada |

Os controles devem corresponder a dúvidas reais sobre a entrada ou o algoritmo.
O registro deve distinguir um erro observado de um risco ainda não testado.
Uma frase que cite uma tecnologia não demonstra automaticamente competência pessoal nessa tecnologia.

## Manutenção das evidências

1. Identifique o arquivo de entrada e seu SHA-256.
2. Registre repositório, commit, versão, licença e configuração do parser.
3. Descreva adaptações de carregamento e rotinas que não foram executadas.
4. Preserve as saídas originais, inclusive falhas e campos vazios.
5. Separe execução de parser, inspeção de código e simulação.
6. Atualize a exportação quando o currículo de origem mudar.
7. Atualize o índice e os registros afetados.
8. Mantenha fontes, licenças e manifestos nas condições já registradas.
9. Remova auxiliares de execução depois de preservar as evidências necessárias.

Os clones completos dos parsers permanecem em referencias/ats/repositorios-local/, fora do Git.
As licenças e o histórico recebidos permanecem com as fontes.
Scripts de manutenção e de fornecedores não integram static/.
Os documentos do projeto continuam sujeitos às [orientações gerais](../AGENTS.md).

## Limites para decisões futuras

Os testes locais não produziram um catálogo integral de ATS brasileiro nem executaram um parser proprietário.
Não foram obtidos resultados de candidatura, pontuação, classificação ou decisão de recrutamento.
A distribuição pública de avaliação do Affinda foi localizada, mas não executada por ausência de Docker neste ambiente.

As falhas dos dois parsers públicos não representam todos os sistemas que aceitam português.
A simulação contextual não comprova o funcionamento de modelos ou taxonomias fechados.
A igualdade documental não demonstra qualidade da identificação de cargos, datas ou formação.

Quando um sistema específico estiver disponível, confira a entrada e os campos devolvidos por esse sistema.
Enquanto essa evidência não existir, descreva os resultados como verificações locais de leitura e interpretação, com os limites registrados.

## Ensaio posterior de dados ocultos — 14 de outubro de 2026

O responsável autorizou um bloco hierárquico oculto no início da página pt-BR, sem alterar a exportação.
Os dois parsers continuaram sem recuperar experiências e graduação. O bloco melhorou nome e perfis somente quando incluído na entrada.
O resultado não atendeu à condição de commit e push. As alterações ficaram locais, aguardando decisão.
O [ensaio posterior](historico-ats/README.md) registra condições, duplicações e próximos passos.
As contagens e hashes dos testes de 13 de outubro descrevem a versão anterior a esse bloco.

Depois, o responsável solicitou testes até recuperar experiência e formação.
As rotinas originais do cvats recuperaram três experiências e a graduação após refinamentos no bloco oculto.
Os cargos originais permanecem nas atividades. Aliases ingleses ajudam a identificação dos cargos pelo parser.
A graduação preserva início, conclusão prevista e formação em andamento.
Quatro controles de remoção e troca de dados confirmaram recuperação a partir das entradas.

O positivo se limita à leitura dedicada do bloco, em linhas lógicas derivadas do HTML.
O DOM completo e a entrada que exclui hidden continuaram negativos.
Os campos de posições da API receberam valores sintéticos. Nenhum PDF ou navegador foi usado nesse ensaio.
O [ensaio consolidado](historico-ats/README.md) registra o plano, as alterações, o resultado e seus limites.

## Revisão adicional das tags — 14 de outubro de 2026

A página principal contém 161 ocorrências e 145 rótulos distintos. A cópia oculta preserva os mesmos itens, na mesma ordem.
A comparação confirmou as mesmas 30 igualdades documentais do registro anterior. A lista atual não produziu novas igualdades.
As contagens excluem a duplicação entre o bloco oculto e o conteúdo principal.

O acervo sustenta associações adicionais para aliases. Algumas relações são conceituais ou parciais. Elas não constituem equivalências literais entre competências.
Os nomes apresentados e os níveis declarados permanecem como base factual.

| Tag atual | Termo consultado | Fonte e limite |
| --- | --- | --- |
| Consultas SQL | SQL | ESCO. Relação entre atividade e linguagem. Não atribui administração de bancos |
| Aprendizado de máquina | machine learning | ESCO. Tradução conceitual. Preservar conhecimento introdutório |
| Suporte Help Desk, N1 | IT support | Odoo. Categoria mais ampla. Preservar Help Desk e N1 |
| Documentação técnica | technical documentation | Nesta e ESCoE. Taxonomia de pesquisa. Preservar autoria e contexto |
| Manuais de usuário | provide user documentation | ESCO. Relação entre documento e atividade. Não confirma todas as atividades de distribuição |
| Pensamento analítico | analytical thinking | Alias ESCO. Não atribui análise de dados ou ferramentas |
| Inteligência de negócios | business intelligence | ESCO. Conteúdo previsto da graduação. Não atribui experiência profissional ou Power BI |

Microsoft Office software também consta no O*NET. Essa variante poderia acrescentar uma igualdade nominal para Microsoft Office.
O teste não demonstrou ganho de extração. A análise recomenda preservar o nome apresentado.

O ensaio executou parseResumeText original do segundo parser público, com a entrada restrita às tags.
Os sete termos da tabela e Microsoft Office software foram acrescentados somente em memória.
O resultado permaneceu com 11 tecnologias: JavaScript, Python, SQL, PostgreSQL, AWS, Azure, Git, GitHub Actions, HTML, CSS e Linux.
Consultas SQL e SQL produziram a mesma saída individual. Os demais pares não produziram competências configuradas nessa rotina.
A taxonomia do código possui 46 rótulos. Ela não inclui os demais candidatos.

O teste não executou leitores de arquivos, aplicação completa ou ATS proprietário.
As rotinas de experiência e formação não foram reavaliadas. Nenhuma regra de extração foi alterada.
Não houve testes de tela, teclado ou impressão. A página e a exportação TXT permaneceram intactas.

Cinco atividades declaradas ainda não aparecem como tags: controle de acessos, controle de permissões, sincronização, histórico de versões e backup.
A declaração limita essas atividades ao ambiente da equipe. Ela não comprova administração corporativa ou arquitetura de infraestrutura em nuvem.
Esses possíveis acréscimos não foram aplicados nem incluídos no teste dos oito aliases.

Office 365 não foi convertido em Microsoft 365. Windows 11 não recebeu a edição Pro.
As fontes não autorizam acrescentar serviços específicos de AWS, Azure ou Vercel por associação com o nome da plataforma.
Metodologias ágeis e Scrum permanecem como conceitos independentes.

O [registro da revisão](historico-ats/README.md) preserva o inventário, fontes, relações, entradas, saídas e hashes.
Os aliases podem orientar uma adequação futura. O ensaio atual não demonstra melhora de extração nem aumento de aprovação em candidaturas.

### Aplicação posterior dos termos ingleses

O responsável autorizou acrescentar os termos correspondentes em inglês nas tags ocultas da página pt-BR.
Foram incluídos sete termos distintos, com nove ocorrências. Technical documentation acompanha as três ocorrências portuguesas nos respectivos contextos.
Os termos permanecem nas listas correspondentes, com lang="en". Os nomes em português foram preservados.

O bloco oculto passou a ter 170 ocorrências e 152 rótulos distintos.
O conteúdo principal mantém 161 ocorrências e 145 rótulos distintos. Ele permaneceu idêntico, byte a byte, ao conteúdo publicado anteriormente.
O inventário TXT anterior continua descrevendo os nomes portugueses do conteúdo principal. A exportação curricular TXT permaneceu intacta.

IT support conserva a indicação N1. Business intelligence permanece nos conteúdos previstos da graduação em andamento.
Um parágrafo explicita o conhecimento introdutório em aprendizado de máquina.
Microsoft Office software e as cinco atividades sem tag não foram acrescentados.

O adaptador reproduziu exatamente as 316 linhas do ensaio positivo anterior, antes da inclusão dos aliases.
Depois, o teste leu o HTML atualizado e executou as rotinas originais do cvats.
As três experiências e a graduação produziram os mesmos campos do positivo anterior.
Os quatro controles de remoção e substituição também passaram.

O segundo parser público recuperou as mesmas 11 tecnologias a partir das tags ocultas.
Esse resultado confirma preservação da extração anterior. Ele não demonstra ganho de recuperação dos novos termos.
Os 17 cursos e os dados da graduação permaneceram intactos.

O positivo continua limitado à leitura dedicada do bloco oculto, com posições lógicas sintéticas.
A leitura da página inteira e a variante que exclui hidden não foram reavaliadas nesta alteração.
Não houve testes de tela, teclado, impressão, PDF ou DOCX. Nenhum ATS proprietário foi executado.

O [teste após a aplicação](historico-ats/README.md) preserva a entrada atual, saídas, controles, fontes e hashes.

### Lista única para consulta

O responsável adotou uma lista única, mantida manualmente. A pasta solicitada é Lista_de_tags, na raiz do projeto.
A [cópia de consulta](../Lista_de_tags/lista-geral-alfabeto-latino.txt) contém os dados públicos do bloco oculto pt-BR.
Ela preserva as 170 ocorrências de tags, os contextos, as experiências, a graduação, os 17 cursos, o TOEIC e os projetos.
As demais traduções ainda não foram acrescentadas. Quatorze arquivos para outros sistemas de escrita foram criados vazios.

O cabeçalho informa o propósito da lista e orienta preservar nomes, datas, qualificações, contextos e atribuições.
Ele aparece no início da cópia TXT. No HTML, aparece depois do nome, ainda no início do bloco oculto.
Essa posição manteve a identificação correta do candidato nos dois parsers públicos anteriores.
As instruções textuais não alteram os algoritmos dos parsers determinísticos.

As rotinas originais do cvats mantiveram as três experiências e a graduação, com os mesmos campos do ensaio anterior.
O segundo parser recuperou as mesmas 11 tecnologias. O conteúdo visível e a exportação curricular TXT permaneceram intactos.
O ensaio não tratou a cópia de consulta como arquivo de currículo submetido ao parser.
Não houve testes de tela, teclado, impressão, PDF ou DOCX. Nenhum ATS proprietário foi executado.

O [registro da lista geral](verificacao-lista-geral-tags-2026-10-14.json) preserva instruções, arquivos, hashes, entradas, saídas e verificações.
O [guia da pasta](../Lista_de_tags/README.md) identifica os arquivos reservados e descreve a manutenção manual.

### Repetição após o commit 9f2b37f

Em 14 de outubro de 2026, a verificação foi repetida sobre a versão 9f2b37f.
O adaptador reproduziu integralmente as 331 linhas do ensaio anterior antes de gerar as 350 linhas atuais.
O relatório passou a registrar a entrada atual e os resultados dos três parsers locais.
Os hashes de texto usam UTF-8 com quebras de linha LF.

O conteúdo principal contém 177 ocorrências de tags e 160 rótulos distintos.
O bloco oculto contém 186 ocorrências e 167 rótulos distintos.
A cópia TXT corresponde às linhas lógicas do bloco oculto, com as instruções antes da identificação.
Os 17 cursos, as três experiências e a graduação mantiveram os dados verificados no ensaio anterior.
Os 14 arquivos reservados permanecem vazios.

O segundo parser preservou as 11 tecnologias anteriores. Ele retornou também C como falso positivo.
Um teste isolado confirmou que o resumo sobre código aberto dispara esse rótulo.
A expressão regular reconhece a letra c antes do caractere ó como uma palavra isolada.
Esse resultado não comprova conhecimento da linguagem C.

O resultado positivo limita-se à integridade da cópia e à preservação dos campos verificados.
As regras dos parsers e os arquivos do site permaneceram intactos nesta repetição.
Não houve testes de navegador, impressão, PDF, DOCX ou ATS proprietário.
Os resultados anteriores permanecem recuperáveis pelo histórico Git e pelo acervo histórico.

Após a revisão do texto sobre CNH e PID, a entrada passou de 350 para 351 linhas.
Os três parsers mantiveram as mesmas saídas. A cópia TXT e os hashes foram atualizados.
As [fontes e os limites sobre condução](referencias/conducao-internacional.md) registram o conteúdo sincronizado nas cinco páginas principais.

Na revisão seguinte, os nomes das instituições dos cursos e os títulos dos projetos receberam links apenas em pt-BR.
O texto do PPC passou a usar “Conforme o projeto pedagógico do curso (PPC)”.
O responsável autorizou retirar a indicação redundante de formação em andamento, mantendo a conclusão prevista.
O cvats manteve os dados da graduação e retirou somente esse sufixo do campo de data.
As experiências e as saídas dos outros dois parsers permaneceram iguais.
A entrada continua com 351 linhas. As tags e os dados dos 17 cursos permaneceram iguais.
Os [destinos e as decisões](referencias/links-instituicoes.md) acompanham o registro atualizado da lista geral.

O terceiro parágrafo da RealFort passou a começar com “Realizei diagnósticos de redes ópticas”, por solicitação do responsável.
O uso de power meter e VFL e o apoio ao diagnóstico por OTDR foram preservados.
O HTML pt-BR, o bloco oculto, a lista geral e a saída do cvats receberam a mesma descrição.
Os três parsers foram executados novamente. As demais experiências e a graduação mantiveram os campos do ensaio anterior.

Na simplificação seguinte da seção Condução, o responsável solicitou acrescentar a tag Permissão Internacional para Dirigir (PID) em pt-BR.
A explicação passou a ter duas frases. O conteúdo principal contém 178 ocorrências de tags e 161 rótulos distintos.
O bloco oculto contém 187 ocorrências e 168 rótulos distintos.
A lista geral e seus hashes foram atualizados. Os três parsers mantiveram as mesmas saídas com 351 linhas de entrada.

Por solicitação posterior, a segunda frase passou a indicar destinos de turismo no Mercosul, Alemanha, França e Itália.
O detalhamento das regras foi retirado da página. A cópia TXT, os hashes e a entrada dos parsers foram sincronizados.
Os três parsers mantiveram as mesmas saídas.

### Revisão das experiências e dos projetos pt-BR

As descrições profissionais foram atualizadas conforme as novas declarações do responsável.
Os projetos passaram a apresentar descrição seguida de tecnologias e competências organizadas por assunto.
O relatório acadêmico do SGCS fundamentou as ferramentas e as competências da equipe.
As [evidências e os limites](experiencias-e-projetos-pt-br-2026-10-14.md) distinguem as ferramentas utilizadas das alternativas avaliadas.

A entrada passou a conter 391 linhas lógicas.
O conteúdo principal possui 212 ocorrências de tags e o bloco oculto possui 222.
O cvats preservou empresas, cargos, datas e graduação. As descrições das experiências refletem a revisão.
O segundo parser manteve os mesmos 12 rótulos, incluindo o falso positivo C já registrado.
O TXT e os hashes foram atualizados. Os dados dos cursos permaneceram iguais.

### Normalização e traduções das tags

A revisão seguinte padronizou nomes de produtos e termos portugueses em pt-BR.
As formas inglesas anteriores de AWS, Azure, NGINX, organização de cabos e comutadores permanecem como aliases ocultos.
O conteúdo visível possui 212 ocorrências de tags. O bloco oculto e a lista geral possuem 227.
As 15 ocorrências suplementares foram justificadas e comparadas por contexto.

As 394 linhas da entrada atual mantiveram as mesmas saídas dos três parsers.
O falso positivo C permanece documentado. Os aliases adicionais não demonstraram ganho de reconhecimento neste ensaio.
Os 14 TXT antes reservados receberam traduções editoriais, com 227 ocorrências e 192 rótulos distintos por arquivo.
O [registro integral](verificacao-normalizacao-tags-pt-br-2026-10-14.json) preserva todas as ocorrências visíveis, ocultas e da lista geral.
O [glossário e o manifesto](tags-multilingues/README.md) preservam as correspondências e os hashes das traduções.
As traduções permanecem fora do site e não declaram fluência do candidato nas línguas de destino.
