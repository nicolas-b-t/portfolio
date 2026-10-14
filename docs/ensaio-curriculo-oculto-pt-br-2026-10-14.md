# Ensaio de dados ocultos no currículo pt-BR

Data: 14 de outubro de 2026.

O responsável autorizou alterações somente na página pt-BR.
Ele condicionou commit e push a resultados positivos nos parsers.
O primeiro ensaio foi negativo e impediu a publicação daquela versão.
O refinamento posterior atingiu o critério de experiência e formação na leitura dedicada do bloco pelo cvats.
As condições e os limites desse resultado estão na seção final.

## Alterações locais

- Foi incluído o botão desabilitado “Baixar currículo”, junto aos dois botões existentes no início da página.
- Os nomes atuais das tecnologias foram preservados.
- Uma seção com o atributo HTML nativo `hidden` foi incluída como primeiro elemento do `body`.
- A seção reúne nome, contatos, resumo, habilidades, experiências, formação, cursos, TOEIC e projetos.
- Os títulos passaram a identificar experiência profissional, formação acadêmica e conteúdos previstos da graduação.
- As experiências passaram a separar cargo, empresa e período, quando declarado.
- A exportação TXT não foi alterada.

O bloco conserva 161 ocorrências de tags, com 145 rótulos distintos.
Ele preserva atribuições pessoais, atividades da equipe, aprendizagem, apoio e conteúdos acadêmicos previstos.
As datas desconhecidas da RealFort continuam ausentes. A conclusão da graduação permanece prevista para julho de 2027.

A cópia oculta reúne os 17 cursos uma vez.
As duas cópias originais permanecem no conteúdo principal.
O DOM completo contém 51 ocorrências de cursos e 322 ocorrências de tags.
Incluir dados ocultos não elimina as duplicações existentes.

## Execução dos parsers

Foram executadas as mesmas rotinas textuais de dois parsers públicos usadas no ensaio anterior.
O [manifesto](referencias/ats/manifesto-parser-publico-2026-10-13.json) registra fontes, commits, licenças e condições de execução.

O primeiro módulo foi executado sem alterações.
No segundo, somente dois imports não utilizados foram omitidos em memória.
O Node.js retirou os tipos TypeScript. Nenhuma regra de extração foi alterada.

O texto foi obtido por percurso do `body`, na ordem do DOM.
Elementos de bloco foram separados por quebras de linha. Os textos inline foram preservados.
Uma variante incluiu todo o DOM. Outra retirou as subárvores com o atributo `hidden`.
Essa segunda variante representa uma estratégia de extração construída por código, sem teste de navegador.
O bloco oculto também foi testado isoladamente para localizar a origem dos erros.

| Entrada após as alterações | Primeiro parser | Segundo parser |
| --- | --- | --- |
| DOM completo | Nome e e-mail corretos. Nenhuma habilidade, experiência ou graduação recuperada | Nome, e-mail e perfis corretos. Doze habilidades, incluindo o falso positivo C. Nenhuma experiência ou graduação recuperada |
| DOM sem elementos `hidden` | Nome incorreto. E-mail correto. Nenhuma habilidade, experiência ou graduação recuperada | Nome e perfis não recuperados corretamente. Doze habilidades, incluindo C. Nenhuma experiência ou graduação recuperada |
| Somente bloco oculto | Nome e e-mail corretos. Nenhuma habilidade, experiência ou graduação recuperada | Nome, e-mail e perfis corretos. Onze habilidades, sem C. Nenhuma experiência ou graduação recuperada |

Os dois controles em inglês recuperaram os campos esperados.
Eles confirmam a execução das rotinas, sem demonstrar cobertura do português.

O segundo parser usa termos ingleses para reconhecer cargos e graus acadêmicos.
O primeiro usa cabeçalhos ingleses para localizar seções.
A hierarquia HTML desaparece quando essas rotinas recebem somente o texto extraído.
O conteúdo invisível não alterou essas regras.

O falso positivo C continua na leitura do DOM completo, que contém “Código deste portfólio”.
Os perfis melhoraram somente na entrada que manteve as URLs pessoais do bloco oculto antes dos links de projetos.
As rotinas não oferecem campos suficientes para verificar todas as atribuições e limitações profissionais.

## Critérios e integridade

O critério mínimo exigiu nome e e-mail corretos, três pares cargo/empresa, graduação na Fatec e ausência de C não declarado.
Os perfis foram conferidos quando o parser oferecia esses campos.
Os casos posteriores falharam nesse critério. Por isso, a condição de publicação não foi atendida.
Datas, conclusão prevista e contexto das tags não foram aprovados por inferência após a perda dos campos principais.

