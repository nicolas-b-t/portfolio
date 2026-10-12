# Pendências do projeto

Atualizado em 10 de outubro de 2026.

## Acesso a Optigrow e SGCS

**Estado: investigação encerrada por decisão do responsável em 10 de outubro de 2026.**

O responsável autorizou e concluiu um login independente no GitHub CLI como `nicolas-b-t`.
Os testes posteriores retornaram HTTP 404 na API e HTTP 403 na leitura pelo Git.
Nenhum dos dois repositórios foi baixado.

Requisições sem credencial e com uma credencial inválida identificaram a mesma conta.
Esse comportamento indica autenticação intermediada pelo ambiente.
Retirar `GH_TOKEN` não demonstrou que as requisições usaram o token do novo login.
A instalação visível do conector pertence à conta `nicolas-b-t`.
O acesso pessoal como editor não comprova autorização dessa integração para repositórios de outros proprietários.

- Optigrow: https://github.com/RodrigoNKC/optigrow.
- SGCS: https://github.com/SGCS-Gestao-de-Chamados-Para-Sindicos/SGCS-espelho.

A configuração local usada no diagnóstico foi removida ao encerrar a investigação.
Essa remoção não revoga a autorização concedida no GitHub.
Código, arquitetura e participação individual permanecem sem análise independente dos repositórios.

## Autoteste de inglês

**Estado: pausado por decisão do responsável em 10 de outubro de 2026.**

Retome a avaliação conforme o [plano](autoavaliacao-ingles.md) e o [guia](guia-autoteste-ingles.md).
A leitura e a primeira escrita já receberam análise orientativa.
Outra escrita, leitura ampliada, compreensão oral e fala permanecem pendentes.
Não publique níveis finais antes de reunir e revisar as evidências.

## Modelo para colegas e amigos

**Estado: intenção futura, sem implementação nesta etapa.**

O portfólio permanece pessoal.
Antes de preparar um modelo, separe conteúdo pessoal e código reutilizável.
Defina a licença autoral, os exemplos neutros e as instruções de personalização.
Planeje também a atualização dos idiomas após estabilizar a página pt-BR.
