# CSS compartilhado entre idiomas

Data: 14 de outubro de 2026.
Escopo: cinco idiomas, página principal, galeria e agradecimentos. Inclui a seleção de idioma.

## Estrutura vigente

Todas as páginas usam static/assets/css/styles.css.
As cinco cópias anteriores foram removidas.
O volume de CSS passou de 44265 para 8848 bytes, uma redução de 35417 bytes, aproximadamente 80%.
Essa economia se refere ao conjunto publicado, não ao primeiro acesso de uma página.
As páginas agora solicitam a mesma URL de CSS, inclusive ao trocar de idioma.
O reaproveitamento depende das condições de cache do navegador e da hospedagem.

As páginas nas pastas de idioma usam ../assets/css/styles.css.
A seleção de idioma usa assets/css/styles.css.
Páginas em outros níveis devem calcular o caminho relativo ao próprio HTML.
Os links não dependem da raiz do domínio.

Não foram adicionados scripts, dependências, imports CSS ou etapas de compilação.
Os estilos visuais foram preservados.
A regra de impressão do contato usa section.contact-section, em vez de IDs traduzidos.
Cada currículo recebeu essa classe. Os IDs existentes e suas âncoras permanecem iguais.

## Novos idiomas e páginas

1. Referencie o CSS compartilhado com caminho relativo.
2. Preserve as classes estruturais das páginas equivalentes.
3. Use contact-section na seção de contato do currículo.
4. Atualize lang, hreflang e os links de idioma.
5. Confira textos longos, teclado e impressão.

Não copie a folha de estilos para cada idioma.
Adicione regras específicas somente quando uma necessidade real de conteúdo ou direção de escrita justificar a diferença.
As [instruções gerais](../AGENTS.md) e o [README](../README.md#organização-do-site) registram essa estrutura.

## Verificação

Foram comparadas capturas antes e depois nas 16 páginas, em 32 cenários.
Os cenários usaram 320 pixels em tema claro e 1280 pixels em tema escuro.
Os hashes das capturas e as medidas de layout permaneceram iguais.
Não houve rolagem horizontal.

O link para pular ao conteúdo transferiu o foco para main nas 15 páginas com cabeçalho.
Os controles de cursos abriram por teclado nos cinco currículos.
A impressão mostrou 17 cursos em cada currículo e preservou break-inside: avoid no contato.
Todos os links locais foram resolvidos. As 16 páginas referenciam um único arquivo CSS.
A seleção de idioma, o currículo pt-BR e a galeria en-US também carregaram o CSS sob o prefixo /static/.
git diff --check passou.

Os [resultados da comparação](verificacao-css-compartilhado-2026-10-14.json) preservam medidas e hashes das capturas.
O teste usou Chromium. Não foram repetidos os testes completos de acessibilidade em outros motores.
A [análise de tamanho anterior](analise-tamanho-paginas-2026-10-14.md) registra o estado com cinco cópias do CSS.
