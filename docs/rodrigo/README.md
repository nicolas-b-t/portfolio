# Portfólio de Rodrigo

Esta adaptação está na branch `rodrigo`.
A página de Rodrigo está em `static/pt-BR/index.html`.
Ela usa o CSS existente e funciona sem JavaScript.

- [Currículo e experiência acrescentada](curriculo.md).
- [Currículo original em PDF](curriculo-rodrigo-2026.pdf).

O PDF original permanece intacto. A experiência de PMO está no documento Markdown e na página.
O termo “presente” da plataforma de jogos foi preservado conforme a fonte.
As demais páginas e idiomas ainda contêm o portfólio original de Nicolas.
A página de Rodrigo não oferece links para essas páginas ou fotografias.
A entrada do site aponta para a página de Rodrigo.
Os documentos anteriores registram o projeto original e não são evidências da trajetória de Rodrigo.

## Verificação local

Na raiz do checkout, execute:

```sh
python3 -m http.server 8002 --bind 127.0.0.1 --directory static
```

Confira a página `/pt-BR/` e o arquivo `/pt-BR/styles.css`.

## Resultados de verificação

- Resposta HTTP 200 na entrada e na página em pt-BR.
- CSS e links locais acessíveis por HTTP.
- Âncoras internas presentes.
- Nenhum script ou manipulador de eventos na página nova.
- Nome, experiência de PMO e período conferidos na página.
- PDF copiado com hash SHA-256 idêntico ao original.
- `git diff --check` sem erros.

Não foi realizada inspeção visual em navegador, nem certificação de acessibilidade.
As alterações permanecem locais. Não houve publicação ou envio ao GitHub.
