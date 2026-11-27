# Decisões de arquitetura

Decisões registradas desde 02/11/2026.
O formato é uma síntese de MADR; o texto completo de cada ADR permanece no histórico Git.
Uma decisão nova recebe o próximo número. Uma decisão substituída mantém o registro e recebe o status `superseded`.

| ID | Decisão | Status |
| --- | --- | --- |
| 0001 | Site estático sem JavaScript | Aceita |
| 0002 | CSS único compartilhado | Aceita |
| 0003 | Cinco variantes com base em `pt-BR` | Aceita |
| 0004 | Cópia estruturada oculta | Aceita |
| 0005 | Ícones por máscara CSS | Aceita |
| 0006 | Projetos apenas em `pt-BR` | superseded |
| 0007 | Publicação restrita a `static/` | Aceita |
| 0008 | Publicação temporária de duas variantes | Aceita |
| 0009 | Competências com âncoras e detalhe expansível | Aceita |
| 0010 | Home de `pt-BR` em painel de atalhos | Aceita |
| 0011 | Comparação da home de `pt-BR` em duas versões | superseded |
| 0012 *(duplicado histórico)* | Painel como home oficial somente em `pt-BR` | Aceita |
| 0012 | Gestão de projetos como subcategoria própria | Aceita |
| 0013 | Finanças e ferramentas Microsoft como subcategorias | Aceita |
| 0014 | Páginas experimentais de Projetos e Agradecimentos | Aceita |
| 0015 | Projetos e publicações nas duas variantes ativas | Aceita |
| 0016 | Arquivo de currículos legados e nomeação de novas edições | Aceita |
| 0017 | Nova rodada de prévias da home e de Projetos (promovida em `pt-BR` e `en`) | Aceita |
| 0018 | Guia público de documentação do portfólio | Aceita |
| 0019 | Correspondência de tarefas NICE abaixo do SFIA | Aceita |
| 0020 | Menu centralizado de páginas experimentais e visão experimental de portfólio | Aceita |
| 0021 | Unificação de documentação técnica ao portfólio experimental, criação do plano de carreira experimental e aposentadoria das prévias promovidas | Aceita |
| 0022 | Seis propostas experimentais de estética e organização | Aceita para avaliação |

## 0001 — Site estático sem JavaScript

**Contexto:** currículo, projetos, galeria e recomendações em cinco variantes, sem login, formulário ou dado de entrada.
**Decisão:** HTML e CSS estáticos; sem JavaScript, formulário, iframe ou rastreador.
**Consequências:** páginas rápidas, previsíveis e auditáveis; publicação direta de `static/`; sem interatividade, formulário ou analytics.
**Confirmação:** nenhum `<script>`, `<form>` ou `<iframe>` nas 23 páginas; workflow sem etapa de build.

## 0002 — CSS único compartilhado

**Contexto:** as cinco variantes usam a mesma identidade e estrutura; não há framework nem pré-processador.
**Decisão:** um CSS comum em `static/assets/css/styles.css`, referenciado por todas as páginas.
**Consequências:** uma alteração vale para todas as variantes; uma regressão também afeta todas.
**Confirmação:** um único arquivo CSS e o mesmo caminho em todas as páginas; conferir impressão, temas e `prefers-reduced-motion`.

## 0003 — Cinco variantes com base em pt-BR

**Contexto:** públicos do Brasil, Portugal, América do Sul, Espanha e leitores de inglês, com risco de divergência factual.
**Decisão:** cinco variantes mantidas manualmente, com `pt-BR` como base factual; `en/` usa `en-US`; `es-419` e `es-ES` preservam diferenças editoriais.
**Consequências:** cada público lê na sua variante; toda mudança de fato exige sincronização.
**Confirmação:** cinco pastas, `lang` correto e links `hreflang`; fatos comparados com `pt-BR` ou divergência registrada.

## 0004 — Cópia estruturada oculta

**Contexto:** leitores automáticos precisam de texto simples; a página visível usa cartões e agrupamentos.
**Decisão:** seções ocultas `#dados-curriculo` e `#dados-projetos`, com `hidden` e os mesmos fatos da tela.
**Consequências:** conteúdo no mesmo documento, sem requisição extra; exige sincronização manual com a tela.
**Confirmação:** dados iguais aos da tela; cópia ausente da tela e da impressão.

