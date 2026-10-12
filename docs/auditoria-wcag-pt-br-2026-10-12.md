# Auditoria WCAG 2.2 — pt-BR, página principal e galeria

Data: 12 de outubro de 2026. Alvo: WCAG 2.2 nível AA.
Estado da conformidade: **não demonstrada integralmente nesta avaliação**.
As verificações locais concluídas não encontraram falhas nas condições examinadas.
Testes em navegador e com tecnologia assistiva permanecem pendentes.

## Escopo e versão

Esta auditoria cobre integralmente o código de duas páginas em pt-BR:

- [Página principal](../static/pt-BR/index.html).
- [Galeria de registros profissionais](../static/pt-BR/galeria.html).

O commit-base é `215b72ff4ce3317dd89a6da1e7c3f4023ccdc4c7`.
A avaliação inclui as correções posteriores presentes no checkout desta entrega.
O [arquivo de evidências](auditoria-wcag-pt-br-2026-10-12.json) identifica páginas, arquivos CSS e variantes de fotografia por SHA-256.
Qualquer alteração nesses arquivos exige revisar os resultados afetados.

As outras páginas e versões de idioma não receberam auditoria completa.
As alterações de CSS foram sincronizadas nos cinco idiomas, conforme as instruções do projeto.
Sites externos e fotografias JPEG abertas isoladamente estão fora da avaliação de conformidade.

## Referência normativa

A referência é a [recomendação WCAG 2.2 de 12 de dezembro de 2024](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html).
A [versão oficial datada](https://www.w3.org/TR/2024/REC-WCAG22-20241212/) identifica a mesma recomendação.
O [manifesto local](referencias/w3c/manifesto.json) registra sua origem e integridade.
O SHA-256 da cópia foi conferido durante a avaliação.
O rascunho de outubro de 2026 não foi usado como requisito normativo.

O nível AA exige atender a todos os critérios A e AA aplicáveis.
A matriz abaixo cobre os 55 critérios desses níveis na WCAG 2.2.
O critério 4.1.1 foi removido dessa versão e não integra a matriz.
Os nomes em português são rótulos descritivos. Os links levam ao texto normativo em inglês.

## Método e limites

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

## Correções e melhorias aplicadas

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

## Resultados das verificações locais

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

## Contraste das cores declaradas

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

## Matriz dos critérios A e AA

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

### Perceptível

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

### Operável

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

### Compreensível

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

### Robusto

| Critério | Nível | Principal | Galeria | Evidência ou pendência |
| --- | --- | --- | --- | --- |
| [4.1.2 Nome, função e valor](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#name-role-value) | A | P | P | Controles e links nativos. Falta confirmar nomes, funções e estado expandido com tecnologia assistiva. |
| [4.1.3 Mensagens de estado](referencias/w3c/wcag-2.2-recomendacao-2024-12-12.html#status-messages) | AA | NA | NA | Sem mensagens de estado dinâmicas. O estado do controle recolhível pertence ao critério 4.1.2. |

## Avaliação dos requisitos de conformidade

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

## Procedimento para concluir a avaliação

Se o ambiente permitir abrir sockets, execute na raiz do repositório:

```sh
python3 -m http.server 8001 --bind 127.0.0.1 --directory static
```

Abra `http://127.0.0.1:8001/pt-BR/`.
Abra também `http://127.0.0.1:8001/pt-BR/galeria.html`.
Registre navegador, sistema, tecnologia assistiva, versões e data de cada ensaio.

| Ensaio pendente | Procedimento | Resultado necessário |
| --- | --- | --- |
| Teclado e foco | Percorra cada página com Tab e Shift+Tab. Ative links com Enter. Alterne os cursos com Enter e Espaço. | Ordem lógica, foco visível e ausência de armadilhas. |
| Link de salto | Ative o primeiro link de cada página. | O foco e a próxima posição de navegação passam ao conteúdo principal. |
| Fotos e retorno | Abra cada foto pelo teclado. Retorne com o comando de voltar do navegador. | Imagem disponível e retorno utilizável à galeria. |
| Leitor de tela | Percorra títulos, listas, regiões e links. Alterne o controle dos cursos. | Estrutura compreensível, nomes úteis e anúncio dos estados aberto e fechado. |
| Tecnologia assistiva adicional | Confira listas sem marcadores no Safari com VoiceOver. | Experiência, habilidades e contato continuam anunciados como listas. |
| Redimensionamento | Amplie o texto a 200%. | Nenhum texto ou controle perde conteúdo ou função. |
| Reorganização | Teste largura de 320 pixels CSS. Teste zoom a 400% em uma janela de 1280 pixels CSS. | Sem rolagem horizontal do conteúdo nem perda de informação. |
| Orientação | Alterne retrato e paisagem em tela pequena. | Todo o conteúdo permanece disponível. |
| Espaçamento de texto | Aplique altura de linha de 1,5 e distância entre parágrafos de duas vezes o tamanho da fonte. | Nenhum texto ou controle fica cortado. |
| Espaçamento entre caracteres | Aplique espaçamento de letras de `0.12em` e de palavras de `0.16em`, junto aos valores anteriores. | Todo o conteúdo e todos os controles continuam utilizáveis. |
| Temas e contraste visual | Confira temas claro e escuro, incluindo apontamento e foco sobre cada foto. | Texto e indicadores mantêm os contrastes exigidos e o foco permanece identificável. |
| Alvos e cancelamento | Meça os alvos renderizados. Confira as exceções de 2.5.8. Pressione um link, afaste o ponteiro e solte. | Alvos atendem ao mínimo ou à exceção. Não há ativação involuntária ao cancelar. |
| Movimento reduzido | Ative a preferência de movimento reduzido. | A rolagem suave e o deslocamento decorativo dos botões são desativados. |
| Impressão complementar | Imprima a principal com os cursos fechados e abertos. Imprima a galeria. | TOEIC sempre presente. Cursos presentes quando abertos. Conteúdo e fotos sem cortes indevidos. |
| Validação e regressão | Execute um validador HTML/CSS. Abra as páginas que compartilham o CSS nos outros idiomas. | Nenhum problema novo de estrutura, recursos ou apresentação. |

Para rastrear a versão auditada, compare os hashes do arquivo de evidências com os arquivos atuais.
Registre uma evidência por ensaio, com captura, saída da ferramenta ou descrição observada.
Se houver falha, corrija a página e repita os ensaios afetados.
Depois, atualize a matriz e a avaliação dos requisitos de conformidade.
