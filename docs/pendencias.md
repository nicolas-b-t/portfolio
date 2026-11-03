# Estado atual e pendências

Última revisão: 02/11/2026.

Esta é a única lista vigente de pendências do projeto.
Os registros históricos mantêm o texto da época; não são atualizados a cada mudança.
Os requisitos e seus estados estão em [Requisitos](requisitos.md).
Os riscos e seus donos estão na seção 1.5 de [Padrões técnicos](padroes-tecnicos.md).

## 1. Decisões do responsável

| ID | Item | Origem | Dono | Situação | Próximo passo |
| --- | --- | --- | --- | --- | --- |
| P-01 | Aceitar formalmente a linha de base de 02/11/2026. | §12; requisitos | Responsável | Aberto | Registrar a data e o commit aceitos. |
| P-02 | Decidir se os sinônimos visíveis de ATS permanecem na tela. | EDIT-01; R13 | Responsável | Aberto | Manter na tela ou mover para a cópia oculta. |
| P-03 | Revisar as frases de ATS em inglês na lista visível. | EDIT-03; R13 | Responsável | Aberto | Decidir junto com P-02. |
| P-04 | Decidir se algum nível SFIA será publicado. | §11.6; R12 | Responsável | Aberto | Exigir evidência antes de publicar. |
| P-05 | Decidir se haverá mapeamento de work roles do NICE. | §11.6 | Responsável | Condicional | Obter os componentes oficiais apenas se a resposta for sim. |
| P-06 | Confirmar a licença canônica dos ícones. | §8.4 | Responsável | Aberto | Confirmar `LICENSE.txt` e retirar a cópia genérica, se aprovado. |
| P-13 | Decidir o COA para publicar o SFIA no site. | [SFIA: viabilidade](sfia-viabilidade.md) | Responsável | Aberto | Escolher A, B, C, D ou E; aprovar habilidades e níveis. |

## 2. Segurança e continuidade

| ID | Item | Origem | Dono | Situação | Próximo passo |
| --- | --- | --- | --- | --- | --- |
| P-07 | Concluir o 2FA e confirmar a proteção da `main`. | NFR-08; R05 | Responsável | Em andamento | Ativar o 2FA, conferir a proteção e registrar a evidência. |
| P-08 | Criar o backup da v2 da base local. | R06 | Responsável | Parcial | Preferir formato aberto e manter cópia externa. |
| P-09 | Publicar a cópia limpa sem dados pessoais. | R09; D-15 | Responsável | Planejado | Executar no encerramento. |

## 3. Verificação e qualidade

| ID | Item | Origem | Dono | Situação | Próximo passo |
| --- | --- | --- | --- | --- | --- |
| P-10 | Testar zoom, tema escuro, impressão e leitor de tela. | TEST-01; NFR-01 | Agente e responsável | Aberto | Executar, registrar a evidência e fechar TEST-01. |
| P-11 | Validar HTML e hierarquia de títulos. | NFR-07 | Agente | Parcial | Definir o método, executar e registrar o resultado. |
| P-12 | Ensaiar em navegador atual e em celular. | NFR-11 | Agente | Parcial | Registrar navegador, largura e resultado. |

## 4. Regras de manutenção

1. Uma pendência nova entra nesta lista com ID, origem, dono e próximo passo.
2. Um item concluído sai da lista e entra no [CHANGELOG](../CHANGELOG.md), quando a mudança for publicada.
3. Um registro histórico não é reescrito para refletir o estado atual.
4. Um item sem dono não entra: a pendência fica com o responsável.
5. A lista é revisada ao fim de cada marco e antes de cada publicação.
