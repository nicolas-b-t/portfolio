# Manutenção do portfólio

Este é o guia operacional.
As regras gerais estão em [AGENTS.md](../AGENTS.md).
O estado atual está em [Pendências](pendencias.md).
A fundamentação e o registro das fases estão em [Padrões técnicos](padroes-tecnicos.md).

## Conteúdo e idiomas

Use `static/pt-BR/index.html` como base factual.
Atualize também `pt-PT`, `en`, `es-419` e `es-ES` quando o conteúdo comum mudar.
Cada idioma mantém `index.html`, `galeria.html`, `rede.html` e `recomendacoes.html`.
Use inglês norte-americano em `en/`, com `lang` e `hreflang` definidos como `en-US`.
Em `es-419`, preserve a redação para o público sul-americano.

Confira as [fontes e atribuições](conteudo-e-fontes.md) antes de alterar competências, cargos, projetos ou formação.
Preserve as três categorias de competências e suas subcategorias.
Use uma tecnologia, competência ou qualificação por tag.
Mantenha observações de nível para suporte técnico, fusão de fibra e inglês.
Registre outras limitações nas descrições e na formação.

A cópia oculta `dados-curriculo` deriva dos dados públicos da página.
Ela não é uma entrada independente para ampliar qualificações.
Confira a coerência entre a página, o bloco oculto e a [lista de consulta](../listas-de-tags/README.md).
Os aliases auxiliam consultas específicas. Eles não garantem reconhecimento por todos os ATS.

## Página de projetos em pt-BR

Desde 02/11/2026, `static/pt-BR/projetos.html` reúne os três projetos e sua cópia estruturada.
A página principal mantém um link no menu, outro na apresentação inicial e uma referência no resumo oculto.
A âncora antiga `index.html#projetos` leva ao acesso da apresentação.
As outras variantes mantêm a estrutura anterior nesta etapa.

