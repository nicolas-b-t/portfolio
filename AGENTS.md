# Orientações do projeto

Estas regras se aplicam ao repositório inteiro.

## Projeto e conteúdo

- Mantenha o site pessoal, estático e funcional com HTML e CSS.
- Não adicione JavaScript, eventos embutidos, rastreadores, widgets, frameworks, backend ou etapa de build.
- Use somente tecnologias e dependências necessárias ao conteúdo.
- Preserve caminhos relativos, fontes do sistema e recursos locais.
- Use `static/pt-BR/index.html` como base factual para os cinco idiomas.
- Preserve nomes oficiais, cargos, vínculos, datas, qualificações, níveis e atribuições individuais ou da equipe.
- Não transforme conteúdos previstos da graduação em formação concluída ou experiência profissional.
- Consulte [fontes e atribuições](docs/conteudo-e-fontes.md) antes de ampliar ou alterar uma afirmação.
- Aplique o [guia de redação](docs/guia-de-redacao.md), baseado na ASD-STE100, edição 9, sem declarar certificação formal.
- Preserve textos e avisos de documentos oficiais. A adaptação editorial aplica-se aos textos autorais.
- Preserve os bytes das cópias oficiais em `docs/referencias/europass/fontes/`. Esses documentos não integram o site publicado.

## Estrutura e idiomas

- `static/` é a única fonte do site publicado.
- O CSS comum fica em `static/assets/css/styles.css`. Não crie cópias por idioma.
- Preserve `pt-BR`, `pt-PT`, `en`, `es-419` e `es-ES`.
- Use inglês norte-americano em `en/`, com `lang` e `hreflang` definidos como `en-US`.
- Em `es-419`, preserve a redação para o público sul-americano.
- Mantenha os três arquivos de cada idioma: `index.html`, `galeria.html` e `rede.html`.
- Sincronize fatos e estrutura comuns entre os idiomas. Preserve as variantes linguísticas.
- Preserve as três categorias de competências e suas subcategorias.
- Ao alterar cursos, atualize as cópias de tela, impressão e resumo estruturado nos idiomas afetados.
- Confira títulos, instituições, datas, cargas horárias e os 17 cursos uma única vez na impressão.
- Mantenha a coerência entre conteúdo visível, resumo oculto e listas de consulta.

## HTML, CSS e acessibilidade

- Siga o HTML Living Standard. Prefira semântica nativa e use ARIA somente quando necessária.
- Mantenha UTF-8, títulos descritivos, hierarquia de cabeçalhos e atributos de idioma corretos.
- Prefira CSS amplamente suportado. Forneça alternativa quando o suporte for limitado.
- Use WCAG 2.2 nível AA como alvo, sem declarar conformidade apenas por testes automáticos.
- Preserve navegação por teclado, foco visível, link de salto e nomes compreensíveis para controles e links.
- Confira contraste, alternativas textuais, reorganização em telas pequenas e zoom.
- Preserve temas claro e escuro, impressão e respeito a `prefers-reduced-motion`.

## Trabalho no repositório

- Confira `git status --short` antes de editar. Preserve alterações existentes.
- Use o checkout atual. Não crie worktrees sem solicitação do responsável.
- Consulte [Manutenção](docs/manutencao.md) para execução, publicação e conferência das páginas.
- Para mudanças visuais, confira também teclado, foco, contraste, telas pequenas, zoom, temas e impressão.
- Execute `git diff --check`. Informe verificações, resultados e limites.
- Use `tree -a -L 3 -I .git` para avaliar reorganizações.
- Mantenha uma síntese vigente por assunto e atualize os links ao mover ou retirar arquivos.
- Guarde scripts temporários, caches, exportações intermediárias e clones de terceiros fora do repositório.
- Preserve fontes, licenças e meios de recuperação antes de retirar um acervo.
- Mantenha os dez PDFs V3 versionados, conforme autorização do responsável.
- Não acrescente credenciais, configurações pessoais de máquina ou documentos restritos ao site.
- Use nomes descritivos em português, sem acentos, com hífens. Preserve nomes oficiais e nomes de arquivos solicitados.
