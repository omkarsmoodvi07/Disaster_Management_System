import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=140, bottom=140, left=180, right=180):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def create_document():
    doc = Document()
    
    # Page setup - 1 inch margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        
    # Styles
    navy = RGBColor(26, 54, 93)      # #1A365D Primary
    crimson = RGBColor(197, 48, 48)  # #C53030 Danger/Emergency
    teal = RGBColor(43, 108, 176)    # #2B6CB0 Accent
    charcoal = RGBColor(45, 55, 72)  # #2D3748 Body text
    gray = RGBColor(113, 128, 150)   # #718096 Subtext
    
    # Title Block
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(0)
    title_p.paragraph_format.space_after = Pt(4)
    title_run = title_p.add_run("DISASTER MANAGEMENT PLATFORM (DMS)")
    title_run.font.name = 'Calibri'
    title_run.font.size = Pt(26)
    title_run.font.bold = True
    title_run.font.color.rgb = navy
    
    sub_p = doc.add_paragraph()
    sub_p.paragraph_format.space_before = Pt(0)
    sub_p.paragraph_format.space_after = Pt(16)
    sub_run = sub_p.add_run("Full Technical Dossier, Architectural Blueprint & Presentation Guide")
    sub_run.font.name = 'Calibri'
    sub_run.font.size = Pt(14)
    sub_run.font.color.rgb = crimson
    sub_run.font.bold = True

    # Meta Table / Document Overview
    meta_table = doc.add_table(rows=4, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_table.autofit = False
    
    meta_data = [
        ("Project Name:", "Real-Time Disaster Management & Emergency Coordination WebApp"),
        ("Author / Maintainer:", "Omkar S Moodvi (omkarsmoodvi05@gmail.com / omkarsmoodvi27@gmail.com)"),
        ("System Architecture:", "Full-Stack Distributed System (React 18 + Node.js/Express + MongoDB + FastAPI AI RAG)"),
        ("Document Classification:", "Project Defense, Evaluation & Stakeholder Presentation Manual")
    ]
    
    for i, (label, val) in enumerate(meta_data):
        row = meta_table.rows[i]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width = Inches(2.2)
        c1.width = Inches(4.3)
        set_cell_background(c0, "EDF2F7")
        set_cell_background(c1, "F7FAFC")
        set_cell_margins(c0, 100, 100, 150, 150)
        set_cell_margins(c1, 100, 100, 150, 150)
        
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_after = Pt(2)
        r0 = p0.add_run(label)
        r0.font.bold = True
        r0.font.name = 'Calibri'
        r0.font.size = Pt(10)
        r0.font.color.rgb = navy
        
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_after = Pt(2)
        r1 = p1.add_run(val)
        r1.font.name = 'Calibri'
        r1.font.size = Pt(10)
        r1.font.color.rgb = charcoal

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    def add_section_heading(num, title):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(18)
        h.paragraph_format.space_after = Pt(6)
        h.paragraph_format.keep_with_next = True
        r_num = h.add_run(f"QUESTION {num}: ")
        r_num.font.bold = True
        r_num.font.name = 'Calibri'
        r_num.font.size = Pt(14)
        r_num.font.color.rgb = crimson
        
        r_title = h.add_run(title)
        r_title.font.bold = True
        r_title.font.name = 'Calibri'
        r_title.font.size = Pt(14)
        r_title.font.color.rgb = navy
        
        # Horizontal rule simulation
        p_line = doc.add_paragraph()
        p_line.paragraph_format.space_before = Pt(0)
        p_line.paragraph_format.space_after = Pt(10)
        r_line = p_line.add_run("―" * 58)
        r_line.font.color.rgb = teal
        r_line.font.size = Pt(8)

    def add_subheading(title):
        sh = doc.add_paragraph()
        sh.paragraph_format.space_before = Pt(10)
        sh.paragraph_format.space_after = Pt(4)
        sh.paragraph_format.keep_with_next = True
        r = sh.add_run(title)
        r.font.bold = True
        r.font.name = 'Calibri'
        r.font.size = Pt(12)
        r.font.color.rgb = teal

    def add_body(text, bold_prefix=None, space_after=6):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            rb = p.add_run(bold_prefix)
            rb.font.bold = True
            rb.font.name = 'Calibri'
            rb.font.size = Pt(11)
            rb.font.color.rgb = navy
        r = p.add_run(text)
        r.font.name = 'Calibri'
        r.font.size = Pt(11)
        r.font.color.rgb = charcoal
        return p

    def add_bullet(bold_prefix, text):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        rb = p.add_run(bold_prefix + " ")
        rb.font.bold = True
        rb.font.name = 'Calibri'
        rb.font.size = Pt(11)
        rb.font.color.rgb = navy
        r = p.add_run(text)
        r.font.name = 'Calibri'
        r.font.size = Pt(11)
        r.font.color.rgb = charcoal

    # =========================================================================
    # SECTION 1: WHAT IT IS
    # =========================================================================
    add_section_heading("1", "WHAT IT IS")
    add_body(
        "The Disaster Management System (DMS) is a centralized, mission-critical web application engineered to "
        "orchestrate emergency response, real-time incident reporting, disaster resource distribution, and humanitarian relief. "
        "Built to bridge the communication chasm that inevitably emerges during natural calamities and catastrophic emergencies, "
        "DMS serves as an end-to-end command and coordination hub linking affected civilians, emergency rescue personnel, "
        "non-governmental organizations (NGOs), healthcare institutions, and administrative authorities onto a single unified platform."
    )
    
    add_subheading("Core Capabilities at a Glance:")
    add_bullet("Real-Time Crowdsourced Incident Triage:", "Empowers citizens to immediately report emergencies (floods, fires, earthquakes, structural collapses, medical crises) with geotagged GPS coordinates, severity levels, and verifiable photographic evidence.")
    add_bullet("Autonomous Multi-Channel Alert Pipelines:", "Whenever an incident is lodged, the system immediately dispatches automated alerts to Telegram emergency responder groups and broadcast emails to accredited NGOs, police departments, and disaster response teams.")
    add_bullet("GIS Emergency Mapping & Safe Shelter Navigation:", "Interactive geospatial maps integrated with OSRM (Open Source Routing Machine) calculate evacuation paths, display active crisis zones, and pinpoint nearby verified shelters and medical centers.")
    add_bullet("Transparent Humanitarian Aid & Payment Orchestration:", "Facilitates transparent donations for disaster victims, offering both monetary contributions via Razorpay payment gateway with cryptographic HMAC verification, as well as material aid (food rations, clothing, medicines, rescue equipment).")
    add_bullet("Offline-Capable AI Disaster Safety Bot:", "An embedded Retrieval-Augmented Generation (RAG) artificial intelligence assistant trained on NDMA and UNICEF disaster safety guidelines that immediately provides life-saving first-aid steps and national emergency helpline phone numbers.")
    add_bullet("Administrative Governance & Crisis Broadcasting:", "Allows emergency authorities to audit reported incidents, verify donation receipts, track relief disbursements, and publish official public safety broadcasts to dispel rumors and misinformation.")

    # =========================================================================
    # SECTION 2: HOW IT IS (TECH STACK & IMPLEMENTATION)
    # =========================================================================
    add_section_heading("2", "HOW IT IS (TECHNICAL IMPLEMENTATION & TECH STACK)")
    add_body(
        "The project is engineered as a modern, decoupled, multi-tier distributed architecture designed for high availability, "
        "responsive rendering under bandwidth-constrained environments, and rapid incident processing. The application is divided "
        "into three primary technical subsystems: a React Single Page Application (SPA), an Express.js REST API with real-time alerting, "
        "and a Python-powered RAG AI Chatbot service."
    )

    add_subheading("Detailed Technology Matrix:")
    
    tech_rows = [
        ("Frontend Client", "React 18, React Router v6, Redux Toolkit, Tailwind CSS, Bootstrap 5, Spline 3D", "Interactive, responsive user interface with role-based routing, real-time reactive state, rich glassmorphic visuals, and responsive mobile-first views."),
        ("GIS & Mapping", "Leaflet, React-Leaflet, OpenStreetMap, OSRM Routing Engine", "Geospatial visualization of disaster hotspots, relief camps, hospitals, and dynamic point-to-point evacuation route planning."),
        ("Primary Backend", "Node.js (v24), Express.js (v4.19), Multer, Mongoose (v8.5)", "RESTful API microservices handling authentication, incident triage, file storage, donation recording, and administrative data endpoints."),
        ("Database Layer", "MongoDB (Local & Atlas-compatible), Mongoose ODM", "Document database storing user credentials, role taxonomies, disaster incidents, donation ledgers, and emergency announcements."),
        ("Notification & Bot", "Telegram Bot API (node-telegram-bot-api), Nodemailer (Gmail SMTP)", "Real-time, zero-latency push alert pipeline sending instant telegram dispatch cards with photo attachments and email alerts to first responders."),
        ("Payment Gateway", "Razorpay REST API & SDK, Crypto (HMAC SHA-256)", "Secure fund mobilization with dynamic order creation and server-side cryptographic checksum verification for transparent relief funding."),
        ("AI Safety Engine", "FastAPI, Python 3.12, LlamaIndex, Sentence-Transformers, NLTK", "RAG vector database search over NDMA & UNICEF safety manuals with rule-based emergency phone lookup and regex action-verb sanitization.")
    ]

    # Table of Tech Stack
    tech_table = doc.add_table(rows=len(tech_rows) + 1, cols=3)
    tech_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    tech_table.autofit = False
    
    headers = ["Layer / Subsystem", "Technologies & Frameworks", "Role & Engineering Responsibility"]
    col_widths = [Inches(1.8), Inches(2.2), Inches(2.5)]
    
    for j, h in enumerate(headers):
        cell = tech_table.rows[0].cells[j]
        cell.width = col_widths[j]
        set_cell_background(cell, "1A365D")
        set_cell_margins(cell, 120, 120, 140, 140)
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.name = 'Calibri'
        r.font.size = Pt(10)

    for i, row_data in enumerate(tech_rows):
        row = tech_table.rows[i + 1]
        bg = "FFFFFF" if i % 2 == 0 else "F7FAFC"
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            cell.width = col_widths[j]
            set_cell_background(cell, bg)
            set_cell_margins(cell, 100, 100, 140, 140)
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
            r = p.add_run(val)
            r.font.name = 'Calibri'
            r.font.size = Pt(9.5)
            r.font.color.rgb = charcoal
            if j == 0:
                r.font.bold = True
                r.font.color.rgb = navy

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # =========================================================================
    # SECTION 3: WHAT IS THE ARCHITECTURE
    # =========================================================================
    add_section_heading("3", "WHAT IS THE ARCHITECTURE")
    add_body(
        "The Disaster Management System adopts a decoupled Three-Tier + Event-Driven Micro-Services Architecture. "
        "This architectural paradigm guarantees that if external services experience downtime or high latency, the core platform "
        "remains resilient and functional."
    )
    
    add_subheading("System Architectural Blueprint:")
    add_body(
        "┌─────────────────────────────────────────────────────────────────────────────┐\n"
        "│                          PRESENTATION TIER (CLIENT)                         │\n"
        "│  React 18 SPA | Redux Store | Leaflet GIS | Tailwind UI | Spline 3D Models  │\n"
        "└───────────────────────┬─────────────────────────────┬───────────────────────┘\n"
        "                        │ HTTP/REST (Port 5000)       │ HTTP/REST (Port 8000)\n"
        "                        ▼                             ▼\n"
        "┌──────────────────────────────────────────┐   ┌──────────────────────────────┐\n"
        "│         APPLICATION TIER (NODE)          │   │      AI RAG TIER (PYTHON)    │\n"
        "│ • Auth Middleware (JWT & bcrypt)         │   │ • FastAPI Server             │\n"
        "│ • Incident Controller & Multer Storage   │   │ • LlamaIndex Vector Store    │\n"
        "│ • Razorpay Payment Verification          │   │ • MiniLM Sentence Embedding  │\n"
        "│ • Places & Announcements Engine          │   │ • Emergency Directory Lookup │\n"
        "└──────┬───────────────┬───────────────────┘   └──────────────┬───────────────┘\n"
        "       │               │                                      │\n"
        "       ▼               ▼                                      ▼\n"
        "┌─────────────┐ ┌──────────────────────────┐   ┌──────────────────────────────┐\n"
        "│ DATA TIER   │ │ EVENT / DISPATCH TIER    │   │ KNOWLEDGE BASE               │\n"
        "│ MongoDB     │ │ • Telegram Bot API       │   │ NDMA & UNICEF First-Aid PDFs │\n"
        "│ Collections │ │ • Nodemailer SMTP Alerts │   │ Emergency Contacts Directory │\n"
        "└─────────────┘ └──────────────────────────┘   └──────────────────────────────┘",
        bold_prefix="Architectural Schematic:\n"
    )

    add_subheading("Key Architectural Components:")
    add_bullet("1. Client Presentation Tier (Port 3000):", "Built with React 18 using React Router for client-side navigation. Employs Redux Toolkit (`roleSlice`) for role persistence (Admin vs Civilian). Integrates Leaflet with OpenStreetMap tiles for map visualization and OSRM for dynamic routing.")
    add_bullet("2. Enterprise API Backend (Port 5000):", "Express.js REST API with modular routers: `/api/auth` (registration, JWT login, email verification), `/api/incidents` (incident creation, image uploads, emergency broadcast dispatch), `/api/donations` (resource logging, Razorpay order creation and signature verification), `/api/announcements` (public broadcast announcements), and `/api/places` (geocoded locations).")
    add_bullet("3. Event-Driven Notification Engine:", "Embedded inside the incident reporting controller. When an emergency incident is saved to MongoDB, asynchronous handlers fire non-blocking dispatch jobs to Telegram channels (`node-telegram-bot-api`) and SMTP servers (`nodemailer`), delivering real-time photo alerts and incident summaries to first responders without stalling the HTTP response.")
    add_bullet("4. RAG Intelligence Tier (Port 8000):", "FastAPI microservice executing a local vector store built on NDMA disaster manuals. When a user submits a query, it executes fuzzy emergency telephone lookups and vector similarity matching (`all-MiniLM-L6-v2`), applying regex rule filtering to extract actionable life-saving steps.")
    add_bullet("5. Data Persistence Tier (MongoDB):", "Structured document schemas enforce referential integrity for Users (with hashed passwords), Incidents (with coordinates, urgency scores, and status lifecycle: Reported -> Verified -> Responding -> Resolved), Donations, and Announcements.")

    # =========================================================================
    # SECTION 4: HOW DOES IT WORK
    # =========================================================================
    add_section_heading("4", "HOW DOES IT WORK (OPERATIONAL WORKFLOW)")
    add_body(
        "The operation of the Disaster Management System unfolds across seven coordinated stages designed to turn chaotic emergency "
        "events into structured, trackable, and resolvable relief workflows."
    )
    
    add_subheading("Step-by-Step Lifecycle:")
    add_bullet("Stage 1: User Onboarding & Access Control:", 
               "Citizens and response personnel sign up via the registration portal. Passwords are salted and hashed using bcrypt (10 rounds). Users can authenticate to unlock citizen tools or access administrative consoles if assigned administrator privileges.")
    
    add_bullet("Stage 2: Real-Time Incident Reporting with Geolocation & Media:", 
               "A witness or victim navigates to 'Report Incident'. They input the incident type (Flood, Fire, Building Collapse, Earthquake, Road Accident), describe the crisis, assign urgency (Critical, High, Medium, Low), specify coordinates/address, and attach an image. Multer securely stores the photo in `/uploads` and writes the incident record to MongoDB.")
               
    add_bullet("Stage 3: Automated Multi-Channel Emergency Dispatch:", 
               "Instantly upon submission, the backend triggers two automated pipelines: (1) Telegram Bot posts an alert card with the incident photo, location, and urgency directly into the emergency response channel; (2) Nodemailer sends an alert email with photo attachments to registered disaster relief organizations, fire rescue, and police desks.")
               
    add_bullet("Stage 4: Interactive GIS Mapping & Evacuation Route Navigation:", 
               "The Incident Map plots all verified crises with visual severity markers. Users can inspect safe shelters, relief camps, and hospitals. Using the OSRM navigation engine, survivors can plot safe walking or driving routes from their current GPS position to the nearest relief point, avoiding hazardous disaster zones.")
               
    add_bullet("Stage 5: Dual-Channel Humanitarian Aid Mobilization:", 
               "Donors can contribute in two ways: (A) Monetary Relief: Donor chooses an amount; backend calls Razorpay API to generate a cryptographically signed order; the frontend opens the Razorpay checkout modal; upon successful payment, the client sends signature, order ID, and payment ID to `/api/donations/verify-and-record` where HMAC SHA-256 verifies payment legitimacy before writing to the ledger. (B) Resource Aid: Donors pledge physical goods (blankets, water bottles, dry food, medical kits) with pickup locations for volunteer collection.")
               
    add_bullet("Stage 6: AI Disaster Triage & Knowledge Retrieval:", 
               "Citizens stranded without access to operators can use the floating AI Chatbot. If a user asks for emergency helplines, the system performs sub-millisecond regex matching across official disaster numbers. For queries like 'What to do in a flood?', the RAG pipeline queries the embedded NDMA manuals and parses actionable safety directives (e.g., '1. Move to higher ground. 2. Turn off main electricity. 3. Avoid walking in moving water').")
               
    add_bullet("Stage 7: Administrative Governance & Crisis Communication:", 
               "Command center administrators use the Admin Dashboard to review incoming incidents, update incident resolution status (Reported -> In Progress -> Resolved), audit donation transactions, and publish official public announcements to counteract rumors and panic on social media.")

    # =========================================================================
    # SECTION 5: WHAT PROBLEM IT SOLVES
    # =========================================================================
    add_section_heading("5", "WHAT PROBLEM IT SOLVES")
    add_body(
        "Conventional disaster response mechanisms suffer from severe systemic vulnerabilities. During catastrophic events, "
        "communication lines break down, emergency dispatchers become overwhelmed, and relief resources are misallocated. "
        "DMS directly addresses these critical challenges through technology."
    )

    # Comparative Problem vs Solution Table
    prob_table = doc.add_table(rows=6, cols=3)
    prob_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    prob_table.autofit = False
    
    p_headers = ["Conventional Disaster Challenge", "Consequences in the Field", "How DMS Solves the Problem"]
    p_widths = [Inches(1.8), Inches(2.3), Inches(2.4)]
    
    for j, h in enumerate(p_headers):
        cell = prob_table.rows[0].cells[j]
        cell.width = p_widths[j]
        set_cell_background(cell, "C53030")
        set_cell_margins(cell, 120, 120, 140, 140)
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.name = 'Calibri'
        r.font.size = Pt(10)

    prob_rows = [
        ("Information Asymmetry & Delays", "Emergency phone lines (100, 108, 112) experience extreme call volume, resulting in unanswered distress calls and delayed rescue deployment.", "Instant web-based crowdsourcing with direct-to-Telegram and direct-to-Email bot dispatching alerts first responders in under 3 seconds with exact GPS locations."),
        ("Lack of Visual Verification", "Responders enter disaster zones blind, lacking photographic evidence of flood levels, road blockages, or building collapses.", "Mandatory image upload with validation gives rescue teams visual ground reality before dispatching boats, ambulances, or excavators."),
        ("Opaque Relief & Financial Fraud", "Public distrust in charity funds; lack of transparency on where disaster relief money is spent leads to reduced donor participation.", "Integrated Razorpay payment gateway with cryptographic HMAC verification and public donation ledgers ensures complete financial auditing."),
        ("Misinformation & Public Panic", "Rumors regarding dam bursts, evacuation orders, or poison gas spread rapidly on social messaging apps without verification.", "Official Public Announcements channel managed exclusively by authenticated administrators ensures citizens receive verified government alerts."),
        ("Fragmented Disaster Knowledge", "Citizens trapped in floods or fires panic and do not know immediate first-aid or escape maneuvers while waiting for rescue.", "Offline-capable AI Chatbot trained on NDMA & UNICEF safety manuals provides instant, action-oriented instructions and telephone helplines.")
    ]

    for i, row_data in enumerate(prob_rows):
        row = prob_table.rows[i + 1]
        bg = "FFFFFF" if i % 2 == 0 else "FFF5F5"
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            cell.width = p_widths[j]
            set_cell_background(cell, bg)
            set_cell_margins(cell, 100, 100, 140, 140)
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
            r = p.add_run(val)
            r.font.name = 'Calibri'
            r.font.size = Pt(9.5)
            r.font.color.rgb = charcoal
            if j == 0:
                r.font.bold = True
                r.font.color.rgb = crimson

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # =========================================================================
    # SECTION 6: HOW DOES THIS BE USEFUL IN THE REAL WORLD
    # =========================================================================
    add_section_heading("6", "HOW DOES THIS BE USEFUL IN THE REAL WORLD")
    add_body(
        "The Disaster Management System is not merely a theoretical exercise; it is an operationally viable, production-ready "
        "framework capable of deployment by government bodies, humanitarian agencies, and smart city administrations."
    )

    add_subheading("Real-World Use Cases & Impact Scenarios:")
    add_bullet("1. Flash Floods & Urban Inundation (e.g., Chennai, Mumbai, Dhaka Floods):",
               "During heavy monsoon downpours, stormwater drains overflow, stranding commuters and submerging neighborhoods. Citizens use DMS on mobile devices to pinpoint flooded streets and waterlogged underpasses. Disaster response authorities instantly route inflatable rescue rafts to geolocated pins while broadcasting evacuation camp locations.")
               
    add_bullet("2. Earthquake Response & Structural Collapses:",
               "Following high-magnitude seismic events, terrestrial telephone towers are often damaged. DMS lightweight web interface functions over low-bandwidth wireless connections. Trapped individuals or neighbors upload photos of damaged buildings, allowing search-and-rescue teams (SDRF/NDRF) to prioritize high-urgency collapses.")
               
    add_bullet("3. Cyclone Preparedness & Evacuation Logistics:",
               "As meteorological centers track cyclone paths, administrators publish broadcast alerts detailing designated cyclone shelters. The OSRM routing engine directs coastal residents along safe inland corridors avoiding hazardous coastlines.")
               
    add_bullet("4. Multi-Agency Coordination Hub for NGOs & Red Cross:",
               "Relief operations frequently fail due to resource imbalances (e.g., one camp receives excessive rice while lacking potable water and insulin). DMS transparent donation and resource tracking ledger provides real-time visibility into supplies, allowing NGOs to balance aid distribution.")
               
    add_bullet("5. Community Empowerment & Citizen Resilience:",
               "Transforms passive victims into proactive community guardians. Ordinary civilians become the eyes and ears of emergency services, accelerating response times from hours to minutes and saving countless human lives.")

    # =========================================================================
    # SECTION 7: STEP-BY-STEP TERMINAL COMMANDS TO RUN & PRESENT
    # =========================================================================
    add_section_heading("7", "STEP-BY-STEP TERMINAL COMMANDS TO RUN AND PRESENT")
    add_body(
        "To present and demonstrate the Disaster Management System smoothly, follow these exact terminal commands. "
        "The project consists of three services that should run simultaneously in separate terminal windows:"
    )
    
    # Terminal Commands Table
    cmd_table = doc.add_table(rows=4, cols=3)
    cmd_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cmd_table.autofit = False
    
    c_headers = ["Service", "Working Directory", "Exact Terminal Command"]
    c_widths = [Inches(1.8), Inches(2.2), Inches(2.5)]
    
    for j, h in enumerate(c_headers):
        cell = cmd_table.rows[0].cells[j]
        cell.width = c_widths[j]
        set_cell_background(cell, "2B6CB0")
        set_cell_margins(cell, 120, 120, 140, 140)
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.name = 'Calibri'
        r.font.size = Pt(10)

    cmd_rows = [
        ("1. Backend API Server", "e:\\Projects\\DisasterManagement\\WebApp\\Backend", "node server.js\n(Runs on http://localhost:5000)"),
        ("2. React Client (Frontend)", "e:\\Projects\\DisasterManagement\\WebApp\\client", "npm start\n(Opens on http://localhost:3000)"),
        ("3. AI Helpline Chatbot", "e:\\Projects\\DisasterManagement\\WebApp", "python chatbot_api.py\n(Runs on http://localhost:8000)")
    ]

    for i, row_data in enumerate(cmd_rows):
        row = cmd_table.rows[i + 1]
        bg = "FFFFFF" if i % 2 == 0 else "EBF8FF"
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            cell.width = c_widths[j]
            set_cell_background(cell, bg)
            set_cell_margins(cell, 100, 100, 140, 140)
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
            r = p.add_run(val)
            r.font.name = 'Consolas' if j == 2 else 'Calibri'
            r.font.size = Pt(9.5)
            r.font.color.rgb = navy if j == 2 else charcoal
            if j == 0:
                r.font.bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    add_subheading("Prerequisites & Startup Checklist:")
    add_bullet("MongoDB Running:", "Ensure MongoDB service is active (`Get-Service -Name MongoDB`). The backend automatically connects to `mongodb://127.0.0.1:27017/dms-project`.")
    add_bullet("Terminal 1 (Backend):", "Open PowerShell, enter `cd e:\\Projects\\DisasterManagement\\WebApp\\Backend` and execute `node server.js`. Look for `Server running on port 5000` and `Connected to DB`.")
    add_bullet("Terminal 2 (Client):", "Open second PowerShell, enter `cd e:\\Projects\\DisasterManagement\\WebApp\\client` and execute `npm start`. The browser will launch `http://localhost:3000`.")
    add_bullet("Terminal 3 (AI Chatbot):", "Open third PowerShell, enter `cd e:\\Projects\\DisasterManagement\\WebApp` and execute `python chatbot_api.py`. Look for Uvicorn running on `http://0.0.0.0:8000`.")

    add_subheading("Recommended Presentation Flow / Live Demo Script:")
    add_bullet("Step 1 (Landing Page):", "Open `http://localhost:3000`. Highlight the modern dark/vibrant emergency design, live crisis metrics counter, and call-to-actions.")
    add_bullet("Step 2 (Citizen Reporting):", "Click 'Report Incident'. Fill in emergency details (e.g., Urban Waterlogging), choose 'High' urgency, attach a photo, and submit. Explain how the backend instantly triggers Telegram alerts and email dispatches to emergency squads.")
    add_bullet("Step 3 (GIS Mapping & Shelters):", "Navigate to '/map' and '/navigation'. Demonstrate geolocation markers for reported incidents and safe navigation routes to medical centers and shelters.")
    add_bullet("Step 4 (Donations & Razorpay):", "Visit '/donate/money'. Enter a donation pledge and show the Razorpay payment gateway checkout modal with test card details. Then demonstrate resource donations for physical supplies.")
    add_bullet("Step 5 (AI RAG Chatbot):", "Open the floating Chatbot Widget. Ask 'What is the ambulance helpline?' to show instant emergency telephone retrieval. Ask 'What to do in a flood?' to demonstrate AI safety guideline synthesis from official NDMA manuals.")
    add_bullet("Step 6 (Admin Oversight):", "Log in as an Administrator to show the Incident Verification console, announcements broadcasting, and donation financial reconciliation.")

    # Save Document
    output_path = r"e:\Projects\DisasterManagement\WebApp\Presentation\Disaster_Management_System_Presentation_Guide.docx"
    doc.save(output_path)
    print("Document saved successfully at:", output_path)

if __name__ == "__main__":
    create_document()
