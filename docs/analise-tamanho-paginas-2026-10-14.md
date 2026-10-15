# Tamanho das páginas e oportunidades de redução

Data: 14 de outubro de 2026.
Base: checkout local após 69fc73d, com alterações pendentes do Optigrow e da variante en-US.
Escopo: arquivos de static/, seleção de idioma e páginas dos cinco idiomas.
Nenhuma otimização foi aplicada nesta análise.
As unidades kB e MB representam 1000 e 1000000 bytes.

## Inventário

O site contém 62 arquivos, com 3,66 MB em disco.
A documentação, os currículos de referência e as listas de tags externas a static/ não entram nesse total.

| Tipo | Quantidade | Tamanho |
| --- | ---: | ---: |
| HTML | 16 | 263,1 kB |
| CSS | 5 | 44,3 kB |
| SVG | 5 | 2,0 kB |
| JPEG | 18 | 1853,4 kB |
| WebP | 18 | 1494,2 kB |

As fotografias ocupam 91,5% do total.
Esse total inclui diferentes resoluções e formatos da mesma fotografia.
Uma visita não precisa baixar todas essas versões.

## Páginas

| Página | HTML local | HTML com gzip estimado |
| --- | ---: | ---: |
| Seleção de idioma | 1,8 kB | 0,7 kB |
| Principal pt-BR | 66,6 kB | 10,1 kB |
| Principal pt-PT | 29,0 kB | 6,2 kB |
| Principal en-US | 28,5 kB | 6,1 kB |
| Principal es-419 | 29,2 kB | 6,2 kB |
| Principal es-ES | 29,2 kB | 6,2 kB |
| Galerias | 11,9–12,1 kB | 1,9 kB |
| Agradecimentos | 3,7 kB | 1,1 kB |

Cada página referencia um CSS de 8,9 kB e um favicon de 0,4 kB.
O CSS resulta em aproximadamente 2,5 kB com gzip local.
As páginas principais e de agradecimentos não contêm imagens.
O CSS já recebido pode ser reutilizado pelo navegador nas páginas do mesmo idioma.

O servidor publicado respondeu com Content-Encoding: gzip e Content-Length: 10581 para a página principal pt-BR.
O cabeçalho Cache-Control indicou max-age=600.
Esse resultado corresponde à versão publicada, que difere do checkout local.
As demais medidas gzip são estimativas de compressão local, sem cabeçalhos HTTP.
O tamanho em disco não deve ser somado diretamente ao tamanho comprimido de transferência.

## Galeria no navegador

O ensaio usou Chromium, contextos novos e altura de 900 pixels CSS.
O navegador selecionou WebP. Cada galeria contém nove fotografias.

| Largura CSS | Densidade de pixels | Fotografias selecionadas |
| --- | ---: | ---: |
| 320 px | 1 | 466,1 kB |
| 320 px | 2 | 466,1 kB |
| 1280 px | 1 | 466,1 kB |
| 1280 px | 2 | 1028,1 kB |

Esses valores incluem somente as imagens. Some HTML e CSS para estimar a visita sem cache.
Uma galeria fica próxima de 487,5 kB sem compressão textual, nos três primeiros cenários.
O cenário de densidade dupla em tela grande fica próximo de 1049,4 kB.
Não foram incluídas fotografias maiores abertas por seus links.

As imagens têm srcset, sizes e loading="lazy".
Neste ensaio local, todas já constavam nas entradas de recursos antes da rolagem completa.
Não se deve presumir uma economia inicial fixa apenas pela presença de loading="lazy".
A seleção de resolução também pode variar com navegador, densidade, cache e condições de rede.

## Prioridades sugeridas

1. Avalie a compressão da galeria, começando pela fotografia da rede aérea rural.
2. Considere variantes menores para as miniaturas, após comparar a qualidade visual.
3. Considere um CSS compartilhado para os cinco idiomas.
4. Avalie a minificação somente depois das oportunidades com maior efeito.

A fotografia rural representa 159,7 kB na versão WebP de 640 pixels.
Ela concentra 34,3% do volume das nove fotografias nessa resolução.
A versão WebP maior ocupa 327,2 kB.
Uma recompressão pode reduzir esses valores, mas o ganho exige medição e comparação visual.

Compartilhar o CSS retiraria quatro cópias idênticas, aproximadamente 35,4 kB em disco.
Isso pode evitar downloads de URLs distintas quando o visitante troca de idioma.
Não reduz o primeiro CSS necessário para abrir uma página.

A cópia oculta do currículo pt-BR ocupa aproximadamente 30 kB do HTML serializado.
Uma simulação de remoção reduziu o gzip em aproximadamente 2,9 kB.
Ela é uma função autorizada para extração de dados e deve ser preservada enquanto essa decisão estiver vigente.
Os resultados ATS existentes não demonstram que sua remoção seria equivalente.

Uma triagem de espaços entre elementos reduziu o gzip do HTML pt-BR em aproximadamente 1,6 kB.
No HTML inglês, a diferença foi de aproximadamente 0,3 kB.
Isso não constitui um minificador validado. Uma implementação exigiria conferir espaços significativos e a impressão.
Não há justificativa, nesta análise, para acrescentar um processo complexo de compilação por essa economia.

## Fontes e limites

Os [dados de medição](medicao-tamanho-paginas-2026-10-14.json) contêm o inventário e as imagens selecionadas por cenário.
As medições de tamanho não são ensaios de velocidade, Core Web Vitals ou qualidade visual.
As referências explicam [imagens responsivas](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images)
e [carregamento diferido](https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/Lazy_loading).
