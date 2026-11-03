# PLANO DE APLICAÇÃO DOS PADRÕES TÉCNICOS — BASE LOCAL

Data: 2 de novembro de 2026.
Projeto: portfólio estático HTML/CSS em cinco variantes linguísticas.
Registro histórico; movido para `docs/historico/` em 3 de novembro de 2026.
Fonte: `docs/referencias/repertorio-tecnico-site/`, com 41 obras e 74 arquivos.
Este plano usa a base local, com uma exceção registrada na fase 11: o SFIA v9 e o NICE Rev. 1 são consultados na biblioteca principal como referência externa. O SFIA não é copiado para a base por causa da licença.

Este é o registro histórico das 12 fases. A versão enxuta para planejamento futuro está em [Mapa essencial e plano enxuto](historico.md). Ela não foi implementada.

## 1. Premissa

A base local cobre cinco pastas de forma direta, quatro de forma parcial, duas sem fonte e uma com referência externa.

| Situação | Pastas |
| --- | --- |
| Cobertura direta | `01`, `02`, `04`, `05`, `08` |
| Cobertura parcial | `03`, `07`, `09`, `10` |
| Referência externa | `11` |
| Sem fonte local | `06`, `12` |

Quando a pasta não tem fonte local, a fase registra a lacuna. Ela não simula aplicação de norma.

## 2. Cobertura da base por pasta

| Pasta | Fonte local | Cobertura |
| --- | --- | --- |
| `01` Gestão de projetos | PM2 3.1 (PT) | direta |
| `02` Análise de negócios | CPRE 3.3.0; Glossário 2.2.0; Redação e Rastreabilidade | direta |
| `03` Processos e qualidade | ISTQB CTFL 4.0.1 | parcial: teste, sem ISO 9001/19011 |
| `04` Engenharia de software | HTML, Encoding e URL; 15 módulos CSS; CSS 2.1; Google HTML/CSS; Diátaxis; MADR; Pro Git; Code Review; RFC 5646; Media Queries 5; CSS Color Adjust 1 | direta para web e documentação; sem SWEBOK, arc42 ou C4 |
| `05` Normas e redação | STE100 Issue 9; WCAG 2.2 EN/PT; WAI-ARIA 1.2; ARIA in HTML; AccName 1.2 | direta; sem ABNT ou Manual da PR |
| `06` Governança de dados | — | sem fonte |
| `07` Engenharia de sistemas | FAS-1654 §2; FAS-1653 §7/9.1 | mínima e histórica |
| `08` Segurança cibernética | NIST SSDF 800-218 1.1 | parcial; sem ASVS, WSTG ou ISO 27001 |
| `09` Governança, arquitetura e serviços | GitHub Pages (EXT-02); RFC 5646 | mínima; sem FitSM, ISO 20000 ou RFCs HTTP |
| `10` Gestão de mudanças | FAS-1653; Pro Git; Google Code Review e Small Change Lists; MADR | parcial; sem guias EC ou TNA |
| `11` Competências profissionais | SFIA v9 (PT); NICE SP 800-181 Rev. 1 (EN) | referência externa; SFIA licenciado, NICE público |
| `12` Gestão estratégica e governança | — | sem fonte |

## 3. Regras de execução

1. Cada fase cita o arquivo local ou a referência externa registrada.
2. Fonte ausente gera registro de lacuna, não aplicação simulada.
3. Fontes históricas entram só nos pontos permitidos pela base: princípios de documentação e controle de configuração. Não importar classes de segurança, obrigações militares ou alegação de conformidade.
4. Cada fase entrega, no máximo, uma seção em `docs/historico/padroes-tecnicos.md`, uma atualização em guia existente e um ADR quando a decisão for estrutural.
5. Não acrescentar JavaScript, backend, framework ou etapa de build.
6. Mudança de conteúdo ou de site exige aprovação do responsável e verificação nas variantes afetadas.
7. As regras ficam nos documentos versionados. A base local é citada como procedência, não como único registro da regra.
8. O plano não declara conformidade com norma, certificação ou equivalência.

