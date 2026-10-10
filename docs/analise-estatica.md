# Análise estática do portfólio

Este documento registra a análise inicial, antes das correções. Para o estado
das versões em `static/`, veja [as alterações de acessibilidade](acessibilidade.md).

## Estrutura

O site inicial contém duas páginas HTML (português e inglês), uma folha CSS
compartilhada e um favicon SVG. Não há JavaScript, dependências, ferramentas
de build, backend ou suíte de testes. A pasta `static/` guarda cópias por
idioma com recursos próprios e caminhos relativos ajustados.

## Pontos positivos

- HTML com `header`, `nav`, `main`, `section`, `article` e `footer`.
- Idiomas declarados com `lang` e alternativas com `hreflang`.
- Títulos e descrições presentes; hierarquia de títulos com um H1 por página.
- Link para pular ao conteúdo e destaque de foco para navegação por teclado.
- Layout com Flexbox, Grid e tamanhos de fonte adaptáveis.
- Tema escuro automático e regras específicas para impressão do currículo.
- Recursos locais e fontes do sistema, sem scripts ou rastreadores externos.

## Pendências encontradas no código

1. Nome, resumo, experiências, formação, projetos e contatos são exemplos.
   Os três links de projetos em cada idioma usam `href="#"` e não abrem projetos.
2. A rolagem suave não possui uma alternativa para `prefers-reduced-motion`.
3. O cabeçalho fixo pode cobrir os títulos ao navegar por âncoras; não há
   `scroll-margin-top` ou `scroll-padding-top` para compensar sua altura.
4. No tema escuro, o botão principal usa texto branco sobre `#8ea2ff`:
   contraste aproximado de 2,4:1, abaixo de 4,5:1 para texto normal.
5. `.hero` e `section` sobrescrevem o padding de `.wrap`, removendo o espaço
   horizontal dessas seções. Em telas pequenas, o conteúdo pode encostar nas bordas.
6. A grade usa colunas com largura mínima de `16rem`; espaços menores podem
   causar transbordamento horizontal. É necessário confirmar em navegador.
7. Não há URL canônica, metadados Open Graph ou imagem de compartilhamento.
   São melhorias para publicação e dependem do domínio definitivo.
8. As traduções são mantidas manualmente; alterações precisam ser revisadas
   nos dois idiomas para evitar divergências.

## Escopo da verificação

Leitura do HTML, CSS e SVG, inspeção de links relativos, IDs e âncoras, e
validação HTTP das cópias estáticas. Links externos e conteúdo pessoal não
foram validados. Não houve auditoria visual, teste com leitor de tela ou
validação completa de conformidade HTML/CSS. Os problemas acima foram
registrados para trabalho posterior; o conteúdo original foi preservado.
