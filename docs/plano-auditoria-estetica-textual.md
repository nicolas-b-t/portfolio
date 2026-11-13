# Auditoria estética e textual e plano de otimização

Auditoria realizada em 12/11/2026. Este documento reúne método, evidências, achados e a sequência de melhorias proposta. As páginas do site não foram alteradas nesta etapa.

## Base disponível

O acervo principal está no `REPERTORIO_TECNICO`, fora do Git e fora de `static/`. Os caminhos abaixo são relativos à raiz desse repertório; os identificadores constam em `catalogo-comum.json`.

| Fonte | Cópia disponível e consulta realizada | Aplicação à auditoria |
| --- | --- | --- |
| Steve Krug, *Don't Make Me Think, Revisited*, 3ª edição, 2014 (`REF-0401`) | Livro integral em `04_ENGENHARIA_DE_SOFTWARE_E_MODELAGEM/04_DESENVOLVIMENTO_WEB/06_DESIGN_E_USABILIDADE/02_DONT_MAKE_ME_THINK/Steve Krug - Dont Make Me Think Revisited (EN) - 3a edicao.pdf`. Consultados os capítulos 2, 3, 5, 6, 7 e 9, especialmente as páginas 39, 48, 65, 77, 83, 114 e 141 do PDF. | Verificar leitura rápida, hierarquia, nomes de links, navegação, apresentação inicial, economia de texto e tarefas reais de leitura. |
| Ellen Lupton, *Thinking with Type*, 2ª edição revista e ampliada, 2010 (`REF-0406`) | Livro integral em `04_ENGENHARIA_DE_SOFTWARE_E_MODELAGEM/04_DESENVOLVIMENTO_WEB/06_DESIGN_E_USABILIDADE/Ellen Lupton - Thinking with Type (EN) - 2a edicao.pdf`. Consultadas as seções *Line Spacing*, *Alignment*, *Marking Paragraphs*, *Hierarchy*, *Long Lists*, *Single-Column Grid*, *Multicolumn Grid* e *Editing*, páginas 108, 112, 126, 132, 146, 178, 180 e 212 do PDF. | Examinar entrelinha, alinhamento, separação de parágrafos, níveis de título, listas extensas, colunas e consistência editorial. |
| Lynch e Horton, *Web Style Guide*, 4ª edição online (`REF-0400`) | Coleção local de 15 páginas HTML, indexada no repertório. Consultados os capítulos 7 (*Interface Design*), 8 (*Graphic Design*), 9 (*Typography*) e 10 (*Editorial Style*). | Complementar navegação, composição visual, tipografia e estilo editorial. |
| ASD-STE100, edição 9; [Manutenção, seção Redação](manutencao.md) | A cópia da referência é privada; a política editorial aplicável está documentada no projeto. | Revisar textos autorais quanto a clareza, terminologia, agente da ação, tempo verbal e extensão, preservando fatos e nomes oficiais. |
| W3C WCAG 2.2 e WCAG-EM 2.0 (`REF-0404`) | Cópias locais e fontes oficiais já catalogadas. | Definir critérios de acessibilidade e registrar amostra, método, evidências e limites da avaliação; nenhum resultado automático isolado implica conformidade. |
| [Europass](referencias/README.md#europass) e [Conteúdo e fontes](conteudo-e-fontes.md) | Orientações oficiais e base factual do projeto; `REF-0405` tem cópias das páginas de criação de CV em português e inglês. | Conferir apresentação de experiência, formação e competências sem ampliar ou mudar atribuições. |

`REF-0403` é apenas a página editorial de *Thinking with Type*, 3ª edição; não deve ser citada como se o livro integral estivesse disponível. `REF-0402` contém material parcial de *Content Design*, 2ª edição. Pode apoiar a identificação das necessidades do leitor, mas o plano não atribui recomendações a capítulos não disponíveis. As páginas citadas dos PDFs são páginas físicas dos arquivos, para permitir localizar o trecho mesmo quando a paginação impressa divergir.

## Escopo, ambiente e método

- **Linha de base:** checkout `387d529`. Antes da auditoria, `git status --short` mostrava `docs/README.md` modificado, este documento ainda não rastreado e dois rascunhos de currículo V4 não rastreados. Todas essas alterações foram preservadas. `git diff -- static` estava vazio.
- **Páginas:** cinco de `static/pt-BR/`, quatro de `static/en/`, raiz, 404 e `wip.html`. As doze páginas das variantes suspensas foram conferidas quanto ao redirecionamento, sem avaliar traduções inativas.
- **Navegador:** navegador interno do ChatGPT na versão publicada `https://nicolas-b-t.github.io/portfolio/`; versão e motor não informados. Larguras de 320, 768 e 1280 CSS px, altura de 900 CSS px e preferência de cor clara. Foram inspecionadas capturas da abertura e das páginas de projetos, galeria, rede, recomendações, seleção de idioma, 404 e preparação. O código do checkout foi comparado com os elementos observados.
- **Percursos:** abertura → projetos; abertura → contato; navegação para experiência e formação; projetos em inglês; acesso a galeria e recomendações; seleção de idioma e recuperação de uma URL inexistente. O botão de baixar currículo está desativado por decisão FR-08 e não foi registrado como defeito.
- **Método:** inspeção editorial e visual baseada nas obras acima; verificação de DOM e caminhos em todas as páginas; teclado e foco na página principal; comparação entre tela, bloco oculto e cópia para impressão dos cursos. A organização de escopo, amostra e limites segue a estrutura da WCAG-EM 2.0, mas esta não é uma avaliação integral de todos os critérios da WCAG.

## Resultados verificados

- Nas 36 combinações de página e largura (12 × 3), `scrollWidth` não superou a largura do viewport. Nenhum `h1` visível faltou; não foram encontrados saltos na hierarquia visível de cabeçalhos, âncoras internas sem alvo, imagens sem `alt` ou links sem nome detectável no DOM.
- Os percursos testados chegaram a `pt-BR/projetos.html`, `pt-BR/index.html#contato` e `en/index.html#projects`. O link de salto recebeu foco pelo teclado e levou o foco a `main`. O foco teve contorno visível; o primeiro `details` de competências abriu e revelou seus itens.
- Nas duas páginas curriculares, títulos e datas dos 17 cursos coincidem entre resumo oculto, tela e cópia para impressão. Os títulos das experiências coincidem entre resumo oculto e tela: cinco em `pt-BR`, três em `en`. Os contatos das duas cópias também coincidem dentro de cada idioma.
- Os arquivos das variantes suspensas contêm o redirecionamento para `wip.html`; o destino foi observado no navegador para as três páginas iniciais. Uma URL inexistente exibiu a página 404 própria com o CSS carregado. As imagens iniciais da galeria carregaram; as demais usam carregamento diferido e não foram todas abertas individualmente.
- As cores declaradas no CSS têm, por cálculo, contraste de 5,77:1 para o acento sobre o fundo claro e 7,92:1 sobre o fundo escuro; o texto dos botões tem 5,88:1 no tema claro e 7,92:1 no escuro. Isso verifica essas combinações de tokens, não todos os estados e componentes. O CSS inclui regras para tema escuro, impressão e movimento reduzido.

## Matriz de achados

As escalas S1–S4 e P1–P4 seguem [Manutenção](manutencao.md#defeitos). As evidências abaixo distinguem problemas confirmados de hipóteses de usabilidade.

| ID | Estado, evidência e consequência | Fundamento | Severidade / prioridade | Proposta e critério de aceitação |
| --- | --- | --- | --- | --- |
| A-01 | **Confirmado; já registrado em P-16.** `pt-BR/index.html` apresenta cinco experiências e 18 subcategorias de competências; `en/index.html` apresenta três experiências e 17 subcategorias. Faltam em `en` Aquecedores e Piscinas Mairiporã, JH Eletrônico e tráfego pago; a seção About também não acompanha o Perfil atual. O leitor em inglês recebe histórico profissional incompleto. | FR-03; [Conteúdo e fontes](conteudo-e-fontes.md); Krug, capítulos 2 e 3. | S2 / P2 | Sincronizar fatos e estrutura aprovados, com tradução en-US, sem inferir vínculo ou experiência. Aceitar quando `en` apresentar os cinco cargos e a subcategoria correspondente, e quando tela, bloco oculto, cursos e resumo editorial coincidirem. |
| A-02 | **Confirmado.** Em `static/404.html`, o link “Outros idiomas em preparação / Other languages in preparation” herda `pt-BR` integralmente. Em `static/wip.html`, ocorre o mesmo com “Voltar à seleção de idioma / Back to language selection”. A parte inglesa pode ser pronunciada como português por tecnologia assistiva. | WCAG 2.2, critério 3.1.2; AGENTS.md. | S2 / P2 | Marcar cada trecho inglês com `lang="en-US"` dentro do link, preservando o texto português e o destino. Aceitar quando o DOM expuser a mudança de idioma sem alterar nome, foco ou navegação do link. |
| A-03 | **Confirmado.** Nas páginas 404 e de preparação, o botão abaixo de `.language-options` começa exatamente no limite inferior dos botões de idioma: distância vertical de 0 CSS px a 768 px de largura. Bordas e sombras se encostam, dificultando separar escolha de idioma e ação secundária. | Lupton, *Hierarchy* (p. 132) e *Single-Column Grid* (p. 178); *Web Style Guide*, capítulos 7 a 9. | S3 / P3 | Acrescentar espaço vertical entre `.language-options` e o parágrafo seguinte, mantendo o espaçamento horizontal existente. Aceitar com separação visual clara e sem transbordamento a 320, 768 e 1280 CSS px nos temas claro e escuro. |
| A-04 | **Confirmado; dependência documental.** [Conteúdo e fontes](conteudo-e-fontes.md#experiencia-profissional) ainda afirma que o local da RealFort “não aparece (P-17)”, mas o mesmo documento registra confirmação posterior de São Paulo e a página o exibe. A contradição pode orientar uma revisão factual futura de forma incorreta. | Base factual do projeto; P-17. | S3 / P3 | Retirar a afirmação vencida e conservar a origem da confirmação do responsável. Aceitar quando documentação e página concordarem, sem alterar o fato publicado. |
| A-05 | **Confirmado; oportunidade editorial.** Os quatro cartões de `rede.html` repetem, em `pt-BR` e `en`, as mesmas duas frases genéricas de agradecimento e indicação do LinkedIn. A repetição ocupa espaço sem distinguir cada pessoa; nomes e links já identificam os perfis. | Krug, capítulo 5; *Web Style Guide*, capítulo 10; [Manutenção](manutencao.md). | S3 / P3 | Concentrar o agradecimento geral na introdução e conservar, em cada cartão, nome e link descritivo. Só acrescentar motivo individual quando o responsável o fornecer. Aceitar quando as quatro pessoas e seus destinos permanecerem corretos nos dois idiomas, com menos texto repetido. |

### Hipóteses para validação com leitores

- **Localização de recomendações:** o menu e o título usam “Minha seleção”, enquanto o conteúdo é apresentado como uma iniciativa recomendada. Testar se visitantes encontram a recomendação por esse rótulo antes de propor uma troca; não há falha de tarefa observada com leitor externo.
- **Densidade na página curricular:** em 320 CSS px, há 18 subcategorias e 76 tags de competência expostas inicialmente; a seção de experiência começa por volta de 5.507 px do topo. O menu oferece acesso direto à experiência. Medir se essa ordem prejudica o percurso antes de mudar a hierarquia ou ocultar conteúdo factual.

## Plano de otimização ordenado

1. **P2 — completar `en` (A-01/P-16).** Preparar tradução dos dois cargos, da subcategoria e do Perfil com base em `pt-BR` e [Conteúdo e fontes](conteudo-e-fontes.md). Conferir responsabilidades individuais, níveis, datas, cópia oculta, lista de consulta e impressão; não reproduzir automaticamente a separação de projetos, que é uma decisão estrutural anterior.
2. **P2 — marcar idiomas nas páginas auxiliares (A-02/P-20).** Alterar somente os dois rótulos bilíngues. Conferir o idioma no DOM, o nome acessível completo, teclado e foco.
3. **P3 — separar os controles (A-03/P-21).** Ajustar o CSS comum para dar margem ao parágrafo após `.language-options`, verificando raiz, 404 e preparação em três larguras, dois temas e foco.
4. **P3 — reconciliar a fonte factual (A-04/P-22).** Atualizar a frase vencida de `docs/conteudo-e-fontes.md` e conferir o registro histórico de P-17. Manter o local publicado, já confirmado pelo responsável.
5. **P3 — condensar os agradecimentos (A-05/P-23).** Preservar os quatro nomes e links, transferir a gratidão geral para a abertura e revisar `pt-BR` e `en` em conjunto. Não inventar motivos individuais.
6. **Após os itens confirmados:** observar, se houver participantes disponíveis, tarefas curtas de localizar recomendações e experiência. Só propor mudança de nome ou ordem após registrar o resultado. Sem participantes, manter as duas hipóteses identificadas como avaliação especializada.

Antes de implementar qualquer item, conferir o estado do Git e preservar as decisões factuais existentes. As mudanças futuras devem manter HTML/CSS estáticos, fontes do sistema, recursos locais, caminhos relativos e somente `pt-BR` e `en` como variantes ativas. Cada mudança visual deve passar por teclado, foco, contraste, telas pequenas, zoom, temas e impressão.

## Verificação das correções locais

Aplicação e verificação no checkout em 12/11/2026, antes do push para `main`. A matriz acima conserva as evidências da auditoria; o estado das correções é registrado aqui.

| Achado | Estado e evidência de correção |
| --- | --- |
| A-01 / P-16 | Corrigido no conteúdo local. `en/index.html` tem cinco experiências, com títulos, datas e descrições iguais entre tela e cópia oculta; as 18 subcategorias também aparecem nos dois blocos. A nova subcategoria tem 24 competências correspondentes entre tela e cópia oculta. As cinco fichas mostram empresa, período e local; o Perfil inglês acompanha os dois parágrafos da base brasileira. A lista de consulta `pt-BR` foi alinhada ao Perfil, aos contatos e aos metadados das experiências. |
| A-02 / P-20 | Corrigido no HTML local. Os dois links preservam texto e destino, com um `span lang="en-US"` para a parte inglesa. A marcação foi conferida no DOM; a leitura por leitor de tela não foi ensaiada. |
| A-03 / P-21 | Regra `.language-options + p { margin-top: 1rem; }` aplicada no CSS comum. A inspeção visual em larguras, temas, zoom e impressão ainda precisa ser concluída; P-21 permanece em confirmação. |
| A-04 / P-22 | Contradição removida de `conteudo-e-fontes.md`. O registro da confirmação de São Paulo em 06/11/2026 permanece, e P-17 saiu da lista vigente; seu fechamento já consta no `CHANGELOG`. |
| A-05 / P-23 | As oito frases genéricas de cada idioma foram retiradas. Cada `rede.html` mantém quatro cartões, cada um com nome e link; a abertura mantém o agradecimento geral. |

**Verificações realizadas:** a página inglesa local abriu no navegador e sua árvore de acessibilidade mostrou as cinco fichas, a nova subcategoria e os atalhos do Perfil. Uma conferência por parser comparou títulos, datas e descrições de tela e cópia oculta nas duas páginas curriculares; conferiu também as 24 competências novas, os dois trechos `lang="en-US"` e os oito cartões. Os 24 arquivos HTML do repositório foram percorridos para detectar IDs duplicados, destinos relativos ausentes e âncoras internas sem alvo: nenhum foi encontrado. A lista de consulta contém os dois parágrafos atuais do Perfil e empresa, período e local das cinco experiências. Seu SHA-256 após a correção é `d0eb36e7608bcdcbf5f6ecf6b7bd2aad686f69d4480ece1adda9646b98207499`. O `manifesto.json` da pasta registra a extração histórica das traduções, não esta lista vigente; por isso não foi alterado.

**Limites desta verificação:** o parser empregado não é um validador formal do HTML Living Standard. A sessão de navegador expôs a página inglesa, mas não concluiu as capturas em 320, 768 e 1280 CSS px, tema escuro, zoom real, impressão renderizada ou leitura por leitor de tela. P-10, P-11, P-12 e P-21 conservam os ensaios correspondentes. A inspeção estática confirma que a regra de impressão existente oculta a cópia estruturada pelo atributo `hidden`, mas não confirma a paginação impressa.

## Limites da auditoria

Não houve participantes externos, celular real, leitor de tela, zoom real de 200%/400%, renderização de impressão, emulação visual do tema escuro nem validação formal do HTML Living Standard. A inspeção do CSS de impressão, das cores escuras e de `prefers-reduced-motion` é estática. As capturas foram amostras dos tipos de página; a análise de DOM e largura cobriu as 12 páginas. P-10, P-11 e P-12 permanecem abertos ou parciais pelos ensaios faltantes. Nenhum teste aqui declara conformidade WCAG 2.2 AA ou certificação de redação.
