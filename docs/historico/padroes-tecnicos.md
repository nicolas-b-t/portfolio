# Padrões técnicos aplicados ao portfólio

Resumo do registro das 12 fases, revisado em 03/11/2026.
O texto integral de 61 KB foi arquivado em `_arquivo/site-curriculo-portfolio/2026-11-03/padroes-tecnicos-integral.md` e permanece no histórico Git.
As regras vivas estão em [Manutenção](../manutencao.md) e [Requisitos](../requisitos.md).
As citações de `docs/referencias/repertorio-tecnico-site/` referem-se à base arquivada em `_arquivo/site-curriculo-portfolio/2026-11-03/repertorio-tecnico-site/`.

Cada seção registra a decisão, o resultado e o limite da fase.
Nenhuma fase declara conformidade, certificação ou equivalência com norma.

## 1. Gestão — fase 01

**Decisão:** aplicar parcialmente o PM2 3.1.
Mantidos ficha do projeto, partes interessadas, plano de trabalho, riscos, decisões e portas de fase.
Dispensados caso de negócio, manual do projeto, externalização, transição e comitê diretivo.
O responsável acumula as funções de decisão; o agente exerce PM e PCT.

**Resultado:** ficha aceita em 02/11/2026; 13 riscos com dono e resposta.

**Limite:** sem PMO, equipe, prazo, custo ou declaração de conformidade.

## 2. Requisitos — fase 02

**Decisão:** aplicar o CPRE 3.3.0 de forma parcial.

**Resultado:** catálogo com 15 requisitos funcionais e 11 não funcionais, glossário de 11 termos, priorização e matriz de rastreabilidade; aceito em 02/11/2026.

**Limite:** sem elicitação com usuários externos, ferramenta de requisitos ou conformidade com o CPRE.

## 3. Processos e qualidade — fase 03

**Decisão:** aplicar o ISTQB CTFL 4.0.1 de forma parcial.
Foram adotados processo de teste, níveis adaptados, abordagem por risco, Definition of Done e registro de defeito.

**Resultado:** o piloto D-001 corrigiu a numeração da seção de mudanças; `git diff --check` limpo.

**Limite:** sem suíte automatizada, equipe independente, ISO 9001, ISO 19011 ou auditoria externa.

## 4. Engenharia de software e modelagem — fase 04

**Decisão:** aplicar os padrões web e a documentação de arquitetura: HTML Living Standard, CSS, Diátaxis, MADR e Git.

**Resultado:** arquitetura textual em quatro blocos, sete ADRs em [Decisões](../decisoes.md) e convenções de HTML e CSS.
O site tem 23 arquivos HTML, um CSS, 28 ícones e 36 arquivos de mídia.

**Limite:** sem SWEBOK, arc42, C4, diagrama gerado ou validação automática de HTML.

## 5. Normas e redação técnica — fase 05

**Decisão:** aplicar parcialmente a redação técnica (ASD-STE100, edição 9) e a acessibilidade (WCAG 2.2, WAI-ARIA e ARIA in HTML).

**Resultado:** auditoria editorial e de acessibilidade.
A11Y-01, A11Y-02 e EDIT-02 foram aplicados; EDIT-01 e EDIT-03 aguardam decisão.

**Limite:** zoom, tema escuro visual, impressão e leitor de tela não testados; sem validação externa.

## 6. Governança de dados — fase 06

**Decisão:** não aplicar norma; registrar a lacuna e o inventário factual mínimo.

**Resultado:** inventário dos dados publicados e dos terceiros.
Os dados publicados foram mantidos e não há aviso de privacidade, conforme D-12.

**Limite:** sem LGPD, jurisdição definida, retenção, canal formal de remoção ou análise jurídica.

## 7. Engenharia de sistemas — fase 07

**Decisão:** aplicar a engenharia de sistemas de forma mínima e textual, com base no FAS-1654 e no FAS-1653.

**Resultado:** fronteira, interfaces, modos de falha, cenários operacionais e critérios de verificação e validação.

**Limite:** sem SEBoK, INCOSE, NIST 800-160, SLA ou ensaio de falha real.

## 8. Segurança cibernética — fase 08

**Decisão:** aplicar o NIST SSDF 800-218 1.1 de forma parcial.

**Resultado:** modelo de ameaças, controles, checklist e plano de incidente simulado em mesa.

**Limite:** 2FA e proteção da `main` pendentes; sem teste de intrusão, análise de dependências ou auditoria externa.

## 9. Governança, arquitetura e serviços de TI — fase 09

**Decisão:** aplicar a governança de serviço de forma mínima, com GitHub Pages e RFC 5646.

**Resultado:** serviço descrito; URL, HTTPS 301, HSTS de um ano, cache de 600 segundos, página 404 e cinco rotas de idioma conferidos.

**Limite:** sem SLA, monitoramento contínuo, domínio próprio ou controle de servidor.

## 10. Mudanças — fase 10

