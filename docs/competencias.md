# Competências e frameworks de referência

Este documento explica o SFIA e o NICE, sua utilidade e a forma de aplicação neste projeto.
As declarações factuais continuam em `dados-pessoais/fontes/competencias-declaradas.json` (local, ignorado pelo Git).

Os frameworks são lentes de organização. Não são certificação, avaliação de proficiência ou prova de experiência.

## 1. SFIA

**Skills Framework for the Information Age.**

O SFIA é mantido pela SFIA Foundation e descreve habilidades e competências para o mundo digital.
Foi lançado em 2000 e é usado por governos, empresas e profissionais em quase 200 países.

### Estrutura

- **Habilidades profissionais:** catálogo de habilidades, cada uma com um código, como `PROG`, `NTAS` ou `DATM`.
- **Sete níveis de responsabilidade:** do nível 1 ao 7.
- **Atributos genéricos:** autonomia, influência, complexidade, conhecimento e comportamento.
- **Fatores comportamentais e declarações de conhecimento:** complementam a descrição de cada nível.

Os sete níveis têm frases orientadoras:

| Nível | Frase |
| --- | --- |
| 1 | Segue |
| 2 | Auxilia |
| 3 | Aplica |
| 4 | Possibilita |
| 5 | Garante e aconselha |
| 6 | Inicia e influencia |
| 7 | Define estratégia, inspira e mobiliza |

### Utilidade

- criar uma linguagem comum para vagas, equipes e desenvolvimento;
- descrever funções e expectativas de responsabilidade;
- analisar lacunas de competência;
- apoiar plano de carreira e treinamento;
- comparar habilidades sem depender de títulos de cargo.

### Limites

- o nível descreve responsabilidade e impacto, não apenas conhecimento técnico;
- não é certificação e não comprova competência por si só;
- exige evidência de prática, autonomia e resultados;
- o uso é licenciado pela SFIA Foundation;
- cópia e redistribuição exigem licença; o projeto não publica trechos nem níveis.

## 2. NICE

**NICE Workforce Framework for Cybersecurity**, do NIST, publicação SP 800-181 Revisão 1.

O NICE é específico de cibersegurança e foi criado para organizar o trabalho, a formação e a força de trabalho do setor.

### Estrutura da Revisão 1

- **Tasks:** o trabalho que precisa ser feito.
- **Knowledge e Skills:** o que a pessoa precisa saber e saber fazer.
- **Work Roles:** agrupamento de trabalho pelo qual alguém responde.
- **Competencies:** combinação de conhecimento, habilidade e contexto.
- **Categories e Specialty Areas:** foram descontinuadas na Revisão 1; organizações ainda podem usá-las.

A Revisão 1 **não define níveis de proficiência**.
Work Roles não são títulos de cargo nem ocupações.
O PDF do NIST não contém o catálogo completo de tarefas e work roles; esses artefatos são mantidos separadamente pelo NICE.

### Utilidade

- descrever trabalho de segurança em termos de tarefas e habilidades;
- apoiar contratação, treinamento e formação de equipes;
- criar perfis de trabalho específicos;
- alinhar educação e necessidades do setor.

### Limites

- foco em cibersegurança e contexto dos EUA;
- não define níveis de proficiência;
- o catálogo completo de work roles e tarefas não está no PDF da Revisão 1;
- sem os componentes adicionais, não há mapeamento completo.

## 3. Comparação

| | SFIA | NICE |
| --- | --- | --- |
| Escopo | TI e digital em geral | Cibersegurança |
| Estrutura | Habilidades e sete níveis | Tarefas, conhecimentos, habilidades e work roles |
| Níveis | Sim, 1 a 7 | Não define |
| Origem | SFIA Foundation | NIST |
| Licença | Uso pessoal/interno gratuito; cópia e redistribuição restritas | Publicação pública do NIST |
| Uso neste projeto | Vocabulário e perfil publicado em pt-BR | Referência para segurança, sem mapeamento de cargo |

## 4. Regras de aplicação

