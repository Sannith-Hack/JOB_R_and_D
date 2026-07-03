from fpdf import FPDF

class UltimateResume(FPDF):
    def __init__(self):
        super().__init__(orientation='P', unit='mm', format='A4')
        self.set_margins(10, 10, 10)
        self.clr_primary = (31, 58, 147) # Navy Blue
        self.clr_secondary = (44, 62, 80) # Charcoal
        self.clr_accent = (52, 152, 219) # Bright Blue
        self.main_w = 125
        self.side_w = 60

    def header(self):
        # Header Banner
        self.set_fill_color(*self.clr_primary)
        self.rect(0, 0, 210, 35, 'F')
        
        self.set_y(10)
        self.set_font('helvetica', 'B', 24)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, 'P. SANNITH', ln=1, align='C')
        
        self.set_font('helvetica', 'B', 11)
        self.cell(0, 8, 'BACKEND ENGINEER | DATA ANALYST | MOBILE DEVELOPER', ln=1, align='C')

    def draw_divider(self, x, y, w):
        self.set_draw_color(200, 200, 200)
        self.set_line_width(0.3)
        self.line(x, y, x + w, y)

    def add_section_title(self, title):
        self.ln(2)
        self.set_font('helvetica', 'B', 12)
        self.set_text_color(*self.clr_primary)
        self.cell(0, 8, title.upper(), ln=1)
        self.draw_divider(self.get_x(), self.get_y() - 1, self.main_w)
        self.ln(2)

pdf = UltimateResume()
pdf.add_page()

# --- SETUP POSITIONS ---
START_Y = 42

# --- MAIN COLUMN (Left: 125mm) ---
pdf.set_left_margin(10)
pdf.set_y(START_Y)

# 1. Summary
pdf.add_section_title("Professional Summary")
pdf.set_font('helvetica', '', 9.5)
pdf.set_text_color(*pdf.clr_secondary)
pdf.multi_cell(pdf.main_w, 5, "High-impact Backend Engineer and Data Analyst with a 440+ day coding streak. Specialized in optimizing database logic, server-side performance, and cross-platform mobile architecture. Proven expertise in building secure, scalable systems like university management portals and ecommerce backends.")

# 2. Experience
pdf.add_section_title("Experience")

# Brain O Vision
pdf.set_font('helvetica', 'B', 11)
pdf.set_text_color(0, 0, 0)
pdf.cell(pdf.main_w - 40, 5, "Agentic AI Virtual Intern")
pdf.set_font('helvetica', 'I', 9)
pdf.cell(40, 5, "Jan 2026 - Present", ln=1, align='R')
pdf.set_font('helvetica', 'B', 9.5)
pdf.set_text_color(*pdf.clr_accent)
pdf.cell(pdf.main_w, 5, "Brain O Vision Solutions", ln=1)
pdf.set_font('helvetica', '', 9)
pdf.set_text_color(*pdf.clr_secondary)
pdf.multi_cell(pdf.main_w, 4.5, "Currently engineering AI-driven automation frameworks and agentic workflows to optimize organizational efficiency.")
pdf.ln(2)

# Orbit Learning
pdf.set_font('helvetica', 'B', 11)
pdf.set_text_color(0, 0, 0)
pdf.cell(pdf.main_w - 40, 5, "AWS Cloud Intern")
pdf.set_font('helvetica', 'I', 9)
pdf.cell(40, 5, "May - Jun 2025", ln=1, align='R')
pdf.set_font('helvetica', 'B', 9.5)
pdf.set_text_color(*pdf.clr_accent)
pdf.cell(pdf.main_w, 5, "Orbit Learning Pvt Ltd", ln=1)
pdf.set_font('helvetica', '', 9)
pdf.set_text_color(*pdf.clr_secondary)
pdf.multi_cell(pdf.main_w, 4.5, "Deployed scalable WordPress hosting solutions using LAMP stack architecture on AWS, focusing on high availability.")
pdf.ln(2)

# 3. Projects
pdf.add_section_title("Selected Projects")

# Project 1
pdf.set_font('helvetica', 'B', 11)
pdf.set_text_color(0, 0, 0)
pdf.cell(pdf.main_w, 5, "KUCET College Management System", ln=1)
pdf.set_font('helvetica', '', 9)
pdf.set_text_color(*pdf.clr_secondary)
pdf.multi_cell(pdf.main_w, 4.5, "Developed a comprehensive academic portal for Kakatiya University. Engineered complex relational database schemas for real-time tracking.")
pdf.set_font('helvetica', 'BI', 8.5)
pdf.set_text_color(*pdf.clr_accent)
pdf.multi_cell(pdf.main_w, 4, "Stack: React, Node.js, Vercel, MySQL")
pdf.ln(2)