**Decisão:** aplicar parcialmente o controle de configuração e de mudanças, com base no FAS-1653, no Pro Git, na revisão do Google e no MADR.

**Resultado:** itens de configuração, tipos de mudança, procedimento e reversão com `git revert` em até cinco commits, conforme D-22.

**Limite:** sem comitê de configuração, auditoria externa ou aprovador diferente do responsável.

## 11. Competências profissionais — fase 11

**Decisão:** usar o SFIA v9 e o NICE Rev. 1 como referências externas, não como certificação.

**Resultado:** sete habilidades SFIA publicadas em pt-BR, com níveis 2 e 3; `CFMG` e `DATM` ficaram fora do piloto; nenhum work role NICE foi atribuído.

**Limite:** sem avaliação certificada; o PDF do NICE não contém o catálogo completo; os níveis foram revisados em 03/11/2026.

## 12. Governança estratégica e riscos — fase 12

**Decisão:** não aplicar ISO 31000 ou modelo do TCU; registrar a lacuna e a linha de base.

**Resultado:** objetivos, indicadores e riscos consolidados; revisão mínima anual em 02/11/2027.

**Limite:** sem monitoramento contínuo, painel, SLA ou avaliação independente.

## 13. Decisões registradas

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
| D-18 | Competências vêm de `dados-pessoais/fontes/competencias-declaradas.json`; certificações concluídas entram manualmente; ajustes são apenas apontados. |
| D-19 | Revisão conforme evento novo; indicadores manuais neste escopo. |
| D-20 | Inglês revisado pelo responsável; espanhol mantém a diferença entre `es-419` e `es-ES`; inconsistências vão ao operador. |
| D-21 | Documentação em pt-BR; o plano fica na raiz e será versionado. |
| D-22 | Reversão: reverter até cinco commits. |
| D-23 | Público principal: recrutadores e gestores de contratação. Objetivo: emprego. Ações: currículo, projetos e contato. |
| D-24 | Manter a voz atual; ajustes de texto são apenas apontados, sem reescrita sem aprovação. |
| D-25 | Ordem das fases e estimativa de cerca de 14 sessões confirmadas. Superada por D-35. |
| D-26 | Apenas o responsável é administrador. Alterações na `main` exigem sua autorização; a proteção técnica será conferida na fase 08. |
| D-27 | O botão de download do currículo permanece visível e inativo até a publicação do PDF. |
| D-28 | O 2FA está em ativação; revisar na fase 08. |
| D-29 | A página 404 e o `CHANGELOG` estão aprovados; foram criados em 02/11/2026. |
| D-30 | O catálogo de requisitos foi aceito em 02/11/2026; não há novos requisitos no momento. |
| D-31 | Critérios qualitativos são avaliados pelo operador, com registro da decisão. |
| D-32 | A fase 11 usa SFIA v9 e NICE Rev. 1 como referência externa. |
| D-33 | O SFIA não é copiado para a base local por causa da licença; o NICE é público. |
| D-34 | Nenhum nível SFIA ou work role NICE será publicado sem evidência e aprovação. |
| D-35 | Estimativa revista para cerca de 15 sessões com a fase 11 em esforço M. |
| D-36 | Revisão mínima anual em 02/11/2027; revisão por evento quando houver dado novo. |
| D-37 | O plano de 12 fases permanece como registro; o mapa essencial e o plano enxuto foram registrados em [Histórico](historico.md) e não serão implementados. |
| D-38 | Linha de base de 02/11/2026 aceita: commit `75d5651`, abrangendo plano, requisitos, decisões e guias. |
| D-39 | Revisão dos níveis SFIA: `HSIN` e `NTAS` rebaixados para o nível 2; os demais mantidos. Evidências preservadas. |

## 14. Medições de 02/11/2026

| Indicador | Linha de base |
| --- | --- |
| Links internos quebrados | 0 |
| Páginas com um `h1` | 23 de 23 |
| Imagens com `alt` | 45 de 45 |
| Itens de acessibilidade com evidência | 12 de 16 |
| Variantes publicadas | 5; `pt-BR` com 5 páginas e as demais com 4 |
| Destinos externos únicos | 31 |
| `static/` | 95 arquivos; 3,65 MiB |
| Maior imagem | 345 KB |
| Segredos e arquivos privados rastreados | 0 e 0 |
| Publicação | raiz 200; HTTP 301; 404 |
| Documentação | 7 ADRs; 26 requisitos; 12 seções |
| Riscos com dono | 13 de 13 |

Nenhum indicador foi criado sem medição.
O peso é informativo, não uma meta de desempenho.

## 15. Regras e limites

- Nenhuma seção declara conformidade, certificação ou equivalência com norma.
- As decisões D-01 a D-37 continuam válidas enquanto não forem superadas.
- As citações da base local usam o caminho anterior ao arquivamento; o conteúdo está em `_arquivo/`.
- O inventário de dados, o modelo de ameaças e o plano de incidente completos estão no texto integral.
- A lista vigente de pendências está em [Requisitos](../requisitos.md), §11.
