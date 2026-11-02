# Organização e recuperação do acervo

Reorganização: 15 de outubro de 2026.
Organização local: 2 de novembro de 2026.
Base anterior: commit `56f6430f296f24048fed4327ab68b9708ffb928d`.

A estrutura foi avaliada com `Get-ChildItem -Recurse -Depth 3 -Force` antes e depois de cada limpeza.
Na reorganização de 15 de outubro, a árvore ativa passou de aproximadamente 110 MB para 14,4 MB, sem contar `.git`, e 125 arquivos de consulta, evidência histórica ou documentação substituída saíram do repositório.

## Organização de 2 de novembro de 2026

O repertório técnico de consulta voltou para `docs/repertorio-tecnico-site/`, com catálogo, índice e as 74 cópias, sem alteração dos bytes. A pasta inteira é ignorada pelo Git.

Os dados pessoais foram reunidos em `dados-pessoais/`, também ignorada pelo Git:

| Pasta | Conteúdo |
| --- | --- |
| `curriculos/` | quatro DOCX originais de outubro de 2026 |
| `experiencia-profissional/` | dois relatórios de experiência |
| `candidaturas/` | dois rascunhos de candidatura |

Duas pastas saíram do repositório, sem alteração dos bytes:

| Pasta | Conteúdo |
| --- | --- |
| `docs/referencias/ats/repositorios-local/` | clones de terceiros usados nos ensaios de leitura |
| `.codex-remote-attachments/` | anexo temporário de sessão remota |

Destino: `C:\Users\admin\Desktop\PROJETOS\IA-PROJETOS\_arquivo\site-curriculo-portfolio\2026-11-02\`.
O catálogo e o índice do repertório não fundamentam regras do projeto; a documentação de manutenção, conteúdo e redação permanece em `docs/`.

## Estrutura mantida

- `static/`: páginas, CSS, favicons e fotografias do site.
- `docs/curriculos/v3/`: dez PDFs atuais, índice e manifesto.
- `docs/fontes/`: declarações, relatório acadêmico do SGCS e manifestos necessários à conferência do conteúdo.
- `docs/referencias/`: Europass, instruções ATS e referências úteis ao desenvolvimento.
- `docs/repertorio-tecnico-site/`: repertório técnico de consulta, ignorado pelo Git.
- `dados-pessoais/`: currículos originais, relatórios de experiência e rascunhos de candidatura, ignorados pelo Git.
- `listas-de-tags/` e `docs/tags-multilingues/`: listas de consulta, glossário e traduções editoriais.
- Guias de manutenção, redação e atribuição de conteúdo, com um índice central.

As pastas com sufixo `-local` guardam cópias de consulta e ficam fora do Git: `docs/referencias/ats-local/` e `docs/fontes/academico-local/`.
As cópias oficiais do Europass ficam em `docs/referencias/europass-fontes/`, versionadas e preservadas byte a byte.

## Padronização de nomes

Na mesma data, as pastas passaram ao padrão do `AGENTS.md`: minúsculas, sem acentos, com hífens e no máximo quatro níveis.

| Antes | Depois |
| --- | --- |
| `Lista_de_tags/` | `listas-de-tags/` |
| `DADOS_PESSOAIS/` | `dados-pessoais/` |
| `docs/REPERTORIO_TECNICO_SITE/` | `docs/repertorio-tecnico-site/` |
| `docs/REPERTORIO_TECNICO_SITE/fontes-local/<grupo>/` | `docs/repertorio-tecnico-site/<grupo>/` |
| `docs/referencias/ats/originais-local/` | `docs/referencias/ats-local/` |
| `docs/referencias/europass/fontes/` | `docs/referencias/europass-fontes/` |
| `docs/fontes/academico/originais-local/` | `docs/fontes/academico-local/` |
| `docs/fontes/curriculos/` | `docs/fontes/curriculos-originais/` |
| `docs/curriculos/v3/<idioma>/` | `docs/curriculos/v3/` |

Nenhum caminho do site publicado mudou.

## Arquivo anterior

As cópias integrais anteriores estão preservadas em seis ZIPs fora do repositório:

`/workspace/documentos-pessoais/arquivo-portfolio/2026-10-15/`

O arquivo `manifesto-arquivo.json`, nessa pasta, registra os membros, os tamanhos e os hashes SHA-256.
Os ZIPs preservam as fontes, as licenças, os avisos e os relatórios recebidos.
O arquivo amplo permanece local. O Drive contém somente a documentação Europass/ATS e os currículos solicitados.

Para recuperar um arquivo versionado anterior, use `git show 56f6430:caminho/do/arquivo` e confira o manifesto quando disponível.
O histórico Git foi preservado. Esta limpeza reduz a árvore de trabalho, sem reescrever commits antigos.
Uma nova cópia obtida com `git clone --depth 1` contém somente o histórico necessário ao estado atual.

Os materiais temporários desta tarefa ficaram em `work/`, fora do checkout do projeto.
Não acrescente esses auxiliares novamente à árvore ativa.
