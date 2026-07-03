from fpdf import FPDF

class PremiumResume(FPDF):
    def __init__(self):
        super().__init__(orientation='P', unit='mm', format='A4')
        self.set_margins(10, 10, 10)
        # Use custom names to avoid conflicts with FPDF internal properties
        self.clr_accent = (41, 128, 185) # Professional Blue
        self.clr_text = (44, 62, 80)    # Deep Charcoal
        self.clr_sidebar_bg = (52, 73, 94) # Dark sidebar

    def header(self):
        # Top Header Banner
        self.set_fill_color(*self.clr_accent)
        self.rect(0, 0, 210, 35, 'F')
        
        self.set_y(10)
        self.set_font('helvetica', 'B', 26)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, 'P. SANNITH', ln=1, align='C')
        
        self.set_font('helvetica', 'B', 12)
        self.cell(0, 8, 'BACKEND ENGINEER | DATA ANALYST | MOBILE DEVELOPER', ln=1, align='C')

    def section_title(self, title):
        self.set_font('helvetica', 'B', 12)
        self.set_text_color(*self.clr_accent)
        self.cell(0, 10, f"{title}", ln=1)
        # Line below title
        curr_x = self.get_x()
        curr_y = self.get_y()
        self.set_draw_color(*self.clr_accent)
        self.set_line_width(0.5)
        self.line(curr_x, curr_y - 2, curr_x + 125, curr_y - 2)
        self.ln(2)

pdf = PremiumResume()
pdf.add_page()

# --- SIDEBAR (70mm background) ---
pdf.set_fill_color(*pdf.clr_sidebar_bg)
pdf.rect(0, 35, 70, 262, 'F')

# --- SIDEBAR CONTENT ---
# We use a smaller margin for the sidebar
pdf.set_left_margin(5)
pdf.set_y(40)

# Contact Info
pdf.set_font('helvetica', 'B', 10)
pdf.set_text_color(255, 255, 255)
pdf.cell(60, 6, "CONTACT", ln=1)
pdf.set_font('helvetica', '', 8.5)
pdf.cell(60, 4, "sunnysunnit@gmail.com", ln=1)
pdf.cell(60, 4, "+91 7498461916", ln=1)
pdf.cell(60, 4, "GitHub: Sannith-Hack", ln=1)
pdf.ln(5)

# Technical Skills
pdf.set_font('helvetica', 'B', 10)
pdf.cell(60, 6, "TECHNICAL SKILLS", ln=1)
skills = [
    ("Languages", "Python, TS, JS, Java, C++, Rust, R, SQL"),
    ("Frameworks", "React, Next.js, Node, React Native, Vite"),
    ("Cloud/DB", "AWS, Supabase, Firebase, MySQL, PostgreSQL"),
    ("Tools", "Docker, Linux, Tableau, Excel, Arduino")
]
for cat, s in skills:
    pdf.set_font('helvetica', 'B', 8.5)
    pdf.cell(60, 4, cat, ln=1)
    pdf.set_font('helvetica', '', 8)
    pdf.multi_cell(60, 4, s)
    pdf.ln(1)

# Education
pdf.ln(4)
pdf.set_font('helvetica', 'B', 10)
pdf.cell(60, 6, "EDUCATION", ln=1)
pdf.set_font('helvetica', 'B', 8.5)
pdf.cell(60, 4, "B.Tech CSE (2023-27)", ln=1)
pdf.set_font('helvetica', '', 8)
pdf.multi_cell(60, 4, "Kakatiya University (KUCE&T)")
pdf.ln(2)
pdf.set_font('helvetica', 'B', 8.5)
pdf.cell(60, 4, "Intermediate (2021-23)", ln=1)
pdf.set_font('helvetica', '', 8)
pdf.cell(60, 4, "Geesukunda Junior College", ln=1)
pdf.ln(2)
pdf.set_font('helvetica', 'B', 8.5)
pdf.cell(60, 4, "10th Grade", ln=1)
pdf.set_font('helvetica', '', 8)
pdf.cell(60, 4, "Vikas English School", ln=1)

