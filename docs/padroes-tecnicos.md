# Padrões técnicos aplicados ao portfólio

Este arquivo registra a aplicação da base local `docs/repertorio-tecnico-site/` ao portfólio.
Cada seção corresponde a uma pasta técnica, de `01` a `12`.
O [plano](../PLANO-APLICACAO-PADROES-TECNICOS.md) define as fases, a ordem e os limites.
A situação das fases fica no plano, §6. Não repita a tabela aqui.

Cada seção termina com uma decisão: aplicada, aplicada parcialmente, não aplicável ou lacuna.
Nenhuma seção declara conformidade, certificação ou equivalência com norma.

## 1. Gestão — fase 01

### 1.1 Decisão

**Aplicar parcialmente o PM2 3.1.**

Fonte: `docs/repertorio-tecnico-site/gestao-requisitos-testes/Comissao Europeia - PM2 Metodologia de Gestao de Projetos (PT) - v3.1.pdf`.

O guia completo pressupõe projeto com mais de 4 ou 5 semanas e mais de 2 ou 3 pessoas (§3.4).
Este projeto tem um responsável, um agente de implementação e cerca de 14 sessões.
O site já está publicado e não tem equipe, orçamento próprio nem contratação.
Por isso, a aplicação completa criaria artefatos sem uso.

O §3.6 pede que a adaptação fique registrada no Manual do Projeto.
Este projeto não cria esse manual, para não duplicar o plano.
A adaptação fica registrada nesta seção, com a justificativa de cada corte.

**Mantido:**

- ficha do projeto, equivalente ao Termo de Abertura (§5.4);
- matriz de partes interessadas (§6.3);
- plano de trabalho com fases, esforço e marcos (§6.4);
- registros de risco e de decisão (§B.8 e §B.10);
- portas de fase com aprovação do responsável (§3.2.6).

**Dispensado, com motivo:**

| Artefato | Motivo |
| --- | --- |
| Caso de Negócio | Não há decisão de investimento, receita ou orçamento. |
| Manual do Projeto | O plano e esta seção cumprem o registro; um manual duplicaria as mesmas regras. |
| Plano de Externalização | Não há contratação. |
| Plano de Transição e Plano de Implementação Operacional | O site já opera em GitHub Pages. |
| Comitê Diretivo e Gabinete de Apoio | Não há equipe nem estrutura organizacional. |
| Nota formal de aceitação | O aceite fica na tabela de situação do plano, §6. |

**Papéis:** o responsável acumula as funções de decisão (AGB, PSC, PO e BM).
O agente de implementação exerce PM e PCT.
Não há SP, PSO, BIG nem equipe separada.

### 1.2 Ficha do projeto

Equivalente ao Termo de Abertura (§5.4): curto, com necessidades de alto nível e sem requisitos detalhados.

| Campo | Conteúdo |
| --- | --- |
| Objeto | Aplicação dos padrões técnicos da base local ao portfólio estático, com formalização iniciada em 28/10/2026. |
| Objetivo | Registrar, por pasta técnica, a decisão de aplicação e a evidência, com foco inicial em pt-BR. |
| Escopo incluído | Doze fases, documentos versionados, verificações estáticas e em navegador, registro de riscos e de decisões. |
| Escopo excluído | Ampliar ou substituir a base local; consultar o acervo principal; alterar conteúdo ou site sem aprovação; novas funcionalidades (blog, formulário, analytics, domínio próprio); traduzir novas páginas antes de concluir pt-BR; JavaScript, backend, framework ou build; declarar conformidade. |
| Entregáveis | Doze seções neste arquivo; `docs/requisitos.md`; `docs/adr/`; `CHANGELOG`; página 404; atualizações de manutenção e do guia de redação; checklist de segurança; registro final. |
| Critérios de aceite | Doze seções preenchidas ou com lacuna registrada; uma decisão por fase; fonte local existente para cada citação; `git diff --check` limpo; revisão do responsável; nenhuma alegação de conformidade. |
| Marcos | M1 processo; M2 produto documentado; M3 publicação e segurança; M4 lacunas. Ver plano, §5. Início da formalização: 28/10/2026. |
| Restrições | Base local somente leitura; uma seção, uma atualização de guia e, quando estrutural, um ADR por fase; sem limite quantitativo de desempenho; teste empírico. |
| Premissas | O responsável aprova mudanças de site e decisões ambíguas; a base local continua disponível; o GitHub Pages continua sendo a hospedagem. |
| Aprovação | Responsável pelo projeto. Aceita em 02/11/2026. |

### 1.3 Partes interessadas

Matriz do §6.3, adaptada. Não há contato pessoal nesta tabela, para não ampliar a exposição de dados.
O responsável é o operador que decide resoluções e aprovações.

