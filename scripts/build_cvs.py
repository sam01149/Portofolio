from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import BaseDocTemplate, Frame, KeepTogether, PageTemplate, Paragraph, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parents[1]
INK = colors.black


def register_fonts():
    fonts = Path("C:/Windows/Fonts")
    for name, filename in {
        "Calibri": "calibri.ttf",
        "Calibri-Bold": "calibrib.ttf",
        "Calibri-Italic": "calibrii.ttf",
        "Calibri-BoldItalic": "calibriz.ttf",
    }.items():
        pdfmetrics.registerFont(TTFont(name, str(fonts / filename)))
    pdfmetrics.registerFontFamily(
        "Calibri", normal="Calibri", bold="Calibri-Bold",
        italic="Calibri-Italic", boldItalic="Calibri-BoldItalic",
    )


COPY = {'en': {'filename': 'CV_Samuel_Armando_Napitu_EN.pdf',
        'location': 'South Jakarta, Indonesia',
        'summary_heading': 'SUMMARY',
        'summary': 'BNSP-certified Data Scientist and Information Systems undergraduate at Telkom University '
                   'Jakarta (GPA: 3.69/4.00), with experience in data governance, Python pipelines, Power '
                   'Automate, and Power BI.',
        'skills_heading': 'SKILLS',
        'skills': [('Data & Machine Learning', 'Python, SQL, Pandas, NumPy, Scikit-learn, CRISP-DM, Streamlit'),
                   ('Data Governance & Automation',
                    'SharePoint, metadata management, naming audit, Power Automate'),
                   ('Business Intelligence', 'Power BI, Power Query'),
                   ('Development & Tools',
                    'JavaScript, PHP, HTML/CSS, Next.js, Laravel, Node.js, REST API, MySQL, Supabase, Redis, '
                    'Git/GitHub, Vercel, Microsoft Entra')],
        'experience_heading': 'EXPERIENCE',
        'experience': [{'title': 'Data &amp; Analytics Intern - PT Telkom Indonesia',
                        'date': 'August 2026 - October 2026',
                        'meta': 'Chapter Data Science & AI / AIX | Digital Product Division | South Jakarta, '
                                'Indonesia',
                        'bullets': ['Built a Python metadata pipeline for 26,713 SharePoint entries, classifying '
                                    'document type, sensitivity, and status.',
                                    'Developed Power Automate inventory flows with pagination and CSV export; '
                                    'diagnosed Power Query refresh limitations.',
                                    'Built a Talent Dashboard portal prototype using Next.js, Microsoft Entra '
                                    'authentication, and Power BI embedding.']}],
        'projects_heading': 'PROJECTS',
        'projects': [{'title': 'AIX Data Governance &amp; Metadata Automation',
                      'date': 'August - October 2026',
                      'meta': 'Internship Project | Python | SharePoint | Power Automate',
                      'bullets': ['Audited a 26,713-entry baseline: identified 22,684 naming violations (84.9%); '
                                  'produced classified Excel/CSV catalogs and SharePoint inventory flows.']},
                     {'title': 'Daun Merah - Forex Intelligence PWA',
                      'date': 'May 2026 - Present',
                      'meta': 'Personal Project | Vanilla JS | Node.js | Redis | Vercel',
                      'bullets': ['Built a serverless forex PWA combining macroeconomic data, technical '
                                  'indicators, and news from FRED, CFTC, Yahoo Finance, and ECB.',
                                  'Implemented Redis caching, distributed locking, and multiple LLM providers '
                                  'with fallback and timeout handling.']},
                     {'title': 'Machine Learning-Based Customer Segmentation',
                      'date': 'April 2026',
                      'meta': 'Certification Project | Python | Scikit-learn | Streamlit',
                      'bullets': ['Built a CRISP-DM customer segmentation model with preprocessing, EDA, '
                                  'GridSearchCV, and a Streamlit prediction app.',
                                  "Presented the methodology as an invited speaker at Telkom University's Data "
                                  'Science Bukan Cuma Coding webinar (June 2026).']},
                     {'title': 'Quality Control System Design',
                      'date': 'September 2024 - June 2025',
                      'meta': 'Academic Research | PT Estima Reka Sakti | System Analysis | UI Design',
                      'bullets': ['Mapped construction quality-control processes and bottlenecks through field '
                                  'research; designed monitoring use cases, relational ERD, and UI wireframes.']}],
        'certifications_heading': 'CERTIFICATIONS',
        'certifications': [('Data Scientist Certification, LSP Data / BNSP', 'April 2026'),
                           ('IBM Data Science Professional Certificate, Coursera', 'March 2026')],
        'organization_heading': 'ORGANIZATION',
        'organization_title': 'Christian Student Fellowship, Telkom University Jakarta',
        'organization_date': 'May 2025',
        'organization_bullets': ['Chaired a three-day Easter retreat with 56 team members and an IDR 36 million '
                                 'budget; coordinated schedules, divisions, and risk management.'],
        'education_heading': 'EDUCATION',
        'education_title': 'Telkom University Jakarta',
        'education_date': '2023 - Present',
        'education_meta': 'Bachelor of Information Systems | GPA: 3.69 / 4.00'},
 'id': {'filename': 'CV_Samuel_Armando_Napitu_ID.pdf',
        'location': 'Jakarta Selatan, Indonesia',
        'summary_heading': 'RINGKASAN',
        'summary': 'Data Scientist tersertifikasi BNSP dan mahasiswa S1 Sistem Informasi Telkom University '
                   'Jakarta (IPK: 3,69/4,00), dengan pengalaman data governance, pipeline Python, Power Automate, '
                   'dan Power BI.',
        'skills_heading': 'KEAHLIAN',
        'skills': [('Data & Machine Learning', 'Python, SQL, Pandas, NumPy, Scikit-learn, CRISP-DM, Streamlit'),
                   ('Data Governance & Otomasi', 'SharePoint, metadata management, naming audit, Power Automate'),
                   ('Business Intelligence', 'Power BI, Power Query'),
                   ('Pengembangan & Tools',
                    'JavaScript, PHP, HTML/CSS, Next.js, Laravel, Node.js, REST API, MySQL, Supabase, Redis, '
                    'Git/GitHub, Vercel, Microsoft Entra')],
        'experience_heading': 'PENGALAMAN',
        'experience': [{'title': 'Data &amp; Analytics Intern - PT Telkom Indonesia',
                        'date': 'Agustus 2026 - Oktober 2026',
                        'meta': 'Chapter Data Science & AI / AIX | Divisi Digital Product | Jakarta Selatan, '
                                'Indonesia',
                        'bullets': ['Membangun pipeline metadata Python untuk 26.713 entri SharePoint, '
                                    'mengklasifikasikan jenis dokumen, sensitivitas, dan status.',
                                    'Mengembangkan flow inventaris Power Automate dengan pagination dan ekspor '
                                    'CSV; mendiagnosis keterbatasan refresh Power Query.',
                                    'Membangun prototipe portal Talent Dashboard dengan Next.js, autentikasi '
                                    'Microsoft Entra, dan embedding Power BI.']}],
        'projects_heading': 'PROYEK',
        'projects': [{'title': 'Data Governance &amp; Otomasi Metadata AIX',
                      'date': 'Agustus - Oktober 2026',
                      'meta': 'Proyek Magang | Python | SharePoint | Power Automate',
                      'bullets': ['Mengaudit baseline 26.713 entri: menemukan 22.684 entri tidak sesuai penamaan '
                                  '(84,9%); menghasilkan katalog Excel/CSV terklasifikasi dan flow inventaris '
                                  'SharePoint.']},
                     {'title': 'Daun Merah - Forex Intelligence PWA',
                      'date': 'Mei 2026 - Sekarang',
                      'meta': 'Proyek Pribadi | Vanilla JS | Node.js | Redis | Vercel',
                      'bullets': ['Membangun PWA forex serverless yang menggabungkan data makroekonomi, indikator '
                                  'teknikal, dan berita dari FRED, CFTC, Yahoo Finance, dan ECB.',
                                  'Menerapkan Redis caching, distributed locking, dan beberapa penyedia LLM '
                                  'dengan penanganan fallback serta timeout.']},
                     {'title': 'Segmentasi Pelanggan Berbasis Machine Learning',
                      'date': 'April 2026',
                      'meta': 'Proyek Sertifikasi | Python | Scikit-learn | Streamlit',
                      'bullets': ['Membangun model segmentasi pelanggan dengan CRISP-DM, praproses, EDA, '
                                  'GridSearchCV, dan aplikasi prediksi Streamlit.',
                                  'Mempresentasikan metodologi sebagai pembicara undangan webinar Data Science '
                                  'Bukan Cuma Coding Telkom University (Juni 2026).']},
                     {'title': 'Perancangan Sistem Quality Control',
                      'date': 'September 2024 - Juni 2025',
                      'meta': 'Penelitian Akademik | PT Estima Reka Sakti | Analisis Sistem | Desain UI',
                      'bullets': ['Memetakan proses dan hambatan quality control konstruksi melalui riset '
                                  'lapangan; merancang use case monitoring, ERD relasional, dan UI wireframe.']}],
        'certifications_heading': 'SERTIFIKASI',
        'certifications': [('Sertifikasi Data Scientist, LSP Data / BNSP', 'April 2026'),
                           ('IBM Data Science Professional Certificate, Coursera', 'Maret 2026')],
        'organization_heading': 'ORGANISASI',
        'organization_title': 'Persekutuan Mahasiswa Kristen, Telkom University Jakarta',
        'organization_date': 'Mei 2025',
        'organization_bullets': ['Menjadi ketua pelaksana Retreat Paskah tiga hari dengan 56 anggota tim dan '
                                 'anggaran Rp36 juta; mengoordinasikan jadwal, divisi, dan manajemen risiko.'],
        'education_heading': 'PENDIDIKAN',
        'education_title': 'Telkom University Jakarta',
        'education_date': '2023 - Sekarang',
        'education_meta': 'S1 Sistem Informasi | IPK: 3,69 / 4,00'}}


