# Manutenção do portfólio

## Conteúdo e idiomas

Use `static/pt-BR/index.html` como base factual.
Atualize também `pt-PT`, `en`, `es-419` e `es-ES` quando o conteúdo comum mudar.
Cada idioma mantém `index.html`, `galeria.html`, `rede.html` e `recomendacoes.html`.
Use inglês norte-americano em `en/`, com `lang` e `hreflang` definidos como `en-US`.
Em `es-419`, preserve a redação para o público sul-americano.

Confira as [fontes e atribuições](conteudo-e-fontes.md) antes de alterar competências, cargos, projetos ou formação.
Preserve as três categorias de competências e suas subcategorias.
Use uma tecnologia, competência ou qualificação por tag.
Mantenha observações de nível para suporte técnico, fusão de fibra e inglês.
Registre outras limitações nas descrições e na formação.

A cópia oculta `dados-curriculo` deriva dos dados públicos da página.
Ela não é uma entrada independente para ampliar qualificações.
Confira a coerência entre a página, o bloco oculto e a [lista de consulta](../listas-de-tags/README.md).
Os aliases auxiliam consultas específicas. Eles não garantem reconhecimento por todos os ATS.

## Página de projetos em pt-BR

Desde 02/11/2026, por solicitação do responsável, `static/pt-BR/projetos.html` reúne os três projetos e sua cópia estruturada. A página principal mantém um link no menu, outro na apresentação inicial e uma referência no resumo oculto. A âncora antiga `index.html#projetos` leva ao acesso da apresentação. As outras variantes linguísticas mantêm a estrutura anterior nesta etapa, conforme o escopo solicitado.

