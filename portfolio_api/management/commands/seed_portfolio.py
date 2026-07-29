from django.core.management.base import BaseCommand
from django.db import connection
from portfolio_api.models import (
    Profile, HomeContent, Project, SkillCategory, ExperienceEntry, Service,
)


def reset_table(model):
    """Truncate a table and restart its id sequence at 1 -- makes re-running
    this command idempotent and keeps project ids predictable."""
    table = model._meta.db_table
    with connection.cursor() as cursor:
        cursor.execute(f'TRUNCATE TABLE "{table}" RESTART IDENTITY CASCADE;')


class Command(BaseCommand):
    help = "Resets and seeds the database with the current, real portfolio content."

    def handle(self, *args, **options):
        # Truncate child-of-Project tables first (CASCADE handles this too,
        # but being explicit is clearer to read).
        reset_table(Service)
        reset_table(Project)
        reset_table(Profile)
        reset_table(HomeContent)
        reset_table(SkillCategory)
        reset_table(ExperienceEntry)

        # --- Profile --------------------------------------------------
        Profile.objects.create(
            name="DJEMAI Mohamed Erraid",
            role="Full-Stack Developer",
            photo_url="https://res.cloudinary.com/umxjpowx/image/upload/v1785082721/AAFuWkQu2jM_1724670310462_jnsj7m.jpg",
            school="ESI — École Nationale Supérieure d'Informatique, Algiers",
            speciality="SIL — Software Engineering",
            school_years="4th year",
            location="Algiers, Algeria",
            seeking="Summer 2026 internship",
            email="nm_djemai@esi.dz",
            phone="+213 776 262 511",
            github="https://github.com/Erraid7",
            linkedin="https://www.linkedin.com/in/djemai-mohamed-erraid-3835862b8/",
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

        # --- Home content -----------------------------------------------
        HomeContent.objects.create(
            tagline="This portfolio works like a real API client -- pick a request from the sidebar, hit Send, and the response renders as a real page instead of raw JSON.",
            how_to_use=[
                "Pick a request from the sidebar on the left (or the menu on mobile).",
                "Hit Send to see the response render below.",
                "Try editing the URL bar yourself -- some ids aren't pinned anywhere.",
            ],
        )

        # --- Projects -----------------------------------------------------
        # Created in this exact order so ids come out 1-7, matching the
        # frontend's sidebar (pins 1-6) and hidden-project id (7).
        esi_flow = Project.objects.create(
            slug="esi-flow", name="ESI Flow", role="Team Lead — 5-person team",
            pinned=True, platform="web",
            summary="A production, multi-role SaaS platform serving students, technicians, and admins at ESI.",
            bullets=[
                "Led a 5-member team through system design, database architecture, and end-to-end implementation using Agile sprints.",
                "Contributed roughly 80% of the Express/TypeScript/PostgreSQL codebase, including JWT-secured role-based access control across 3 user types and the full Prisma schema.",
                "Validated cross-layer reliability across 15+ frontend pages and the REST API with function and integration tests, then deployed to Vercel and Render.",
            ],
            stack=["Next.js", "TypeScript", "Express.js", "Prisma", "PostgreSQL", "JWT"],
            media=[
                {"type": "image", "src": "https://res.cloudinary.com/umxjpowx/image/upload/v1785167285/Capture_d_%C3%A9cran_2026-07-27_163903_hyeabf.png", "alt": "ESI Flow Responsive WebApp"},
                {"type": "image", "src": "https://res.cloudinary.com/umxjpowx/image/upload/v1785167265/Capture_d_%C3%A9cran_2026-07-27_164013_wubf58.png", "alt": "ESI Flow login"},
                {"type": "image", "src": "https://res.cloudinary.com/umxjpowx/image/upload/v1785167254/Capture_d_%C3%A9cran_2026-07-27_163945_i18lxg.png", "alt": "ESI Flow home"},
                {"type": "image", "src": "https://res.cloudinary.com/umxjpowx/image/upload/v1785167243/Capture_d_%C3%A9cran_2026-07-27_164124_wd7ki9.png", "alt": "ESI Flow admin panel"},
                {"type": "image", "src": "https://res.cloudinary.com/umxjpowx/image/upload/v1785167240/Capture_d_%C3%A9cran_2026-07-27_164215_gevbgq.png", "alt": "ESI Flow tasks management"},
                {"type": "image", "src": "https://res.cloudinary.com/umxjpowx/image/upload/v1785167241/Capture_d_%C3%A9cran_2026-07-27_164140_yprwu1.png", "alt": "ESI Flow requests management"},
            ],
            links={
                "live": {"available": True, "url": "https://esi-flow.vercel.app"},
                "github": {"available": True, "url": "https://github.com/Erraid7/esi_flow_front"},
                "demoVideo": {"available": True, "url": "https://drive.google.com/file/u/0/d/1tgZCjCQEHpD4X_ky7EZoUFjWV6vSUqin/view"},
            },
            docs_markdown="## ESI Flow\n\nESI Flow is a multi-role SaaS platform built to give ESI's students, technicians, and admins a single system for filing, tracking, and resolving requests — the kind of internal tool a school actually needs but rarely has.\n\nAs team lead on a 5-person team, I owned the system design and database architecture from the start: a Prisma/PostgreSQL schema supporting 3 distinct user roles, each with different permissions enforced through JWT-secured role-based access control. I wrote roughly 80% of the Express/TypeScript backend myself, while coordinating the rest of the team through Agile sprints — planning, reviewing, and keeping the whole thing shippable rather than just architecturally correct.\n\nThe frontend spans 15+ pages across the three roles, backed by a REST API validated with function and integration tests before deployment. It's live today on Vercel (frontend) and Render (backend), not a class demo that only ran once.",
        )

        khatma = Project.objects.create(
            slug="khatma", name="Khatma", role="Solo Full-Stack Developer",
            pinned=True, platform="mobile",
            summary="A full-stack Quran memorization platform, sole-authored across web and mobile.",
            bullets=[
                "Covered 3 user roles (Hafiz, Teacher, Admin) across a Next.js web app and a cross-platform Flutter app.",
                "Designed the full Prisma/PostgreSQL schema and built a secure REST API with JWT authentication, independently.",
                "Implemented all backend logic in TypeScript/Express, from data model to deployed service.",
            ],
            stack=["Next.js", "TypeScript", "Flutter", "Node.js", "Express", "Prisma", "PostgreSQL", "JWT"],
            media=[
                {"type": "image", "src": "https://res.cloudinary.com/umxjpowx/image/upload/v1785167264/Capture_d_%C3%A9cran_2026-07-27_164351_izzuyq.png", "alt": "Khatma home"},
                {"type": "image", "src": "https://res.cloudinary.com/umxjpowx/image/upload/v1785167248/Capture_d_%C3%A9cran_2026-07-27_164431_d0ymgv.png", "alt": "Khatma student dashboard"},
                {"type": "image", "src": "https://res.cloudinary.com/umxjpowx/image/upload/v1785167228/Capture_d_%C3%A9cran_2026-07-27_164447_gnfif0.png", "alt": "Khatma hifz map"},
            ],
            links={
                "live": {"available": False, "reason": "Not deployed publicly yet — currently used within a closed pilot group."},
                "github": {"available": True, "url": "https://github.com/Erraid7/khatma-frontend"},
                "demoVideo": {"available": False, "reason": "No demo recording yet — check back soon."},
            },
            docs_markdown="## Khatma\n\nKhatma is a Quran memorization platform built end-to-end, alone — architecture, schema, backend, and both front-facing clients.\n\nIt supports 3 distinct roles: the Hafiz (student) tracking their own memorization progress, the Teacher reviewing and guiding that progress, and an Admin overseeing the whole structure. Rather than build one interface and call it done, I shipped two: a Next.js web app and a cross-platform Flutter app, both talking to the same backend.\n\nThe backend is a TypeScript/Express API secured with JWT authentication, sitting on a Prisma/PostgreSQL schema I designed to model the relationships between students, teachers, and memorization progress cleanly. Every layer — data model, API, both clients — was my own work, which made this the project where I learned the most about keeping a solo build coherent across platforms instead of just fast.",
        )

        pharmaflow = Project.objects.create(
            slug="pharmaflow", name="PharmaFlow", role="Full-Stack Developer",
            pinned=True, platform="mobile",
            summary="A live, mobile-first pharmacy management platform for tracking and ordering pharmacy products, with role-based access for admins and workers.",
            bullets=[
                "Built a fully separated frontend/backend architecture — Next.js 16 frontend, Express 5 API — deployable and scalable independently.",
                "Implemented JWT authentication over HttpOnly cookies with Admin/Worker roles, so only admins can mark products as ordered or manage users.",
                "Designed a mobile-first responsive UI (bottom navigation on mobile, sidebar on desktop) covering the full 320px–1440px range, with real-time product status updates, search/filter, and toast feedback on every action.",
                "Hardened the API with Zod validation, rate limiting, Helmet, and CORS, and shipped a seed script for demo admin/worker accounts.",
            ],
            stack=["Next.js", "TypeScript", "Express.js", "MongoDB", "Mongoose", "JWT", "TanStack Query", "Zod", "Tailwind CSS"],
            media=[
                {"type": "image", "src": "https://res.cloudinary.com/umxjpowx/image/upload/v1785189087/capture_d_%C3%A9cran_2026-07-27_164448_yqkzog.png", "alt": "PharmaFlow login"},
                {"type": "image", "src": "https://res.cloudinary.com/umxjpowx/image/upload/v1785189073/Capture_d_%C3%A9cran_2026-07-27_224722_esbkua.png", "alt": "PharmaFlow needed products"},
                {"type": "image", "src": "https://res.cloudinary.com/umxjpowx/image/upload/v1785189072/Capture_d_%C3%A9cran_2026-07-27_224750_wotcs3.png", "alt": "PharmaFlow ordered products"},
                {"type": "image", "src": "https://res.cloudinary.com/umxjpowx/image/upload/v1785190940/Copy_of_ESI_FLOW_PROJECT_vffkty.png", "alt": "PharmaFlow mobile view"},
            ],
            links={
                "live": {"available": True, "url": "https://pharmacy-product-platform.vercel.app"},
                "github": {"available": True, "url": "https://github.com/Erraid7/pharmacy-product-platform"},
                "demoVideo": {"available": False, "reason": "No walkthrough video — the live site above covers this."},
            },
            docs_markdown="## PharmaFlow\n\nPharmaFlow is a pharmacy product management platform built for real day-to-day use, not a class exercise — pharmacy staff track which products are needed and mark them as ordered once resolved, with the whole flow built mobile-first since that's how the people actually using it work.\n\nThe architecture is a fully separated frontend and backend: a Next.js 16 app (shadcn/ui, Tailwind CSS v4, TanStack Query, React Hook Form + Zod) talking to an Express 5 API (MongoDB/Mongoose, JWT auth over HttpOnly cookies, Zod validation, Helmet, CORS, and rate limiting) — deployable and scaled independently of each other.\n\nAuthentication distinguishes Admin and Worker roles: both can view and manage products, but only admins can mark a product as ordered or manage user accounts. The UI adapts fully across 320px–1440px, switching between bottom navigation on mobile and a sidebar on desktop, with empty states, loading skeletons, and toast notifications on every action so nothing feels like it silently failed.\n\nIt's live in production today, seeded with demo admin and worker accounts for anyone who wants to try it out.",
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
            media=[
                {"type": "image", "src": "https://res.cloudinary.com/umxjpowx/image/upload/v1785268059/ChatGPT_Image_Jul_28_2026_08_37_35_PM_dlhrls.png", "alt": "Refactoring Swarm pipeline"},
            ],
            links={
                "live": {"available": False, "reason": "This is a CLI/pipeline tool, not a hosted app — no live URL applies."},
                "github": {"available": True, "url": "https://github.com/Erraid7/Refactoring-Swarm-Equipe-24"},
                "demoVideo": {"available": False, "reason": "Recording planned — check back soon."},
            },
            docs_markdown="## Refactoring Swarm\n\nRefactoring Swarm is an autonomous pipeline of 4 LLM-powered agents — Auditor, Fixer, Tester, Documenter — that walks through a Python codebase the way a careful senior engineer would, without a human in the loop.\n\nThe Auditor analyzes code quality and flags issues; the Fixer proposes and applies refactors; the Tester generates tests against the refactored code; the Documenter updates documentation to match. Each agent has a narrow, clearly separated responsibility, and each one's output becomes verified input for the next — so mistakes don't silently compound down the chain.\n\nThis was my first real exploration of applying swarm-intelligence principles (coordination through role separation, not a single do-everything prompt) to a genuine engineering workflow, rather than a toy demo. It's the project I'd point to if asked how far multi-agent systems can actually go in day-to-day software work.",
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
            media=[
                {"type": "image", "src": "https://res.cloudinary.com/umxjpowx/image/upload/v1785193429/Capture_d_%C3%A9cran_2026-07-27_235001_avdi6y.png", "alt": "CSE Club Website"},
                {"type": "image", "src": "https://res.cloudinary.com/umxjpowx/image/upload/v1785193459/Capture_d_%C3%A9cran_2026-07-27_235217_pweay1.png", "alt": "CSE Club About"},
                {"type": "image", "src": "https://res.cloudinary.com/umxjpowx/image/upload/v1785193436/Capture_d_%C3%A9cran_2026-07-27_235050_jkazwo.png", "alt": "CSE Club TrustedBy"},
                {"type": "image", "src": "https://res.cloudinary.com/umxjpowx/image/upload/v1785193452/Capture_d_%C3%A9cran_2026-07-27_235134_keuusl.png", "alt": "CSE Club Events"},
                {"type": "image", "src": "https://res.cloudinary.com/umxjpowx/image/upload/v1785193469/Capture_d_%C3%A9cran_2026-07-27_235418_wcdvbp.png", "alt": "CSE Club Community"},
            ],
            links={
                "live": {"available": True, "url": "https://cse.club/"},
                "github": {"available": False, "reason": "Confidential club project."},
                "demoVideo": {"available": False, "reason": "No walkthrough video recorded yet."},
            },
            docs_markdown="## CSE Club Website\n\nThe public-facing website for Club Scientifique de l'ESI (CSE), the 1,000+ member student tech club I now lead as president.\n\nI contributed responsive frontend components used across the site, and built the sponsor section's infinite-scroll slider — direction-reactive, so it responds naturally to how a visitor scrolls rather than looping on a fixed timer. Small in scope compared to the other projects here, but it's real, shipped, and still live for the club today.",
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
            media=[
                {"type": "image", "src": "https://res.cloudinary.com/umxjpowx/image/upload/v1785191802/Capture_d_%C3%A9cran_2026-07-27_233315_xhy89x.png", "alt": "ESI Run dashboard"},
                {"type": "image", "src": "https://res.cloudinary.com/umxjpowx/image/upload/v1785191799/Capture_d_%C3%A9cran_2026-07-27_233326_i37xb8.png", "alt": "ESI Run user management"},
                {"type": "image", "src": "https://res.cloudinary.com/umxjpowx/image/upload/v1785191799/Capture_d_%C3%A9cran_2026-07-27_233406_bq9fmm.png", "alt": "ESI Run new user"},
                {"type": "image", "src": "https://res.cloudinary.com/umxjpowx/image/upload/v1785191796/Capture_d_%C3%A9cran_2026-07-27_233419_qc4mj9.png", "alt": "ESI Run transport passes"},
                {"type": "image", "src": "https://res.cloudinary.com/umxjpowx/image/upload/v1785191799/Capture_d_%C3%A9cran_2026-07-27_233429_b7ijxx.png", "alt": "ESI Run pass details"},
                {"type": "image", "src": "https://res.cloudinary.com/umxjpowx/image/upload/v1785191795/Capture_d_%C3%A9cran_2026-07-27_233507_mqzkwo.png", "alt": "ESI Run new pass"},
                {"type": "image", "src": "https://res.cloudinary.com/umxjpowx/image/upload/v1785191796/Capture_d_%C3%A9cran_2026-07-27_233540_jrnxqa.png", "alt": "ESI Run complaints"},
                {"type": "image", "src": "https://res.cloudinary.com/umxjpowx/image/upload/v1785191796/Capture_d_%C3%A9cran_2026-07-27_233559_yktook.png", "alt": "ESI Run new complaint"},
            ],
            links={
                "live": {"available": False, "reason": "Desktop application, there's no hosted version."},
                "github": {"available": True, "url": "https://github.com/Erraid7/javaFX_project"},
                "demoVideo": {"available": False, "reason": "Recording planned — check back soon."},
            },
            docs_markdown="## ESI Run\n\nESI Run is a desktop management system for a public-transportation network: user accounts, transit pass issuance and renewal, complaint handling, and pass validation, all in one Java/JavaFX application.\n\nI implemented the full business logic across these subsystems with CSV-based persistence, then backed it with unit and integration tests across the user, pass, and validation flows — the part of the project that mattered most, since a transit system with silent validation bugs is worse than no system at all.\n\nIt's a good example of solid engineering discipline outside the web stack I use most: same care about correctness and testing, applied to a desktop Java codebase instead of a REST API.",
        )

        Project.objects.create(
            slug="hamsynet", name="HamsyNet",
            role="Full-Stack Developer (confidential client project)",
            pinned=False, platform="web",
            summary="A confidential, full Arabic (RTL) platform — a kind of mini ERP — for managing an organisation's members, executive structure, roles, and files.",
            bullets=[
                "Built a role-based authentication and authorization system reflecting the organisation's real executive hierarchy, not just a flat admin/user split.",
                "Modeled the organisation's structure of executive members (\"responsables\") with scoped roles and permissions tied to that structure.",
                "Designed a fully right-to-left (RTL) Arabic interface for a non-technical member base — a different UX/i18n problem than the LTR work elsewhere on this site.",
                "Implemented file management integrated directly into the member and role workflows.",
            ],
            stack=["Next.js", "TypeScript", "Express.js", "PostgreSQL", "Prisma", "JWT"],
            media=[],
            links={
                "live": {"available": False, "reason": "Confidential — the client hasn't authorized a public link."},
                "github": {"available": False, "reason": "Private repository under client confidentiality."},
                "demoVideo": {"available": False, "reason": "Not permitted to share due to client confidentiality."},
            },
            docs_markdown="## HamsyNet\n\nHamsyNet is a confidential full-stack platform built for a private organisation — internally, it's basically a mini ERP: it manages the organisation's members, its executive hierarchy (\"responsables\"), role assignment, and internal files, all in one place.\n\nThe interesting engineering problem here wasn't CRUD, it was modeling a real executive tree faithfully enough that role-based authorization actually reflects how authority flows through the organisation, rather than a generic admin/user split. The entire interface is Arabic and right-to-left, built for a non-technical member base — a genuinely different UX and internationalization problem than anything else in this portfolio.\n\nOut of respect for the client's confidentiality, that's as specific as this one gets — no public link, repo, or screenshots. If you want more detail, ask me directly.",
        )

        # --- Skills ---------------------------------------------------
        SkillCategory.objects.create(key="frontend", label="Frontend", order=1, items=["Next.js", "React", "TypeScript", "Tailwind CSS", "HTML5", "CSS3", "JavaScript (ES6+)"])
        SkillCategory.objects.create(key="backend", label="Backend", order=2, items=["Node.js", "Express.js", "REST API design", "JWT Authentication", "OAuth"])
        SkillCategory.objects.create(key="database", label="Database", order=3, items=["PostgreSQL", "Prisma ORM", "Firebase", "SQL schema design"])
        SkillCategory.objects.create(key="mobile", label="Mobile", order=4, items=["Flutter", "Dart"])
        SkillCategory.objects.create(key="ai", label="AI & Agents", order=5, items=["Python", "LLM APIs", "Multi-agent systems", "Swarm intelligence"])
        SkillCategory.objects.create(key="design", label="Design & UI", order=6, items=["Figma", "Design systems", "Component libraries", "Dark mode"])
        SkillCategory.objects.create(key="devops", label="Testing & DevOps", order=7, items=["Jest", "Integration testing", "Git", "GitHub", "Vercel", "Render"])

        # --- Experience -------------------------------------------------
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

        # --- Services -----------------------------------------------------
        Service.objects.create(
            key="fullstack", order=1,
            title="Full-Stack Web Applications",
            tagline="A complete product, built and shipped -- not just a frontend.",
            description="End-to-end ownership of a web application: system design, database schema, backend API, and the frontend that sits on top of it, deployed and actually working -- the same way ESI Flow, Khatma, and PharmaFlow were built.",
            deliverables=[
                "System design and database schema from scratch",
                "A working REST API with authentication and role-based access",
                "A responsive frontend, built and connected to that API",
                "Deployment to production, not just a local demo",
            ],
            example_project=esi_flow,
            example_label="See it in ESI Flow",
        )
        Service.objects.create(
            key="backend-api", order=2,
            title="Backend & API Systems",
            tagline="The part that has to be right, even when no one sees it.",
            description="For teams that already have a frontend (or a designer) but need a real backend behind it: schema design, authentication, role-based permissions, and an API built to hold up under real use -- not just pass a demo.",
            deliverables=[
                "Database schema design (PostgreSQL / Prisma)",
                "JWT authentication with role-based access control",
                "A documented REST API, tested before it ships",
                "Guidance on hosting and deployment",
            ],
            example_project=pharmaflow,
            example_label="See it in PharmaFlow",
        )
        Service.objects.create(
            key="mobile-first", order=3,
            title="Mobile-First & Cross-Platform Apps",
            tagline="Built for the screen people actually use.",
            description="Responsive, mobile-first web apps or true cross-platform builds with Flutter, for products where most real usage happens on a phone, not a desktop demo.",
            deliverables=[
                "Mobile-first responsive design, not a desktop layout squeezed down",
                "Cross-platform delivery with Flutter when a native-feeling app matters",
                "Real device testing across the 320px--1440px range",
                "The same backend/API work from the other two services, if needed",
            ],
            example_project=khatma,
            example_label="See it in Khatma",
        )

        self.stdout.write(self.style.SUCCESS("Portfolio reset and seeded -- 7 projects, 7 skill categories, 5 experience entries, 3 services."))