def make_styles():
    base = getSampleStyleSheet()
    return {
        "name": ParagraphStyle("Name", parent=base["Normal"], fontName="Calibri-Bold", fontSize=20, leading=22, alignment=TA_CENTER, spaceAfter=6),
        "contact": ParagraphStyle("Contact", parent=base["Normal"], fontName="Calibri", fontSize=9, leading=10.5, alignment=TA_CENTER),
        "section": ParagraphStyle("Section", parent=base["Normal"], fontName="Calibri-Bold", fontSize=11, leading=12, spaceBefore=6, spaceAfter=3),
        "body": ParagraphStyle("Body", parent=base["Normal"], fontName="Calibri", fontSize=10, leading=11.5, alignment=TA_LEFT),
        "title": ParagraphStyle("Title", parent=base["Normal"], fontName="Calibri-Bold", fontSize=11, leading=12.5),
        "date": ParagraphStyle("Date", parent=base["Normal"], fontName="Calibri", fontSize=10, leading=12.5, alignment=TA_RIGHT),
        "meta": ParagraphStyle("Meta", parent=base["Normal"], fontName="Calibri-Italic", fontSize=10, leading=10.5, spaceAfter=2),
        "bullet": ParagraphStyle("Bullet", parent=base["Normal"], fontName="Calibri", fontSize=10, leading=11.5, leftIndent=20, firstLineIndent=-10, bulletIndent=7, spaceAfter=1.5),
    }


