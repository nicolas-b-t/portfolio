"""Gera os dois currículos gerais V5 em DOCX a partir da página pt-BR."""

from __future__ import annotations

import re
from pathlib import Path

from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.shared import Cm, Pt, RGBColor
from lxml import html


ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
INDEX = html.parse(str(ROOT / "static/pt-BR/index.html"))
PROJECT_PAGE = html.parse(str(ROOT / "static/pt-BR/projetos.html"))
BLACK = RGBColor(0, 0, 0)

CONTACTS = [
    ("Telefone", "+55 11 95057-1593", "tel:+5511950571593"),
    ("E-mail", "beraldesnicolas@gmail.com", "mailto:beraldesnicolas@gmail.com"),
    ("Portfólio", "nicolas-b-t.github.io/portfolio", "https://nicolas-b-t.github.io/portfolio/"),
    ("LinkedIn", "linkedin.com/in/nicolas-t-a1ab74321", "https://www.linkedin.com/in/nicolas-t-a1ab74321/"),
    ("GitHub", "github.com/nicolas-b-t", "https://github.com/nicolas-b-t"),
    ("Lattes", "lattes.cnpq.br/1293729943180703", "https://lattes.cnpq.br/1293729943180703"),
]

EXPERIENCE_SUMMARIES = {
    "Gestor de tráfego pago": (
        "Criei e gerencio o site e os canais no Mercado Livre e na Shopee. Organizei o "
        "acervo documental e backups, removi sites obsoletos e cópias com uso indevido "
        "da marca, treinei os sócios em ferramentas da Meta e presto suporte de TI sob "
        "demanda. Também planejo e otimizo campanhas no Google Ads e Meta Ads, com "
        "medição no Google Tag Manager e análise no GA4."
    ),
    "Auxiliar de instalação de fibra óptica": (
        "Instalei e mantive redes FTTH e rádio; lancei cabos drop, fiz conectorização SC/APC, "
        "montei conectores RJ45 e configurei ONU, ONT e roteadores. Diagnostiquei falhas com power meter, "
        "OTDR e VFL. Realizei fusão de fibra como aprendiz."
    ),
    "Técnico de suporte Help Desk": (
        "Prestei suporte N1 a ERP e PDV, configurei sistemas, diagnostiquei falhas por "
        "acesso remoto e orientei clientes. Encaminhei chamados e analisei NF-e e NFC-e."
    ),
    "Técnico de suporte de TI": (
        "Prestei suporte N1/N2 em sistemas hospitalares, fiz manutenção de computadores "
        "e impressoras, fiz a gestão de ativos de TI, administrei o Microsoft Active Directory e "
        "produzi documentação técnica e procedimentos."
    ),
    "Assistente de E-commerce": (
        "Gerenciei catálogo e anúncios, atendi clientes B2C e B2B, prospectei leads e "
        "elaborei orçamentos. Acompanhei pedidos e a conferência pré-expedição com o "
        "Bling ERP e conduzi tratativas com o Mercado Livre."
    ),
}

PROJECTS = [
    (
        "Portfólio pessoal",
        "Site pessoal em HTML e CSS, com design responsivo, recursos de acessibilidade e "
        "publicação por GitHub Actions e GitHub Pages.",
        "https://nicolas-b-t.github.io/portfolio/",
    ),
    (
        "Optigrow",
        "Projeto colaborativo com Rodrigo Nascimento: ferramenta de marketing e tecnologia "
        "para óticas da região do Porto, em Portugal.",
        "https://optigrow.vercel.app/",
    ),
    (
        "SGCS — Sistema de Gestão de Chamados para Síndicos",
        "Pesquisa acadêmica e SaaS em desenvolvimento pela equipe. Gerencio o projeto, "
        "coordeno prazos e entregáveis e integro as ferramentas de trabalho.",
        "https://sgcs-seven.vercel.app/",
    ),
]

SFIA = [
    ("USUP", "Gestão de incidentes", 3),
    ("ASUP", "Suporte a aplicações", 3),
    ("NTAS", "Suporte a redes", 2),
    ("HSIN", "Instalação e remoção de sistemas", 2),
    ("ITOP", "Operações de infraestrutura", 2),
    ("PROG", "Programação e desenvolvimento de software", 2),
    ("CHMG", "Controle de mudanças", 2),
]

