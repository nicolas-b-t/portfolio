# Análise de palavras-chave — cinco idiomas

Data: 13 de outubro de 2026.
Base: conteúdo sincronizado em pt-BR, pt-PT, inglês, es-419 e es-ES, com as declarações confirmadas do responsável.
As recomendações não foram aplicadas à versão examinada por este relatório.
O responsável autorizou a aplicação posterior em 13 de outubro.
O [relatório de adequação](../../relatorio-adequacao-termos-ats-2026-10-13.md) registra os termos aplicados e suas evidências.
Os CSVs e o manifesto desta análise preservam a versão anterior à adequação.

## Resultado e leitura dos arquivos

A análise encontrou relações úteis para suporte, manutenção, documentação, colaboração e gestão de projetos.
Os termos específicos de redes continuam necessários para explicar o trabalho realizado.
As fontes editoriais fornecem vocabulário complementar. Elas não demonstram um catálogo completo de ATS brasileiro.

- [Inventário](inventario-conteudo-2026-10-13.csv): trechos das páginas e declarações, com contexto, linha e idioma.
- [Correspondências](correspondencias-palavras-chave-2026-10-13.csv): registros das fontes, classes, justificativas, limites e recomendações.
- [Manifesto da análise](manifesto-analise-2026-10-13.json): hashes das páginas, entradas examinadas e contagens.
- [Manifesto das novas fontes](manifesto-fontes-editoriais-2026-10-13.json): versões, licenças, hashes e recuperação dos clones locais.

O inventário contém 1.254 unidades textuais. Há 248 por idioma e 14 declarações adicionais em português brasileiro.
Ele inclui descrições, títulos, cursos, metadados, fotografias e agradecimentos.
A cópia exclusiva para impressão foi desconsiderada.
Um assunto pode aparecer em várias seções. Essas ocorrências preservam contextos diferentes.

O CSV contém 2.205 registros de análise.
Há 324 relações revisadas semanticamente, 1.158 achados lexicais e 723 unidades sem correspondência confirmada.
Essas contagens incluem repetições entre idiomas, trechos e fontes.
Elas não representam uma quantidade de competências nem uma pontuação de ATS.

## Método e prioridade das fontes

A triagem normalizou Unicode, caixa e espaços. Ela preservou acentos e procurou palavras completas.
Nomes alternativos com até três caracteres foram excluídos da triagem por ambiguidade.
Assim, a preposição portuguesa “em” não foi tratada como abreviação de um cargo de engenharia.

O campo estado_revisao separa triagem_lexical, revisado_semanticamente e sem_correspondencia_confirmada.
Uma coincidência literal identifica vocabulário. Ela não confirma o alcance da competência.
As relações revisadas consideram atividades, autoria, formação e definições originais.

| Classe | Significado |
| --- | --- |
| correspondencia_literal | O trecho contém o rótulo da fonte como palavras completas |
| sinonimo_declarado_pela_fonte | A fonte apresenta o nome alternativo. A classificação não valida automaticamente essa relação |
| equivalencia_por_uri | Os rótulos oficiais compartilham a URI ESCO. O contexto pessoal foi examinado separadamente |
| interpretacao_editorial | A associação depende de tradução ou interpretação do contexto |
| relacao_parcial | Os conceitos compartilham apenas parte do alcance, ou a evidência é insuficiente |
| ausencia | Nenhuma correspondência foi confirmada no recorte. Isso não demonstra falta de competência |

Odoo fornece registros iniciais e demonstrativos ligados ao recrutamento.
O recorte Sólides fornece 21 campos hardSkills de quatro vagas públicas, com IDs e nomes originais.
Esses campos podem refletir configurações das empresas. Eles não demonstram um catálogo global curado.
O campo level expressa o requisito da vaga. Ele não avalia o responsável pelo portfólio.

ESCO fornece definições e rótulos oficiais. O*NET fornece referências ocupacionais e nomes de software.
Nesta fornece uma taxonomia de pesquisa. Os dois repositórios e o artigo fornecem sugestões editoriais.
Essas fontes complementares não foram apresentadas como cadastros internos de fornecedores.

A ESCO v1.2.1 possui 13.939 URIs distintas nos três idiomas examinados.
As etiquetas pt e es não distinguem variantes regionais.
O CSV preserva rótulos oficiais portugueses, ingleses e espanhóis sem adaptar os originais.
O idioma da página e o idioma do trecho aparecem em campos separados.
Isso preserva os títulos oficiais de cursos dentro das traduções.

## Correspondências prioritárias