## 0005 — Ícones por máscara CSS

**Contexto:** ícones pequenos em títulos, listas e botões, com cor herdada nos temas claro e escuro.
**Decisão:** máscara CSS com 28 SVGs em `static/assets/icons/` e o seletor `[data-icon]` com `mask` e `currentcolor`.
**Consequências:** cor acompanha o texto; HTML curto; depende de suporte a `mask`; a licença Lucide precisa ser preservada.
**Confirmação:** 28 SVGs, seletores `[data-icon]` correspondentes e `LICENSE.txt` com a licença ISC/MIT.

## 0006 — Projetos separados apenas em pt-BR

**Contexto:** `pt-BR` tem uma página própria de projetos; as outras variantes têm quatro páginas.
**Decisão:** manter `projetos.html` apenas em `pt-BR`; a expansão entra depois da conclusão de `pt-BR`.
**Consequências:** escopo menor e base factual concentrada; a navegação difere entre variantes.
**Confirmação:** cinco páginas em `pt-BR` e quatro nas demais; menus apontam apenas para páginas existentes.

Esta decisão foi substituída pela decisão 0015.

## 0007 — Publicação restrita a static

**Contexto:** o repositório contém documentação, fontes privadas e dados pessoais ignorados pelo Git.
**Decisão:** publicar somente `static/`; o workflow copia a pasta para uma área temporária e envia ao Pages, com ações fixadas por SHA e permissões mínimas.
**Consequências:** documentação e base privada não são publicadas; todo arquivo do site precisa estar em `static/`.
**Confirmação:** passo que copia `static/.`; permissões `contents: read`, `pages: write` e `id-token: write`; página publicada aberta após o push.

## 0008 — Publicação temporária de duas variantes

**Contexto:** `pt-BR` está em revisão como base do modelo; manter as traduções de `pt-PT`, `es-419` e `es-ES` atualizadas durante a revisão consome recursos e cria divergência.
**Decisão:** publicar somente `pt-BR` e `en`; `pt-PT`, `es-419` e `es-ES` redirecionam para `wip.html`. As pastas e o conteúdo anterior permanecem no histórico Git.
**Consequências:** visitantes desses idiomas veem a página de trabalho em andamento; a tradução será refeita a partir da base concluída. A decisão 0003 permanece vigente como destino.
**Confirmação:** apenas `pt-BR` e `en` têm conteúdo; as demais páginas usam `meta refresh` para `wip.html`; os links de idioma ativos apontam para `pt-BR` e `en`.

## 0009 — Competências com âncoras e detalhe expansível

**Contexto:** a seção `#habilidades` de `pt-BR` exibia 165 tags, e seis subcategorias tinham 9 ou mais tags. A cópia oculta `#dados-curriculo` e a lista de consulta já preservam a cobertura para leitura automática.
**Decisão:** subcategorias com até 8 tags continuam em lista aberta. Com 9 ou mais, a tela mostra quatro âncoras escolhidas entre as tags existentes e um `details.skill-group` fechado por padrão com as demais tags em ordem alfabética. O controle é `summary.skill-more`, com o texto `[ver mais]` e um `aria-label` próprio por subcategoria. As âncoras não se repetem na lista expandida. Sem JavaScript, sem persistência de estado e sem frase por subcategoria.
**Consequências:** a tela inicial de `pt-BR` passa de 165 para 76 tags visíveis e o DOM mantém as 165. A cópia oculta e a lista de tags não mudam. Na impressão, as âncoras e as listas abertas aparecem; as colapsadas não aparecem, porque `summary` fica oculto. A contagem da tela e da impressão deixa de ser igual à da cópia oculta; a soma da tela com as listas expandidas continua igual.
**Confirmação:** seis subcategorias colapsadas em `pt-BR` e quatro em `en`, conforme a contagem de tags de cada idioma; `details` fechados por padrão; `aria-label` único; contagem do DOM igual à anterior; `git diff --check` limpo.

