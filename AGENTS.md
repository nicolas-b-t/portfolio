# Orientações do projeto

Estas instruções se aplicam ao repositório inteiro e orientam pessoas e agentes
que trabalhem no portfólio.

## Redação: ASD-STE100, edição 9

Toda a documentação autoral e todo o texto apresentado ao visitante devem
seguir os princípios da ASD-STE100, edição 9, adaptados ao idioma do texto.
A referência está em
`docs/referencias/asd-ste100/ASD-STE100-issue-9-2025-01-15.pdf`, de 15 de
janeiro de 2025. O PDF permanece somente no ambiente local.

Para textos em português, aplique estas regras do projeto:

- Use palavras conhecidas e termos técnicos precisos. Use o mesmo termo para
  o mesmo conceito. Explique siglas quando o contexto não esclarecer seu sentido.
- Preserve a gramática portuguesa. O dicionário e as restrições gramaticais
  da norma inglesa não constituem um dicionário aprovado em português.
- Prefira voz ativa e verbos diretos. Identifique quem realiza a ação.
  Use passado para atividades concluídas e presente para atividades atuais.
- Nas instruções, use o imperativo e apresente uma ação por frase.
  Coloque uma condição necessária antes da ação correspondente.
- Adote como limites de revisão 20 palavras por frase de instrução e
  25 palavras por frase descritiva. Divida frases longas sem alterar seu sentido.
- Trate nomes próprios, títulos oficiais, identificadores e unidades como
  elementos únicos na contagem, conforme a seção 8 da referência.
  A contagem automática por espaços serve apenas como triagem.
- Apresente um assunto por parágrafo, com no máximo seis frases.
  Ordene a informação conforme a necessidade do leitor.
- Separe instruções, informações e resultados de verificação.
  Descreva condições, fontes e limites quando forem necessários à compreensão.
- Use pontos para separar frases. Evite ponto e vírgula na prosa.
  Preserve pontuação exigida por código, dados estruturados e citações.
- Nas tags, mantenha “habilidade, observação”. Acrescente observações somente
  quando necessárias. Use “e” para unir competências, sem barras ambíguas.
  Preserve barras que integrem identificadores técnicos, como SC/APC e N1/N2.
- Preserve nomes oficiais, qualificações, datas, valores e contexto profissional.
  A revisão de texto não autoriza ampliar competências ou remover limitações.
- Preserve documentos oficiais, fontes recebidas, licenças e citações literais.
  A regra aplica-se aos textos que escrevemos sobre essas fontes.
- Revise clareza e precisão manualmente. Não declare conformidade formal com
  STE com base nesta adaptação ou em verificações automáticas.

Esta é uma política de redação baseada na norma inglesa, não uma tradução
oficial nem uma certificação STE. Nos demais idiomas, preserve a gramática
local e aplique os mesmos princípios de clareza e precisão.
O guia detalhado está em `docs/guia-de-redacao.md`, versionado no repositório.

## Objetivos

Priorize robustez, compatibilidade, acessibilidade, portabilidade e minimalismo.
Use somente as tecnologias e dependências necessárias para atender ao conteúdo.

## Regra: site sem JavaScript

- O portfólio deve funcionar integralmente com HTML e CSS, sem JavaScript.
- Não adicione scripts próprios ou externos.
  Não adicione elementos `script`, eventos como `onclick` ou URLs `javascript:`.
  Não adicione frameworks ou componentes que dependam de JavaScript.
- Não adicione rastreadores, widgets ou embeds que executem JavaScript.
- Use elementos HTML nativos e CSS para navegação e apresentação.
  Se um recurso exigir JavaScript, explique a limitação.
  Proponha uma alternativa sem scripts.
  Não altere esta regra sem uma decisão explícita do responsável pelo projeto.
- Esta regra se refere ao site entregue ao visitante.
  Ferramentas de manutenção externas não devem introduzir scripts no conteúdo
  publicado. Não acrescente dependências sem necessidade demonstrada.
- Preserve as cópias oficiais e seus avisos de licença em `docs/referencias/`,
  inclusive scripts dos documentos originais. Não os incorpore ao site.
- A documentação de `docs/` é versionada desde 10 de outubro de 2026.
  Essa decisão substitui a exclusão anterior da pasta inteira.
  Preserve as exceções específicas do `.gitignore` para PDFs restritos e dados privados.
  Não use `git add --force` para incluir essas exceções.
  Mantenha os originais excluídos no ambiente e documente sua recuperação.
- O projeto permanece pessoal. A adaptação como modelo para colegas e amigos
  está planejada para uma etapa futura, sem autorização para reutilizar dados pessoais.

## HTML, CSS e compatibilidade