## 4. Fases

### Fase 01 — `01_GESTAO_DE_PROJETOS`

- **Fonte:** `docs/referencias/repertorio-tecnico-site/gestao-requisitos-testes/Comissao Europeia - PM2 Metodologia de Gestao de Projetos (PT) - v3.1.pdf`.
- **Aplicar:** ficha do projeto com escopo, interessados, entregas, critérios de aceite, marcos e riscos iniciais. Tailoring do PM2 proporcional ao porte. Gates deste plano.
- **Verificar:** ficha aprovada. Cada fase com responsável, data e critério de saída.
- **Saída:** seção “Gestão” em `docs/historico/padroes-tecnicos.md`.
- **Esforço:** P.

### Fase 02 — `02_ANALISE_DE_NEGOCIOS`

- **Fontes:** CPRE 3.3.0, Glossário 2.2.0 e Redação e Rastreabilidade de Requisitos.
- **Aplicar:** catálogo de requisitos funcionais e não funcionais com ID, fonte, critério de aceite e método de verificação. Glossário do site. Matriz requisito → fonte → verificação → fase. Usar as características de qualidade do CPRE: clareza, completude, consistência, verificabilidade e rastreabilidade.
- **Verificar:** requisito único e testável. Nenhum órfão. Termo do glossário com fonte.
- **Saída:** `docs/requisitos.md` e seção correspondente.
- **Esforço:** M.

### Fase 03 — `03_GESTAO_DE_PROCESSOS_E_QUALIDADE`

- **Fonte:** ISTQB CTFL 4.0.1.
- **Aplicar:** processo de teste com planejamento, análise, desenho, implementação, execução e encerramento. Abordagem baseada em risco. Níveis adaptados ao site: inspeção estática, ensaio em navegador, revisão de conteúdo e conferência pós-publicação. Relatório de defeito e Definition of Done.
- **Limite:** a base não tem ISO 9001 ou ISO 19011. Não chamar o resultado de sistema de gestão da qualidade.
- **Verificar:** aplicar a uma mudança real. Registrar defeito e correção.
- **Saída:** atualização de `docs/manutencao.md` e seção.
- **Esforço:** M.

### Fase 04 — `04_ENGENHARIA_DE_SOFTWARE_E_MODELAGEM`

- **Fontes:** HTML Living Standard, Encoding e URL; módulos CSS e CSS 2.1; Google HTML/CSS; Diátaxis; MADR; Pro Git; Code Review; RFC 5646; Media Queries 5; CSS Color Adjust 1.
- **Aplicar:**
  - ADRs com MADR para as decisões vigentes: site estático sem JavaScript, CSS único, cinco variantes, cópias ocultas, ícones por máscara, projetos em pt-BR separados e publicação restrita a `static/`.
  - Arquitetura em texto com contexto, blocos, implantação e decisões transversais. Sem C4 ou arc42 formais.
  - Convenções HTML/CSS: semântica, hierarquia de títulos, caminhos relativos, fontes do sistema, ausência de estilo embutido, nomenclatura, cascata e impressão.
  - Diátaxis: classificar os guias existentes e ajustar `docs/README.md`.
  - Git e revisão: mudanças pequenas, mensagem, checklist e reversão.
  - RFC 5646: conferir `lang` e `hreflang`.
- **Verificar:** árvore real × documento. Estrutura HTML, CSS e links internos. Um ADR por decisão. Uma mudança revisada pelo checklist.
- **Saída:** `docs/decisoes.md`, seção e atualização de `docs/manutencao.md`.
- **Esforço:** G.

### Fase 05 — `05_NORMAS_E_REDACAO_TECNICA`

