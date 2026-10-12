# Referências para desenvolvimento web

Consulta: 12 de outubro de 2026. Escopo: portfólio estático com HTML e CSS.
As fontes oficiais foram preservadas integralmente, sem tradução ou alteração.
O [manifesto](manifesto-web-2026-10-12.json) registra origem, estado, versão, data, licença, tamanho e SHA-256.
A data dos nomes de arquivo identifica a captura, não a publicação da especificação.

## Documentos e aplicação

| Cópia local | Estado da publicação | Aplicação no projeto |
| --- | --- | --- |
| [HTML Living Standard](whatwg/html-living-standard-2026-10-12.html) | Living Standard | Estrutura, semântica, links, imagens responsivas e controles nativos |
| [Encoding Living Standard](whatwg/encoding-2026-10-12.html) | Living Standard | UTF-8 e interpretação de texto |
| [CSS Snapshot 2026](w3c/css-snapshot-2026-2026-10-12.html) | Group Note | Mapa dos módulos CSS e seus estados |
| [CSS Flexible Box Layout Level 1](w3c/css-flexbox-1-2026-10-12.html) | Candidate Recommendation Draft | Tags e navegação com quebra de linha |
| [CSS Grid Layout Level 1](w3c/css-grid-1-2026-10-12.html) | Candidate Recommendation Draft | Grades de projetos e fotografias |
| [CSS Values and Units Level 3](w3c/css-values-3-2026-10-12.html) | Candidate Recommendation Draft | Unidades relativas e cálculos de tamanho |
| [CSS Box Sizing Level 3](w3c/css-sizing-3-2026-10-12.html) | Working Draft | Dimensionamento fluido e conteúdo longo |
| [CSS Custom Properties Level 1](w3c/css-variables-1-2026-10-12.html) | Candidate Recommendation Snapshot | Variáveis de cores, espaçamento e temas |
| [Media Queries Level 5](w3c/mediaqueries-5-2026-10-12.html) | Working Draft | Temas, movimento reduzido e condições de apresentação |
| [CSS Fragmentation Level 3](w3c/css-break-3-2026-10-12.html) | Candidate Recommendation | Quebras de página na impressão |
| [ARIA in HTML](w3c/html-aria-2026-10-12.html) | Recommendation | Uso de ARIA compatível com elementos nativos |
| [WCAG Evaluation Methodology 2.0](w3c/wcag-em-2-2026-10-12.html) | Group Note | Método de avaliação de acessibilidade |
| [RFC 5646 — Tags for Identifying Languages](ietf/rfc-5646-2026-10-12.txt) | Best Current Practice | Etiquetas lang e hreflang |
| [RFC 9110 — HTTP Semantics](ietf/rfc-9110-2026-10-12.txt) | Standards Track | Tipos de conteúdo, respostas e requisições condicionais |
| [RFC 9111 — HTTP Caching](ietf/rfc-9111-2026-10-12.txt) | Standards Track | Cache de recursos em hospedagem estática |
| [RFC 9649 — WebP Image Format](ietf/rfc-9649-2026-10-12.txt) | Informational | Formato das imagens otimizadas |
| [WCAG 2.2](w3c/wcag-2.2-recomendacao-2024-12-12.html) | Recommendation, 12 de dezembro de 2024 | Critérios de acessibilidade, alvo AA |

## Como escolher a referência

Use HTML Living Standard para sintaxe, semântica, elementos e atributos HTML.
Consulte imagens responsivas, `picture`, `srcset`, `sizes`, dimensões e carregamento tardio antes de alterar fotografias.
Use Encoding Standard para codificação e UTF-8.
Use ARIA in HTML para verificar atributos ARIA permitidos nos elementos nativos.
Use WCAG 2.2 para critérios de acessibilidade.
Use WCAG-EM 2.0 para organizar a avaliação e suas evidências.

Use os módulos CSS correspondentes às propriedades alteradas.
O CSS Snapshot organiza especificações por estabilidade, não por adoção nos navegadores.
Candidate Recommendation e Working Draft não significam Recommendation aprovada.
Living Standard tem manutenção contínua e exige identificar a captura usada.
Group Note oferece informação e método, sem acrescentar critérios normativos à WCAG.
O RFC de WebP é informativo. Ele não constitui um Internet Standard.

Para compatibilidade, consulte [Baseline](https://web.dev/baseline) e teste os navegadores relevantes.
Baseline é uma orientação de interoperabilidade, não certificação de acessibilidade ou norma de conformidade.
A ausência de scripts no site continua definida pelas instruções do projeto.

## Otimização e idiomas

Use RFC 9110 para semântica HTTP, tipos de conteúdo e requisições condicionais.
Use RFC 9111 para cache e validação de recursos.
A configuração desses recursos depende da hospedagem. Os documentos não alteram o GitHub Pages automaticamente.
Use RFC 9649 para interpretar o formato WebP.
Compare bytes, dimensões e qualidade visual antes de substituir imagens.
Preserve JPEG como alternativa quando necessário.

RFC 5646 integra BCP 47 e define etiquetas de idioma.
BCP 47 também inclui RFC 4647, sobre correspondência entre etiquetas.
Essa correspondência não integra o seletor manual atual do portfólio.
Mantenha `lang` e `hreflang` coerentes nas cinco versões.

## Licenças e limites locais

Os avisos de direitos autorais e licença permanecem dentro de cada documento.
As [licenças W3C](w3c/licencas/) acompanham as cópias aplicáveis.
Os documentos WHATWG identificam CC BY 4.0 para o texto e BSD de três cláusulas para trechos incorporados em código.
Os RFCs preservam o aviso do IETF Trust e suas condições de reprodução.
A atribuição a cada documento está no manifesto e no próprio original.

Estes arquivos não formam um espelho completo para consulta sem conexão.
Estilos, imagens, scripts oficiais e links complementares podem depender da internet.
Os scripts originais foram preservados como partes das referências. Não os incorpore ao site publicado.
O GitHub Pages recebe somente `static/`.
A inclusão dessas fontes não comprova conformidade nem implementação de todas as funcionalidades descritas.

## Atualizar e verificar

1. Consulte a origem oficial registrada no manifesto.
2. Confira o estado e a data da versão publicada.
3. Distinga recomendações, notas e rascunhos.
4. Baixe a versão escolhida para um arquivo novo.
5. Preserve o documento integral e os avisos de licença.
6. Registre a URL de origem e a versão datada, quando existir.
7. Registre o tamanho e o SHA-256.
8. Confira o título e o estado no arquivo recebido.
9. Atualize este índice e o manifesto.
10. Revise os efeitos da nova referência antes de alterar o site.

Para conferir uma cópia no PowerShell, execute:

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath docs/referencias/whatwg/html-living-standard-2026-10-12.html
```

Compare o resultado com o manifesto.
Use o [relatório de verificação](../relatorio-final-verificacao-pt-br-2026-10-12.md) para repetir os ensaios do projeto.
