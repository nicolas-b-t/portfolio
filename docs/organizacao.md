# Organização e recuperação do acervo

Reorganização: 15 de outubro de 2026.
Base anterior: commit `56f6430f296f24048fed4327ab68b9708ffb928d`.

O comando `tree -a -L 3 -I .git` foi usado para avaliar a estrutura antes e depois da limpeza.
A árvore ativa passou de aproximadamente 110 MB para 14,4 MB, sem contar `.git`.
Foram retirados 125 arquivos de consulta, evidência histórica ou documentação substituída.

## Estrutura mantida

- `static/`: páginas, CSS, favicons e fotografias do site.
- `docs/curriculos/v3/`: dez PDFs atuais, índice e manifesto.
- `docs/fontes/`: declarações, relatório acadêmico do SGCS e manifestos necessários à conferência do conteúdo.
- `docs/referencias/`: Europass, instruções ATS e referências úteis ao desenvolvimento.
- `Lista_de_tags/` e `docs/tags-multilingues/`: listas de consulta, glossário e traduções editoriais.
- Guias de manutenção, redação e atribuição de conteúdo, com um índice central.

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
