"""Gera os dois rascunhos DOCX V4 antes de atualizar os PDFs."""

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
OUTPUT_ONE = Path(__file__).resolve().parent / "V4-geral-uma_coluna-pt-BR-rascunho.docx"
OUTPUT_SIDE = Path(__file__).resolve().parent / "V4-geral_coluna_lateral-pt-BR-rascunho.docx"
INDEX = html.parse(str(ROOT / "static/pt-BR/index.html"))
BLACK = RGBColor(0, 0, 0)


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def setup_style(style, size: float, *, bold: bool = False, before: float = 0,
                after: float = 0, line: float = 1.08, next_: bool = False) -> None:
    style.font.name = "Arial"
    style.font.size = Pt(size)
    style.font.bold = bold
    style.font.color.rgb = BLACK
    style.font.underline = False
    style.paragraph_format.space_before = Pt(before)
    style.paragraph_format.space_after = Pt(after)
    style.paragraph_format.line_spacing = line
    style.paragraph_format.keep_with_next = next_
    style.paragraph_format.widow_control = True
    rpr = style.element.get_or_add_rPr()
    lang = rpr.find(qn("w:lang"))
    if lang is None:
        lang = OxmlElement("w:lang")
        rpr.append(lang)
    lang.set(qn("w:val"), "pt-BR")


def add(document, value: str, style: str = "Normal"):
    p = document.add_paragraph(style=style)
    p.add_run(value)
    return p


def add_hyperlink(paragraph, value: str, url: str) -> None:
    rid = paragraph.part.relate_to(url, RT.HYPERLINK, is_external=True)
    link = OxmlElement("w:hyperlink")
    link.set(qn("r:id"), rid)
    run = OxmlElement("w:r")
    props = OxmlElement("w:rPr")
    font = OxmlElement("w:rFonts")
    font.set(qn("w:ascii"), "Arial")
    font.set(qn("w:hAnsi"), "Arial")
    props.append(font)
    color = OxmlElement("w:color")
    color.set(qn("w:val"), "000000")
    props.append(color)
    underline = OxmlElement("w:u")
    underline.set(qn("w:val"), "none")
    props.append(underline)
    run.append(props)
    node = OxmlElement("w:t")
    node.text = value
    run.append(node)
    link.append(run)
    paragraph._p.append(link)


def add_contact(container, style: str = "Contact") -> None:
    if style == "Sidebar":
        for value, url in [
            ("+55 11 95057-1593", "tel:+5511950571593"),
            ("beraldesnicolas@gmail.com", "mailto:beraldesnicolas@gmail.com"),
            ("nicolas-b-t.github.io/portfolio", "https://nicolas-b-t.github.io/portfolio"),
        ]:
            p = container.add_paragraph(style=style)
            add_hyperlink(p, value, url)
        return
    p = container.add_paragraph(style=style)
    p.add_run("Telefone: ")
    add_hyperlink(p, "+55 11 95057-1593", "tel:+5511950571593")
    p.add_run(" · E-mail: ")
    add_hyperlink(p, "beraldesnicolas@gmail.com", "mailto:beraldesnicolas@gmail.com")
    p = container.add_paragraph(style=style)
    p.add_run("Portfólio: ")
    add_hyperlink(p, "nicolas-b-t.github.io/portfolio", "https://nicolas-b-t.github.io/portfolio")


def add_company(container, company: str, suffix: str) -> None:
    urls = {
        "RealFort Sistemas": "https://realfortsistemas.com.br/",
        "Lukos Tecnologia": "https://lukos.com.br/",
        "Instituto Alpha de Saúde Integral": "https://alphainstituto.com.br/",
        "JH Eletrônico": "https://institucional.jheletronico.com.br/",
    }
    p = container.add_paragraph(style="Meta")
    if company in urls:
        add_hyperlink(p, company, urls[company])
    else:
        p.add_run(company)
    p.add_run(suffix)


def add_heading(document, value: str):
    return add(document, value, "Section")


