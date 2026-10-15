# Manutenção do portfólio

## Conteúdo e idiomas

Use `static/pt-BR/index.html` como base factual.
Atualize também `pt-PT`, `en`, `es-419` e `es-ES` quando o conteúdo comum mudar.
Cada idioma mantém `index.html`, `galeria.html` e `rede.html`.
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
