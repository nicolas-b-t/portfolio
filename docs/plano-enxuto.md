# MAPA ESSENCIAL E PLANO ENXUTO

Registro em 02/11/2026.
Situação: **registrado, não implementado**.
Este documento registra a avaliação do plano de 12 fases e uma versão enxuta para planejamento futuro.
Nada aqui foi executado além do próprio registro.
O plano de 12 fases permanece como histórico em [PLANO-APLICACAO-PADROES-TECNICOS.md](../PLANO-APLICACAO-PADROES-TECNICOS.md).

## 1. Lição registrada

- A biblioteca é um acervo, não um plano de projeto.
- Cobertura de pastas não é o mesmo que adequação ao risco.
- Documentação deve ser proporcional ao porte e à manutenção.
- Framework é meio de organização, não certificação e não fim.
- O plano de 12 fases cumpriu a cobertura pedida, mas criou simetria artificial.
- O SFIA e o NICE complementaram o contexto de competências e permanecem como referência interna.

## 2. O que permanece

Nada será apagado.

| Item | Situação |
| --- | --- |
| 12 seções em `docs/padroes-tecnicos.md` | Permanecem como registro e consulta. |
| 25 requisitos | Permanecem aceitos. |
| 7 ADRs | Permanecem vigentes. |
| `CHANGELOG` | Permanece ativo. |
| Página 404 | Permanece publicada. |
| Licença dos ícones | Permanece incluída. |
| SFIA e NICE | Permanecem como referência interna, sem níveis publicados. |

## 3. Mapa essencial

O mapa reduz o dia a dia a cinco frentes.

| Frente | Padrões mínimos | Onde está | Situação |
| --- | --- | --- | --- |
| Conteúdo e idiomas | `pt-BR` como base, RFC 5646, guia de redação | Site, `docs/requisitos.md`, `docs/guia-de-redacao.md` | Ativa. |
| Web e acessibilidade | HTML Living Standard, CSS, WCAG 2.2 AA | `static/`, seção 5, `docs/manutencao.md` | Ativa; faltam testes de zoom, tema escuro, impressão e leitor de tela. |
| Segurança e privacidade | SSDF em nível alto, controles do GitHub, inventário de dados | Seções 6 e 8, licença dos ícones | Ativa; 2FA e proteção da `main` pendentes. |
| Publicação e serviço | GitHub Pages, HTTPS, 404, verificação pós-push | Seção 9, `README.md`, workflow | Ativa. |
| Documentação e mudança | Diátaxis, MADR, Git, `CHANGELOG` | `docs/`, ADRs, plano, changelog | Ativa. |

## 4. O que vai para arquivo

Estes itens continuam consultáveis, mas não precisam ser mantidos como checklist diário:

- a narrativa completa das 12 fases;
- os registros de lacuna das fases 06 e 12;
- o piloto SFIA e a explicação do NICE;
- as decisões históricas D-01 a D-36;
- o detalhamento de fases que não geram operação recorrente.

Arquivo não significa descartar. Significa consultar quando houver auditoria, dúvida ou mudança estrutural.

## 5. Plano enxuto

Versão para planejamento futuro. Não implementada.

| Frente | Objetivo | Entregáveis | Rotina |
| --- | --- | --- | --- |
| 1. Conteúdo e idiomas | Manter `pt-BR` como base e as cinco variantes coerentes. | Conteúdo, guia de redação, requisitos de idioma. | Revisão por evento. |
| 2. Web e acessibilidade | Manter HTML/CSS, responsividade e alvo WCAG 2.2 AA. | CSS, checklist, evidência de ensaio. | Revisão por mudança visual. |
| 3. Segurança e privacidade | Reduzir exposição, perda de conta e dados. | Inventário, controles, licença, plano de incidente. | Revisão por evento e alerta. |
| 4. Publicação e serviço | Publicar com HTTPS, 404 e verificação. | Workflow, página 404, checklist pós-push. | Cada push. |
| 5. Documentação e mudança | Registrar decisões e mudanças sem excesso. | Requisitos, ADRs, `CHANGELOG`, riscos. | Cada mudança relevante. |

Revisão mínima anual: 02/11/2027.
Revisão por evento: novo projeto, certificado, formação, idioma, funcionalidade, incidente ou link quebrado.

## 6. O que não fazer

- Não reabrir as 12 fases.
- Não criar novos manuais por fase.
- Não adotar ISO 9001, ISO 27001, ISO 20000, ISO 31000, DAMA, FitSM, ASVS ou WSTG para este site.
- Não publicar níveis SFIA ou work roles NICE sem evidência e aprovação.
- Não transformar o plano enxuto em execução sem decisão do responsável.

## 7. Relação com o plano de 12 fases

O plano de 12 fases é o **registro de cobertura e auditoria**.
O plano enxuto é a **referência de planejamento futuro**.

O plano enxuto não substitui automaticamente o plano antigo.
Se for adotado, a substituição deve ser registrada como decisão, sem apagar o histórico.

## 8. Pendências que continuam

1. Concluir o 2FA e confirmar a proteção da `main`.
2. Decidir sobre os sinônimos visíveis de ATS.
3. Testar zoom, tema escuro, impressão e leitor de tela.
4. Obter os componentes do NICE, se houver mapeamento de work roles.
5. Decidir se algum nível SFIA será publicado.
6. Publicar a cópia limpa sem dados pessoais.
7. Aceitar formalmente a linha de base.

## 9. Situação

Este documento é um registro.
Nenhuma fase foi reaberta.
Nenhum arquivo do site foi alterado.
Nenhum framework novo foi adotado.
