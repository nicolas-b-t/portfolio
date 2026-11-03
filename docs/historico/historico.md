# Histórico do projeto

Registros de 15 de outubro, 2 e 3 de novembro de 2026.
Este documento preserva decisões, medições e evidências da época.
Ele não é instrução vigente.

Instruções atuais: [Manutenção](../manutencao.md), [Requisitos](../requisitos.md) e [Competências](../competencias.md).

## Organização e recuperação

Reorganização: 15/10/2026.
Organização local: 02/11/2026.
Base anterior: commit `56f6430f296f24048fed4327ab68b9708ffb928d`.

Na reorganização de outubro, a árvore ativa passou de aproximadamente 110 MB para 14,4 MB, sem `.git`.
Saíram do repositório 125 arquivos de consulta, evidência histórica ou documentação substituída.

Em 02/11/2026, o repertório técnico voltou para `docs/repertorio-tecnico-site/` com catálogo, índice e 74 cópias, sem alteração dos bytes. Em 03/11/2026, foi movido para `docs/referencias/repertorio-tecnico-site/`.
Os dados pessoais foram reunidos em `dados-pessoais/`:

| Pasta | Conteúdo |
| --- | --- |
| `curriculos/` | quatro DOCX originais de outubro de 2026 |
| `experiencia-profissional/` | dois relatórios de experiência |
| `candidaturas/` | dois rascunhos de candidatura |