## 0010 — Home de `pt-BR` em painel de atalhos

**Contexto:** a página inicial de `pt-BR` acumulava cerca de 1.500 palavras visíveis, 130 itens de lista e 18 subcategorias de competências antes da seção Experiência, que começava a cerca de 5.500 CSS px do topo a 320 CSS px. A avaliação de terceiros apontou excesso de conteúdo e rolagem até a informação desejada.
**Decisão:** a home de `pt-BR` abre com `section.hero.panel`, um painel com identidade, duas ações, três portas por âncora (Experiência, Competências, Formação), seis atalhos para subcategorias técnicas, três cartões de projeto e uma faixa de contato. Experiência passa a vir antes de Competências. O cabeçalho fica com a marca, o link de Contato e o seletor de idioma; os demais links passam para o rodapé e para o painel. A seção Perfil é removida, porque repetia as três portas. Os conteúdos previstos da graduação passam para um `details` fechado. A mudança vale apenas para `pt-BR` nesta etapa; `en` mantém a estrutura anterior.
**Consequências:** o painel tem cerca de 190 palavras e a Experiência começa logo depois dele, a um clique de qualquer seção. A página não encurta no total: as seções abaixo do painel mantêm o conteúdo atual. A estrutura de `pt-BR` e de `en` diverge até a sincronização; a regra 8 do AGENTS.md fica com esta exceção registrada. Os atalhos e os cartões do painel não são impressos; a impressão mantém a identidade e as seções completas. Os três cartões repetem uma frase de cada projeto de `projetos.html` e exigem sincronização manual.
**Confirmação:** âncoras do painel resolvem para seções e `h4` existentes; nenhuma âncora dentro de `details` fechado; `git diff --check` limpo; verificação visual e de impressão pendente.

## 0011 — Comparação da home de `pt-BR` em duas versões

**Contexto:** a decisão 0010 substituiu a home de `pt-BR`, mas a escolha entre as duas estruturas depende de comparação em produção, no mesmo aparelho e com o mesmo CSS.
**Decisão:** manter `index.html` com a estrutura anterior como versão principal e publicar o painel em `pt-BR/painel.html`, sem link no menu, com `noindex` e sem os `link rel="alternate"` de idioma. Cada página oferece um ícone `⇄` no rodapé, ao lado do controle de estilos, que alterna entre as duas. As duas usam a mesma folha e mantêm o seletor de estilos experimentais.
**Consequências:** o visitante vê a versão anterior por padrão e só encontra a candidata pelo ícone do rodapé. O parâmetro de cache `?v=20261114-comparacao` vale para as duas páginas. A candidata é uma duplicata da principal: `noindex` evita a indexação e os alternates de idioma ficam só na principal. A sincronização de `en` continua pendente, agora junto da escolha da versão (P-22). Remover a versão descartada exige apagar `painel.html`, o atalho e o bloco `.footer-tools`.
**Confirmação:** os ícones alternam entre `index.html` e `painel.html` nos dois sentidos; as duas páginas carregam o CSS comum; `painel.html` tem `noindex` e nenhum alternate de idioma; sem rolagem horizontal a 1280×800 e 390×844; `git diff --check` limpo.

## 0012 — Gestão de projetos como subcategoria própria

**Contexto:** a subcategoria Gestão e produtividade misturava administração, ferramentas de escritório e gestão de projetos. Competências amplas, como gestão de tráfego pago e comércio eletrônico, ficavam ocultas no controle de expansão.
**Decisão:** separar Gestão de projetos de Gestão administrativa e produtividade nas variantes `pt-BR` e `en`. Renomear a subcategoria de marketing, selecionar quatro âncoras que incluam competências amplas e manter as demais tags no detalhe expansível. O primeiro atalho do painel aponta para Gestão de projetos.
**Consequências:** os três grupos principais e a quantidade de tags permanecem; o leitor vê gestão de projetos e competências amplas sem expandir listas. As cópias estruturadas preservam todas as tags e separam a nova subcategoria.
**Confirmação:** comparar tags visíveis e ocultas antes e depois da mudança, verificar as seis âncoras do painel, a cópia estruturada e `git diff --check`.

