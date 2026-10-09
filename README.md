# Portfólio

Currículo e portfólio estático em português (Brasil e Portugal), inglês e
espanhol (template sul-americano e variante de Espanha), feito com
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
│   ├── pt-PT/               # Português de Portugal
│   ├── en/                  # HTML, CSS e recursos em inglês
│   ├── es-419/              # Espanhol neutro para a América do Sul
│   ├── es-ES/               # Espanhol de Espanha
│   ├── media/realfort/      # Fotos otimizadas compartilhadas
│   └── README.md            # Organização das versões estáticas
└── docs/
    ├── analise-estatica.md   # Análise inicial e pendências
    ├── acessibilidade.md    # Alterações, verificações e limites
    ├── fontes-do-conteudo.md # Fontes das informações profissionais
    ├── otimizacao-imagens.json # Dimensões e compressão das fotos
    ├── pendencias.md        # Lembrete sobre acesso aos projetos privados
    ├── historico-de-desenvolvimento.md # Etapas e decisões deste desenvolvimento
    ├── avaliacao-do-desenvolvimento.md # Avaliação e recomendações ao responsável
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

A página inicial oferece a escolha de idioma; as versões ficam em `/pt-BR/`,
`/pt-PT/`, `/en/`, `/es-419/` e `/es-ES/`. Se a porta estiver ocupada, escolha
outra. Use `Ctrl+C` para encerrar.
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
As páginas ficam sob `/portfolio/`, nas pastas de cada idioma.

## Editar e verificar

Leia [AGENTS.md](AGENTS.md) antes de alterar o projeto. Edite o `index.html`
na pasta de cada idioma em `static/`. A apresentação pessoal está em revisão,
com experiência de telecomunicações e formação complementar extraídas das fontes enviadas.
Preserve a correspondência entre traduções e revise `lang`,
`hreflang` e os links de troca de idioma.

O template sul-americano usa espanhol neutro com `es-419`, etiqueta BCP 47 que
abrange América Latina e Caribe. A variante europeia usa `es-ES` para Espanha.
Não há detecção automática de idioma ou redirecionamento: a escolha é do visitante.

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
O conteúdo profissional está sendo preenchido a partir de fontes verificáveis.
Veja [fontes e pendências](docs/fontes-do-conteudo.md). A área de agradecimentos
e recomendações está em `rede.html` em cada idioma, separada da página principal
e acessível pelo rodapé. A galeria de trabalho está em `galeria.html` em cada
idioma, com fotos WebP/JPEG responsivas compartilhadas em `static/media/realfort/`.
As fotos não são incorporadas ao currículo principal. Não publique documentos
privados junto com o site.

O [histórico do desenvolvimento](docs/historico-de-desenvolvimento.md) reúne as
etapas e decisões do projeto. A [avaliação do desenvolvimento](docs/avaliacao-do-desenvolvimento.md)
registra observações sobre as ações do responsável e recomendações práticas.
O acesso independente aos repositórios privados está anotado em
[pendências](docs/pendencias.md) para ser retomado posteriormente.

As [referências W3C](docs/referencias/w3c/README.md) são cópias documentais e
podem conter scripts originais. Preserve-as intactas e não as incorpore ao site.
Na hospedagem, publique apenas os arquivos necessários ao portfólio.

O `.editorconfig` define UTF-8, indentação de dois espaços e finais de linha
LF, com exceções para Markdown, scripts Windows e referências oficiais.
Ele não reformata arquivos automaticamente nem acrescenta dependências ao site.

A identificação visível `ES-SAM` distingue o espanhol sul-americano nos seletores.
É uma abreviação do projeto; `es-419` permanece como etiqueta padrão em
`lang`, `hreflang` e no caminho da página.
