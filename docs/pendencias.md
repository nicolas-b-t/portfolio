# Pendências do projeto

Atualizado em 9 de outubro de 2026.

## Autenticação independente para Optigrow e SGCS

**Estado: pendente de escolha e autorização do responsável.**

Lembrete para Nicolas: configurar posteriormente uma autenticação GitHub
independente do conector para baixar e analisar estes repositórios privados:

- Optigrow: https://github.com/RodrigoNKC/optigrow.
- SGCS: https://github.com/SGCS-Gestao-de-Chamados-Para-Sindicos/SGCS-espelho.

O login independente ainda não foi iniciado; a investigação solicitada limitou-se
à documentação e à ajuda da CLI, sem modificar credenciais ou configurações.

### O que já verificamos

- A autenticação atual identifica `nicolas-b-t` e consegue ler o portfólio.
- Os dois clones privados retornaram HTTP 403 e a API retornou HTTP 404.
- Os projetos não aparecem na lista de repositórios autorizados à instalação
  visível de `chatgpt-codex-connector` na conta `nicolas-b-t`.
- Os sites publicados funcionam e já estão ligados às cinco versões do portfólio.
- Código, arquitetura e participação individual ainda não foram analisados.

### Checklist para retomar

- [ ] Confirmar o acesso pessoal aos dois repositórios e a condição de membro
  ou colaborador externo na organização do SGCS.
- [ ] Escolher uma forma de autenticação compatível com esses acessos e políticas.
- [ ] Autorizar explicitamente a configuração antes de iniciar um novo login.
- [ ] Fornecer eventual token pelo mecanismo seguro de segredos do ambiente,
  sem incluir valores na conversa, no código, no histórico do terminal ou no Git.
- [ ] Isolar a nova credencial da autenticação existente do portfólio e verificar
  sua compatibilidade com o proxy do ambiente.
- [ ] Testar leitura e baixar os projetos fora do checkout do portfólio,
  sem executar automaticamente o código recebido ou enviar alterações.
- [ ] Analisar os projetos e confirmar a contribuição de Nicolas antes de
  acrescentar tecnologias, responsabilidades ou resultados ao currículo.
- [ ] Revogar a autorização temporária e remover credenciais locais ao terminar.

### Alternativas documentadas

- **GitHub CLI:** permite autorizar no navegador por código, sem compartilhar
  a senha; verificar expiração ou revogar a autorização após o uso.
- **PAT clássico:** pode atender ao acesso como colaborador, mas o escopo `repo`
  é amplo e inclui escrita; definir expiração e respeitar políticas organizacionais.
- **PAT granular:** pode limitar leitura a repositórios selecionados de um
  proprietário, mas atualmente não suporta acesso como colaborador externo;
  no SGCS a viabilidade depende da condição de membro e da aprovação da organização.
- **Deploy key SSH:** é somente leitura por padrão e exige uma chave por
  repositório, cadastrada por quem administra suas configurações; não expira
  automaticamente e o funcionamento SSH neste ambiente não foi testado.
- **Arquivo ZIP:** permite analisar o código fornecido manualmente sem iniciar
  uma autenticação independente neste ambiente.

`GH_TOKEN` tem prioridade sobre `GITHUB_TOKEN` na GitHub CLI, mas `git clone`
não utiliza essas variáveis automaticamente; a ligação entre Git e a credencial
precisaria ser configurada e validada quando esta pendência for retomada.

### Referências oficiais

- [Tokens pessoais do GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).
- [Login pela GitHub CLI](https://cli.github.com/manual/gh_auth_login).
- [GitHub CLI como auxiliar de credenciais do Git](https://cli.github.com/manual/gh_auth_setup-git).
- [Chaves de deploy](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/managing-deploy-keys).

Consultar novamente essas referências ao retomar, pois as opções e limitações
do GitHub podem mudar.
