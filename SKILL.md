---
name: job-resume-builder
description: Analyzes a job description, cross-references it with industry standards (skills, tools, experience, knowledge), and writes a tailored resume aligned to the user's experience, roles, and titles. Trigger when the user shares a job posting/description and asks for a resume, CV, or wants their resume tailored to a role.
---

# Job Resume Builder

Tailor a resume to a specific job posting by analyzing the job description, comparing it against industry standards for the role, and aligning the user's real experience to what the employer is looking for.

## Inputs

Required from the user (ask if not provided):

1. **Job description** — pasted text, a file path, or a URL. If a URL is provided, use WebFetch to retrieve it.
2. **User profile / experience** — look for one of the following before asking:
   - `profile.md`, `resume.md`, `experience.md`, or `cv.md` in the current working directory
   - `~/.claude/profile.md` or `~/.claude/resume.md`
   - A path the user explicitly provides

   If no profile is found, ask the user for: full name, contact info, current/past roles and titles, years in each role, key accomplishments, education, certifications, and any tools/skills they want emphasized. Offer to save the captured info to `~/.claude/profile.md` for reuse.

3. **Output format** — ask whether they want Markdown (`.md`), plain text (`.txt`), or a Word-style file (`.docx` via pandoc if available). Default to Markdown.

## Workflow

### Step 1 — Extract job requirements

Parse the job description and extract a structured summary:

- **Role & title** (e.g., "Senior Backend Engineer")
- **Company & industry**
- **Seniority level** (junior / mid / senior / lead / staff / principal)
- **Required hard skills** (languages, frameworks, platforms)
- **Required tools** (e.g., Docker, Terraform, Jira, Figma, SAP)
- **Required experience** (years, types of projects, scale)
- **Required knowledge / domain** (e.g., HIPAA, PCI, distributed systems)
- **Soft skills** (leadership, communication, mentoring)
- **Nice-to-haves**
- **Keywords likely to be scanned by ATS** — list verbatim

### Step 2 — Cross-reference with industry standards

For the identified role, list what is typically expected in the industry at that seniority level even if not stated in the posting. Use the following baseline categories:

- **Core technical skills** for that role family
- **Standard tooling** used in the industry for that role
- **Typical experience milestones** at that seniority
- **Domain knowledge** commonly expected
- **Certifications** that are standard or differentiating

Then produce a **gap analysis table**:

| Requirement | In job posting? | Industry standard? | Present in user profile? | Action |
|---|---|---|---|---|

The "Action" column indicates: `emphasize`, `mention`, `reframe existing experience`, or `omit / flag as gap`.

### Step 3 — Map user's experience to the requirements

For every requirement (job-stated or industry-standard), find the strongest evidence in the user's profile:

- Match real roles, titles, and accomplishments — **never invent experience, employers, dates, or credentials**.
- Reframe existing bullets to use the posting's verbatim keywords where truthful.
- Prefer quantified achievements (numbers, %, scale, $).
- Use strong action verbs; lead with impact, not duties.

If a required item is genuinely absent from the user's background, do **not** fabricate it. Flag it back to the user as a gap and ask whether they have any related experience to surface, or whether to omit it.

### Step 4 — Write the tailored resume

Default structure (reorder to match what the posting prioritizes):

1. **Header** — name, location (city/region only), email, phone, LinkedIn/portfolio
2. **Professional Summary** — 2–4 lines, tuned to the target role, naturally including the top 3–5 ATS keywords
3. **Core Skills** — grouped (Languages / Frameworks / Tools / Platforms / Domain), only skills the user actually has
4. **Professional Experience** — reverse chronological; role, company, dates; 3–6 bullets per role, each starting with an action verb and prioritized so the most relevant-to-this-job bullet comes first
5. **Education**
6. **Certifications / Licenses** (if any)
7. **Selected Projects** (optional, useful for early-career or career-changers)

Style rules:
- One page for <10 years experience, two pages max otherwise.
- No first-person pronouns. Past tense for past roles, present tense for current.
- Mirror the posting's language (e.g., if it says "observability," don't only say "monitoring").
- Don't use tables, columns, headers/footers, or graphics — they break ATS parsers.
- No photos, no DOB, no marital status.

### Step 5 — Deliver

1. Write the resume to a file (default: `resume-<company>-<role>.md` in the current directory, sanitized for filesystem-safe names).
2. If a non-Markdown format was requested, convert via `pandoc` if available; otherwise warn and keep Markdown.
3. Print a short report to the user:
   - Top keywords incorporated
   - Gaps flagged (anything required but missing from their profile)
   - Suggested next steps (e.g., "consider getting AWS certified," "add a project demonstrating X")

## Guardrails

- **Truthfulness is non-negotiable.** Do not invent jobs, dates, titles, degrees, certifications, metrics, or technologies. Reframing is allowed; fabrication is not.
- If the user asks to "just add" a skill or experience they don't have, refuse and offer to surface adjacent real experience instead.
- Do not include sensitive personal data (full address, government IDs, salary history) unless the user explicitly requests it.
- If the job description is in a language other than English, write the resume in the same language as the posting unless told otherwise.