## 0013 — Finanças e ferramentas Microsoft como subcategorias

**Contexto:** Gestão administrativa e produtividade ainda agrupava finanças e produtos Microsoft. O responsável pediu subcategorias próprias para os dois conjuntos.
**Decisão:** mover capitalização, fluxo de caixa e gestão financeira para Finanças; mover os produtos Microsoft para Ferramentas Microsoft. Indicadores estratégicos e melhoria de processos permanecem em Gestão administrativa e produtividade. A versão `en` usa Finance e Microsoft tools. Os aliases permanecem na cópia estruturada.
**Consequências:** as três categorias principais, os seis atalhos do painel e os níveis das tags permanecem. Microsoft 365 substitui Office 365 na lista de tela; Office 365 continua na cópia estruturada. Microsoft Word e Microsoft 365 passam a constar da lista de competências em `en`, em alinhamento com a base `pt-BR`.
**Confirmação:** conferir a distribuição e a contagem das tags em `pt-BR`, `en` e na lista de consulta; verificar as quatro âncoras da subcategoria administrativa e executar `git diff --check`.

## 0012 — Painel como home oficial somente em `pt-BR`

**Contexto:** o responsável escolheu a versão alternativa como oficial, apenas em `pt-BR`.
**Decisão:** promover o conteúdo de `painel.html` a `index.html`, restaurar o título e os alternates de idioma, retirar `noindex`, remover a página alternativa e o atalho de comparação. Preservar o seletor de estilos. Substitui a decisão 0011.
**Consequências:** o endereço principal apresenta o painel; a versão anterior permanece recuperável no Git. `en` mantém sua estrutura por escopo explícito do pedido.
**Confirmação:** verificar âncoras, links locais, metadados e apresentação responsiva; executar `git diff --check`.

### Extensão da decisão 0012 — sincronização de `en`

Em pedido posterior, o responsável autorizou atualizar a home em inglês. O painel, a ordem das seções, os conteúdos previstos colapsados, o perfil SFIA e as competências seguem a base `pt-BR`, com redação en-US. *(Nota: o trecho anterior que mantinha fichas completas em `en/index.html` foi superado pela decisão 0015 e pela promoção da decisão 0017, com `en/projetos.html` e dois cartões no painel.)* As regras visuais são compartilhadas no CSS comum. A restrição anterior de manter a estrutura de `en` deixa de valer.

## 0014 — Páginas experimentais de Projetos e Agradecimentos

**Contexto:** o responsável quer avaliar a nova organização de perfis e créditos em produção.
**Decisão:** publicar as prévias com `noindex` e acesso pelo ícone ⇄ no rodapé, seguindo a decisão 0011. As páginas oficiais mantêm seu conteúdo. Em inglês, a prévia de Projetos contém a ficha do SGCS, cuja versão oficial fica na home.
**Confirmação:** verificar a alternância nos dois sentidos, os links entre créditos e perfis experimentais e a troca de idioma em Agradecimentos. A promoção das prévias depende da avaliação do responsável.

### Extensão da decisão 0014 — promoção das páginas

Em 19/11/2026, o responsável aprovou a estrutura experimental de Projetos em `pt-BR` e de Agradecimentos em `pt-BR` e `en` como principal. Os endereços oficiais recebem essa estrutura; os endereços experimentais redirecionam para eles. Agradecimentos conserva âncoras estáveis para os quatro perfis reais e a introdução da página anterior. Os marcadores de texto pessoal e o perfil fictício de professor ficam fora das páginas oficiais até que o responsável forneça conteúdo confirmado.

## 0015 — Projetos e publicações nas duas variantes ativas

**Decisão:** manter `projetos.html` em `pt-BR` e `en`, com as mesmas seções e navegação entre idiomas. A página inicial inglesa conserva links nos destinos das âncoras antigas. A antiga página experimental inglesa do SGCS redireciona à ficha oficial.

## 0016 — Arquivo de currículos legados e nomeação de novas edições

