# Recuperar referências locais após clonar

A documentação e as cópias versionadas acompanham o clone do repositório.
Seis PDFs permanecem locais e são excluídos pelo `.gitignore`.
Cinco contêm restrições explícitas de reprodução.
O PPC recebido contém CPFs de terceiros.
Preservamos todos os originais no ambiente, sem edição.

## Obter os documentos oficiais

1. Abra a página oficial indicada na tabela.
2. Confira a edição e as condições de uso.
3. Obtenha uma cópia para consulta conforme essas condições.
4. Salve o documento no caminho indicado.
5. Compare seu tamanho e SHA-256 com o manifesto correspondente.
6. Se o conteúdo mudar, registre a diferença antes de substituir a referência.

| Arquivo local | Fonte oficial | Manifesto |
| --- | --- | --- |
| `referencias/asd-ste100/ASD-STE100-issue-9-2025-01-15.pdf` | https://www.asd-ste100.org/STE_downloads.html | [ASD-STE100](referencias/asd-ste100/manifesto.json) |
| `referencias/idiomas/otan/STANAG-6001-edicao-5.pdf` | https://nato-bilc.org/stanag-6001/ | [OTAN](referencias/idiomas/otan/manifesto.json) |
| `referencias/idiomas/otan/ATrainP-5-edicao-A-versao-2-en.pdf` | https://nato-bilc.org/stanag-6001/ | [OTAN](referencias/idiomas/otan/manifesto.json) |
| `referencias/idiomas/otan/ATrainP-5-edicao-A-versao-2-fr.pdf` | https://nato-bilc.org/stanag-6001/ | [OTAN](referencias/idiomas/otan/manifesto.json) |
| `referencias/idiomas/qecr-cefr/CEFR-volume-complementar-2020-en.pdf` | https://www.coe.int/en/web/common-european-framework-reference-languages/the-cefr-descriptors | [QECR](referencias/idiomas/qecr-cefr/manifesto.json) |

Os caminhos da tabela são relativos a `docs/`.
Os manifestos também registram os endereços diretos consultados anteriormente.
Links oficiais podem mudar e não garantem disponibilidade permanente.
Um hash igual demonstra igualdade com a cópia registrada, sem constituir assinatura do autor.
Não publique novamente os PDFs restritos sem autorização aplicável.

## Recuperar o PPC

Solicite ao responsável uma cópia autorizada do PPC de Gestão da Tecnologia da Informação.
Guarde a cópia recebida em `docs/fontes/academico/PPC_GTI.pdf`, somente localmente.
Compare o hash com o [manifesto acadêmico](fontes/academico/manifesto.json).
O arquivo original recebido não acompanha o clone porque contém identificadores pessoais de terceiros.
A síntese das competências e as páginas consultadas estão no [índice acadêmico](fontes/academico/README.md).

## Verificar a cópia

Execute na raiz do repositório, ajustando o caminho do documento:

```sh
sha256sum docs/referencias/idiomas/otan/ATrainP-5-edicao-A-versao-2-en.pdf
```

Compare o resultado com o campo `sha256` do manifesto.
Em sistemas sem `sha256sum`, use uma ferramenta equivalente que calcule SHA-256.
O site pode funcionar sem esses PDFs.
A consulta aos descritores completos exige recuperar as referências correspondentes.