# Project 2
pdf.set_font('helvetica', 'B', 11)
pdf.set_text_color(0, 0, 0)
pdf.cell(pdf.main_w, 5, "TODO LIST Mobile Application", ln=1)
pdf.set_font('helvetica', '', 9)
pdf.set_text_color(*pdf.clr_secondary)
pdf.multi_cell(pdf.main_w, 4.5, "Cross-platform React Native task orchestrator. Integrated native SDK features for seamless Android/iOS performance.")
pdf.set_font('helvetica', 'BI', 8.5)
pdf.set_text_color(*pdf.clr_accent)
pdf.multi_cell(pdf.main_w, 4, "Stack: React Native, TypeScript, Android/iOS SDK")
pdf.ln(2)

# Project 3
pdf.set_font('helvetica', 'B', 11)
pdf.set_text_color(0, 0, 0)
pdf.cell(pdf.main_w, 5, "EcoHaven Marketplace", ln=1)
pdf.set_font('helvetica', '', 9)
pdf.set_text_color(*pdf.clr_secondary)
pdf.multi_cell(pdf.main_w, 4.5, "Sustainable ecommerce backend prototype with secure multi-factor authentication and dynamic inventory scaling.")
pdf.set_font('helvetica', 'BI', 8.5)
pdf.set_text_color(*pdf.clr_accent)
pdf.multi_cell(pdf.main_w, 4, "Stack: TypeScript, Firebase, Auth-Services")

# --- SIDEBAR COLUMN (Right: 60mm) ---
pdf.set_left_margin(145)
pdf.set_y(START_Y)

# Sidebar Background (Subtle grey)
pdf.set_fill_color(248, 249, 250)
pdf.rect(140, 35, 70, 262, 'F')

# Contact
pdf.ln(2)
pdf.set_font('helvetica', 'B', 11)
pdf.set_text_color(*pdf.clr_primary)
pdf.cell(pdf.side_w, 8, "CONTACT", ln=1)
pdf.draw_divider(145, pdf.get_y() - 1, 55)
pdf.set_font('helvetica', '', 8.5)
pdf.set_text_color(*pdf.clr_secondary)
pdf.multi_cell(55, 4, "sunnysunnit@gmail.com\n+91 7498461916\nGitHub: Sannith-Hack\nWarangal, Telangana")
pdf.ln(4)

# Skills
pdf.set_font('helvetica', 'B', 11)
pdf.set_text_color(*pdf.clr_primary)
pdf.cell(pdf.side_w, 8, "TECHNICAL SKILLS", ln=1)
pdf.draw_divider(145, pdf.get_y() - 1, 55)
pdf.set_font('helvetica', 'B', 8.5)
pdf.set_text_color(*pdf.clr_secondary)
skills = [
    ("Core", "Python, TS, JS, Java, C++, SQL"),
    ("Web", "React, Next.js, Node.js"),
    ("Mobile", "React Native (iOS/Android)"),
    ("Cloud", "AWS, Firebase, Supabase"),
    ("Data", "Tableau, Excel, R, Jupyter")
]
for cat, s in skills:
    pdf.set_font('helvetica', 'B', 8.5)
    pdf.cell(55, 4, cat, ln=1)
    pdf.set_font('helvetica', '', 8)
    pdf.multi_cell(55, 4, s)
    pdf.ln(1)

# Education
pdf.ln(4)
pdf.set_font('helvetica', 'B', 11)
pdf.set_text_color(*pdf.clr_primary)
pdf.cell(pdf.side_w, 8, "EDUCATION", ln=1)
pdf.draw_divider(145, pdf.get_y() - 1, 55)

pdf.set_font('helvetica', 'B', 8.5)
pdf.cell(55, 4, "B.Tech CSE (2023-27)", ln=1)
pdf.set_font('helvetica', '', 8)
pdf.multi_cell(55, 4, "Kakatiya University")

pdf.ln(2)
pdf.set_font('helvetica', 'B', 8.5)
pdf.cell(55, 4, "Intermediate (2021-23)", ln=1)
pdf.set_font('helvetica', '', 8)
pdf.multi_cell(55, 4, "Geesukunda Jr College")

pdf.ln(2)
pdf.set_font('helvetica', 'B', 8.5)
pdf.cell(55, 4, "10th Grade", ln=1)
pdf.set_font('helvetica', '', 8)
pdf.multi_cell(55, 4, "Vikas English School")

# Achievements
pdf.ln(6)
pdf.set_font('helvetica', 'B', 11)
pdf.set_text_color(*pdf.clr_primary)
pdf.cell(pdf.side_w, 8, "ACHIEVEMENTS", ln=1)
pdf.draw_divider(145, pdf.get_y() - 1, 55)
pdf.set_font('helvetica', '', 8)
achievs = ["440+ Days Coding Streak", "Kaggle Vampire Badge", "Kaggle Python Coder", "Pair Extraordinaire", "Pull Shark Badge"]
for ach in achievs:
    pdf.multi_cell(55, 4, f"- {ach}")

pdf.output("Sannith_Resume_Final.pdf")
print("Final Premium Resume generated: Sannith_Resume_Final.pdf")
