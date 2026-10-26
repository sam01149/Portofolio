from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
NAVY = colors.HexColor("#173A70")
RUST = colors.HexColor("#B65D3B")
INK = colors.HexColor("#1F2937")
MUTED = colors.HexColor("#4B5563")
LINE = colors.HexColor("#D7DDE5")
PAPER = colors.HexColor("#FFFFFF")


COPY = {
    "en": {
        "filename": "CV_Samuel_Armando_Napitu_EN.pdf",
        "location": "South Jakarta, Indonesia",
        "summary_title": "PROFESSIONAL SUMMARY",
        "summary": (
            "BNSP-certified Data Scientist and Information Systems undergraduate with hands-on experience "
            "in data governance, metadata management, data pipelines, and business intelligence. Built a "
            "metadata catalog pipeline for 26,713 SharePoint entries during an internship at Telkom Indonesia "
            "and developed data-driven applications using Python, SQL, Power BI, and web technologies."
        ),
        "skills_title": "TECHNICAL SKILLS",
        "skills": [
            ("Data & BI", "Python, SQL, Pandas, NumPy, Scikit-learn, Power BI, Power Query"),
            ("Governance & Automation", "Data governance, metadata management, data quality audit, SharePoint, Power Automate"),
            ("Application Development", "Next.js, JavaScript, PHP, Laravel, Node.js, HTML/CSS, RESTful APIs"),
            ("Platforms & Tools", "Microsoft Entra, MySQL, Supabase, Redis, Git/GitHub, Vercel, Streamlit"),
        ],
        "experience_title": "PROFESSIONAL EXPERIENCE",
        "experience": [
            {
                "role": "Data Scientist Intern",
                "company": "PT Telkom Indonesia - Chapter AI & Experience, Digital Product Division",
                "date": "Aug 2026 - Oct 2026",
                "location": "South Jakarta, Indonesia - Hybrid",
                "bullets": [
                    "Built a metadata catalog pipeline for 26,713 SharePoint repository entries to support repository visibility and governance.",
                    "Audited metadata quality and naming convention compliance, and supported SharePoint inventory automation using Power Automate and Power Query.",
                    "Developed a Talent Dashboard portal prototype with Microsoft Entra authentication and Power BI integration using Next.js.",
                ],
            },
            {
                "role": "Business Process Analyst & UI Designer Intern",
                "company": "PT Estima Reka Sakti",
                "date": "Sep 2024 - Jun 2025",
                "location": "South Tangerang, Indonesia",
                "bullets": [
                    "Mapped construction quality-control processes through field research and identified operational bottlenecks.",
                    "Delivered an accepted web-based monitoring system design covering use cases, relational ERD, and UI wireframes.",
                ],
            },
        ],
        "education_title": "EDUCATION",
        "education": "Bachelor of Information Systems - Telkom University Jakarta",
        "education_meta": "2023 - Present | GPA: 3.69 / 4.00",
        "cert_title": "CERTIFICATIONS",
        "certs": [
            "Data Scientist Certification - LSP Data / BNSP, April 2026",
            "IBM Data Science Professional Certificate - Coursera, March 2026",
        ],
        "projects_title": "SELECTED PROJECTS",
        "projects_continued": "SELECTED PROJECTS - CONTINUED",
        "projects": [
            {
                "title": "Daun Merah - Forex Intelligence PWA",
                "date": "May 2026 - Present",
                "stack": "Vanilla JavaScript | Node.js | Redis | Vercel | AI APIs",
                "bullets": [
                    "Designed and developed a serverless Progressive Web App integrating macroeconomic data, technical indicators, and market news for forex analysis.",
                    "Implemented Redis caching and distributed locking across data sources including FRED, CFTC, Yahoo Finance, and ECB.",
                    "Integrated multiple LLM providers with fallback and timeout mechanisms to improve analysis reliability.",
                ],
            },
            {
                "title": "Machine Learning-Based Customer Segmentation",
                "date": "April 2026",
                "stack": "Python | Pandas | Scikit-learn | Streamlit | CRISP-DM",
                "bullets": [
                    "Built a customer segmentation model using the CRISP-DM workflow, including preprocessing, EDA, modeling, and GridSearchCV optimization.",
                    "Developed a Streamlit application to automate segment predictions for new customers.",
                    "Presented the project methodology as an invited speaker at Telkom University's Data Science Bukan Cuma Coding webinar in June 2026.",
                ],
            },
            {
                "title": "National Airline Management Application",
                "date": "December 2024",
                "stack": "PHP | Laravel | MySQL",
                "bullets": [
                    "Built modules for flight scheduling, passenger management, and ticket booking using Laravel MVC and relational database design.",
                    "Implemented form validation, middleware-based route protection, and table relationships following Laravel conventions.",
                ],
            },
        ],
        "leadership_title": "LEADERSHIP",
        "leadership": (
            "Committee Chairperson, Easter Retreat - Christian Student Fellowship, Telkom University Jakarta "
            "(May 2025). Led 56 team members and managed a budget of IDR 36 million for a three-day program."
        ),
    },
    "id": {
        "filename": "CV_Samuel_Armando_Napitu_ID.pdf",
        "location": "Jakarta Selatan, Indonesia",
        "summary_title": "RINGKASAN PROFESIONAL",
        "summary": (
            "Data Scientist tersertifikasi BNSP dan mahasiswa S1 Sistem Informasi dengan pengalaman praktis "
            "dalam data governance, metadata management, data pipeline, dan business intelligence. Membangun "
            "pipeline katalog metadata untuk 26.713 entri SharePoint selama magang di Telkom Indonesia serta "
            "mengembangkan aplikasi berbasis data menggunakan Python, SQL, Power BI, dan teknologi web."
        ),
        "skills_title": "KEAHLIAN TEKNIS",
        "skills": [
            ("Data & BI", "Python, SQL, Pandas, NumPy, Scikit-learn, Power BI, Power Query"),
            ("Governance & Otomatisasi", "Data governance, metadata management, audit kualitas data, SharePoint, Power Automate"),
            ("Pengembangan Aplikasi", "Next.js, JavaScript, PHP, Laravel, Node.js, HTML/CSS, RESTful API"),
            ("Platform & Tools", "Microsoft Entra, MySQL, Supabase, Redis, Git/GitHub, Vercel, Streamlit"),
        ],
        "experience_title": "PENGALAMAN PROFESIONAL",
        "experience": [
            {
                "role": "Data Scientist Intern",
                "company": "PT Telkom Indonesia - Chapter AI & Experience, Divisi Digital Product",
                "date": "Agu 2026 - Okt 2026",
                "location": "Jakarta Selatan, Indonesia - Hybrid",
                "bullets": [
                    "Membangun pipeline katalog metadata untuk 26.713 entri repositori SharePoint guna mendukung visibilitas dan tata kelola repositori.",
                    "Mengaudit kualitas metadata dan kepatuhan konvensi penamaan serta mendukung otomatisasi inventaris SharePoint menggunakan Power Automate dan Power Query.",
                    "Mengembangkan prototipe portal Talent Dashboard dengan autentikasi Microsoft Entra dan integrasi Power BI menggunakan Next.js.",
                ],
            },
            {
                "role": "Business Process Analyst & UI Designer Intern",
                "company": "PT Estima Reka Sakti",
                "date": "Sep 2024 - Jun 2025",
                "location": "Tangerang Selatan, Indonesia",
                "bullets": [
                    "Memetakan proses quality control konstruksi melalui riset lapangan dan mengidentifikasi hambatan operasional.",
                    "Menghasilkan rancangan sistem monitoring berbasis web yang diterima klien, mencakup use case, ERD relasional, dan UI wireframe.",
                ],
            },
        ],
        "education_title": "PENDIDIKAN",
        "education": "S1 Sistem Informasi - Telkom University Jakarta",
        "education_meta": "2023 - Sekarang | IPK: 3,69 / 4,00",
        "cert_title": "SERTIFIKASI",
        "certs": [
            "Sertifikasi Data Scientist - LSP Data / BNSP, April 2026",
            "IBM Data Science Professional Certificate - Coursera, Maret 2026",
        ],
        "projects_title": "PROYEK PILIHAN",
        "projects_continued": "PROYEK PILIHAN - LANJUTAN",
        "projects": [
            {
                "title": "Daun Merah - Forex Intelligence PWA",
                "date": "Mei 2026 - Sekarang",
                "stack": "Vanilla JavaScript | Node.js | Redis | Vercel | AI APIs",
                "bullets": [
                    "Merancang dan mengembangkan Progressive Web App serverless yang mengintegrasikan data makroekonomi, indikator teknikal, dan berita pasar untuk analisis forex.",
                    "Mengimplementasikan Redis caching dan distributed locking untuk sumber data termasuk FRED, CFTC, Yahoo Finance, dan ECB.",
                    "Mengintegrasikan beberapa penyedia LLM dengan mekanisme fallback dan timeout untuk meningkatkan keandalan analisis.",
                ],
            },
            {
                "title": "Segmentasi Pelanggan Berbasis Machine Learning",
                "date": "April 2026",
                "stack": "Python | Pandas | Scikit-learn | Streamlit | CRISP-DM",
                "bullets": [
                    "Membangun model segmentasi pelanggan menggunakan alur CRISP-DM, mencakup praproses, EDA, pemodelan, dan optimasi GridSearchCV.",
                    "Mengembangkan aplikasi Streamlit untuk mengotomatiskan prediksi segmen pelanggan baru.",
                    "Mempresentasikan metodologi proyek sebagai pembicara undangan pada webinar Data Science Bukan Cuma Coding Telkom University pada Juni 2026.",
                ],
            },
            {
                "title": "Aplikasi Manajemen Maskapai Penerbangan Nasional",
                "date": "Desember 2024",
                "stack": "PHP | Laravel | MySQL",
                "bullets": [
                    "Membangun modul penjadwalan penerbangan, manajemen penumpang, dan pemesanan tiket menggunakan Laravel MVC dan basis data relasional.",
                    "Mengimplementasikan validasi formulir, proteksi route berbasis middleware, dan relasi tabel sesuai konvensi Laravel.",
                ],
            },
        ],
        "leadership_title": "KEPEMIMPINAN",
        "leadership": (
            "Ketua Pelaksana Retreat Paskah - Persekutuan Mahasiswa Kristen, Telkom University Jakarta "
            "(Mei 2025). Memimpin 56 anggota tim dan mengelola anggaran Rp36 juta untuk program tiga hari."
        ),
    },
}


