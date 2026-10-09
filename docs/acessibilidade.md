# Aplicação das diretrizes de acessibilidade

Referência: WCAG 2.2, recomendação publicada em 12 de dezembro de 2024.
Data da revisão: 9 de outubro de 2026. Alvo: nível AA.

## Escopo e decisões

Conforme escolha do responsável, as alterações foram aplicadas somente em
`static/pt-BR/` e `static/en/`. Posteriormente, o responsável autorizou remover
as versões antigas e publicar somente `static/` por GitHub Actions.
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

## Limitações e próximos passos

Esta revisão não certifica conformidade WCAG AA. Ainda são necessários testes
com leitores de tela e outros navegadores, zoom real de 200%/400%, cores forçadas
e revisão completa do conteúdo e da impressão. Larguras reduzidas são uma
verificação de reflow, não substituem todos os testes de zoom.

O conteúdo profissional e os contatos ainda são exemplos. Os links de contato
externos precisam receber destinos reais antes da publicação. Quando houver URLs
dos projetos, substitua os avisos por links com nomes que identifiquem cada projeto.

Não houve validação independente completa da folha CSS ou teste de todos os
critérios WCAG. Os testes registrados correspondem às alterações desta revisão.