| Conteúdo atual | Referência e classificação | Recomendação para revisão posterior |
| --- | --- | --- |
| Gestão de projetos | ESCO project management. Rótulos ligados pela mesma URI | Manter cursos e SGCS como evidências. Preservar projeto acadêmico em andamento |
| Suporte hospitalar, N1/N2 | ESCO provide ICT support. Sólides ID 2064833 | Manter setor, níveis e incidentes descritos. Não copiar requisitos de plataformas não utilizadas |
| Manutenção de computadores e periféricos | ESCO maintain computer hardware | Manter manutenção preventiva e corretiva, com os equipamentos efetivamente atendidos |
| Manutenção de impressoras | Sólides ID 1890998 | Considerar a associação específica. Não inferir a formação técnica exigida por outro registro |
| Manuais de usuário | ESCO provide user documentation | Preservar autoria e finalidade dos manuais. Não abranger todos os tipos de documentação |
| Trabalho em equipe | ESCO work in teams. Sólides ID 872818 | Distinguir colaboração de gestão de equipe. Ignorar o nível exigido pela vaga |
| Gestão da equipe do SGCS | ESCO lead a team | Restringir a afirmação ao projeto acadêmico e às responsabilidades descritas |
| Levantamento de requisitos | ESCO identify customer requirements | Preservar a atribuição à equipe do SGCS. Não transferir a execução integral ao responsável |
| Modelagem de dados | ESCO data models, com nome alternativo data modelling | Preservar o curso. Não acrescentar SQL, ETL ou administração de bancos |
| Uso das plataformas declaradas | ESCO web based collaborative platforms e nomes O*NET | Considerar inclusão contextual das ferramentas. Não afirmar administração corporativa |

Os exemplos da ESCO são referências de nomenclatura.
Quando o conceito é classificado como conhecimento, o CSV preserva essa informação.
O contexto acadêmico não foi convertido em experiência profissional concluída.

## Relações que exigem restrição

| Associação candidata | Limite e decisão |
| --- | --- |
| Gestão de projetos e PMO, Sólides ID 1943693 | Somente gestão de projetos está sustentada. Não acrescentar PMO |
| Gestão financeira e FP&A | Cursos e PPC não demonstram planejamento financeiro empresarial ou modelagem profissional |
| Chamados e incident management | Resolver e escalonar chamados não demonstra responsabilidade por todo o processo de gestão |
| Prototipação, MVP e prototyping | MVP não é sinônimo de protótipo. Preservar a participação da equipe |
| GitHub Actions e CI/CD | A publicação automatizada não demonstra integração contínua completa ou operação DevOps |
| Fusão e splice cable | O conceito inclui outros cabos. Preservar fibra óptica e condição de aprendiz |
| Fluxo de caixa e handle cash flow | A definição original também cita apostas. Rejeitar substituição baseada apenas no nome |
| Melhoria de processos e melhoria contínua | A formação White Belt é introdutória. Não afirmar implantação ou resultados sem evidência |
| Controle de permissões e manage cloud data and storage | A definição exige retenção, criptografia e capacidade. Rejeitar a competência ampla |
| JavaScript e Java | São linguagens distintas. A triagem não aceita correspondência por parte da palavra |
| Python e pandas | São uma linguagem e uma biblioteca. O campo synonyms do dataset não prova equivalência |
| Produtos citados em fotografias e perfis | A presença no texto não demonstra domínio nem execução individual |

O dataset editorial possui 116 registros, 63 rótulos distintos e dez famílias profissionais.
O README anuncia 120+. A contagem dos arquivos examinados foi preservada no manifesto.
CSV, JSON e recortes por profissão são consistentes.
Não há proveniência individual dos anúncios alegados pela metodologia.
Os níveis junior, mid e senior permanecem como metadados da fonte.

As listas editoriais possuem maior concentração em funções digitais e de negócios.
Elas não cobrem adequadamente cada ferramenta de suporte e instalação de redes deste perfil.
Ausência de SC/APC, OTDR ou PPPoE nessas listas não autoriza remover esses termos.
Não foi escolhida uma vaga específica para orientar a comparação.

## Próxima revisão e limites de verificação

1. Priorize relações marcadas como revisado_semanticamente.
2. Confira a fonte, a definição e o contexto de cada sugestão.
3. Preserve rótulos, limitações e qualificações oficiais.
4. Registre a justificativa antes de modificar o conteúdo publicado.

A decisão inicial desta etapa limitou a entrega à análise e às recomendações.
O relatório de adequação registra a autorização posterior e as alterações resultantes.
Nenhum currículo foi enviado a um serviço externo de avaliação.
Nenhum parser de ATS ou processo real de seleção foi testado.
Não há promessa de pontuação, aprovação ou aumento de convites para entrevistas.

O PPC público já vinculado no currículo não substitui o documento específico da Fatec Franco da Rocha.
Essa limitação permanece registrada no [guia das fontes acadêmicas](../guia-de-uso.md#fontes-acadêmicas).
A sincronização preservou a referência vigente. Ela não ampliou competências a partir desse documento.
