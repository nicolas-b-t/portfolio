# Revisão de código e acessibilidade

Data: 14 de outubro de 2026.
Base Git: a0863e5, com as alterações solicitadas posteriormente ainda no checkout.
Escopo: cinco idiomas, página principal, galeria e agradecimentos. Inclui a página de seleção de idioma.

## Adequações

O link para pular ao conteúdo passou a ser o primeiro elemento do corpo da página pt-BR.
Antes, a cópia oculta do currículo precedia esse link. O axe apontava uma ocorrência na regra region.
A ocorrência deixou de aparecer após a mudança.

Os links diretamente contidos em títulos h3 e h4 passaram a ter área mínima de 24 por 24 pixels CSS.
O ajuste foi aplicado aos cinco arquivos CSS. Os arquivos permanecem idênticos.
O site publicado continua sem JavaScript, fontes remotas ou dependências novas.
Os scripts de verificação foram usados somente no ambiente de manutenção.

O commit também reúne as alterações anteriores de termos, traduções das tags, vínculo Contractor e descrição de condução.
As tags, qualificações, datas e títulos oficiais foram preservados nesta revisão de acessibilidade.

## Verificações

| Verificação | Resultado |
| --- | --- |
| 16 páginas, em Chromium 151 | 80 cenários sem rolagem horizontal ou imagens inválidas |
| Larguras de 320 e 1280 pixels CSS | Temas claro e escuro verificados |
| Texto a 200%, em largura de 640 pixels | Sem rolagem horizontal |
| Espaçamento ampliado, nas 16 páginas | Sem rolagem horizontal em 320 pixels |
| Teclado, 318 alvos | Foco visível, dentro da janela e fora do bloco oculto |
| Tab e Shift+Tab | Navegação direta e reversa verificadas |
| Link para pular ao conteúdo | Enter transferiu o foco para main nas 15 páginas com cabeçalho |
| Troca de idioma | Ativação por teclado verificada nas 15 páginas traduzidas |
| Cursos recolhíveis | Enter abriu e Espaço fechou os controles nos cinco currículos |
| Impressão dos cursos | 17 cursos, uma única vez, com o controle aberto e fechado |
| Cópias de cursos na tela e impressão | Títulos, instituições, datas e cargas horárias iguais nos cinco idiomas |
| Movimento reduzido | Rolagem suave desativada nos testes |
| Cores forçadas | Indicador de foco preservado no ensaio pt-BR |
| axe-core 4.10.3 | 32 execuções, sem violações ou resultados inconclusivos |
| HTML5 e CSS | Nenhum erro de análise nas 16 páginas e nos cinco CSS |
| Links locais, recursos, âncoras e favicon | Destinos locais encontrados, inclusive âncoras entre páginas |
| git diff --check | Sem erros |

O axe avaliou regras WCAG A e AA disponíveis até 2.2, além de boas práticas.
As execuções incluíram contraste nos temas claro e escuro.
O ensaio de espaçamento usou entrelinha 1,5, espaçamento entre letras 0,12 em e entre palavras 0,16 em.
Os parágrafos receberam margem inferior de 2 em.

A análise de sintaxe usou html5lib 1.1 e tinycss2 1.4.0.
Ela não substitui um validador completo de conformidade HTML ou CSS.
O site não recebeu dependências dessas ferramentas.

Foram inspecionadas capturas do início, das competências, da galeria, dos projetos e dos agradecimentos.
As capturas mostram reorganização do conteúdo e preservação das qualificações em telas pequenas.
Uma cópia pública do currículo foi impressa em PDF, com 12 páginas.

## Evidências e limites

- [Resultados de navegador, teclado e axe](verificacao-acessibilidade-2026-10-14.json).
- [Espaçamento, navegação reversa e idiomas](verificacao-complementar-2026-10-14.json).
- [Análise de sintaxe](verificacao-sintaxe-2026-10-14.json).
- [Captura das competências em tema claro](evidencias-acessibilidade-2026-10-14/pt-BR-competencias-320-light.png).
- [Captura das competências em tema escuro](evidencias-acessibilidade-2026-10-14/pt-BR-competencias-320-dark.png).
- [Currículo impresso](evidencias-acessibilidade-2026-10-14/curriculo-pt-BR.pdf).

A largura de 320 pixels testa a reorganização correspondente a uma janela de 1280 pixels com ampliação de 400%.
Não foi usado o comando de zoom da interface de um navegador desktop.
Não foram realizados testes com leitores de tela, Firefox, Safari ou dispositivos móveis físicos.
Os resultados não constituem certificação WCAG ou STE.
Os links externos não foram percorridos integralmente. A verificação de destinos abrange os recursos locais.

O registro ATS anterior preserva suas entradas e saídas originais.
Uma nota nesse registro identifica o ajuste posterior do texto de condução e a nova posição do link de salto.
As traduções das tags continuam iguais e o manifesto aponta para a fonte HTML atual.

A contagem de 98 países solicitada para a PID provém de uma publicação do Detran-PR de 2006.
Ela não foi confirmada como contagem atual nesta revisão de acessibilidade.

Referências: [WCAG 2.2 e documentos explicativos](https://www.w3.org/WAI/WCAG22/Understanding/),
[axe-core](https://github.com/dequelabs/axe-core) e
[publicação do Detran-PR](https://www.detran.pr.gov.br/Noticia/DetranPR-comeca-emitir-PID).