| Parte interessada | Papel no projeto | Interesse | Influência |
| --- | --- | --- | --- |
| Responsável pelo projeto | Aprova escopo, mudanças e aceite; dono do repositório | Alto | Alta |
| Agente de implementação | Executa as fases, registra evidência e propõe decisões | Alto | Média |
| Visitantes e recrutadores | Leem o currículo, usam teclado, leitor de tela e impressão | Alto | Baixa |
| GitHub | Hospeda o repositório e publica o site | Médio | Média |
| Sites externos vinculados | Destino de links para Drive, LinkedIn, projetos e instituições | Baixo | Baixa |
| Mantenedores das fontes | Procedência das normas citadas | Baixo | Baixa |

### 1.4 Plano de trabalho

O plano completo está em `PLANO-APLICACAO-PADROES-TECNICOS.md`, §5.
Ele contém a ordem das doze fases, os quatro marcos e o esforço estimado.
A ordem e o motivo de cada fase não se repetem aqui, conforme a diretriz de não duplicar informação (§6.6).

| Fase | Executa | Critério de saída |
| --- | --- | --- |
| 01 | Agente | Seção “Gestão” aceita. |
| 02 | Agente | Requisitos, glossário e matriz aceitos. |
| 03 | Agente | Processo e Definition of Done aplicados a uma mudança. |
| 04 | Agente | ADRs, arquitetura e convenções aceitos. |
| 05 | Agente | Checklist de acessibilidade e backlog aprovados. |
| 06 | Agente | Inventário e decisão sobre privacidade registrados. |
| 07 | Agente | Princípios de documentação e linha de base registrados. |
| 08 | Agente | Checklist de segurança e inventário de ativos aceitos. |
| 09 | Agente | Publicação, HTTPS e idiomas conferidos. |
| 10 | Agente | Procedimento aplicado a uma mudança piloto. |
| 11 | Agente | Terminologia das competências revisada. |
| 12 | Agente | Riscos, indicadores e data de revisão registrados. |

O agente executa. O responsável responde pelas decisões e aprova mudanças de site.
O escopo inicial prioriza pt-BR. As cinco variantes continuam publicadas e recebem sincronização; novas páginas e traduções entram em expansão futura.
A formalização começou em 28/10/2026. As fases seguintes não têm data marcada; o responsável registra a data quando cada uma começar.

A linha de base passa a valer quando o responsável aprovar o plano e o arquivo for versionado.
Mudança de ordem, escopo ou critério exige pedido, análise de impacto e aprovação, conforme a fase 10.

### 1.5 Riscos iniciais

Registro no formato do §B.8. Escala de 1 a 5; nível = probabilidade × impacto, em valor absoluto.

| ID | Risco | P | I | NR | Dono | Resposta | Fase |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R01 | O site publica nome, contato, país, formação, experiências e fotografias sem aviso de privacidade. O visitante não encontra como pedir correção ou remoção. | 3 | -4 | 12 | Responsável | Aceitar: a decisão de 02/11/2026 mantém os dados e dispensa aviso; revisar se a exposição mudar. | 06 |
| R02 | Mudança feita só em pt-BR deixa as cinco variantes com fatos diferentes. O visitante lê informação desatualizada em outro idioma. | 3 | -3 | 9 | Agente | Reduzir: sincronizar a partir de pt-BR e conferir as variantes afetadas. | 03 e 05 |
| R03 | Link externo expira ou muda de endereço. O visitante encontra página inexistente e perde a evidência. | 4 | -2 | 8 | Agente | Reduzir: conferência periódica e registro do resultado. | 09 e 12 |
| R04 | Mudança de CSS ou conteúdo remove foco visível, contraste ou nome acessível. O visitante que usa teclado ou leitor de tela perde acesso. | 3 | -3 | 9 | Agente | Reduzir: checklist WCAG 2.2 e ensaio manual. | 05 |
| R05 | A perda de acesso à conta ou ao repositório interrompe a publicação e o histórico. O site sai do ar sem via de correção. | 2 | -5 | 10 | Responsável | Reduzir: concluir o 2FA; manter admin único, autorização de alterações e cópia local. | 08 |
| R06 | A base local é ignorada pelo Git e existe só nesta máquina. Uma falha de disco remove a procedência das fontes citadas. | 2 | -3 | 6 | Responsável | Reduzir: backup RAR da v1 concluído; criar backup da v2, preferir formato aberto e cópia externa. | 07 |
| R07 | Cada fase cria um manual próprio. O volume cresce e as regras divergem. | 3 | -2 | 6 | Responsável | Reduzir: orçamento documental do plano, §3. | 01 e 04 |
| R08 | Alterações locais não versionadas se perdem. O trabalho de conteúdo não chega ao site. | 2 | -3 | 6 | Responsável | Reduzir: os cinco arquivos entram no próximo commit. | 10 |
| R09 | O repositório público expõe dados pessoais e o histórico. A cópia de publicação pode manter informação que não deve ser pública. | 3 | -3 | 9 | Responsável | Reduzir: publicar cópia limpa sem dados pessoais e revisar o histórico. | 08 |
| R10 | Os ícones Lucide estão no site sem arquivo de licença. A procedência pode ficar duvidosa. | 2 | -2 | 4 | Agente | Reduzir: incluir o aviso ISC e a origem dos ícones. | 04 |

