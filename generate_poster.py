import os
import requests

def generate_qr_codes():
    print("Generating QR codes...")
    urls = {
        "website": "https://fil-m.github.io/stina-3d/",
        "channel": "https://t.me/stina3ddruku",
        "organizer": "https://t.me/robosapiens8"
    }
    
    # Try using qrcode library if installed
    try:
        import qrcode
        print("Using local 'qrcode' library.")
        for name, url in urls.items():
            qr = qrcode.QRCode(version=1, box_size=10, border=1)
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(f"assets/qr_{name}.png")
            print(f"Generated assets/qr_{name}.png")
    except ImportError:
        print("Local 'qrcode' library not found. Fetching from QR Server API...")
        os.makedirs("assets", exist_ok=True)
        for name, url in urls.items():
            api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={url}"
            try:
                response = requests.get(api_url, timeout=10)
                if response.status_code == 200:
                    with open(f"assets/qr_{name}.png", "wb") as f:
                        f.write(response.content)
                    print(f"Downloaded assets/qr_{name}.png")
                else:
                    print(f"Failed to fetch QR code for {name}: HTTP {response.status_code}")
            except Exception as e:
                print(f"Error fetching QR code for {name}: {e}")

def create_html_poster():
    print("Creating HTML poster...")
    html_content = """<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Стіна 3D — Афіша А4</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        /* CSS reset & variables optimized for B&W print */
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
            color: #000000;
            background: #ffffff;
            line-height: 1.4;
            padding: 0;
            -webkit-print-color-adjust: exact;
            print-color-adjust: exact;
        }
        
        /* A4 Page size settings */
        @page {
            size: A4;
            margin: 15mm;
        }
        
        .poster-container {
            width: 100%;
            max-width: 210mm; /* A4 width */
            min-height: 297mm; /* A4 height */
            margin: 0 auto;
            padding: 0;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        /* Top Header styling */
        .header {
            text-align: center;
            border-bottom: 3px solid #000;
            padding-bottom: 8px;
            margin-bottom: 24px;
        }
        .header-badge {
            display: inline-block;
            border: 2px solid #000;
            padding: 4px 12px;
            font-weight: 700;
            font-size: 13px;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 12px;
        }
        .header h1 {
            font-size: 42px;
            font-weight: 900;
            letter-spacing: -1px;
            text-transform: uppercase;
            line-height: 1;
            margin-bottom: 8px;
        }
        .header h1 span {
            background: #000;
            color: #fff;
            padding: 0 8px;
            display: inline-block;
        }
        .header .tagline {
            font-size: 18px;
            font-weight: 600;
            margin-top: 4px;
        }

        /* Main content layout */
        .main-content {
            flex-grow: 1;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .section-box {
            border: 2px solid #000;
            padding: 16px;
            background: #ffffff;
        }
        
        .section-title {
            font-size: 20px;
            font-weight: 800;
            text-transform: uppercase;
            border-bottom: 2px solid #000;
            padding-bottom: 4px;
            margin-bottom: 12px;
            display: inline-block;
        }

        /* Mission / What we do */
        .mission-grid {
            display: flex;
            gap: 16px;
            margin-bottom: 4px;
        }
        .mission-item {
            flex: 1;
        }
        .mission-item h3 {
            font-size: 16px;
            font-weight: 700;
            margin-bottom: 4px;
        }
        .mission-item p {
            font-size: 14px;
            color: #333;
        }

        /* Offer list */
        .list-items {
            list-style: none;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px 24px;
        }
        .list-items li {
            position: relative;
            padding-left: 20px;
            font-size: 14px;
        }
        .list-items li::before {
            content: "▪";
            position: absolute;
            left: 0;
            top: 0;
            font-size: 16px;
        }
        .list-items li strong {
            display: block;
            font-size: 15px;
            font-weight: 700;
            margin-bottom: 2px;
        }

        /* Civic offer highlight box */
        .highlight-box {
            border: 2px dashed #000;
            background: #f9f9f9;
            padding: 14px;
            text-align: center;
            margin-top: 4px;
        }
        .highlight-box h3 {
            font-size: 18px;
            font-weight: 800;
            text-transform: uppercase;
            margin-bottom: 6px;
        }
        .highlight-box p {
            font-size: 15px;
            font-weight: 600;
        }

        /* QR Codes section */
        .qr-section {
            border-top: 3px double #000;
            padding-top: 20px;
            margin-top: 20px;
        }
        .qr-title {
            text-align: center;
            font-size: 16px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 16px;
        }
        .qr-grid {
            display: flex;
            justify-content: space-around;
            align-items: flex-start;
            gap: 16px;
        }
        .qr-card {
            flex: 1;
            text-align: center;
            max-width: 140px;
        }
        .qr-image-wrapper {
            border: 2px solid #000;
            padding: 4px;
            background: #fff;
            display: inline-block;
            margin-bottom: 8px;
        }
        .qr-card img {
            width: 110px;
            height: 110px;
            display: block;
        }
        .qr-card h4 {
            font-size: 13px;
            font-weight: 700;
            text-transform: uppercase;
            margin-bottom: 4px;
        }
        .qr-card p {
            font-size: 11px;
            color: #444;
            line-height: 1.2;
        }

        /* Footer info */
        .footer-note {
            text-align: center;
            font-size: 12px;
            font-weight: 600;
            margin-top: 16px;
            border-top: 1px solid #ddd;
            padding-top: 8px;
        }

        /* Non-printable preview info banner */
        .no-print-banner {
            background: #f0f0f0;
            border: 1px solid #ccc;
            padding: 12px;
            margin-bottom: 20px;
            text-align: center;
            font-size: 14px;
        }
        .no-print-banner button {
            background: #000;
            color: #fff;
            border: none;
            padding: 8px 16px;
            font-weight: 700;
            cursor: pointer;
            margin-top: 8px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .no-print-banner button:hover {
            background: #333;
        }

        @media print {
            .no-print-banner {
                display: none !important;
            }
            body {
                padding: 0;
            }
            .poster-container {
                min-height: auto;
            }
        }
    </style>
</head>
<body>

    <div class="no-print-banner">
        <strong>Афіша підготовлена до друку на форматі A4 (чорно-біла).</strong><br>
        Відкрийте цю сторінку в браузері, натисніть кнопку нижче або комбінацію клавіш <strong>Ctrl + P</strong> і виберіть принтер або збереження в PDF.<br>
        <button onclick="window.print()">Друк / Зберегти як PDF</button>
    </div>

    <div class="poster-container">
        <div class="header">
            <div class="header-badge">Проект Ukrainer in Karlsruhe e.V.</div>
            <h1>Стіна <span>3D</span> друкарня</h1>
            <p class="tagline">Бюджетна волонтерська 3D-ферма під егідою «Ukrainer in Karlsruhe e.V.»</p>
        </div>

        <div class="main-content">
            <div class="section-box">
                <div class="section-title">Хто ми та що робимо?</div>
                <div class="mission-grid">
                    <div class="mission-item">
                        <h3>🏥 Медичні компоненти</h3>
                        <p>Безкоштовно друкуємо деталі для протезів, хірургічні інструменти та засоби реабілітації як гуманітарну допомогу для шпиталів в Україні в межах волонтерської мережі <strong>Друкармія</strong>.</p>
                    </div>
                    <div class="mission-item">
                        <h3>🛠️ Власна 3D-ферма</h3>
                        <p>Починали з одного принтера, а зараз звели стіну з 8 принтерів завдяки допомозі спільноти ферайну «Українці в Карлсруе».</p>
                    </div>
                </div>
            </div>

            <div class="section-box">
                <div class="section-title">Як підтримати наш проект?</div>
                <ul class="list-items">
                    <li>
                        <strong>🧵 Пластик (Filament)</strong>
                        Маєте невикористаний пластик (PLA, PETG)? Приймаємо залишки котушок або цілі матеріали для волонтерського друку.
                    </li>
                    <li>
                        <strong>🔌 Обладнання та деталі</strong>
                        Потрібні блоки живлення (12/24V), Raspberry Pi, крокові двигуни та будь-які запчастини для 3D-принтерів.
                    </li>
                    <li>
                        <strong>🏠 Місце та розетка</strong>
                        Шукаємо додатковий простір у Карлсруе з підключенням до електрики для розширення нашої стіни принтерів.
                    </li>
                    <li>
                        <strong>🤝 Волонтерство та медіа</strong>
                        Потрібні люди для налаштування принтерів, логістики готової продукції та поширення інформації.
                    </li>
                </ul>
            </div>

            <div class="highlight-box">
                <h3>Друк для допомоги та суспільних потреб</h3>
                <p>Приймаємо пластик на друк медичної допомоги, а також на суспільні та освітні потреби. Якщо вам потрібно надрукувати власну деталь — ми допоможемо виготовити її з вашого матеріалу, а залишки пластику використаємо для медичних волонтерських виробів.</p>
            </div>
        </div>

        <div class="qr-section">
            <div class="qr-title">Дізнатися більше, приєднатися або зв'язатися з нами:</div>
            <div class="qr-grid">
                <div class="qr-card">
                    <div class="qr-image-wrapper">
                        <img src="assets/qr_website.png" alt="QR Website">
                    </div>
                    <h4>Сайт проекту</h4>
                    <p>Детальна інформація та опис нашої роботи</p>
                </div>
                
                <div class="qr-card">
                    <div class="qr-image-wrapper">
                        <img src="assets/qr_channel.png" alt="QR Telegram Channel">
                    </div>
                    <h4>Наш Telegram</h4>
                    <p>Анонси, новини друкарні та звіти про роботу</p>
                </div>

                <div class="qr-card">
                    <div class="qr-image-wrapper">
                        <img src="assets/qr_organizer.png" alt="QR Telegram Contact">
                    </div>
                    <h4>Зв'язок</h4>
                    <p>Напишіть організатору особисто: @robosapiens8</p>
                </div>
            </div>
        </div>

        <div class="footer-note">
            Стіна 3D · Ein Projekt des Ukrainer in Karlsruhe e.V.<br>
            <span style="font-size: 10px; font-weight: normal; color: #666; display: block; margin-top: 4px;">Impressum: Ukrainer in Karlsruhe e.V., Gellertstraße 14, 76185 Karlsruhe | VR 701389 (Amtsgericht Mannheim) | welcomeinkarlsruhe@gmail.com</span>
        </div>
    </div>

</body>
</html>
"""
    with open("poster.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Created poster.html")

