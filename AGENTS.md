# Orientações do projeto

Estas instruções se aplicam ao repositório inteiro e orientam pessoas e agentes
que trabalhem no portfólio.

## Objetivos

Priorize robustez, compatibilidade, acessibilidade, portabilidade e minimalismo.
Use o mínimo de tecnologias e dependências necessário para atender ao conteúdo.

## Regra: site sem JavaScript

- O portfólio deve funcionar integralmente com HTML e CSS, sem JavaScript.
- Não adicione scripts próprios ou externos, elementos `script`, atributos de
  eventos como `onclick`, URLs `javascript:`, frameworks ou componentes que
  dependam de JavaScript.
- Não adicione rastreadores, widgets ou embeds que executem JavaScript.
- Use elementos HTML nativos e CSS para navegação e apresentação. Se um recurso
  exigir JavaScript, explique a limitação e proponha uma alternativa sem scripts.
  Não altere esta regra sem uma decisão explícita do responsável pelo projeto.
- Esta regra se refere ao site entregue ao visitante. Ferramentas de manutenção
  externas ao site não devem introduzir scripts no conteúdo publicado nem novas
  dependências sem necessidade demonstrada.
- Documentos oficiais de terceiros em `docs/referencias/` são referências,
  não páginas do portfólio. Preserve suas cópias e avisos de licença intactos,
  inclusive scripts presentes nos documentos originais. Não os incorpore ao site.

## HTML, CSS e compatibilidade

- Siga o HTML Living Standard da WHATWG. Prefira elementos semânticos e recursos
  nativos; use ARIA apenas quando a semântica HTML não for suficiente.
- Mantenha UTF-8, títulos descritivos, uma hierarquia coerente de títulos e o
  atributo `lang` correto em cada página.
- Prefira recursos CSS amplamente suportados, usando Baseline Widely Available
  como referência. Para recursos de suporte limitado, forneça uma alternativa.
- Use layouts fluidos que suportem telas pequenas, zoom e textos longos.
- Preserve foco visível, respeite `prefers-reduced-motion` e confira temas claro
  e escuro e a impressão do currículo.
- Use fontes do sistema e recursos locais. Evite serviços externos para funções
  básicas, bibliotecas de ícones e dependências puramente decorativas.
- Prefira código legível, seletores simples e nomes descritivos. Respeite a
  formatação existente e evite abstrações sem benefício concreto.

## Acessibilidade

- Use WCAG 2.2 nível AA como alvo. As referências estão em
  `docs/referencias/w3c/`; diferencie recomendações publicadas de rascunhos.
- Garanta navegação por teclado, link para pular ao conteúdo, ordem lógica de
  foco e nomes compreensíveis para links e controles.
- Confira contraste de texto e controles, alternativas textuais quando
  necessárias e conteúdo que se reorganize sem perda de informação.
- Evite links vazios ou de exemplo na versão destinada à publicação.
- Não declare conformidade apenas com base em verificações automáticas.

## Idiomas, estrutura e portabilidade

- Mantenha as versões em português brasileiro (`pt-BR`) e inglês (`en`), com
  `lang`, `hreflang` e links de troca de idioma corretos.
- A pasta `static/` é a única fonte do site publicado. `static/index.html`
  permite escolher o idioma; `static/pt-BR/` e `static/en/` contêm as páginas.
- Revise o impacto de alterações nas duas traduções. Enquanto houver CSS e
  recursos duplicados por idioma, mantenha-os consistentes. Prefira recursos
  compartilhados quando uma reorganização da estrutura estiver no escopo.
- Use caminhos relativos para recursos e páginas internas, de modo que o site
  possa ser servido em diferentes hospedagens e subdiretórios.
- Preserve o funcionamento como arquivos estáticos, sem exigir backend,
  framework, gerenciador de pacotes ou etapa de build.
- Não inclua credenciais ou configurações específicas de uma máquina no site.

## Verificação e trabalho no repositório

- Leia estas instruções e confira `git status --short` antes de editar. Preserve
  mudanças existentes e não sobrescreva arquivos do usuário sem necessidade.
- Use o checkout existente. Cada tarefa cloud já é isolada; não crie worktrees
  sem pedido explícito do usuário.
- Para verificar `static/`, execute na raiz:
  `python3 -m http.server 8001 --bind 127.0.0.1 --directory static`.
  A escolha de idioma está em `/`, e as páginas em `/pt-BR/` e `/en/`;
  use outra porta se estiver ocupada.
  O servidor Python é uma ferramenta de desenvolvimento, não uma dependência
  do site publicado.
- Após mudanças, verifique as páginas afetadas, CSS, favicon, links relativos,
  âncoras e troca de idioma. Use validação HTML/CSS quando pertinente.
- Para mudanças visuais ou de interação, confira também teclado, foco, contraste,
  telas pequenas e zoom. Diferencie inspeção de código de validação em navegador.
- Execute `git diff --check` e informe o que foi verificado, os resultados e
  limitações. Não adicione ferramentas ou testes que apenas repitam a implementação.
