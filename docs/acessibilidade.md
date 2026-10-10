# Aplicação das diretrizes de acessibilidade

Referência: WCAG 2.2, recomendação publicada em 12 de dezembro de 2024.
Data da revisão: 9 de outubro de 2026. Alvo: nível AA.

## Escopo e decisões

Conforme escolha do responsável, as primeiras alterações foram aplicadas em
`static/pt-BR/` e `static/en/`. Posteriormente, o responsável autorizou remover
as versões antigas e publicar somente `static/` por GitHub Actions. O escopo
de publicação inclui as cinco versões de idioma e suas páginas complementares.
A revisão atual das competências foi limitada pelo responsável somente à página
principal `static/pt-BR/index.html`; as demais páginas e idiomas ficam para depois.
O site continua sem JavaScript e sem novas dependências de execução.

Também foram escolhidos: cabeçalho no fluxo normal da página, azul preservado
com texto escuro nos botões do tema escuro e aviso textual no lugar dos links
de projetos ainda sem destino.

## Alterações

| Alteração | Motivo e referência |
| --- | --- |
| Cor específica para texto de botões em cada tema | Corrige contraste no tema escuro; 1.4.3. |
| Cabeçalho sem posicionamento fixo | Evita que o cabeçalho cubra destinos e elementos focados; 2.4.11. |
| `tabindex="-1"` no conteúdo principal | Permite receber foco pelo link de salto sem acrescentar uma parada ao Tab; 2.4.1. |
| Indicador de foco com `:focus` | Mantém uma indicação explícita para controles focados, incluindo navegadores sem `:focus-visible`; 2.4.7. |
| Fundo do link de salto igual ao da página | Mantém contraste entre seu indicador de foco e o fundo nos dois temas. |
| Grade fluida, quebra de palavras e padding das seções | Melhora reorganização, espaço lateral e leitura em larguras reduzidas; 1.4.10 e 1.4.12. |
| Links do menu com dimensões mínimas de 24 px | Amplia os alvos de interação; 2.5.8. Links inline em parágrafos têm exceção nesse critério. |
| `nav` para a escolha de idioma | Corrige o uso inválido de nome ARIA em uma `div` genérica; estrutura e identificação de navegação, relacionadas a 1.3.1. |
| Aviso no lugar de `href="#"` nos projetos | Evita apresentar um link funcional quando ainda não existe um destino. |
| Respeito a `prefers-reduced-motion` | Desativa rolagem suave e deslocamento no hover para quem solicita menos movimento; melhoria relacionada a 2.3.3, nível AAA, além do alvo AA. |

## Evidências

### Optigrow e link para Rodrigo — pt-BR

O Optigrow recebeu três tags de participação e um link para
`rede.html#rodrigo-nascimento`. Na página de agradecimentos, somente a âncora
do cartão de Rodrigo foi acrescentada. O Chromium com JavaScript desativado
confirmou a abertura pelo teclado, o destino visível e o LinkedIn já existente.
As duas páginas passaram no Nu HTML Checker sem erros; os 19 avisos conhecidos
de `role="list"` referem-se às listas da página principal.

As 413 referências locais passaram, e foram conferidos temas claro/escuro,
larguras de 240/320/1280 px, espaçamento e ampliação de texto CSS em 200%.
A página principal contém 95 tags; as novas competências e o contato de
Rodrigo apareceram na impressão. A revisão se limita à página principal pt-BR
e à âncora necessária no cartão de Rodrigo, preservando os demais idiomas.

### Competências por projeto e formação — somente pt-BR

A página principal pt-BR recebeu listas de tags nos projetos Portfólio e SGCS
e na formação em GTI, reutilizando `.skill-list`, títulos `h4` e `role="list"`.
As 47 tags superiores foram preservadas; a página contém agora 92 tags:
12 no projeto Portfólio, 14 no SGCS e 19 na formação.

O Nu HTML Checker não encontrou erros; os 18 avisos de papel redundante nas
listas seguem a opção de acessibilidade já documentada. Foram conferidas 412
referências locais e a preservação dos demais arquivos do site e das cinco
folhas CSS. A âncora antiga do SGCS foi mantida no artigo atualizado.

No Chromium com JavaScript desativado, as listas dos projetos e da formação
foram expostas na árvore de acessibilidade. Os seis cenários de tema claro/escuro
e largura 240/320/1280 px passaram sem transbordamento ou tags cortadas,
inclusive com espaçamento aumentado. A ampliação de texto CSS em 200% passou
em 320 px nos dois temas. Link de salto, navegação para Projetos e abertura
dos cursos por teclado passaram. As 92 tags foram encontradas no PDF de seis
páginas; foram inspecionadas as capturas de Projetos e a página de Formação
na impressão. Isso não substitui testes com outros navegadores, leitores de
tela ou zoom real, nem certifica conformidade WCAG.

