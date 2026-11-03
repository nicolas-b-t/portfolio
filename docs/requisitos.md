# Requisitos do site

Catálogo aceito em 02/11/2026, na fase 02 do [plano](../PLANO-APLICACAO-PADROES-TECNICOS.md).
As fontes normativas estão na base local `docs/repertorio-tecnico-site/`. As demais fontes são os documentos do projeto e as decisões registradas.
Os requisitos marcados como vigentes descrevem o comportamento atual. O catálogo aceito é a linha de base.

Não há declaração de conformidade com o CPRE, com a WCAG ou com qualquer norma.

## 1. Finalidade e escopo

O catálogo registra o que o site precisa entregar e como cada item será verificado.
Ele cobre o site estático em HTML e CSS, a documentação versionada e a publicação no GitHub Pages.
O escopo inicial prioriza `pt-BR`. As outras quatro variantes continuam publicadas e recebem sincronização.
Aceite: 02/11/2026. Não há novos requisitos no momento.

## 2. Partes interessadas e objetivos

Decisão D-23, de 02/11/2026.

| Parte | Papel |
| --- | --- |
| Recrutadores e gestores de contratação | Público principal. |
| Responsável pelo projeto | Aprova escopo, mudanças e aceite. |
| Agente de implementação | Executa, verifica e registra evidência. |
| Visitantes em geral | Leem, imprimem e usam tecnologia assistiva. |
| GitHub | Hospeda o repositório e publica o site. |

Objetivo: apoiar a candidatura a emprego.
Ações esperadas: abrir o currículo, ver os projetos e entrar em contato.

## 3. Fronteira do sistema

Fronteira definida conforme o CPRE §4.1, página 31.

**Dentro da fronteira:** os arquivos HTML, o CSS, as imagens locais, os ícones, o workflow de publicação e a documentação do projeto.

**Fora da fronteira:** o navegador do visitante, o GitHub Pages, o DNS e o TLS, o Google Drive, o LinkedIn e os sites externos vinculados.

**Fora do escopo inicial:** backend, formulário, blog, analytics, domínio próprio, novas variantes e novas funcionalidades. Decisões D-07 e D-09.

## 4. Glossário

Termos do projeto. As definições gerais seguem o glossário de engenharia de requisitos, versão 2.2.0.

| Termo | Definição |
| --- | --- |
| Variante | Uma das cinco versões linguísticas publicadas: `pt-BR`, `pt-PT`, `en`, `es-419` e `es-ES`. |
| Página | Um arquivo HTML dentro de uma variante. |
| Cópia estruturada | Seção oculta com os dados do currículo ou dos projetos para leitura automática. |
| Tag | Um item de competência, tecnologia ou qualificação. |
| Subcategoria | Agrupamento dentro de uma categoria de competências. |
| Projeto | Trabalho acadêmico ou profissional com link público. |
| Recomendação | Texto de terceiro publicado com autorização. |
| Publicação | Cópia de `static/` para o GitHub Pages pelo workflow. |
| Linha de base | Estado aprovado do plano e dos documentos. |
| Critério de aceite | Condição observável que permite aceitar o requisito. |
| Operador | O responsável, que decide resoluções e aprovações. |

## 5. Convenções

Cada requisito tem identificador, texto, prioridade, fonte, critério de aceite, fase e situação.
As prioridades são essencial, esperado e opcional.
As situações são: vigente, vigente com lacuna, lacuna, aprovado e não implementado, futuro e parcial.
Critérios qualitativos são avaliados pelo operador, com registro da decisão. Decisão D-31.

As características de qualidade seguem o CPRE §3.8, páginas 29 e 30:

- para um requisito: adequado, necessário, sem ambiguidade, completo, compreensível e verificável;
- para o conjunto: consistente, sem redundância, completo, modificável, rastreável e conforme.

## 6. Requisitos funcionais