def add_experience(document) -> None:
    add_heading(document, "Histórico profissional")
    entries = [
        (
            "Gestor de tráfego pago",
            "Aquecedores e Piscinas Mairiporã | jan/2026 – atual",
            "Planejo campanhas em Google Ads e Meta Ads e a medição com Google Tag Manager e GA4. Criei o site e canais no Mercado Livre e na Shopee; organizei documentos e treinei os sócios em ferramentas digitais.",
        ),
        (
            "Auxiliar de instalação de fibra óptica",
            "RealFort Sistemas | 28/08/2026 – 28/09/2026",
            "Instalei redes FTTH e conexões a rádio, configurei ONU, ONT e roteadores e diagnostiquei falhas com power meter, OTDR e VFL. Realizei fusão de fibra como aprendiz.",
        ),
        (
            "Técnico de suporte Help Desk",
            "Lukos Tecnologia | set/2025 – dez/2025",
            "Configurei e dei suporte a ERP e PDV; diagnostiquei falhas remotamente e analisei NF-e e NFC-e.",
        ),
        (
            "Técnico de suporte de TI",
            "Instituto Alpha de Saúde Integral | abr/2023 – jun/2024",
            "Prestei suporte N1/N2 em sistemas hospitalares; mantive computadores e impressoras, administrei o Microsoft Active Directory e produzi documentação técnica.",
        ),
        (
            "Assistente de E-commerce",
            "JH Eletrônico | jul/2022 – jan/2023",
            "Gerenciei catálogo e anúncios; atendi clientes B2C e B2B, elaborei orçamentos e acompanhei pedidos com o Bling ERP.",
        ),
    ]
    assert len(entries) == 5
    for title, meta, detail in entries:
        add(document, title, "Role")
        company, dates = meta.split(" | ", 1)
        add_company(document, company, " | " + dates)
        add(document, detail, "Normal")


def add_courses(document) -> None:
    add_heading(document, "Cursos e certificados")
    root = INDEX.xpath('//main//details[contains(@class,"courses-screen")]')[0]
    count = 0
    for item in root.xpath('.//h5[contains(@class,"skill-subheading")] | .//ul[contains(@class,"course-list")]/li'):
        if item.tag == "h5":
            add(document, normalize(item.text_content()), "Category")
            continue
        title = normalize(item.xpath('./h6')[0].text_content())
        metadata = normalize(item.xpath('./p')[1].text_content())
        hours = re.search(r"(\d+)\s*h", metadata)
        date = item.xpath('.//time')[0].text_content().strip()
        assert hours and re.fullmatch(r"\d{2}/\d{2}/\d{4}", date), title
        add(document, f"{title} — {hours.group(1)} h · Conclusão: {date}", "Course")
        count += 1
    assert count == 17


def add_projects(document) -> None:
    add_heading(document, "Projetos")
    projects = [
        (
            "Site e portfólio pessoal",
            "Projeto pessoal em HTML e CSS, com publicação por GitHub Actions e GitHub Pages. Inclui layout responsivo, temas e recursos de acessibilidade.",
            "https://nicolas-b-t.github.io/portfolio",
        ),
        (
            "Optigrow",
            "Projeto colaborativo para serviços de marketing e tecnologia voltados a óticas da região do Porto, em Portugal.",
            "https://optigrow.vercel.app/",
        ),
        (
            "SGCS — Sistema de Gestão de Chamados para Síndicos",
            "Pesquisa acadêmica e MVP em desenvolvimento pela equipe. Gerencio o projeto, coordeno prazos e entregáveis e integro as ferramentas de trabalho.",
            "https://sgcs-seven.vercel.app/",
        ),
    ]
    for title, detail, url in projects:
        p = document.add_paragraph(style="Role")
        add_hyperlink(p, title, url)
        add(document, detail)