O registro é revisto ao fim de cada marco.
Risco novo entra com ID seguinte, dono e resposta.

### 1.6 Portas de fase

Adaptação do §3.2.6, ajustada pela decisão de 02/11/2026.
As portas continuam como checkpoints de evidência, mas não param o trabalho.
O agente segue quando não houver ambiguidade nem mudança de site.
Mudança de site, conteúdo ou decisão ambígua exige aprovação antes.

| Porta | Momento | Evidência | Efeito |
| --- | --- | --- | --- |
| RfP adaptado | Fim do marco M1 | Ficha, matriz, riscos, requisitos, procedimento de mudança e processo de teste registrados | M2 liberado; a ficha foi aceita em 02/11/2026 |
| RfE adaptado | Fim do marco M2 | ADRs, arquitetura, linha de base, guia de redação e checklist de acessibilidade | Segue para M3 salvo ambiguidade |
| RfC adaptado | Fim do marco M4 | Doze seções, decisões, evidências, `git diff --check` limpo e lições | Encerramento após aceite final |

O aceite da ficha não fecha o RfP.
O RfP fecha no fim do M1, com requisitos, mudança e qualidade registrados.

### 1.7 Verificação da fase

| Item | Resultado |
| --- | --- |
| Fonte local consultada | PM2 3.1, §3.2 a §3.6, §4.12, §5.4, §5.5, §6.3, §6.4, §6.6, §B.8 e §B.10. |
| Critério de aplicação | §3.4 usado para justificar a aplicação parcial; §3.6 usado para registrar a adaptação. |
| Coerência com o plano | Ordem, marcos e critério de conclusão conferidos no plano, §5 e §9. |
| Aceite da ficha | 02/11/2026, pelo responsável. |
| Estado do repositório | 22 arquivos HTML; nenhum aviso de privacidade localizado; cinco arquivos do responsável aguardam o próximo commit. |
| Datas | Formalização em 28/10/2026; fases seguintes sem data. |
| Documentação | Este arquivo criado e indexado em `docs/README.md`. |
| Verificação de texto | `git diff --check` e conferência de espaços finais. |

**Ressalvas:**

- A formalização começou em 28/10/2026. As fases 02 a 12 não têm data; o responsável registra a data ao liberar cada fase.
- A ficha foi aceita em 02/11/2026. O RfP só fecha no fim do M1.
- A base local não está no Git. A citação de caminho e edição preserva a procedência, não o arquivo.
- A publicação depende de commit e push, ainda não executados.

### 1.8 Limites

- Não há PMO, Comitê Diretivo, Caso de Negócio nem equipe dedicada.
- Não há promessa de prazo, custo ou benefício financeiro.
- Não há declaração de conformidade com o PM2.
- Não há aviso de privacidade, por decisão de 02/11/2026. A fase 06 registra a decisão.
- Não há limite quantitativo de desempenho. A avaliação é empírica e busca valor com economia de recursos.
- Não há blog, formulário, analytics ou domínio próprio no escopo inicial.
- O encerramento usa o critério de conclusão do plano, §9, e uma nota final nesta seção.
- Lições aprendidas e resultado final entram aqui, sem relatório separado.

### 1.9 Registro de decisões

Registro do §B.10, com as decisões recebidas em 02/11/2026.
Decisão nova entra com ID seguinte e data.