- **Fontes:** STE100 Issue 9; WCAG 2.2 EN/PT; WAI-ARIA 1.2; ARIA in HTML; AccName 1.2.
- **Aplicar:** auditoria editorial nas cinco variantes com um termo por conceito, voz ativa, revisão de frases longas e inglês norte-americano. Corrigir só texto autoral. Checklist WCAG 2.2 AA por tipo de página. Conferir nomes acessíveis, foco, teclado, contraste, 320 CSS px, zoom, temas, impressão e uso mínimo de ARIA.
- **Limite:** a base não tem ABNT nem Manual de Redação da Presidência da República. Não citar essas normas.
- **Verificar:** ensaio manual em navegador. Registrar evidência e limites. Nenhuma declaração de conformidade.
- **Saída:** atualização de `docs/guia-de-redacao.md` e `docs/manutencao.md`, seção e backlog de correções.
- **Esforço:** G.

### Fase 06 — `06_GOVERNANCA_DE_DADOS`

- **Fonte:** nenhuma na base.
- **Aplicar:** não aplicar norma. Registrar a lacuna. Produzir apenas inventário factual: dados publicados (nome, contato, país, formação, experiências e fotos), terceiros (GitHub Pages, Drive e links externos) e confirmação de ausência de cookies, scripts e formulários.
- **Verificar:** inventário completo e varredura estática. Nenhuma alegação de LGPD ou ANPD.
- **Saída:** seção “Lacuna — dados pessoais”.
- **Esforço:** P.

### Fase 07 — `07_ENGENHARIA_DE_SISTEMAS`

- **Fontes:** FAS-1654 §2, princípios de documentação; FAS-1653 §7/9.1, controle de configuração e baseline.
- **Aplicar:** princípios de documentação para os guias do projeto. Linha de base de configuração com os arquivos controlados, a forma de versionamento e o registro de mudanças.
- **Limite:** sem SEBoK, INCOSE ou NIST 800-160. Não importar contexto militar nem classes de segurança.
- **Verificar:** lista de itens de configuração. Guias alinhados aos princípios.
- **Saída:** seção e lista de linha de base.
- **Esforço:** P.

### Fase 08 — `08_SEGURANCA_CIBERNETICA`

- **Fonte:** NIST SSDF 800-218 1.1.
- **Aplicar:** práticas do SSDF adaptadas ao site estático:
  - preparar a organização: proteger conta e repositório;
  - proteger o software: revisão, ausência de segredos e integridade dos SVGs;
  - produzir software seguro;
  - responder a vulnerabilidades: despublicar, reverter, corrigir e registrar.
- **Limite:** sem ASVS, WSTG ou ISO 27001. Não declarar verificação de aplicação.
- **Verificar:** checklist de configuração do repositório com o responsável. Permissões do workflow. Ausência de segredos. Inventário dos ativos.
- **Saída:** seção e checklist.
- **Esforço:** M.

### Fase 09 — `09_GOVERNANCA_ARQUITETURA_E_SERVICOS_DE_TI`

- **Fontes:** `docs/referencias/repertorio-tecnico-site/complementos/github-pages.html` (EXT-02) e RFC 5646.
- **Aplicar:** conferir a publicação com origem em GitHub Actions, permissões mínimas e envio apenas de `static/`. Conferir HTTPS, 404, roteamento de idiomas e atributos `lang` e `hreflang`.
- **Limite:** sem FitSM, ISO 20000 ou RFCs HTTP. Não criar catálogo de serviços nem SLA.
- **Verificar:** workflow, status e cabeçalhos no publicado, troca de idioma e 404.
- **Saída:** atualização de `README.md` e `docs/manutencao.md`, com seção.
- **Esforço:** P.

### Fase 10 — `10_GESTAO_DE_MUDANCAS`

- **Fontes:** FAS-1653; Pro Git; Google Code Review e Small Change Lists; MADR.
- **Aplicar:** controle de mudança com itens de configuração, linha de base, pedido, análise de impacto, aprovação do responsável, reversão com `git revert` e registro. Revisão por mudanças pequenas e descrição clara.
- **Limite:** sem guias EC ou TNA. Não tratar continuidade digital como coberta.
- **Verificar:** aplicar a uma mudança piloto. Rollback ensaiado em branch local. Registro completo.
- **Saída:** atualização de `docs/manutencao.md` e seção.
- **Esforço:** P.

