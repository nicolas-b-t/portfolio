# Padrão de HTML

Norma de montagem da página principal em `pt-BR`.
O objetivo é a replicabilidade: conteúdo novo é copiado de um modelo em `docs/modelos/` e preenchido.
Não há etapa de build. A conferência da seção 8 substitui o build.

## 1. Escopo

- Vale para `static/pt-BR/index.html`.
- `en/` segue os fatos e a estrutura comum da base `pt-BR`; os modelos deste documento são exclusivos da página brasileira.
- A página de projetos, a galeria e as recomendações não fazem parte deste padrão.

## 2. Onde ficam os modelos

- `docs/modelos/` guarda os modelos.
- Nunca copie um modelo com `{{CAMPO}}` para `static/`. O site publicado não pode conter marcador.
- Um modelo não contém dado real, para não envelhecer.

## 3. Convenções dos modelos

| Convenção | Uso |
| --- | --- |
| `{{CAMPO}}` | Campo obrigatório. |
| Bloco comentado com `OPCIONAL` | Campo que só entra quando a fonte confirma. Apague o comentário ao usar. |
| `{{ITEM_1}}`, `{{ITEM_2}}` | Item repetível. |
| `<!-- ===== TELA ===== -->` | Início do bloco visível. |
| `<!-- ===== CÓPIA OCULTA ===== -->` | Início do espelho em `#dados-curriculo`. |
| `<!-- ===== IMPRESSÃO ===== -->` | Início do espelho de impressão. |

Mantenha a indentação de 2 espaços do HTML atual.

## 4. Blocos e campos

### 4.1 Documento

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| `{{LANG}}` | Sim | `pt-BR`. |
| `{{TITULO}}` | Sim | Nome e função, sem slogan. |
| `{{DESCRICAO}}` | Sim | Uma frase, repetida no `lead` do hero. |
| `{{URL_ESTA}}`, `{{URL_ALT}}` | Sim | Caminhos relativos dos `hreflang`. |

### 4.2 Cabeçalho

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Itens do menu | Sim | Sete itens, na ordem vigente. Não reordene sem decisão. |
| Links de idioma | Sim | `pt-BR` atual e `en`. |

### 4.3 Hero

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| `{{NOME}}` | Sim | `h1`, único na página. |
| `{{FRASE_SINTESE}}` | Sim | Mesma frase da `meta description`. |
| Botões | Sim | Projetos, contato, idioma e currículo. |

### 4.4 Perfil

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| `{{POSICIONAMENTO}}` | Sim | Uma frase, sem repetir empregos nem datas. |
| `{{VALORES}}` | Sim | Um parágrafo autoral. |
| Atalhos | Sim | Experiência, habilidades e formação. |

### 4.5 Competências

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| `{{CATEGORIA}}` | Sim | Uma das três: técnicas, sociais, práticas. |
| `{{SUBCATEGORIA}}` | Sim | Nome existente. Não crie sinônimo. |
| `{{TAG}}` | Sim | Uma competência por `li`. |
| `{{LANG}}` | Condicional | `lang="en"` quando a tag está em inglês. |
| `{{NOTA}}` | Não | Nível ou qualificador em `span.skill-note`. |
| `{{ANCORA}}` | Condicional | Quatro tags existentes, quando a subcategoria tem 9 ou mais tags. Não se repetem na lista expandida. |
| `details.skill-group` | Condicional | Fechado por padrão; `summary.skill-more` com `aria-label` próprio por subcategoria. |
| Limiar | Sim | Até 8 tags, lista aberta; 9 ou mais, quatro âncoras e o restante no `details`. |
| Ordem | Sim | Âncoras na ordem aprovada; demais tags em ordem alfabética dentro do `details`. |

### 4.6 SFIA

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| `{{CODIGO}}` | Sim | Quatro letras. |
| `{{NOME}}` | Sim | Nome da habilidade. |
| `{{NIVEL}}` | Sim | 1 a 7. |
| `{{RESPONSABILIDADE}}` | Sim | Auxilia, Aplica ou equivalente. |
| `{{EVIDENCIA}}` | Sim | Fato verificável na própria página. |

O bloco `details` e o espelho `.sfia-print` precisam ter o mesmo conteúdo.

### 4.7 Experiência

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| `{{CARGO}}` | Sim | Título aprovado, sem reescrever. |
| `{{ICONE}}` | Sim | Nome existente em `static/assets/icons/`. |
| `{{EMPRESA}}` | Sim | Nome oficial. |
| `{{URL_EMPRESA}}` | Não | `https`. Sem link, use `dd` sem `<a>`. |
| `{{VINCULO}}` | Não | Não registrar vínculo empregatício; o campo não é exibido. |
| `{{INICIO_ISO}}` | Sim | `AAAA-MM`, ou `AAAA-MM-DD` quando a fonte dá o dia. |
| `{{INICIO_TEXTO}}` | Sim | Mês por extenso. |
| `{{FIM}}` | Sim | `<time>` do fim ou a palavra `atual`. |
| `{{CIDADE}}`, `{{UF}}` | Não | Cidade e UF. O país é sempre Brasil. |
| `{{ATIVIDADE_n}}` | Sim, ao menos 1 | Frase completa. Presente na experiência atual; passado nas encerradas. |

Ordem das fichas: data de término decrescente. Experiência atual primeiro.