def styles():
    base = getSampleStyleSheet()
    return {
        "name": ParagraphStyle("Name", parent=base["Heading1"], fontName="Helvetica-Bold", fontSize=21, leading=24, textColor=NAVY, alignment=TA_CENTER, spaceAfter=4),
        "contact": ParagraphStyle("Contact", parent=base["BodyText"], fontName="Helvetica", fontSize=8.2, leading=11, textColor=MUTED, alignment=TA_CENTER),
        "section": ParagraphStyle("Section", parent=base["Heading2"], fontName="Helvetica-Bold", fontSize=10.5, leading=12, textColor=NAVY, spaceBefore=9, spaceAfter=5),
        "body": ParagraphStyle("Body", parent=base["BodyText"], fontName="Helvetica", fontSize=8.7, leading=11.6, textColor=INK, alignment=TA_LEFT),
        "label": ParagraphStyle("Label", parent=base["BodyText"], fontName="Helvetica-Bold", fontSize=8.7, leading=11.6, textColor=INK),
        "role": ParagraphStyle("Role", parent=base["BodyText"], fontName="Helvetica-Bold", fontSize=9.4, leading=12, textColor=INK),
        "company": ParagraphStyle("Company", parent=base["BodyText"], fontName="Helvetica", fontSize=8.5, leading=10.5, textColor=MUTED),
        "date": ParagraphStyle("Date", parent=base["BodyText"], fontName="Helvetica-Bold", fontSize=8.2, leading=10.5, textColor=RUST, alignment=TA_RIGHT),
        "bullet": ParagraphStyle("Bullet", parent=base["BodyText"], fontName="Helvetica", fontSize=8.45, leading=11.1, textColor=INK, leftIndent=10, firstLineIndent=-7, spaceAfter=2.2),
        "project": ParagraphStyle("Project", parent=base["BodyText"], fontName="Helvetica-Bold", fontSize=9.5, leading=11.5, textColor=INK),
        "stack": ParagraphStyle("Stack", parent=base["BodyText"], fontName="Helvetica-Oblique", fontSize=8.1, leading=10, textColor=MUTED, spaceAfter=3),
        "footer": ParagraphStyle("Footer", parent=base["BodyText"], fontName="Helvetica", fontSize=7.5, leading=9, textColor=MUTED, alignment=TA_CENTER),
    }


