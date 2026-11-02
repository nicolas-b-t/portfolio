# Manutenção do portfólio

## Desenvolvimento da versão 2

Siga o [fluxo documentado](desenvolvimento-v2.md) em cada mudança.
Consulte a fonte pertinente no [índice local](referencias/desenvolvimento-v2/indice-local.md) e registre a seção usada, a decisão e a verificação.
As fontes privadas ficam neste projeto, fora de `static/` e ignoradas pelo Git.
Não dependa das pastas externas `REPERTORIO_TECNICO` e `fas-doddir` para continuar o trabalho.

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
Confira a coerência entre a página, o bloco oculto e a [lista de consulta](../Lista_de_tags/README.md).
Os aliases auxiliam consultas específicas. Eles não garantem reconhecimento por todos os ATS.

## Página de projetos em pt-BR

Desde 02/11/2026, por solicitação do responsável, `static/pt-BR/projetos.html` reúne os três projetos e sua cópia estruturada. A página principal mantém um link no menu, outro na apresentação inicial e uma referência no resumo oculto. A âncora antiga `index.html#projetos` leva ao acesso da apresentação. As outras variantes linguísticas mantêm a estrutura anterior nesta etapa, conforme o escopo solicitado.

Para editar projetos em pt-BR, use a nova página e confira sua cópia estruturada, as atribuições em [Conteúdo e fontes](conteudo-e-fontes.md#projetos) e as listas de consulta. A impressão da página principal apresenta o currículo sem os cartões; a página de projetos permite imprimir os três cartões. Os PDFs V3 permanecem edições históricas.

Objetivo e decisão: separar a apresentação dos projetos, com acesso no início do currículo, reutilizando o CSS comum e preservando integralmente as descrições. Fundamentação local: REF-0041, HTML Living Standard, seções 4.3.4 (nav), 4.4.14 (main) e 4.5.1 (a); REF-0127, WCAG 2.2, critérios 1.4.10, 2.4.4 e 2.4.7. São referências técnicas; a restrição desta entrega ao pt-BR é decisão do responsável.

Verificação em 02/11/2026: navegação de ida, três cartões na nova página, links e âncoras locais, um main por página, link de salto por teclado com foco visível, temas claro/escuro e larguras de 1280 e 320 CSS px no Chromium local. Não houve transbordamento horizontal; 320 CSS px cobre a largura equivalente a 400% de zoom em 1280 px. Em mídia de impressão, a cópia oculta permanece invisível e os 17 cursos aparecem na lista de impressão do currículo. Inspeção visual de capturas e cálculo amostral de contraste realizados. Limites: zoom real e paginação física não ensaiados; sem validação externa de HTML, leitor de tela ou declaração de conformidade WCAG. O comando tree solicitado não aceita esses parâmetros no Windows; a estrutura pt-BR foi conferida por listagem local. Sem publicação nesta entrega.

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

A página mantém duas cópias de tela e impressão dos 17 cursos, além do resumo estruturado.
Quando um curso mudar, atualize suas ocorrências em cada idioma.
Preserve títulos oficiais, instituições, datas, cargas horárias e atributos de idioma.
Confira os 17 cursos uma única vez na impressão, com o controle recolhível aberto e fechado.

Os [PDFs V3](curriculos/v3/README.md) são edições identificadas, não exportações automáticas de cada alteração do site.
Ao gerar uma nova edição, confira o conteúdo, a extração textual, as margens e a paginação do DOCX e do PDF.
Atualize o manifesto da edição e mantenha somente os arquivos necessários à sua manutenção.
Os DOCX V3 estão na [pasta de currículos no Drive](https://drive.google.com/drive/folders/1v7H0YOlGlE_R9osngevcE5LquYOzcIDI).

## HTML, CSS e publicação

Todas as páginas usam `static/assets/css/styles.css`.
Calcule os caminhos relativos conforme a profundidade de cada página.
Preserve fontes do sistema, recursos locais e as imagens WebP/JPEG compartilhadas em `static/media/realfort/`.
Não adicione JavaScript, backend, frameworks, rastreadores ou etapa de build.

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

## Organização

Use `tree -a -L 3 -I .git` para revisar a estrutura antes e depois de reorganizações.
Mantenha regras gerais em `AGENTS.md`, instruções práticas neste guia e as fontes em `docs/referencias/`.
Preserve uma síntese vigente por assunto. Não acrescente planos, caches, saídas brutas ou clones de terceiros à árvore ativa.
Antes de retirar uma fonte necessária, preserve sua origem, licença e forma de recuperação.
O [registro da organização](organizacao.md) identifica o acervo anterior e sua recuperação.

Ao concluir, execute `git diff --check` e informe as verificações e suas limitações.