| ID | Decisão |
| --- | --- |
| D-01 | Ficha da fase 01 aceita em 02/11/2026. |
| D-02 | Formalização do projeto iniciada em 28/10/2026. |
| D-03 | Fases 06, 11 e 12 registram a lacuna e um inventário factual mínimo. |
| D-04 | Fases 05 e 09 corrigem apenas itens objetivos e reversíveis, com aprovação item a item. |
| D-05 | Git: commit e push autorizados, na branch `main`, sem parada obrigatória em cada porta. |
| D-06 | Parada apenas para decisão ambígua, mudança de site ou conteúdo. |
| D-07 | Escopo inicial em pt-BR; expansão de idiomas e novas funcionalidades ficam para depois. |
| D-08 | Sem limite quantitativo de desempenho; teste empírico. |
| D-09 | Sem blog, formulário, analytics ou domínio próprio no escopo inicial. |
| D-10 | Pré-publicação: conferir HTML, links internos e temas claro e escuro. |
| D-11 | Manter `CHANGELOG`. |
| D-12 | Sem aviso de privacidade; dados publicados mantidos como estão. Dados sensíveis ficam só em cópia local. |
| D-13 | Fotografias são de autoria do responsável; recomendações têm autorização. |
| D-14 | Backup em RAR da v1 concluído; criar a v2. |
| D-15 | Segurança: 2FA desativado; apenas o responsável é admin; repositório público; cópia limpa sem dados pessoais ao final. |
| D-16 | Incidente: resposta em até 1 dia. |
| D-17 | Manter GitHub Pages; criar página 404 no mesmo estilo; acompanhamento manual. |
| D-18 | Competências vêm de `docs/fontes/competencias-declaradas.json`; certificações concluídas entram manualmente; ajustes são apenas apontados. |
| D-19 | Revisão conforme evento novo; indicadores manuais neste escopo. |
| D-20 | Inglês revisado pelo responsável; espanhol mantém a diferença entre `es-419` e `es-ES`; inconsistências vão ao operador. |
| D-21 | Documentação em pt-BR; o plano fica na raiz e será versionado. |
| D-22 | Reversão: reverter até cinco commits. |
| D-23 | Público principal: recrutadores e gestores de contratação. Objetivo: emprego. Ações: currículo, projetos e contato. |
| D-24 | Manter a voz atual; ajustes de texto são apenas apontados, sem reescrita sem aprovação. |
| D-25 | Ordem das fases e estimativa de cerca de 14 sessões confirmadas. |
| D-26 | Apenas o responsável é administrador. Alterações na `main` exigem sua autorização; a proteção técnica será conferida na fase 08. |
| D-27 | O botão de download do currículo permanece visível e inativo até a publicação do PDF. |
| D-28 | O 2FA está em ativação; revisar na fase 08. |
| D-29 | A página 404 e o `CHANGELOG` estão aprovados; serão criados nas fases 09 e 10. |
| D-30 | O catálogo de requisitos foi aceito em 02/11/2026; não há novos requisitos no momento. |
| D-31 | Critérios qualitativos são avaliados pelo operador, com registro da decisão. |

## 2. Requisitos — fase 02

### 2.1 Decisão

**Aplicar o CPRE 3.3.0 de forma parcial.**

Fontes: `gestao-requisitos-testes/IREB - CPRE Foundation Level Syllabus (EN) - v3.3.0.pdf`, `gestao-requisitos-testes/IREB Martin Glinz - Glossary of Requirements Engineering Terminology (EN) - v2.2.0.pdf` e `documentacao-revisao/Organizacao - Redacao e Rastreabilidade de Requisitos (PT-BR) - v1.0.md`.

O catálogo está em [Requisitos do site](requisitos.md).
Aceite: 02/11/2026.
A aplicação parcial mantém a disciplina de qualidade, a fronteira do sistema, o glossário, a rastreabilidade e a priorização.
Não há elicitação com usuários externos nem ferramenta de gestão de requisitos.

### 2.2 O que foi aplicado

| Prática | Fonte | Resultado |
| --- | --- | --- |
| Características de qualidade | CPRE §3.8, páginas 29 e 30 | Critérios por requisito e por conjunto. |
| Fronteira, contexto e fontes | CPRE §4.1, página 31 | Fronteira e lista de partes interessadas. |
| Glossário | CPRE §3.5; glossário 2.2.0 | Onze termos do projeto definidos. |
| Rastreabilidade | CPRE §6.6, página 43 | Matriz requisito, fonte, critério, fase e situação. |
| Priorização | CPRE §6.8, página 44 | Prioridade essencial, esperado ou opcional. |
| Redação e fundamentação | Documento local, §“Manter a fundamentação” | Identificador, fonte, critério e evidência por item. |

O catálogo tem 14 requisitos funcionais e 11 não funcionais.
Cada item cita uma fonte ou uma decisão registrada.

### 2.3 Verificação

- Todo requisito tem identificador, texto, prioridade, fonte, critério, fase e situação.
- Nenhum requisito ficou sem fonte local ou decisão registrada.
- A conferência estática encontrou 22 arquivos HTML, 45 imagens com `alt` e nenhum link interno quebrado.
- A situação separa comportamento vigente, lacuna, item aprovado e item futuro.
- `git diff --check` passou.

### 2.4 Limites

- O catálogo foi aceito em 02/11/2026 e é a linha de base.
- Critérios qualitativos são avaliados pelo operador, conforme a decisão D-31.
- Não houve validação com usuários externos, leitor de tela ou ferramenta de acessibilidade.
- Não há declaração de conformidade com o CPRE.
- FR-08 foi resolvido: o botão permanece inativo por decisão D-27.
- A página 404 segue pendente. O `CHANGELOG` foi criado na fase 10.

### 2.5 Pendências

1. NFR-08: concluir o 2FA e confirmar a proteção da `main` na fase 08.
2. FR-13: implementar a página 404 na fase 09.

## 3. Processos e qualidade — fase 03

### 3.1 Decisão

**Aplicar o ISTQB CTFL 4.0.1 de forma parcial.**

Fonte: `gestao-requisitos-testes/ISTQB - Certified Tester Foundation Level Syllabus (EN) - v4.0.1.pdf`.

Aplicação: processo de teste, abordagem baseada em risco, níveis adaptados ao site, teste estático, gestão de defeitos e critérios de conclusão.
A base não contém ISO 9001 nem ISO 19011.
Este processo não é um sistema de gestão da qualidade e não declara conformidade.