### Fase 11 — `11_COMPETENCIAS_PROFISSIONAIS`

- **Fontes:** SFIA v9 (Referência da Estrutura e Sobre o SFIA, PT) e NICE SP 800-181 Rev. 1 (EN), na biblioteca principal.
- **Aplicar:** usar SFIA e NICE como referência de vocabulário e organização, sem certificação. Registrar o que são, a utilidade e as regras de aplicação. Publicar um perfil piloto de sete habilidades com níveis 2 e 3, como autoavaliação, após aprovação. Não publicar níveis 4 a 7, work roles ou selos sem evidência e aprovação.
- **Limite:** SFIA é licenciado; o PDF não é copiado para a base. O NICE Rev. 1 não traz o catálogo completo de tarefas e work roles. Não criar níveis ou certificações.
- **Verificar:** cada nível cita a habilidade e a evidência; nenhum nível 4 a 7 publicado; terminologia revisada contra `dados-pessoais/fontes/competencias-declaradas.json`.
- **Saída:** `docs/competencias.md`, bloco em `static/pt-BR/index.html` e seção.
- **Esforço:** M.

### Fase 12 — `12_GESTAO_ESTRATEGICA_E_GOVERNANCA`

- **Fonte:** nenhuma na base.
- **Aplicar:** não aplicar norma. Registrar a lacuna. Opcionalmente, listar riscos já conhecidos do projeto como prática de gestão: exposição de dados, conteúdo desatualizado, links quebrados, perda de conta ou repositório e regressão de acessibilidade. Não apresentar como ISO 31000 ou modelo TCU.
- **Verificar:** riscos com dono e mitigação. Data de revisão.
- **Saída:** seção “Lacuna — riscos”.
- **Esforço:** P.

## 5. Ordem e marcos

| Ordem | Fase | Motivo |
| --- | --- | --- |
| 1 | 01 | define escopo e gates |
| 2 | 02 | base para qualidade e testes |
| 3 | 10 | procedimento usado pelas demais fases |
| 4 | 03 | processo de teste e Definition of Done |
| 5 | 04 | ADRs, arquitetura e convenções |
| 6 | 07 | princípios de documentação e linha de base |
| 7 | 05 | redação e acessibilidade |
| 8 | 08 | segurança do desenvolvimento |
| 9 | 09 | publicação e idiomas |
| 10 | 06 | lacuna e inventário de dados |
| 11 | 11 | lacuna e terminologia |
| 12 | 12 | lacuna e riscos |

Marcos:

- **M1 — Processo:** fases 01, 02, 10 e 03.
- **M2 — Produto documentado:** fases 04, 07 e 05.
- **M3 — Publicação e segurança:** fases 08 e 09.
- **M4 — Lacunas:** fases 06, 11 e 12.

Esforço total estimado: cerca de 15 sessões. As fases 04, 05 e 11 concentram o trabalho.

## 6. Situação das fases

| Fase | Situação | Evidência |
| --- | --- | --- |
| 01 | Concluída — aceita em 02/11/2026 | `docs/historico/padroes-tecnicos.md` §1 |
| 02 | Concluída — aceita em 02/11/2026 | `docs/requisitos.md`; `docs/historico/padroes-tecnicos.md` §2 |
| 03 | Executada — processo e piloto D-001 | `docs/historico/padroes-tecnicos.md` §3 |
| 04 | Executada — ADRs, arquitetura e convenções | `docs/decisoes.md`; `docs/historico/padroes-tecnicos.md` §4 |
| 05 | Executada — auditoria e correções A11Y-01, A11Y-02 e EDIT-02 | `docs/historico/padroes-tecnicos.md` §5; `static/assets/css/styles.css` |
| 06 | Executada — lacuna e inventário de dados | `docs/historico/padroes-tecnicos.md` §6 |
| 07 | Executada — fronteira, interfaces e cenários | `docs/historico/padroes-tecnicos.md` §7 |
| 08 | Executada — modelo de ameaças, controles e licença | `docs/historico/padroes-tecnicos.md` §8; `static/assets/icons/LICENSE.txt` |
| 09 | Executada — serviço, HTTPS e página 404 | `docs/historico/padroes-tecnicos.md` §9; `static/404.html` |
| 10 | Executada — procedimento e CHANGELOG | `docs/historico/padroes-tecnicos.md` §10; `CHANGELOG.md` |
| 11 | Executada — SFIA e NICE documentados | `docs/competencias.md`; `docs/historico/padroes-tecnicos.md` §11 |
| 12 | Executada — linha de base de governança | `docs/historico/padroes-tecnicos.md` §12 |

