# Decisões de arquitetura

Nove decisões aceitas entre 02/11/2026 e 11/11/2026.
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
