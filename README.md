# Portfólio

Este projeto apresenta o currículo e os projetos de Nicolas Beraldes Tarifa.
O site usa HTML e CSS, sem JavaScript.
As cinco versões atendem aos públicos brasileiro, português, inglês,
sul-americano e espanhol de Espanha.

Os objetivos são robustez, compatibilidade, acessibilidade, portabilidade e
minimalismo. O projeto usa poucas tecnologias e dependências.

## Regras de redação

Toda a documentação autoral e todo o texto apresentado devem seguir os
princípios da ASD-STE100, edição 9, adaptados ao idioma usado.
As [orientações do projeto](AGENTS.md) definem a regra e os critérios de revisão.

No português, usamos termos consistentes, voz ativa e frases curtas.
As instruções apresentam uma ação por frase. Os parágrafos apresentam um assunto
por vez. Esta adaptação não declara conformidade formal com STE.

A referência oficial está em
`docs/referencias/asd-ste100/ASD-STE100-issue-9-2025-01-15.pdf`.
O guia local está em `docs/guia-de-redacao.md`.
Preservamos os documentos oficiais, as licenças e as fontes recebidas sem edição.

## Estrutura

```text
.
├── AGENTS.md                    # Regras de desenvolvimento e redação
├── .editorconfig                # Formatação nos editores compatíveis
├── .github/workflows/pages.yml  # Publicação no GitHub Pages
├── static/
│   ├── index.html               # Escolha de idioma
│   ├── pt-BR/                   # Português brasileiro
│   ├── pt-PT/                   # Português de Portugal
│   ├── en/                      # Inglês
│   ├── es-419/                  # Espanhol para o público sul-americano
│   ├── es-ES/                   # Espanhol de Espanha
│   ├── media/realfort/           # Fotografias compartilhadas
│   └── README.md                # Organização das páginas
└── docs/                        # Documentação somente local
    ├── guia-de-redacao.md        # Adaptação dos princípios da ASD-STE100
    ├── analise-estatica.md       # Análise inicial
    ├── acessibilidade.md        # Alterações e verificações
    ├── fontes-do-conteudo.md    # Origem das informações profissionais
    ├── competencias-e-evidencias.md # Evidências das competências
    ├── coa-competencias.md      # Proposta de reorganização e resultado
    ├── otimizacao-imagens.json  # Dimensões, compressão e integridade
    ├── pendencias.md            # Tarefas futuras
    ├── historico-de-desenvolvimento.md # Etapas e decisões
    ├── avaliacao-do-desenvolvimento.md # Avaliação e recomendações
    ├── fontes/academico/        # PDFs do SGCS e do curso de GTI
    └── referencias/
        ├── w3c/                # Acessibilidade
        ├── asd-ste100/          # Redação técnica
        └── idiomas/            # STANAG 6001 e QECR/CEFR
```

A pasta `static/` contém o site publicado. Removemos as páginas antigas.
Cada idioma mantém seu CSS e favicon. As cinco cópias desses recursos devem
permanecer consistentes.

A pasta `docs/` fica somente neste ambiente e é ignorada pelo Git.
Seus arquivos não acompanham clones, commits ou pushes.
Os caminhos de `docs/` citados neste README identificam arquivos locais.
As instruções da raiz permanecem versionadas no GitHub.

## Executar para desenvolvimento

O site não exige instalação de pacotes nem compilação.
Com Python 3 disponível, execute este comando na raiz do repositório:

```sh
python3 -m http.server 8001 --bind 127.0.0.1 --directory static
```

Abra `http://127.0.0.1:8001/` no navegador.
A página inicial permite escolher o idioma.
As versões ficam em `/pt-BR/`, `/pt-PT/`, `/en/`, `/es-419/` e `/es-ES/`.

Se a porta estiver ocupada, escolha outra porta.
Use `Ctrl+C` para encerrar o servidor.
O servidor Python serve para desenvolvimento. O site publicado não depende de
Python ou de um servidor de aplicação.

## Publicar no GitHub Pages

O workflow `.github/workflows/pages.yml` publica `static/` após cada push em
`main`. A aba Actions também permite iniciar a publicação manualmente.
As ações oficiais usam referências fixadas por SHA de commit.