def configure(doc, *, lateral: bool = False) -> None:
    sec = doc.sections[0]
    sec.page_width = Cm(21)
    sec.page_height = Cm(29.7)
    sec.top_margin = Cm(1.4)
    sec.bottom_margin = Cm(1.4)
    sec.left_margin = Cm(1.55)
    sec.right_margin = Cm(1.55)

    styles = doc.styles
    setup_style(styles["Normal"], 9.1 if lateral else 10, after=2.4 if lateral else 3.8, line=1.05 if lateral else 1.1)
    setup_style(styles["Title"], 20, bold=True, after=6, line=1.0)
    title_ppr = styles["Title"].element.get_or_add_pPr()
    title_border = title_ppr.find(qn("w:pBdr"))
    if title_border is not None:
        title_ppr.remove(title_border)
    setup_style(styles.add_style("Contact", 1), 8.6 if lateral else 9.6, after=2, line=1.06)
    setup_style(styles.add_style("Section", 1), 10 if lateral else 11, bold=True, before=7 if lateral else 10, after=3 if lateral else 4.5, next_=True)
    setup_style(styles.add_style("Role", 1), 9.2 if lateral else 10.1, bold=True, before=4 if lateral else 6.5, after=1, next_=True)
    setup_style(styles.add_style("Meta", 1), 8.5 if lateral else 9.4, after=1.5, next_=True)
    setup_style(styles.add_style("Category", 1), 8.9 if lateral else 9.7, bold=True, before=5 if lateral else 7.5, after=1.5 if lateral else 2, next_=True)
    setup_style(styles.add_style("Course", 1), 8.6 if lateral else 9.5, after=1.5 if lateral else 2, line=1.04 if lateral else 1.08)
    setup_style(styles.add_style("Sidebar", 1), 8.35, after=2.6, line=1.07)
    setup_style(styles.add_style("SidebarHeading", 1), 9.1, bold=True, before=9, after=3, next_=True)


def add_about(container) -> None:
    add_heading(container, "Sobre")
    add(container, "Atuo em operações digitais e de TI, com experiência em tráfego pago, comércio eletrônico, suporte técnico e redes. Curso Gestão da Tecnologia da Informação.")


def add_primary_skills(container, sidebar: bool = False) -> None:
    if sidebar:
        add(container, "Principais competências", "SidebarHeading")
        add(container, "Tráfego pago (Google Ads e Meta Ads); análise digital (Google Tag Manager e GA4); comércio eletrônico (Mercado Livre, Shopee e Bling ERP); gestão documental; atendimento B2C e B2B.", "Sidebar")
    else:
        add_heading(container, "Principais competências")
        add(container, "Tráfego pago (Google Ads e Meta Ads); análise digital (Google Tag Manager e GA4); comércio eletrônico (Mercado Livre, Shopee e Bling ERP); gestão documental; atendimento B2C e B2B.")


def add_sfia(container, sidebar: bool = False) -> None:
    if sidebar:
        add(container, "Competências de TI — SFIA 9", "SidebarHeading")
        for line in [
            "USUP Gestão de incidentes — nível 3",
            "ASUP Suporte a aplicações — nível 3",
            "NTAS Suporte a redes — nível 2",
            "HSIN Instalação e remoção de sistemas — nível 2",
            "ITOP Operações de infraestrutura — nível 2",
            "PROG Programação e desenvolvimento de software — nível 2",
            "CHMG Controle de mudanças — nível 2",
        ]:
            add(container, line, "Sidebar")
    else:
        add_heading(container, "Competências de TI — SFIA 9")
        add(container, "Gestão de incidentes (USUP, nível 3); suporte a aplicações (ASUP, nível 3); suporte a redes (NTAS, nível 2); instalação e remoção de sistemas (HSIN, nível 2); operações de infraestrutura (ITOP, nível 2); programação e desenvolvimento de software (PROG, nível 2); controle de mudanças (CHMG, nível 2).")


def add_formation(container) -> None:
    add_heading(container, "Formação")
    p = container.add_paragraph()
    p.add_run("Curso superior de tecnologia em Gestão da Tecnologia da Informação — ")
    add_hyperlink(p, "Fatec Franco da Rocha – Giuliano Cecchettini", "https://fatecfrancodarocha.cps.sp.gov.br/gestao-da-tecnologia-da-informacao/")
    p.add_run(". Início: jul/2024; conclusão prevista: jul/2027.")