**Contexto:** as edições V3, V4 e V5 estavam lado a lado com a próxima edição, sem distinção entre arquivo e trabalho atual.
**Decisão:** reunir V3, V4 e V5 em `docs/curriculos/cvs-legados/`. Iniciar a próxima edição em `docs/curriculos/CV-NicolasBt-2026-11-01/` e usar `CV-NicolasBt-AAAA-MM-VV` para as edições seguintes. O mês usa dois dígitos e a versão reinicia em `01` a cada mês.
**Consequências:** links e caminhos dos geradores acompanham o novo local. Os PDFs V5 disponibilizados em `static/assets/curriculos/` continuam sendo a edição publicada até a próxima estar pronta.
**Confirmação:** conferir links internos, caminhos dos geradores, hashes dos currículos legados e os downloads do site.

### Edição publicada de novembro de 2026

Em 23/11/2026, o responsável pediu a edição `CV-NicolasBt-2026-11-01` com base na V5 e nas informações atuais do site. Os quatro PDFs dessa edição passam a ser os destinos dos downloads nas variantes ativas. Os quatro DOCX e o manifesto ficam na pasta da edição.

Ainda em 23/11/2026, o responsável pediu a versão `CV-NicolasBt-2026-11-02` para abreviar a indicação de autoavaliação no perfil SFIA. A edição também incorpora o vínculo de prestação de serviços da JH Eletrônico, atualizado no site depois da versão 01. Os quatro PDFs da versão 02 substituem os destinos dos downloads.

Na revisão seguinte, o responsável aprovou um perfil profissional mais próximo do cotidiano de usuários e clientes e a apresentação de suas preferências de desenvolvimento na home. A edição `CV-NicolasBt-2026-11-03` incorpora o novo perfil e substitui os quatro downloads nas variantes ativas.

Depois de avaliar essa redação, o responsável pediu um perfil mais geral e aprovou o texto que apresenta sua atuação em tecnologia, a graduação em andamento e suas experiências sem enumerar critérios de desenvolvimento. A edição `CV-NicolasBt-2026-11-04` aplica o texto aprovado aos quatro currículos e atualiza os downloads em pt-BR e en-US.

## 0017 — Nova rodada de prévias da home e de Projetos em `pt-BR`

Em 24/11/2026, o responsável aprovou a publicação de duas prévias para avaliar a navegação em telas estreitas. A [prévia da home](../static/pt-BR/painel.html) parte de uma cópia da página publicada. Ela antecipa os atalhos de experiência, projetos e contato e permite voltar ao painel após as seções longas. A [prévia de Projetos](../static/pt-BR/projetos-experimental.html) recupera o endereço do teste de 19/11. Ela usa as fichas vigentes, com um índice por nome e detalhes expansíveis.

Os dois endereços usam `noindex`, acesso direto e links para comparar com as páginas oficiais. O CSS comum restringe os ajustes às prévias. A promoção das mudanças depende da avaliação do responsável.

Após avaliar a prévia de Projetos, o responsável substituiu o índice por dois grupos recolhíveis na mesma página (**Projetos** e **Publicações**), iniciando **abertos** (`<details open>`) para acesso direto às fichas e publicações.

Em 25/11/2026, o responsável aprovou a promoção das prévias para as páginas principais (`pt-BR/index.html` e `pt-BR/projetos.html`) e o alinhamento técnico e de conteúdo em `en/index.html` e `en/projetos.html` (incluindo a seção **Princípios de desenvolvimento** / **Development principles**). As prévias (`painel.html` e `projetos-experimental.html`) permanecem acessíveis com `noindex` pelo atalho `⇄` no rodapé de `pt-BR`.

## 0018 — Guia público de documentação do portfólio

Em 24/11/2026, o responsável autorizou a publicação de uma seleção da documentação técnica. O [guia público](../static/pt-BR/documentacao/index.html) apresenta versões de Requisitos, Personas, Arquitetura e Evolução. Com a promoção da decisão 0017 (25/11/2026), o link para o guia foi movido do destaque inicial para o card "Este portfólio" / "This portfolio" em `pt-BR/projetos.html` e `en/projetos.html` (além de `projetos-experimental.html`), removendo-o do destaque inicial de `painel.html`. As páginas do guia usam `noindex`, `styles.css` e `planejamento.css` (em Pendências e Roadmap).

