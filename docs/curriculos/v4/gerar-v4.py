"""Gera o currículo geral V4 de uma coluna a partir da base pt-BR."""

from __future__ import annotations

import html
import re
from pathlib import Path

from lxml import html as lhtml
from reportlab import rl_config
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = Path(__file__).resolve().parent / "V4-geral-uma_coluna-pt-BR.pdf"
INDEX = lhtml.parse(str(ROOT / "static/pt-BR/index.html"))
PROJECTS = lhtml.parse(str(ROOT / "static/pt-BR/projetos.html"))
BLACK = colors.black

pdfmetrics.registerFont(TTFont("Arial", "C:/Windows/Fonts/arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", "C:/Windows/Fonts/arialbd.ttf"))
pdfmetrics.registerFontFamily("Arial", normal="Arial", bold="Arial-Bold")
rl_config.canvas_basefontname = "Arial"


def clean(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def node_text(node) -> str:
    return clean(node.text_content())


def first(root, query):
    matches = root.xpath(query)
    if not matches:
        raise ValueError(query)
    return matches[0]


STYLE = {
    "name": ParagraphStyle("name", fontName="Arial-Bold", fontSize=20, leading=23,
                           textColor=BLACK, spaceAfter=7),
    "contact": ParagraphStyle("contact", fontName="Arial", fontSize=9.6, leading=12.7,
                              textColor=BLACK, spaceAfter=2),
    "section": ParagraphStyle("section", fontName="Arial-Bold", fontSize=11, leading=13.5,
                              textColor=BLACK, spaceBefore=12, spaceAfter=5, keepWithNext=True),
    "role": ParagraphStyle("role", fontName="Arial-Bold", fontSize=10.1, leading=12.5,
                           textColor=BLACK, spaceBefore=7, spaceAfter=2, keepWithNext=True),
    "meta": ParagraphStyle("meta", fontName="Arial", fontSize=9.4, leading=11.7,
                           textColor=BLACK, spaceAfter=2, keepWithNext=True),
    "body": ParagraphStyle("body", fontName="Arial", fontSize=10, leading=13.2,
                           textColor=BLACK, spaceAfter=4),
    "small": ParagraphStyle("small", fontName="Arial", fontSize=9.4, leading=12.2,
                            textColor=BLACK, spaceAfter=2),
    "category": ParagraphStyle("category", fontName="Arial-Bold", fontSize=9.7, leading=12,
                               textColor=BLACK, spaceBefore=9, spaceAfter=3, keepWithNext=True),
    "course": ParagraphStyle("course", fontName="Arial", fontSize=9.5, leading=12.8,
                             textColor=BLACK, spaceAfter=2.5),
}


def paragraph(value: str, kind: str = "body") -> Paragraph:
    return Paragraph(html.escape(value, quote=False), STYLE[kind])


def section(story: list, title: str) -> None:
    story.append(paragraph(title, "section"))


def experience(story: list) -> None:
    section(story, "Histórico profissional")
    entries = [
        (
            "Gestor de tráfego pago; apoio documental e treinamento digital",
            "Aquecedores e Piscinas Mairiporã | jan/2026 – atual",
            "Planejo campanhas em Google Ads e Meta Ads e a medição com Google Tag Manager e GA4. Criei o site e canais no Mercado Livre e na Shopee; organizei documentos e treinei os sócios em ferramentas digitais.",
        ),
        (
            "Auxiliar de instalação de fibra óptica",
            "RealFort Sistemas | prestação de serviços | 28/08/2026 – 28/09/2026",
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
            "JH Eletrônico | autônomo | jul/2022 – jan/2023",
            "Gerenciei catálogo e anúncios; atendi clientes B2C e B2B, elaborei orçamentos e acompanhei pedidos com o Bling ERP.",
        ),
    ]
    source_titles = [node_text(x) for x in INDEX.xpath('//main//section[@id="experiencia"]/ol/li/h3')]
    assert [entry[0] for entry in entries] == source_titles
    for role, meta, detail in entries:
        story.append(KeepTogether([paragraph(role, "role"), paragraph(meta, "meta"), paragraph(detail)]))


def courses(story: list) -> None:
    section(story, "Cursos e certificados")
    root = first(INDEX, '//main//details[contains(@class,"courses-screen")]')
    count = 0
    for item in root.xpath('.//h5[contains(@class,"skill-subheading")] | .//ul[contains(@class,"course-list")]/li'):
        if item.tag == "h5":
            story.append(paragraph(node_text(item), "category"))
            continue
        title = node_text(first(item, './h6'))
        metadata = node_text(item.xpath('./p')[1])
        hours = re.search(r"(\d+)\s*h", metadata)
        date = first(item, './/time').text_content().strip()
        assert hours and re.fullmatch(r"\d{2}/\d{2}/\d{4}", date), title
        story.append(Paragraph(f"{html.escape(title)} — {hours.group(1)} h · Conclusão: {date}", STYLE["course"]))
        count += 1
    assert count == 17, count


def projects(story: list) -> None:
    section(story, "Projetos")
    entries = [
        ("Este portfólio", "Projeto pessoal em HTML e CSS, com publicação por GitHub Actions e GitHub Pages. Inclui layout responsivo, temas e recursos de acessibilidade."),
        ("Optigrow", "Projeto colaborativo com Rodrigo Nascimento para serviços de marketing e tecnologia voltados a óticas da região do Porto, em Portugal."),
        ("SGCS — Sistema de Gestão de Chamados para Síndicos", "Pesquisa acadêmica e MVP em desenvolvimento pela equipe. Gerencio o projeto, coordeno prazos e entregáveis e integro as ferramentas de trabalho."),
    ]
    source_titles = [node_text(x) for x in PROJECTS.xpath('//main//section[@id="projetos"]//article/h3')]
    assert [entry[0] for entry in entries] == source_titles
    for title, detail in entries:
        story.append(KeepTogether([paragraph(title, "role"), paragraph(detail)]))


def build() -> None:
    doc = SimpleDocTemplate(
        str(OUTPUT), pagesize=A4, leftMargin=43, rightMargin=43,
        topMargin=38, bottomMargin=38, title="Currículo geral V4 — Nicolas Beraldes Tarifa",
        author="Nicolas Beraldes Tarifa", subject="Currículo geral em português brasileiro",
    )
    story = [
        paragraph("Nicolas Beraldes Tarifa", "name"),
        Paragraph(
            'Telefone: +55 11 95057-1593 · E-mail: <link href="mailto:beraldesnicolas@gmail.com" color="black">beraldesnicolas@gmail.com</link>',
            STYLE["contact"],
        ),
        Paragraph(
            'Portfólio: <link href="https://nicolas-b-t.github.io/portfolio" color="black">nicolas-b-t.github.io/portfolio</link>',
            STYLE["contact"],
        ),
    ]
    section(story, "Sobre")
    story.append(paragraph(
        "Atuo em operações digitais e de TI, com experiência em tráfego pago, comércio eletrônico, suporte técnico e redes. Curso Gestão da Tecnologia da Informação."
    ))
    experience(story)
    section(story, "Principais competências")
    story.append(paragraph(
        "Tráfego pago (Google Ads e Meta Ads); análise digital (Google Tag Manager e GA4); comércio eletrônico (Mercado Livre, Shopee e Bling ERP); gestão documental; atendimento B2C e B2B."
    ))
    section(story, "Competências de TI — SFIA 9")
    story.append(paragraph(
        "Autoavaliação: gestão de incidentes (USUP, nível 3); suporte a aplicações (ASUP, nível 3); suporte a redes (NTAS, nível 2); instalação e remoção de sistemas (HSIN, nível 2); operações de infraestrutura (ITOP, nível 2); programação e desenvolvimento de software (PROG, nível 2); controle de mudanças (CHMG, nível 2)."
    ))
    section(story, "Formação")
    story.append(paragraph(
        "Curso superior de tecnologia em Gestão da Tecnologia da Informação — Fatec Franco da Rocha – Giuliano Cecchettini. Início: jul/2024; conclusão prevista: jul/2027."
    ))
    story.append(paragraph(
        "Inglês: TOEIC Listening & Reading 910 (Listening 450; Reading 460), teste em 26/02/2025, resultado válido até 26/02/2027.",
        "small",
    ))
    story.append(PageBreak())
    courses(story)
    projects(story)
    doc.build(story)


if __name__ == "__main__":
    build()
    print(OUTPUT)
