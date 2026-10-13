# Sincronização — cinco idiomas, currículo, galeria e agradecimentos

Data: 13 de outubro de 2026. Base Git: faa2b98, com alterações locais anteriores preservadas.
A revisão atualizou 12 páginas traduzidas a partir do pt-BR vigente.
Os textos pt-BR, as fotografias e os cinco arquivos CSS foram preservados.

## Conteúdo sincronizado

As traduções apresentam as mesmas três experiências profissionais, três projetos e 17 cursos.
RealFort Sistemas substituiu o nome antigo nas versões traduzidas.
O portfólio aparece na seção de projetos. O SGCS aparece como projeto acadêmico com MVP em desenvolvimento.
As descrições distinguem a participação pessoal, a participação das equipes e a formação em andamento.

Os currículos traduzidos reproduzem os grupos de competências e cursos do pt-BR.
Os títulos oficiais, as instituições, as datas e as cargas horárias dos cursos permanecem iguais.
Cada idioma possui uma cópia recolhível para tela e uma cópia exclusiva para impressão.
A antiga âncora de projetos futuros permanece no cartão do SGCS.

As galerias apresentam oito fotografias de redes e uma fotografia de eletrônica.
Os textos alternativos, as legendas e os rótulos dos links foram traduzidos.
Os atributos sizes seguem a grade e as bordas da versão pt-BR.
Os agradecimentos preservam as quatro pessoas e os destinos dos perfis.

Não foram aplicadas recomendações ATS aos textos publicados.
O [relatório de palavras-chave](referencias/ats/analise-palavras-chave-2026-10-13.md) registra a análise posterior e seus limites.

## Verificações e evidências

| Verificação | Resultado e evidência |
| --- | --- |
| HTML local | Zero erros em 15 páginas. Nu HTML Checker 26.10.12, commit 0a70d65. [Resultado JSON](validacao-html-idiomas-2026-10-13.json) |
| Avisos HTML | 105 avisos sobre role=list em listas nativas. A justificativa de compatibilidade permanece no relatório anterior |
| Estrutura | 16 páginas, incluindo a escolha de idioma, sem scripts, IDs duplicados ou destinos locais ausentes. [Registro](verificacao-estrutura-idiomas-2026-10-13.json) |
| Idiomas | lang, hreflang, destinos de troca de idioma e âncoras conferidos nas 15 páginas |
| CSS | Cinco cópias idênticas, com o mesmo SHA-256 anterior à tarefa. Nenhuma alteração final nos estilos |
| Navegador | 15 páginas em Chromium 151.0.7922.34, com JavaScript desativado. Zero falhas nos cenários registrados. [Resultados](testes-idiomas-2026-10-13.json) |
| Teclado | Tab e Shift+Tab percorreram os controles. O salto ao main e o foco visível foram conferidos |
| Cursos | Enter e Espaço alternaram o controle. Dez cenários de impressão apresentaram 17 títulos visíveis, sem repetição |
| Fotografias | Os nove links de cada galeria abriram por teclado. As imagens locais carregaram nos cenários examinados |
| Reorganização | Sem excesso de largura a 320 e 1280 pixels nas 15 páginas |
| Texto e temas | Fonte raiz a 200%, espaçamento WCAG, temas claro e escuro e movimento reduzido sem excesso de largura |
| Contraste | 14 combinações conferidas. Menor razão: 5,774:1. [Cálculo](contrastes-idiomas-2026-10-13.json) |
| PDF | Cinco currículos de sete páginas. Cada título de curso aparece uma vez no texto extraído. [Registro](verificacao-impressao-idiomas-2026-10-13.json) |
| Inspeção visual | Currículos impressos e capturas das páginas examinados. [Acervo de evidências](evidencias-idiomas-2026-10-13/) |
| Referências | Dois clones completos ignorados, sem arquivos no índice Git. Manifestos registram versões, licenças e hashes |
| Integridade do diff | git diff --check concluído sem erros |

As fontes seguiram os procedimentos de verificação e inspeção das skills verification e pdf.
Esses procedimentos não acrescentaram dependências ao site.
O servidor Python e os utilitários de teste serviram apenas à manutenção local.

### Impressão e geração dos PDFs de teste

A produção consecutiva de evidências em processos reutilizados omitiu alguns caracteres nas primeiras imagens.
Uma troca temporária da fonte de impressão não resolveu todos os arquivos.
Essa alteração foi revertida. Os cinco CSS finais conservam os bytes originais.

Cada PDF final foi gerado em uma sessão Chromium independente, com os estilos originais.
Cada documento foi rasterizado em um processo PDFium independente. As imagens finais foram inspecionadas.
Os títulos dos cursos foram conferidos também por extração de texto.
As primeiras evidências defeituosas foram substituídas pelos arquivos finais.

### Validação local e proteção dos dados

A revisão automática de aprovação rejeitou o envio do HTML ao validador W3C externo.
O motivo informado foi a presença de dados pessoais no currículo.
A validação foi concluída com o Nu HTML Checker local, sem enviar esse conteúdo a um serviço externo.
O hash do utilitário e a origem da distribuição estão no resultado JSON.

## Repetição e limites

1. Sirva static/ pelo procedimento do README da raiz.
2. Abra currículo, galeria e agradecimentos em cada idioma.
3. Confira navegação, foco, temas e telas pequenas.
4. Abra e feche os cursos com o teclado.
5. Confira a impressão nos dois estados do controle.
6. Gere cada PDF automatizado em uma sessão independente do navegador.
7. Rasterize cada documento em um processo independente.
8. Inspecione as páginas e confira os 17 títulos.
9. Valide o HTML localmente antes de enviar conteúdo pessoal a serviços externos.
10. Execute git diff --check.

Os testes usaram Chromium. Eles não cobrem todos os navegadores, leitores de tela ou impressoras.
A ampliação de texto e o viewport estreito foram examinados. O zoom nativo da interface do navegador não foi automatizado.
Os links externos e os repositórios privados não foram auditados como serviços disponíveis.
O CSS final corresponde ao arquivo já validado e documentado na revisão de 12 de outubro.
A conformidade integral com WCAG ou STE não foi demonstrada por estes ensaios.

Os scripts temporários de execução foram removidos após o registro dos procedimentos e resultados.
Nenhum commit ou publicação foi realizado nesta tarefa.
