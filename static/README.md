# Versões estáticas por idioma

- `pt-BR/index.html`: português brasileiro.
- `en/index.html`: inglês.

Cada idioma mantém seu HTML, CSS e favicon. Os links de troca de idioma
apontam para a pasta irmã. Esta pasta é a única fonte do site publicado.
Ao alterar o estilo compartilhado, atualize as duas cópias de `styles.css`.

As correções de acessibilidade foram aplicadas somente às versões desta pasta.
Consulte o [registro de alterações e verificações](../docs/acessibilidade.md).

Para servir somente estas versões, na raiz do repositório execute:

```sh
python3 -m http.server 8001 --bind 127.0.0.1 --directory static
```

As páginas ficam nos caminhos `/pt-BR/` e `/en/`. A raiz apresenta a escolha
de idioma. O servidor Python é apenas para desenvolvimento.

O workflow `.github/workflows/pages.yml` publica esta pasta no GitHub Pages.
`README.md` é documentação e é excluído do artefato de publicação.
