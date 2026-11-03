# Manutenção do portfólio

Este é o guia operacional.
As regras gerais estão em [AGENTS.md](../AGENTS.md).
O estado atual está em [Requisitos](requisitos.md), §11.
O registro histórico está em [Histórico](historico/historico.md).

## Conteúdo e idiomas

Use `static/pt-BR/index.html` como base factual.
Estado atual: somente `pt-BR` e `en` são publicados. As pastas `pt-PT`, `es-419` e `es-ES` redirecionam para `static/wip.html` até a conclusão da base e da tradução.
Quando a base pt-BR estiver concluída, atualize as traduções e reative os links de idioma.
Cada variante ativa mantém `index.html`, `galeria.html`, `rede.html` e `recomendacoes.html`; em pt-BR, há também `projetos.html`.
Use inglês norte-americano em `en/`, com `lang` e `hreflang` definidos como `en-US`.
Em `es-419`, preserve a redação para o público sul-americano quando a variante for reativada.

Confira as [fontes e atribuições](conteudo-e-fontes.md) antes de alterar competências, cargos, projetos ou formação.
Preserve as três categorias de competências e suas subcategorias.
Use uma tecnologia, competência ou qualificação por tag.
Mantenha observações de nível para suporte técnico, fusão de fibra e inglês.
Registre outras limitações nas descrições e na formação.

A cópia oculta `dados-curriculo` deriva dos dados públicos da página.
Ela não é uma entrada independente para ampliar qualificações.
Confira a coerência entre a página, o bloco oculto e a [lista de consulta](listas-de-tags/README.md).
Os aliases auxiliam consultas específicas; não garantem reconhecimento por todos os ATS.

## Redação

Aplique os princípios da ASD-STE100, edição 9, aos textos autorais do projeto.
As regras gerais estão em [AGENTS.md](../AGENTS.md).
O responsável preserva a referência inglesa na cópia pessoal por restrição de reprodução.
Ela não acompanha clones.
Consulte [a origem e as condições](referencias/manifestos/asd-ste100.json).

### Escrever e revisar

1. Identifique o leitor e a finalidade do texto.
2. Escolha um termo preciso para cada conceito.
3. Use o mesmo termo nas ocorrências seguintes.
4. Prefira voz ativa e verbos diretos.
5. Identifique quem realiza cada ação.
6. Use o passado para atividades concluídas.
7. Use o presente para atividades atuais.
8. Apresente uma ação por frase de instrução.
9. Coloque a condição necessária antes da ação.
10. Revise instruções com mais de 20 palavras.
11. Revise descrições com mais de 25 palavras.
12. Apresente um assunto por parágrafo.
13. Limite cada parágrafo a seis frases.
14. Separe instruções, informações e resultados.
15. Explique siglas quando o contexto não esclarecer seu significado.
16. Preserve datas, qualificações e limites das fontes.
17. Use pontos para separar frases na prosa.
18. Revise clareza e precisão manualmente.

Nas tags, use uma tecnologia, competência ou qualificação por item.
Separe conceitos independentes. Preserve nomes oficiais que formem uma unidade.
Use “habilidade, observação” somente para suporte técnico, fusão de fibra e inglês.
Preserve outras limitações nas descrições e nos dados da formação.
Preserve identificadores técnicos como SC/APC e N1/N2.
Nomes oficiais e identificadores exigem análise contextual na contagem de palavras.
Uma contagem automática por espaços serve apenas para triagem.

### Revisar a compreensão do leitor

1. Identifique quem realiza a ação e o objeto dessa ação.
2. Troque nomes internos de equipes por funções compreensíveis, quando confirmadas.
3. Explique o contexto de palavras genéricas como materiais, serviços e sistemas.
4. Preserve termos técnicos necessários à identificação da atividade.
5. Distinga repetição útil de informação que não acrescenta fatos.
6. Confirme detalhes antes de tornar uma atividade mais específica.
7. Não substitua uma ação declarada por inspeção ou auditoria sem evidência.

As revisões anteriores estão preservadas no [registro histórico](historico/historico.md).
As orientações não substituem testes de compreensão com os leitores.
Os limites numéricos de frases são uma política editorial do projeto.

### Inglês norte-americano

