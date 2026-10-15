# Normalização e verificação integral das tags pt-BR

Data: 14 de outubro de 2026.
Base Git: a0863e5, com a retirada posterior do link privado do SGCS já preservada no checkout.
Escopo: página principal pt-BR, bloco oculto, lista geral e preparação dos 14 arquivos de outros sistemas de escrita.
As outras páginas e os quatro idiomas publicados não foram alterados nesta etapa.

## Termos padronizados

| Forma anterior | Forma vigente |
| --- | --- |
| Amazon Web Services AWS software | Amazon Web Services (AWS) |
| Microsoft Azure software | Microsoft Azure |
| Nginx web server | NGINX |
| Cable management | Organização de cabos |
| Switches | Comutadores de rede |
| Preparo de postes para passagem de fibra | Preparação de postes para passagem de fibra |
| Manutenção de CTO (caixa de distribuição óptica) | Manutenção de caixas de terminação óptica (CTO) |
| Desenvolvimento tradicional (cascata) | Desenvolvimento em cascata |
| Banco de dados | Bancos de dados |
| Suporte Help Desk | Suporte de help desk |

As cinco primeiras formas anteriores foram preservadas como aliases no bloco oculto.
Os demais ajustes mantêm o conceito e suas qualificações, sem criar novas competências.
Os títulos oficiais dos cargos e dos cursos não foram alterados.
O uso genérico de help desk passou a usar letras minúsculas na apresentação e nos metadados.
O texto sobre código aberto passou a usar verbos e termos diretos em português.
Nomes cuja grafia depende da fonte declarada, como Fusimech, foram preservados.

As fontes consultadas para os nomes de produtos foram [AWS](https://aws.amazon.com/pt/), [Microsoft Azure](https://azure.microsoft.com/pt-br) e [NGINX](https://github.com/nginx/nginx).
A expansão de CTO foi conferida na [especificação técnica do fabricante](https://www.furukawalatam.com/pt_BR/versao-et-pdf/caixa-de-terminacao-optica-fk-cto-16mcii).
Essa referência esclarece o nome do equipamento. Ela não identifica o fabricante dos equipamentos utilizados pelo responsável.

## Contagens verificadas

| Base | Ocorrências | Rótulos distintos |
| --- | ---: | ---: |
| Página visível | 212 | 180 |
| Bloco oculto | 227 | 192 |
| Tags na lista geral | 227 | 192 |
| Cada tradução | 227 | 192 |

A verificação abrange todos os itens de listas com a classe skill-list.
Listas de cursos, navegação e parágrafos das experiências não são contados como tags.
O inventário completo preserva texto, contexto, grupo, idioma e identificador.
Na lista geral, cada ocorrência também registra sua linha no TXT.

Os 32 grupos visíveis foram comparados com os correspondentes ocultos.
Todas as tags visíveis estão presentes no bloco oculto, no mesmo contexto.
As 15 ocorrências suplementares são aliases de busca documentados.
As 227 ocorrências do TXT correspondem à sequência do bloco oculto.
As repetições entre formação, competências e projetos foram mantidas pelos seus contextos distintos.

O [registro integral](verificacao-normalizacao-tags-pt-br-2026-10-14.json) contém as comparações, as ocorrências e as duplicações por contexto.
O [registro da lista geral](verificacao-lista-geral-tags-2026-10-14.json) mantém a entrada atual e as saídas dos parsers.

## Outros sistemas de escrita

Os 14 arquivos foram preenchidos conforme a confirmação do responsável.
Eles abrangem russo, ucraniano, búlgaro, sérvio cirílico, grego, chinês simplificado, chinês tradicional, japonês, coreano, hindi, tailandês, árabe, persa e hebraico.
Cada arquivo mantém as 227 ocorrências da base, com nomes, siglas e qualificações preservados.
O total é de 3.178 ocorrências nos 14 arquivos.
O [glossário e o manifesto](tags-multilingues/README.md) permitem conferir as correspondências e a integridade.

Os arquivos são traduções de tags. Eles não são traduções completas do currículo nem declarações de fluência do candidato.
As traduções editoriais não receberam revisão de especialistas nativos.
Os TXT permanecem em Lista_de_tags/, fora do site publicado.

## Resultados e limites

Os três parsers locais foram executados novamente com 394 linhas lógicas.
As saídas permaneceram iguais às da verificação anterior.
As três experiências, a graduação e os dados dos 17 cursos foram preservados.
O segundo parser continua retornando C como falso positivo na palavra código.
Não foi demonstrado ganho de reconhecimento em ATS por acrescentar aliases.

Também foram conferidos UTF-8, Unicode NFC, ausência de tags vazias, links locais, âncoras e ausência de scripts.
As verificações de integridade passaram para todos os arquivos traduzidos.
Não foram realizados novos testes de tela, teclado ou impressão, conforme a dispensa do responsável.
Esta revisão não constitui certificação STE, linguística ou de acessibilidade.