Nas configurações do repositório, abra **Settings → Pages → Build and deployment → Source**.
Selecione **GitHub Actions**.
Habilite GitHub Actions no repositório.
Permita que o ambiente `github-pages` publique a branch `main`.

O workflow usa as permissões `contents: read`, `pages: write` e `id-token: write`.
Ele não exige segredos personalizados.
O artefato exclui `static/README.md`, documentos locais e instruções da raiz.

Site: https://nicolas-b-t.github.io/portfolio/
As páginas usam o caminho `/portfolio/`, seguido da pasta de cada idioma.

## Editar e verificar

Leia [AGENTS.md](AGENTS.md) antes de editar.
A revisão atual abrange toda a documentação autoral e somente
`static/pt-BR/index.html`, conforme decisão de 9 de outubro de 2026.
As demais páginas e idiomas aguardam revisão posterior.
Os commits devem indicar o escopo “pt-BR, página principal”.

O conteúdo profissional usa currículos, certificados, relatos e confirmações
do responsável. Confira os fatos e seus limites antes de alterar o texto.
Quando uma revisão incluir traduções, confira `lang`, `hreflang` e os links
entre idiomas.

Após editar, confira:

- Entrega das páginas, CSS e favicon por HTTP.
- Links relativos, âncoras e troca de idioma.
- Validade do HTML e CSS, conforme a mudança.
- Teclado, foco, contraste, zoom e telas pequenas.
- Temas claro e escuro, movimento reduzido e impressão.
- Clareza dos textos, consistência dos termos e preservação dos fatos.

Execute este comando:

```sh
git diff --check
```

O repositório não contém uma suíte de testes automatizados.
As verificações automáticas não substituem a avaliação manual de acessibilidade
ou a revisão das informações profissionais.

## Conteúdo e padrões

O site usa HTML semântico, CSS amplamente suportado, fontes do sistema e caminhos
relativos. Ele funciona sem scripts, frameworks, rastreadores ou widgets que
exijam JavaScript.

WCAG 2.2 nível AA é o alvo de acessibilidade.
Os testes realizados não certificam conformidade com todos os critérios.
O registro local está em `docs/acessibilidade.md`.

Cada idioma contém `rede.html`, com agradecimentos e convites para conhecer
perfis, e `galeria.html`, com fotografias profissionais.
O rodapé liga essas páginas ao currículo principal.
As fotografias usam WebP e JPEG responsivos em `static/media/realfort/`.
O currículo principal não carrega fotografias.

As competências usam listas de tags em três categorias: técnicas, sociais e
habilidades práticas e operacionais. As subcategorias organizam os assuntos.
O formato é “habilidade, observação”, com observações somente quando necessárias.
Os projetos e a formação também apresentam competências no seu contexto.
O curso de GTI permanece em andamento.

As fontes estão em `docs/fontes-do-conteudo.md`.
A matriz `docs/competencias-e-evidencias.md` registra evidências e limites das
inferências. Os currículos e certificados integrais permanecem fora do projeto.
Os PDFs acadêmicos ficam somente em `docs/fontes/academico/`.
Não publique documentos privados junto com o site.

O histórico está em `docs/historico-de-desenvolvimento.md`.
A avaliação está em `docs/avaliacao-do-desenvolvimento.md`.
O acesso independente aos repositórios privados permanece pendente em
`docs/pendencias.md`.

As referências oficiais podem conter scripts originais.
Preserve as cópias e seus avisos. Publique somente os arquivos necessários ao site.

O `.editorconfig` orienta UTF-8, indentação de dois espaços e finais de linha LF.
Ele contém exceções para Markdown, scripts Windows e referências oficiais.
Ele não reformata arquivos automaticamente.

## Idiomas

O visitante escolhe o idioma, sem detecção automática ou redirecionamento.
A etiqueta `es-419` abrange América Latina e Caribe.
O projeto usa espanhol neutro para seu público sul-americano.

A marca visível `ES-SAM` facilita a identificação dessa versão.
Ela é uma abreviação do projeto. `es-419` permanece em `lang`, `hreflang` e nos caminhos.
A etiqueta `es-ES` identifica a variante de Espanha.