A inspeção de código confirmou os mesmos rótulos e observações nas cópias principal e oculta.
Os dados dos cursos correspondem às cópias originais.
UTF-8, idioma pt-BR, identificadores únicos, links locais e ausência de JavaScript foram conferidos.
O botão não tem ação e está desabilitado.
O SHA-256 da exportação TXT permaneceu igual.

Não houve ensaio de tela, teclado, impressão, PDF ou DOCX.
Nenhum currículo foi enviado a serviço externo. Nenhum ATS proprietário foi executado.
As entradas completas, saídas, controles, hashes e verificações estão no [registro JSON](verificacao-curriculo-oculto-pt-br-2026-10-14.json).

## O que falta para avançar

1. Teste um parser que reconheça português ou adapte uma rotina pública de manutenção para esse idioma.
2. Verifique a recuperação de cargos, empresas, períodos, graduação em andamento e conclusão prevista.
3. Corrija a associação de C sem adicionar ou remover competências declaradas.
4. Defina uma entrada que preserve os dados necessários quando o conteúdo oculto for descartado.
5. Repita a comparação com as saídas anteriores antes de decidir sobre commit e push.

Dados ocultos podem facilitar leitores do código-fonte, mas não garantem interpretação correta em qualquer sistema.
Alterar um parser local também não comprova compatibilidade com sistemas proprietários.
O trabalho aguardou a nova solicitação do responsável, que autorizou planejamento e testes adicionais.

## Reteste de experiências, formação, cursos e projetos

O responsável solicitou conferir esses conteúdos e repetir os testes.
As informações já estavam no bloco oculto. A página e a exportação foram preservadas nesta etapa.

O leitor estrutural local comparou os dados ocultos com a página principal.
Ele recuperou três experiências, uma graduação, 17 cursos, um resultado TOEIC e três projetos.
Os cargos, empresas, datas, instituições, cargas horárias declaradas, qualificações e atribuições corresponderam ao conteúdo principal.
Os 21 conteúdos acadêmicos permaneceram identificados como previstos.
Essa leitura conhece a hierarquia HTML do projeto. Ela não representa um ATS proprietário.

As rotinas públicas foram novamente executadas com o DOM completo, com o bloco isolado e com entradas por seção.
Também foi repetida a variante que exclui elementos `hidden`.
As três entradas anteriormente testadas produziram os mesmos hashes e as mesmas saídas.

| Conteúdo | Conferência estrutural local | Parsers públicos originais |
| --- | --- | --- |
| Experiências | Três cargos, empresas, atividades e períodos declarados recuperados | Nenhuma experiência recuperada, inclusive no teste isolado |
| Graduação | Fatec, curso, formação em andamento e conclusão prevista recuperados | Graduação não recuperada, inclusive no teste isolado |
| Cursos | Dezessete títulos, instituições, qualificações, datas e cargas horárias declaradas recuperados | Saídas sem campo próprio para cursos. O segundo reconheceu apenas Cisco Networking Academy como instituição |
| TOEIC | Resultado de 910 pontos, componentes, instituição, data e validade preservados | Saídas sem campo próprio para resultado TOEIC |
| Projetos | Três projetos com descrições, grupos de tags e atribuições recuperados | Saídas sem campo próprio para projetos. A recuperação lexical de tecnologias não recuperou as participações |

Os controles ingleses recuperaram os campos esperados.
Os controles portugueses falharam na associação de cargo, empresa e instituição.
Os controles são sintéticos. Eles não acrescentam informações ao currículo.

No teste isolado dos projetos, o segundo parser recuperou JavaScript a partir da declaração “sem JavaScript”.
Controles adicionais confirmaram a recuperação dessa tecnologia mesmo quando seu uso era negado.
Os casos preliminares também mostraram interferência do ponto final após um nome de tecnologia.
As entradas posteriores controlaram essa pontuação. Todas as saídas foram preservadas.

O reteste dos dois parsers anteriores permaneceu negativo. Naquela etapa, não houve commit ou push.
Os [resultados do reteste](reteste-conteudos-ocultos-pt-br-2026-10-14.json) registram dados estruturais, comparações, entradas, saídas e controles.
Os resultados demonstram presença e integridade dos conteúdos, com falhas de interpretação nas rotinas públicas testadas.