Use inglês norte-americano nos textos autorais da versão en, inclusive nas tags e nos textos alternativos das imagens.
A pasta `en/` permanece igual. Use `en-US` para identificar as páginas e os links dessa versão.
Preserve os idiomas originais dos títulos oficiais de cursos e das citações.

| Forma britânica | Forma adotada |
| --- | --- |
| Fibre-optic | Fiber optic |
| Fibres | Fibers |
| Modelling | Modeling |
| Organisation | Organization |
| Organised | Organized |
| Optimisation | Optimization |
| Analysed | Analyzed |
| Prioritise | Prioritize |
| Licence | License |
| Programme | Program |

Preserve qualificações como learner e os níveis de suporte ao revisar as tags.
Não altere nomes oficiais, documentos recebidos ou resultados históricos para aplicar esta preferência editorial.
A grafia escolhida não garante reconhecimento por todos os sistemas ATS.

### Revisão editorial e acessibilidade

Antes de publicar um texto, confira:

- um termo para cada conceito;
- variações de ATS apenas quando houver justificativa registrada;
- frases de descrição com no máximo 25 palavras;
- grafia norte-americana em `en/`;
- nomes oficiais, datas e níveis preservados;
- texto alternativo e nome compreensível para links e controles;
- teclado, foco, contraste, 320 CSS px, zoom, temas e impressão.

Registre cada achado na lista vigente de [Requisitos](requisitos.md), §11.
Não declare conformidade com a WCAG ou com o STE100.

### Limites

A adaptação preserva a gramática portuguesa.
Ela não constitui tradução oficial ou certificação STE.
O dicionário inglês não define palavras aprovadas em português.
Preserve documentos oficiais, licenças, fontes recebidas e citações literais.
Não corrija os erros de uma amostra de avaliação dentro da citação original.
Aplique a revisão aos comentários e às instruções que escrevemos sobre essas fontes.

## Página de projetos em pt-BR

Desde 02/11/2026, `static/pt-BR/projetos.html` reúne os três projetos e sua cópia estruturada.
A página principal mantém um link no menu, outro na apresentação inicial e uma referência no resumo oculto.
A âncora antiga `index.html#projetos` leva ao acesso da apresentação.
As outras variantes mantêm a estrutura anterior nesta etapa.

