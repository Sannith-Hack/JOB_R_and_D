from fpdf import FPDF

class FinalOnePageResume(FPDF):
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
        self.set_y(15)
        self.set_x(5)
        self.set_font('helvetica', 'B', 20)
        self.set_text_color(255, 255, 255)
        self.cell(self.sidebar_w - 10, 10, "P. SANNITH ", ln=1, align='C')
        self.set_font('helvetica', 'B', 10)
        self.cell(self.sidebar_w - 10, 6, "BACKEND & DATA ANALYST", ln=1, align='C')
        self.ln(4)

        # Contact
        self.section_title_side("CONTACT")
        self.set_font('helvetica', '', 9)
        self.set_x(8)
        self.multi_cell(self.sidebar_w - 16, 4.5, "sunnysunnit@gmail.com\n+91 7498461916\nGitHub: Sannith-Hack\nWarangal, Telangana")
        self.ln(1.5)

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
            self.cell(0, 4.5, cat, ln=1)
            self.set_x(8)
            self.set_font('helvetica', '', 8.5)
            self.multi_cell(self.sidebar_w - 16, 3.8, s)
            self.ln(0.3)
        self.ln(1.5)

        # Education
        self.section_title_side("EDUCATION")
        edu = [
            ("B.Tech CSE", "Kakatiya University", "2023 - 2027"),
            ("Intermediate (MPC)", "Geesukunda Jr College", "2021 - 2023"),
            ("10th Grade", "Vikas English School", "Grad. 2021")
        ]
        for deg, inst, date in edu:
            self.set_x(8)
            self.set_font('helvetica', 'B', 9.5)
            self.cell(0, 4.5, deg, ln=1)
            self.set_x(8)
            self.set_font('helvetica', 'I', 8.5)
            self.cell(0, 4, inst, ln=1)
            self.set_x(8)
            self.set_font('helvetica', '', 8.5)
            self.cell(0, 3.5, date, ln=1)
            self.ln(0.7)

    def section_title_side(self, title):
        self.set_x(8)
        self.set_font('helvetica', 'B', 10)
        self.set_text_color(*self.clr_accent)
        self.cell(0, 7, title, ln=1)
        self.set_draw_color(*self.clr_accent)
        self.set_line_width(0.5)
        self.line(8, self.get_y() - 1, self.sidebar_w - 8, self.get_y() - 1)
        self.set_text_color(255, 255, 255)
        self.ln(0.5)

    def main_content(self):
        self.set_y(15)
        self.set_left_margin(self.main_x)
        self.set_text_color(*self.clr_sidebar)
        
        # Professional Summary
        self.set_font('helvetica', 'B', 13)
        self.cell(0, 6, "PROFESSIONAL SUMMARY", ln=1)
        self.set_font('helvetica', '', 9.5)
        self.set_text_color(*self.clr_text_main)
        summary = (
            "Highly motivated Backend Engineer and Data Analyst with a 440+ day coding streak. "
            "Specialized in optimizing database logic and server-side performance. Expert in building "
            "secure, scalable systems using modern frameworks and cloud infrastructures."
        )
        self.multi_cell(self.main_w, 4.3, summary)
        self.ln(0.5)

        # Experience
        self.main_section_title("WORK EXPERIENCE")
        exp = [
            ("Agentic AI Virtual Intern", "Brain O Vision Solutions", "Jan 2026 - Present", 
             "Developing AI-driven automation frameworks and agentic workflows to optimize organizational efficiency and decision-making."),
            ("AWS Cloud Intern", "Orbit Learning Pvt Ltd", "May - Jun 2025", 
             "Deployed and managed scalable WordPress hosting using LAMP stack on AWS. Optimized cloud resources for high-availability performance.")
        ]
        for role, comp, date, desc in exp:
            self.set_font('helvetica', 'B', 10.5)
            self.set_text_color(*self.clr_sidebar)
            self.cell(80, 5, role)
            self.set_font('helvetica', 'I', 9)
            self.cell(0, 5, date, ln=1, align='R')
            self.set_font('helvetica', 'B', 10)
            self.set_text_color(*self.clr_accent)
            self.cell(0, 4, comp, ln=1)
            self.set_font('helvetica', '', 9.5)
            self.set_text_color(*self.clr_text_main)
            self.multi_cell(self.main_w, 4, f"- {desc}")
            self.ln(0.2)

        # Projects
        self.main_section_title("FEATURED PROJECTS")
        projs = [
            ("KUCET College Management System", 
             "Academic portal for Kakatiya University. Designed complex relational schemas to handle thousands of real-time student records and enrollments.", 
             "React, Node.js, Vercel, MySQL"),
            ("TODO LIST Mobile Application", 
             "Developed a high-performance cross-platform task manager. Integrated native device SDKs for a seamless user experience.", 
             "React Native, TypeScript, Android/iOS SDK"),
            ("EcoHaven Marketplace", 
             "Sustainable second-hand marketplace backend. Integrated secure authentication and dynamic inventory management systems.", 
             "TypeScript, Firebase, Auth")
        ]
        for name, desc, tech in projs:
            self.set_font('helvetica', 'B', 10.5)
            self.set_text_color(*self.clr_sidebar)
            self.cell(0, 5, name, ln=1)
            self.set_font('helvetica', '', 9.5)
            self.set_text_color(*self.clr_text_main)
            self.multi_cell(self.main_w, 4, desc)
            self.set_font('helvetica', 'BI', 9)
            self.set_text_color(*self.clr_accent)
            self.ln(0.2)

        # Achievements
        self.main_section_title("CERTIFICATIONS & ACHIEVEMENTS")
        self.set_font('helvetica', '', 9.5)
        self.set_text_color(*self.clr_text_main)
        achievs = [
            "440+ Days Coding Streak - Consistent daily growth.",
            "5-Day AI Agents Intensive Course with Google.",
            "Graduate Certificate in Data Analytics - PI LABS (2025).",
            "Deloitte Data Analytics & TATA Cybersecurity simulations.",
            "Kaggle Badges: Vampire, Code Forker, & Python Coder.",
            "GitHub Achievements: Pair Extraordinaire & Pull Shark."
        ]
        for ach in achievs:
            self.multi_cell(self.main_w, 4.2, f"- {ach}")

    def main_section_title(self, title):
        self.set_font('helvetica', 'B', 12)
        self.set_text_color(*self.clr_accent)
        self.cell(0, 6.5, title, ln=1)
        self.set_draw_color(220, 220, 220)
        self.set_line_width(0.3)
        self.line(self.main_x, self.get_y(), 200, self.get_y())
        self.ln(0.8)

pdf = FinalOnePageResume()
pdf.add_page()
pdf.sidebar()
pdf.main_content()
pdf.output("Sannith_Resume_Professional_Final.pdf")
print("One Page Professional Resume Generated: Sannith_Resume_Professional_Final.pdf")
