import re

with open('admin.js', 'r', encoding='utf-8') as f:
    content = f.read()

def replace_defaults(func_name, new_defaults, text):
    func_pattern = re.compile(rf'function {func_name}\(\)\s*\{{.*?const data = getData\(\'.*?\'\) \|\| \{{\}};\s*(const defaults = \{{.*?\}});', re.DOTALL)
    match = func_pattern.search(text)
    if not match:
        print(f"Could not find defaults for {func_name}")
        return text
    
    old_defaults = match.group(1)
    return text.replace(old_defaults, new_defaults)

hero_defaults = """const defaults = {
            badge: 'Architecture & Design',
            title: 'Creative <span>Architecture Student</span> Passionate about Spatial Planning & Design',
            headline: 'Architectural Design • Interior • Landscape',
            description: "Hi, I'm <strong>Farah Maher Saleh</strong>. A detail-oriented Architecture student with a strong foundation in architectural design, technical drafting, and 3D visualization.",
            stat1Value: '4+',
            stat1Label: 'Key Projects',
            stat2Value: '2027',
            stat2Label: 'Expected Grad',
            cvFileName: 'Farah_Maher_CV.docx'
        }"""

about_defaults = """const defaults = {
            leadParagraph: 'Detail-oriented Architecture student at Damanhur University with a strong foundation in architectural design, spatial planning, technical drafting, and 3D visualization.',
            paragraph2: 'Experienced across academic and voluntary projects spanning educational facilities, commercial showrooms, and landscape master plans. Proficient in AutoCAD, SketchUp, Lumion, V-Ray, and Photoshop. Growing expertise in interior design visualization and UI/UX.',
            paragraph3: 'Eager to contribute creative design solutions and technical precision to a professional architectural firm.',
            feature1Title: 'Architectural Design',
            feature1Desc: 'Specialized in spatial planning, creating functional and aesthetic environments for residential and commercial spaces.',
            feature2Title: '3D Visualization',
            feature2Desc: 'Skilled in modeling and rendering realistic architectural and interior visualizations.',
            location: 'Damanhur, Beheira, Egypt',
            educationFocus: 'B.Sc. Architecture Engineering',
            graduationYear: 'Expected 2027',
            languages: 'Arabic (Native) • English (Good)'
        }"""

exp_defaults = """const defaults = {
            entries: [
                {
                    role: 'Primary School Design',
                    company: 'Academic Project',
                    badge: 'Architecture',
                    duration: '2023 – 2024',
                    bullets: [
                        'Designed an educational facility with structured zoning separating educational, administrative, and recreational areas to ensure safety and functionality.',
                        'Incorporated interactive outdoor learning areas promoting student engagement and physical activity.'
                    ],
                    skills: ['AutoCAD', 'SketchUp', 'Lumion', 'Photoshop']
                },
                {
                    role: 'Car Showroom Design',
                    company: 'Academic Project',
                    badge: 'Architecture',
                    duration: '2023 – 2024',
                    bullets: [
                        'Conceptualized a modern commercial showroom with a geometric facade balancing aesthetic impact and sun-shading functionality.',
                        'Produced complete hand-drawn documentation including plans, elevations, and perspectives; proposed sustainable cladding materials.'
                    ],
                    skills: ['Freehand sketching', 'Manual drafting', 'Marker rendering']
                },
                {
                    role: 'University Campus Landscape Design',
                    company: 'Academic Project',
                    badge: 'Landscape',
                    duration: '2024 – 2025',
                    bullets: [
                        'Developed a sustainable landscape master plan optimizing land use with multi-functional zones and clear pedestrian circulation.',
                        'Applied sustainable strategies including low-maintenance greenery selection and water-efficient irrigation planning.'
                    ],
                    skills: ['AutoCAD', 'SketchUp', 'Lumion', 'Photoshop']
                },
                {
                    role: 'Student Housing Landscape Design',
                    company: 'Voluntary Project',
                    badge: 'Landscape',
                    duration: '2024 – 2025',
                    bullets: [
                        'Designed gender-segregated spatial zoning ensuring privacy, comfort, and dedicated outdoor social areas for each housing zone.'
                    ],
                    skills: ['AutoCAD', 'SketchUp', 'Lumion']
                },
                {
                    role: 'Interior Design Visualization',
                    company: 'Personal Development',
                    badge: 'Interior',
                    duration: '2024 – Present',
                    bullets: [
                        'Self-directed exploration of space planning and photorealistic visualization across residential, commercial, and hospitality typologies.',
                        'Developing material selection and lighting technique skills.'
                    ],
                    skills: ['Interior Design', 'Visualization', 'Space Planning']
                }
            ]
        }"""

