# Histórico de mudanças

Registra as mudanças publicadas no site e nos documentos.
A entrada mais recente fica no topo.
O histórico completo está no Git.
As datas usam o formato AAAA-MM-DD.

| Data | Mudança | Evidência |
| --- | --- | --- |
| 2026-11-12 | Condensa as quatro atividades de Aquecedores e Piscinas Mairiporã de 591 para 525 caracteres (−11,2%), sem retirar fato, na tela, na cópia oculta e na lista de consulta. Mantém os quatro parágrafos e o texto visível. | Este commit; [conteúdo e fontes](docs/conteudo-e-fontes.md). |
| 2026-11-12 | Remove o vínculo empregatício das cinco experiências de `pt-BR` e da experiência da RealFort em `en`, na tela, na cópia oculta e na lista de consulta. Encurta o cargo em Aquecedores e Piscinas Mairiporã para "Gestor de tráfego pago", mantendo as demais atividades. | Este commit; [conteúdo e fontes](docs/conteudo-e-fontes.md); P-17. |
| 2026-11-11 | Reestrutura as competências de `pt-BR` e `en` com âncoras e detalhe expansível: subcategorias com 9 ou mais tags mostram quatro âncoras e um `details` fechado com as demais, aberto por `[ver mais]`. Reduz a tela inicial de `pt-BR` de 165 para 76 tags visíveis. Mantém a cópia oculta, a lista de tags e os cartões de projeto. | Este commit; [decisões](docs/decisoes.md), 0009; FR-10. |
| 2026-11-11 | Registra a Portugal Digital Solutions como projeto empresarial em abertura em `pt-BR` e `en`: consultoria digital para PME em Portugal, com posicionamento, ofertas previstas e limites da fonte. Atualiza a apresentação, a meta descrição, o cartão de `en` e a lista de consulta. Mantém a empresa fora de Experiência até a constituição (P-18). | Este commit; [conteúdo e fontes](docs/conteudo-e-fontes.md); P-18. |
| 2026-11-06 | Fecha a P-17: confirma vínculos e locais das cinco experiências e exibe Aquecedores (prestação de serviços, Mairiporã), RealFort (São Paulo), Lukos (CLT) e Alpha (CLT) na ficha e na cópia estruturada de `pt-BR`. Documenta o padrão de HTML em Manutenção e no índice de documentação. | Este commit; P-17. |
| 2026-11-06 | Padroniza a seção Experiência de `pt-BR` em fichas `<dl class="experience-meta">` com ordem fixa de campos, exibe o período da RealFort Sistemas (28/08/2026 a 28/09/2026) e alinha a cópia estruturada. Cria o [Padrão de HTML](docs/padrao-html.md) e os modelos de `docs/modelos/`. Registra a P-17 para os vínculos e locais sem fonte. | Este commit; P-17. |
| 2026-11-06 | Inclui o Currículo Lattes nos contatos de `pt-BR` e `en`, com o endereço curto canônico e sem o token de sessão. | Este commit; [conteúdo e fontes](docs/conteudo-e-fontes.md). |
| 2026-11-06 | Troca a seção Sobre por Perfil em `pt-BR`: remove a lista de empregos e a frase de apresentação, mantém os valores e inclui três atalhos para Experiência, Competências e Formação. Atualiza o menu e a cópia estruturada. Registra a pendência de sincronizar `en`. | Este commit; P-16. |
| 2026-11-05 | Cria a documentação formal com o índice, a arquitetura e os processos do projeto. | [Índice](docs/documentacao-formal/README.md); [arquitetura](docs/documentacao-formal/arquitetura.md); [processos](docs/documentacao-formal/processos.md). |
| 2026-11-04 | Cria o currículo geral V4 em pt-BR: PDF de uma coluna com duas páginas, cinco experiências, 17 cursos e três projetos, mais dois rascunhos DOCX em revisão. O manifesto registra tamanho, hash e conferência do PDF. | [Pasta V4](docs/curriculos/v4/README.md). |
| 2026-11-03 | Detalha a lista de países: a CNH liga aos acordos de trânsito com o Brasil e a PID à lista de Estados-partes da Convenção de Viena, em `pt-BR` e `en`. | Este commit. |
| 2026-11-03 | Remove a afirmação de aceitação da PID na Convenção de Viena e mantém apenas o link para a lista de países em `pt-BR` e `en`. | Este commit. |
| 2026-11-03 | Corrige o período da experiência na JH Eletrônico para julho de 2022 a janeiro de 2023 em `pt-BR`, nas fontes e na lista de consulta; atualiza o relatório local para a versão 1.2. | Este commit. |
| 2026-11-03 | Inclui a experiência de assistente de e-commerce na JH Eletrônico (julho de 2021 a janeiro de 2022, autônomo) em `pt-BR`, com as tags de comércio eletrônico e vendas, a cópia estruturada e a lista de consulta. | Este commit. |
| 2026-11-03 | Publica somente `pt-BR` e `en`; redireciona `pt-PT`, `es-419` e `es-ES` para `wip.html`; corrige os caminhos da página 404; padroniza as datas de cursos em `en`; cita a lista oficial de países da Convenção de Viena; registra a pendência de CI. | Este commit. |
| 2026-11-03 | Registra a linha de base de 02/11 (`75d5651`) e revisa os níveis SFIA: `HSIN` e `NTAS` no nível 2. | Este commit. |
| 2026-11-03 | Corrige manifestos, funde o guia de redação em Manutenção e resume o registro das 12 fases. | `8dd903f` |
| 2026-11-03 | Consolida as listas de tags em `docs/listas-de-tags/` e remove a coluna Fase dos requisitos. | `7a096cb` |
| 2026-11-03 | Arquiva a base técnica de 67 MB e mantém catálogo e índice. | `89892e1` |
| 2026-11-03 | Unifica referências e repertório técnico em `docs/referencias/`. | `8ad499c` |
| 2026-11-03 | Move `docs/fontes/` para `dados-pessoais/fontes/` e funde os manifestos em um único arquivo. | `9372ba9` |
| 2026-11-03 | Consolida dados e documentos: arquiva capturas, remove cópias e funde históricos, decisões, referências e pendências. | `56d6393` |
| 2026-11-03 | Remove a cópia anterior e descontinuada do relatório de Aquecedores. | `14d76e5` |
| 2026-11-03 | Remove textos e a metodologia da página principal pt-BR. | `316da4b` |
| 2026-11-03 | Deixa a seção Perfil SFIA fechada por padrão e adiciona cópia de impressão. | `64d8e39` |
| 2026-11-03 | Torna a seção Perfil SFIA colapsável, aberta por padrão. | `55ddd21` |
| 2026-11-02 | Troca CFMG por CHMG no perfil SFIA publicado. | `75d5651` |
| 2026-11-02 | Adiciona visualização colapsável com metodologia e habilidades não publicadas ao perfil SFIA. | `b1b094d` |
| 2026-11-02 | Publica o perfil SFIA em pt-BR e registra a rubrica interna (COA A+B). | `7a879ff` |
| 2026-11-02 | Registra viabilidade e COAs para publicar o SFIA; cópia privada em `docs/referencias/sfia-local/`. | `ca9ca0a` |
| 2026-11-02 | Reorganiza a documentação: pendências únicas, histórico separado e remoção de duplicidade. | `ad0ae8e` |
| 2026-11-02 | Registra o mapa essencial e o plano enxuto, sem reimplementação. | `35c264d` |
| 2026-11-02 | Governança estratégica, indicadores e riscos (fase 12). | `ad2b01a` |
| 2026-11-02 | Competências: SFIA e NICE documentados, com regras de aplicação (fase 11). | `f71c9f3` |
| 2026-11-02 | Governança de dados: lacuna e inventário factual (fase 06). | `4453a80` |
| 2026-11-02 | Serviço, HTTPS, página 404 e verificação de publicação (fase 09). | `8d767c3` |
| 2026-11-02 | Segurança: modelo de ameaças, controles e licença dos ícones (fase 08). | `226f76e` |
| 2026-11-02 | Correções de acessibilidade e revisão editorial: botão desativado, `aria-current="page"` e RDBMS. | `9053f2f` |
| 2026-11-02 | Auditoria editorial e de acessibilidade, com backlog (fase 05). | `d3fa16a` |
| 2026-11-02 | Fronteira, interfaces e cenários de sistema (fase 07). | `41c8f88` |
| 2026-11-02 | Decisões de arquitetura, convenções e classificação Diátaxis (fase 04). | `187baf0` |
| 2026-11-02 | Processo de qualidade, Definition of Done e registro de defeito (fase 03). | `0174749` |
| 2026-11-02 | Aceite do catálogo de requisitos (fase 02). | `90c7e8a` |
| 2026-11-02 | Procedimento de mudanças e criação deste histórico (fase 10). | `e4d2535` |
| 2026-11-02 | Ajustes nos requisitos e nas decisões do responsável. | `caa78a4` |
| 2026-11-02 | Requisitos do site e seção da fase 02. | `b391701` |
| 2026-11-02 | Ficha do projeto, riscos e decisões da fase 01. | `1135ea1` |
| 2026-11-02 | Competências e tags em pt-BR, incluindo variações para ATS. | `182dab9` |
| 2026-11-02 | Correção do início da atuação em tráfego pago para janeiro de 2026. | `8156be8` |

Mudanças anteriores a 02/11/2026 permanecem apenas no histórico do Git.
