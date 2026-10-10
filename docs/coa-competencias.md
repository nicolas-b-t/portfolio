# COA — reorganização das competências

Status: aplicado em 9 de outubro de 2026, somente na página principal
`static/pt-BR/index.html`. Base: versão publicada no commit `824a8b6`.
As demais páginas e idiomas ficam para uma decisão posterior; os commits
desta etapa devem indicar explicitamente o escopo pt-BR, página principal.

## Objetivo e critério

Dar a cada competência um destino principal, preservando informação e reduzindo
sobreposições. Classificar os conhecimentos especializados pelo domínio técnico,
as competências sociais pelo comportamento e as habilidades gerais pela atividade
operacional. Manter “habilidade, observação” e os qualificadores necessários.

## Análise

- Impressoras são periféricos, e as duas tags de manutenção podem ser reunidas.
- A experiência no Instituto Alpha sustenta classificar essa manutenção em Suporte de TI.
- Clivador, cabeamento SC/APC/RJ45 e fusão óptica são específicos de Redes.
- Ferramentas gerais, vivência em altura e preparação de materiais cabem na área operacional.
- Habilitação e direção podem formar uma única tag com a credencial como observação.
- Organização de demandas e preparação física de materiais têm escopos distintos e devem permanecer representadas.
- Aprendizado/adaptabilidade fica mais claro sob Organização e desenvolvimento.

## Realocações e consolidações

| Itens atuais | Destino proposto | Redação proposta |
| --- | --- | --- |
| Manutenção de computadores/periféricos e manutenção de impressoras | Técnicas → Suporte de TI | Manutenção de computadores/periféricos |
| Clivador e cabeamento SC/APC/RJ45 | Técnicas → Redes | Clivador; Cabeamento SC/APC/RJ45, em tags separadas |
| Fusão de fibra óptica, aprendiz | Técnicas → Redes | Fusão de fibra óptica, aprendiz |
| Habilitação A/B, brasileira; direção de carros; direção de motos | Práticas → Condução | Condução de carros/motos, habilitação brasileira A/B |
| Alicates/furadeira; trabalho em altura; preparação de materiais | Práticas → Campo e ferramentas | Preservar as três tags e a observação “vivência orientada” |

“Impressoras” permanece explícito na experiência profissional, que documenta
a atividade. A tag consolidada mantém o escopo de computadores/periféricos,
sem ampliar a descrição para reparação eletrônica ou outros tipos de hardware.

## Estrutura proposta

| Categoria principal | Subcategorias |
| --- | --- |
| Competências técnicas | Suporte de TI; Redes; Web; Programação e dados; Gestão e produtividade; Idiomas |
| Competências sociais | Relacionamento; Organização e desenvolvimento |
| Habilidades práticas e operacionais | Condução; Campo e ferramentas |

O resultado previsto é passar de 11 para 10 subcategorias e de 49 para 46 tags:
35 técnicas, 7 sociais e 4 práticas. A redução vem das duas fusões, enquanto
as demais alterações apenas realocam o conteúdo. Os conhecimentos de formação
mantêm essa indicação no agrupamento, e apoio, aprendiz e escopo do TOEIC
continuam explícitos.

## Execução autorizada

1. Aplicar as realocações e consolidações somente em `static/pt-BR/index.html`.
2. Atualizar a matriz local de evidências e medir o texto final incluindo os títulos.
3. Conferir preservação das informações, hierarquia HTML, referências, contraste, teclado, telas pequenas e impressão.
4. Registrar o resultado e o escopo no commit, realizar push e confirmar a publicação.

Os documentos detalhados e esta proposta ficam em `docs/`.
Desde 10 de outubro de 2026, essa documentação é versionada no Git.

## Resultado da aplicação

- Commit enviado à `main`: `fecc004`, com o escopo explícito no título e na descrição.
- Publicação confirmada pelo workflow `37976876594` e pela conferência dos 42 arquivos públicos.
- A página principal pt-BR passou de 11 para 10 subcategorias e de 49 para 46 tags.
- O texto da seção passou de 149 para 144 palavras contando os títulos e as observações.
- A comparação de hashes confirmou alteração somente em `static/pt-BR/index.html` entre os 43 arquivos de `static/`.
- As 413 referências locais foram conferidas e as cinco folhas CSS permanecem idênticas.
- A página passou no Nu HTML Checker sem erros, com dez avisos já esperados sobre `role="list"`.
- O Chromium com JavaScript desativado confirmou teclado, contraste e seis cenários de largura e tema sem transbordamento.
- Espaçamento aumentado e texto CSS em 200% passaram nas verificações, e as 46 tags apareceram no PDF de impressão.
- As capturas em 320 px no tema claro e 1280 px no tema escuro foram inspecionadas.
