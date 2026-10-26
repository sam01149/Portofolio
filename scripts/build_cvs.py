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
BLUE = colors.HexColor("#1F4E79")


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


COPY = {
    "en": {
        "filename": "CV_Samuel_Armando_Napitu_EN.pdf",
        "location": "South Jakarta, Indonesia",
        "summary_heading": "SUMMARY",
        "summary": (
            "BNSP-certified Data Scientist and Information Systems undergraduate at Telkom University Jakarta "
            "with a GPA of 3.69/4.00. Experienced in data governance, metadata management, data pipelines, "
            "business intelligence, and application development using Python, SQL, Power BI, and web technologies."
        ),
        "skills_heading": "SKILLS",
        "skills": [
            ("Programming", "Python, SQL, JavaScript, PHP, HTML/CSS"),
            ("Data & Machine Learning", "Pandas, NumPy, Scikit-learn, CRISP-DM, data quality audit"),
            ("Business Intelligence", "Power BI, Power Query, Power Automate"),
            ("Data Governance", "Metadata management, naming convention audit, SharePoint"),
            ("Development", "Next.js, Laravel, Node.js, RESTful API, Streamlit"),
            ("Database & Tools", "MySQL, Supabase, Redis, Git/GitHub, Vercel, Microsoft Entra"),
        ],
        "experience_heading": "EXPERIENCE",
        "experience": [
            {
                "title": "Data Scientist Intern - PT Telkom Indonesia",
                "date": "August 2026 - October 2026",
                "meta": "Chapter AI & Experience | Digital Product Division | South Jakarta, Indonesia",
                "bullets": [
                    "Built a metadata catalog pipeline for 26,713 SharePoint repository entries.",
                    "Audited metadata quality and naming convention compliance and supported inventory automation using Power Automate and Power Query.",
                    "Developed a Talent Dashboard portal prototype with Microsoft Entra authentication and Power BI integration using Next.js.",
                ],
            },
            {
                "title": "Business Process Analyst & UI Designer Intern - PT Estima Reka Sakti",
                "date": "September 2024 - June 2025",
                "meta": "South Tangerang, Indonesia",
                "bullets": [
                    "Mapped construction quality-control processes through field research and identified operational bottlenecks.",
                    "Delivered an accepted web-based monitoring system design covering use cases, relational ERD, and UI wireframes.",
                ],
            },
        ],
        "projects_heading": "PROJECTS",
        "projects": [
            {
                "title": "Daun Merah - Forex Intelligence PWA",
                "date": "May 2026 - Present",
                "meta": "Personal Project | Vanilla JS | Node.js | Redis | Vercel",
                "bullets": [
                    "Designed and developed a serverless Progressive Web App integrating macroeconomic data, technical indicators, and market news for forex analysis.",
                    "Implemented Redis caching and distributed locking across data sources including FRED, CFTC, Yahoo Finance, and ECB.",
                    "Integrated multiple LLM providers with fallback and timeout mechanisms to improve service reliability.",
                ],
            },
            {
                "title": "Machine Learning-Based Customer Segmentation",
                "date": "April 2026",
                "meta": "BNSP Data Scientist | Python | Pandas | Scikit-learn | Streamlit",
                "bullets": [
                    "Built a customer segmentation model using the CRISP-DM workflow, including preprocessing, EDA, modeling, and GridSearchCV optimization.",
                    "Developed a Streamlit application to automate segment predictions for new customers.",
                    "Presented the methodology as an invited speaker at Telkom University's Data Science Bukan Cuma Coding webinar in June 2026.",
                ],
            },
            {
                "title": "National Airline Management Application",
                "date": "December 2024",
                "meta": "Academic Project | PHP | Laravel | MySQL",
                "bullets": [
                    "Built modules for flight scheduling, passenger management, and ticket booking using Laravel MVC and relational database design.",
                    "Implemented form validation, middleware-based route protection, and table relationships following Laravel conventions.",
                ],
            },
        ],
        "certifications_heading": "CERTIFICATIONS",
        "certifications": [
            ("Data Scientist Certification, LSP Data / BNSP", "April 2026"),
            ("IBM Data Science Professional Certificate, Coursera", "March 2026"),
        ],
        "organization_heading": "ORGANIZATION",
        "organization_title": "Christian Student Fellowship, Telkom University Jakarta - Committee Chairperson, Easter Retreat",
        "organization_date": "May 2025",
        "organization_bullets": [
            "Led 56 team members and managed an IDR 36 million budget for a three-day program.",
            "Coordinated schedules, divisions, communication, and risk management to keep the program on track.",
        ],
        "education_heading": "EDUCATION",
        "education_title": "Telkom University",
        "education_date": "2023 - Present",
        "education_meta": "Bachelor of Information Systems | GPA: 3.69 / 4.00",
    },
    "id": {
        "filename": "CV_Samuel_Armando_Napitu_ID.pdf",
        "location": "Jakarta Selatan, Indonesia",
        "summary_heading": "RINGKASAN",
        "summary": (
            "Data Scientist tersertifikasi BNSP dan mahasiswa S1 Sistem Informasi Telkom University Jakarta "
            "dengan IPK 3,69/4,00. Berpengalaman dalam data governance, metadata management, data pipeline, "
            "business intelligence, dan pengembangan aplikasi menggunakan Python, SQL, Power BI, dan teknologi web."
        ),
        "skills_heading": "KEAHLIAN",
        "skills": [
            ("Pemrograman", "Python, SQL, JavaScript, PHP, HTML/CSS"),
            ("Data & Machine Learning", "Pandas, NumPy, Scikit-learn, CRISP-DM, audit kualitas data"),
            ("Business Intelligence", "Power BI, Power Query, Power Automate"),
            ("Data Governance", "Metadata management, audit konvensi penamaan, SharePoint"),
            ("Pengembangan", "Next.js, Laravel, Node.js, RESTful API, Streamlit"),
            ("Database & Tools", "MySQL, Supabase, Redis, Git/GitHub, Vercel, Microsoft Entra"),
        ],
        "experience_heading": "PENGALAMAN",
        "experience": [
            {
                "title": "Data Scientist Intern - PT Telkom Indonesia",
                "date": "Agustus 2026 - Oktober 2026",
                "meta": "Chapter AI & Experience | Divisi Digital Product | Jakarta Selatan, Indonesia",
                "bullets": [
                    "Membangun pipeline katalog metadata untuk 26.713 entri repositori SharePoint.",
                    "Mengaudit kualitas metadata dan kepatuhan konvensi penamaan serta mendukung otomatisasi inventaris menggunakan Power Automate dan Power Query.",
                    "Mengembangkan prototipe portal Talent Dashboard dengan autentikasi Microsoft Entra dan integrasi Power BI menggunakan Next.js.",
                ],
            },
            {
                "title": "Business Process Analyst & UI Designer Intern - PT Estima Reka Sakti",
                "date": "September 2024 - Juni 2025",
                "meta": "Tangerang Selatan, Indonesia",
                "bullets": [
                    "Memetakan proses quality control konstruksi melalui riset lapangan dan mengidentifikasi hambatan operasional.",
                    "Menghasilkan rancangan sistem monitoring berbasis web yang diterima klien, mencakup use case, ERD relasional, dan UI wireframe.",
                ],
            },
        ],
        "projects_heading": "PROYEK",
        "projects": [
            {
                "title": "Daun Merah - Forex Intelligence PWA",
                "date": "Mei 2026 - Sekarang",
                "meta": "Proyek Pribadi | Vanilla JS | Node.js | Redis | Vercel",
                "bullets": [
                    "Merancang dan mengembangkan Progressive Web App serverless yang mengintegrasikan data makroekonomi, indikator teknikal, dan berita pasar untuk analisis forex.",
                    "Mengimplementasikan Redis caching dan distributed locking untuk sumber data termasuk FRED, CFTC, Yahoo Finance, dan ECB.",
                    "Mengintegrasikan beberapa penyedia LLM dengan mekanisme fallback dan timeout untuk meningkatkan keandalan layanan.",
                ],
            },
            {
                "title": "Segmentasi Pelanggan Berbasis Machine Learning",
                "date": "April 2026",
                "meta": "BNSP Data Scientist | Python | Pandas | Scikit-learn | Streamlit",
                "bullets": [
                    "Membangun model segmentasi pelanggan menggunakan alur CRISP-DM, mencakup praproses, EDA, pemodelan, dan optimasi GridSearchCV.",
                    "Mengembangkan aplikasi Streamlit untuk mengotomatiskan prediksi segmen pelanggan baru.",
                    "Mempresentasikan metodologi sebagai pembicara undangan pada webinar Data Science Bukan Cuma Coding Telkom University pada Juni 2026.",
                ],
            },
            {
                "title": "Aplikasi Manajemen Maskapai Penerbangan Nasional",
                "date": "Desember 2024",
                "meta": "Proyek Akademik | PHP | Laravel | MySQL",
                "bullets": [
                    "Membangun modul penjadwalan penerbangan, manajemen penumpang, dan pemesanan tiket menggunakan Laravel MVC dan basis data relasional.",
                    "Mengimplementasikan validasi formulir, proteksi route berbasis middleware, dan relasi tabel sesuai konvensi Laravel.",
                ],
            },
        ],
        "certifications_heading": "SERTIFIKASI",
        "certifications": [
            ("Sertifikasi Data Scientist, LSP Data / BNSP", "April 2026"),
            ("IBM Data Science Professional Certificate, Coursera", "Maret 2026"),
        ],
        "organization_heading": "ORGANISASI",
        "organization_title": "Persekutuan Mahasiswa Kristen Telkom University Jakarta - Ketua Pelaksana Retreat Paskah",
        "organization_date": "Mei 2025",
        "organization_bullets": [
            "Memimpin 56 anggota tim dan mengelola anggaran Rp36 juta untuk program tiga hari.",
            "Mengoordinasikan jadwal, divisi, komunikasi, dan manajemen risiko agar program berjalan sesuai rencana.",
        ],
        "education_heading": "PENDIDIKAN",
        "education_title": "Telkom University",
        "education_date": "2023 - Sekarang",
        "education_meta": "S1 Sistem Informasi | IPK: 3,69 / 4,00",
    },
}


