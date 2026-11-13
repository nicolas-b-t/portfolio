# Orientações do projeto

Estas regras se aplicam ao repositório inteiro.
Este arquivo é auto-contido: não depende de instruções fora da raiz do projeto, para permitir sandboxing.

## Escopo e conteúdo

1. Mantenha o site pessoal, estático, em HTML e CSS. Não adicione JavaScript, framework, backend ou etapa de build.
2. `static/` é a única fonte do site publicado.
3. Preserve nomes oficiais, cargos, vínculos, datas, qualificações e atribuições; não transforme graduação prevista em formação concluída.
4. Consulte [fontes e atribuições](docs/conteudo-e-fontes.md) antes de ampliar ou alterar uma afirmação.
5. Preserve os bytes das cópias oficiais em `docs/referencias/europass-fontes/`; elas não são publicadas.
6. Enquanto a base estiver em revisão, somente `pt-BR` e `en` são publicados; `pt-PT`, `es-419` e `es-ES` redirecionam para `wip.html` (decisão 0008).

## Idiomas e estrutura

7. Preserve os cinco idiomas, a estrutura de páginas e as três categorias de competências descritas em [Manutenção](docs/manutencao.md).
8. Sincronize fatos e estrutura comuns entre idiomas, preservando as variantes linguísticas.
9. Mantenha o CSS comum em `static/assets/css/styles.css`, sem cópias por idioma.

## Trabalho no repositório

10. Confira `git status --short` antes de editar e preserve alterações existentes.
11. Use o checkout atual; não crie worktrees sem solicitação do responsável.
12. Execute `git diff --check` e informe verificações, resultados e limites.
13. Mantenha `dados-pessoais/` fora do Git.
14. Termine cada turno com as listas de inferências assumidas e pendências.

O detalhe de redação, acessibilidade, publicação e organização está em [Regras técnicas](docs/regras-tecnicas.md) e [Manutenção](docs/manutencao.md).
