# Versões estáticas por idioma

- `pt-BR/index.html`: português brasileiro.
- `pt-PT/index.html`: português de Portugal.
- `en/index.html`: inglês.
- `es-419/index.html`: espanhol neutro para o público sul-americano.
- `es-ES/index.html`: espanhol de Espanha.

Cada pasta também contém `rede.html`, com agradecimentos e recomendações de
contatos, e `galeria.html`, com fotografias profissionais otimizadas. O rodapé
do portfólio aponta para essas páginas separadas. As fotografias são compartilhadas
em `media/realfort/`, com versões WebP e JPEG; não se deve duplicá-las por idioma.

`es-419` é a etiqueta BCP 47 para América Latina e Caribe, uma região maior
que a América do Sul. Não existe uma etiqueta regional equivalente apenas
para a América do Sul; o template usa redação neutra, sem escolher um país.
`es-ES` representa a variante de Espanha, não todos os falantes na Europa.

Cada idioma mantém seu HTML, CSS e favicon. Os links de troca de idioma
apontam para a pasta irmã. Esta pasta é a única fonte do site publicado.
Ao alterar o estilo compartilhado, atualize as cinco cópias de `styles.css`.

As correções de acessibilidade foram aplicadas somente às versões desta pasta.
Consulte o [registro de alterações e verificações](../docs/acessibilidade.md).

Para servir somente estas versões, na raiz do repositório execute:

```sh
python3 -m http.server 8001 --bind 127.0.0.1 --directory static
```

As páginas ficam em `/pt-BR/`, `/pt-PT/`, `/en/`, `/es-419/` e `/es-ES/`.
A raiz apresenta a escolha
de idioma. O servidor Python é apenas para desenvolvimento.

O workflow `.github/workflows/pages.yml` publica esta pasta no GitHub Pages.
`README.md` é documentação e é excluído do artefato de publicação.

A identificação visível `ES-SAM` distingue o espanhol sul-americano nos seletores.
É uma abreviação do projeto; `es-419` permanece como etiqueta padrão em
`lang`, `hreflang` e no caminho da página.
