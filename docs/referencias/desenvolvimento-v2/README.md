# Base documental de desenvolvimento — versão 2

Seleção realizada em 30/10/2026 para o portfólio estático HTML/CSS.
Foram analisados os catálogos de `REPERTORIO_TECNICO` e `fas-doddir`, os sumários e trechos pertinentes das candidatas, além de fontes oficiais complementares.
O nome `fas-ddoir` informado na solicitação correspondeu à pasta encontrada `fas-doddir`.

São **41 obras ou coleções, 74 arquivos e 66.843.699 bytes (63,75 MiB)**.
Abra o [índice local](indice-local.md) para consultar os documentos. O [catálogo](catalogo.json) conserva os identificadores, caminhos de origem relativos aos acervos, URLs e condições recebidas.
O [fluxo da versão 2](../../desenvolvimento-v2.md) relaciona as fontes com decisões e verificações.

## Plano e critérios de seleção

A base atende planejamento, requisitos, conteúdo, implementação, acessibilidade, idiomas, revisão, testes, publicação e manutenção.
Foram priorizados documentos aplicáveis à arquitetura existente, fontes institucionais e materiais com conteúdo local legível.
O pedido do responsável autoriza selecionar e copiar. Não se registra aprovação individual de cada obra, interpretação ou requisito em seu nome.

| Grupo | Seleção e aplicação | Limites |
| --- | --- | --- |
| Gestão, requisitos e testes | PM² 3.1 em português; IREB CPRE 3.3.0 e glossário 2.2.0; ISTQB CTFL 4.0.1 | Referências de método; adaptar ao porte do projeto; não declarar certificações |
| Segurança do desenvolvimento | NIST SP 800-218 v1.1 | Aplicar proteção de fontes, revisão e controle de mudanças; não transformar o site estático em sistema com autenticação ou backend |
| HTML e CSS | WHATWG HTML, Encoding e URL; módulos CSS de cascata, layout, texto, cores, fontes, seletores, unidades e mídia; CSS 2.1 para fundamentos e impressão; guia HTML/CSS do Google | Cópias datadas; módulos têm maturidades diferentes. Consultar o status interno e testar suporte antes de usar propriedades |
| Acessibilidade | WCAG 2.2 em inglês e português, ARIA in HTML, Accessible Name 1.2 e WAI-ARIA 1.2 | Texto normativo e apoio não substituem ensaio manual. Preferir semântica nativa |
| Documentação e redação | Diátaxis: 17 páginas catalogadas; MADR 4.0.0: quatro modelos e duas licenças; ASD-STE100 edição 9; orientação local sobre requisitos | Seleção de coleção, não garantia de espelho integral. ASD é cópia pessoal privada; a adaptação portuguesa não é tradução oficial |
| Revisão e versões | Google Code Review: 13 páginas catalogadas; Pro Git, 2ª edição | Aplicar práticas pertinentes a HTML/CSS e Git; preservar alterações anteriores |
| FAS histórico | FAS-1653, NCSC-TG-006-88: seções 7 e 9.1, controle de configuração e baseline; FAS-1654: seção 2, princípios de documentação | Contexto TCSEC histórico. Não importar classes de segurança, obrigações militares ou alegações de conformidade. A data de tg007 não foi confirmada no HTML |
| Complementos oficiais | RFC 5646, workflows GitHub Pages, Media Queries 5 e CSS Color Adjustment 1 | Cobrem lacunas da seleção dos acervos; identificar rascunho e candidata a recomendação corretamente |

## Comparação com fontes oficiais