1. `dados-pessoais/fontes/competencias-declaradas.json` é a fonte factual local.
2. SFIA e NICE não criam competência; apenas organizam o que foi declarado e comprovado.
3. Nenhum nível SFIA será publicado sem evidência e aprovação do responsável.
4. Nenhum work role do NICE será tratado como cargo ou certificação.
5. Não haverá logotipo, selo ou alegação de certificação SFIA ou NICE.
6. O mapeamento foi publicado como autoavaliação em pt-BR; novas habilidades exigem aprovação.
7. A publicação continua em pt-BR primeiro.

## 5. Perfil SFIA

Perfil publicado em pt-BR em 02/11/2026 como autoavaliação.
Os níveis 4 a 7 não foram usados.
A revisão dos níveis está em [Requisitos](requisitos.md), §11 (P-14).

| Área declarada | Evidência atual | Habilidade SFIA | Níveis da habilidade | Nível adotado | Situação |
| --- | --- | --- | --- | --- | --- |
| Suporte técnico e incidentes | Lukos e Alpha; relatórios e texto do currículo | `USUP` — Gestão de incidentes | 1 a 6 | 3 — Aplica | Publicado. |
| Redes e fibra óptica | RealFort; relatório e galeria | `NTAS` — Suporte a redes | 1 a 5 | 3 — Aplica | Publicado. |
| Instalação e manutenção de sistemas | RealFort e Alpha | `HSIN` — Instalação e remoção de sistemas | 1 a 5 | 3 — Aplica | Publicado. |
| Suporte a aplicações | Lukos; ERP/PDV e NF-e/NFC-e | `ASUP` — Suporte a aplicações | 2 a 5 | 3 — Aplica | Publicado. |
| Operações de infraestrutura | Alpha e Lukos; suporte e monitoramento | `ITOP` — Operações de infraestrutura | 1 a 5 | 2 — Auxilia | Publicado. |
| Dados e SQL | Curso, projeto e competências | `DATM` — Gestão de dados | 2 a 6 | — | Não publicado; faixa 1–2. |
| Desenvolvimento web | Portfólio, SGCS e cursos | `PROG` — Programação/desenvolvimento de software | 2 a 6 | 2 — Auxilia | Publicado. |
| Gestão da configuração | Git, GitHub e documentação | `CFMG` — Gestão da configuração | 2 a 6 | — | Não publicado; evidência de versionamento. |
| Controle de mudanças | Procedimento de mudanças, commits e reversão | `CHMG` — Controle de mudanças | 2 a 6 | 2 — Auxilia | Publicado. |

Sete habilidades foram publicadas.
A publicação é uma autoavaliação.
Os níveis e as evidências podem ser revistos pelo responsável sem alterar a estrutura do bloco.

## 6. Piloto NICE

Não há mapeamento de work role nesta etapa.

Motivos:

- o PDF da Revisão 1 descreve a estrutura, mas não o catálogo completo;
- o site não publica um cargo de segurança;
- o conteúdo de segurança é transversal, não uma função dedicada;
- faltam os componentes de tarefas e work roles do NICE.

Próximo passo possível: obter os componentes oficiais do NICE e mapear apenas as tarefas de segurança que tenham evidência.
Sem esses componentes, o mapeamento seria inventado.

## 7. Publicação

O site exibe um bloco compacto em pt-BR desde 02/11/2026.
O bloco tem sete habilidades, níveis 2 e 3, evidência curta e nota de autoavaliação.
A seção inteira é um `<details>` nativo, fechada por padrão e colapsável.
A seção não depende de JavaScript.
Na impressão, uma cópia estática mostra o título e os cartões; a seção interativa fica oculta.
Os outros idiomas não receberam o bloco nesta etapa.
Não há work role NICE, selo ou logotipo.
A decisão A+B foi registrada em 02/11/2026: perfil em pt-BR, níveis 2 e 3, `CHMG` no lugar de `CFMG`; `CFMG` e `DATM` ficaram fora.
O histórico completo está no Git.

Qualquer nova publicação exige:

1. evidência da competência;
2. proposta de nível ou tarefa;
3. revisão do responsável;
4. registro da decisão.

