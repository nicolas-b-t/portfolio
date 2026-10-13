# Relatório final de verificação — pt-BR, currículo, galeria e agradecimentos

Data: 12 de outubro de 2026. Versão examinada: `d7aebe2`. Alvo: WCAG 2.2 AA.
Este relatório consolida a auditoria de código e os testes posteriores em navegador.
A conformidade integral permanece não demonstrada. Nenhuma falha foi encontrada nos ensaios descritos.

## Aplicação das referências técnicas — revisão atual

Data: 12 de outubro de 2026. Base Git: `d7aebe2`, com alterações locais ainda não publicadas.
Escopo atual: currículo, galeria e agradecimentos em pt-BR. Correções do CSS foram sincronizadas nos cinco idiomas.
O responsável autorizou a ampliação técnica e editorial nesta revisão.
As seções posteriores preservam os resultados da versão anterior. Não descrevem integralmente o estado atual.

### Alterações realizadas

- A principal mantém os cursos recolhíveis na tela e uma cópia exclusiva para impressão.
- As duas cópias preservam os mesmos 17 títulos, instituições, datas e cargas horárias.
- A impressão oculta o controle original e mostra apenas a cópia completa.
- Links independentes receberam dimensão mínima de 24 pixels. Links de empresas permanecem dentro dos títulos dos cargos.
- A grade de fotos usa uma coluna e passa a duas colunas a partir de 45rem.
- O atributo `sizes` da galeria pt-BR acompanha esse limite e desconta as bordas.
- As regras de impressão permitem dividir seções longas e evitam quebras dentro de cursos e cartões.
- As fotografias impressas ficam em uma coluna, com altura máxima de 17 centímetros e proporção preservada.
- A redação da introdução da galeria e dos agradecimentos usa verbos diretos. Fatos e destinos foram preservados.

As listas sem marcadores preservam `role="list"` pela justificativa de compatibilidade já registrada.
Esse atributo não substitui a semântica nativa nem os testes com tecnologia assistiva.
Nenhuma fotografia foi recomprimida. O workflow e a hospedagem não foram alterados.
Nenhum script foi acrescentado ao site.

### Referências aplicadas

| Referência oficial local | Aplicação |
| --- | --- |
| [HTML Living Standard](referencias/whatwg/html-living-standard-2026-10-12.html) e [Encoding](referencias/whatwg/encoding-2026-10-12.html) | Estrutura, UTF-8, controles nativos e imagens responsivas |
| [ARIA in HTML](referencias/w3c/html-aria-2026-10-12.html) | Nomes, funções, estados e uso dos atributos ARIA |
| [WCAG 2.2](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html) e [WCAG-EM 2.0](referencias/w3c/wcag-em-2-2026-10-12.html) | Critérios e registro dos ensaios, com limites explícitos |
| [Grid](referencias/w3c/css-grid-1-2026-10-12.html), [Flexbox](referencias/w3c/css-flexbox-1-2026-10-12.html) e [Fragmentation](referencias/w3c/css-break-3-2026-10-12.html) | Grades, alvos e apresentação para impressão |
| [RFC 5646](referencias/ietf/rfc-5646-2026-10-12.txt) | Conferência das etiquetas de idioma |
| [RFC 9110](referencias/ietf/rfc-9110-2026-10-12.txt) e [RFC 9111](referencias/ietf/rfc-9111-2026-10-12.txt) | Tipos de conteúdo, cache e respostas condicionais |
| [RFC 9649](referencias/ietf/rfc-9649-2026-10-12.txt) | Identificação do formato WebP e preservação da alternativa JPEG |

