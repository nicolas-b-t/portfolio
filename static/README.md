# Páginas por idioma

A pasta `static/` contém o site publicado.
A página `index.html` permite escolher o idioma.

| Pasta | Público ou idioma |
| --- | --- |
| `pt-BR/` | Português brasileiro |
| `pt-PT/` | Português de Portugal |
| `en/` | Inglês |
| `es-419/` | Espanhol neutro para o público sul-americano |
| `es-ES/` | Espanhol de Espanha |

Cada pasta contém o currículo em `index.html`, os agradecimentos em `rede.html`
e a galeria em `galeria.html`. O rodapé liga o currículo às páginas separadas.
As fotografias WebP e JPEG ficam em `media/realfort/`, compartilhadas pelos idiomas.
Não duplique as fotografias por idioma.

Cada idioma mantém seu HTML, CSS e favicon.
Os links de idioma apontam para as pastas vizinhas.
Ao alterar o estilo comum, atualize as cinco cópias de `styles.css`.

A etiqueta `es-419` abrange América Latina e Caribe.
Não existe uma etiqueta regional equivalente apenas para a América do Sul.
A redação é neutra, sem escolher um país.
A marca visível `ES-SAM` identifica o público sul-americano.
A etiqueta `es-ES` identifica a variante de Espanha.

## Redação e escopo

Siga os princípios da ASD-STE100, edição 9, adaptados ao idioma do texto.
Consulte [AGENTS.md](../AGENTS.md) para os critérios.
A revisão atual inclui toda a documentação autoral e somente
`pt-BR/index.html`. As demais páginas e idiomas aguardam revisão posterior.

Aplicamos as correções de acessibilidade somente às versões em `static/`.
O registro está em `docs/acessibilidade.md`, relativo à raiz do repositório.
A pasta `docs/` é somente local e não acompanha clones.

## Conferir as páginas

Na raiz do repositório, execute este comando:

```sh
python3 -m http.server 8001 --bind 127.0.0.1 --directory static
```

Abra `http://127.0.0.1:8001/` no navegador.
As versões ficam em `/pt-BR/`, `/pt-PT/`, `/en/`, `/es-419/` e `/es-ES/`.
O servidor Python serve apenas para desenvolvimento.

O workflow `.github/workflows/pages.yml` publica esta pasta no GitHub Pages.
Ele exclui este README do artefato de publicação.