Para editar projetos em pt-BR, use a nova página e confira sua cópia estruturada, as atribuições em [Conteúdo e fontes](conteudo-e-fontes.md#projetos) e as listas de consulta. A impressão da página principal apresenta o currículo sem os cartões; a página de projetos permite imprimir os três cartões. Os PDFs V3 permanecem edições históricas.

Objetivo e decisão: separar a apresentação dos projetos, com acesso no início do currículo, reutilizando o CSS comum e preservando integralmente as descrições. Fundamentação: HTML Living Standard, seções de navegação, conteúdo principal e links; WCAG 2.2, critérios de reorganização, propósito do link e foco visível. A restrição desta entrega ao pt-BR é decisão do responsável.

Verificação em 02/11/2026: navegação de ida, três cartões na nova página, links e âncoras locais, um main por página, link de salto por teclado com foco visível, temas claro/escuro e larguras de 1280 e 320 CSS px no Chromium local. Não houve transbordamento horizontal; 320 CSS px cobre a largura equivalente a 400% de zoom em 1280 px. Em mídia de impressão, a cópia oculta permanece invisível e os 17 cursos aparecem na lista de impressão do currículo. Inspeção visual de capturas e cálculo amostral de contraste realizados. Limites: zoom real e paginação física não ensaiados; sem validação externa de HTML, leitor de tela ou declaração de conformidade WCAG. A estrutura pt-BR foi conferida por listagem local. Sem publicação nesta entrega.

## Recomendações

Use `recomendacoes.html` para divulgar projetos, iniciativas, livros e recursos selecionados pelo responsável.
A página `rede.html` mantém os agradecimentos às pessoas da rede.
Preserve o acesso às recomendações pelo menu, pela seção Contato e pelo rodapé da página principal.
O acesso junto aos contatos fica oculto na impressão do currículo.

Crie categorias somente quando houver indicações. Não publique seções vazias ou itens de exemplo.
Cada indicação usa um cartão com título, descrição curta e link descritivo para a fonte.
Nos livros, preserve o título oficial e identifique a autoria e a edição quando informadas.
Acrescente motivos pessoais para recomendar um item somente quando o responsável os fornecer.
Confira a fonte e registre o contexto em [fontes e atribuições](conteudo-e-fontes.md).
Traduza o conteúdo comum nos cinco idiomas e confira os links de troca de idioma.
Prefira o destino no idioma da página quando houver uma tradução disponível.

## Cursos e currículos

A página mantém duas cópias de tela e impressão dos cursos, além do resumo estruturado.
Quando um curso mudar, atualize suas ocorrências em cada idioma.
Preserve títulos oficiais, instituições, datas, cargas horárias e atributos de idioma.
Confira cada curso uma única vez na impressão, com o controle recolhível aberto e fechado.

Os [PDFs V3](curriculos/v3/README.md) são edições identificadas, não exportações automáticas de cada alteração do site.
Ao gerar uma nova edição, confira o conteúdo, a extração textual, as margens e a paginação do DOCX e do PDF.
Atualize o manifesto da edição e mantenha somente os arquivos necessários à sua manutenção.
Os DOCX V3 estão na [pasta de currículos no Drive](https://drive.google.com/drive/folders/1v7H0YOlGlE_R9osngevcE5LquYOzcIDI).

## HTML, CSS e publicação

Todas as páginas usam `static/assets/css/styles.css`.
Calcule os caminhos relativos conforme a profundidade de cada página.
Preserve fontes do sistema, recursos locais e as imagens WebP/JPEG compartilhadas em `static/media/realfort/`.
Não adicione JavaScript, backend, frameworks, rastreadores ou etapa de build.

### Ícones Lucide em pt-BR

Desde 02/11/2026, por solicitação do responsável, a pasta compartilhada `static/assets/icons/` armazena 28 arquivos SVG da biblioteca Lucide Icons (com licença ISC/MIT preservada em `static/assets/icons/LICENSE`). O estilo comum `static/assets/css/styles.css` alimenta os ícones por `[data-icon]::before` com `background-color: currentColor` e `mask`. Nesta etapa, os atributos `data-icon` foram aplicados apenas às páginas em `static/pt-BR/` (`index.html`, `projetos.html`, `galeria.html`, `rede.html` e `recomendacoes.html`), nos títulos (`h2`), subtítulos até `h3` e links de contato (`.contact-list a`), sem alterar os blocos ocultos de extração (`#dados-curriculo` e `#dados-projetos`) nem as demais variantes linguísticas.

Objetivo, decisão e fundamentação: centralizar a manutenção dos ícones em uma única pasta e no CSS compartilhado, mantendo HTML/CSS estáticos sem JavaScript e herança automática de cor nos temas claro, escuro, `:hover` e impressão. Fundamentação: HTML Living Standard (atributos `data-*`), CSS Color Level 4 (`currentcolor`), CSS Values and Units Level 4 (resolução de URLs relativas ao arquivo CSS), WCAG 2.2 (critérios `1.1.1` — Conteúdo Não Textual / Decoração e `1.4.11` — Contraste Não Textual) e CSS Color Adjustment Level 1 (`prefers-color-scheme` e `print-color-adjust: exact`). A restrição desta entrega ao pt-BR é decisão do responsável.

Verificação em 02/11/2026 (inspeção de código e checagem estática): conferência dos 28 arquivos SVG em `static/assets/icons/`, correspondência de todos os seletores `[data-icon]` em `static/assets/css/styles.css` com as ocorrências em `static/pt-BR/*.html`, preservação de `#dados-curriculo` e `#dados-projetos` sem atributos visuais, preservação dos 17 cursos na cópia de tela e de impressão, e `git diff --check` sem erros. Limitações: verificação realizada por inspeção estática de código; ensaio visual interativo em navegador (renderização de `mask`, teclado, foco, contraste amostral, largura de 320 CSS px, zoom de 400%, alternância de temas claro/escuro e paginação física de impressão) pendente de execução no servidor local (`http://127.0.0.1:8001/pt-BR/`). Demais idiomas não alterados por decisão de escopo do responsável.

Execute na raiz:

```sh
python3 -m http.server 8001 --bind 127.0.0.1 --directory static
```

Abra `http://127.0.0.1:8001/`.
Confira links, âncoras, troca de idioma, CSS, favicon e páginas afetadas.
Para mudanças visuais, confira teclado, foco, contraste, telas pequenas, zoom, temas e impressão.
Use validação HTML/CSS quando pertinente. Diferencie inspeção de código de ensaio em navegador.

O workflow `.github/workflows/pages.yml` publica somente `static/` após push em `main`.
No GitHub, a origem de publicação deve ser GitHub Actions.
As permissões mínimas do workflow são `contents: read`, `pages: write` e `id-token: write`.

## Mudanças

Toda mudança segue o procedimento da seção 3 de [Padrões técnicos](padroes-tecnicos.md).

1. Descreva o pedido, a finalidade e a fonte.
2. Analise o impacto nas variantes, páginas, links, acessibilidade, impressão e documentos.
3. Obtenha autorização do responsável antes de alterar conteúdo ou site.
4. Faça uma mudança pequena, com um propósito.
5. Verifique HTML, links internos e temas. Acrescente as verificações da fase afetada.
6. Use mensagem de commit clara, com o motivo e a fase.
7. Registre no `CHANGELOG.md` e atualize a situação no plano.
8. Depois do push, confira a página publicada.

Reversão: use `git revert` em até cinco commits. Não reescreva o histórico da `main`. Registre o motivo e o resultado. Acima de cinco commits ou em caso de conflito, pare e peça decisão ao responsável.

## Organização

Use `Get-ChildItem -Recurse -Depth 3 -Force | Where-Object { $_.FullName -notmatch '\\\.git\\' }` para revisar a estrutura antes e depois de reorganizações.
Mantenha regras gerais em `AGENTS.md`, instruções práticas neste guia e as fontes em `docs/referencias/`.
Preserve uma síntese vigente por assunto. Não acrescente planos, caches, saídas brutas ou clones de terceiros à árvore ativa.
Antes de retirar uma fonte necessária, preserve sua origem, licença e forma de recuperação.
O [registro da organização](organizacao.md) identifica o acervo anterior e sua recuperação.

Ao concluir, execute `git diff --check` e informe as verificações e suas limitações.
