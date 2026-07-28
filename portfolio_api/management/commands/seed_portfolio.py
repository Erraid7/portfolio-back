from django.core.management.base import BaseCommand
from portfolio_api.models import Profile, HomeContent, Project, SkillCategory, ExperienceEntry


class Command(BaseCommand):
    help = "Seeds the database with the real portfolio content."

    def handle(self, *args, **options):
        Profile.objects.all().delete()
        Profile.objects.create(
            name="DJEMAI Mohamed Erraid",
            role="Full-Stack Developer",
            photo_url="https://placehold.co/256x256/1a1a1e/8a8a8e?text=DJ",
            school="ESI — École Nationale Supérieure d'Informatique, Algiers",
            speciality="SIL — Software Engineering",
            school_years="4th year",
            location="Algiers, Algeria",
            seeking="Summer 2026 internship",
            email="nm_djemai@esi.dz",
            phone="+213 776 262 511",
            github="https://github.com/Erraid7",
            linkedin="https://www.linkedin.com/in/djemai-mohamed-erraid",
            bio=[
                "4th-year Software Engineering (SIL) student at ESI Algiers who ships production systems rather than class exercises — ESI Flow is a live multi-role SaaS, Khatma is a solo-built cross-platform app, PharmaFlow is a live mobile-first platform, and Refactoring Swarm is an autonomous multi-agent pipeline.",
                "President of CSE (Club Scientifique de l'ESI), a 1,000+ member student tech club with 10 departments; organizer of the DATAHACK hackathon series; mentor at HACKIN and DevSprint hackathons.",
            ],
            journey=[
                "Like a lot of people in this field, it started with curiosity about how the things I used every day actually worked — that curiosity turned into building small tools, then real applications, then systems other people would actually depend on.",
                "ESI and SIL gave me the fundamentals, but CSE is where I learned to build with other people instead of just alone — leading a 1,000+ member club, organizing DATAHACK, and mentoring at hackathons taught me as much about shipping software as any project did on its own.",
                "Right now I'm chasing an internship where I can bring that same production mindset from day one — a team building real systems, not prototypes, where full-stack ownership and careful engineering actually matter.",
            ],
            interests=["Systems design", "Multi-agent AI", "Mentoring", "Hackathons", "Open source"],
        )

        HomeContent.objects.all().delete()
        HomeContent.objects.create(
            tagline="This portfolio works like a real API client -- pick a request from the sidebar, hit Send, and the response renders as a real page instead of raw JSON.",
            how_to_use=[
                "Pick a request from the sidebar on the left (or the menu on mobile).",
                "Hit Send to see the response render below.",
                "Try editing the URL bar yourself -- some ids aren't pinned anywhere.",
            ],
        )

        Project.objects.all().delete()
        Project.objects.create(
            slug="esi-flow", name="ESI Flow", role="Team Lead — 5-person team",
            pinned=True, platform="web",
            summary="A production, multi-role SaaS platform serving students, technicians, and admins at ESI.",
            bullets=[
                "Led a 5-member team through system design, database architecture, and end-to-end implementation using Agile sprints.",
                "Contributed roughly 80% of the Express/TypeScript/PostgreSQL codebase, including JWT-secured role-based access control across 3 user types and the full Prisma schema.",
                "Validated cross-layer reliability across 15+ frontend pages and the REST API with function and integration tests, then deployed to Vercel and Render.",
            ],
            stack=["Next.js", "TypeScript", "Express.js", "Prisma", "PostgreSQL", "JWT"],
            media=[],
            links={
                "live": {"available": True, "url": "https://esi-flow.vercel.app"},
                "github": {"available": True, "url": "https://github.com/Erraid7"},
                "demoVideo": {"available": False, "reason": "No walkthrough video recorded yet — the live site above covers this."},
            },
            docs_markdown="## ESI Flow\n\nESI Flow is a multi-role SaaS platform built to give ESI's students, technicians, and admins a single system for filing, tracking, and resolving requests...",
        )
        Project.objects.create(
            slug="khatma", name="Khatma", role="Solo Full-Stack Developer",
            pinned=True, platform="mobile",
            summary="A full-stack Quran memorization platform, sole-authored across web and mobile.",
            bullets=[
                "Covered 3 user roles (Hafiz, Teacher, Admin) across a Next.js web app and a cross-platform Flutter app.",
                "Designed the full Prisma/PostgreSQL schema and built a secure REST API with JWT authentication, independently.",
                "Implemented all backend logic in TypeScript/Express, from data model to deployed service.",
            ],
            stack=["Next.js", "TypeScript", "Flutter", "Node.js", "Express", "Prisma", "PostgreSQL", "JWT"],
            media=[],
            links={
                "live": {"available": False, "reason": "Not deployed publicly yet — currently used within a closed pilot group."},
                "github": {"available": True, "url": "https://github.com/Erraid7"},
                "demoVideo": {"available": False, "reason": "No demo recording yet — check back soon."},
            },
            docs_markdown="## Khatma\n\nKhatma is a Quran memorization platform built end-to-end, alone...",
        )
        Project.objects.create(
            slug="refactoring-swarm", name="Refactoring Swarm", role="Designer & Builder",
            pinned=True, platform="cli",
            summary="An autonomous 4-agent pipeline — Auditor, Fixer, Tester, Documenter — that reviews, refactors, tests, and documents Python code.",
            bullets=[
                "Eliminated manual code-review overhead by chaining agents that analyze code quality, propose refactors, generate tests, and update documentation.",
                "Applied swarm intelligence principles to coordinate LLM-powered agents with clearly separated responsibilities.",
                "Structured inter-agent communication so each agent's output becomes verified input for the next.",
            ],
            stack=["Python", "LLM APIs", "Multi-agent systems"],
            media=[],
            links={
                "live": {"available": False, "reason": "This is a CLI/pipeline tool, not a hosted app — no live URL applies."},
                "github": {"available": True, "url": "https://github.com/Erraid7"},
                "demoVideo": {"available": False, "reason": "Recording planned — check back soon."},
            },
            docs_markdown="## Refactoring Swarm\n\nAn autonomous pipeline of 4 LLM-powered agents...",
        )
        Project.objects.create(
            slug="esi-run", name="ESI Run", role="Developer",
            pinned=True, platform="desktop",
            summary="A desktop public-transportation management system: accounts, pass management, complaint handling, and validation workflows.",
            bullets=[
                "Implemented full business logic in Java/JavaFX with CSV-based persistence.",
                "Wrote unit and integration tests across the user, pass, and validation subsystems.",
            ],
            stack=["Java", "JavaFX"],
            media=[],
            links={
                "live": {"available": False, "reason": "Desktop application — not applicable, there's no hosted version."},
                "github": {"available": True, "url": "https://github.com/Erraid7"},
                "demoVideo": {"available": False, "reason": "Recording planned — check back soon."},
            },
            docs_markdown="## ESI Run\n\nA desktop management system for a public-transportation network...",
        )
        Project.objects.create(
            slug="cse-website", name="CSE Club Website", role="Contributor",
            pinned=True, platform="web",
            summary="The public site for Club Scientifique de l'ESI — responsive components and an infinite-scroll, direction-reactive sponsor slider.",
            bullets=[
                "Built responsive frontend components used across the club's public site.",
                "Implemented an infinite-scroll sponsor slider with direction-reactive animation.",
            ],
            stack=["Next.js", "TypeScript", "Tailwind CSS"],
            media=[],
            links={
                "live": {"available": False, "reason": "Public URL not yet finalized — replace with the real link when live."},
                "github": {"available": True, "url": "https://github.com/Erraid7"},
                "demoVideo": {"available": False, "reason": "No walkthrough video recorded yet."},
            },
            docs_markdown="## CSE Club Website\n\nThe public-facing website for Club Scientifique de l'ESI...",
        )
        Project.objects.create(
            slug="pharmaflow", name="PharmaFlow", role="Full-Stack Developer",
            pinned=True, platform="mobile",
            summary="A live, mobile-first pharmacy management platform for tracking and ordering pharmacy products, with role-based access for admins and workers.",
            bullets=[
                "Built a fully separated frontend/backend architecture — Next.js 16 frontend, Express 5 API — deployable and scalable independently.",
                "Implemented JWT authentication over HttpOnly cookies with Admin/Worker roles.",
                "Designed a mobile-first responsive UI covering 320px–1440px, with real-time product status updates.",
                "Hardened the API with Zod validation, rate limiting, Helmet, and CORS.",
            ],
            stack=["Next.js", "TypeScript", "Express.js", "MongoDB", "Mongoose", "JWT", "TanStack Query", "Zod", "Tailwind CSS"],
            media=[],
            links={
                "live": {"available": True, "url": "https://pharmacy-product-platform.vercel.app"},
                "github": {"available": False, "reason": "Repository is private for now — happy to walk through the code on request."},
                "demoVideo": {"available": False, "reason": "No walkthrough video recorded yet — the live site above covers this."},
            },
            docs_markdown="## PharmaFlow\n\nPharmaFlow is a pharmacy product management platform built for real day-to-day use...",
        )
        Project.objects.create(
            slug="hamsynet", name="HamsyNet",
            role="Full-Stack Developer (confidential client project)",
            pinned=False, platform="web",
            summary="A confidential, full Arabic (RTL) platform — a kind of mini ERP — for managing an organisation's members, executive structure, roles, and files.",
            bullets=[
                "Built a role-based authentication and authorization system reflecting the organisation's real executive hierarchy.",
                "Modeled the organisation's structure of executive members (\"responsables\") with scoped roles and permissions.",
                "Designed a fully right-to-left (RTL) Arabic interface for a non-technical member base.",
                "Implemented file management integrated directly into the member and role workflows.",
            ],
            stack=["Next.js", "TypeScript", "Express.js", "PostgreSQL", "Prisma", "JWT"],
            media=[],
            links={
                "live": {"available": False, "reason": "Confidential — the client hasn't authorized a public link."},
                "github": {"available": False, "reason": "Private repository under client confidentiality."},
                "demoVideo": {"available": False, "reason": "Not permitted to share due to client confidentiality."},
            },
            docs_markdown="## HamsyNet\n\nA confidential full-stack platform for a private organisation...",
        )

        SkillCategory.objects.all().delete()
        SkillCategory.objects.create(key="frontend", label="Frontend", order=1, items=["Next.js", "React", "TypeScript", "Tailwind CSS", "HTML5", "CSS3", "JavaScript (ES6+)"])
        SkillCategory.objects.create(key="backend", label="Backend", order=2, items=["Node.js", "Express.js", "REST API design", "JWT Authentication", "OAuth"])
        SkillCategory.objects.create(key="database", label="Database", order=3, items=["PostgreSQL", "Prisma ORM", "Firebase", "SQL schema design"])
        SkillCategory.objects.create(key="mobile", label="Mobile", order=4, items=["Flutter", "Dart"])
        SkillCategory.objects.create(key="ai", label="AI & Agents", order=5, items=["Python", "LLM APIs", "Multi-agent systems", "Swarm intelligence"])
        SkillCategory.objects.create(key="design", label="Design & UI", order=6, items=["Figma", "Design systems", "Component libraries", "Dark mode"])
        SkillCategory.objects.create(key="devops", label="Testing & DevOps", order=7, items=["Jest", "Integration testing", "Git", "GitHub", "Vercel", "Render"])

        ExperienceEntry.objects.all().delete()
        ExperienceEntry.objects.create(
            role="Freelance Full-Stack Developer", org="Independent",
            period="2025 -- Present", is_current=True, order=1,
            bullets=[
                "Building production systems directly for clients end-to-end — requirements, architecture, and deployment — including PharmaFlow and HamsyNet.",
                "Working solo across the full stack: schema design, API design and auth, and the frontend clients that sit on top of them.",
            ],
        )
        ExperienceEntry.objects.create(
            role="President", org="Club Scientifique de l'ESI (CSE)",
            period="08/2025 -- 08/2026", is_current=False, order=2,
            bullets=[
                "Led a 1,000+ member organisation across 10 departments — strategy, budget, Agile team coordination.",
                "Delivered DATAHACK 3 (2025/2026) as the year's flagship event.",
                "Drove new project launches, inter-club partnerships, and a structured workshop programme.",
            ],
        )
        ExperienceEntry.objects.create(
            role="Mentor", org="HACKIN 7.0 Hackathon & DevSprint",
            period="2024 -- 2025", is_current=False, order=3,
            bullets=["Coached student teams on full-stack architecture, REST API design, and sprint-based delivery."],
        )
        ExperienceEntry.objects.create(
            role="Logistics Manager — RELEV Dept.", org="Club Scientifique de l'ESI (CSE)",
            period="08/2024 -- 07/2025", is_current=False, order=4,
            bullets=["Delivered DATAHACK 2 — 120 participants, largest edition at the time — coordinating a 50-person committee."],
        )
        ExperienceEntry.objects.create(
            role="Workshop Instructor & Multimedia Member", org="Club Scientifique de l'ESI (CSE)",
            period="11/2023 -- 07/2024", is_current=False, order=5,
            bullets=[
                "Designed and delivered 5 technical workshops (C, Pascal, HTML/CSS/JS, Back-End, GitHub) to ~20 students per session.",
                "Supported club media and helped organise DATAHACK 1.",
            ],
        )

        self.stdout.write(self.style.SUCCESS("Portfolio seeded."))