from fpdf import FPDF

class FullPageProfessionalResume(FPDF):
    def __init__(self):
        super().__init__(orientation='P', unit='mm', format='A4')
        self.set_margins(0, 0, 0)
        self.clr_sidebar = (44, 62, 80)
        self.clr_accent = (41, 128, 185)
        self.clr_text_main = (52, 73, 94)
        self.sidebar_w = 70
        self.main_x = 78
        self.main_w = 122

    def sidebar(self):
        # Sidebar Background
        self.set_fill_color(*self.clr_sidebar)
        self.rect(0, 0, self.sidebar_w, 297, 'F')
        
        # Profile Section
        self.set_y(20)
        self.set_x(5)
        self.set_font('helvetica', 'B', 18)
        self.set_text_color(255, 255, 255)
        self.cell(self.sidebar_w - 10, 10, "SANNITH P.", ln=1, align='C')
        self.set_font('helvetica', 'B', 10)
        self.cell(self.sidebar_w - 10, 6, "BACKEND & DATA ANALYST", ln=1, align='C')
        self.ln(12)

        # Contact
        self.section_title_side("CONTACT")
        self.set_font('helvetica', '', 9.5)
        self.set_x(8)
        self.multi_cell(self.sidebar_w - 16, 6, "sunnysunnit@gmail.com\n+91 7498461916\nGitHub: Sannith-Hack\nWarangal, Telangana")
        self.ln(8)

        # Skills
        self.section_title_side("CORE SKILLS")
        skills = [
            ("LANGUAGES", "Python, TS, JS, Java, C++, SQL, Rust, R"),
            ("WEB STACK", "React, Next.js, Node.js, Vite, Tailwind"),
            ("MOBILE", "React Native (iOS/Android)"),
            ("CLOUD & DB", "AWS, Firebase, Supabase, MySQL, PostgreSQL")
        ]
        for cat, s in skills:
            self.set_x(8)
            self.set_font('helvetica', 'B', 9)
            self.cell(0, 5, cat, ln=1)
            self.set_x(8)
            self.set_font('helvetica', '', 8.5)
            self.multi_cell(self.sidebar_w - 16, 4.5, s)
            self.ln(2)
        self.ln(8)

        # Education
        self.section_title_side("EDUCATION")
        edu = [
            ("B.Tech CSE", "Kakatiya University", "2023 - 2027"),
            ("Intermediate (MPC)", "Geesukunda Jr College", "2021 - 2023"),
            ("10th Grade", "Vikas English School", "Grad. 2021")
        ]
        for deg, inst, date in edu:
            self.set_x(8)
            self.set_font('helvetica', 'B', 9)
            self.cell(0, 5, deg, ln=1)
            self.set_x(8)
            self.set_font('helvetica', 'I', 8.5)
            self.cell(0, 4, inst, ln=1)
            self.set_x(8)
            self.set_font('helvetica', '', 8)
            self.cell(0, 4, date, ln=1)
            self.ln(3)

    def section_title_side(self, title):
        self.set_x(8)
        self.set_font('helvetica', 'B', 11)
        self.set_text_color(*self.clr_accent)
        self.cell(0, 8, title, ln=1)
        self.set_draw_color(*self.clr_accent)
        self.set_line_width(0.5)
        self.line(8, self.get_y() - 1, self.sidebar_w - 8, self.get_y() - 1)
        self.set_text_color(255, 255, 255)
        self.ln(2)

    def main_content(self):
        self.set_y(20)
        self.set_left_margin(self.main_x)
        self.set_text_color(*self.clr_sidebar)
        
        # Professional Summary
        self.set_font('helvetica', 'B', 15)
        self.cell(0, 10, "PROFESSIONAL SUMMARY", ln=1)
        self.set_font('helvetica', '', 10.5)
        self.set_text_color(*self.clr_text_main)
        summary = (
            "Highly motivated and results-driven Computer Science student with a 440+ day coding streak. "
            "Specialized in Backend Engineering and Data Analytics, with a focus on optimizing database logic "
            "and server-side performance. Expert in building secure, scalable systems using modern frameworks "
            "and cloud infrastructures."
        )
        self.multi_cell(self.main_w, 6, summary)
        self.ln(10)

        # Experience
        self.main_section_title("WORK EXPERIENCE")
        exp = [
            ("Agentic AI Virtual Intern", "Brain O Vision Solutions", "Jan 2026 - Present", 
             "Spearheading the development of AI-driven automation frameworks. Designing agentic workflows to improve operational efficiency and decision-making processes."),
            ("AWS Cloud Intern", "Orbit Learning Pvt Ltd", "May - Jun 2025", 
             "Implemented scalable WordPress hosting environments using LAMP stack on AWS. Managed cloud resources and optimized server performance for high traffic.")
        ]
        for role, comp, date, desc in exp:
            self.set_font('helvetica', 'B', 12)
            self.set_text_color(*self.clr_sidebar)
            self.cell(80, 7, role)
            self.set_font('helvetica', 'I', 10)
            self.cell(0, 7, date, ln=1, align='R')
            self.set_font('helvetica', 'B', 11)
            self.set_text_color(*self.clr_accent)
            self.cell(0, 6, comp, ln=1)
            self.set_font('helvetica', '', 10.5)
            self.set_text_color(*self.clr_text_main)
            self.multi_cell(self.main_w, 5.5, f"- {desc}")
            self.ln(6)

        # Projects
        self.main_section_title("FEATURED PROJECTS")
        projs = [
            ("KUCET College Management System", 
             "Architected a comprehensive management portal for Kakatiya University. Engineered complex relational database schemas to handle thousands of real-time student records and enrollments.", 
             "React, Node.js, Vercel, MySQL"),
            ("TODO LIST Mobile Application", 
             "Developed a high-performance cross-platform task manager. Leveraged React Native and native SDKs to ensure a seamless and responsive user experience on both Android and iOS.", 
             "React Native, TypeScript, Android/iOS SDK"),
            ("EcoHaven Marketplace", 
             "Built a sustainable second-hand marketplace backend. Integrated secure authentication and multi-factor security protocols alongside dynamic inventory management systems.", 
             "TypeScript, Firebase, Authentication")
        ]
        for name, desc, tech in projs:
            self.set_font('helvetica', 'B', 12)
            self.set_text_color(*self.clr_sidebar)
            self.cell(0, 7, name, ln=1)
            self.set_font('helvetica', '', 10.5)
            self.set_text_color(*self.clr_text_main)
            self.multi_cell(self.main_w, 5.5, desc)
            self.set_font('helvetica', 'BI', 9.5)
            self.set_text_color(*self.clr_accent)
            self.multi_cell(self.main_w, 5, f"Tech Stack: {tech}")
            self.ln(6)

        # Certifications & Achievements
        self.main_section_title("CERTIFICATIONS & ACHIEVEMENTS")
        self.set_font('helvetica', '', 10.5)
        self.set_text_color(*self.clr_text_main)
        achievs = [
            "440+ Days Coding Streak - Demonstrating consistency and growth.",
            "5-Day AI Agents Intensive Course with Google.",
            "Graduate Certificate in Data Analytics - PI LABS (Aug-Nov 2025).",
            "Deloitte Data Analytics & TATA Cybersecurity Job Simulations.",
            "Kaggle Badges: Vampire, Code Forker, & Python Coder.",
            "GitHub Achievements: Pair Extraordinaire, Pull Shark, & YOLO."
        ]
        for ach in achievs:
            self.multi_cell(self.main_w, 6, f"- {ach}")
        self.ln(5)

    def main_section_title(self, title):
        self.set_font('helvetica', 'B', 13)
        self.set_text_color(*self.clr_accent)
        self.cell(0, 10, title, ln=1)
        self.set_draw_color(220, 220, 220)
        self.set_line_width(0.3)
        self.line(self.main_x, self.get_y(), 200, self.get_y())
        self.ln(5)

pdf = FullPageProfessionalResume()
pdf.add_page()
pdf.sidebar()
pdf.main_content()
pdf.output("Sannith_Resume_Full_Page.pdf")
print("Full Page Resume Generated: Sannith_Resume_Full_Page.pdf")
