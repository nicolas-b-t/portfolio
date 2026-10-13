# Portfólio

Este projeto apresenta o currículo e os projetos de Nicolas Beraldes Tarifa.
O site usa HTML e CSS, sem JavaScript, pacotes de execução ou compilação.
Ele oferece versões em pt-BR, pt-PT, inglês, es-419 e es-ES.

## Orientações e documentação

Leia [AGENTS.md](AGENTS.md) antes de editar.
Esse arquivo centraliza regras de desenvolvimento, redação, acessibilidade, escopo e trabalho no repositório.
O projeto permanece pessoal. A documentação prepara uma futura distribuição como template.
A cópia genérica ainda não foi criada.

- [Guia de uso e manutenção](docs/referencias/guia-de-uso.md): edição, consulta aos dicionários e preparação do template futuro.
- [Índice da documentação](docs/README.md): registros, fontes e referências locais.
- [Relatório final de verificação](docs/relatorio-final-verificacao-pt-br-2026-10-12.md): resultados, limites e procedimento para repetir os testes.
- [Insumos de competências](docs/referencias/guia-de-uso.md#insumos-ats-e-classificações): dicionários, originais, licenças e limites.
- [Guia de redação](docs/guia-de-redacao.md): aplicação dos princípios da ASD-STE100.

## Estrutura

```text
.
├── AGENTS.md                    # Regras gerais
├── README.md                    # Apresentação, execução e publicação
├── .editorconfig                # Formatação nos editores compatíveis
├── .github/workflows/pages.yml  # Publicação no GitHub Pages
├── static/                      # Fonte do site publicado
│   ├── index.html               # Escolha de idioma
│   ├── pt-BR/
│   ├── pt-PT/
│   ├── en/
│   ├── es-419/
│   ├── es-ES/
│   └── media/realfort/           # Fotografias compartilhadas
└── docs/                        # Documentação, evidências e fontes
    ├── README.md                # Índice
    ├── fontes/academico/        # Documentos acadêmicos
    └── referencias/             # Normas, redação, idiomas e acervo ATS
```

A documentação acompanha o repositório, mas não integra o site publicado.
Os documentos privados preservados pelo responsável não acompanham clones.
Consulte [referências locais](docs/README.md#referências-locais) para conhecer as condições de recuperação.

## Organização do site

Cada pasta de idioma contém o currículo em index.html, os agradecimentos em rede.html e a galeria em galeria.html.
O rodapé liga o currículo às páginas complementares.
Cada idioma mantém seu HTML, CSS e favicon. Os links de idioma apontam para as pastas vizinhas.
As fotografias WebP e JPEG ficam em static/media/realfort/, compartilhadas pelos idiomas.

A etiqueta es-419 abrange América Latina e Caribe.
A redação atende ao público sul-americano, identificado pela marca visível ES-SAM.
A etiqueta es-ES identifica a variante de Espanha.

## Executar para desenvolvimento

Com Python 3 disponível, execute na raiz:

```sh
python3 -m http.server 8001 --bind 127.0.0.1 --directory static
```

No Windows, use o executável Python instalado se `python3` não estiver disponível.
Abra `http://127.0.0.1:8001/` no navegador.
A página inicial permite escolher o idioma.
As versões ficam em `/pt-BR/`, `/pt-PT/`, `/en/`, `/es-419/` e `/es-ES/`.
Se a porta estiver ocupada, escolha outra porta.
Encerre o servidor com Ctrl+C.
O servidor Python serve apenas para desenvolvimento.

## Publicar no GitHub Pages

O [workflow](.github/workflows/pages.yml) publica `static/` após cada push em `main`.
A aba Actions também permite iniciar a publicação manualmente.
As ações oficiais usam referências fixadas por SHA de commit.

1. Abra **Settings → Pages → Build and deployment → Source**.
2. Selecione **GitHub Actions**.
3. Habilite GitHub Actions no repositório.
4. Permita que o ambiente `github-pages` publique a branch `main`.

O workflow usa `contents: read`, `pages: write` e `id-token: write`.
Ele não exige segredos personalizados.
O artefato contém somente os arquivos de `static/`.
A documentação e as instruções da raiz permanecem fora da publicação.

[Site publicado](https://nicolas-b-t.github.io/portfolio/).
As páginas usam `/portfolio/`, seguido da pasta de cada idioma.

## Verificação

As verificações exigidas estão em [AGENTS.md](AGENTS.md#verificação-e-trabalho-no-repositório).
O [relatório final](docs/relatorio-final-verificacao-pt-br-2026-10-12.md) descreve os ensaios e suas evidências.
O [relatório dos cinco idiomas](docs/relatorio-sincronizacao-idiomas-2026-10-13.md) registra a sincronização posterior de currículo, galeria e agradecimentos.
O [relatório de adequação ATS](docs/relatorio-adequacao-termos-ats-2026-10-13.md) registra a nomenclatura aplicada nos cinco currículos.
O [relatório de organização das tags](docs/relatorio-organizacao-tags-2026-10-13.md) registra a compactação posterior.
WCAG 2.2 nível AA é o alvo. A conformidade integral ainda não foi demonstrada.

## Distribuição futura como template

O [guia de uso](docs/referencias/guia-de-uso.md#preparar-a-distribuição-futura-como-template) identifica conteúdo pessoal, recursos e documentação que precisarão de revisão.
Ele também descreve a preparação da cópia genérica e das instruções de personalização.
Os dados pessoais do portfólio atual não foram substituídos nesta organização documental.