TECHNICAL_SKILLS = [
    ("Gestão de projetos", "Metodologias ágeis, Scrum, metas, coordenação e entregáveis."),
    ("Desenvolvimento com IA", "Agentes de IA, Codex (OpenAI), Claude Code e OpenCode em desenvolvimento e operações."),
    ("Desenvolvimento de software", "Especificações, prototipação e produto mínimo viável (MVP)."),
    ("Suporte de TI", "ERP (N1), hospitais (N1/N2), gestão de ativos de TI, incidentes e documentação técnica."),
    ("Redes", "FTTH, LAN, OTDR e configuração de roteadores."),
    ("Ferramentas Microsoft", "Microsoft Word, Microsoft Teams e Microsoft 365."),
]
SOCIAL_SKILLS = [
    ("Organização e desenvolvimento", "Autonomia, pensamento analítico e resolução de problemas."),
]
PRACTICAL_SKILLS = [
    ("Campo e ferramentas", "Trabalho em altura."),
    ("Condução", "CNH AB."),
]


def clean(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def text(node) -> str:
    return clean(node.text_content())


def source_experiences() -> list[dict[str, str]]:
    items = INDEX.xpath('//main/section[@id="experiencia"]/ol/li')
    assert len(items) == 5, "A página deixou de conter cinco experiências"
    result = []
    for item in items:
        role = text(item.xpath('./h3')[0])
        nodes = item.xpath('./dl/*')
        info = {text(nodes[i]): text(nodes[i + 1]) for i in range(0, len(nodes), 2)}
        assert role in EXPERIENCE_SUMMARIES, role
        result.append({"role": role, "company": info["Empresa"],
                       "period": info["Período"], "place": info["Local"],
                       "summary": EXPERIENCE_SUMMARIES[role]})
    return result


def source_courses() -> list[tuple[str, str, str, str]]:
    root = INDEX.xpath('//main//details[contains(@class,"courses-screen")]')[0]
    courses = []
    category = ""
    for item in root.xpath('.//h5[contains(@class,"skill-subheading")] | .//ul[contains(@class,"course-list")]/li'):
        if item.tag == "h5":
            category = text(item)
            continue
        title = text(item.xpath('./h6')[0])
        metadata = text(item.xpath('./p')[1])
        match = re.search(r"(\d+)\s*h", metadata)
        date = text(item.xpath('.//time')[0])
        assert match and re.fullmatch(r"\d{2}/\d{2}/\d{4}", date), title
        assert category
        courses.append((category, title, match.group(1), date))
    assert len(courses) == 18, f"A página contém {len(courses)} cursos, não 18"
    assert len({title for _, title, _, _ in courses}) == 18
    return courses


def validate_sources() -> None:
    projects = [text(n) for n in PROJECT_PAGE.xpath('//main//section[@id="projetos"]//article/h3')]
    assert len(projects) == 4, projects
    assert all(("Este portfólio" if name == "Portfólio pessoal" else name) in projects
               for name, _, _ in PROJECTS), projects
    categories = {text(n) for n in INDEX.xpath('//main//section[@id="habilidades"]//h4[contains(@class,"skill-subheading")]')}
    assert all(name in categories for name, _ in TECHNICAL_SKILLS + SOCIAL_SKILLS + PRACTICAL_SKILLS)
    assert len(SFIA) == 7


def set_style(style, size: float, *, bold=False, before=0, after=0,
              line=1.08, keep=False) -> None:
    style.font.name = "Arial"
    style.font.size = Pt(size)
    style.font.bold = bold
    style.font.color.rgb = BLACK
    style.paragraph_format.space_before = Pt(before)
    style.paragraph_format.space_after = Pt(after)
    style.paragraph_format.line_spacing = line
    style.paragraph_format.keep_with_next = keep
    style.paragraph_format.widow_control = True
    rpr = style.element.get_or_add_rPr()
    lang = rpr.find(qn("w:lang"))
    if lang is None:
        lang = OxmlElement("w:lang")
        rpr.append(lang)
    lang.set(qn("w:val"), "pt-BR")


def setup(doc: Document, sidebar=False) -> None:
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21), Cm(29.7)
    sec.top_margin = Cm(1.35)
    sec.bottom_margin = Cm(1.3)
    sec.left_margin = Cm(1.5)
    sec.right_margin = Cm(1.5)
    styles = doc.styles
    set_style(styles["Normal"], 9.5 if sidebar else 10,
              after=2.5 if sidebar else 2.8, line=1.07)
    set_style(styles["Title"], 19 if sidebar else 20, bold=True, after=5, line=1)
    ppr = styles["Title"].element.get_or_add_pPr()
    border = ppr.find(qn("w:pBdr"))
    if border is not None:
        ppr.remove(border)
    for name, size, bold, before, after, keep in [
        ("CV Section", 10.5 if sidebar else 11.1, True, 8, 3, True),
        ("CV Role", 9.65 if sidebar else 10.3, True, 5, 0.9, True),
        ("CV Meta", 8.7 if sidebar else 9.1, False, 0, 1.2, True),
        ("CV Small", 8.8 if sidebar else 9.2, False, 0, 2, False),
        ("CV Course", 8.9 if sidebar else 9.4, False, 0, 2.4, False),
        ("CV Course Group", 9 if sidebar else 9.6, True, 5, 1.5, True),
        ("CV Side Head", 9.1, True, 7, 2.3, True),
        ("CV Side", 8.8, False, 0, 3, False),
    ]:
        set_style(styles.add_style(name, 1), size, bold=bold, before=before,
                  after=after, keep=keep)


