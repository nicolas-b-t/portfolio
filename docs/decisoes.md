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
| 0006 | Projetos apenas em `pt-BR` | Aceita |
| 0007 | Publicação restrita a `static/` | Aceita |
| 0008 | Publicação temporária de duas variantes | Aceita |
| 0009 | Competências com âncoras e detalhe expansível | Aceita |
| 0010 | Home de `pt-BR` em painel de atalhos | Aceita |
| 0011 | Comparação da home de `pt-BR` em duas versões | superseded |
| 0012 | Painel como home oficial somente em `pt-BR` | Aceita |
| 0012 | Gestão de projetos como subcategoria própria | Aceita |
| 0013 | Finanças e ferramentas Microsoft como subcategorias | Aceita |
| 0014 | Páginas experimentais de Projetos e Agradecimentos | Aceita |

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

Em pedido posterior, o responsável autorizou atualizar a home em inglês. O painel, a ordem das seções, os conteúdos previstos colapsados, o perfil SFIA e as competências seguem a base `pt-BR`, com redação en-US. As fichas completas dos projetos permanecem em `en/index.html`, e os três destaques apontam para suas âncoras. As regras visuais são compartilhadas no CSS comum; o escopo adicional é somente a home inglesa. A restrição anterior de manter a estrutura de `en` deixa de valer.

## 0014 — Páginas experimentais de Projetos e Agradecimentos

**Contexto:** o responsável quer avaliar a nova organização de perfis e créditos em produção.
**Decisão:** publicar as prévias com `noindex` e acesso pelo ícone ⇄ no rodapé, seguindo a decisão 0011. As páginas oficiais mantêm seu conteúdo. Em inglês, a prévia de Projetos contém a ficha do SGCS, cuja versão oficial fica na home.
**Confirmação:** verificar a alternância nos dois sentidos, os links entre créditos e perfis experimentais e a troca de idioma em Agradecimentos. A promoção das prévias depende da avaliação do responsável.

### Extensão da decisão 0014 — promoção das páginas

Em 19/11/2026, o responsável aprovou a estrutura experimental de Projetos em `pt-BR` e de Agradecimentos em `pt-BR` e `en` como principal. Os endereços oficiais recebem essa estrutura; os endereços experimentais redirecionam para eles. Projetos conserva o SGCS antes da Portugal Digital Solutions nas fichas visíveis e na cópia estruturada. Agradecimentos conserva âncoras estáveis para os quatro perfis reais e a introdução da página anterior. Os marcadores de texto pessoal e o perfil fictício de professor ficam fora das páginas oficiais até que o responsável forneça conteúdo confirmado.