### COA aplicado somente à página principal pt-BR

Esta etapa preservou as três categorias e reorganizou as competências em dez
subcategorias e 46 tags com títulos `h3`/`h4` e listas nativas. As outras páginas
e idiomas mantêm a apresentação anterior, conforme o escopo autorizado.

A página principal pt-BR passou no Nu HTML Checker sem erros. Os dez avisos
de `role="list"` em `ul` correspondem à opção de preservar a identificação das
listas sem marcadores em Safari/VoiceOver; este ambiente não testou essa dupla.
No Chromium com JavaScript desativado, a árvore de acessibilidade apresentou
as 46 tags e dez subtítulos, e os testes de teclado e contraste passaram.

Seis cenários de tema claro/escuro e largura 240/320/1280 px passaram sem
transbordamento ou tags cortadas, inclusive com espaçamento aumentado.
O texto CSS ampliado em 200% passou em 320 px nos dois temas; essa verificação
não substitui zoom real em outros navegadores. As 46 tags foram encontradas
no PDF de impressão. As capturas em 320 px claro e 1280 px escuro foram
inspecionadas, e a conferência das 413 referências locais passou.

### Verificações anteriores

- Validador Nu da W3C: HTML português e inglês sem erros ou avisos após as correções.
- Chromium 151, com JavaScript desativado: ambos os idiomas e temas claro/escuro.
- Sem transbordamento horizontal nas larguras de 240, 320 e 1280 px testadas.
- Link de salto acessível pelo Tab, foco transferido ao `main` e próximo Tab
  seguindo para o primeiro link do conteúdo.
- Indicador de foco presente e elementos de amostra visíveis na área do navegador.
- Contraste do texto do botão principal: 5,88:1 no tema claro e 7,92:1 no escuro,
  incluindo hover. Antes, o tema escuro tinha 2,40:1.
- Links dos menus de seções e idioma com largura e altura de pelo menos 24 px.
- Preferência de movimento reduzido resulta em rolagem automática sem animação.
- Simulação de espaçamento de texto em 320 px sem transbordamento horizontal.
- Regras de impressão verificadas para ocultação do cabeçalho e padding das seções.
- 32 referências locais verificadas, recursos HTML/CSS/SVG servidos por HTTP e
  folhas CSS dos dois idiomas idênticas.
- Inspeção de imagens do topo da página em 320 px no tema claro e 1280 px no escuro.
  Essa inspeção revelou o conflito de padding, corrigido e verificado em navegador.

As ferramentas de teste usam automação externa ao site. Nenhum script de teste
ou biblioteca foi incorporado às páginas.

### Currículos e competências

As cinco versões receberam o histórico profissional dos currículos e três
listas semânticas: 12 competências técnicas, 7 sociais e 6 habilidades práticas
e operacionais. Cada item tem um rótulo e uma descrição; não há gráficos ou
notas de domínio. As expressões inglesas dos títulos têm identificação de idioma.
As fontes e critérios estão em [competencias-e-evidencias.md](competencias-e-evidencias.md).

Nesta atualização, as 16 páginas passaram no Nu HTML Checker local sem erros
ou avisos, e 413 referências locais foram conferidas. As cinco folhas CSS
permanecem idênticas; não foram incorporados JavaScript nem documentos privados.

Em Chromium com JavaScript desativado, as cinco páginas principais passaram
nos testes de foco do link de salto e abertura/fechamento dos cursos por teclado.
Os 30 cenários de idioma, tema claro/escuro e largura de 240/320/1280 px
não apresentaram transbordamento horizontal, inclusive com espaçamento de texto
aumentado. As três listas continuam visíveis no modo de impressão, e as capturas
da seção em 320 px claro e 1280 px escuro foram inspecionadas.

### Apresentação das competências em tags

A revisão seguinte condensou os itens em tags e retirou os parágrafos de
descrição da seção. As três categorias e os 25 itens continuam como listas
HTML, com quebra de linha automática e contraste de texto superior a 4,5:1
nos temas claro e escuro. As tags não recebem foco nem representam controles.

As listas mantêm `role="list"` para preservar sua identificação em leitores
de tela que deixam de anunciar listas com `list-style: none`, comportamento
conhecido no Safari/VoiceOver. O Nu HTML Checker não encontrou erros, mas
apontou 15 avisos de papel redundante, um por lista nas cinco versões.
A validação automática do HTML não considera esse efeito do CSS na acessibilidade.
Safari/VoiceOver não foi testado nesta revisão.