## Planejamento e resultado positivo no cvats

O responsável definiu sucesso como recuperação de experiência e formação.
O plano fixou os fatos esperados, pesquisou uma opção pública, refinou a entrada e verificou controles de erro.
As falhas anteriores foram preservadas.

Foi recebido o clone completo do [cvats](https://github.com/rntxbr/cvats-app), no commit bd53d0e9eb3489e975a1724270cf83a9a692c7bd.
O projeto inclui reconhecimento de cabeçalhos, cargos e formação em português.
Sua lista de cargos não inclui os termos Técnico e Auxiliar presentes neste currículo.
As [fontes e a licença AGPL-3.0](referencias/ats/manifesto-cvats-2026-10-14.json) foram preservadas no acervo local ignorado pelo Git.

O ensaio executou groupLinesIntoSections, extractWorkExperience e extractEducation originais.
Somente os aliases de módulos foram resolvidos e os tipos TypeScript foram retirados pelo Node.js.
Nenhuma regra de extração foi alterada.

As entradas foram linhas derivadas dos elementos do HTML.
Títulos e strong forneceram ênfase semântica. A API recebeu posições lógicas uniformes exigidas pelo seu esquema.
Essas posições são sintéticas. Elas não representam medidas de navegador ou PDF.
A aplicação completa, o leitor PDF e o frontend não foram executados.

### Refinamentos do bloco

- Cargo, empresa, vínculo, período e local passaram a ter limites distintos.
- Os cargos receberam aliases ingleses reconhecidos pelo parser. Os títulos originais permanecem nas atividades e no conteúdo principal.
- As atividades passaram a usar itens de lista.
- A graduação passou a formar um registro único com curso, instituição, início, conclusão prevista e situação.
- Conteúdos previstos e cursos complementares foram separados da graduação por cabeçalhos reconhecíveis.

| Cargo original preservado | Alias inglês do bloco oculto |
| --- | --- |
| Auxiliar de instalação de fibra óptica | Fiber Optic Installation Assistant |
| Técnico de suporte Help Desk | Help Desk Support Technician |
| Técnico de suporte de TI | IT Support Technician |

Essas traduções não acrescentam qualificações.
Aprendizagem na fusão, apoio com OTDR e vivência orientada em altura permanecem nas atividades.
O conteúdo principal foi preservado byte a byte durante esse refinamento.
As 161 tags, os 17 cursos, os projetos e a exportação TXT também foram preservados.

### Resultado observado

| Registro | Campos recuperados no cvats |
| --- | --- |
| RealFort Sistemas | Alias do cargo, título original nas atividades e empresa correta. Período permanece vazio |
| Lukos Tecnologia | Cargo, empresa e período de setembro a dezembro de 2025 |
| Instituto Alpha de Saúde Integral | Cargo, empresa e período de abril de 2023 a junho de 2024 |
| Graduação | Curso superior de tecnologia em Gestão da Tecnologia da Informação e Fatec Franco da Rocha – Giuliano Cecchettini |
| Situação acadêmica | Início em julho de 2024, conclusão prevista para julho de 2027 e formação em andamento |

O resultado do bloco oculto foi positivo para esses campos.
O teste comparou o alias recuperado, o cargo original retornado nas atividades, a empresa e os períodos declarados.
A verificação não aceitou datas inventadas nem substituição da graduação por uma instituição de curso complementar.

Os quatro controles seguintes passaram:

1. Remover uma experiência reduziu a saída para duas experiências.
2. Trocar uma empresa fez o parser retornar o nome de controle.
3. Trocar a instituição fez o parser retornar a instituição de controle.
4. Remover a graduação deixou a saída acadêmica vazia.

Os controles modificaram somente entradas em memória. Eles não alteraram a página.
Os [resultados completos](verificacao-cvats-pt-br-2026-10-14.json) preservam as iterações, entradas, saídas, hashes e controles.

### Limites do positivo

O positivo depende da leitura dedicada do bloco oculto.
A leitura do DOM completo mistura as cópias e continua com registros incorretos.
A entrada que exclui hidden também continua negativa.
O primeiro parser anterior, mesmo com normalização local da entrada, continuou falhando nas experiências.

Esse resultado confirma as rotinas textuais do cvats nas condições registradas.
Ele não demonstra interpretação universal, leitura de PDF ou reconhecimento por um ATS proprietário.
Não houve teste de tela, teclado ou impressão. Nenhum currículo foi enviado a serviço externo.