skills_defaults = """const defaults = {
            entries: [
                { name: 'AutoCAD', category: 'design', progress: 90 },
                { name: 'SketchUp', category: 'design', progress: 85 },
                { name: '3ds Max', category: 'design', progress: 70 },
                { name: 'Adobe Photoshop', category: 'design', progress: 80 },
                { name: 'Lumion', category: 'render', progress: 85 },
                { name: 'V-Ray for SketchUp', category: 'render', progress: 75 },
                { name: 'V-Ray for 3ds Max', category: 'render', progress: 65 },
                { name: 'Shop Drawings', category: 'drafting', progress: 85 },
                { name: 'Technical Drafting', category: 'drafting', progress: 90 },
                { name: 'Freehand Sketching', category: 'drafting', progress: 80 },
                { name: 'Problem-Solving', category: 'soft', progress: 85 },
                { name: 'Attention to Detail', category: 'soft', progress: 90 },
                { name: 'Time Management', category: 'soft', progress: 80 }
            ]
        }"""

certs_defaults = """const defaults = {
            entries: [
                {
                    title: 'Interior Design Basics',
                    issuer: 'Online Learning',
                    summary: 'Explored core interior design principles and visualization workflows.'
                },
                {
                    title: 'Advanced AutoCAD Drafting',
                    issuer: 'Engineering Syndicate',
                    summary: 'Mastered complex technical and shop drawings.'
                }
            ]
        }"""

edu_defaults = """const defaults = {
            institution: 'Damanhur University, Egypt',
            degree: 'B.Sc. in Architecture Engineering',
            faculty: 'Faculty of Engineering',
            graduationDate: 'Expected Graduation: July 2027',
            curriculum: 'Architecture Department',
            grade: 'Very Good'
        }"""

contact_defaults = """const defaults = {
            introParagraph: 'I am open to internships, entry-level opportunities, and graduate development programs in Architecture and Design. Please feel free to reach out via phone, email, or LinkedIn.',
            email: 'farahmaher164@gmail.com',
            phone: '+20 101 692 4332',
            location: 'Damanhur, Beheira, Egypt',
            linkedin: 'https://linkedin.com/in/farah-maher',
            linkedinDisplay: 'linkedin.com/in/farah-maher',
            web3formsKey: 'YOUR_ACCESS_KEY_HERE'
        }"""

seo_defaults = """const defaults = {
            pageTitle: 'Farah Maher | Architecture & Design Portfolio',
            metaDescription: 'Professional portfolio of Farah Maher, an Architecture student specializing in architectural design, interior, and landscape design.',
            metaKeywords: 'Farah Maher, Architecture, Architectural Design, Interior Design, Landscape Design, Damanhur University',
            ogTitle: 'Farah Maher | Architecture Portfolio',
            ogDescription: 'Explore the professional projects, skills, and designs of Farah Maher in Architecture.'
        }"""

footer_defaults = """const defaults = {
            copyrightText: '© 2026 Farah Maher. All Rights Reserved.',
            copyrightLink: '#'
        }"""

content = replace_defaults('renderHeroEditor', hero_defaults, content)
content = replace_defaults('renderAboutEditor', about_defaults, content)
content = replace_defaults('renderExperienceEditor', exp_defaults, content)
content = replace_defaults('renderSkillsEditor', skills_defaults, content)
content = replace_defaults('renderCertificationsEditor', certs_defaults, content)
content = replace_defaults('renderEducationEditor', edu_defaults, content)
content = replace_defaults('renderContactEditor', contact_defaults, content)
content = replace_defaults('renderSEOEditor', seo_defaults, content)
content = replace_defaults('renderFooterEditor', footer_defaults, content)

with open('admin.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done updating admin.js")