### 3.2 Processo adaptado

Atividades do §1.4.1, páginas 18 e 19.

| Atividade | Aplicação no site | Evidência |
| --- | --- | --- |
| Planejamento | Definir objetivo, páginas, riscos, ambiente e critérios de saída. | Registro na mudança. |
| Monitoramento e controle | Acompanhar as conferências e corrigir o plano. | Lista de verificações. |
| Análise | Identificar o que testar a partir dos requisitos e riscos. | Requisito e páginas afetadas. |
| Desenho | Transformar a análise em checklist e casos manuais. | Checklist da mudança. |
| Implementação | Preparar servidor local, navegador e dados. | Comando e ambiente usados. |
| Execução | Comparar resultado esperado e obtido. | Resultado por item. |
| Encerramento | Registrar defeitos, lições e pendências. | Relatório da mudança. |

### 3.3 Níveis e tipos

Níveis do §2.2, páginas 28 e 29, adaptados ao porte do projeto.

| Nível adaptado | Objeto | Objetivo |
| --- | --- | --- |
| Inspeção estática | HTML, CSS, documentos e workflow | Encontrar erro antes de abrir o navegador. |
| Ensaio em navegador | Páginas no servidor local | Conferir comportamento e apresentação. |
| Revisão de conteúdo | Fatos, fontes e textos | Preservar precisão e limites da fonte. |
| Conferência pós-publicação | Site publicado | Confirmar que a mudança chegou ao ar. |

Tipos: funcional, não funcional (acessibilidade, compatibilidade, desempenho) e regressão.
A inspeção estática segue o capítulo 3.

### 3.4 Abordagem baseada em risco

Riscos do §5.2, página 51.
O esforço cresce com a exposição do item:

1. dados pessoais, privacidade e segurança;
2. acessibilidade e navegação por teclado;
3. publicação e disponibilidade;
4. conteúdo factual e paridade entre variantes;
5. apresentação e impressão.

Mudança de alto risco exige conferência completa.
Mudança de baixo risco pode usar a conferência mínima, com justificativa registrada.

### 3.5 Definition of Done

Uma mudança termina quando todos os itens aplicáveis estão atendidos.

| Área | Critério |
| --- | --- |
| Autorização | Pedido e aprovação registrados. |
| Escopo | Arquivos e páginas afetados identificados. |
| Conteúdo | Fatos com fonte; variantes sincronizadas ou lacuna registrada. |
| Estrutura | HTML semântico, títulos, links internos e âncoras conferidos. |
| Acessibilidade | Teclado, foco, contraste, 320 CSS px, zoom, temas e impressão conferidos quando aplicável. |
| Cópia oculta | Dados iguais aos da tela; ausente na impressão. |
| Publicação | Workflow e permissões conferidos; página publicada aberta. |
| Documentação | Plano, requisitos, guia e `CHANGELOG` atualizados. |
| Texto | `git diff --check` limpo e sem espaços finais. |
| Qualidade | Critérios qualitativos avaliados pelo operador, conforme D-31. |

### 3.6 Registro de defeito

Formato do §5.5, páginas 56 e 57.

Campos: identificador, data, título, objeto e ambiente, contexto, passos, resultado esperado, resultado obtido, severidade, prioridade, situação, causa, correção e verificação.

Severidade: S1 bloqueia o uso; S2 afeta conteúdo ou acesso relevante; S3 afeta documentação ou apresentação; S4 é cosmético.
Prioridade: P1 corrige antes de publicar; P2 corrige na mesma fase; P3 entra no backlog; P4 pode ser aceito.

Fluxo: aberto, em análise, corrigido, em confirmação, fechado.
Defeito falso ou duplicado é rejeitado com motivo.

### 3.7 Piloto

O piloto usou um defeito real encontrado na revisão da fase 10.

| Campo | Conteúdo |
| --- | --- |
| ID | D-001 |
| Data | 02/11/2026 |
| Título | Seção de mudanças numerada como 3 em vez de 10. |
| Objeto e ambiente | `docs/padroes-tecnicos.md`, revisão estática. |
| Contexto | Conferência da numeração por pasta técnica. |
| Esperado | Seção 10, coerente com a pasta `10_GESTAO_DE_MUDANCAS`. |
| Obtido | Seção 3, na ordem de execução. |
| Severidade | S3. |
| Prioridade | P2. |
| Causa | Numeração usada pela ordem de execução, não pela pasta. |
| Correção | Renumeração para 10 e ajuste das referências. |
| Verificação | Títulos 1, 2 e 10; links conferidos; commit `61fa42a`. |
| Situação | Fechado. |

Lição: conferir a numeração por pasta antes de cada commit.

### 3.8 Verificação e limites

- O processo foi aplicado ao piloto D-001, com correção e confirmação registradas.
- Não há suíte automatizada nem equipe independente de testes.
- Não há ISO 9001, ISO 19011 ou auditoria externa.
- O operador avalia os critérios qualitativos.
- A conferência de acessibilidade continua pendente na fase 05.