# Achievements
pdf.ln(6)
pdf.set_font('helvetica', 'B', 10)
pdf.cell(60, 6, "ACHIEVEMENTS", ln=1)
pdf.set_font('helvetica', '', 8)
achs = ["440+ Days Coding Streak", "Kaggle Vampire Badge", "Kaggle Python Coder", "Pair Extraordinaire", "Pull Shark"]
for ach in achs:
    pdf.cell(60, 4, f"- {ach}", ln=1)

# --- MAIN CONTENT ---
pdf.set_left_margin(75)
pdf.set_y(40)

# Summary
pdf.section_title("PROFESSIONAL SUMMARY")
pdf.set_font('helvetica', '', 9.5)
pdf.set_text_color(*pdf.clr_text)
pdf.multi_cell(0, 5, "Results-driven Backend Engineer and Data Analyst with a focus on optimizing database logic and server-side performance. Specialist in architecting secure systems and scalable mobile applications. Proven track record of consistent growth and project delivery.")
pdf.ln(4)

# Experience
pdf.section_title("EXPERIENCE")
experiences = [
    ("Agentic AI Virtual Intern", "Brain O Vision Solutions", "Jan 2026 - Present", "Developing AI-driven automation solutions and agentic frameworks."),
    ("AWS Cloud Intern", "Orbit Learning Pvt Ltd", "May - Jun 2025", "Engineered scalable WordPress hosting using LAMP stack on AWS infrastructure.")
]
for role, company, date, desc in experiences:
    pdf.set_font('helvetica', 'B', 11)
    pdf.set_text_color(*pdf.clr_text)
    pdf.cell(90, 5, role)
    pdf.set_font('helvetica', 'I', 9)
    pdf.cell(0, 5, date, ln=1, align='R')
    pdf.set_font('helvetica', 'B', 9.5)
    pdf.set_text_color(*pdf.clr_accent)
    pdf.cell(0, 5, company, ln=1)
    pdf.set_font('helvetica', '', 9)
    pdf.set_text_color(*pdf.clr_text)
    pdf.multi_cell(0, 4.5, f"- {desc}")
    pdf.ln(3)

# Projects
pdf.section_title("SELECTED PROJECTS")
projects = [
    ("KUCET College Management System", "Comprehensive portal for university operations. Managed complex database relationships and real-time student tracking.", "React, Node.js, Vercel"),
    ("TODO LIST Mobile Application", "High-performance React Native app for task orchestration across Android/iOS platforms.", "React Native, TypeScript"),
    ("EcoHaven Marketplace", "Sustainable commerce platform featuring advanced authentication and state-based product management.", "TypeScript, Firebase")
]
for name, desc, tech in projects:
    pdf.set_font('helvetica', 'B', 11)
    pdf.set_text_color(*pdf.clr_text)
    pdf.cell(0, 5, name, ln=1)
    pdf.set_font('helvetica', '', 9)
    pdf.multi_cell(0, 4.5, desc)
    pdf.set_font('helvetica', 'BI', 8.5)
    pdf.set_text_color(*pdf.clr_accent)
    pdf.cell(0, 4, f"Tech Stack: {tech}", ln=1)
    pdf.set_text_color(*pdf.clr_text)
    pdf.ln(2)

# Certifications
pdf.section_title("CERTIFICATIONS")
pdf.set_font('helvetica', '', 9)
pdf.set_text_color(*pdf.clr_text)
certs = [
    "5-Day AI Agents Intensive Course - Google",
    "Data Analytics Graduate Certificate - PI LABS",
    "Data Analytics Job Simulation - Deloitte",
    "Cybersecurity Job Simulation - TATA (IAM Focus)"
]
for cert in certs:
    pdf.cell(0, 5, f"- {cert}", ln=1)

pdf.output("Sannith_Resume_Premium.pdf")
print("Premium Resume generated successfully: Sannith_Resume_Premium.pdf")
