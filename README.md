# Portfólio

Currículo e portfólio estático em português brasileiro e inglês, feito com
HTML e CSS, sem JavaScript. O projeto prioriza robustez, compatibilidade,
acessibilidade, portabilidade e poucas tecnologias e dependências.

## Estrutura

```text
.
├── AGENTS.md                # Regras e orientações de desenvolvimento
├── .editorconfig            # Convenções para editores compatíveis
├── .github/workflows/pages.yml # Deploy no GitHub Pages
├── static/
│   ├── index.html           # Escolha de idioma
│   ├── pt-BR/               # HTML, CSS e recursos em português
│   ├── en/                  # HTML, CSS e recursos em inglês
│   └── README.md            # Organização das versões estáticas
└── docs/
    ├── analise-estatica.md   # Análise inicial e pendências
    └── referencias/w3c/     # Documentos oficiais, licença e proveniência
```

A pasta `static/` é a única fonte do site publicado. As versões antigas foram
removidas. Cada idioma tem seu próprio CSS e favicon; alterações nesses recursos
precisam ser mantidas consistentes.

## Executar para desenvolvimento

Não há dependências de pacotes para instalar nem etapa de build.
Com Python 3 disponível, execute na raiz do repositório:

```sh
python3 -m http.server 8001 --bind 127.0.0.1 --directory static
```

A página inicial oferece a escolha de idioma; as versões ficam em `/pt-BR/`
e `/en/`. Se a porta estiver ocupada, escolha outra. Use `Ctrl+C` para encerrar.
O servidor Python é somente uma ferramenta de desenvolvimento; o site
publicado não depende de Python ou de um backend.

## Deploy no GitHub Pages

O workflow `.github/workflows/pages.yml` publica os arquivos de `static/`
a cada push em `main`, sem compilar o site. Também permite execução manual
pela aba Actions. As ações oficiais são fixadas por SHA de commit.

Em **Settings → Pages → Build and deployment → Source**, selecione
**GitHub Actions**. GitHub Actions deve estar habilitado, e o ambiente
`github-pages` deve permitir deploy da branch `main`.

O workflow usa permissões `contents: read`, `pages: write` e `id-token: write`.
Não requer secrets personalizados. O artefato exclui `static/README.md` e não
inclui documentos, referências W3C ou instruções da raiz do repositório.

Endereço do site: https://nicolas-b-t.github.io/portfolio/
As páginas de idioma ficam em `/portfolio/pt-BR/` e `/portfolio/en/`.

## Editar e verificar

Leia [AGENTS.md](AGENTS.md) antes de alterar o projeto. Edite as páginas em
`static/pt-BR/index.html` e `static/en/index.html` para trabalhar nas páginas
por idioma. Preserve a correspondência entre traduções e revise `lang`,
`hreflang` e os links de troca de idioma.

Após alterações, confira:

- Entrega das páginas, CSS e favicon por HTTP.
- Links relativos, âncoras e troca de idioma.
- Validade do HTML/CSS quando pertinente.
- Teclado, foco visível, contraste, zoom e telas pequenas para mudanças visuais.
- Temas claro e escuro, preferência por movimento reduzido e impressão.

Execute também:

```sh
git diff --check
```

Não há suíte de testes automatizados no projeto. Verificações automáticas
não substituem a avaliação manual de acessibilidade.

## Padrões e estado atual

O site deve permanecer sem scripts, frameworks, rastreadores ou widgets que
dependam de JavaScript. Use HTML semântico, CSS amplamente suportado, fontes
do sistema, recursos locais e caminhos relativos.

WCAG 2.2 nível AA é o alvo de acessibilidade, não uma certificação já obtida.
Veja a [análise inicial](docs/analise-estatica.md) para os problemas registrados.
O conteúdo ainda inclui nomes, contatos e projetos de exemplo que precisam
ser substituídos antes da publicação.

As [referências W3C](docs/referencias/w3c/README.md) são cópias documentais e
podem conter scripts originais. Preserve-as intactas e não as incorpore ao site.
Na hospedagem, publique apenas os arquivos necessários ao portfólio.

O `.editorconfig` define UTF-8, indentação de dois espaços e finais de linha
LF, com exceções para Markdown, scripts Windows e referências oficiais.
Ele não reformata arquivos automaticamente nem acrescenta dependências ao site.