Atualize a situação e a evidência ao concluir cada fase. Não registre aprovação do responsável sem confirmação dele.

## 7. O que este plano não faz

- Não amplia a base, não copia fonte nova e não consulta o acervo principal.
- Não aplica ABNT, LGPD ou ANPD, ISO 9001 ou 19011, ASVS ou WSTG, FitSM ou ISO 20000, SFIA ou NICE, ISO 31000.
- Não declara conformidade. Não transforma fonte histórica em obrigação atual.
- Não altera o site sem aprovação. Correções de acessibilidade e conteúdo viram backlog quando necessário.
- Não cria JavaScript, backend, framework ou etapa de build.

## 8. Decisões e pendências

Decisões recebidas em 02/11/2026:

- ficha da fase 01 aceita;
- formalização iniciada em 28/10/2026;
- fases 06, 11 e 12 registram lacuna e inventário factual mínimo;
- fases 05 e 09 corrigem apenas itens objetivos e reversíveis, com aprovação item a item;
- Git: commit e push autorizados, branch `main`, `CHANGELOG` na fase 10;
- parada apenas para decisão ambígua ou mudança de site/conteúdo;
- escopo inicial em pt-BR; expansão de idiomas e novas funcionalidades ficam para depois;
- sem limite quantitativo de desempenho;
- sem aviso de privacidade; dados publicados mantidos como estão;
- botão de download do currículo permanece inativo;
- 2FA em ativação;
- alterações na `main` exigem autorização do responsável;
- página 404 e `CHANGELOG` aprovados para as fases 09 e 10;
- catálogo de requisitos aceito em 02/11/2026;
- critérios qualitativos avaliados pelo operador;
- fase 11 usa SFIA v9 e NICE Rev. 1 como referência externa; o SFIA não é copiado por licença.

Pendências resolvidas em 02/11/2026:

1. Q4: reverter até cinco commits.
2. R1–R3: público principal são recrutadores e gestores de contratação; objetivo é emprego; ações são currículo, projetos e contato.
3. C1–C2: manter a voz atual; ajustes são apenas apontados, sem reescrita.
4. P6: publicação aprovada.
5. P5: ordem das fases confirmada; estimativa revista para cerca de 15 sessões na fase 11.
6. S2: apenas o responsável é administrador; alterações na `main` exigem sua autorização.

Pendência operacional: conferir a proteção técnica da `main` na fase 08.

## 9. Critério de conclusão

O plano termina quando:

- as 12 seções estiverem preenchidas em `docs/historico/padroes-tecnicos.md`;
- cada fase tiver decisão registrada: aplicada, parcial, não aplicável ou lacuna;
- as fontes citadas estiverem disponíveis na base local ou na referência externa registrada;
- as mudanças de documentação passarem em `git diff --check`;
- o responsável revisar o resultado e as decisões pendentes.

Situação em 02/11/2026: as doze seções estão preenchidas.
O encerramento depende do aceite do responsável e das pendências da seção 12.6.

As verificações de navegador, teclado, contraste, zoom, temas e impressão registram evidência e limites. Elas não substituem ensaio manual nem validação externa.