### 4.8 Formação

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| `{{INSTITUICAO}}` | Sim | Nome oficial. |
| `{{URL_INSTITUICAO}}` | Sim | `https`. |
| `{{CURSO}}` | Sim | Nome oficial do curso. |
| `{{INICIO}}`, `{{FIM_PREVISTO}}` | Sim | `<time>` com `AAAA-MM`. |
| `{{URL_PPC}}` | Sim | Projeto pedagógico. |
| `{{CONTEUDO_n}}` | Sim | Conteúdo previsto, nunca formação concluída. |

### 4.9 Cursos

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| `{{CURSO}}` | Sim | Título oficial. |
| `{{LANG}}` | Condicional | `lang="en"` no título estrangeiro. |
| `{{INSTITUICAO}}`, `{{URL_INSTITUICAO}}` | Sim | Nome e link oficiais. |
| `{{TIPO}}` | Sim | Conclusão de curso, Participação, Curso SENAI ou Formação introdutória. |
| `{{HORAS}}` | Sim | Inteiro. |
| `{{DATA_BR}}`, `{{DATA_ISO}}` | Sim | `DD/MM/AAAA` e `AAAA-MM-DD`. |
| `{{GRUPO}}`, `{{SUBCATEGORIA}}` | Sim | Nomes existentes. |

O bloco `.courses-screen` e o bloco `.courses-print` precisam ter o mesmo conteúdo.

### 4.10 Contato

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| `{{ICONE}}` | Sim | `mail`, `linkedin`, `github` ou `graduation-cap`. |
| `{{URL}}` | Sim | Destino. |
| `{{ROTULO}}` | Sim | Nome do canal. |
| `{{IDENTIFICADOR}}` | Sim | Endereço, nome ou identificador. |
| `{{HREFLANG}}` | Condicional | Quando o destino está em outro idioma. |

### 4.11 Rodapé

| Campo | Obrigatório | Regra |
| --- | --- | --- |
| Links | Sim | Galeria, agradecimentos à rede e seleção pessoal. |
| Ano | Sim | `span` com o ano corrente. |

### 4.12 Cópia oculta

- Reproduz os mesmos fatos da tela, na mesma ordem.
- Usa `h2` no topo e `h3` por seção.
- Não repete o cargo: o `h4` já o declara.
- Não usa marcador manual dentro de `li`.
- Fica dentro de `<section id="dados-curriculo" hidden>`.

## 5. Invariantes

1. Um `h1` por página.
2. `h2` por seção, `h3` por item, `h4` subcategoria, `h5` e `h6` só dentro de cursos.
3. IDs fixos: `#dados-curriculo`, `#main`, `#sobre`, `#habilidades`, `#experiencia`, `#formacao`, `#contato`.
4. Data sempre em `<time datetime>`.
5. Uma competência por `li`, sem separador no texto.
6. `data-icon` só com nome existente.
7. Link externo em outro idioma recebe `hreflang`.
8. Proibido `<script>`, `<form>`, `<iframe>`, `style=` e atributo `on*`.
9. Classe nova exige regra no CSS comum ou registro como gancho semântico.
10. Nenhum marcador `{{` no site publicado.

## 6. Espelhos

| Origem | Espelho | Regra |
| --- | --- | --- |
| `#experiencia` | cópia oculta | Mesmos fatos e ordem. |
| `.courses-screen` | `.courses-print` | Mesmo conteúdo, mesma contagem. |
| `.sfia-profile` | `.sfia-print` | Mesmo conteúdo, mesma contagem. |
| `.skill-anchors` + `.skill-group` | cópia oculta | Mesmas tags, sem repetir âncoras; a cópia oculta mantém a lista completa. |
| Tela | cópia oculta | Nenhum fato exclusivo de um lado. |

## 7. Ordem

- Menu: ordem vigente, sem reordenação.
- Experiências: término decrescente; experiência atual primeiro.
- Competências: âncoras primeiro, na ordem aprovada; demais tags alfabéticas.
- Cursos: data decrescente dentro da subcategoria.

## 8. Conferência

Execute antes de publicar:

```powershell
# nenhum marcador restante
Select-String -Path static\pt-BR\*.html -Pattern '\{\{'

# espaços e conflitos
git diff --check

# um h1
(Select-String -Path static\pt-BR\index.html -Pattern '<h1').Count

# contagem de cursos na tela e na impressão
(Select-String -Path static\pt-BR\index.html -Pattern 'course-list').Count

# competências: um controle por subcategoria colapsada
(Select-String -Path static\pt-BR\index.html -Pattern 'skill-more').Count
```

Confira também, no navegador:

- âncoras internas resolvem;
- ícones carregam;
- impressão mostra as cinco experiências e oculta a cópia estruturada;
- cada `[ver mais]` abre pelo teclado e anuncia a subcategoria;
- impressão mostra as âncoras e as listas abertas e omite as colapsadas;
- 320 CSS px sem rolagem horizontal;
- zoom de 200% sem corte;
- temas claro e escuro;
- teclado e foco visível.

## 9. Fluxo para adicionar conteúdo

1. Escolha o modelo em `docs/modelos/`.
2. Copie para a seção e preencha os campos.
3. Apague os blocos opcionais sem fonte confirmada.
4. Espelhe na cópia oculta.
5. Se for curso ou SFIA, espelhe na impressão.
6. Rode a conferência da seção 8.
7. Registre no `CHANGELOG.md`.

## 10. Limites

- O modelo é copiado à mão; não há geração automática.
- O padrão não valida fatos. Fonte e atribuição continuam em [Conteúdo e fontes](conteudo-e-fontes.md).
- Os modelos não cobrem a redação de `en/`; a versão inglesa segue as regras de idioma de [Manutenção](manutencao.md).
- A declaração de conformidade com norma continua fora de escopo.