Ao atualizar o guia, revise a versão pública de cada documento e confira seus links. O workflow publica os arquivos revisados em `static/`.

As páginas [Pendências](../static/pt-BR/documentacao/pendencias.html) e [Roadmap](../static/pt-BR/documentacao/roadmap.html) integram o guia e usam a mesma navegação. As fontes da documentação do repositório são vinculadas no GitHub.

## 0019 — Correspondência de tarefas NICE abaixo do SFIA

Em 24/11/2026, o responsável aprovou um bloco recolhível abaixo do SFIA nas duas homes ativas e no painel experimental. O bloco relaciona as tarefas `T0237`, `T1412` e `T1567` de Technical Support (`IO-WRL-007`) às atividades profissionais já descritas. A cópia estruturada, a impressão e a lista de consulta acompanham as fichas visíveis. [Catálogo NICE](https://www.nist.gov/itl/applied-cybersecurity/nice/nice-framework-resource-center/nice-framework-current-versions)

## 0020 — Menu centralizado de páginas experimentais e visão experimental de portfólio

**Contexto:** após a promoção da decisão 0017, as prévias (`painel.html` e `projetos-experimental.html`) continuaram acessíveis, e o responsável aprovou testar uma visão leve de gestão de portfólio e priorização (Valor × Complexidade) sem alterar a documentação oficial consolidada.
**Decisão:** criar o menu centralizado `static/pt-BR/experimentais.html` (com `noindex`) e redirecionar o botão `⇄` no rodapé de `static/pt-BR/index.html` para esse menu. Criar `static/pt-BR/portfolio-experimental.html` (com `noindex`) reunindo o enquadramento de governança leve (*tailoring*), o mapa de artefatos do site e a classificação Valor × Complexidade das pendências vigentes (`P-01`–`P-09`, vinculadas às âncoras de `documentacao/pendencias.html`). Adicionar link de retorno ao menu experimental nos rodapés de `painel.html` e `projetos-experimental.html`.
**Procedência e limites:** a estrutura conceitual decorre de consulta local em modo somente leitura a referências de gestão de portfólio (PM² Portfolio Management Guide v1.5 e Guia Referencial para Gerenciamento de Projetos e Portfólios), sem copiar arquivos privados para este repositório e sem declarar certificação ou conformidade integral com frameworks institucionais.
**Consequências:** todas as prévias passam a ter um ponto único de entrada a partir da home `pt-BR`; as páginas oficiais de documentação permanecem inalteradas até eventual promoção; nenhuma alteração de CSS ou JavaScript é necessária.
**Confirmação:** verificar navegação `index.html` → `experimentais.html` → `painel.html` / `projetos-experimental.html` / `portfolio-experimental.html` e retorno, validar âncoras `P-01`–`P-09`, confirmar `noindex` e ausência de `<script>`/`<form>`/`<iframe>`, e executar `git diff --check`.

## 0021 — Unificação de documentação técnica ao portfólio experimental, plano de carreira experimental e aposentadoria das prévias promovidas

**Contexto:** as prévias `painel.html` e `projetos-experimental.html` já haviam sido promovidas às páginas principais (`pt-BR/index.html` e `pt-BR/projetos.html`) e o responsável solicitou manter a documentação técnica unificada à gestão de portfólio apenas em ambiente experimental, além de criar uma página experimental de plano de carreira.
**Decisão:** converter `static/pt-BR/painel.html` e `static/pt-BR/projetos-experimental.html` em redirecionamentos estáticos (`meta refresh` + `canonical` + `noindex`) para `index.html` e `projetos.html`, removendo o atalho `⇄` do rodapé de `pt-BR/projetos.html`. Unificar o índice da documentação técnica dentro de `static/pt-BR/portfolio-experimental.html`, converter `static/pt-BR/documentacao/index.html` em redirecionamento para `../portfolio-experimental.html`, atualizar o menu das seis subpáginas de `documentacao/` e remover o link público da documentação nos cards de `pt-BR/projetos.html` e `en/projetos.html`. Criar `static/pt-BR/carreira-experimental.html` (com `noindex`) baseado nos dados verificados do portfólio e atualizar `static/pt-BR/experimentais.html` para listar apenas as duas prévias ativas (`portfolio-experimental.html` e `carreira-experimental.html`).
**Consequências:** as páginas principais ficam livres de links para documentação experimental e prévias antigas; endereços antigos não quebram graças aos redirecionamentos estáticos; o menu experimental concentra apenas iniciativas em evolução ativa.
**Confirmação:** verificar redirecionamentos, links e âncoras em todas as páginas alteradas, ausência de `<script>`/`<form>`/`<iframe>`, `noindex` nas páginas experimentais e `git diff --check`.

## 0022 — Seis propostas experimentais de estética e organização

**Contexto:** em 27/11/2026, o responsável pediu novas propostas minimalistas, brutalistas, de terminal, militaristas, NATO e construtivistas, com publicação experimental e foco em funcionalidade. Esclareceu que o repositório da nuvem é a fonte e que o Lovable só deve fornecer recursos sem geração paga.

**Decisão:** publicar `pt-BR/estudos-visuais.html` e seis páginas `estudo-*.html`, acessíveis pelo menu experimental existente. Cada proposta combina uma hierarquia de conteúdo com uma composição própria. A série usa HTML e CSS locais, fontes do sistema, links diretos e controles `details` nativos. Todas as páginas recebem `noindex` e links para comparar propostas e voltar ao portfólio atual. Os estilos ficam no CSS comum, restritos a `.lab-page` e classes `lab-*`.

| Página | Direção | Estrutura de consulta |
| --- | --- | --- |
| `estudo-minimalista.html` | Índice editorial | Coluna de identidade e experiência antes dos projetos. |
| `estudo-brutalista.html` | Estrutura bruta | Projetos numerados e experiências em blocos. |
| `estudo-terminal.html` | Diretório pessoal | Índice lateral, campos alinhados e listas expansíveis. |
| `estudo-campo.html` | Manual de campo | Competências antes da experiência, com fichas de consulta. |
| `estudo-nato.html` | Dossiê técnico | Projetos comparáveis por objetivo, contribuição e resultado. |
| `estudo-construtivista.html` | Forma e função | Composição assimétrica, numeração e sequência editorial. |

**Conteúdo e limites:** a base é `d75baf3`, com os textos vigentes de `index.html` e `projetos.html`. As cinco experiências, as três categorias de competências e suas subcategorias preservam os fatos e qualificadores. Os três projetos mantêm atribuições individuais e de equipe. A formação é resumida, com acesso ao conteúdo completo e aos PDFs existentes. As prévias não acrescentam competências ou resultados. SFIA e NICE remetem às seções oficiais. As referências NATO e militares são visuais, sem insígnias ou alegação de vínculo institucional.

**Consequências:** esta série é uma experiência apenas em `pt-BR`, seguindo o escopo das prévias existentes. Não modifica as homes oficiais nem seus resumos ocultos. Cada prévia apresenta os dados em HTML semântico e dispensa uma segunda cópia oculta dos mesmos trechos; a cópia estruturada completa continua na página oficial. Tradução, adoção como página principal e eventual consolidação dependem da escolha posterior do responsável. As seis cópias exigem sincronização quando a base factual mudar. As consultas ao Lovable não encontraram modelos ou sistemas de design reutilizáveis; nenhuma geração foi solicitada.

**Verificação:** Chromium 151, sete páginas novas, 56 combinações de largura (320, 390, 768 e 1440 CSS px) e tema; sem transbordamento horizontal. Controles por teclado, links locais, âncoras, downloads e impressão conferidos. HTML-Validate 11.23.0 sem erros no perfil recomendado, com exceção documentada para `role="list"` em listas sem marcadores (preserva semântica no Safari) e regras editoriais de título/espaçamento. Axe-core 4.14.1 sem violações automáticas nos critérios selecionados de WCAG A/AA, nas sete páginas em ambos os temas com detalhes abertos. Esses ensaios não certificam acessibilidade. A captura da home oficial em 1440 px permaneceu idêntica antes e depois. Leitor de tela, Safari, Firefox e dispositivos físicos não foram ensaiados.