| ID | Requisito | Prioridade | Fonte | Critério de aceite | Fase | Situação |
| --- | --- | --- | --- | --- | --- | --- |
| FR-01 | O visitante encontra as cinco variantes, com `lang` correto e links `hreflang` recíprocos. | Essencial | RFC 5646; AGENTS.md; auditoria de 02/11/2026. | As 23 páginas declaram o idioma; os cinco links abrem a variante certa; não há link interno quebrado. | 09 | Vigente. |
| FR-02 | Cada variante oferece currículo, galeria, rede e recomendações. Em `pt-BR`, há também a página de projetos. | Essencial | AGENTS.md; auditoria de 02/11/2026. | As quatro páginas existem em cada variante; `projetos.html` existe em `pt-BR`; o menu alcança todas. | 04 | Vigente. |
| FR-03 | O conteúdo de `pt-BR` é a base factual das demais variantes. | Essencial | AGENTS.md; `docs/manutencao.md`; D-23. | Fato alterado em `pt-BR` aparece igual nas outras variantes, ou a divergência está registrada. | 03 e 05 | Vigente com lacuna. |
| FR-04 | A página de projetos lista os trabalhos com link de site e de repositório quando existirem. | Essencial | `static/pt-BR/projetos.html`; auditoria de 02/11/2026. | Cada projeto tem descrição, link e atribuição individual ou de equipe. | 05 | Vigente. |
| FR-05 | O visitante acessa e-mail, LinkedIn e GitHub pelos links de contato. | Essencial | `static/pt-BR/index.html`; auditoria de 02/11/2026. | Os três links abrem o destino correto; o e-mail abre o cliente de e-mail. | 05 | Vigente. |
| FR-06 | A galeria mostra imagens locais com texto alternativo e legenda. | Esperado | AGENTS.md; auditoria de 02/11/2026. | Toda imagem tem `alt`; nenhuma imagem depende de servidor externo; a legenda descreve o conteúdo. | 05 | Vigente. |
| FR-07 | A página de recomendações publica textos autorizados, sem alterar o sentido. | Esperado | D-13; `docs/conteudo-e-fontes.md`. | Cada recomendação tem autor e autorização registrada; o texto preserva o original. | 06 | Vigente. |
| FR-08 | O botão de download do currículo permanece visível e inativo até a publicação do PDF. | Esperado | D-27; `static/pt-BR/index.html`; auditoria de 02/11/2026. | O botão aparece desativado nas cinco variantes; não aponta para arquivo inexistente; a decisão está registrada. | 02 | Vigente; decisão D-27. |
| FR-09 | A cópia estruturada oculta mantém os mesmos dados da tela. | Esperado | `docs/manutencao.md`; auditoria de 02/11/2026. | Os dados conferem; a cópia não aparece na tela nem na impressão. | 03 | Vigente. |
| FR-10 | As competências mantêm três categorias, com subcategorias, uma tag por item e níveis preservados. | Essencial | AGENTS.md; `docs/fontes/competencias-declaradas.json`. | Três categorias; subcategorias coerentes; níveis de suporte, fibra e inglês preservados. | 05 e 11 | Vigente. |
| FR-11 | A raiz apresenta as cinco variantes e leva à escolhida. | Esperado | `static/index.html`; auditoria de 02/11/2026. | A raiz lista as cinco opções; cada link abre a variante correspondente. | 09 | Vigente. |
| FR-12 | A impressão mostra o conteúdo e oculta menus e cópia estruturada. | Esperado | `static/assets/css/styles.css`; auditoria de 02/11/2026. | A impressão mostra as seções; a cópia oculta não aparece; não há corte de conteúdo. | 05 | Vigente. |
| FR-13 | O site tem página 404 no mesmo estilo, com retorno ao início. | Opcional | D-17; documentação do GitHub Pages (EXT-02). | A página abre no lugar do erro padrão; mantém `lang` e link de retorno. | 09 | Vigente; implementado em 02/11/2026. |
| FR-14 | A estrutura aceita novas variantes sem duplicar CSS ou workflow. | Opcional | D-07; AGENTS.md. | Uma variante nova usa o mesmo CSS e o mesmo workflow; `pt-BR` está concluído antes. | 02 e 04 | Futuro. |

## 7. Requisitos não funcionais

