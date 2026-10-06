<picture>
  <source media="(prefers-color-scheme: dark) and (prefers-reduced-motion: reduce)" srcset="./assets/masthead-dark.png" />
  <source media="(prefers-reduced-motion: reduce)" srcset="./assets/masthead-light.png" />
  <source media="(prefers-color-scheme: dark)" srcset="./assets/masthead-dark.gif" />
  <img src="./assets/masthead-light.gif" width="100%" alt="Muhammad Sibtain Asad — Software Engineer. Lahore, Pakistan. SIBTAIN-ASAD on GitHub." />
</picture>

[Portfolio](https://www.sibtainasad.com/) &nbsp; / &nbsp; [LinkedIn](https://www.linkedin.com/in/sibtain-asad/) &nbsp; / &nbsp; [Repositories](https://github.com/SIBTAIN-ASAD?tab=repositories)

I’m **Muhammad Sibtain Asad**, a software engineer based in **Lahore, Pakistan**. My experience spans backend architecture, full-stack enterprise applications, data-collection pipelines, and LLM evaluation. I work primarily with **Python, Django, FastAPI, React, and TypeScript**.

<p>
<a href="#contributions"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/nav-contributions-slim-dark.svg" /><img src="./assets/nav-contributions-slim-light.svg" alt="Open source" width="120" /></picture></a>
<a href="#experience"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/nav-experience-slim-dark.svg" /><img src="./assets/nav-experience-slim-light.svg" alt="Experience" width="120" /></picture></a>
<a href="#projects"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/nav-projects-slim-dark.svg" /><img src="./assets/nav-projects-slim-light.svg" alt="Projects" width="120" /></picture></a>
<a href="#skills"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/nav-skills-slim-dark.svg" /><img src="./assets/nav-skills-slim-light.svg" alt="Toolkit" width="120" /></picture></a>
</p>

At **NavForward**, my work covers backend services and distributed scraping pipelines. Previously, I worked on **AI-agent evaluation at Turing**, **healthcare and AI workflow products at Devsinc**, and **production operations at i2c**. I also contribute fixes, typing improvements, and regression tests to open source.

<a id="contributions"></a>

## Open-source contributions

Selected fixes and improvements **merged upstream**. Each links to the original pull request.

<a href="https://github.com/apache/airflow/pull/72659">
<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="./assets/contribution-airflow-mobile-slim-dark.png" />
  <source media="(max-width: 600px)" srcset="./assets/contribution-airflow-mobile-slim-light.png" />
  <source media="(prefers-color-scheme: dark)" srcset="./assets/contribution-airflow-slim-dark.png" />
  <img src="./assets/contribution-airflow-slim-light.png" width="100%" alt="Apache Airflow: merged async datetime sensor fix, pull request 72659." />
</picture>
</a>

<a href="https://github.com/typeddjango/django-stubs/pull/3642">
<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="./assets/contribution-django-mobile-slim-dark.png" />
  <source media="(max-width: 600px)" srcset="./assets/contribution-django-mobile-slim-light.png" />
  <source media="(prefers-color-scheme: dark)" srcset="./assets/contribution-django-slim-dark.png" />
  <img src="./assets/contribution-django-slim-light.png" width="100%" alt="django-stubs: merged mutable request typing helper, pull request 3642." />
</picture>
</a>

<a href="https://github.com/amd/gaia/pull/3263">
<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="./assets/contribution-gaia-mobile-slim-dark.png" />
  <source media="(max-width: 600px)" srcset="./assets/contribution-gaia-mobile-slim-light.png" />
  <source media="(prefers-color-scheme: dark)" srcset="./assets/contribution-gaia-slim-dark.png" />
  <img src="./assets/contribution-gaia-slim-light.png" width="100%" alt="AMD Gaia: merged Telegram media feedback and regression test, pull request 3263." />
</picture>
</a>

<details>
<summary><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/control-contributions-slim-dark.svg" /><img src="./assets/control-contributions-slim-light.svg" width="320" align="absmiddle" alt="Show or hide: Contribution details & all merged pull requests" /></picture></summary>

These changes were accepted and merged into the upstream projects. Each addresses a specific failure or developer-experience issue.

| Project | Contribution & significance |
| :--- | :--- |
| **Apache Airflow** | [Async datetime sensor fix](https://github.com/apache/airflow/pull/72659) — prevented raw Jinja targets from being parsed during DAG construction, preserving the normal rendering path. |
| **django-stubs** | [Mutable request typing](https://github.com/typeddjango/django-stubs/pull/3642) — added a helper for tests and request factories while preserving inference for custom request subclasses. |
| **AMD Gaia** | [Telegram media feedback](https://github.com/amd/gaia/pull/3263) — replaced silent handling of unsupported uploads with explicit feedback and a video-path regression test. |

[All merged contributions →](https://github.com/search?q=is%3Apr+is%3Amerged+author%3ASIBTAIN-ASAD+-user%3ASIBTAIN-ASAD&type=pullrequests)

</details>



<a id="experience"></a>

<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="./assets/career-mobile-slim-dark.png" />
  <source media="(max-width: 600px)" srcset="./assets/career-mobile-slim-light.png" />
  <source media="(prefers-color-scheme: dark)" srcset="./assets/career-slim-dark.png" />
  <img src="./assets/career-slim-light.png" width="100%" alt="Professional experience: NavForward, Senior Software Engineer; Turing and Devsinc, Software Engineer; i2c, Associate Software Engineer." />
</picture>

<details>
<summary><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/control-career-slim-dark.svg" /><img src="./assets/control-career-slim-light.svg" width="320" align="absmiddle" alt="Show or hide: Career history, responsibilities & earlier experience" /></picture></summary>

### NavForward · Senior Software Engineer
<sub>June 2025 – Present · Remote</sub>

- Designed Django and Django REST Framework backend services and helped define microservice boundaries for US product teams.
- Built Selenium and Celery scraping pipelines with Redis-backed task processing, retries, and duplicate detection; worked with Docker, AWS, and MySQL-backed APIs.

### Turing · Software Engineer
<sub>June 2025 – December 2025 · Remote</sub>

- Worked on LLM training for AI agents and evaluation of agent task completion.
- Built evaluation pipelines covering dataset design, scoring, and prompt-refinement workflows.

### Devsinc · Software Engineer
<sub>November 2023 – June 2025 · Lahore, hybrid</sub>

- Built full-stack enterprise applications with React, Django, and FastAPI for healthcare and AI workflow products.
- Led frontend architecture with TypeScript and Material UI, including component systems and state patterns; worked on Adobe authentication, Microsoft Dynamics integrations, and patient-referral workflows.

### i2c · Associate Software Engineer
<sub>September 2023 – November 2023 · Lahore</sub>

- Supported deployments, release workflows, infrastructure monitoring, and operational runbooks.
- Worked with engineering teams to troubleshoot production issues and improve handoffs between operations and development.

<details>
<summary><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/control-earlier-slim-dark.svg" /><img src="./assets/control-earlier-slim-light.svg" width="320" align="absmiddle" alt="Show or hide: Earlier experience & freelance work" /></picture></summary>

**Q Information Hub · Software Engineer** · June 2021 – October 2023<br>
React and Django applications, REST APIs, JWT authentication, role-based access control, and PostgreSQL query optimization.

**Fiverr · Freelance Full Stack Engineer** · March 2021 – October 2023<br>
React and Django projects, AWS deployments, Firebase backends, and third-party integrations, from scoping through delivery.

**Upwork · Freelance Full Stack Engineer** · June 2020 – May 2023<br>
Web applications, dashboards, REST APIs, integrations, and ongoing maintenance for client teams.

[More about my experience →](https://www.sibtainasad.com/)

</details>

</details>


<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="./assets/professional-work-mobile-slim-dark.png" />
  <source media="(max-width: 600px)" srcset="./assets/professional-work-mobile-slim-light.png" />
  <source media="(prefers-color-scheme: dark)" srcset="./assets/professional-work-slim-dark.png" />
  <img src="./assets/professional-work-slim-light.png" width="100%" alt="Selected work: legal data intelligence at NavForward, healthcare workflows at Devsinc, and AI-agent evaluation at Turing." />
</picture>

<details>
<summary><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/control-work-slim-dark.svg" /><img src="./assets/control-work-slim-light.svg" width="320" align="absmiddle" alt="Show or hide: Read the professional project stories" /></picture></summary>

**Legal data intelligence · NavForward**<br>
I worked on data-collection services where scraping, background jobs, and API delivery needed to work together. The implementation combined Django, Selenium, Celery, and Redis with retries and duplicate detection, deployed through Docker and AWS.

**Healthcare referral workflows · Devsinc**<br>
My work connected a React and TypeScript frontend to enterprise workflows, including Adobe authentication and Microsoft Dynamics. I led frontend architecture while working with the wider team on patient-referral functionality.

**AI-agent evaluation · Turing**<br>
I worked on assessing whether agents completed their assigned tasks, including evaluation datasets, scoring pipelines, and prompt refinement. This was evaluation and training work, alongside my application-engineering experience.

</details>


<a id="projects"></a>

## Selected projects

<a href="https://github.com/SIBTAIN-ASAD/Spotter">
<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="./assets/spotter-panel-mobile-slim-dark.png" />
  <source media="(max-width: 600px)" srcset="./assets/spotter-panel-mobile-slim-light.png" />
  <source media="(prefers-color-scheme: dark)" srcset="./assets/spotter-panel-slim-dark.png" />
  <img src="./assets/spotter-panel-slim-light.png" width="100%" alt="Spotter: route planning and fuel optimization, built with Python, Django REST, GeoJSON, Docker and automated tests." />
</picture>
</a>

<details>
<summary><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/control-spotter-slim-dark.svg" /><img src="./assets/control-spotter-slim-light.svg" width="320" align="absmiddle" alt="Show or hide: Spotter — problem, implementation & engineering detail" /></picture></summary>

### [Spotter](https://github.com/SIBTAIN-ASAD/Spotter)

**Route planning & fuel optimization**

**The problem:** Plan a US driving route and recommend fuel stops using station prices and vehicle-range constraints.

**My implementation:** A Django REST API and interactive map, with separate services for routing, geocoding, station lookup, and fuel optimization. The API returns GeoJSON route geometry and fuel recommendations.

**Engineering detail:** Injectable external clients let tests exercise the planner without depending on live routing services. The project includes request IDs, health checks, throttling, and a Docker setup.

<sub>Python &nbsp; · &nbsp; Django REST Framework &nbsp; · &nbsp; GeoJSON &nbsp; · &nbsp; Docker &nbsp; · &nbsp; pytest</sub>

[Repository →](https://github.com/SIBTAIN-ASAD/Spotter) &nbsp; [Implementation notes →](https://github.com/SIBTAIN-ASAD/Spotter#readme)

</details>


<a href="https://www.sibtainasad.com/">
<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="./assets/portfolio-panel-mobile-slim-dark.png" />
  <source media="(max-width: 600px)" srcset="./assets/portfolio-panel-mobile-slim-light.png" />
  <source media="(prefers-color-scheme: dark)" srcset="./assets/portfolio-panel-slim-dark.png" />
  <img src="./assets/portfolio-panel-slim-light.png" width="100%" alt="SAM Portfolio: my experience, projects and code, presented using React, TypeScript, Three.js and motion." />
</picture>
</a>

<details>
<summary><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/control-portfolio-slim-dark.svg" /><img src="./assets/control-portfolio-slim-light.svg" width="320" align="absmiddle" alt="Show or hide: SAM Portfolio — implementation & source" /></picture></summary>

### [SAM Portfolio](https://github.com/SIBTAIN-ASAD/SAM-portfolio)

**Personal portfolio & interactive frontend**

**The purpose:** Bring my professional experience and projects together in one personal site.

**My implementation:** A React and TypeScript interface with Three.js visuals, Framer Motion transitions, and Tailwind CSS styling. The source organizes the experience, project, and technology content separately from the UI components.

<sub>TypeScript &nbsp; · &nbsp; React &nbsp; · &nbsp; Three.js &nbsp; · &nbsp; Tailwind CSS &nbsp; · &nbsp; Framer Motion</sub>

[Live portfolio →](https://www.sibtainasad.com/) &nbsp; [Source →](https://github.com/SIBTAIN-ASAD/SAM-portfolio)

</details>


<a id="skills"></a>

<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="./assets/skills-panel-mobile-slim-dark.png" />
  <source media="(max-width: 600px)" srcset="./assets/skills-panel-mobile-slim-light.png" />
  <source media="(prefers-color-scheme: dark)" srcset="./assets/skills-panel-slim-dark.png" />
  <img src="./assets/skills-panel-slim-light.png" width="100%" alt="Technical background: frontend; backend and data; infrastructure; machine learning." />
</picture>

<details>
<summary><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/control-technology-slim-dark.svg" /><img src="./assets/control-technology-slim-light.svg" width="320" align="absmiddle" alt="Show or hide: Full technology list" /></picture></summary>

| Area | Technologies |
| :--- | :--- |
| **Frontend** | TypeScript, JavaScript, React, Next.js, Tailwind CSS, Three.js |
| **Backend & data** | Python, Django, Django REST Framework, FastAPI, PostgreSQL, Redis |
| **Infrastructure** | Docker, GitHub Actions, AWS, Azure, Google Cloud |
| **Machine learning** | PyTorch, TensorFlow, reinforcement learning |

</details>

<details>
<summary><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/control-more-slim-dark.svg" /><img src="./assets/control-more-slim-light.svg" width="320" align="absmiddle" alt="Show or hide: More projects & implementation details" /></picture></summary>

**Spotter deployment scope:** Public routing and geocoding services support experimentation; larger deployments would need their own service arrangements.

**Other public repositories**

- [Flight booking management system](https://github.com/SIBTAIN-ASAD/Flight-MS-Python) — a terminal-based Python application with customer memberships, services, bookings, and text-file persistence.
- [C data structures and algorithms](https://github.com/SIBTAIN-ASAD/C-ADTs-DSA) — heap and binary search tree implementations.
- [Quora-style web application](https://github.com/SIBTAIN-ASAD/quora) — questions, answers, and comments.
- [C++ Checkers](https://github.com/SIBTAIN-ASAD/Checkers-C-) — move suggestions and file-based game data.

</details>

---

[**sibtainasad.com**](https://www.sibtainasad.com/) &nbsp; · &nbsp; [**LinkedIn**](https://www.linkedin.com/in/sibtain-asad/)
