from fpdf import FPDF

class ProfessionalResume(FPDF):
    def header(self):
        # Name and Title
        self.set_font('helvetica', 'B', 22)
        self.set_text_color(44, 62, 80) # Dark Blue/Grey
        self.cell(0, 12, 'P. SANNITH', ln=True, align='C')
        
        # Subtitle
        self.set_font('helvetica', 'B', 11)
        self.set_text_color(52, 152, 219) # Professional Blue
        self.cell(0, 5, 'BACKEND ENGINEER | DATA ANALYST | MOBILE DEVELOPER', ln=True, align='C')
        
        # Contact Info
        self.set_font('helvetica', '', 9)
        self.set_text_color(127, 140, 141) # Grey
        contact = "Email: sunnysunnit@gmail.com | Phone: +91 7498461916 | GitHub: Sannith-Hack"
        self.cell(0, 5, contact, ln=True, align='C')
        self.ln(5)
        
        # Thin line
        self.set_draw_color(189, 195, 199)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)

    def section_header(self, title):
        self.set_font('helvetica', 'B', 12)
        self.set_text_color(44, 62, 80)
        self.set_fill_color(236, 240, 241) # Very light grey background
        self.cell(0, 7, f"  {title}", ln=True, fill=True)
        self.ln(2)

    def project_item(self, title, desc, tech):
        self.set_font('helvetica', 'B', 10)
        self.set_text_color(44, 62, 80)
        self.cell(0, 5, title, ln=True)
        self.set_font('helvetica', '', 9)
        self.set_text_color(52, 73, 94)
        self.multi_cell(0, 4, desc)
        self.set_font('helvetica', 'I', 8)
        self.set_text_color(52, 152, 219)
        self.cell(0, 4, f"Tech: {tech}", ln=True)
        self.ln(2)

    def skill_line(self, category, skills):
        self.set_font('helvetica', 'B', 9)
        self.set_text_color(44, 62, 80)
        self.write(4, f"{category}: ")
        self.set_font('helvetica', '', 9)
        self.set_text_color(52, 73, 94)
        self.write(4, f"{skills}\n")
        self.ln(1)

pdf = ProfessionalResume()
pdf.set_auto_page_break(auto=True, margin=10)
pdf.add_page()

# 1. SUMMARY
pdf.set_font('helvetica', '', 9.5)
pdf.set_text_color(52, 73, 94)
summary = (
    "Results-driven Computer Science student with 440+ days coding streak. Specialist in Backend Engineering and "
    "Data Analytics, with proven expertise in architecting secure systems and scalable mobile applications. "
    "Passionate about optimizing engine-room logic and database performance."
)
pdf.multi_cell(0, 4.5, summary)
pdf.ln(3)

# 2. TECHNICAL SKILLS
pdf.section_header("TECHNICAL SKILLS")
pdf.skill_line("Languages", "TypeScript, JavaScript, Python, Rust, C++, Java, R, SQL, HTML5/CSS3")
pdf.skill_line("Frameworks", "React.js, Next.js, React Native (Android/iOS), Node.js, Vite, Tailwind CSS")
pdf.skill_line("Backend/Cloud", "Supabase, Firebase, AWS (LAMP Stack), PostgreSQL, MySQL, MS SQL Server")
pdf.skill_line("Tools", "Docker, Linux, Git, Arduino, Tableau, Excel, 3D Visualization (Jupyter)")
pdf.ln(2)

# 3. EXPERIENCE & INTERNSHIPS
pdf.section_header("PROFESSIONAL EXPERIENCE")

# Item 1
pdf.set_font('helvetica', 'B', 10)
pdf.set_text_color(44, 62, 80)
pdf.cell(140, 5, "Agentic AI Virtual Intern | Brain O Vision Solutions")
pdf.set_font('helvetica', 'I', 9)
pdf.cell(0, 5, "Jan 2026 - Present", ln=True, align='R')
pdf.ln(1)

# Item 2
pdf.set_font('helvetica', 'B', 10)
pdf.set_text_color(44, 62, 80)
pdf.cell(140, 5, "AWS Cloud Intern | Orbit Learning Pvt Ltd")
pdf.set_font('helvetica', 'I', 9)
pdf.cell(0, 5, "May 2025 - Jun 2025", ln=True, align='R')
pdf.set_font('helvetica', '', 9)
pdf.set_text_color(52, 73, 94)
pdf.cell(0, 4, "- Engineered scalable WordPress hosting environments using LAMP Stack on AWS.", ln=True)
pdf.ln(2)

# 4. PROJECTS
pdf.section_header("KEY PROJECTS")

pdf.project_item(
    "KUCET College Management System",
    "A comprehensive academic management portal for Kakatiya University. Features robust student record tracking, course enrollments, and performance analytics.",
    "JavaScript, React, Node.js, Vercel"
)

pdf.project_item(
    "TODO LIST Mobile Application",
    "Cross-platform React Native app built for high performance. Implements native Android/iOS configurations and complex state management.",
    "React Native, TypeScript, Android/iOS SDK"
)

pdf.project_item(
    "EcoHaven Marketplace",
    "Full-stack sustainable second-hand marketplace prototype. Includes secure authentication and comprehensive product lifecycle management.",
    "TypeScript, Firebase, Authentication"
)

# 5. EDUCATION
pdf.section_header("EDUCATION")

# B.Tech
pdf.set_font('helvetica', 'B', 10)
pdf.cell(140, 5, "B.Tech in Computer Science and Engineering")
pdf.set_font('helvetica', 'I', 9)
pdf.cell(0, 5, "2023 - 2027", ln=True, align='R')
pdf.set_font('helvetica', '', 9)
pdf.cell(0, 4, "Kakatiya University College of Engineering and Technology (KUCE&T)", ln=True)
pdf.ln(1)

# Intermediate & 10th
pdf.set_font('helvetica', 'B', 10)
pdf.cell(140, 5, "Intermediate (MPC) - Geesukunda Junior College")
pdf.set_font('helvetica', 'I', 9)
pdf.cell(0, 5, "2021 - 2023", ln=True, align='R')
pdf.ln(1)
pdf.set_font('helvetica', 'B', 10)
pdf.cell(0, 5, "10th Grade - Vikas English Middle High School", ln=True)
pdf.ln(2)

# 6. CERTIFICATIONS
pdf.section_header("CERTIFICATIONS & HONORS")
pdf.set_font('helvetica', '', 9)
certs = [
    "5-Day AI Agents Intensive Course with Google",
    "Graduate Certificate in Data Analytics - PI LABS (Aug-Nov 2025)",
    "Data Analytics Job Simulation - Deloitte (Tableau, Excel Modeling)",
    "Cybersecurity Analyst Job Simulation - TATA via Forage",
    "Kaggle Badges: Vampire, Code Forker, Python Coder",
    "GitHub Achievements: Pair Extraordinaire, Pull Shark, YOLO"
]
for cert in certs:
    pdf.cell(0, 4, f"- {cert}", ln=True)

pdf.output("Sannith_Resume_Professional.pdf")
print("Professional Resume generated successfully.")