## 8. Fontes e licenças

| Fonte | Caminho ou endereço | Uso |
| --- | --- | --- |
| SFIA — Referência da Estrutura, v9 (PT) | `REPERTORIO_TECNICO/11_COMPETENCIAS_PROFISSIONAIS/01_FRAMEWORKS_DE_COMPETENCIAS/SFIA - Referencia da Estrutura (PT) - v9.pdf` | Consulta interna. |
| SFIA — Sobre o SFIA, v9 (PT) | `REPERTORIO_TECNICO/11_COMPETENCIAS_PROFISSIONAIS/01_FRAMEWORKS_DE_COMPETENCIAS/SFIA - Sobre o SFIA (PT) - v9.pdf` | Consulta interna. |
| SFIA oficial | https://www.sfia-online.org | Referência e licenciamento. |
| NICE — SP 800-181 Rev. 1 (EN) | `REPERTORIO_TECNICO/11_COMPETENCIAS_PROFISSIONAIS/01_FRAMEWORKS_DE_COMPETENCIAS/NIST - SP 800-181 NICE Workforce Framework for Cybersecurity (EN) - Rev 1.pdf` | Consulta interna. |
| NICE oficial | https://doi.org/10.6028/NIST.SP.800-181r1 | Publicação pública do NIST. |

O SFIA é propriedade da SFIA Foundation.
O uso pessoal e a maior parte do uso interno de gestão são gratuitos; cópia, redistribuição e uso comercial exigem licença.
O projeto não copia o PDF para a base local versionada nem publica descrições ou tabelas do PDF no site.
A consulta usa a biblioteca principal; não há cópia local versionada.
O NICE é publicação do NIST, sem direitos autorais nos Estados Unidos; a atribuição é apreciada.

Os caminhos da tabela são relativos à raiz `REPERTORIO_TECNICO`.

## 9. Limites e revisão

- Não há avaliação independente de proficiência.
- Não há mapeamento NICE completo.
- Os níveis SFIA são autoavaliação.
- Nenhum nível 4 a 7 foi publicado.
- A revisão dos níveis está em [Requisitos](requisitos.md), §11 (P-14).
- O perfil SFIA é uma proposta de vocabulário, não um resultado.
- A revisão ocorre quando houver nova competência, certificação, projeto ou decisão de publicação.

## 10. Rubrica interna

A rubrica orienta a proposta de nível.
Ela não substitui evidência nem aprovação do responsável.
Os critérios são uma paráfrase interna; não reproduzem os descritores oficiais.

| Nível | Critério interno | Evidência mínima |
| --- | --- | --- |
| 1 | Executa tarefas rotineiras sob supervisão próxima e segue procedimentos. | Instrução recebida e tarefa conferida. |
| 2 | Auxilia a equipe, trabalha sob supervisão rotineira e resolve problemas rotineiros com critérios próprios. | Apoio documentado em rotina, chamado ou projeto. |
| 3 | Aplica métodos padrão, trabalha sob direção geral, gerencia o próprio trabalho e cumpre prazos. | Autonomia parcial e resultado entregue. |
| 4 | Possibilita o trabalho de outras pessoas, planeja e monitora atividades e melhora métodos. | Coordenação de pessoas ou processos. |
| 5 | Garante resultados e aconselha; define metas de qualidade e influencia decisões. | Responsabilidade por área ou serviço. |
| 6 | Inicia e influencia; define direção em uma área significativa. | Impacto organizacional amplo. |
| 7 | Define estratégia, inspira e mobiliza. | Responsabilidade estratégica. |

Processo:

1. Reunir evidência de experiência, projeto, curso ou certificação.
2. Comparar a evidência com o critério do nível.
3. Propor o nível e registrar a justificativa.
4. O responsável revisa e aprova.
5. Atualizar `dados-pessoais/fontes/competencias-declaradas.json` e o bloco do site.
6. Revisar quando houver novo projeto, certificado, função ou correção factual.

A rubrica não cria competência.
Ela apenas organiza a evidência que já existe.