| ID | Requisito | Prioridade | Fonte | Critério de aceite | Fase | Situação |
| --- | --- | --- | --- | --- | --- | --- |
| NFR-01 | O site busca o nível AA da WCAG 2.2, sem declarar conformidade. | Essencial | WCAG 2.2; D-23. | Teclado, foco visível, nomes acessíveis, contraste, 320 CSS px, zoom, temas e impressão verificados por tipo de página. | 05 | Parcial; auditoria pendente. |
| NFR-02 | O site não usa JavaScript, formulário, iframe ou rastreador. | Essencial | AGENTS.md; D-09. | Zero `<script>`, `<form>`, `<iframe>`, `style=` e código de analytics. | 03 | Vigente. |
| NFR-03 | O site usa recursos locais e fontes do sistema. | Essencial | AGENTS.md; auditoria de 02/11/2026. | Nenhum recurso de fonte, imagem ou script é carregado de servidor externo. | 04 | Vigente. |
| NFR-04 | O desempenho é avaliado por teste empírico, com economia de recursos. | Essencial | D-08; R07. | O teste fica registrado; não há meta numérica inventada. | 03 e 05 | Vigente. |
| NFR-05 | O layout funciona de 320 CSS px até tela ampla, sem rolagem horizontal. | Essencial | WCAG 2.2; auditoria de 02/11/2026. | A 320 CSS px, o conteúdo fica legível e sem transbordamento horizontal. | 05 | Vigente. |
| NFR-06 | O site respeita tema claro, tema escuro, impressão e `prefers-reduced-motion`. | Esperado | `static/assets/css/styles.css`; AGENTS.md. | As quatro condições funcionam nas páginas conferidas. | 05 | Vigente. |
| NFR-07 | O HTML é semântico, com hierarquia de títulos e um `h1` por página. | Essencial | HTML Living Standard; AGENTS.md. | Cada página tem um `h1`; a hierarquia não salta níveis sem motivo; o HTML passa em uma validação declarada e registrada. | 04 | Parcial; validação pendente. |
| NFR-08 | A publicação usa permissões mínimas, ações fixadas e nenhum segredo no repositório. | Essencial | NIST SSDF 800-218; auditoria de 02/11/2026. | Workflow com `contents: read`; ações por SHA; nenhum segredo; 2FA concluído; alterações na `main` autorizadas. | 08 | Parcial; 2FA em ativação e proteção técnica a confirmar. |
| NFR-09 | O site não usa cookies nem analytics e mantém os dados publicados como estão. | Essencial | D-12; auditoria de 02/11/2026. | Nenhum cookie ou analytics; dados publicados conforme a decisão; dados sensíveis só em cópia local. | 06 | Vigente. |
| NFR-10 | O projeto mantém um CSS, documentação indexada, `CHANGELOG` e nenhuma etapa de build. | Esperado | AGENTS.md; D-11. | Um CSS comum; documentos ligados no índice; `CHANGELOG` atualizado; publicação sem build. | 03 e 10 | Vigente; `CHANGELOG` criado em 02/11/2026. |
| NFR-11 | O site funciona nos navegadores atuais e em celular. | Esperado | D-23; R06; Q3. | Ensaio em LibreWolf e em navegador atual; limitação registrada quando não houver cobertura. | 05 | Parcial; ensaio no LibreWolf e registro anterior no Chromium. |

## 8. Rastreabilidade

A tabela acima é a matriz de rastreabilidade, conforme o CPRE §6.6, página 43.
Cada linha liga requisito, fonte, critério de aceite, fase e situação.
O identificador não muda quando o texto é ajustado. Uma mudança de sentido cria um identificador novo ou registra a versão.

## 9. Fora do escopo

- Blog, formulário de contato, analytics e domínio próprio.
- Backend, banco de dados, framework e etapa de build.
- Tradução de novas páginas antes de concluir `pt-BR`.
- Declaração de conformidade com norma ou certificação.
- Uso de ISO 31000 ou LGPD como fundamento, pois a base local não os contém.
- Publicação de níveis SFIA ou work roles NICE sem evidência e aprovação; ambos são referências externas, não certificação.

## 10. Verificação e limites

Verificação de 02/11/2026:

- 23 arquivos HTML, cinco variantes, um redirecionamento na raiz e uma página 404;
- nenhum `<script>`, `<form>`, `<iframe>` ou `style=` embutido;
- 45 imagens, nenhuma sem `alt`;
- links internos, âncoras e identificadores sem erro na conferência estática;
- workflow publica somente `static/`, com permissões mínimas e ações por SHA.

Limites:

- Não houve ensaio com leitor de tela nem validação externa de acessibilidade.
- A conferência de links não prova que o destino externo continua disponível.
- O catálogo foi aceito em 02/11/2026 e é a linha de base. A implementação de itens parciais continua pendente.
- A página 404 e o `CHANGELOG` foram criados em 02/11/2026.

## 11. Pendências

A lista vigente está em [Pendências](pendencias.md).
Os requisitos parciais são NFR-01, NFR-07, NFR-08 e NFR-11.
A situação de cada um é atualizada na lista, não neste catálogo.
