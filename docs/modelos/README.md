# Modelos de HTML

Modelos para copiar e preencher ao adicionar conteúdo em `static/pt-BR/index.html`.
A norma que explica as regras está em [Padrão de HTML](../padrao-html.md).

## Índice

| Modelo | Usar para |
| --- | --- |
| [pagina.html](pagina.html) | Estrutura do documento, cabeçalho, hero, rodapé e cópia oculta. |
| [perfil.html](perfil.html) | Seção Perfil e o resumo profissional oculto. |
| [competencias.html](competencias.html) | Categoria, subcategoria, âncora e tag de competência. |
| [experiencia.html](experiencia.html) | Item da linha do tempo e o espelho oculto. |
| [formacao.html](formacao.html) | Instituição, curso e conteúdos previstos. |
| [cursos.html](cursos.html) | Curso na tela e na impressão. |
| [sfia.html](sfia.html) | Item SFIA na tela e na impressão. |
| [contato.html](contato.html) | Item de contato e o espelho oculto. |

## Como usar

1. Copie o bloco para a seção certa.
2. Preencha todos os `{{CAMPO}}`.
3. Apague os blocos marcados como `OPCIONAL` que não tiverem fonte confirmada.
4. Espelhe o mesmo conteúdo na cópia oculta e, quando existir, na impressão.
5. Rode a conferência da seção 8 do [Padrão de HTML](../padrao-html.md).
6. Registre a mudança no [CHANGELOG](../../CHANGELOG.md).

## Regras rápidas

- Não copie modelo para `static/` com marcador.
- Não invente fato para preencher campo.
- Não reordene o menu.
- Uma competência por `li`.
- Data sempre em `<time datetime>`.
- Tela, cópia oculta e impressão precisam ter os mesmos fatos.