def section_heading(label, st):
    return KeepTogether([
        Paragraph(label, st["section"]),
        Table([[""]], colWidths=[181 * mm], rowHeights=[0.45], style=TableStyle([("BACKGROUND", (0, 0), (-1, -1), LINE)])),
        Spacer(1, 3),
    ])


def bullet(text, st):
    return Paragraph(f"- {text}", st["bullet"])


def entry_header(title, date, subtitle, location, st):
    left = [Paragraph(title, st["role"]), Paragraph(subtitle, st["company"])]
    right = [Paragraph(date, st["date"]), Paragraph(location, st["date"])]
    table = Table([[left, right]], colWidths=[126 * mm, 55 * mm], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return table


def project_header(title, date, st):
    table = Table([[Paragraph(title, st["project"]), Paragraph(date, st["date"])]], colWidths=[135 * mm, 46 * mm])
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
    ]))
    return table


def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, A4[1] - 5 * mm, A4[0], 5 * mm, fill=1, stroke=0)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawCentredString(A4[0] / 2, 8 * mm, f"Samuel Armando Napitu | Page {doc.page}")
    canvas.restoreState()


def build(lang):
    data = COPY[lang]
    st = styles()
    path = ROOT / data["filename"]
    doc = BaseDocTemplate(
        str(path),
        pagesize=A4,
        rightMargin=14.5 * mm,
        leftMargin=14.5 * mm,
        topMargin=15 * mm,
        bottomMargin=14 * mm,
        title=f"Samuel Armando Napitu - CV ({lang.upper()})",
        author="Samuel Armando Napitu",
        subject="Data Scientist, Data Governance, and Business Intelligence",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="cv", frames=[frame], onPage=on_page)])

    linkedin = "linkedin.com/in/samuel-armando-4149a4247"
    github = "github.com/sam01149"
    contact = (
        f"{data['location']} | +62 812-6059-2450 | samuelarmando93@gmail.com<br/>"
        f'<link href="https://www.{linkedin}/" color="#173A70">{linkedin}</link> | '
        f'<link href="https://{github}" color="#173A70">{github}</link>'
    )
    story = [
        Paragraph("SAMUEL ARMANDO NAPITU", st["name"]),
        Paragraph(contact, st["contact"]),
        Spacer(1, 4),
        section_heading(data["summary_title"], st),
        Paragraph(data["summary"], st["body"]),
        section_heading(data["skills_title"], st),
    ]

    skills_rows = []
    for label, values in data["skills"]:
        skills_rows.append([Paragraph(label, st["label"]), Paragraph(values, st["body"])])
    skills_table = Table(skills_rows, colWidths=[42 * mm, 139 * mm])
    skills_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2),
        ("TOPPADDING", (0, 0), (-1, -1), 1),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
    ]))
    story.append(skills_table)
    story.append(section_heading(data["experience_title"], st))

    for item in data["experience"]:
        parts = [entry_header(item["role"], item["date"], item["company"], item["location"], st)]
        parts.extend(bullet(text, st) for text in item["bullets"])
        parts.append(Spacer(1, 4))
        story.append(KeepTogether(parts))

    story.append(section_heading(data["projects_title"], st))
    first_project = data["projects"][0]
    first_parts = [project_header(first_project["title"], first_project["date"], st), Paragraph(first_project["stack"], st["stack"])]
    first_parts.extend(bullet(text, st) for text in first_project["bullets"])
    story.append(KeepTogether(first_parts))
    story.append(PageBreak())
    story.append(Paragraph("SAMUEL ARMANDO NAPITU", ParagraphStyle("Page2Name", parent=st["name"], fontSize=14, leading=16, spaceAfter=1)))
    story.append(Paragraph("DATA SCIENCE | DATA GOVERNANCE | BUSINESS INTELLIGENCE", st["contact"]))
    story.append(Spacer(1, 4))
    story.append(section_heading(data["projects_continued"], st))

    for project in data["projects"][1:]:
        parts = [project_header(project["title"], project["date"], st), Paragraph(project["stack"], st["stack"])]
        parts.extend(bullet(text, st) for text in project["bullets"])
        parts.append(Spacer(1, 6))
        story.append(KeepTogether(parts))

    story.extend([
        section_heading(data["education_title"], st),
        entry_header(data["education"], data["education_meta"].split(" | ")[0], data["education_meta"].split(" | ")[1], "Jakarta, Indonesia", st),
        section_heading(data["cert_title"], st),
    ])
    story.extend(bullet(item, st) for item in data["certs"])
    story.extend([
        section_heading(data["leadership_title"], st),
        Paragraph(data["leadership"], st["body"]),
    ])
    doc.build(story)
    return path


if __name__ == "__main__":
    for language in ("en", "id"):
        print(build(language))