Em 30/10/2026, o [HTML Living Standard](https://html.spec.whatwg.org/) indicava atualização de 30/10/2026; a cópia do acervo indica 20/10/2026.
A base preserva essa cópia de 20/10, sem alegar equivalência completa com a edição online posterior.
A [WCAG 2.2](https://www.w3.org/TR/WCAG22/) consultada identifica a recomendação de 12/12/2024, correspondente à URL da cópia inglesa selecionada.
Essa comparação confirma a identificação da edição, não igualdade de todos os bytes com a publicação remota.

Foram salvos quatro complementos oficiais:

- EXT-01: [RFC 5646](https://www.rfc-editor.org/rfc/rfc5646.txt), para etiquetas de idioma.
- EXT-02: [GitHub Pages: workflows personalizados](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages), para configuração e permissões de publicação.
- EXT-03: [Media Queries Level 5](https://www.w3.org/TR/2026/WD-mediaqueries-5-20260219/), Working Draft de 19/02/2026, para preferências de movimento e tema.
- EXT-04: [CSS Color Adjustment Level 1](https://www.w3.org/TR/2025/CR-css-color-adjust-1-20251216/), Candidate Recommendation Snapshot de 16/12/2025, para esquemas de cor e ajustes do agente de usuário.

URLs registram a procedência. A consulta cotidiana deve usar os arquivos locais.

## Exclusões e lacunas

FAS-0719, DTM 21-001, “DoD Public Web Program”, foi examinado e excluído: aplica-se a órgãos do DoD e a página 1 prevê expiração em 15/06/2025.
Não foi feita investigação de atos posteriores; a cópia não é base normativa para este portfólio.
Os demais temas militares, COMSEC, operações, infraestrutura complexa, Android, linguagens de programação e protocolos sem aplicação direta foram excluídos pelo escopo.
NASA, modelagem extensa e conjuntos completos de normas de engenharia acrescentariam carga documental desproporcional nesta etapa.

A base não comprova fatos profissionais, direitos sobre fotografias ou certificados. Para isso, continuam valendo as fontes factuais do projeto.
Não inclui uma matriz atualizada de compatibilidade de navegadores, todos os documentos citados por cada norma nem todas as técnicas complementares da WCAG.
Essas lacunas devem ser tratadas quando a mudança depender delas. Não atribuir a uma cópia datada a condição de norma mais recente.

## Preservação, privacidade e disponibilidade local

Os 70 arquivos dos acervos foram copiados sem alteração. Os quatro complementos foram baixados das fontes oficiais e copiados sem alteração.
As 74 cópias foram comparadas diretamente com os arquivos de origem ou os downloads recebidos; os bytes são idênticos.
Os originais externos não foram modificados. Avisos de autoria e licenças internos permanecem intactos; as licenças do MADR foram incluídas.
Não se presume autorização de redistribuição a partir da disponibilidade no acervo.

`fontes-local/` fica excluída do Git e fora de `static/`. A pasta deve permanecer no computador para consulta.
O índice, o catálogo e as orientações podem acompanhar o repositório; os originais privados não acompanham um clone.
Antes de trocar de computador, preserve uma cópia privada desta pasta completa. Não execute limpezas que apaguem arquivos ignorados pelo Git.

Os PDFs foram abertos por `pdfinfo` e tiveram texto inicial extraído. Os HTMLs foram inspecionados como texto, sem executar scripts.
O texto das fontes está incorporado nos arquivos locais. Estilos, imagens, scripts e navegação entre páginas originais podem depender da rede.
Não foi produzido nem validado um espelho visual completo offline. Use o índice relativo para abrir documentos e leitura textual para consulta independente da rede.
Os scripts presentes nos documentos recebidos são parte das cópias oficiais e nunca integram o site publicado.

## Atualização da base

### Conferência da entrega de 30/10/2026

- Todos os 74 caminhos do catálogo existem, têm o tamanho registrado e são arquivos reais, sem links simbólicos.
- Os links locais deste plano e do índice foram resolvidos com sucesso dentro do projeto.
- A conferência final leu apenas a base local, sem chamadas de rede ou leitura dos acervos externos. Não houve isolamento de rede imposto pelo sistema.
- As 74 fontes estão ignoradas pelo Git; o workflow existente publica somente `static/`.
- `git diff --check` e `git diff --cached --check` passaram. As alterações anteriores, inclusive as já preparadas para commit, foram preservadas.
- O comando `tree -a -L 3 -I .git` não é compatível com o `tree.com` disponível no Windows; a nova estrutura foi conferida por listagem PowerShell limitada à base.
- Esta entrega altera documentação e exclusões do Git. Não houve alteração do site, ensaio visual, commit ou publicação nesta tarefa.

### Próximas alterações documentais

Preserve esta seleção e registre futuras substituições com edição, motivo e efeitos nas decisões.
Não sobrescreva silenciosamente documentos usados como fundamento. Mudanças de escopo ou novos requisitos devem ser explicitados ao responsável.
Depois do encerramento do acesso aos acervos, o trabalho continua com esta pasta e as demais fontes já presentes no projeto.