def add_english(container, sidebar: bool = False) -> None:
    if sidebar:
        add(container, "Idioma", "SidebarHeading")
        add(container, "Inglês avançado · TOEIC Listening & Reading: 910/990 pontos.", "Sidebar")
    else:
        add(container, "Inglês avançado · TOEIC Listening & Reading: 910/990 pontos.", "Meta")


def set_cell_margins(cell, top=90, start=110, bottom=90, end=110) -> None:
    tcpr = cell._tc.get_or_add_tcPr()
    margins = tcpr.first_child_found_in("w:tcMar")
    if margins is None:
        margins = OxmlElement("w:tcMar")
        tcpr.append(margins)
    for edge, size in [("top", top), ("start", start), ("bottom", bottom), ("end", end)]:
        tag = qn("w:" + edge)
        node = margins.find(tag)
        if node is None:
            node = OxmlElement("w:" + edge)
            margins.append(node)
        node.set(qn("w:w"), str(size))
        node.set(qn("w:type"), "dxa")


def clear_initial_paragraph(cell) -> None:
    first = cell.paragraphs[0]
    if not first.text and len(cell.paragraphs) > 1:
        cell._tc.remove(first._p)


def make_lateral_table(doc):
    table = doc.add_table(rows=1, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.columns[0].width = Cm(5.15)
    table.columns[1].width = Cm(12.75)
    left, right = table.rows[0].cells
    left.width = Cm(5.15)
    right.width = Cm(12.75)
    left.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.TOP
    right.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.TOP
    set_cell_margins(left, 65, 100, 65, 160)
    set_cell_margins(right, 65, 160, 65, 70)
    shade = OxmlElement("w:shd")
    shade.set(qn("w:fill"), "F2F2F2")
    left._tc.get_or_add_tcPr().append(shade)
    return left, right


def build_one() -> None:
    doc = Document()
    configure(doc)

    add(doc, "Nicolas Beraldes Tarifa", "Title")
    add_contact(doc)
    add_about(doc)
    add_experience(doc)
    add_primary_skills(doc)
    add_sfia(doc)
    add_formation(doc)
    add_english(doc)

    page_break = doc.add_paragraph()
    page_break.add_run().add_break(WD_BREAK.PAGE)
    add_courses(doc)
    add_projects(doc)

    doc.core_properties.title = "Currículo geral V4 de Nicolas Beraldes Tarifa"
    doc.core_properties.subject = "Rascunho para revisão em português brasileiro"
    doc.core_properties.author = "Nicolas Beraldes Tarifa"
    doc.save(OUTPUT_ONE)
    print(OUTPUT_ONE)


def build_side() -> None:
    doc = Document()
    configure(doc, lateral=True)
    add(doc, "Nicolas Beraldes Tarifa", "Title")
    left, right = make_lateral_table(doc)
    add(left, "Contato", "SidebarHeading")
    add_contact(left, "Sidebar")
    add_primary_skills(left, sidebar=True)
    add_sfia(left, sidebar=True)
    add_english(left, sidebar=True)
    add_about(right)
    add_experience(right)
    add_formation(right)
    clear_initial_paragraph(left)
    clear_initial_paragraph(right)

    p = doc.add_paragraph()
    p.add_run().add_break(WD_BREAK.PAGE)
    left, right = make_lateral_table(doc)
    add_projects(left)
    add_courses(right)
    clear_initial_paragraph(left)
    clear_initial_paragraph(right)

    doc.core_properties.title = "Currículo geral V4 com coluna lateral de Nicolas Beraldes Tarifa"
    doc.core_properties.subject = "Rascunho para revisão em português brasileiro"
    doc.core_properties.author = "Nicolas Beraldes Tarifa"
    doc.save(OUTPUT_SIDE)
    print(OUTPUT_SIDE)


if __name__ == "__main__":
    build_one()
    build_side()