Duas pastas saíram do repositório sem alteração dos bytes: `docs/referencias/ats/repositorios-local/` e `.codex-remote-attachments/`.
Destino: `C:\Users\admin\Desktop\PROJETOS\IA-PROJETOS\_arquivo\site-curriculo-portfolio\2026-11-02\`.
O catálogo e o índice do repertório não fundamentam regras do projeto.

### Estrutura mantida

- `static/`: páginas, CSS, favicons e fotografias.
- `docs/curriculos/v3/`: dez PDFs atuais, índice e manifesto.
- `dados-pessoais/fontes/`: declarações, relatório acadêmico e manifestos.
- `docs/referencias/`: Europass, ATS e fontes externas.
- `docs/referencias/repertorio-tecnico-site/`: repertório técnico, ignorado pelo Git.
- `dados-pessoais/`: currículos, relatórios e rascunhos, ignorados pelo Git.
- `listas-de-tags/` e `docs/tags-multilingues/`: listas e traduções editoriais.

As cópias oficiais do Europass ficam em `docs/referencias/europass-fontes/`, versionadas e preservadas byte a byte.

### Padronização de nomes

As pastas passaram ao padrão do `AGENTS.md`: minúsculas, sem acentos, com hífens e no máximo quatro níveis.

| Antes | Depois |
| --- | --- |
| `Lista_de_tags/` | `listas-de-tags/` |
| `DADOS_PESSOAIS/` | `dados-pessoais/` |
| `docs/REPERTORIO_TECNICO_SITE/` | `docs/referencias/repertorio-tecnico-site/` |
| `docs/referencias/ats/originais-local/` | `docs/referencias/ats-local/` (arquivada em 03/11/2026) |
| `docs/referencias/europass/fontes/` | `docs/referencias/europass-fontes/` |
| `docs/fontes/academico/originais-local/` | `docs/fontes/academico-local/` (arquivada em 03/11/2026) |
| `docs/fontes/curriculos/` | `docs/fontes/curriculos-originais/` |

Em 03/11/2026, o conteúdo de `docs/fontes/` foi movido para `dados-pessoais/fontes/`.
| `docs/curriculos/v3/<idioma>/` | `docs/curriculos/v3/` |

### Arquivo anterior

As cópias integrais anteriores estão em seis ZIPs fora do repositório:
`/workspace/documentos-pessoais/arquivo-portfolio/2026-10-15/`.
O `manifesto-arquivo.json` registra membros, tamanhos e hashes SHA-256.
Para recuperar um arquivo versionado, use `git show 56f6430:caminho/do/arquivo`.
O histórico Git foi preservado; a limpeza não reescreveu commits.

## Mapa essencial e plano enxuto

Registro de 02/11/2026.
O plano enxuto foi registrado, não implementado.
O plano de 12 fases permanece em [Plano de 12 fases](plano-12-fases.md).

### Lição

- A biblioteca é um acervo, não um plano de projeto.
- Cobertura de pastas não é o mesmo que adequação ao risco.
- Documentação deve ser proporcional ao porte e à manutenção.
- Framework é meio de organização, não certificação e não fim.
- O plano de 12 fases cumpriu a cobertura pedida, mas criou simetria artificial.

### Cinco frentes

| Frente | Padrões mínimos | Onde está | Situação em 02/11/2026 |
| --- | --- | --- | --- |
| Conteúdo e idiomas | `pt-BR` como base, RFC 5646, guia de redação | Site, [Requisitos](../requisitos.md), [Guia de redação](../guia-de-redacao.md) | Ativa. |
| Web e acessibilidade | HTML Living Standard, CSS, WCAG 2.2 AA | `static/`, [Manutenção](../manutencao.md) | Ativa; faltavam testes de zoom, tema escuro, impressão e leitor de tela. |
| Segurança e privacidade | SSDF em nível alto, controles do GitHub, inventário de dados | [Manutenção](../manutencao.md), licença dos ícones | Ativa; 2FA e proteção da `main` pendentes. |
| Publicação e serviço | GitHub Pages, HTTPS, 404, verificação pós-push | `README.md`, workflow | Ativa. |
| Documentação e mudança | Diátaxis, Git, `CHANGELOG` | `docs/`, [Decisões](../decisoes.md) | Ativa. |

O plano enxuto não substitui automaticamente o plano de 12 fases.
Se for adotado, a substituição deve ser registrada como decisão.

## Verificações de 02/11/2026

### Página de projetos em pt-BR

Objetivo: separar a apresentação dos projetos, com acesso no início do currículo, CSS comum e descrições preservadas.
Fundamentação: HTML Living Standard, WCAG 2.2, propósito do link e foco visível.

Verificação: navegação de ida, três cartões, links e âncoras, um `main` por página, link de salto por teclado, temas claro/escuro e larguras de 1280 e 320 CSS px no Chromium local.
Não houve transbordamento horizontal.
Em impressão, a cópia oculta permaneceu invisível e os 17 cursos apareceram uma vez.

Limites: zoom real e paginação física não ensaiados; sem validação externa de HTML, leitor de tela ou conformidade WCAG.

### Ícones Lucide em pt-BR

Objetivo: centralizar os ícones em uma pasta e no CSS comum, com HTML/CSS estáticos e herança de cor nos temas.
Fundamentação: HTML Living Standard (`data-*`), CSS Color 4 (`currentcolor`), CSS Values 4 (URLs relativas), WCAG 2.2 (`1.1.1` e `1.4.11`) e CSS Color Adjustment 1.

Verificação: 28 SVGs em `static/assets/icons/`, seletores `[data-icon]` correspondentes, blocos ocultos preservados, 17 cursos na tela e na impressão, `git diff --check` limpo.

Limites: inspeção estática; ensaio visual interativo de `mask`, teclado, foco, contraste, 320 px, zoom, temas e paginação ficou pendente.

## Consolidação de 03/11/2026

- `docs/referencias/sfia-local/`: removida. Os originais permanecem na biblioteca principal e o perfil está em [Competências](../competencias.md).
- `docs/referencias/ats-local/`: movida para `_arquivo/site-curriculo-portfolio/2026-11-03/referencias-ats-local/`.
- `docs/fontes/academico-local/`: o PPC foi integrado em `dados-pessoais/fontes/academico/`; a pasta intermediária foi removida.
- `docs/fontes/`: movida para `dados-pessoais/fontes/`; os arquivos deixam de acompanhar o Git.
- `docs/referencias/repertorio-tecnico-site/`: base movida para dentro de `referencias`; o arquivamento dos 67 MB depende de P-15 em [Requisitos](../requisitos.md), §11.

Os antigos arquivos de histórico, o plano enxuto, as pendências, a análise SFIA e os ADRs foram fundidos nos documentos atuais.
O texto integral permanece no histórico Git.

## Regras

1. Não atualize um registro histórico para refletir o estado atual.
2. Uma correção factual entra como nota datada, não como reescrita.
3. Uma decisão nova entra em [Requisitos](../requisitos.md) ou em [Decisões](../decisoes.md).
4. Preserve os caminhos e as datas citados.
