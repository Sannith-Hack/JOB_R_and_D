const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

const resumeHTML = `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sannith - Professional Resume</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Helvetica', Arial, sans-serif;
            background: white;
            color: #345e94;
        }
        
        .container {
            display: flex;
            height: 100vh;
            background: white;
        }
        
        .sidebar {
            width: 23%;
            background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            color: white;
            padding: 30px 15px;
            overflow-y: auto;
        }
        
        .main-content {
            width: 77%;
            padding: 30px 25px;
            overflow-y: auto;
            color: #345e94;
        }
        
        .profile-section {
            text-align: center;
            margin-bottom: 20px;
            border-bottom: 2px solid #2980b9;
            padding-bottom: 15px;
        }
        
        .profile-name {
            font-size: 24px;
            font-weight: bold;
            letter-spacing: 1px;
            margin-bottom: 5px;
        }
        
        .profile-title {
            font-size: 12px;
            font-weight: bold;
            letter-spacing: 0.5px;
            color: #ecf0f1;
        }
        
        .section-title {
            font-size: 11px;
            font-weight: bold;
            margin-top: 15px;
            margin-bottom: 8px;
            padding-bottom: 6px;
            border-bottom: 1.5px solid #2980b9;
            color: #2980b9;
        }
        
        .sidebar .section-title {
            color: #2980b9;
            border-bottom: 1.5px solid #2980b9;
            text-align: left;
        }
        
        .contact-info {
            font-size: 9px;
            line-height: 1.4;
            text-align: left;
        }
        
        .skill-category {
            font-size: 9px;
            font-weight: bold;
            margin-top: 8px;
            margin-bottom: 2px;
        }
        
        .skill-items {
            font-size: 8.5px;
            line-height: 1.3;
            margin-bottom: 5px;
        }
        
        .education-item {
            font-size: 9px;
            margin-bottom: 10px;
        }
        
        .education-degree {
            font-weight: bold;
            margin-bottom: 2px;
        }
        
        .education-school {
            font-style: italic;
            font-size: 8.5px;
            margin-bottom: 1px;
        }
        
        .education-date {
            font-size: 8.5px;
            color: #bdc3c7;
        }
        
        .main-section-title {
            font-size: 13px;
            font-weight: bold;
            color: #2980b9;
            margin-top: 12px;
            margin-bottom: 8px;
            padding-bottom: 5px;
            border-bottom: 1px solid #ddd;
        }
        
        .summary-text {
            font-size: 10px;
            line-height: 1.5;
            margin-bottom: 8px;
            text-align: justify;
        }
        
        .experience-item {
            margin-bottom: 8px;
        }
        
        .experience-header {
            display: flex;
            justify-content: space-between;
            margin-bottom: 2px;
        }
        
        .experience-role {
            font-weight: bold;
            font-size: 11px;
            color: #2c3e50;
        }
        
        .experience-date {
            font-size: 9.5px;
            font-style: italic;
            color: #34495e;
        }
        
        .experience-company {
            font-weight: bold;
            font-size: 10.5px;
            color: #2980b9;
            margin-bottom: 2px;
        }
        
        .experience-description {
            font-size: 9.5px;
            line-height: 1.4;
            margin-left: 10px;
        }
        
        .project-item {
            margin-bottom: 7px;
        }
        
        .project-name {
            font-weight: bold;
            font-size: 11px;
            color: #2c3e50;
            margin-bottom: 2px;
        }
        
        .project-description {
            font-size: 9.5px;
            line-height: 1.4;
            margin-bottom: 2px;
        }
        
        .achievement-item {
            font-size: 9.5px;
            line-height: 1.4;
            margin-bottom: 3px;
            margin-left: 10px;
        }
        
        @media print {
            body {
                margin: 0;
                padding: 0;
            }
            .container {
                height: auto;
            }
            .sidebar, .main-content {
                page-break-inside: avoid;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- SIDEBAR -->
        <div class="sidebar">
            <div class="profile-section">
                <div class="profile-name">P. SANNITH</div>
                <div class="profile-title">BACKEND & DATA ANALYST</div>
            </div>
            
            <div class="section-title">CONTACT</div>
            <div class="contact-info">
                sunnysunnit@gmail.com<br>
                +91 7498461916<br>
                GitHub: Sannith-Hack<br>
                Warangal, Telangana
            </div>
            
            <div class="section-title">CORE SKILLS</div>
            <div class="skill-category">LANGUAGES</div>
            <div class="skill-items">Python, TypeScript, JavaScript, Java, C++, SQL, Rust, R</div>
            
            <div class="skill-category">WEB STACK</div>
            <div class="skill-items">React, Next.js, Node.js, Vite, Tailwind CSS</div>
            
            <div class="skill-category">MOBILE</div>
            <div class="skill-items">React Native (iOS/Android)</div>
            
            <div class="skill-category">CLOUD & DB</div>
            <div class="skill-items">AWS, Firebase, Supabase, MySQL, PostgreSQL</div>
            
            <div class="section-title">EDUCATION</div>
            <div class="education-item">
                <div class="education-degree">B.Tech CSE</div>
                <div class="education-school">Kakatiya University</div>
                <div class="education-date">2023 - 2027</div>
            </div>
            
            <div class="education-item">
                <div class="education-degree">Intermediate (MPC)</div>
                <div class="education-school">Geesukunda Jr College</div>
                <div class="education-date">2021 - 2023</div>
            </div>
            
            <div class="education-item">
                <div class="education-degree">10th Grade</div>
                <div class="education-school">Vikas English School</div>
                <div class="education-date">Grad. 2021</div>
            </div>
        </div>
        
        <!-- MAIN CONTENT -->
        <div class="main-content">
            <div class="main-section-title">PROFESSIONAL SUMMARY</div>
            <div class="summary-text">
                Highly motivated Backend Engineer and Data Analyst with a 440+ day coding streak. Specialized in optimizing database logic and server-side performance. Expert in building secure, scalable systems using modern frameworks and cloud infrastructures.
            </div>
            
            <div class="main-section-title">WORK EXPERIENCE</div>
            
            <div class="experience-item">
                <div class="experience-header">
                    <span class="experience-role">Agentic AI Virtual Intern</span>
                    <span class="experience-date">Jan 2026 - Present</span>
                </div>
                <div class="experience-company">Brain O Vision Solutions</div>
                <div class="experience-description">
                    • Developing AI-driven automation frameworks and agentic workflows to optimize organizational efficiency and decision-making.
                </div>
            </div>
            
            <div class="experience-item">
                <div class="experience-header">
                    <span class="experience-role">AWS Cloud Intern</span>
                    <span class="experience-date">May - Jun 2025</span>
                </div>
                <div class="experience-company">Orbit Learning Pvt Ltd</div>
                <div class="experience-description">
                    • Deployed and managed scalable WordPress hosting using LAMP stack on AWS. Optimized cloud resources for high-availability performance.
                </div>
            </div>
            
            <div class="main-section-title">FEATURED PROJECTS</div>
            
            <div class="project-item">
                <div class="project-name">KUCET College Management System</div>
                <div class="project-description">
                    Academic portal for Kakatiya University. Designed complex relational schemas to handle thousands of real-time student records and enrollments.
                </div>
                <div style="font-size: 9px; color: #2980b9; font-weight: 600;">React, Node.js, Vercel, MySQL</div>
            </div>
            
            <div class="project-item">
                <div class="project-name">TODO LIST Mobile Application</div>
                <div class="project-description">
                    Developed a high-performance cross-platform task manager. Integrated native device SDKs for a seamless user experience.
                </div>
                <div style="font-size: 9px; color: #2980b9; font-weight: 600;">React Native, TypeScript, Android/iOS SDK</div>
            </div>
            
            <div class="project-item">
                <div class="project-name">EcoHaven Marketplace</div>
                <div class="project-description">
                    Sustainable second-hand marketplace backend. Integrated secure authentication and dynamic inventory management systems.
                </div>
                <div style="font-size: 9px; color: #2980b9; font-weight: 600;">TypeScript, Firebase, Auth</div>
            </div>
            
            <div class="main-section-title">CERTIFICATIONS & ACHIEVEMENTS</div>
            <div class="achievement-item">• 440+ Days Coding Streak - Consistent daily growth.</div>
            <div class="achievement-item">• 5-Day AI Agents Intensive Course with Google.</div>
            <div class="achievement-item">• Graduate Certificate in Data Analytics - PI LABS (2025).</div>
            <div class="achievement-item">• Deloitte Data Analytics & TATA Cybersecurity simulations.</div>
            <div class="achievement-item">• Kaggle Badges: Vampire, Code Forker, & Python Coder.</div>
            <div class="achievement-item">• GitHub Achievements: Pair Extraordinaire & Pull Shark.</div>
        </div>
    </div>
</body>
</html>
`;

async function generatePDF() {
    try {
        const browser = await puppeteer.launch({
            headless: 'new',
            args: ['--no-sandbox', '--disable-setuid-sandbox']
        });
        
        const page = await browser.newPage();
        await page.setContent(resumeHTML, { waitUntil: 'networkidle0' });
        
        // Set viewport to A4 size
        await page.setViewport({
            width: 2480,  // A4 width in pixels at 96 DPI
            height: 3508  // A4 height in pixels at 96 DPI
        });
        
        const pdfPath = path.join(__dirname, 'Sannith_Resume_Professional_Final.pdf');
        
        await page.pdf({
            path: pdfPath,
            format: 'A4',
            margin: 0,
            printBackground: true,
            scale: 1
        });
        
        await browser.close();
        
        console.log(`✓ Professional Resume Generated Successfully!`);
        console.log(`✓ File: ${pdfPath}`);
        console.log(`✓ All content (Summary, Experience, Projects, Certifications) included`);
        
    } catch (error) {
        console.error('Error generating PDF:', error);
        process.exit(1);
    }
}

generatePDF();