## 4. Engenharia de software e modelagem — fase 04

### 4.1 Decisão

**Aplicar parcialmente os padrões web e a documentação de arquitetura.**

Fontes: `html-css/WHATWG - HTML Living Standard (EN).html`, `WHATWG - Encoding Living Standard (EN).html` e `WHATWG - URL Living Standard (EN).html`; os módulos CSS da pasta `html-css/`; `html-css/Google - HTML CSS Style Guide (EN).html`; `documentacao-revisao/Daniele Procida - Diataxis (EN).html` e os demais textos de Diátaxis; `documentacao-revisao/MADR - ADR Template (EN) - v4.0.0.md`; `documentacao-revisao/Scott Chacon e Ben Straub - Pro Git (EN) - 2a edicao.pdf`; os guias de revisão do Google; `complementos/rfc5646.txt`.

Não há SWEBOK, arc42 nem C4 na base.
A arquitetura fica em texto, sem diagrama que exija ferramenta ou build.

### 4.2 Arquitetura

**Contexto**

```text
Visitante
  └─ navegador
       ├─ GitHub Pages: HTML, CSS, mídia e ícones
       ├─ links externos: Drive, LinkedIn, projetos e instituições
       └─ DNS e TLS: fornecidos pelo GitHub
```

**Blocos**

| Bloco | Conteúdo | Responsabilidade |
| --- | --- | --- |
| Páginas | 22 arquivos HTML em cinco variantes | Conteúdo, navegação e cópia estruturada. |
| Ativos | `static/assets/css/styles.css`, `static/assets/icons/` e `static/media/` | Estilo, ícones e fotografias. |
| Documentação | `docs/`, plano, requisitos e ADRs | Regras, decisões e evidência. |
| Publicação | `.github/workflows/pages.yml` | Copiar `static/` e publicar no Pages. |

**Implantação**

1. O responsável autoriza a mudança.
2. O commit entra na `main`.
3. O workflow copia `static/` para uma pasta temporária.
4. O GitHub Pages publica a pasta.
5. A página publicada é conferida.

**Decisões transversais:** sem JavaScript, CSS único, cinco variantes, cópia oculta, ícones por máscara, projetos apenas em `pt-BR` e publicação restrita a `static/`.

### 4.3 Registros de decisão

Sete ADRs em [docs/adr/](adr/README.md), no formato MADR 4.0.0.

| ID | Decisão |
| --- | --- |
| [0001](adr/0001-site-estatico-sem-javascript.md) | Site estático sem JavaScript |
| [0002](adr/0002-css-unico-compartilhado.md) | CSS único compartilhado |
| [0003](adr/0003-cinco-variantes-linguisticas.md) | Cinco variantes com base em `pt-BR` |
| [0004](adr/0004-copia-estruturada-oculta.md) | Cópia estruturada oculta |
| [0005](adr/0005-icones-por-mascara-css.md) | Ícones por máscara CSS |
| [0006](adr/0006-projetos-apenas-em-pt-br.md) | Projetos apenas em `pt-BR` |
| [0007](adr/0007-publicacao-restrita-a-static.md) | Publicação restrita a `static/` |

### 4.4 Convenções de HTML e CSS

**HTML**

- UTF-8 e `lang` correto em cada página.
- `hreflang` recíproco entre as variantes.
- Elementos semânticos: `header`, `nav`, `main`, `section`, `footer`.
- Um `h1` por página e hierarquia sem saltos.
- Caminhos relativos.
- Sem `style` embutido, `<script>`, `<form>` ou `<iframe>`.
- Toda imagem tem `alt`; a galeria usa `figure` e `figcaption`.
- A cópia estruturada usa `hidden` e dados iguais aos da tela.

**CSS**

- Um arquivo comum: `static/assets/css/styles.css`.
- Classes descritivas em kebab-case.
- Propriedades customizadas para cores e medidas.
- Media queries por largura, tema e impressão.
- Foco visível, contraste e `prefers-reduced-motion`.
- Sem framework e sem pré-processador.

### 4.5 Documentação com Diátaxis

| Documento | Tipo |
| --- | --- |
| `README.md` da raiz | Como fazer |
| `docs/manutencao.md` | Como fazer |
| `docs/padroes-tecnicos.md` | Explicação |
| `docs/requisitos.md` | Referência |
| `docs/guia-de-redacao.md` | Referência |
| `docs/conteudo-e-fontes.md` | Referência |
| `docs/adr/` | Explicação |
| `PLANO-APLICACAO-PADROES-TECNICOS.md` | Explicação |
| `CHANGELOG.md` | Referência |
| PDFs V3, Europass, ATS, Referências, Tags e Glossário | Referência |
| `docs/organizacao.md` | Explicação |

Não há tutorial: o site é usado, não ensinado.
O índice `docs/README.md` recebeu a coluna de tipo.

### 4.6 Git e revisão

