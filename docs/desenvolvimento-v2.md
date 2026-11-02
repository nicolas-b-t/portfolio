# Desenvolvimento da versão 2

Início: 30/10/2026, por solicitação do responsável.
A versão 2 identifica a nova etapa de desenvolvimento do portfólio, apoiada em documentação técnica em todas as fases.
Não identifica uma nova edição dos currículos V3 nem uma publicação já realizada.

## Objetivo e arquitetura mantida

O produto é um currículo e portfólio estático, pessoal e multilíngue.
O público inclui recrutadores, profissionais da rede e leitores com diferentes dispositivos e necessidades de acesso.
`static/` contém o produto publicado. HTML, CSS comum, imagens e fontes do sistema constituem sua implementação.
GitHub Actions publica esse diretório no GitHub Pages. Não há JavaScript, backend ou etapa de build do site.
As regras de conteúdo e idiomas existentes continuam em [AGENTS.md](../AGENTS.md), [Manutenção](manutencao.md) e [Conteúdo e fontes](conteudo-e-fontes.md).

## Base e consulta

O [plano documental](referencias/desenvolvimento-v2/README.md) explica a seleção e suas limitações.
O [índice local](referencias/desenvolvimento-v2/indice-local.md) permite abrir cada documento sem acesso às bibliotecas externas.
O [catálogo](referencias/desenvolvimento-v2/catalogo.json) registra edição, procedência, tamanho e verificação das cópias.
Uma fonte técnica orienta o desenvolvimento; não amplia fatos do currículo.
Não confunda recomendações de guias, rascunhos e exemplos com requisitos obrigatórios.

## Fluxo de trabalho

1. Identifique a mudança, o público afetado e o resultado observável esperado.
2. Consulte a regra do projeto e a fonte local pertinente. Leia a seção aplicável, não apenas o título ou o catálogo.
3. Registre requisito, fonte e critério de aceitação na síntese do assunto. Para escolhas de arquitetura, registre contexto, alternativas, decisão e consequências.
4. Implemente a alteração e sincronize idiomas, conteúdo visível, impressão e dados derivados quando afetados.
5. Verifique o critério de aceitação. Registre resultado, ambiente, data e limitações; diferencie inspeção de código, teste automático e ensaio manual.
6. Revise o diff e a documentação. Antes de publicar, confira que somente `static/` será enviada e que a mudança tem autorização de publicação.
7. Após uma publicação autorizada, confira o resultado e registre o identificador da revisão e o meio de recuperação.

O tamanho do registro deve ser proporcional à mudança. Correções pequenas podem usar um parágrafo na síntese vigente.
Não crie relatórios paralelos para repetir a mesma conclusão. Quando faltar fundamento local, registre a lacuna antes de decidir pela ampliação da base.

## Matriz inicial de regras e evidências

Esta matriz operacionaliza regras já definidas pelo responsável. As fontes são apoio técnico, não declaração de certificação.
Os identificadores de fonte resolvem para arquivos no índice local. A verificação do produto deverá ocorrer nas mudanças pertinentes; não foi executada nesta preparação documental.

| ID | Regra ou decisão | Fonte e localização para consulta | Aceitação e evidência |
| --- | --- | --- | --- |
| V2-01 | Manter HTML/CSS estáticos e semântica nativa | AGENTS.md; REF-0041, “Semantics, structure, and APIs of HTML documents” e “The elements of HTML” | Revisar elementos, títulos, estrutura, links e ausência de scripts no produto; validar HTML quando pertinente |
| V2-02 | Manter CSS comum, recursos locais e alternativas compatíveis | REF-0045, cascata; REF-0049, display; REF-0050/0052, layouts; REF-0059, media types; REF-0058, paged media | Conferir telas pequenas, zoom, impressão, suporte das propriedades alteradas e caminhos relativos |
| V2-03 | Usar WCAG 2.2 AA como alvo | REF-0127/0128: 1.1.1, 1.3.1, 1.4.3, 1.4.4, 1.4.10, 1.4.11, 2.1.1, 2.4.1, 2.4.7, 2.4.11 e 2.5.8; REF-0124, requisitos de uso de ARIA | Verificar alternativas textuais, teclado, foco, contraste, reorganização e alvos; registrar exceções e limitações sem declarar conformidade integral |
| V2-04 | Preservar temas e redução de movimento | EXT-03, “prefers-reduced-motion” e “prefers-color-scheme”; EXT-04, “Preferred Color Schemes” e “Forced Color Palettes” | Exercitar preferências e temas afetados; tratar o rascunho e a candidata a recomendação como referências com suporte a confirmar |
| V2-05 | Sincronizar cinco variantes sem ampliar qualificações | Conteúdo e fontes; EXT-01, seção 2, “The Language Tag”; REF-0041, atributo lang e hreflang | Conferir pt-BR, pt-PT, en-US, es-419 e es-ES, nomes oficiais, datas, cursos e limites factuais |
| V2-06 | Escrever textos autorais claros e rastrear requisitos | Guia de redação; REF-0368, Part 1, Writing Rules; REF-0122, “Formular requisitos” e “Manter a fundamentação”; REF-0020, Work Products | Revisão humana de clareza; cada requisito com origem, resultado observável e método de verificação |
| V2-07 | Documentar decisões e organizar orientação por finalidade | REF-0341, ADR Template Minimal; REF-0071, How-to Guides, Reference e Explanation; FAS-1654, seção 2 | Registrar contexto, decisão, consequências e referências na síntese apropriada; fonte FAS apenas histórica |
| V2-08 | Revisar mudanças e verificar regressões proporcionais ao risco | REF-0117, What to Look for in a Code Review e Small Change Lists; REF-0025, fundamentos de teste e testes de manutenção | Diff revisado, git diff --check e evidências dos fluxos afetados; registrar testes não realizados |
| V2-09 | Controlar versões, proteger fontes privadas e limitar publicação | REF-0116, Git Basics; FAS-1653, seções 7 e 9.1; REF-0035, Protect the Software; EXT-02, Deploying GitHub Pages artifacts | Identificar revisão, preservar alterações existentes, excluir fontes do Git e conferir artefato contendo somente static/ |
| V2-10 | Planejar, acompanhar e encerrar cada entrega | REF-0001, seções 2.2.2, 3.2 e 3.6 | Objetivo, escopo, resultado, verificação e pendências registrados; adaptar os artefatos ao porte pessoal do projeto |

## Registro mínimo de mudança

Use os campos abaixo na documentação do assunto; não preencha resultados antes de realizar a verificação.

```text
Data e revisão:
Objetivo e arquivos afetados:
Regra/requisito:
Fonte local e seção/página:
Decisão e justificativa:
Critério de aceitação:
Verificação realizada, ambiente e resultado:
Limitações ou pendências:
```

## Decisão inicial V2-D01

Contexto: o responsável solicitou literatura local antes de encerrar o acesso às bibliotecas externas.
Decisão: copiar uma seleção de fontes para `docs/referencias/desenvolvimento-v2/fontes-local/`, preservar os bytes e manter catálogo e índice relativos.
Alternativas avaliadas: depender das pastas externas impediria a consulta após revogação; copiar os acervos inteiros acrescentaria material sem aplicação ao portfólio.
Consequência: o projeto local dispõe das fontes selecionadas; clones do Git exigem transferência separada da pasta privada para reproduzir essa disponibilidade.
Fundamentação: pedido do responsável; REF-0341 como estrutura de decisão; FAS-1653, conceito histórico de baseline; regras de preservação do projeto.
Estado: execução do pedido de seleção e cópia. Não equivale a aprovação humana individual das interpretações nem a revisão integral do site.
