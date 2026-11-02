# Competências e frameworks de referência

Este documento explica o SFIA e o NICE, sua utilidade e a forma de aplicação neste projeto.
As declarações factuais continuam em [competências declaradas](fontes/competencias-declaradas.json).

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
- não é certificação;
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
| Uso neste projeto | Vocabulário e candidatos de habilidade | Referência para segurança, sem mapeamento de cargo |

## 4. Regras de aplicação

1. `docs/fontes/competencias-declaradas.json` é a fonte factual.
2. SFIA e NICE não criam competência; apenas organizam o que foi declarado e comprovado.
3. Nenhum nível SFIA será publicado sem evidência e aprovação do responsável.
4. Nenhum work role do NICE será tratado como cargo ou certificação.
5. Não haverá logotipo, selo ou alegação de certificação SFIA ou NICE.
6. O mapeamento começa como proposta e só vira conteúdo do site após aprovação.
7. A publicação continua em pt-BR primeiro.

## 5. Piloto SFIA

Candidatos de habilidade, sem atribuição de nível.
O nível depende de evidência de autonomia, complexidade e impacto.

| Área declarada | Evidência atual | Habilidade SFIA | Níveis da habilidade | Situação |
| --- | --- | --- | --- | --- |
| Suporte técnico e incidentes | Relatórios de experiência e texto do currículo | `USUP` — Gestão de incidentes | 1 a 6 | Candidato. |
| Redes e fibra óptica | Relatório da RealFort e galeria | `NTAS` — Suporte a redes | 1 a 5 | Candidato. |
| Instalação e manutenção de sistemas | Relatório da RealFort e experiência | `HSIN` — Instalação e remoção de sistemas | 1 a 5 | Candidato. |
| Operações de infraestrutura | Experiência em suporte e redes | `ITOP` — Operações de infraestrutura | 1 a 5 | Candidato. |
| Dados e SQL | Curso, projeto e competências | `DATM` — Gestão de dados | 2 a 6 | Candidato. |
| Desenvolvimento web | Projetos e competências | `PROG` — Programação e desenvolvimento de software | 2 a 6 | Candidato. |
| Gestão da configuração | Git, GitHub e documentação | `CFMG` — Gestão da configuração | 2 a 6 | Candidato. |
| Controle de mudanças | Fluxo de commits e revisão | `CHMG` — Controle de mudanças | 2 a 6 | Candidato. |

Nenhum nível foi atribuído.
Nenhum candidato foi publicado no site.

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

Nesta etapa, o uso é interno.
O site não exibe níveis SFIA, work roles NICE, selos ou logotipos.
Qualquer publicação exige:

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
O projeto não copia o PDF para a base local nem publica trechos no site.
O NICE é publicação do NIST, sem direitos autorais nos Estados Unidos; a atribuição é apreciada.

Os caminhos da tabela são relativos à raiz `REPERTORIO_TECNICO`.

## 9. Limites e revisão

- Não há avaliação de proficiência.
- Não há mapeamento NICE completo.
- Não há aprovação para publicar níveis ou work roles.
- O piloto SFIA é uma proposta de vocabulário, não um resultado.
- A revisão ocorre quando houver nova competência, certificação, projeto ou decisão de publicação.