- Siga o HTML Living Standard da WHATWG. Prefira elementos semânticos e recursos
  nativos. Use ARIA apenas quando a semântica HTML não for suficiente.
- Mantenha UTF-8 em cada página.
  Use títulos descritivos e uma hierarquia coerente.
  Confira o atributo `lang` de cada página.
- Prefira recursos CSS amplamente suportados, usando Baseline Widely Available
  como referência. Para recursos de suporte limitado, forneça uma alternativa.
- Use layouts fluidos que suportem telas pequenas, zoom e textos longos.
- Preserve o foco visível. Respeite `prefers-reduced-motion`.
  Confira temas claro e escuro e a impressão do currículo.
- Use fontes do sistema e recursos locais. Evite serviços externos para funções
  básicas, bibliotecas de ícones e dependências puramente decorativas.
- Prefira código legível, seletores simples e nomes descritivos. Respeite a
  formatação existente e evite abstrações sem benefício concreto.

## Acessibilidade

- Use WCAG 2.2 nível AA como alvo. As referências estão em
  `docs/referencias/w3c/`. Diferencie recomendações publicadas de rascunhos.
- Garanta navegação por teclado, link para pular ao conteúdo, ordem lógica de
  foco e nomes compreensíveis para links e controles.
- Confira contraste de texto e controles, alternativas textuais quando
  necessárias e conteúdo que se reorganize sem perda de informação.
- Evite links vazios ou de exemplo na versão destinada à publicação.
- Não declare conformidade apenas com base em verificações automáticas.

## Idiomas, estrutura e portabilidade

- A revisão atual abrange toda a documentação autoral e somente a página
  principal `static/pt-BR/index.html`. O responsável confirmou esse escopo em
  9 de outubro de 2026 para aplicar os princípios da ASD-STE100.
  As demais páginas e idiomas aguardam revisão posterior.
  Esta restrição prevalece sobre a orientação geral de sincronizar traduções.
- Os commits dessa revisão devem informar explicitamente o escopo “pt-BR,
  página principal” no título ou na descrição. Registros de escopo nas instruções
  da raiz são permitidos. Mantenha a documentação detalhada em `docs/`, agora versionada.
- Mantenha as versões `pt-BR`, `pt-PT`, `en`, `es-419` e `es-ES`, com `lang`,
  `hreflang` e links de troca de idioma corretos. `es-419` usa redação neutra
  para o público sul-americano. A etiqueta abrange América Latina e Caribe.
- A pasta `static/` é a única fonte do site publicado. `static/index.html`
  permite escolher o idioma. Cada etiqueta tem sua própria pasta de páginas.
- Revise o impacto de alterações nas cinco versões. Enquanto houver CSS e
  recursos duplicados por idioma, mantenha-os consistentes. Prefira recursos
  compartilhados quando uma reorganização da estrutura estiver no escopo.
- Use caminhos relativos para recursos e páginas internas, de modo que o site
  possa ser servido em diferentes hospedagens e subdiretórios.
- Nas competências, preserve as três categorias principais.
  Organize as tags em subcategorias. Use o formato “habilidade, observação”.
  Reserve observações para informações necessárias.
  Preserve as qualificações aprovadas pelo responsável e a formação em andamento.
- Preserve o funcionamento como arquivos estáticos, sem exigir backend,
  framework, gerenciador de pacotes ou etapa de build.
- Não inclua credenciais ou configurações específicas de uma máquina no site.

## Verificação e trabalho no repositório

- Leia estas instruções antes de editar.
  Confira `git status --short`. Preserve mudanças existentes.
  Não sobrescreva arquivos do usuário sem necessidade.
- Use o checkout existente. Cada tarefa na nuvem já é isolada.
  Não crie worktrees sem pedido explícito do usuário.
- Para verificar `static/`, execute na raiz:
  `python3 -m http.server 8001 --bind 127.0.0.1 --directory static`.
  A escolha de idioma está em `/`, e as páginas em `/pt-BR/`, `/pt-PT/`,
  `/en/`, `/es-419/` e `/es-ES/`. Use outra porta se estiver ocupada.
  O servidor Python é uma ferramenta de desenvolvimento, não uma dependência
  do site publicado.
- Após mudanças, verifique as páginas afetadas, CSS, favicon, links relativos,
  âncoras e troca de idioma. Use validação HTML/CSS quando pertinente.
- Para mudanças visuais ou de interação, confira também teclado, foco, contraste,
  telas pequenas e zoom. Diferencie inspeção de código de validação em navegador.
- Execute `git diff --check`.
  Informe verificações, resultados e limitações.
  Não adicione ferramentas ou testes que apenas repitam a implementação.