def make_styles():
    base = getSampleStyleSheet()
    return {
        "name": ParagraphStyle("Name", parent=base["Normal"], fontName="Calibri-Bold", fontSize=20, leading=22, alignment=TA_CENTER, spaceAfter=6),
        "contact": ParagraphStyle("Contact", parent=base["Normal"], fontName="Calibri", fontSize=9, leading=10.5, alignment=TA_CENTER),
        "section": ParagraphStyle("Section", parent=base["Normal"], fontName="Calibri-Bold", fontSize=11, leading=12, spaceBefore=12, spaceAfter=3),
        "body": ParagraphStyle("Body", parent=base["Normal"], fontName="Calibri", fontSize=10, leading=12.4, alignment=TA_LEFT),
        "title": ParagraphStyle("Title", parent=base["Normal"], fontName="Calibri-Bold", fontSize=11, leading=12.5),
        "date": ParagraphStyle("Date", parent=base["Normal"], fontName="Calibri", fontSize=10, leading=12.5, alignment=TA_RIGHT),
        "meta": ParagraphStyle("Meta", parent=base["Normal"], fontName="Calibri-Italic", fontSize=10, leading=11.5, spaceAfter=3),
        "bullet": ParagraphStyle("Bullet", parent=base["Normal"], fontName="Calibri", fontSize=10, leading=12.2, leftIndent=20, firstLineIndent=-10, bulletIndent=7, spaceAfter=1.5),
    }


def section_heading(text, styles, width):
    line = Table([[""]], colWidths=[width], rowHeights=[0.7])
    line.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), BLUE)]))
    return KeepTogether([Paragraph(text, styles["section"]), line, Spacer(1, 5)])


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
    return Paragraph(text, styles["bullet"], bulletText="•")


def build(language):
    data = COPY[language]
    styles = make_styles()
    output = ROOT / data["filename"]
    doc = BaseDocTemplate(
        str(output), pagesize=LETTER,
        leftMargin=0.69 * inch, rightMargin=0.69 * inch,
        topMargin=0.62 * inch, bottomMargin=0.58 * inch,
        title=f"Samuel Armando Napitu - CV ({language.upper()})",
        author="Samuel Armando Napitu",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates(PageTemplate(id="cv", frames=[frame]))

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
        block.append(Spacer(1, 4))
        story.append(KeepTogether(block))

    story.append(section_heading(data["projects_heading"], styles, doc.width))
    for item in data["projects"]:
        block = [dated_title(item["title"], item["date"], styles, doc.width), Paragraph(item["meta"], styles["meta"])]
        block.extend(bullet(text, styles) for text in item["bullets"])
        block.append(Spacer(1, 4))
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