def section_heading(text, styles, width):
    line = Table([[""]], colWidths=[width], rowHeights=[0.7])
    line.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), INK)]))
    return KeepTogether([Paragraph(text, styles["section"]), line, Spacer(1, 3)])


def dated_title(title, date, styles, width):
    table = Table([[Paragraph(title, styles["title"]), Paragraph(date, styles["date"])]], colWidths=[width - 130, 130])
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
    ]))
    return table


def bullet(text, styles):
    return Paragraph(text, styles["bullet"], bulletText="\u2022")


def draw_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Calibri", 8)
    canvas.setFillColor(INK)
    canvas.drawString(doc.leftMargin, 0.3 * inch, "Samuel Armando Napitu")
    canvas.drawRightString(LETTER[0] - doc.rightMargin, 0.3 * inch, str(doc.page))
    canvas.restoreState()


def build(language):
    data = COPY[language]
    styles = make_styles()
    output = ROOT / data["filename"]
    doc = BaseDocTemplate(
        str(output), pagesize=LETTER,
        leftMargin=0.55 * inch, rightMargin=0.55 * inch,
        topMargin=0.5 * inch, bottomMargin=0.5 * inch,
        title=f"Samuel Armando Napitu - CV ({language.upper()})",
        author="Samuel Armando Napitu",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates(PageTemplate(id="cv", frames=[frame], onPage=draw_footer))

    linkedin = "linkedin.com/in/samuel-armando-4149a4247"
    github = "github.com/sam01149"
    contact = (
        f"{data['location']} | +62 812-6059-2450 | samuelarmando93@gmail.com | "
        f'<u><link href="https://www.{linkedin}/" color="#000000">{linkedin}</link></u> | '
        f'<u><link href="https://{github}" color="#000000">{github}</link></u>'
    )
    story = [
        Paragraph("Samuel Armando Napitu", styles["name"]),
        Paragraph(contact, styles["contact"]),
        section_heading(data["summary_heading"], styles, doc.width),
        Paragraph(data["summary"], styles["body"]),
        section_heading(data["skills_heading"], styles, doc.width),
    ]
    for label, value in data["skills"]:
        story.append(Paragraph(f"<b>{label} :</b> {value}", styles["body"]))

    story.append(section_heading(data["experience_heading"], styles, doc.width))
    for item in data["experience"]:
        block = [dated_title(item["title"], item["date"], styles, doc.width), Paragraph(item["meta"], styles["meta"])]
        block.extend(bullet(text, styles) for text in item["bullets"])
        block.append(Spacer(1, 2))
        story.append(KeepTogether(block))

    story.append(section_heading(data["projects_heading"], styles, doc.width))
    for item in data["projects"]:
        block = [dated_title(item["title"], item["date"], styles, doc.width), Paragraph(item["meta"], styles["meta"])]
        block.extend(bullet(text, styles) for text in item["bullets"])
        block.append(Spacer(1, 2))
        story.append(KeepTogether(block))

    story.append(section_heading(data["certifications_heading"], styles, doc.width))
    for title, date in data["certifications"]:
        story.append(dated_title(title, date, styles, doc.width))

    story.append(section_heading(data["organization_heading"], styles, doc.width))
    org = [dated_title(data["organization_title"], data["organization_date"], styles, doc.width)]
    org.extend(bullet(text, styles) for text in data["organization_bullets"])
    story.append(KeepTogether(org))

    story.append(section_heading(data["education_heading"], styles, doc.width))
    story.append(dated_title(data["education_title"], data["education_date"], styles, doc.width))
    story.append(Paragraph(data["education_meta"], styles["meta"]))
    doc.build(story)
    return output


if __name__ == "__main__":
    register_fonts()
    for lang in ("en", "id"):
        print(build(lang))