Com JavaScript desativado em Chromium, as cinco versões passaram em 30 cenários
de tema e largura de 240/320/1280 px, incluindo espaçamento de texto aumentado,
e em dez cenários com tamanho de texto ampliado para 200% por CSS em 320 px.
Nenhuma etiqueta foi cortada ou causou transbordamento horizontal. A árvore
de acessibilidade expôs 25 itens de lista por idioma. Teclado e foco do link
de salto continuaram funcionando. As 25 tags foram encontradas nos cinco PDFs
de impressão, e as capturas em 320 px claro e 1280 px escuro foram inspecionadas.
Foram conferidas novamente as 413 referências locais e a igualdade dos cinco CSS.
O aumento de texto por CSS não foi apresentado como teste de zoom real do navegador.

### Subcategorias e observações concisas

As três categorias principais mantêm títulos de nível 3 e agora contêm 11
subcategorias com títulos de nível 4, seguidos de listas. O conteúdo anterior
foi desmembrado em 49 tags curtas no formato “habilidade, observação”. As
observações têm cor própria, mas continuam como texto explícito; a informação
não depende apenas da cor. Formação indicada no título aplica-se ao agrupamento.

Nas cinco versões, Chromium com JavaScript desativado expôs os 49 itens e os
11 títulos de nível 4 na árvore de acessibilidade. Foram verificados 30 cenários
de tema/largura e espaçamento, dez cenários de texto ampliado para 200% por CSS,
contraste de texto e observações, teclado e impressão. Os 49 itens apareceram
nos cinco PDFs, e as capturas claro/escuro foram inspecionadas. A leitura de
arquivos pelo esquema `file:` foi bloqueada pela política do navegador do
ambiente; a inspeção foi realizada por HTTP local.

As 16 páginas passaram no Nu HTML Checker sem erros. Permanecem 55 avisos de
`role="list"` redundante, um por lista, pelo motivo documentado na revisão
anterior. As 413 referências locais e a igualdade dos cinco CSS foram conferidas.
O escopo não inclui leitores de tela externos, outros navegadores ou zoom real.

## Limitações e próximos passos

### Conteúdo profissional e galeria

O conteúdo pessoal foi complementado com o relatório REALFORT e o ZIP de
certificados enviados pelo responsável. A seção nativa `details`/`summary`
permite abrir os 17 cursos e formações por teclado, sem JavaScript; o resultado
TOEIC é apresentado separadamente. As fontes e limites de interpretação estão
em [fontes-do-conteudo.md](fontes-do-conteudo.md).

`galeria.html` nos cinco idiomas reúne quatro fotografias com `picture`, WebP,
fallback JPEG, dimensões explícitas, `srcset`, `sizes`, carregamento lazy,
legendas e alternativas textuais. O currículo principal não incorpora nem
requisita fotografias. Imagens otimizadas são compartilhadas pelos idiomas,
com proporção e pessoas preservadas; os originais estão fora da pasta publicada.

Foram verificados os temas claro/escuro, reflow 240/320/1280 px, abertura dos
cursos por teclado, foco do link de salto, navegação entre as páginas e idiomas,
carregamento de fotos e retorno ao currículo. A galeria foi verificada também
nos limites de seus breakpoints. As 16 páginas HTML passaram no Nu HTML Checker
local, sem envio dos dados pessoais ao serviço remoto.

### Ampliação dos templates de idioma

Foram adicionados `pt-PT`, `es-419` e `es-ES`, com conteúdo de exemplo traduzido,
seletores com nomes de idioma e região e alternativas `hreflang` recíprocas.
O seletor permite quebra de linha para acomodar os cinco idiomas em telas estreitas.
`x-default` agora aponta para a página de escolha de idioma.

Na ampliação, as seis páginas HTML passaram no validador Nu da W3C sem mensagens.
Foram verificadas 123 referências locais e os recursos servidos por HTTP.
As cinco versões passaram nos testes de Chromium com JavaScript desativado,
nos temas claro/escuro: larguras de 240/320/1280 px, link de salto, alvos do seletor
de idioma e espaçamento de texto aumentado. Foi inspecionada também uma imagem
do topo da versão espanhola de Espanha em 320 px. CSS e favicon são idênticos
entre as cinco versões. As traduções são templates e ainda precisam de revisão
editorial com o conteúdo profissional definitivo.

Esta revisão não certifica conformidade WCAG AA. Ainda são necessários testes
com leitores de tela e outros navegadores, zoom real de 200%/400%, cores forçadas
e revisão completa do conteúdo e da impressão. Larguras reduzidas são uma
verificação de reflow, não substituem todos os testes de zoom.

O conteúdo profissional foi complementado com as fontes recebidas, e os links
de contato e dos projetos já têm destinos reais fornecidos pelo responsável.
As descrições de Optigrow e SGCS usam somente seu conteúdo público; a análise
dos repositórios privados e a contribuição individual continuam pendentes.
As traduções e os dados profissionais ainda precisam da revisão editorial do
responsável, sem apresentar exemplos antigos como informações confirmadas.

Não houve validação independente completa da folha CSS ou teste de todos os
critérios WCAG. Os testes registrados correspondem às alterações desta revisão.