- Uma mudança resolve um assunto.
- A mensagem diz o que mudou e por quê, no imperativo.
- A revisão confere estrutura, links, conteúdo e documentação.
- Mudança grande é dividida antes da revisão.
- Reversão segue a seção 10, com `git revert` em até cinco commits.

### 4.7 Idioma e RFC 5646

Cada página declara `lang` conforme a variante.
Os links `alternate` e `hreflang` apontam para a página correspondente.
`en/` usa `en-US`; `es-419` e `es-ES` mantêm etiquetas distintas.
`x-default` aponta para a raiz.

### 4.8 Verificação

- 22 arquivos HTML, cinco variantes e um redirecionamento.
- Um CSS, 29 ícones e 36 arquivos de mídia.
- Nenhum `<script>`, `<form>`, `<iframe>` ou `style=` embutido.
- Links internos, âncoras e identificadores sem erro.
- Sete ADRs aceitos e indexados.
- `docs/README.md` classificado por tipo.
- `git diff --check` limpo.

### 4.9 Limites

- Não há SWEBOK, arc42 ou C4. A arquitetura é textual e proporcional ao porte.
- Não há validação automática de HTML nem diagrama gerado.
- A conferência de acessibilidade completa continua na fase 05.
- Os ADRs registram decisões vigentes; não são certificação de arquitetura.

## 7. Engenharia de sistemas — fase 07

### 7.1 Decisão

**Aplicar a engenharia de sistemas de forma mínima e textual.**

Fontes: `historico-fas/tg007.htm` (FAS-1654), §2.1 e §2.3; `historico-fas/tg006.htm` (FAS-1653), §7.2 e §9.1.

A contribuição é genérica: documentar as propriedades do sistema, manter o nível de detalhe proporcional ao uso e controlar a linha de base.
Não há SEBoK, INCOSE ou NIST 800-160 na base.
Não há classes de segurança, contexto militar ou declaração de conformidade.

### 7.2 Fronteira e contexto

```text
Visitante
  └─ navegador
       ├─ GitHub Pages: HTML, CSS, ícones e mídia
       ├─ links externos: Drive, LinkedIn, projetos e instituições
       └─ DNS e TLS: GitHub
```

**Dentro da fronteira:** os arquivos de `static/`, o workflow, a documentação e as decisões.
**Fora da fronteira:** navegador, GitHub Pages, DNS, TLS, Google Drive, LinkedIn e sites vinculados.

### 7.3 Interfaces e modos de falha

| Interface | Dono | Troca | Modo de falha | Comportamento esperado |
| --- | --- | --- | --- | --- |
| Navegador e HTML/CSS | Projeto | Página e estilos | HTML ou CSS inválido | Conteúdo legível; correção antes de publicar. |
| Teclado e leitor de tela | Visitante e tecnologia | Estrutura e foco | Nome ou foco ausente | HTML semântico, link de salto e foco visível. |
| Links externos | Terceiros | Clique | 404, timeout ou bloqueio | Link permanece; falha é registrada, sem promessa de disponibilidade. |
| Repositório e GitHub Actions | Responsável e GitHub | Push e workflow | Deploy falha | Versão anterior permanece; conferir a execução e corrigir. |
| GitHub Pages, DNS e TLS | GitHub | HTTPS | Certificado ou DNS indisponível | Erro de HTTPS; não publicar conteúdo misto. |
| Google Drive | Terceiro | Abertura de PDF | Acesso negado | O link não é essencial; o site continua legível. |

### 7.4 Cenários operacionais

| Cenário | Resultado esperado | Verificação |
| --- | --- | --- |
| Abrir a raiz e escolher idioma | A variante escolhida abre. | Teste manual. |
| Abrir o currículo em cada variante | Conteúdo e navegação coerentes. | Teste manual nas cinco pastas. |
| Trocar de idioma | A página correspondente abre; `hreflang` confere. | Inspeção e clique. |
| Imprimir o currículo | Conteúdo visível; menu e cópia oculta ausentes. | Emulação de impressão. |
| Navegar só com teclado | Link de salto e foco funcionam. | Teste manual. |
| Usar leitor de tela | Ordem e nomes compreensíveis. | Não executado; limite da fase 05. |
| Abrir link externo indisponível | O restante da página continua utilizável. | Teste com link inválido. |
| Falhar a publicação | A versão anterior continua no ar. | Conferir a execução do workflow. |
| Tela de 320 CSS px e zoom | Sem rolagem horizontal e sem corte. | Teste manual. |
| Rede indisponível | O site não carrega; não há modo offline. | Limite conhecido. |

### 7.5 Verificação e validação

**Verificação:** confirmar que a página cumpre os requisitos e as convenções.
Inclui inspeção estática, links, HTML, CSS, impressão e conferência pós-publicação.

**Validação:** confirmar que o site atende ao objetivo de apoiar a candidatura a emprego.
Inclui revisão do responsável, clareza do conteúdo e ações esperadas: currículo, projetos e contato.