def create_pdf_poster():
    print("Creating PDF poster...")
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.units import mm
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib import colors
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
    except ImportError:
        print("Reportlab not available. Cannot generate PDF directly. Use HTML poster and print as PDF.")
        return

    # Check for Arial font on Windows
    arial_path = "C:\\Windows\\Fonts\\arial.ttf"
    arial_bold_path = "C:\\Windows\\Fonts\\arialbd.ttf"
    
    if os.path.exists(arial_path) and os.path.exists(arial_bold_path):
        pdfmetrics.registerFont(TTFont('Arial', arial_path))
        pdfmetrics.registerFont(TTFont('Arial-Bold', arial_bold_path))
        FONT_NORMAL = 'Arial'
        FONT_BOLD = 'Arial-Bold'
        print("Using system Arial font for Cyrillic support.")
    else:
        FONT_NORMAL = 'Helvetica'
        FONT_BOLD = 'Helvetica-Bold'
        print("Arial font not found. Falling back to Helvetica (Cyrillic characters might not render).")

    doc = SimpleDocTemplate(
        "stina_3d_poster_a4.pdf",
        pagesize=A4,
        rightMargin=15*mm,
        leftMargin=15*mm,
        topMargin=15*mm,
        bottomMargin=15*mm
    )

    styles = getSampleStyleSheet()

    # Define custom styles
    title_p1_style = ParagraphStyle('T1', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=32, leading=36, alignment=2)
    title_p2_style = ParagraphStyle('T2', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=32, leading=36, alignment=1)
    
    badge_style = ParagraphStyle('Badge', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=10, leading=12, alignment=1)
    tagline_style = ParagraphStyle('Tagline', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=13, leading=16, alignment=1)
    
    sec_title_style = ParagraphStyle('SecTitle', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=13, leading=15, spaceAfter=4)
    body_style = ParagraphStyle('BodyTextCustom', parent=styles['Normal'], fontName=FONT_NORMAL, fontSize=9.5, leading=12.5)
    
    highlight_title_style = ParagraphStyle('HighlightTitle', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=13, leading=15, alignment=1, spaceAfter=3)
    highlight_body_style = ParagraphStyle('HighlightBody', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=10.5, leading=13.5, alignment=1)
    
    qr_title_style = ParagraphStyle('QRTitle', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=11, leading=13, alignment=1)
    qr_label_style = ParagraphStyle('QRLabel', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=9.5, leading=11, alignment=1)
    qr_desc_style = ParagraphStyle('QRDesc', parent=styles['Normal'], fontName=FONT_NORMAL, fontSize=8, leading=10, alignment=1)
    
    footer_style = ParagraphStyle('FooterStyle', parent=styles['Normal'], fontName=FONT_NORMAL, fontSize=8.5, leading=11, alignment=1, textColor=colors.HexColor('#555555'))

    story = []

    # 1. Header Badge
    badge_p = Paragraph("ВОЛОНТЕРСЬКИЙ ПРОЕКТ · КАРЛСРУЕ", badge_style)
    badge_table = Table([[badge_p]], colWidths=[72*mm])
    badge_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOX', (0,0), (-1,-1), 1.5, colors.black),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    badge_table.hAlign = 'CENTER'
    story.append(badge_table)
    story.append(Spacer(1, 4*mm))

    # 2. Main Title: СТІНА 3D (styled as logo)
    title_p1 = Paragraph("СТІНА", title_p1_style)
    title_p2 = Paragraph("<font color=white>3D</font>", title_p2_style)
    # Col widths sum to 75mm. To keep them looking aligned, we can adjust sizes.
    title_table = Table([[title_p1, title_p2]], colWidths=[45*mm, 20*mm])
    title_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BACKGROUND', (1,0), (1,0), colors.black),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (1,0), (1,0), 6),
        ('RIGHTPADDING', (1,0), (1,0), 6),
    ]))
    title_table.hAlign = 'CENTER'
    story.append(title_table)
    story.append(Spacer(1, 3*mm))

    # Tagline
    story.append(Paragraph("Бюджетна волонтерська 3D-ферма під егідою «Ukrainer in Karlsruhe e.V.»", tagline_style))
    story.append(Spacer(1, 3*mm))

    # Thin line under header
    line_table = Table([[""]], colWidths=[180*mm], rowHeights=[2])
    line_table.setStyle(TableStyle([
        ('LINEBELOW', (0,0), (-1,-1), 2, colors.black),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(line_table)
    story.append(Spacer(1, 6*mm))

    # 3. Section 1: Who we are
    sec1_content = [
        [Paragraph("ХТО МИ ТА ЩО РОБИМО?", sec_title_style), ""],
        [
            Paragraph("<b>🏥 Медичні компоненти</b><br/>Безкоштовно друкуємо деталі для протезів, хірургічні інструменти та засоби реабілітації як гуманітарну допомогу для шпиталів в Україні в межах волонтерської мережі <b>Друкармія</b>.", body_style),
            Paragraph("<b>🛠️ Власна 3D-ферма</b><br/>Починали з одного принтера, а зараз звели стіну з 8 принтерів завдяки допомозі спільноти ферайну «Українці в Карлсруе».", body_style)
        ]
    ]
    sec1_table = Table(sec1_content, colWidths=[88*mm, 88*mm])
    sec1_table.setStyle(TableStyle([
        ('SPAN', (0,0), (1,0)),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOX', (0,0), (-1,-1), 1.5, colors.black),
        ('TOPPADDING', (0,0), (-1,0), 8),
        ('BOTTOMPADDING', (0,0), (-1,0), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,1), (-1,-1), 10),
        ('TOPPADDING', (0,1), (-1,-1), 4),
    ]))
    sec1_table.hAlign = 'CENTER'
    story.append(sec1_table)
    story.append(Spacer(1, 5*mm))

    # 4. Section 2: How to support
    sec2_content = [
        [Paragraph("ЯК ПІДТРИМАТИ НАШ ПРОЕКТ?", sec_title_style), ""],
        [
            Paragraph("<b>🧵 Пластик (Filament)</b><br/>Маєте невикористаний пластик (PLA, PETG)? Приймаємо залишки котушок або цілі матеріали для волонтерського друку.", body_style),
            Paragraph("<b>🔌 Обладнання та деталі</b><br/>Потрібні блоки живлення (12/24V), Raspberry Pi, крокові двигуни та запчастини для 3D-принтерів.", body_style)
        ],
        [
            Paragraph("<b>🏠 Місце та розетка</b><br/>Шукаємо додатковий простір у Карлсруе з підключенням до електрики для розширення нашої стіни принтерів.", body_style),
            Paragraph("<b>🤝 Волонтерство та медіа</b><br/>Потрібні люди для налаштування принтерів, логістики готової продукції та поширення інформації.", body_style)
        ]
    ]
    sec2_table = Table(sec2_content, colWidths=[88*mm, 88*mm])
    sec2_table.setStyle(TableStyle([
        ('SPAN', (0,0), (1,0)),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOX', (0,0), (-1,-1), 1.5, colors.black),
        ('TOPPADDING', (0,0), (-1,0), 8),
        ('BOTTOMPADDING', (0,0), (-1,0), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,-1), (-1,-1), 10),
        ('TOPPADDING', (0,1), (-1,-1), 4),
        ('BOTTOMPADDING', (0,1), (-1,-2), 6),
    ]))
    sec2_table.hAlign = 'CENTER'
    story.append(sec2_table)
    story.append(Spacer(1, 5*mm))

    # 5. Highlight box: Civic print / donation print
    civic_content = [
        [Paragraph("ДРУК ДЛЯ ДОПОМОГИ ТА СУСПІЛЬНИХ ПОТРЕБ", highlight_title_style)],
        [Paragraph("Приймаємо пластик на друк медичної допомоги, а також на суспільні та освітні потреби. Якщо вам потрібно надрукувати власну деталь — ми допоможемо виготовити її з вашого матеріалу, а залишки пластику використаємо для медичних волонтерських виробів.", highlight_body_style)]
    ]
    civic_table = Table(civic_content, colWidths=[176*mm])
    civic_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOX', (0,0), (-1,-1), 1.5, colors.black),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f2f2f2')),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ]))
    civic_table.hAlign = 'CENTER'
    story.append(civic_table)
    story.append(Spacer(1, 6*mm))

    # Helper function to frame images tightly
    def make_boxed_image(path):
        img = Image(path, width=28*mm, height=28*mm)
        t = Table([[img]], colWidths=[30*mm], rowHeights=[30*mm])
        t.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('BOX', (0,0), (-1,-1), 1, colors.black),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ]))
        return t

    # 6. QR Section Title
    story.append(Paragraph("ДІЗНАТИСЯ БІЛЬШЕ, ПРИЄДНАТИСЯ АБО ЗВ'ЯЗАТИСЯ З НАМИ:", qr_title_style))
    story.append(Spacer(1, 4*mm))

    # QR Codes Grid
    qr1 = make_boxed_image("assets/qr_website.png")
    qr2 = make_boxed_image("assets/qr_channel.png")
    qr3 = make_boxed_image("assets/qr_organizer.png")

    qr_table_data = [
        [qr1, qr2, qr3],
        [
            Paragraph("САЙТ ПРОЕКТУ", qr_label_style),
            Paragraph("НАШ TELEGRAM", qr_label_style),
            Paragraph("ЗВ'ЯЗОК", qr_label_style)
        ],
        [
            Paragraph("Детальна інформація та опис нашої роботи", qr_desc_style),
            Paragraph("Анонси, новини друкарні та звіти про роботу", qr_desc_style),
            Paragraph("Напишіть організатору особисто: @robosapiens8", qr_desc_style)
        ]
    ]
    qr_table = Table(qr_table_data, colWidths=[58*mm, 58*mm, 58*mm])
    qr_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,0), 3),
        ('BOTTOMPADDING', (0,1), (-1,1), 1),
        ('TOPPADDING', (0,1), (-1,-1), 3),
    ]))
    qr_table.hAlign = 'CENTER'
    story.append(qr_table)
    story.append(Spacer(1, 6*mm))

    # Separator line
    sep_table = Table([[""]], colWidths=[176*mm], rowHeights=[1])
    sep_table.setStyle(TableStyle([
        ('LINEBELOW', (0,0), (-1,-1), 1, colors.HexColor('#dddddd')),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(sep_table)
    story.append(Spacer(1, 4*mm))

    # 7. Footer
    footer_p = Paragraph("Стіна 3D · Ein Projekt des Ukrainer in Karlsruhe e.V.<br/><font size=7.5 color='#666666'>Impressum: Ukrainer in Karlsruhe e.V., Gellertstraße 14, 76185 Karlsruhe | VR 701389 (Amtsgericht Mannheim) | welcomeinkarlsruhe@gmail.com</font>", footer_style)
    story.append(footer_p)

    doc.build(story)
    print("Created stina_3d_poster_a4.pdf")

if __name__ == "__main__":
    os.makedirs("assets", exist_ok=True)
    generate_qr_codes()
    create_html_poster()
    create_pdf_poster()
