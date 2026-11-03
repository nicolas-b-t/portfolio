# SFIA no portfólio: viabilidade e cursos de ação

Análise de 02/11/2026.
Situação: **COA A+B implementado em 02/11/2026; níveis publicados como autoavaliação, sujeitos a revisão.**
Documentos consultados em `docs/referencias/sfia-local/`, cópia privada ignorada pelo Git.
A referência principal de códigos e níveis é o SFIA 9 em português, na biblioteca principal.

## 1. O que foi analisado

- SFIA 5, 7 e 8: versões históricas e referência de terminologia em inglês.
- SFIA 8 (2021 e 2023): referência da estrutura, resumos visuais e licenciamento.
- SFIA 9: perfis ilustrativos de funções, de 2026.
- SFIA 9 em português: referência da estrutura usada pelo projeto.
- `rate card` comercial de 2025: referência de licenciamento, não de uso pessoal.

A cópia privada está em `docs/referencias/sfia-local/`.
Ela não integra a base `docs/repertorio-tecnico-site/`, não é versionada e não é publicada.
A decisão D-33 continua válida: o SFIA não entra na base local versionada.

## 2. O que “implementar SFIA” pode significar

O SFIA não é certificação nem teste de proficiência.
Os sete níveis descrevem responsabilidade, autonomia, complexidade e impacto.
Uma habilidade pode existir em vários níveis; o nível não mede apenas conhecimento técnico.

Implementar pode ser:

1. usar o SFIA como rubrica interna, sem mudança visível;
2. publicar um bloco compacto de habilidades e níveis;
3. criar uma página dedicada de competências;
4. publicar o perfil nos cinco idiomas;
5. usar o SFIA apenas no PDF do currículo.

## 3. Viabilidade

### 3.1 Técnica

Viável.
O site é HTML e CSS estáticos, sem JavaScript.
Um bloco com 5 a 7 habilidades cabe na página inicial em pt-BR.
Cartões ou lista descritiva funcionam melhor que tabela larga em 320 CSS px.
A cópia estruturada oculta e a impressão precisam receber o mesmo conteúdo.
Não é necessário backend, banco, framework ou etapa de build.

### 3.2 Editorial

Viável com limite.
O SFIA recomenda 5 a 7 habilidades por perfil.
O texto deve ter código, nome oficial da habilidade, nível e uma linha de evidência.
Não convém reproduzir as descrições oficiais nem os descritores dos níveis.
O bloco precisa de uma nota curta: autoavaliação, não certificação.

### 3.3 Jurídica

Segundo a documentação da SFIA Foundation, o uso para desenvolvimento pessoal de carreira e para a maior parte do uso interno é gratuito.
A própria documentação cita a criação de currículos e perfis pessoais de competências.
Publicar um perfil pessoal com código, nome e nível tende a ser compatível com esse uso; a publicação pública, porém, exige cautela.

Há limites:

- copiar o material exige autorização escrita ou licença válida;
- redistribuir, traduzir e distribuir uma versão traduzida exige licença;
- usar o SFIA para marketing, certificação externa, rate card ou promoção de organização é proibido sem licença especial;
- o logotipo e o selo não devem ser usados sem autorização.

Mitigação para o site:

1. publicar apenas código, nome oficial, nível e evidência autoral;
2. não copiar descrições, tabelas ou descritores oficiais;
3. não usar logotipo, selo ou alegação de certificação;
4. manter os documentos SFIA fora do site e fora do Git;
5. em outros idiomas, usar o nome oficial disponível ou manter o termo em inglês, sem traduzir o SFIA por conta própria.

Esta análise não é parecer jurídico.
Se o responsável quiser publicar descrições completas, logotipo ou uma versão traduzida, deve pedir autorização à SFIA Foundation.

### 3.4 Evidência

A evidência atual sugere uma faixa de níveis 2–3 em várias áreas.
Não há, no material consultado, evidência para níveis 4 ou superiores, que exigem possibilitar o trabalho de outras pessoas, planejar e assumir responsabilidade ampliada.
A decisão final de cada nível é do responsável.

## 4. Condições mínimas

1. O responsável revisa e aprova cada habilidade, nível e texto de evidência.
2. O perfil usa o SFIA 9 como referência; o SFIA 8 serve apenas para conferir terminologia.
3. O bloco tem no máximo 7 habilidades.
4. A primeira publicação é em pt-BR.
5. Não há logotipo, selo, certificação ou promessa de proficiência.
6. O conteúdo visível e a cópia estruturada são iguais.
7. A mudança passa por teclado, foco, contraste, 320 CSS px, zoom, temas e impressão.
8. O texto e os níveis são revisados quando houver novo projeto, certificado ou função.

## 5. Evidência e faixas prováveis

As faixas abaixo são hipóteses de trabalho, não níveis atribuídos.