Para editar, use a página de projetos e confira a cópia estruturada, as atribuições em [Conteúdo e fontes](conteudo-e-fontes.md#projetos) e as listas de consulta.
A impressão da página principal mostra o currículo sem os cartões; a página de projetos permite imprimir os três cartões.
Os PDFs V3 permanecem edições históricas.
Evidência e limites: [Histórico](historico/historico.md).

## Recomendações

Use `recomendacoes.html` para divulgar projetos, iniciativas, livros e recursos selecionados pelo responsável.
A página `rede.html` mantém os agradecimentos às pessoas da rede.
Preserve o acesso às recomendações pelo menu, pela seção Contato e pelo rodapé da página principal.
O acesso junto aos contatos fica oculto na impressão do currículo.

Crie categorias somente quando houver indicações. Não publique seções vazias ou itens de exemplo.
Cada indicação usa um cartão com título, descrição curta e link descritivo para a fonte.
Nos livros, preserve o título oficial e identifique a autoria e a edição quando informadas.
Acrescente motivos pessoais para recomendar um item somente quando o responsável os fornecer.
Confira a fonte e registre o contexto em [Conteúdo e fontes](conteudo-e-fontes.md).
Traduza o conteúdo comum nos idiomas ativos e confira os links de troca de idioma.
Quando as demais variantes forem reativadas, retome a tradução a partir da base pt-BR.
Prefira o destino no idioma da página quando houver uma tradução disponível.

## Cursos e currículos

A página mantém duas cópias de tela e impressão dos cursos, além do resumo estruturado.
Quando um curso mudar, atualize suas ocorrências nos idiomas ativos.
Preserve títulos oficiais, instituições, datas, cargas horárias e atributos de idioma.
Confira cada curso uma única vez na impressão, com o controle recolhível aberto e fechado.
As cargas horárias e a origem das datas estão em [Cursos](conteudo-e-fontes.md#cursos-complementares).

Os [PDFs V3](curriculos/v3/README.md) são edições identificadas, não exportações automáticas de cada alteração do site.
Ao gerar uma nova edição, confira o conteúdo, a extração textual, as margens e a paginação do DOCX e do PDF.
Atualize o manifesto da edição e mantenha somente os arquivos necessários.
Os DOCX V3 estão na [pasta de currículos no Drive](https://drive.google.com/drive/folders/1v7H0YOlGlE_R9osngevcE5LquYOzcIDI).

## HTML, CSS e publicação

Todas as páginas usam `static/assets/css/styles.css`.
Calcule os caminhos relativos conforme a profundidade de cada página. A página 404 é a exceção: usa caminhos absolutos sob `/portfolio/` para funcionar em URLs aninhadas.
Preserve fontes do sistema, recursos locais e as imagens WebP/JPEG em `static/media/realfort/`.
Não adicione JavaScript, backend, frameworks, rastreadores ou etapa de build.

Convenções de HTML:

- UTF-8 e `lang` correto em cada página.
- `hreflang` recíproco entre as variantes ativas.
- Elementos semânticos: `header`, `nav`, `main`, `section`, `footer`.
- Um `h1` por página e hierarquia sem saltos.
- Caminhos relativos, exceto na página 404.
- Sem `style` embutido, `<script>`, `<form>` ou `<iframe>`.
- Toda imagem tem `alt`; a galeria usa `figure` e `figcaption`.
- A cópia estruturada usa `hidden` e dados iguais aos da tela.

Convenções de CSS:

- Um arquivo comum, com classes descritivas em kebab-case.
- Propriedades customizadas para cores e medidas.
- Media queries por largura, tema e impressão.
- Foco visível, contraste e `prefers-reduced-motion`.
- Sem framework e sem pré-processador.

Antes de mudar a estrutura do site, consulte [Decisões](decisoes.md).
Uma decisão estrutural nova exige uma decisão registrada.

### Ícones Lucide em pt-BR

A pasta `static/assets/icons/` armazena 28 SVGs da biblioteca Lucide Icons.
A licença com a lista de ícones derivados do Feather está em `static/assets/icons/LICENSE.txt`.
O arquivo `LICENSE` é a cópia genérica recebida.
O CSS comum alimenta os ícones por `[data-icon]::before` com `background-color: currentColor` e `mask`.
Nesta etapa, `data-icon` aparece apenas em `static/pt-BR/`.
Não altere os blocos ocultos de extração nem as demais variantes sem decisão.

### Servidor local

Execute na raiz:

```sh
python3 -m http.server 8001 --bind 127.0.0.1 --directory static
```

Abra `http://127.0.0.1:8001/`.
Confira links, âncoras, troca de idioma, CSS, favicon e páginas afetadas.
Para mudanças visuais, confira teclado, foco, contraste, telas pequenas, zoom, temas e impressão.
Diferencie inspeção de código de ensaio em navegador.

### Publicação

O workflow `.github/workflows/pages.yml` publica somente `static/` após push em `main`.
No GitHub, a origem de publicação deve ser GitHub Actions.
As permissões mínimas são `contents: read`, `pages: write` e `id-token: write`.

## Serviço

O site é publicado em `https://nicolas-b-t.github.io/portfolio/`.
O HTTP redireciona para HTTPS com 301; o HSTS cobre cerca de um ano.
A página 404 fica em `static/404.html` e responde com status 404.
O cache é de 600 segundos; a publicação pode levar alguns minutos.
A troca de idioma não é automática; o visitante escolhe na raiz.

Depois do push, confira a raiz, o redirecionamento, a 404 e a troca de idioma.
Não há SLA nem monitoramento contínuo. Incidente: resposta em até um dia.

## Qualidade e testes

### Antes de publicar

- Confira o requisito ou a decisão que autoriza a mudança.
- Verifique HTML, links internos e âncoras.
- Confira as variantes afetadas.
- Em mudança visual, verifique teclado, foco, contraste, 320 CSS px, zoom, temas e impressão.
- Confira nomes acessíveis, texto alternativo, ARIA mínimo e leitor de tela quando possível.
- Em mudança de conteúdo, confira a cópia estruturada e a impressão.
- Execute `git diff --check`.
- Atualize o `CHANGELOG.md` e a situação em [Requisitos](requisitos.md), §11.

### Definition of Done

Uma mudança termina quando todos os itens aplicáveis estão atendidos.

| Área | Critério |
| --- | --- |
| Autorização | Pedido e aprovação registrados. |
| Escopo | Arquivos e páginas afetados identificados. |
| Conteúdo | Fatos com fonte; variantes sincronizadas ou lacuna registrada. |
| Estrutura | HTML semântico, títulos, links internos e âncoras conferidos. |
| Acessibilidade | Teclado, foco, contraste, 320 CSS px, zoom, temas e impressão conferidos quando aplicável. |
| Cópia oculta | Dados iguais aos da tela; ausente na impressão. |
| Publicação | Workflow e permissões conferidos; página publicada aberta. |
| Documentação | Requisitos, este guia e `CHANGELOG` atualizados. |
| Texto | `git diff --check` limpo. |
| Qualidade | Critérios qualitativos avaliados pelo responsável. |

### Defeitos

Registre identificador, data, título, ambiente, contexto, passos, resultado esperado, resultado obtido, severidade, prioridade, situação, causa, correção e verificação.

Severidade: S1 bloqueia o uso; S2 afeta conteúdo ou acesso relevante; S3 afeta documentação ou apresentação; S4 é cosmético.
Prioridade: P1 corrige antes de publicar; P2 corrige na mesma fase; P3 entra no backlog; P4 pode ser aceito.
Fluxo: aberto, em análise, corrigido, em confirmação, fechado.

## Segurança

Controles atuais:

- 2FA e proteção da `main`: pendentes (P-07).
- Apenas o responsável é administrador; alterações na `main` exigem autorização.
- Workflow com permissões mínimas e ações fixadas por SHA.
- Nenhum segredo no repositório.
- `dados-pessoais/` e a base local fora do Git.
- Licença dos ícones preservada.
- Backups: RAR da v1; base técnica arquivada em `_arquivo/`; cópia externa pendente (P-08).
- Página 404 publicada.
- Cópia limpa sem dados pessoais planejada.
- Sem teste de intrusão, análise de dependências ou auditoria externa.

### Incidente

**Detecção:** commit não reconhecido, alteração visual, falha de TLS, link malicioso ou relato de terceiro.

**Contenção:** reverter o commit suspeito com `git revert`; despublicar o site se o conteúdo estiver exposto; encerrar sessões e trocar a senha; revogar tokens e chaves.

**Erradicação:** identificar a via de acesso, corrigir a causa e ativar o 2FA.

**Recuperação:** publicar a partir de um commit conhecido e conferir as páginas.

**Comunicação:** informar o responsável em até um dia.

**Registro:** anotar causa, ações, commits e verificação no `CHANGELOG`.

## Mudanças

1. Descreva o pedido, a finalidade e a fonte.
2. Analise o impacto nas variantes, páginas, links, acessibilidade, impressão e documentos.
3. Obtenha autorização do responsável antes de alterar conteúdo ou site.
4. Faça uma mudança pequena, com um propósito.
5. Verifique HTML, links internos e temas; acrescente as verificações da área afetada.
6. Use mensagem de commit clara, com o motivo.
7. Registre no `CHANGELOG.md` e atualize a situação em [Requisitos](requisitos.md), §11.
8. Depois do push, confira a página publicada.

Reversão: use `git revert` em até cinco commits.
Não reescreva o histórico da `main`.
Registre o motivo e o resultado.
Acima de cinco commits ou em caso de conflito, pare e peça decisão ao responsável.

## Organização

Use `Get-ChildItem -Recurse -Depth 3 -Force | Where-Object { $_.FullName -notmatch '\\\.git\\' }` para revisar a estrutura antes e depois de reorganizações.
Mantenha regras gerais em `AGENTS.md`, instruções práticas neste guia e fontes em `docs/referencias/`.
Preserve uma síntese vigente por assunto.
Não acrescente planos, caches, saídas brutas ou clones de terceiros à árvore ativa.
Antes de retirar uma fonte necessária, preserve origem, licença e forma de recuperação.
O [histórico](historico/historico.md) identifica o acervo anterior e sua recuperação.
O [índice](README.md) classifica os documentos.

Ao concluir, execute `git diff --check` e informe as verificações e suas limitações.
