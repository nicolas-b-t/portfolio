# Relatos profissionais em validação

Registro de trabalho iniciado em 23/11/2026 a partir das declarações do responsável nesta conversa. Serve para preparar o perfil profissional e identificar evidências a reunir. **Relato pessoal, preferência, artefato de projeto e resultado medido são tipos diferentes de informação.** Este documento não autoriza transformar uma preferência em experiência comprovada nem publicar métricas sem registro.

## Perfil profissional aprovado para publicação

> Trabalho com tecnologia e curso Gestão da Tecnologia da Informação. Já atuei em suporte, redes e comércio eletrônico. Hoje também desenvolvo projetos de software e reúno neste site alguns trabalhos dessa trajetória.

Texto aprovado pelo responsável em 23/11/2026 para o site e a edição `CV-NicolasBt-2026-11-04`. Substitui o perfil da edição 03, que detalhava preferências de desenvolvimento no resumo. As práticas e preferências abaixo continuam classificadas de acordo com a evidência disponível.

## Práticas e experiências declaradas

| ID | Relato do responsável | Situação documental em 23/11/2026 | Evidência que pode ser reunida |
| --- | --- | --- | --- |
| RP-01 | Define critérios para requisitos funcionais, não funcionais e de segurança. | Há listas de requisitos em projetos públicos, como o [portfólio](requisitos.md) e o [site de Aquecedores](https://github.com/nicolas-b-t/site-aquecedores-mairipora/blob/main/docs/lista-requisitos.md). A autoria individual de cada decisão não foi verificada. | Registro de uma decisão de escopo, critérios de aceite e participação individual. |
| RP-02 | Define ou examina personas e mapas de processos atuais e propostos. | Relato pessoal; não foi localizado um caso específico com autoria e versão documentadas nesta revisão. | Exemplo anonimizado de persona e de processo antes/depois, com contexto e decisão resultante. |
| RP-03 | A implementação de código pode ser delegada a agentes de IA; o responsável define critérios e acompanha a entrega. | Relato pessoal. Os repositórios documentam o uso de agentes, mas não permitem atribuir cada trecho de código. | Exemplo de requisito, entrega, verificação e decisão do responsável no mesmo projeto. |
| RP-04 | Realiza testes de uso, interações inesperadas, falha e excesso de carga ou usuários. Relatou experiências em projetos hospedados por Vercel, GitHub Pages e Cloudflare. | Não há nesta revisão relatórios com cenário, ferramenta, carga e resultado. Testes exploratórios, de carga, de estresse e de falha devem ser descritos separadamente. | Roteiro e relatório reproduzível de pelo menos um cenário, com ambiente, limites, resultado e ajuste feito. |
| RP-05 | Publica sistemas e acompanha sua manutenção. | Há histórico de commits e workflows de publicação nos projetos públicos. A rotina operacional pessoal ainda não está descrita por caso. | Histórico de uma publicação, incidente ou melhoria posterior à entrega. |
| RP-06 | Mantém contato com clientes para adaptar soluções a necessidades que mudam. | O [site de Aquecedores](https://github.com/nicolas-b-t/site-aquecedores-mairipora/blob/main/docs/lista-requisitos.md) registra mudança de escopo. O contato e a decisão individual seguem como relato pessoal. | Briefing, solicitação de mudança e decisão, com dados do cliente protegidos quando necessário. |
| RP-07 | Refaz e melhora sites legados, preservando versões anteriores para consulta e comparação. | O [site de Aquecedores](https://github.com/nicolas-b-t/site-aquecedores-mairipora) mantém a versão anterior e a nova. Não foram verificados resultados de otimização medidos nem outros casos de legado. | Comparação antes/depois de estrutura, manutenção, experiência de uso ou desempenho, com método explícito. |
| RP-08 | Já operou serviços em contêineres. | Relato pessoal; não foram encontrados arquivos de contêiner ou implantação correspondente nos repositórios examinados. Isso não invalida a experiência relatada. | Projeto demonstrativo ou registro de implantação com configuração e procedimento de operação. |

## Preferências de desenvolvimento declaradas

| ID | Preferência | Indício atual e limite | Exemplo futuro útil |
| --- | --- | --- | --- |
| PD-01 | Escolher a menor combinação de tecnologias que atenda ao problema, com custo e manutenção sob controle. | O [portfólio](../README.md) usa HTML e CSS sem build; o [site de Aquecedores](https://github.com/nicolas-b-t/site-aquecedores-mairipora) publica arquivos estáticos com JavaScript onde há cálculos. Isso mostra escolhas nesses projetos, sem estabelecer uma regra universal. | Registrar opções consideradas e por que a solução escolhida bastou. |
| PD-02 | Equilibrar simplicidade de manutenção, desempenho e custo, aceitando em alguns casos menos desempenho para facilitar manutenção e crescimento. | Preferência declarada, sem comparação documentada de alternativas nesta revisão. | Decisão arquitetural com restrições, alternativas, teste e justificativa. |
| PD-03 | Considerar escala horizontal desde o desenho da solução. | Preferência declarada. Não foi localizada implantação com múltiplas instâncias nos repositórios examinados. | Demonstração de serviço sem estado local obrigatório, com duas instâncias e cenário de aumento de carga. |
| PD-04 | Usar SQLite quando o contexto permitir e PostgreSQL quando ele simplificar uma solução maior. | O catálogo do [site de Aquecedores](https://github.com/nicolas-b-t/site-aquecedores-mairipora/blob/main/docs/refinamento/catalogo/publicar.py) usa SQLite para preparar dados publicados em JSON. Não foi localizado exemplo de PostgreSQL nesta revisão. | Documentar critérios de escolha, incluindo concorrência de escrita, operação e custo. |
| PD-05 | Priorizar soluções diretas, funcionais e passíveis de verificação. | Há documentação, histórico e verificadores nos projetos públicos. Esses artefatos não equivalem a auditoria independente nem comprovam todos os atributos em produção. | Critérios de aceite, testes e histórico de uma mudança após uso real. |

## Uso editorial

- No perfil profissional, apresentar preferências como forma de trabalhar, sem lista de tecnologias ou resultados não medidos.
- Em fichas de projeto, atribuir ao responsável apenas decisões e ações que ele confirmou; distinguir implementação delegada de validação da entrega.
- Reservar alegações de escala horizontal, operação em contêineres e desempenho medido para casos com demonstração ou registro específico.
- Preparar a lista de projetos e afirmações a oficializar depois de fechar a redação do perfil profissional.
