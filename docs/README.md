# Documentação do portfólio

As [orientações gerais](../AGENTS.md) definem as regras permanentes.
Este índice reúne os documentos necessários à manutenção do conteúdo vigente.

## Uso e verificação

| Documento | Finalidade |
| --- | --- |
| [README da raiz](../README.md) | Estrutura, execução local e publicação |
| [Guia de uso](referencias/guia-de-uso.md) | Edição, consulta aos acervos e recuperação de fontes |
| [Guia de redação](guia-de-redacao.md) | Clareza e precisão do texto autoral |
| [Currículos gerais V3 em PDF](curriculos/v3/README.md) | Dez PDFs versionados, com dois formatos nos cinco idiomas e manifesto de integridade |
| [Sincronização vigente dos idiomas](sincronizacao-idiomas-2026-10-14.md) | Conteúdo pt-BR aplicado às quatro traduções, verificações estáticas e limpeza |
| [Tamanho das páginas](analise-tamanho-paginas-2026-10-14.md) | Inventário, gzip, imagens escolhidas pelo navegador e oportunidades de redução |
| [CSS compartilhado](css-compartilhado-2026-10-14.md) | Estrutura para novos idiomas, economia e comparação visual das 16 páginas |
| [Revisão de código e acessibilidade de 14 de outubro](revisao-codigo-acessibilidade-2026-10-14.md) | Correções, teclado, apresentação, contraste e evidências das 16 páginas |
| [Síntese dos testes ATS e orientações para currículos](sintese-testes-ats-e-orientacoes-para-curriculos-2026-10-13.md) | Resultados, limites e procedimento para este portfólio e futuros currículos |
| [Histórico dos testes ATS](historico-ats/README.md) | Sete registros anteriores preservados integralmente em ZIP, com manifesto e hashes |
| [Lista geral de tags](../Lista_de_tags/README.md) | Cópia de consulta, instruções para leitura e traduções para outros sistemas de escrita |
| [Teste da lista geral de tags](verificacao-lista-geral-tags-2026-10-14.json) | Integridade da cópia, traduções e resultados da extração do bloco oculto |
| [Normalização de termos e verificação integral](normalizacao-tags-pt-br-2026-10-14.md) | Nomes padronizados, cobertura das três bases de tags e limites |
| [Tags multilíngues](tags-multilingues/README.md) | Glossário, correspondências e manifesto dos 14 arquivos traduzidos |
| [Manifesto do cvats](referencias/ats/manifesto-cvats-2026-10-14.json) | Clone, versão, licença, fontes e limites da execução |
| [Revisão de linguagem simples pt-BR](revisao-linguagem-simples-pt-br-2026-10-13.md) | Expressões vagas, repetições, propostas e limites das fontes |
| [Relatório do site de 13 de outubro](relatorio-verificacao-site-2026-10-13.md) | Alterações e verificações gerais da versão daquela data |
| [Resultados do site de 13 de outubro](verificacao-site-2026-10-13.json) | Ensaios de apresentação e conteúdo daquela versão |
| [Revisão de experiências e projetos pt-BR](experiencias-e-projetos-pt-br-2026-10-14.md) | Descrições, estrutura dos projetos, tecnologias confirmadas e evidências do SGCS |
| [Registro anterior das tags](referencias/ats/verificacao-tags-2026-10-13.json) | Contextos, referências e limites da versão anterior dos cinco idiomas |
| [Tags e correspondências anteriores pt-BR](historico-ats/README.md#exportações-substituídas) | Evidências e comparação após o commit-base 6a96e0b, anteriores à normalização atual |
| [Currículo textual anterior pt-BR](historico-ats/README.md#exportações-substituídas) | Exportação histórica preservada em ZIP, com manifesto e hashes |
| [Manifesto dos parsers públicos](referencias/ats/manifesto-parser-publico-2026-10-13.json) | Origens, commits, licenças e hashes das cópias locais |
| [Histórico consolidado](registro-de-desenvolvimento.md) | Decisões duradouras |
| [Otimização de imagens](otimizacao-imagens.json) | Dimensões, tamanhos e hashes |

Os relatórios substituídos e os auxiliares de execução foram retirados na limpeza de 13 de outubro de 2026.
O histórico Git preserva os arquivos anteriormente versionados.
Os READMEs e as licenças recebidos dos fornecedores permanecem com os respectivos acervos.

Na limpeza de 14 de outubro, sete registros ATS anteriores passaram para o arquivo compactado em historico-ats/.
A síntese e a verificação da lista geral descrevem o estado atual. O histórico compactado preserva todas as evidências anteriores.
As fontes recebidas, licenças, dicionários e declarações continuam disponíveis nas condições registradas.

O TXT acompanha as alterações recentes das tags no currículo pt-BR.
Os resultados anteriores de navegador e impressão não foram repetidos nesta comparação.
O currículo textual e os resultados da extração permanecem na documentação. Eles não integram o site publicado.
A síntese dos testes ATS centraliza a aplicação dos resultados. O inventário, as saídas e os manifestos preservam as evidências.

## Fontes e referências

| Assunto | Onde consultar |
| --- | --- |
| HTML, CSS, HTTP e imagens | [Referências web](referencias/guia-de-uso.md#referências-web) |
| Acessibilidade | [W3C](referencias/guia-de-uso.md#acessibilidade-e-css-w3c) |
| Redação | [ASD-STE100](referencias/guia-de-uso.md#redação-asd-ste100) |
| Idiomas | [QECR e STANAG 6001](referencias/guia-de-uso.md#referências-de-idiomas) |
| Acervo ATS | [Fontes, dicionários e classificações](referencias/guia-de-uso.md#insumos-ats-e-classificações) |
| Declarações profissionais | [Ferramentas e atividades informadas](fontes/competencias-declaradas.json) |
| Currículos originais | [Versões recebidas do Google Drive](fontes/curriculos/README.md) |
| Condução internacional | [Fontes e limites do texto sobre CNH e PID](referencias/conducao-internacional.md) |
| Links de cursos e projetos | [Instituições, destinos e decisões de redação](referencias/links-instituicoes.md) |
| Fontes acadêmicas | [Documentos e limites](referencias/guia-de-uso.md#fontes-acadêmicas) |
| Originais e hashes | [Manifestos](referencias/guia-de-uso.md#conferir-os-originais) |

## Versionamento e publicação

A documentação integra o repositório desde 10 de outubro de 2026.
O GitHub Pages recebe somente static/.
Versionar um documento não o adiciona às páginas do currículo.
Os currículos oficiais integrais, os certificados e os documentos restritos permanecem fora do checkout versionado.
A autorização de 15 de outubro de 2026 inclui os dez [PDFs gerais V3](curriculos/v3/README.md) no repositório, sem exclusão pelo Git.
A exportação TXT deriva dos dados destinados ao currículo público.

## Referências locais

Os seis PDFs privados do acervo inicial não acompanham clones.
As cópias comerciais em referencias/ats/originais-local/ permanecem excluídas do Git.
Os clones completos dos guias editoriais em referencias/ats/repositorios-local/ também permanecem excluídos.
O PPC público da Fatec Franco da Rocha permanece em fontes/academico/originais-local/, excluído do Git.
O [manifesto acadêmico](fontes/academico/manifesto.json) permite recuperar e conferir essa cópia.
O [manifesto editorial](referencias/ats/manifesto-fontes-editoriais-2026-10-13.json) registra URLs, commits, licenças e hashes para recuperação.
O guia reúne as [condições comerciais](referencias/guia-de-uso.md#licenças-e-cópias-comerciais) e os caminhos dos originais.

1. Obtenha cada referência conforme suas condições de uso.
2. Solicite uma cópia autorizada ao responsável quando necessária.
3. Salve o arquivo no caminho registrado no manifesto.
4. Compare o tamanho e o SHA-256 antes de usar a cópia.
