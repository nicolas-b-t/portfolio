# Documentação formal do projeto

> Índice da documentação formal · versão 1.0 · situação: revisão · base: 445ea45 · revisão: 2026-11-05 · responsável: operador

Ponto de entrada para pessoas e agentes. Os dois documentos abaixo são a fonte canônica.
Este arquivo não repete o conteúdo deles; apenas indica onde ler e como conferir.

## 1. Ordem de leitura

1. `../../AGENTS.md`: regras que valem para todo o repositório.
2. `../requisitos.md`: requisitos, pendências e limites.
3. `../decisoes.md`: decisões de arquitetura.
4. `../manutencao.md`: operação, publicação e incidente.
5. `arquitetura.md`: estrutura do site e da publicação.
6. `processos.md`: processos de mudança, edição de currículo e incidente.

## 2. Documentos

| ID | Documento | Conteúdo | Situação |
| --- | --- | --- | --- |
| DOC-ARQ-01 | [Arquitetura](arquitetura.md) | Contexto, contêineres, componentes, implantação, mapa do site, modelo de conteúdo e decisões. | Revisão |
| DOC-PRC-01 | [Processos](processos.md) | Papéis, cadeia de valor, PRC-01 a PRC-03, portas G0 a G4, decisões e registros. | Revisão |

## 3. Diagramas

Nove diagramas, todos em Mermaid. Mermaid é a ferramenta; o perfil é do projeto.
Não há conformidade com C4, BPMN 2.0 ou DMN.

| ID | Diagrama | Tipo | Onde | Mostra |
| --- | --- | --- | --- | --- |
| D-01 | Contexto | Fluxo | `arquitetura.md` §3 | Atores, sistema e links externos. |
| D-02 | Contêineres | Fluxo | `arquitetura.md` §4 | Navegador, site, Pages, Actions e repositório. |
| D-03 | Componentes de página | Fluxo | `arquitetura.md` §5 | Cabeçalho, conteúdo, CSS e cópias. |
| D-04 | Implantação | Fluxo | `arquitetura.md` §6 | Envio, workflow, Pages e navegador. |
| D-05 | Modelo de conteúdo | ER | `arquitetura.md` §8 | Entidades e relações. |
| D-06 | Cadeia de valor | Fluxo | `processos.md` §3 | Demanda até registro. |
| D-07 | PRC-01 | Fluxo com raias | `processos.md` §4 | Mudança e publicação. |
| D-08 | PRC-02 | Fluxo | `processos.md` §5 | Edição de currículo. |
| D-09 | PRC-03 | Fluxo | `processos.md` §6 | Incidente. |

Legenda: retângulo é ator, sistema, componente, etapa ou entidade; seta é fluxo ou relação;
subgrafo é raia; o diagrama ER usa pé de galinha. As tabelas de decisão de `processos.md` §8
não são diagramas.

Verificação manual: abra o arquivo no GitHub e confira a renderização dos 9 blocos.

## 4. Fatos e fontes

| Assunto | Fonte canônica |
| --- | --- |
| Regras do projeto | [`AGENTS.md`](../../AGENTS.md) |
| Requisitos e pendências | [`docs/requisitos.md`](../requisitos.md) |
| Decisões de arquitetura | [`docs/decisoes.md`](../decisoes.md) |
| Operação e publicação | [`docs/manutencao.md`](../manutencao.md) |
| Conteúdo e atribuições | [`docs/conteudo-e-fontes.md`](../conteudo-e-fontes.md) |
| Histórico de mudanças | [`CHANGELOG.md`](../../CHANGELOG.md) |
| Páginas publicadas | [`static/`](../../static/) |

## 5. Invariantes

- O site é estático. Não adicione JavaScript, formulário, iframe ou etapa de build.
- Não altere `static/` sem autorização do responsável.
- Preserve fatos, datas, vínculos, cargos e níveis. Não infira o que não está escrito.
- Um fato ausente é "não confirmado". Registre a lacuna; não invente a fonte.
- A documentação não é publicada. O workflow publica somente `static/`.
- Os textos seguem a redação enxuta do projeto, sem declarar certificação.

## 6. Como citar

| Alvo | Forma | Exemplo |
| --- | --- | --- |
| Documento Markdown | Caminho e âncora de seção | `docs/manutencao.md#definition-of-done` |
| Código ou arquivo estável | Caminho e linha | `static/pt-BR/index.html:17` |
| Decisão | ID e âncora | `docs/decisoes.md#0008--publicação-temporária-de-duas-variantes` |
| Requisito | ID | `NFR-02` |

Não cite linha de documento Markdown: o número muda a cada edição.

## 7. Verificação

Execute na raiz do repositório:

```powershell
git diff --check
git status --short
```

Depois confira:

- cada link relativo abre o arquivo indicado;
- cada citação `arquivo#âncora` corresponde a um título existente;
- cada citação `arquivo:linha` existe no arquivo;
- `static/` não tem alteração sem autorização;
- a contagem de páginas HTML confere com a seção 7 de `arquitetura.md`.

Não há validador automático nem CI de documentação (`P-15`). A conferência é manual.

## 8. Referências de método

A estrutura adapta estas obras. Não há cópia nem declaração de conformidade.

| Referência | Obra | Uso |
| --- | --- | --- |
| `REF-0078` | arc42, versão 8.3 | Seções de arquitetura. |
| `REF-0070` | C4 model | Contexto, contêineres e componentes. |
| `REF-0024` | BPMN 2.0 | Notação adaptada dos processos. |
| `REF-0013` | DMN | Tabelas de decisão. |

Os identificadores remetem ao catálogo do `REPERTORIO_TECNICO`, fora deste repositório.