Para editar, use a página de projetos e confira a cópia estruturada, as atribuições em [Conteúdo e fontes](conteudo-e-fontes.md#projetos) e as listas de consulta.
A impressão da página principal mostra o currículo sem os cartões; a página de projetos permite imprimir os três cartões.
Os PDFs V3 permanecem edições históricas.
Evidência e limites do ensaio: [Verificações de 02/11/2026](historico/verificacoes.md).

## Recomendações

Use `recomendacoes.html` para divulgar projetos, iniciativas, livros e recursos selecionados pelo responsável.
A página `rede.html` mantém os agradecimentos às pessoas da rede.
Preserve o acesso às recomendações pelo menu, pela seção Contato e pelo rodapé da página principal.
O acesso junto aos contatos fica oculto na impressão do currículo.

Crie categorias somente quando houver indicações. Não publique seções vazias ou itens de exemplo.
Cada indicação usa um cartão com título, descrição curta e link descritivo para a fonte.
Nos livros, preserve o título oficial e identifique a autoria e a edição quando informadas.
Acrescente motivos pessoais para recomendar um item somente quando o responsável os fornecer.
Confira a fonte e registre o contexto em [fontes e atribuições](conteudo-e-fontes.md).
Traduza o conteúdo comum nos cinco idiomas e confira os links de troca de idioma.
Prefira o destino no idioma da página quando houver uma tradução disponível.

## Cursos e currículos

A página mantém duas cópias de tela e impressão dos cursos, além do resumo estruturado.
Quando um curso mudar, atualize suas ocorrências em cada idioma.
Preserve títulos oficiais, instituições, datas, cargas horárias e atributos de idioma.
Confira cada curso uma única vez na impressão, com o controle recolhível aberto e fechado.
As cargas horárias e a origem das datas estão em [Cursos complementares](fontes/cursos/README.md).

Os [PDFs V3](curriculos/v3/README.md) são edições identificadas, não exportações automáticas de cada alteração do site.
Ao gerar uma nova edição, confira o conteúdo, a extração textual, as margens e a paginação do DOCX e do PDF.
Atualize o manifesto da edição e mantenha somente os arquivos necessários à sua manutenção.
Os DOCX V3 estão na [pasta de currículos no Drive](https://drive.google.com/drive/folders/1v7H0YOlGlE_R9osngevcE5LquYOzcIDI).

## HTML, CSS e publicação

Todas as páginas usam `static/assets/css/styles.css`.
Calcule os caminhos relativos conforme a profundidade de cada página.
Preserve fontes do sistema, recursos locais e as imagens WebP/JPEG compartilhadas em `static/media/realfort/`.
Não adicione JavaScript, backend, frameworks, rastreadores ou etapa de build.
As convenções de HTML e CSS estão na seção 4 de [Padrões técnicos](padroes-tecnicos.md) e nos [ADRs](adr/README.md).
Antes de mudar a estrutura do site, consulte o ADR relacionado.
Uma decisão estrutural nova exige ADR novo ou atualização do status do anterior.

### Ícones Lucide em pt-BR

A pasta `static/assets/icons/` armazena 28 arquivos SVG da biblioteca Lucide Icons.
A licença com a lista de ícones derivados do Feather está em `static/assets/icons/LICENSE.txt`.
O arquivo `LICENSE` é a cópia genérica recebida.
O CSS comum alimenta os ícones por `[data-icon]::before` com `background-color: currentColor` e `mask`.
Nesta etapa, `data-icon` aparece apenas em `static/pt-BR/`.
Não altere os blocos ocultos de extração nem as demais variantes sem decisão.
Evidência e limites do ensaio: [Verificações de 02/11/2026](historico/verificacoes.md).

### Servidor local

Execute na raiz:

```sh
python3 -m http.server 8001 --bind 127.0.0.1 --directory static
```

Abra `http://127.0.0.1:8001/`.
Confira links, âncoras, troca de idioma, CSS, favicon e páginas afetadas.
Para mudanças visuais, confira teclado, foco, contraste, telas pequenas, zoom, temas e impressão.
Use validação HTML/CSS quando pertinente. Diferencie inspeção de código de ensaio em navegador.

### Publicação

O workflow `.github/workflows/pages.yml` publica somente `static/` após push em `main`.
No GitHub, a origem de publicação deve ser GitHub Actions.
As permissões mínimas do workflow são `contents: read`, `pages: write` e `id-token: write`.

## Serviço

O site é publicado pelo workflow em `https://nicolas-b-t.github.io/portfolio/`.
O HTTP redireciona para HTTPS com 301; o HSTS cobre cerca de um ano.
A página 404 fica em `static/404.html` e responde com status 404.
O cache é de 600 segundos, então a publicação pode levar alguns minutos.
A troca de idioma não é automática; o visitante escolhe na raiz.

Depois do push, confira a raiz, o redirecionamento, a 404 e a troca de idioma.
Não há SLA nem monitoramento contínuo. Incidente: resposta em até um dia.
A descrição do serviço está na seção 9 de [Padrões técnicos](padroes-tecnicos.md).

## Qualidade e testes

O processo, o checklist de acessibilidade e o plano de incidente estão nas seções 3, 5 e 8 de [Padrões técnicos](padroes-tecnicos.md).
A situação de cada verificação está em [Pendências](pendencias.md).

Antes de publicar, confira:

- o requisito ou a decisão que autoriza a mudança;
- HTML, links internos e âncoras;
- as variantes afetadas;
- teclado, foco, contraste, 320 CSS px, zoom, temas e impressão em mudança visual;
- nomes acessíveis, texto alternativo, ARIA mínimo e leitor de tela quando possível;
- a cópia estruturada e a impressão em mudança de conteúdo;
- `git diff --check`;
- `CHANGELOG.md` e a situação no plano.

Registre cada defeito com identificador, severidade, prioridade, correção e verificação.
Critérios qualitativos são avaliados pelo responsável.

## Mudanças

Toda mudança segue o procedimento da seção 10 de [Padrões técnicos](padroes-tecnicos.md).

1. Descreva o pedido, a finalidade e a fonte.
2. Analise o impacto nas variantes, páginas, links, acessibilidade, impressão e documentos.
3. Obtenha autorização do responsável antes de alterar conteúdo ou site.
4. Faça uma mudança pequena, com um propósito.
5. Verifique HTML, links internos e temas. Acrescente as verificações da fase afetada.
6. Use mensagem de commit clara, com o motivo e a fase.
7. Registre no `CHANGELOG.md` e atualize a situação no plano.
8. Depois do push, confira a página publicada.

Reversão: use `git revert` em até cinco commits. Não reescreva o histórico da `main`. Registre o motivo e o resultado. Acima de cinco commits ou em caso de conflito, pare e peça decisão ao responsável.

## Organização

Use `Get-ChildItem -Recurse -Depth 3 -Force | Where-Object { $_.FullName -notmatch '\\\.git\\' }` para revisar a estrutura antes e depois de reorganizações.
Mantenha regras gerais em `AGENTS.md`, instruções práticas neste guia e as fontes em `docs/referencias/`.
Preserve uma síntese vigente por assunto. Não acrescente planos, caches, saídas brutas ou clones de terceiros à árvore ativa.
Antes de retirar uma fonte necessária, preserve sua origem, licença e forma de recuperação.
O [histórico](historico/README.md) identifica o acervo anterior e sua recuperação.
O [índice](README.md) classifica os documentos por assunto e tipo.

Ao concluir, execute `git diff --check` e informe as verificações e suas limitações.