Cada cenário do §7.4 tem resultado esperado.
A ausência de teste fica registrada como limite, não como aprovação.

### 7.6 Limites

- Sem modelo formal de sistema, sem SEBoK, INCOSE ou NIST 800-160.
- Sem SLA e sem controle sobre a disponibilidade do GitHub, do Drive ou dos sites vinculados.
- Sem ensaio com leitor de tela, dispositivo físico ou falha real de rede.
- A fonte histórica contribui apenas com princípios de documentação e linha de base.

## 10. Mudanças — fase 10

### 10.1 Decisão

**Aplicar parcialmente o controle de configuração e de mudanças.**

Fontes: `historico-fas/tg006.htm` (FAS-1653), §7.2, §9.1 e §9.3; `documentacao-revisao/Scott Chacon e Ben Straub - Pro Git (EN) - 2a edicao.pdf`, capítulo 2 e referência de `git revert`; `documentacao-revisao/Google - Code Review Standard (EN).html`, `Small Change Lists` e `Writing Good Change List Descriptions`; `documentacao-revisao/MADR - ADR Template (EN) - v4.0.0.md`.

A fonte histórica contribui apenas com princípios gerais: avaliar, coordenar, aprovar, manter rastreabilidade e atualizar a documentação afetada.
Não há classes de segurança, obrigações militares nem declaração de conformidade.

Não há Comitê de Controle de Configuração.
O responsável é o único aprovador. O agente prepara a análise e executa a mudança autorizada.

### 10.2 Itens de configuração

| Item | Controle | Linha de base |
| --- | --- | --- |
| `static/` | HTML, CSS, mídia, ícones e favicon | Commit aprovado; publicação somente por push. |
| `.github/workflows/pages.yml` | Publicação | Permissões mínimas e ações por SHA. |
| `docs/` e plano | Regras, requisitos, decisões e evidência | Documento revisado e versionado. |
| `CHANGELOG.md` | Registro resumido das mudanças | Entrada por mudança publicada. |
| `docs/fontes/` e listas de tags | Dados declarados e consulta | Fonte factual preservada. |

A linha de base vigente é o commit aprovado na `main`.
Mudança aprovada atualiza a linha de base. Mudança não aprovada não entra na `main`.

### 10.3 Tipos de mudança e impacto

| Tipo | Exemplos | Impacto a conferir |
| --- | --- | --- |
| Conteúdo | Currículo, competências, projetos, recomendações | Fatos e fontes; cópia estruturada; variantes afetadas; impressão. |
| Visual | CSS, ícones, temas, layout | Teclado, foco, contraste, 320 CSS px, zoom, temas e impressão. |
| Estrutura | Página nova, navegação, seções | Links internos, títulos, menu, `hreflang` e workflow. |
| Publicação | Workflow, permissões, domínio, 404 | Segurança, disponibilidade, cache e retorno. |
| Documentação | Guias, plano, requisitos, ADRs | Índice, coerência e decisões afetadas. |

Toda análise registra: o que muda, por quê, quais páginas e variantes são afetadas, qual risco aumenta e como a mudança será verificada.

### 10.4 Procedimento

1. Registre o pedido, a finalidade e a fonte.
2. Analise o impacto pelo quadro do §10.3.
3. Peça autorização ao responsável antes de alterar conteúdo ou site.
4. Faça uma mudança pequena, com um único propósito.
5. Verifique HTML, links internos e temas. Acrescente as verificações da fase afetada.
6. Use mensagem de commit clara, com o motivo e a fase.
7. Registre no `CHANGELOG` e atualize a situação no plano.
8. Faça o push e confira a página publicada.
9. Registre o resultado e as limitações.

### 10.5 Reversão

A reversão usa `git revert`, que cria um commit com o efeito contrário.
O histórico da `main` não é reescrito.

- Reverta até cinco commits, conforme a decisão D-22.
- Acima de cinco commits, ou em caso de conflito, pare e peça decisão ao responsável.
- Verifique o resultado antes do push.
- Registre o motivo, os commits revertidos e a verificação.

O ensaio usa `git revert --no-commit` seguido de `git revert --abort`, para conferir o mecanismo sem publicar.

### 10.6 Revisão e mensagem

- Uma mudança resolve um assunto.
- Conteúdo e documentação entram em commits separados quando possível.
- A mensagem diz o que mudou e por quê, no imperativo.
- A mensagem cita o requisito ou a fase quando existir.
- Mudança grande é dividida antes da revisão.

### 10.7 Changelog

O `CHANGELOG.md` fica na raiz.
Cada entrada tem data, resumo e evidência.
A entrada mais recente fica no topo.
Não há número de versão inventado. O histórico completo permanece no Git.

### 10.8 Verificação e limites

- A própria fase 10 serve de mudança piloto: pedido, impacto, autorização, verificação, commit e registro.
- O ensaio de reversão foi feito sem publicar.
- Não há comitê, auditoria externa nem fonte local sobre continuidade digital.
- A responsabilidade pela aprovação é do responsável, não do agente.