| Habilidade | Evidência atual | Faixa provável | O que falta confirmar |
| --- | --- | --- | --- |
| `USUP` — Gestão de incidentes | Suporte N1/N2 em ERP/PDV e ambiente hospitalar; diagnóstico e orientação a usuários. | 2–3 | Se diagnostica e resolve incidentes sob direção geral, não apenas segue procedimento. |
| `NTAS` — Suporte a redes | RealFort: FTTH, rádio, cabo drop, SC/APC, RJ45, ONU/ONT, roteadores, power meter, OTDR e VFL. | 2–3 | Se instala e diagnostica redes com autonomia, e não apenas auxilia. |
| `HSIN` — Instalação e remoção de sistemas | RealFort e Alpha: instalação, manutenção, ativos e hardware. | 2–3 | Se instala, remove e entrega sistemas ao usuário com autonomia. |
| `ASUP` — Suporte a aplicações | Lukos: suporte a ERP/PDV, configuração, diagnóstico remoto e NF-e/NFC-e. | 2–3 | Se resolve problemas de aplicação e orienta usuários sob direção geral. |
| `ITOP` — Operações de infraestrutura | Alpha e Lukos: suporte, monitoramento e manutenção. | 2–3 | Se opera e monitora infraestrutura além de atender chamados. |
| `DATM` — Gestão de dados | Curso de modelagem, SQL e dados do SGCS. | 1–2 | Se aplica práticas de gestão de dados em projeto real. |
| `PROG` — Programação/desenvolvimento | Portfólio em HTML/CSS, cursos de Python e JavaScript, SGCS e Optigrow. | 2–3 | Se contribui com código em projeto colaborativo e mantém qualidade. |
| `CFMG` — Gestão da configuração | Git, GitHub, documentação versionada e manifestos. | 2–3 | Se aplica versionamento e configuração de forma consistente. |
| `CHMG` — Controle de mudanças | Commits, revisão, reversão e procedimento de mudança. | 2–3 | Se controla mudanças com análise de impacto e aprovação. |

## 6. Cursos de ação

| COA | Escopo | Esforço | Risco | Valor | Decisão |
| --- | --- | --- | --- | --- | --- |
| **A. Interno** | Usar o SFIA só como rubrica; nenhuma mudança no site. | 0 | Baixo | Baixo | Alternativa de contingência. |
| **B. Bloco compacto em pt-BR** | 5 a 7 habilidades no `index.html`, com código, nome, nível, evidência e nota de autoavaliação. | 2 sessões | Baixo a médio | Alto | **Implementado em 02/11/2026.** |
| **C. Página dedicada em pt-BR** | `competencias.html` com método, tabela, evidências e limites; link no menu. | 3 a 4 sessões | Médio | Alto | Avaliar depois do piloto. |
| **D. Cinco idiomas** | Repetir o bloco nas cinco variantes. | 6 a 10 sessões | Alto | Médio | Não agora. |
| **E. Apenas no PDF** | Usar o SFIA no currículo PDF, sem mudar o site. | 1 a 2 sessões | Baixo | Médio | Alternativa se o site deve ficar simples. |
| **F. Nível sem evidência ou selo** | Publicar níveis sem comprovação, logotipo ou selo. | 0 | Muito alto | Negativo | Rejeitado. |

## 7. Implementação adotada

**COA A+B, em pt-BR, com sete habilidades.**

Conjunto publicado em 02/11/2026:

- `USUP` — Gestão de incidentes — nível 3;
- `NTAS` — Suporte a redes — nível 3;
- `HSIN` — Instalação e remoção de sistemas — nível 3;
- `ASUP` — Suporte a aplicações — nível 3;
- `ITOP` — Operações de infraestrutura — nível 2;
- `PROG` — Programação/desenvolvimento de software — nível 2;
- `CHMG` — Controle de mudanças — nível 2.

Não publicadas nesta etapa:

- `CFMG` — Gestão da configuração;
- `DATM` — Gestão de dados.

A rubrica interna está em [Competências](competencias.md), seção 10.
Os níveis são autoavaliação e estão sujeitos a revisão do responsável (P-14).
Não há níveis 4 a 7.

## 8. O que o COA B mudou

Arquivos alterados:

- `static/pt-BR/index.html`: seção “Perfil SFIA” e cópia estruturada;
- `static/assets/css/styles.css`: estilos do bloco, impressão e telas pequenas;
- `docs/fontes/competencias-declaradas.json`: habilidades, níveis e evidências aprovadas;
- `docs/competencias.md`: método, níveis e limites;
- `docs/requisitos.md`: requisito FR-15 do perfil SFIA;
- `CHANGELOG.md`: registro da publicação.

O bloco usa HTML semântico, sem JavaScript.
A seção inteira é um `<details>` nativo, fechada por padrão e colapsável.
Dentro dela, um segundo `<details>` reúne a metodologia e a lista das nove habilidades.
Na impressão, uma cópia estática mostra o título e os cartões; a metodologia e a seção interativa ficam ocultas.
A nota visível diz que é autoavaliação baseada no SFIA 9, sem certificação, endosso ou afiliação.
O logotipo não é usado.

## 9. Estado das decisões

1. COA A+B aprovado e implementado.
2. Níveis publicados; revisão do responsável em P-14.
3. Leitura conservadora da licença mantida; sem logo, selo ou descrições oficiais.
4. Cópia privada mantida em `docs/referencias/sfia-local/`.
5. Bloco publicado na página inicial em pt-BR; COA C e D ficam para avaliação futura.

## 10. Limites

- Não há avaliação independente de competência.
- Não há certificação SFIA.
- Não há parecer jurídico.
- As faixas de nível foram publicadas como autoavaliação; a revisão está em P-14.
- A cópia privada não é publicada e não deve ser redistribuída.
- O SFIA 8 não substitui a referência v9 usada pelo projeto.