def add(container, value: str, style="Normal"):
    para = container.add_paragraph(style=style)
    para.add_run(value)
    return para


def link(paragraph, label: str, url: str) -> None:
    rid = paragraph.part.relate_to(url, RT.HYPERLINK, is_external=True)
    node = OxmlElement("w:hyperlink")
    node.set(qn("r:id"), rid)
    run = OxmlElement("w:r")
    props = OxmlElement("w:rPr")
    color = OxmlElement("w:color")
    color.set(qn("w:val"), "000000")
    props.append(color)
    underline = OxmlElement("w:u")
    underline.set(qn("w:val"), "single")
    props.append(underline)
    run.append(props)
    value = OxmlElement("w:t")
    value.text = label
    run.append(value)
    node.append(run)
    paragraph._p.append(node)


def heading(container, value, side=False):
    return add(container, value, "CV Side Head" if side else "CV Section")


def contacts(container, side=False) -> None:
    if side:
        heading(container, "Contato", True)
        for label, value, url in CONTACTS:
            para = container.add_paragraph(style="CV Side")
            para.add_run(label + "\n")
            link(para, value, url)
    else:
        for pair in (CONTACTS[:3], CONTACTS[3:]):
            para = container.add_paragraph(style="CV Small")
            for index, (label, value, url) in enumerate(pair):
                if index:
                    para.add_run("  |  ")
                para.add_run(label + ": ")
                link(para, value, url)


def experience(container, compact=False) -> None:
    heading(container, "Experiência profissional")
    for item in source_experiences():
        add(container, item["role"], "CV Role")
        add(container, f'{item["company"]}  |  {item["period"]}  |  {item["place"]}', "CV Meta")
        add(container, item["summary"], "CV Small" if compact else "Normal")


def education(container, side=False) -> None:
    heading(container, "Formação acadêmica" if not side else "Formação", side)
    add(container, "Curso superior de tecnologia em Gestão da Tecnologia da Informação, em andamento.",
        "CV Side" if side else "CV Small")
    para = container.add_paragraph(style="CV Side" if side else "CV Small")
    link(para, "Fatec Franco da Rocha – Giuliano Cecchettini",
         "https://fatecfrancodarocha.cps.sp.gov.br/gestao-da-tecnologia-da-informacao/")
    add(container, "Início: julho de 2024  |  Conclusão prevista: julho de 2027",
        "CV Side" if side else "CV Small")


def skills(container, side=False) -> None:
    heading(container, "Competências", side)
    for title, groups in [
        ("Competências técnicas", TECHNICAL_SKILLS),
        ("Competências sociais", SOCIAL_SKILLS),
        ("Habilidades práticas e operacionais", PRACTICAL_SKILLS),
    ]:
        add(container, title, "CV Course Group")
        for name, detail in groups:
            add(container, f"{name}: {detail}", "CV Side" if side else "CV Small")


def languages(container, side=False) -> None:
    heading(container, "Idiomas", side)
    add(container, "Inglês avançado - conversacional.", "CV Side" if side else "CV Small")
    add(container, "TOEIC Listening & Reading: 910/990 pontos.", "CV Side" if side else "CV Small")


def courses(container, compact=False) -> None:
    heading(container, "Cursos e certificados")
    previous = None
    for category, title, hours, date in source_courses():
        if category != previous:
            add(container, category, "CV Course Group")
            previous = category
        add(container, f"{title}  —  {hours} h", "CV Course")


def projects(container, compact=False) -> None:
    heading(container, "Projetos")
    for title, summary, url in PROJECTS:
        para = container.add_paragraph(style="CV Role")
        link(para, title, url)
        add(container, summary, "CV Small" if compact else "Normal")


