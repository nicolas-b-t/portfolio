# Organização do site

A pasta `static/` contém a fonte do site publicado.
A página `index.html` permite escolher o idioma.

| Pasta | Público ou idioma |
| --- | --- |
| `pt-BR/` | Português brasileiro |
| `pt-PT/` | Português de Portugal |
| `en/` | Inglês |
| `es-419/` | Espanhol neutro para o público sul-americano |
| `es-ES/` | Espanhol de Espanha |

Cada pasta contém o currículo em `index.html`, os agradecimentos em `rede.html` e a galeria em `galeria.html`.
O rodapé liga o currículo às páginas complementares.
As fotografias WebP e JPEG ficam em `media/realfort/`, compartilhadas pelos idiomas.
Cada idioma mantém seu HTML, CSS e favicon.
Os links de idioma apontam para as pastas vizinhas.

A etiqueta `es-419` abrange América Latina e Caribe.
A redação atende ao público sul-americano, identificado pela marca visível `ES-SAM`.
A etiqueta `es-ES` identifica a variante de Espanha.

## Manutenção e verificação

As regras gerais, o escopo editorial e a consistência dos recursos estão em [AGENTS.md](../AGENTS.md).
Consulte [a execução local](../README.md#executar-para-desenvolvimento) para servir o site.
Consulte [o relatório final](../docs/relatorio-final-verificacao-pt-br-2026-10-12.md) para repetir as verificações.

O [workflow](../.github/workflows/pages.yml) publica esta pasta no GitHub Pages.
Ele exclui este README do artefato de publicação.
