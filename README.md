# Portfólio de Nicolas Beraldes Tarifa

Currículo, projetos e registros profissionais em cinco variantes linguísticas.
O site usa HTML e CSS, sem JavaScript, backend ou etapa de build.

[Site publicado](https://nicolas-b-t.github.io/portfolio/) · [PDFs V3](docs/curriculos/v3/README.md) · [Documentação](docs/README.md)

## Executar

Com Python 3 disponível, execute na raiz:

```sh
python3 -m http.server 8001 --bind 127.0.0.1 --directory static
```

Abra `http://127.0.0.1:8001/`.
As páginas ficam em `/pt-BR/`, `/pt-PT/`, `/en/`, `/es-419/` e `/es-ES/`.
Cada idioma tem currículo e portfólio, galeria, agradecimentos e uma página de recomendações (`recomendacoes.html`). Em pt-BR, `projetos.html` separa os projetos.
Use outra porta se necessário. Encerre o servidor com Ctrl+C.

## Estrutura

```text
.
├── AGENTS.md             # Regras para trabalhar no projeto
├── README.md             # Execução, estrutura e publicação
├── .github/workflows/    # Publicação no GitHub Pages
├── static/               # Site, CSS e fotografias
├── docs/                 # Guias, fontes atuais, PDFs V3 e repertório técnico local
├── listas-de-tags/      # Listas de consulta e traduções editoriais
└── dados-pessoais/       # Currículos originais e rascunhos, fora do Git
```

Use `Get-ChildItem -Recurse -Depth 3 -Force | Where-Object { $_.FullName -notmatch '\\\.git\\' }` para inspecionar a árvore completa.
As regras estão em [AGENTS.md](AGENTS.md). Os procedimentos estão em [Manutenção](docs/manutencao.md).

## Publicar e manter

O [workflow](.github/workflows/pages.yml) publica somente `static/` após push em `main`.
No GitHub, configure **Settings → Pages → Source → GitHub Actions**.
O site usa HTTPS com HSTS e o HTTP redireciona com 301.
A página 404 personalizada fica em `static/404.html`.
A disponibilidade depende do GitHub Pages e não há SLA.
Depois do push, confira a página publicada, a troca de idioma e uma URL inexistente.

Use pt-BR como base factual e sincronize o conteúdo comum nas outras variantes.
Todas as páginas compartilham `static/assets/css/styles.css`.
A documentação e os currículos em `docs/` acompanham o repositório, fora do site publicado.
`docs/repertorio-tecnico-site/` e `dados-pessoais/` ficam somente no computador e são ignorados pelo Git.

O acervo anterior foi preservado fora da árvore ativa.
Consulte o [registro da organização](docs/organizacao.md) para recuperar fontes e históricos.