O [índice das referências](referencias/guia-de-uso.md#referências-web) distingue recomendações, notas e rascunhos.
A aplicação não transforma rascunhos em recomendações aprovadas nem implica conformidade com todas as especificações.

### Resultados atuais

| Verificação | Resultado |
| --- | --- |
| HTML W3C | Zero erros nas três páginas. Principal: 21 avisos sobre `role="list"`. Galeria e agradecimentos: zero avisos. |
| CSS W3C, perfil CSS3 | Válido, zero erros e 16 avisos. Avisos sobre variáveis e `-webkit-text-size-adjust`, preservados e justificados. |
| Estrutura e recursos | Um `h1`, UTF-8 e `lang="pt-BR"` em cada página. Sem IDs duplicados, scripts ou referências inválidas. Os 54 recursos locais únicos retornaram HTTP 200. |
| Cursos | As cópias são iguais. Na tela aberta, 17 cursos visíveis. Na simulação de impressão, 17 cursos nos estados fechado e aberto. |
| Teclado | Percurso completo com Tab e Shift+Tab nas três páginas. Salto ao `main` confirmado. Enter e Espaço alternaram os cursos. |
| Reorganização | Sem excesso de largura a 320 pixels e em paisagem de 640 por 320 pixels nas três páginas. |
| Texto e espaçamento | Fonte raiz a 200% e os quatro valores de espaçamento WCAG aplicados em variantes temporárias. Sem caixas textuais excedendo a largura. |
| Temas e movimento | Cores escuras e regras de movimento reduzido conferidas por simulação CSS, sem mudança da preferência real do sistema. |
| Contraste | Quatorze combinações recalculadas. Todas acima de 4,5:1 nos dois temas. |
| Fotografias | Nove arquivos maiores abriram por teclado. Descritores de largura coincidem com os pixels reais. Arredondamentos das variantes menores ficam dentro de um pixel. |
| Grade e seleção | Medidas a 320, 640, 704, 720, 992 e 1280 pixels. WebP de 640 e 1280 pixels selecionados conforme a condição e o cache. |
| Regressão | As quinze páginas dos cinco idiomas abriram a 320 e 1280 pixels, sem excesso de largura. CSS idêntico por SHA-256. |

Links independentes medidos na principal atendem ao mínimo de 24 pixels por dimensão.
Os links das empresas integram texto de títulos e usam a exceção de links em linha do critério 2.5.8.
A diferença entre `sizes` e largura renderizada pode incluir a barra de rolagem.
O navegador pode reutilizar uma variante maior já carregada. Isso não constitui falha de seleção.

### HTTP da publicação atual

Cinco recursos publicados retornaram `200`. As cinco requisições com `If-None-Match` retornaram `304`.
As respostas incluem `Cache-Control: max-age=600`, ETag e Last-Modified.
Foram conferidos HTML, CSS, SVG, WebP e JPEG, com tipos de conteúdo correspondentes.
Essas medidas descrevem a publicação anterior, não as alterações locais desta revisão.

### Limites da conclusão atual

A API disponível não oferece emulação de mídia nem controle de leitor de tela.
As regras de impressão foram aplicadas a cópias temporárias para examinar visibilidade e apresentação contínua.
Essa simulação não confirma paginação real, margens físicas ou cortes entre folhas.
O zoom nativo não respondeu aos atalhos. A fonte a 200% não substitui esse ensaio.
Não foram realizados testes com leitor de tela, Safari com VoiceOver ou cancelamento de ponteiro.
A inspeção da árvore de acessibilidade não substitui esses testes.
A versão do navegador não foi exposta pela API disponível.
A conformidade integral WCAG AA permanece não demonstrada.

### Evidências atuais

- [Inspeção, dimensões e hashes](evidencias-wcag-2026-10-12/inspecao-aplicacao.json).
- [Validação HTML](evidencias-wcag-2026-10-12/validacao-html-aplicacao.json).
- [Validação CSS](evidencias-wcag-2026-10-12/validacao-css-aplicacao.xml).
- [Navegador, percursos e medidas](evidencias-wcag-2026-10-12/navegador-aplicacao.json).
- [Contrastes calculados](evidencias-wcag-2026-10-12/contrastes-aplicacao.json).
- [Cabeçalhos HTTP](evidencias-wcag-2026-10-12/http-publicacao.json).
- [Recursos HTTP locais](evidencias-wcag-2026-10-12/recursos-http-locais.json).
- [Cursos no estilo de impressão simulado](evidencias-wcag-2026-10-12/impressao-css-cursos.png).
- [Cursos abertos na tela estreita](evidencias-wcag-2026-10-12/cursos-tela-320.png).

### Repetição e manutenção

Use o procedimento de repetição deste relatório também para `/pt-BR/rede.html`.
Confira todos os cursos uma única vez na impressão real, com o controle fechado e aberto.
Ao editar cursos, atualize as duas cópias e compare seu conteúdo integral.
Confira a grade imediatamente antes e depois de 45rem, além da largura máxima de 62rem.
Registre tamanho de fonte, largura CSS e variante de imagem selecionada.
Use preferências reais de tema e movimento reduzido quando o ambiente permitir.
Preserve as respostas dos validadores e os hashes da versão examinada.

## Registro da avaliação anterior

As seções seguintes foram preservadas como evidência da versão `d7aebe2` anterior a esta aplicação.

## Ambiente e método

Os ensaios usaram o Codex In-app Browser no Windows e o servidor Python local na porta 8001.
A API disponível não informou a versão do navegador.
A inspeção combinou teclado, árvore de acessibilidade, capturas e medidas do DOM renderizado.
A árvore do navegador não substitui um ensaio com leitor de tela.

Variantes temporárias aplicaram espaçamento de texto, tamanho de fonte e as cores do tema escuro.
Essas variantes não adicionaram scripts e foram removidas após os ensaios.
O tema escuro foi aplicado pelas mesmas regras CSS, sem alterar a preferência do sistema.
A ampliação de texto usou fonte raiz de 32 pixels, contra 16 pixels na apresentação normal.
Isso não equivale ao zoom nativo do navegador.

## Resultados

| Ensaio | Resultado e limite |
| --- | --- |
| HTML, Nu Html Checker W3C | Zero erros nas duas páginas. Principal: 21 avisos. Galeria: zero avisos. |
| CSS, serviço W3C, perfil CSS3 | Válido, zero erros e 16 avisos. A primeira requisição POST falhou no serviço. A requisição GET concluiu a validação. |
| Referências locais | 26 na principal e 72 na galeria, sem destinos ou âncoras inválidos. Inclui CSS, favicon, troca de idioma e variantes de imagem. |
| Teclado | Tab percorreu todos os controles nas duas páginas e retornou ao início, sem armadilha observada. Shift+Tab foi amostrado. |
| Link de salto | Enter transferiu o foco para `main` nas duas páginas. |
| Cursos | Enter e Espaço alternaram o controle nativo. Os 17 cursos apareceram ao abrir. |
| Foco | Os controles percorridos apresentaram contorno sólido. O link de salto exibiu contorno de três pixels. Não houve sobreposição fixa observada. |
| Tela estreita | Largura de 320 pixels, com largura de conteúdo de 305 pixels nas duas páginas. Sem rolagem horizontal. |
| Paisagem | Largura de 640 pixels e altura de 320 pixels. Conteúdo com largura de 625 pixels nas duas páginas. |
| Texto ampliado | Fonte raiz a 200%, largura de 320 pixels. Sem rolagem horizontal. A principal também foi examinada com cursos abertos. |
| Espaçamento WCAG | Altura de linha 1,5, parágrafos 2em, letras 0,12em e palavras 0,16em. Nenhuma caixa textual excedeu sua largura disponível. |
| Tema escuro | Cores esperadas renderizadas nas duas páginas, sem excesso de largura. Não foi testada a mudança da preferência do sistema. |
| Fotografias | As nove fotos abriram por Enter, carregaram e permitiram retornar à galeria. Imagens com carregamento tardio não foram tratadas como falhas. |
| Alvos da galeria | Navegação e troca de idioma mediram pelo menos 24 pixels por dimensão. Os nove links de foto excederam esse mínimo. |
| Cinco idiomas | Páginas principais abriram a 1280 pixels, com `lang` esperado, um `h1` e sem excesso de largura. Inspeção de regressão limitada. |
| CSS e scripts | Cinco CSS idênticos. Nenhum script ou evento próprio nas duas páginas auditadas. |

Os avisos HTML apontam `role="list"` redundante em listas nativas.
Esses atributos foram preservados pela justificativa de compatibilidade registrada na auditoria anterior.
Os avisos CSS tratam da extensão `-webkit-text-size-adjust` e de variáveis não avaliadas estaticamente pelo serviço.
A validação de sintaxe não comprova acessibilidade.
Os contrastes calculados anteriormente continuam associados ao mesmo CSS. Não foram recalculados nesta rodada.

## Evidências

- [Saída do validador HTML](validacao-html-pt-br-2026-10-12.json).
- [Saída do validador CSS](validacao-css-pt-br-2026-10-12.xml).
- [Percursos, medidas, fotos e hashes](testes-navegador-pt-br-2026-10-12.json).
- [Galeria com tema escuro a 320 pixels](evidencias-wcag-2026-10-12/galeria-escuro-320.png).
- [Principal com fonte a 200% e largura de 320 pixels](evidencias-wcag-2026-10-12/principal-texto-200-320.png).

## Limites da conclusão

O atalho de zoom não alterou a largura CSS nem a escala observável no navegador disponível.
O zoom nativo a 200% e 400% permanece pendente.
Também permanecem pendentes os ensaios com leitor de tela, Safari com VoiceOver, impressão e preferência real de movimento reduzido.
Faltam cancelamento de ponteiro, percurso inverso completo e inspeção visual de cada indicador de foco nos dois temas.
As medidas de alvos desta rodada cobrem a galeria, não todos os links da principal.
As capturas mostram trechos das páginas, não cada estado ou região.

Os resultados complementam critérios de teclado, salto, reorganização, espaçamento e finalidade dos links.
A matriz de código abaixo preserva os resultados e limites da avaliação inicial.
Esta rodada não emite declaração formal de conformidade WCAG.

## Repetir a verificação

Execute os comandos na raiz do repositório. Use Python disponível no ambiente.

```sh
git status --short
git rev-parse HEAD
python3 -m http.server 8001 --bind 127.0.0.1 --directory static
```

No Windows, substitua `python3` pelo executável Python instalado, se necessário.
Se a porta estiver ocupada, escolha outra porta.

1. Abra `http://127.0.0.1:8001/pt-BR/`.
2. Abra `http://127.0.0.1:8001/pt-BR/galeria.html`.
3. Registre data, commit, sistema, navegador, versão e tecnologia assistiva.
4. Envie cada HTML ao [Nu Html Checker W3C](https://validator.w3.org/nu/).
5. Envie `static/pt-BR/styles.css` ao [validador CSS W3C](https://jigsaw.w3.org/css-validator/).
6. Preserve as respostas dos validadores junto aos hashes dos arquivos examinados.
7. Percorra cada página com Tab e Shift+Tab.
8. Ative o link inicial com Enter.
9. Confirme o foco no conteúdo principal.
10. Alterne os cursos com Enter e Espaço.
11. Abra cada fotografia com Enter.
12. Retorne à galeria pelo comando Voltar.
13. Confira nomes, funções, listas, títulos e estados com leitor de tela.
14. Confira o foco em cada controle, incluindo as bordas da tela.
15. Confira largura de 320 pixels CSS.
16. Confira uma tela de 640 por 320 pixels CSS.
17. Amplie o texto a 200%.
18. Aplique zoom nativo de 400% em uma janela de 1280 pixels CSS.
19. Confira temas claro e escuro com a preferência real do sistema.
20. Ative a preferência de movimento reduzido.
21. Meça os alvos e examine as exceções do critério 2.5.8.
22. Pressione um link e solte o ponteiro fora dele.
23. Confirme que o cancelamento não ativa o link.
24. Imprima a principal com os cursos fechados e abertos.
25. Confirme a presença do TOEIC nos dois estados.
26. Imprima a galeria e examine cortes de imagens e legendas.
27. Abra as cinco versões de idioma.
28. Confira CSS, favicon, links relativos, âncoras e troca de idioma.

Para testar espaçamento, aplique este CSS somente em uma cópia temporária ou nas ferramentas do navegador.

```css
* {
  line-height: 1.5 !important;
  letter-spacing: 0.12em !important;
  word-spacing: 0.16em !important;
}
p { margin-bottom: 2em !important; }
```

Use `:root { font-size: 200%; }` para repetir a simulação de fonte ampliada.
Registre essa simulação separadamente do zoom nativo.
Não publique regras de teste nem acrescente scripts ao site.

Se houver alteração no CSS, recalcule os contrastes dos dois temas.
Use luminância relativa sRGB e a fórmula `(L1 + 0,05) / (L2 + 0,05)`.
Compare texto comum com 4,5:1 e indicadores relevantes com 3:1.
Confira os critérios aplicáveis na recomendação WCAG citada neste relatório.

Ao terminar, remova as cópias temporárias.
Encerre o servidor com Ctrl+C.
Execute `git diff --check`.
Revise `git diff` e `git status --short`.
Registre falhas, resultados e testes não executados.
Só declare conformidade integral após reunir evidências suficientes para todos os requisitos aplicáveis.

## Matriz e verificações de código de origem

Esta seção descreve a avaliação anterior à versão `d7aebe2`.
Suas contagens e estados não representam uma nova auditoria integral da versão atual.
A principal ganhou quatro links e mudou a ordem das subcategorias.
Os resultados atuais de navegador e validação estão nas seções anteriores.

### Referência normativa

A referência é a [recomendação WCAG 2.2 de 12 de dezembro de 2024](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html).
A [versão oficial datada](https://www.w3.org/TR/2024/REC-WCAG22-20241212/) identifica a mesma recomendação.
O [manifesto local](referencias/w3c/manifesto.json) registra sua origem e integridade.
O SHA-256 da cópia foi conferido durante a avaliação.
O rascunho de outubro de 2026 não foi usado como requisito normativo.

O nível AA exige atender a todos os critérios A e AA aplicáveis.
A matriz abaixo cobre os 55 critérios desses níveis na WCAG 2.2.
O critério 4.1.1 foi removido dessa versão e não integra a matriz.
Os nomes em português são rótulos descritivos. Os links levam ao texto normativo em inglês.

### Método e limites

A avaliação combinou leitura do HTML e CSS, inspeção das nove fotografias e verificações locais com Python.
As verificações examinaram referências, âncoras, estrutura explícita, idiomas, cursos, datas, variantes de imagem e contrastes declarados.
O cálculo de contraste usou luminância relativa sRGB e a fórmula `(L1 + 0,05) / (L2 + 0,05)`.
Uma análise de código não substitui a renderização ou o cálculo da árvore de acessibilidade do navegador.

O servidor local falhou com `PermissionError: [Errno 1] Operation not permitted`.
O Chromium falhou com `setsockopt: Operation not permitted`.
Por isso, esta entrega não inclui evidências de renderização, teclado, zoom ou impressão em navegador.
Também não inclui testes com leitor de tela nem validação formal HTML/CSS.

As imagens foram abertas diretamente para comparar seu conteúdo com as alternativas textuais.
A galeria usa essas fotos como registros profissionais, sem apresentar uma análise dos valores exibidos nos equipamentos.
O texto incidental de placas e telas não substitui informações textuais do currículo.
A abertura de JPEG depende do visualizador do navegador. A descrição e a legenda permanecem na galeria.

### Correções e melhorias aplicadas

| Registro | Condição anterior | Alteração | Critérios relacionados |
| --- | --- | --- | --- |
| A01 | A ação dos links de fotografia aparecia somente nos nomes ARIA. | Cada foto ganhou a ação visível “Ver fotografia em tamanho maior”. O nome nativo reúne descrição e ação. | 1.1.1, 2.4.4, 2.5.3, 4.1.2 |
| A02 | O link continha uma imagem em bloco, mas permanecia um elemento em linha. | O link passou a ocupar um bloco. Isso define sua área de interação e a caixa do contorno de foco. | 1.4.11, 2.4.7, 2.5.8 |
| A03 | As categorias da galeria apareciam em um parágrafo com links em linha. | As categorias passaram a formar uma navegação nomeada. Os links recebem as dimensões mínimas da navegação. | 1.3.1, 2.4.6, 2.5.8 |
| A04 | A navegação definia altura mínima de 24 pixels, sem largura mínima explícita. | Os links de navegação receberam largura mínima de 24 pixels CSS. | 2.5.8 |
| A05 | As listas de experiência e contato removiam os marcadores pelo CSS. | Foi explicitado `role="list"`, para preservar a intenção semântica em implementações que alteram listas sem marcadores. | 1.3.1, 4.1.2 |
| A06 | Os dados completos do TOEIC estavam dentro de uma seção recolhível. | O exame voltou ao fluxo visível, com datas e pontuações preservadas. Seus trechos em inglês receberam `lang="en"`. | 3.1.2 e verificação complementar de impressão |

Essas alterações incluem medidas preventivas e melhorias de clareza.
A inspeção não comprovou que todas as condições anteriores constituíam falhas WCAG.
Links em linha podem usar a exceção prevista no critério 2.5.8.
A regressão de impressão do TOEIC é uma questão complementar, não uma falha WCAG confirmada.

Os 17 cursos continuam organizados nas categorias existentes, dentro de um controle HTML nativo.
Antes de imprimir os cursos, abra essa seção.
Os dados do TOEIC não dependem mais do estado desse controle.
A confirmação do resultado impresso permanece pendente.

### Resultados das verificações locais

| Verificação | Página principal | Galeria |
| --- | --- | --- |
| Idioma e codificação | `pt-BR`, UTF-8 | `pt-BR`, UTF-8 |
| Título da página | Presente e descritivo | Presente e descritivo |
| Estrutura principal | Um `h1` e um `main` | Um `h1` e um `main` |
| Níveis de títulos | Sem saltos na estrutura explícita | Sem saltos na estrutura explícita |
| Link para pular ao conteúdo | Destino `main` existente, com `tabindex="-1"` | Destino `main` existente, com `tabindex="-1"` |
| Navegações | Nomes distintos no código | Nomes distintos no código |
| Links com nome no código | 27, nenhum vazio | 19, nenhum vazio |
| Referências locais e âncoras | 26 verificadas, nenhuma inválida | 72 verificadas, nenhuma inválida |
| Fotografias | Nenhuma no conteúdo | Nove descrições e legendas revisadas |
| Variantes de imagem | Não aplicável | Todas as larguras de `srcset` conferidas com os arquivos |
| Formação e datas | 17 cursos e todas as datas preservados | Não aplicável |
| Scripts e eventos próprios | Nenhum | Nenhum |
| `tabindex` positivo | Nenhum | Nenhum |

As 98 referências incluem ocorrências repetidas em `href`, `src` e `srcset`.
Os destinos externos não foram requisitados.
Os nomes dos links foram examinados no código, sem cálculo completo do nome acessível pelo navegador.
O fechamento explícito de elementos não apresentou erros na verificação local.
Isso não equivale a uma validação formal do HTML Living Standard.

Os cinco arquivos CSS são idênticos por SHA-256.
O comando `git diff --check` não apontou erros de espaçamento.

### Contraste das cores declaradas

Os valores abaixo foram arredondados somente para apresentação.
Os limites foram comparados com os resultados completos, preservados no arquivo de evidências.
Texto comum exige pelo menos 4,5:1. Componentes e indicadores relevantes exigem pelo menos 3:1.

| Combinação | Tema claro | Tema escuro |
| --- | --- | --- |
| Texto principal / fundo da página | 19,44:1 | 17,21:1 |
| Texto principal / painel | 19,80:1 | 16,00:1 |
| Texto secundário / fundo da página | 8,70:1 | 9,32:1 |
| Texto secundário / painel | 8,86:1 | 8,67:1 |
| Cor de destaque / fundo da página | 5,77:1 | 7,92:1 |
| Cor de destaque / painel | 5,88:1 | 7,37:1 |
| Texto do botão / fundo do botão | 5,88:1 | 7,92:1 |

As combinações examinadas atendem ao limite de texto comum nos dois temas.
O destaque do foco tem contraste calculado suficiente contra os fundos declarados.
Sua visibilidade efetiva, geometria e relação com as fotografias ainda exigem inspeção no navegador.
O cálculo não avaliou cores introduzidas por extensões, recursos externos ou modos personalizados do usuário.

### Matriz dos critérios A e AA

- **V**: verificado pelas evidências descritas, dentro dos limites desta avaliação.
- **P**: há evidência de código, mas falta confirmação comportamental, visual ou com tecnologia assistiva.
- **NA**: a condição que torna o critério aplicável não existe nas páginas examinadas.

“V” não constitui certificação nem declaração isolada de conformidade.
“P” não significa falha confirmada. Significa evidência insuficiente para encerrar o critério.

| Página | V | P | NA | Total |
| --- | --- | --- | --- | --- |
| Principal | 15 | 18 | 22 | 55 |
| Galeria | 15 | 17 | 23 | 55 |

Essas contagens não representam uma porcentagem de conformidade.
Cada critério aplicável deve ser atendido para demonstrar o nível AA.

#### Perceptível

| Critério | Nível | Principal | Galeria | Evidência ou pendência |
| --- | --- | --- | --- | --- |
| [1.1.1 Conteúdo não textual](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#non-text-content) | A | V | V | Nove fotos comparadas visualmente com seus textos alternativos. A página principal não apresenta imagens no conteúdo. |
| [1.2.1 Áudio e vídeo pré-gravados](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#audio-only-and-video-only-prerecorded) | A | NA | NA | Sem áudio ou vídeo. |
| [1.2.2 Legendas pré-gravadas](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#captions-prerecorded) | A | NA | NA | Sem mídia temporal. |
| [1.2.3 Audiodescrição ou alternativa](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#audio-description-or-media-alternative-prerecorded) | A | NA | NA | Sem mídia temporal. |
| [1.2.4 Legendas ao vivo](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#captions-live) | AA | NA | NA | Sem transmissão ao vivo. |
| [1.2.5 Audiodescrição pré-gravada](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#audio-description-prerecorded) | AA | NA | NA | Sem vídeo. |
| [1.3.1 Informações e relações](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#info-and-relationships) | A | P | P | Títulos, listas, navegações e legendas estruturados. Falta confirmar sua exposição com leitor de tela. |
| [1.3.2 Sequência significativa](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#meaningful-sequence) | A | P | P | O código segue a ordem do conteúdo, sem reordenação CSS. Falta comparar leitura e renderização. |
| [1.3.3 Características sensoriais](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#sensory-characteristics) | A | V | V | As instruções não dependem somente de posição, forma, cor ou som. |
| [1.3.4 Orientação](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#orientation) | AA | P | P | Não há bloqueio de orientação. Falta testar retrato e paisagem. |
| [1.3.5 Finalidade dos campos](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#identify-input-purpose) | AA | NA | NA | Sem campos de entrada de dados pessoais. |
| [1.4.1 Uso de cor](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#use-of-color) | A | V | V | Links de conteúdo sublinhados. A ação das fotografias também aparece em texto. |
| [1.4.2 Controle de áudio](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#audio-control) | A | NA | NA | Sem áudio automático. |
| [1.4.3 Contraste mínimo](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#contrast-minimum) | AA | V | V | Quatorze combinações de cores calculadas, todas acima de 4,5:1. |
| [1.4.4 Redimensionamento de texto](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#resize-text) | AA | P | P | Tamanhos relativos e viewport sem bloqueio de zoom. Falta testar texto a 200%. |
| [1.4.5 Imagens de texto](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#images-of-text) | AA | V | V | Conteúdo editorial em HTML. Textos incidentais das fotos fazem parte dos registros visuais, sem substituir conteúdo editorial. |
| [1.4.10 Reorganização do conteúdo](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#reflow) | AA | P | P | Grades fluidas e quebra de palavras. Falta testar 320 pixels CSS e zoom a 400%. |
| [1.4.11 Contraste não textual](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#non-text-contrast) | AA | P | P | Bordas e destaque contrastam com os fundos declarados. Falta verificar indicadores e foco na renderização. |
| [1.4.12 Espaçamento de texto](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#text-spacing) | AA | P | P | Sem alturas fixas para conteúdo textual. Falta aplicar os quatro valores normativos no navegador. |
| [1.4.13 Conteúdo em foco ou apontamento](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#content-on-hover-or-focus) | AA | NA | NA | Nenhum conteúdo adicional aparece somente em foco ou apontamento. |

#### Operável

| Critério | Nível | Principal | Galeria | Evidência ou pendência |
| --- | --- | --- | --- | --- |
| [2.1.1 Teclado](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#keyboard) | A | P | P | Links e controle recolhível são nativos. Falta executar Tab, Shift+Tab, Enter e Espaço. |
| [2.1.2 Ausência de armadilha de teclado](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#no-keyboard-trap) | A | P | P | Sem scripts de captura de foco. Falta percorrer toda a página por teclado. |
| [2.1.4 Atalhos de caracteres](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#character-key-shortcuts) | A | NA | NA | Sem atalhos próprios. |
| [2.2.1 Limites de tempo](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#timing-adjustable) | A | NA | NA | Sem temporizadores ou expiração de tarefas. |
| [2.2.2 Pausar, parar ou ocultar](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#pause-stop-hide) | A | NA | NA | Sem movimento contínuo, rolagem automática ou atualização periódica. |
| [2.3.1 Limite de flashes](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#three-flashes-or-below-threshold) | A | V | V | Sem animações, vídeos ou conteúdo que produza flashes no código examinado. |
| [2.4.1 Pular blocos](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#bypass-blocks) | A | P | P | Link inicial aponta para `main` focalizável. Falta confirmar a transferência do foco. |
| [2.4.2 Título de página](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#page-titled) | A | V | V | Títulos distinguem currículo e registros profissionais. |
| [2.4.3 Ordem do foco](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#focus-order) | A | P | P | Ordem natural, sem `tabindex` positivo. Falta verificar o percurso renderizado. |
| [2.4.4 Finalidade dos links](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#link-purpose-in-context) | A | V | V | Nomes e contexto identificam os destinos. As fotografias incluem descrição e ação. |
| [2.4.5 Múltiplas formas de localização](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#multiple-ways) | AA | V | V | A principal aponta à galeria na experiência e no rodapé. A galeria retorna pela marca e pela navegação. |
| [2.4.6 Títulos e rótulos](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#headings-and-labels) | AA | V | V | Títulos descrevem os assuntos. Navegações têm nomes distintos. |
| [2.4.7 Foco visível](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#focus-visible) | AA | P | P | Contorno de três pixels com afastamento. Falta inspeção visual de cada controle. |
| [2.4.11 Foco não encoberto](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#focus-not-obscured-minimum) | AA | P | P | Sem cabeçalho fixo ou sobreposição permanente. Falta confirmar os controles nas bordas da tela. |
| [2.5.1 Gestos de ponteiro](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#pointer-gestures) | A | NA | NA | Sem gestos complexos ou multiponto próprios. |
| [2.5.2 Cancelamento do ponteiro](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#pointer-cancellation) | A | P | P | Ativação nativa, sem eventos próprios. Falta testar pressionar, afastar o ponteiro e soltar. |
| [2.5.3 Rótulo no nome](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#label-in-name) | A | V | V | Os links usam seu conteúdo para formar o nome. O texto visível das fotografias não recebe substituição ARIA. |
| [2.5.4 Acionamento por movimento](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#motion-actuation) | A | NA | NA | Sem controles acionados por movimento do dispositivo. |
| [2.5.7 Arrastar](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#dragging-movements) | AA | NA | NA | Sem funções que exigem arrastar. |
| [2.5.8 Tamanho mínimo dos alvos](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#target-size-minimum) | AA | P | P | Navegação com mínimos de 24 pixels. Fotos em bloco e links textuais em linha. Falta medir alvos e exceções renderizados. |

#### Compreensível

| Critério | Nível | Principal | Galeria | Evidência ou pendência |
| --- | --- | --- | --- | --- |
| [3.1.1 Idioma da página](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#language-of-page) | A | V | V | As duas páginas declaram `lang="pt-BR"`. |
| [3.1.2 Idioma das partes](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#language-of-parts) | AA | V | V | Troca de idioma e trechos em inglês identificados. Nomes próprios e termos técnicos usam as exceções normativas. |
| [3.2.1 Ao receber foco](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#on-focus) | A | P | P | Sem scripts ou navegação por foco no código. Falta verificar o comportamento nativo. |
| [3.2.2 Ao fornecer entrada](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#on-input) | A | P | NA | A principal tem um controle recolhível nativo, sem navegação automática. Falta confirmar seu comportamento. A galeria não tem entrada. |
| [3.2.3 Navegação consistente](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#consistent-navigation) | AA | V | V | Marca e troca de idiomas preservam posição e ordem. A navegação de seções varia conforme a página. |
| [3.2.4 Identificação consistente](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#consistent-identification) | AA | V | V | Link de salto e troca de idioma mantêm os nomes. As fotografias usam a mesma ação visível. |
| [3.2.6 Ajuda consistente](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#consistent-help) | A | NA | NA | Não há mecanismo de ajuda repetido nas duas páginas. O contato aparece somente na principal. |
| [3.3.1 Identificação de erros](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#error-identification) | A | NA | NA | Sem formulário ou validação de entrada. |
| [3.3.2 Rótulos e instruções](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#labels-or-instructions) | A | NA | NA | Sem solicitação de dados. |
| [3.3.3 Sugestão para erros](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#error-suggestion) | AA | NA | NA | Sem validação de entrada. |
| [3.3.4 Prevenção de erros](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#error-prevention-legal-financial-data) | AA | NA | NA | Sem transações ou alterações de dados do usuário. |
| [3.3.7 Entrada redundante](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#redundant-entry) | A | NA | NA | Sem processo de entrada de dados. |
| [3.3.8 Autenticação acessível](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#accessible-authentication-minimum) | AA | NA | NA | Sem autenticação. |

#### Robusto

| Critério | Nível | Principal | Galeria | Evidência ou pendência |
| --- | --- | --- | --- | --- |
| [4.1.2 Nome, função e valor](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#name-role-value) | A | P | P | Controles e links nativos. Falta confirmar nomes, funções e estado expandido com tecnologia assistiva. |
| [4.1.3 Mensagens de estado](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#status-messages) | AA | NA | NA | Sem mensagens de estado dinâmicas. O estado do controle recolhível pertence ao critério 4.1.2. |

### Avaliação dos requisitos de conformidade

| Requisito da seção 5.2 | Resultado desta avaliação |
| --- | --- |
| [5.2.1 Nível de conformidade](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#cc1) | Alvo AA. Os critérios marcados P impedem afirmar atendimento integral. |
| [5.2.2 Páginas completas](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#cc2) | Todo o código das duas páginas foi examinado. As variações responsivas e os estados interativos ainda exigem testes. |
| [5.2.3 Processos completos](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#cc3) | Não há cadastro, compra ou processo de entrada em etapas. A navegação e a abertura das fotos permanecem sem ensaio completo. |
| [5.2.4 Tecnologias com suporte à acessibilidade](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#cc4) | HTML e CSS nativos. A combinação de navegador e tecnologia assistiva ainda precisa de evidência prática. |
| [5.2.5 Não interferência](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#cc5) | Sem scripts, áudio automático ou flashes. A ausência de armadilha de teclado ainda precisa de teste. |

Esta entrega é uma auditoria técnica com correções e pendências documentadas.
Ela não emite certificação, selo ou declaração formal de conformidade WCAG.
Uma declaração posterior deve identificar data, páginas, versão WCAG, nível alcançado e tecnologias utilizadas.
Ela só pode ser emitida após reunir evidências suficientes para os requisitos aplicáveis.


## Consolidação dos registros

Este relatório substitui os relatórios separados de auditoria e testes complementares.
As evidências originais foram preservadas com sua data, método e versão.
O arquivo de pendências foi removido por decisão do responsável.
A remoção desse arquivo não transforma testes não executados em resultados aprovados.