def sfia(container, compact=False) -> None:
    heading(container, "Perfil SFIA 9")
    add(container, "Autoavaliação de responsabilidade; não representa certificação.", "CV Small")
    if compact:
        for code, label, level in SFIA:
            add(container, f"{code}: {label} (nível {level})", "CV Small")
    else:
        first = "; ".join(f"{code} {label} (nível {level})" for code, label, level in SFIA[:4])
        second = "; ".join(f"{code} {label} (nível {level})" for code, label, level in SFIA[4:])
        add(container, first + ".", "CV Small")
        add(container, second + ".", "CV Small")


def page_break(doc) -> None:
    para = doc.add_paragraph()
    para.add_run().add_break(WD_BREAK.PAGE)


def cell_padding(cell, top=100, start=120, bottom=100, end=120) -> None:
    tcpr = cell._tc.get_or_add_tcPr()
    margins = OxmlElement("w:tcMar")
    for edge, amount in [("top", top), ("start", start),
                         ("bottom", bottom), ("end", end)]:
        node = OxmlElement("w:" + edge)
        node.set(qn("w:w"), str(amount))
        node.set(qn("w:type"), "dxa")
        margins.append(node)
    tcpr.append(margins)


def columns(doc):
    table = doc.add_table(rows=1, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.columns[0].width, table.columns[1].width = Cm(5.2), Cm(12.8)
    left, right = table.rows[0].cells
    left.width, right.width = Cm(5.2), Cm(12.8)
    left.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.TOP
    right.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.TOP
    cell_padding(left, end=170)
    cell_padding(right, start=170)
    shading = OxmlElement("w:shd")
    shading.set(qn("w:fill"), "F2F2F2")
    left._tc.get_or_add_tcPr().append(shading)
    return left, right


def remove_empty_cell_start(cell) -> None:
    para = cell.paragraphs[0]
    if not para.text and len(cell.paragraphs) > 1:
        cell._tc.remove(para._p)


def build_standard() -> Path:
    doc = Document()
    setup(doc)
    add(doc, "Nicolas Beraldes Tarifa", "Title")
    contacts(doc)
    heading(doc, "Resumo profissional")
    add(doc, "Atuo em suporte de TI, redes e gestão de projetos. Desenvolvo este portfólio "
        "com agentes de IA e aplico ferramentas de IA em rotinas de desenvolvimento e "
        "operações. Tenho experiência adicional em comércio eletrônico e tráfego pago. "
        "Curso Gestão da Tecnologia da Informação.")
    experience(doc)
    education(doc)
    skills(doc)
    languages(doc)
    courses(doc)
    projects(doc)
    sfia(doc)
    doc.core_properties.title = "Currículo geral V5 de Nicolas Beraldes Tarifa"
    doc.core_properties.subject = "Modelo padrão em português brasileiro"
    doc.core_properties.author = "Nicolas Beraldes Tarifa"
    path = OUT / "V5-geral-padrao-pt-BR.docx"
    doc.save(path)
    return path


def build_sidebar() -> Path:
    doc = Document()
    setup(doc, sidebar=True)
    add(doc, "Nicolas Beraldes Tarifa", "Title")
    left, right = columns(doc)
    contacts(left, True)
    skills(left, True)
    languages(left, True)
    education(left, True)
    heading(right, "Perfil profissional")
    add(right, "Atuo em suporte de TI, redes e gestão de projetos. Desenvolvo este portfólio "
        "com agentes de IA e aplico ferramentas de IA em desenvolvimento e operações. "
        "Também tenho experiência em comércio eletrônico e tráfego pago. Curso "
        "Gestão da Tecnologia da Informação.")
    experience(right, compact=True)
    remove_empty_cell_start(left)
    remove_empty_cell_start(right)
    page_break(doc)
    left, right = columns(doc)
    projects(left, compact=True)
    sfia(left, compact=True)
    courses(right, compact=True)
    remove_empty_cell_start(left)
    remove_empty_cell_start(right)
    doc.core_properties.title = "Currículo geral V5 com barra lateral de Nicolas Beraldes Tarifa"
    doc.core_properties.subject = "Modelo de perfil em português brasileiro"
    doc.core_properties.author = "Nicolas Beraldes Tarifa"
    path = OUT / "V5-geral-barra-lateral-pt-BR.docx"
    doc.save(path)
    return path


if __name__ == "__main__":
    validate_sources()
    print(build_standard())
    print(build_sidebar())
