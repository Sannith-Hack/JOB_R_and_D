from fpdf import FPDF

class ResumePDF(FPDF):
    def header(self):
        if self.page_no() == 1:
            self.set_font('Arial', 'B', 24)
            self.set_text_color(33, 37, 41)
            self.cell(0, 15, 'P. SANNITH', ln=True, align='C')
            self.set_font('Arial', 'I', 12)
            self.cell(0, 10, 'Backend Engineer | Data Analyst | Mobile Developer', ln=True, align='C')
            self.set_font('Arial', '', 10)
            self.cell(0, 5, 'Email: sunnysunnit@gmail.com | Phone: +91 7498461916', ln=True, align='C')
            self.cell(0, 5, 'GitHub: Sannith-Hack | LinkedIn: sannith-pasunooti-183b86302', ln=True, align='C')
            self.ln(10)
            self.line(10, self.get_y(), 200, self.get_y())
            self.ln(5)

    def section_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.set_fill_color(240, 240, 240)
        self.cell(0, 10, title, ln=True, fill=True)
        self.ln(3)

    def add_bullet(self, text, bold_text=""):
        self.set_font('Arial', '', 11)
        if bold_text:
            self.set_font('Arial', 'B', 11)
            self.write(5, f" - {bold_text}: ")
            self.set_font('Arial', '', 11)
            self.write(5, f"{text}\n")
        else:
            self.write(5, f" - {text}\n")
        self.ln(2)

pdf = ResumePDF()
pdf.add_page()

# SUMMARY
pdf.section_title("PROFESSIONAL SUMMARY")
pdf.set_font('Arial', '', 11)
summary_text = (
    "Highly motivated Computer Science student with a focus on Backend Engineering, Data Analytics, and Mobile Development. "
    "Expertise in architecting secure systems, optimizing databases (PostgreSQL, MySQL, SQL Server), and building cross-platform "
    "mobile applications (React Native). Proven track record of consistent coding (440+ day streak) and successful implementation "
    "of diverse projects like the NCC Air Wing portal and EcoHaven."
)
pdf.multi_cell(0, 6, summary_text)
pdf.ln(5)

# SKILLS
pdf.section_title("TECHNICAL SKILLS")
pdf.add_bullet("TypeScript, JavaScript, Python, Rust, C++, Java, R, SQL, HTML5/CSS3", "Languages")
pdf.add_bullet("React.js, Next.js, React Native (Android/iOS), Node.js, Vite, Tailwind CSS", "Frameworks")
pdf.add_bullet("Supabase, Firebase, AWS (LAMP Stack), PostgreSQL, MySQL, MS SQL Server, Oracle", "Backend/Cloud")
pdf.add_bullet("Docker, Linux, Git/GitHub, Arduino, Tableau, Excel, 3D Visualization (Jupyter)", "Tools")
pdf.ln(3)

# EXPERIENCE & INTERNSHIPS
pdf.section_title("INTERNSHIPS & EXPERIENCE")

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 6, "Agentic AI Virtual Intern | Brain O Vision Solutions")
pdf.set_font('Arial', 'I', 10)
pdf.cell(0, 6, "Jan 2026 - Present", ln=True, align='R')
pdf.ln(1)

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 6, "Data Science & Analytics Intern | Proxenix (Offer Received)")
pdf.set_font('Arial', 'I', 10)
pdf.cell(0, 6, "Dec 2025 - Jan 2026", ln=True, align='R')
pdf.ln(1)

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 6, "AWS Cloud Intern | Orbit Learning Pvt Ltd")
pdf.set_font('Arial', 'I', 10)
pdf.cell(0, 6, "May 2025 - Jun 2025", ln=True, align='R')
pdf.set_font('Arial', '', 11)
pdf.add_bullet("Engineered Scalable WordPress Hosting using LAMP Stack on AWS.")
pdf.ln(2)

# PROJECTS
pdf.section_title("KEY PROJECTS")
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 6, "NCC Air Wing Portal")
pdf.ln(5)
pdf.set_font('Arial', '', 11)
pdf.multi_cell(0, 5, "Sophisticated student information system built with React, Vite, and Supabase. Features real-time admin dashboards and student record management.")
pdf.ln(2)

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 6, "TODO LIST Mobile App")
pdf.ln(5)
pdf.set_font('Arial', '', 11)
pdf.multi_cell(0, 5, "Cross-platform React Native application built with TypeScript for Android/iOS, integrating native build configurations and debugging.")
pdf.ln(2)

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 6, "EcoHaven")
pdf.ln(5)
pdf.set_font('Arial', '', 11)
pdf.multi_cell(0, 5, "Sustainable second-hand marketplace prototype using TypeScript and Firebase, featuring secure auth and product lifecycle management.")
pdf.ln(2)

# EDUCATION
pdf.section_title("EDUCATION")
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 6, "B.Tech in Computer Science and Engineering")
pdf.set_font('Arial', 'I', 10)
pdf.cell(0, 6, "2023 - 2027", ln=True, align='R')
pdf.set_font('Arial', '', 11)
pdf.cell(0, 6, "Kakatiya University College of Engineering and Technology (KUCE&T)", ln=True)
pdf.ln(2)

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 6, "Intermediate (MPC)")
pdf.set_font('Arial', 'I', 10)
pdf.cell(0, 6, "2021 - 2023", ln=True, align='R')
pdf.set_font('Arial', '', 11)
pdf.cell(0, 6, "Geesukunda Junior College", ln=True)
pdf.ln(2)

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 6, "10th Grade (Secondary Education)")
pdf.set_font('Arial', '', 11)
pdf.cell(0, 6, "Vikas English Middle High School", ln=True)
pdf.ln(5)

# CERTIFICATIONS
pdf.section_title("CERTIFICATIONS & ACHIEVEMENTS")
pdf.add_bullet("5-Day AI Agents Intensive Course with Google")
pdf.add_bullet("Graduate Certificate in Data Analytics - PI LABS (Aug-Nov 2025)")
pdf.add_bullet("Data Analytics Job Simulation - Deloitte (Tableau, Excel)")
pdf.add_bullet("Cybersecurity Analyst Job Simulation - TATA via Forage")
pdf.add_bullet("Agentic AI Saksham Program Participant - NASSCOM")
pdf.add_bullet("Kaggle Badges: Vampire, Code Forker, Python Coder")

pdf.output("Sannith_Resume.pdf")
print("Resume generated successfully: Sannith_Resume.pdf")
