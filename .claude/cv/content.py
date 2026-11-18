"""The emailable CV: content and design, written out as HTML for WeasyPrint.

Run through build.sh, which prepares the images and renders the PDF. The HTML
refers to img/ and fonts/ relative to the build directory it is written to.

The content is the short form of data/resume.ts. When a role, project or
figure changes there, change it here too. Durations and the years of
experience are calculated from today's date, as the site calculates them.
"""
import datetime
import sys
from pathlib import Path

TODAY = datetime.date.today()
NOW = (TODAY.year, TODAY.month)


def months(start, end=None):
    """Inclusive month count, as utils/period.ts computes it."""
    sy, sm = map(int, start.split("-"))
    ey, em = map(int, end.split("-")) if end else NOW
    return (ey - sy) * 12 + (em - sm) + 1


def duration(start, end=None):
    n = months(start, end)
    y, m = divmod(n, 12)
    parts = []
    if y:
        parts.append(f"{y} yr" + ("s" if y > 1 else ""))
    if m:
        parts.append(f"{m} mo" + ("s" if m > 1 else ""))
    return " ".join(parts)


MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


def fmt(ym):
    y, m = ym.split("-")
    return f"{MONTHS[int(m) - 1]} {y}"


def period(start, end=None):
    return f"{fmt(start)} – {fmt(end) if end else 'Present'}"


YEARS = (NOW[0] * 12 + NOW[1] - (2015 * 12 + 2)) // 12  # softwareSince 2015-02

# ---------------------------------------------------------------- content ---

PROFILE = (
    "I design, build and run the systems businesses depend on: integration platforms, "
    "ERPs, multi-tenant SaaS and the cloud infrastructure behind them. I bring "
    f"{YEARS}+ years of software delivery as an independent consultant, a technical "
    "co-founder and the lead engineer on client platforms in the UK, US and South Africa. "
    "Before software I spent over a decade as a pharmacist, which still shapes how I "
    "build for regulated, compliance-heavy businesses."
)

SKILLS = [
    ("Engineering", ["Python", "Django", "Django REST Framework", "Celery", "TypeScript",
                     "Next.js", "Nuxt", "Vue", "PostgreSQL", "Redis", "RabbitMQ"]),
    ("Integrations", ["HubSpot", "Shopify", "NetSuite", "Bullhorn", "Microsoft Graph",
                      "Dynamics 365", "Business Central", "Sage 100 Contractor",
                      "QuickBooks", "REST APIs", "Webhooks"]),
    ("Cloud and DevOps", ["AWS ECS / Fargate", "Azure", "Cloudflare Workers", "Terraform",
                          "Docker", "GitHub Actions", "Sentry", "Grafana"]),
    ("AI", ["LLM agents (pydantic-ai)", "MCP servers", "AI-assisted engineering"]),
    ("Leadership", ["Technical leadership", "Code review", "Architecture decisions",
                    "Client delivery", "SLAs and security policy"]),
]

ROLES_P1 = [
    dict(title="Lead Software Engineer", org="Purpose Factory Partners", logo="pfp",
         start="2026-06",
         ctx="A US leadership-coaching and business-advisory group, building an AI and "
             "data platform for its member companies.",
         bullets=[
             "Lead engineer on a multi-tenant operations platform for the group and its "
             "member companies. Wrote most of the code (451 of 565 merged pull requests) "
             "and own the architecture through 40+ recorded design decisions.",
             "Own the Azure infrastructure end to end: Terraform, a self-hosted CI runner "
             "and 18 GitHub Actions pipelines for a Django/Celery API and Next.js front "
             "ends on Cloudflare Workers.",
             "Built Microsoft 365 and Google Workspace integrations behind a "
             "Microsoft-verified app, an MCP server for AI agents, and a read-only Sage 100 "
             "Contractor integration across seven companies, blocked from personal data.",
             "Lead and review a small distributed team. Shipped a second product on the same "
             "infrastructure: an omnichannel messaging console for a non-profit.",
         ]),
    dict(title="Co-founder", org="FlowConnect", logo="flowconnect", start="2023-09",
         ctx="An integration platform (iPaaS) that keeps a company's CRM, e-commerce, ERP, "
             "recruiting and phone systems in step. Spun out of Six & Flow, a UK HubSpot "
             "agency, where I am Development Lead.",
         bullets=[
             "Designed and built the integration engine (Django, Celery, Postgres, "
             "RabbitMQ) from the first commit.",
             "Delivered and support 29 client integrations across about 38 connectors, "
             "linking HubSpot with Shopify, OrderWise, NetSuite, Dynamics / Business "
             "Central, Bullhorn, Workday and others.",
             "Run the AWS infrastructure (ECS/Fargate, Terraform) with gated deploys, "
             "rollback, and Sentry and Grafana monitoring. Built the multi-tenant client "
             "dashboard and an on-site agent for clients' on-premises systems.",
             "Added HubSpot embedded calling and SMS logging to a major contact-centre "
             "vendor's official HubSpot integration.",
             "Lead the engineering team (hiring and code review) and act as the technical "
             "contact for clients. Wrote the SLA, security policy and support agreements.",
         ]),
]

ROLES_P2 = [
    dict(title="Senior Software Engineering Lead", org="Accruvia | ROI Developers",
         logo="accruvia", start="2018-04", end="2023-05",
         ctx="A custom software development house specialising in API integrations.",
         bullets=[
             "Planned, built, deployed and maintained custom software for the company's "
             "clients.",
             "Introduced agile workflows, code quality standards and automated CI/CD "
             "pipelines that increased delivery speed, improved estimation and "
             "significantly reduced end-user downtime.",
             "Introduced hiring processes that significantly reduced developer churn.",
         ]),
    dict(title="Director", org="AdminOut (Pty) Ltd", logo="adminout", start="2017-01",
         ctx="My software consultancy, through which I deliver independent client work.",
         bullets=[
             "Built the batch manufacturing ERP that took W.Last, a GMP complementary-"
             "medicine manufacturer, off paper. In 2026 rebuilt it on Django and Next.js "
             "with a full migration from the legacy system.",
             "Built the Virtual Inspection system for the Metal Recyclers Association of "
             "South Africa, approved by the South African Police Service and in production "
             "since 2021.",
             "Long-running client relationships, with nearly every client returning for "
             "follow-up work.",
         ]),
    dict(title="Freelance Software Engineer", org="Gift2Give", logo="g2g",
         start="2015-02", end="2018-01", ctx=None,
         bullets=[
             "Built a gift voucher redemption proxy server and terminal UI for a chain of "
             "malls and retailers, and ran its Linux and Apache servers.",
         ]),
    dict(title="Acting Responsible Pharmacist", org="W.LAST Manufacturing", logo="wlast",
         start="2009-09", end="2019-08", ctx=None,
         bullets=[
             "Responsible for GMP compliance through SOPs, for FDA and SAHPRA "
             "registrations, and for procurement and product formulation at a "
             "complementary-medicine factory.",
         ]),
]

EARLIER = [
    ("Pharmacy Manager (community service)", "Fezile Dabi District Municipality",
     "2008-06", "2009-06", "fezile"),
    ("Locum Retail Pharmacist", "Springbok Pharmacy", "2005-10", "2017-08", "springbok"),
]

PROJECTS = [
    dict(img="wlast-dashboard", title="Batch manufacturing ERP, rebuilt",
         meta="W.Last, GMP manufacturer · Sole developer",
         text="Rebuilt the ERP that took the factory off paper. Every material, product, "
              "supplier and batch record moved across, and it now runs the factory day to day.",
         stack="Django · Django REST Framework · Next.js · PostgreSQL"),
    dict(img="ops-platform", title="Multi-company operations platform",
         meta="US business-advisory group · Lead engineer",
         text="One place for communications, documents, recruiting, estimating and "
              "accounting data across member companies, with AI agents working on top of it.",
         stack="Django · Celery · PostgreSQL · Next.js · Azure"),
    dict(img="flowconnect", title="FlowConnect integration platform",
         meta="Co-founded · Co-founder and lead architect",
         text="Keeps clients' CRM, e-commerce, ERP, recruiting and phone systems in step "
              "automatically, with alerts when something breaks. 29 client integrations.",
         stack="Django · Celery · PostgreSQL · RabbitMQ · AWS"),
    dict(img="messaging-console", title="Omnichannel messaging console",
         meta="Non-profit outreach organisation · Lead developer",
         text="Brings conversations from eight channels into one inbox per contact, with a "
              "pipeline and analytics behind it. Rebuilt from a contractor's prototype.",
         stack="Django · Next.js · Cloudflare Workers · Docker"),
    dict(img="virtual-inspection", title="Virtual Inspection system",
         meta="Metal Recyclers Association of SA · Designer and developer",
         text="Replaces physical annual inspections of scrap-metal dealers with a virtual "
              "process approved by the South African Police Service. In production since 2021.",
         stack="Django · Vue"),
    dict(img="contact-centre", title="HubSpot calling and SMS",
         meta="Major contact-centre SaaS vendor · Integration engineer",
         text="Added embedded calling inside HubSpot and SMS logging to the vendor's "
              "official HubSpot integration, working in the vendor's own repositories.",
         stack="JavaScript · HubSpot Calling Extensions SDK · Ruby"),
    dict(img="crypto-rollout", title="National cryptocurrency rollout",
         meta="Crypto as legal tender · Contractor team lead",
         text="Brought in to resolve severe issues that surfaced during a national rollout of "
              "cryptocurrency as legal tender, leading a team of contractors and supporting "
              "the project's stakeholders.",
         stack=""),
]

# ------------------------------------------------------------------- html ---

FONTS = "".join(
    f'@font-face {{ font-family: "Inter"; src: url(fonts/Inter-{f}.ttf); '
    f"font-weight: {w}; font-style: {s}; }}\n"
    for f, w, s in [("Regular", 400, "normal"), ("Italic", 400, "italic"),
                    ("Medium", 500, "normal"), ("SemiBold", 600, "normal"),
                    ("Bold", 700, "normal"), ("ExtraBold", 800, "normal")]
)

CSS = FONTS + """
@page { size: A4; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body { font-family: "Inter", "DejaVu Sans", sans-serif; font-size: 8.4pt; line-height: 1.45;
       color: #1E2F33; }
a { color: inherit; text-decoration: none; }

.sheet { width: 210mm; height: 297mm; display: flex; position: relative; overflow: hidden;
         break-after: page; }
.sheet.last { break-after: auto; }

/* ---------------- sidebar ---------------- */
.side { width: 66mm; flex: none; background: #172A2E; color: #D3E2E1;
        padding: 13mm 7.5mm 12mm 8.5mm; }
.photo { display: block; width: 40mm; height: 40mm; margin: 0 auto 7mm;
         border-radius: 50%; border: 1.6pt solid #3FA9A0; }
.side h3 { font-size: 7.6pt; font-weight: 700; color: #7FD1C8; text-transform: uppercase;
           letter-spacing: 1.4pt; margin: 6.5mm 0 2.6mm; padding-bottom: 1.4mm;
           border-bottom: .5pt solid #34545A; }
.side h3.first { margin-top: 0; }
.contact .k { font-size: 6.4pt; text-transform: uppercase; letter-spacing: .9pt;
              color: #8FAAAD; margin-top: 2.2mm; }
.contact .v { font-size: 8pt; color: #FFFFFF; font-weight: 500; }
.side h4 { font-size: 7.4pt; font-weight: 600; color: #FFFFFF; margin: 2.8mm 0 1.4mm; }
.chips { line-height: 1; }
.chip { display: inline-block; font-size: 6.6pt; color: #E6F1F0; border: .5pt solid #3C6367;
        border-radius: 7pt; padding: .9mm 1.9mm; margin: 0 .9mm 1.2mm 0; }
.stat { margin-bottom: 3mm; }
.stat .n { font-size: 17pt; font-weight: 800; color: #FFFFFF; line-height: 1.05; }
.stat .n span { color: #3FA9A0; }
.stat .l { font-size: 7pt; color: #A9C2C4; }
.edu { display: flex; align-items: center; }
.edu img { width: 10mm; height: 10mm; border-radius: 1.6mm; background: #FFFFFF;
           padding: .6mm; margin-right: 3mm; flex: none; }
.edu .t { font-weight: 600; color: #FFFFFF; font-size: 8pt; }
.edu .s { font-size: 7.2pt; color: #A9C2C4; }
.plain { list-style: none; margin: 0; padding: 0; }
.plain li { margin-bottom: 2.4mm; font-size: 7.6pt; }
.plain li b { color: #FFFFFF; font-weight: 600; display: block; }
.plain li span { color: #A9C2C4; font-size: 7pt; }
.side .chips + h3 { margin-top: 5.4mm; }
.qr { background: #FFFFFF; border-radius: 2mm; padding: 3mm; display: flex; align-items: center; }
.qr img { width: 20mm; height: 20mm; flex: none; margin-right: 3mm; }
.qr div { color: #1E2F33; font-size: 7pt; line-height: 1.35; }
.qr b { display: block; color: #0C7471; font-size: 7.6pt; }

/* ---------------- main column ---------------- */
.main { flex: 1; padding: 13mm 12mm 14mm 10mm; position: relative; }
.name { font-size: 27pt; font-weight: 800; color: #172A2E; letter-spacing: -.3pt;
        line-height: 1.05; margin: 1mm 0 1.6mm; }
.headline { font-size: 10pt; font-weight: 600; color: #0C7471; margin-bottom: 5mm; }
.rule { height: 1.1mm; width: 18mm; background: #3FA9A0; border-radius: .6mm; margin-bottom: 6mm; }
h2 { font-size: 10pt; font-weight: 800; color: #172A2E; text-transform: uppercase;
     letter-spacing: 1.6pt; margin: 0 0 3.6mm; display: flex; align-items: center; }
h2 span.bar { display: inline-block; width: 3.2mm; height: 3.2mm; border-radius: .8mm;
              background: #0C7471; margin-right: 2.4mm; }
h2.next { margin-top: 6mm; }
p.profile { font-size: 8.9pt; line-height: 1.55; color: #33474B; margin: 0 0 6.5mm; }

.timeline { border-left: .8pt solid #CFE2E0; margin-left: 5mm; padding-left: 0; }
.job { position: relative; padding: 0 0 4.6mm 9mm; break-inside: avoid; }
.job .logo { position: absolute; left: -5.2mm; top: -.6mm; width: 10.4mm; height: 10.4mm;
             border-radius: 2.2mm; background: #FFFFFF; border: .6pt solid #CFE2E0; padding: .9mm; }
.job.short { padding-bottom: 3.6mm; }
.job .logo img { width: 100%; height: 100%; border-radius: 1.2mm; }
.job .top { display: flex; justify-content: space-between; align-items: baseline; }
.job h3 { font-size: 9.6pt; font-weight: 700; color: #172A2E; margin: 0; }
.job .dates { font-size: 7pt; font-weight: 600; color: #0C7471; background: #E6F1F0;
              border-radius: 6pt; padding: .7mm 2.2mm; white-space: nowrap; margin-left: 3mm; }
.job .org { font-size: 8.2pt; font-weight: 600; color: #0C7471; margin-top: .4mm; }
.job .org span { color: #6B7E81; font-weight: 400; }
.job .ctx { font-size: 7.8pt; font-style: italic; color: #5C6F72; margin: 1mm 0 1.2mm; }
.job ul { margin: 1mm 0 0; padding-left: 3.6mm; }
.job li { margin-bottom: 1mm; padding-left: .6mm; }
.job li::marker { color: #3FA9A0; }

.foot { position: absolute; left: 10mm; right: 12mm; bottom: 7mm; display: flex;
        justify-content: space-between; font-size: 6.8pt; color: #8A9A9D; }

/* ---------------- selected work ---------------- */
.work { display: block; }
.band { background: #172A2E; color: #FFFFFF; padding: 9mm 12mm 7mm 14mm; display: flex;
        justify-content: space-between; align-items: flex-end; }
.band .t { font-size: 21pt; font-weight: 800; letter-spacing: -.2pt; }
.band .s { font-size: 8.4pt; color: #A9C2C4; margin-top: 1mm; }
.band .r { font-size: 7.6pt; color: #A9C2C4; text-align: right; line-height: 1.5; }
.band .r b { color: #7FD1C8; font-weight: 600; }
.cards { display: flex; flex-wrap: wrap; justify-content: space-between; padding: 5mm 12mm 0 14mm; }
.card { width: 89mm; margin-bottom: 3.8mm; border: .5pt solid #DCE7E6; border-radius: 2.4mm;
        overflow: hidden; break-inside: avoid; }
.card img { display: block; width: 89mm; height: 31.79mm; border-bottom: .5pt solid #DCE7E6; }
.card .b { padding: 2.6mm 3.4mm 3mm; }
.card h3 { font-size: 9.2pt; font-weight: 700; color: #172A2E; margin: 0 0 .5mm; }
.card .m { font-size: 7pt; font-weight: 600; color: #0C7471; margin-bottom: 1.2mm; }
.card p { font-size: 7.5pt; line-height: 1.42; color: #33474B; margin: 0 0 1.4mm; }
.card .st { font-size: 6.6pt; color: #6B7E81; }
.work .foot { left: 14mm; }
.card.feat { width: 100%; display: flex; align-items: center; }
.card.feat img { width: 76mm; height: 38mm; border-bottom: none; border-right: .5pt solid #DCE7E6; flex: none; }
.card.feat .b { padding: 3mm 5mm; }
.card.feat h3 { font-size: 10.4pt; }
.card.feat p { font-size: 7.9pt; }
.card .eyebrow { font-size: 6.4pt; font-weight: 700; color: #D08C3F; text-transform: uppercase; letter-spacing: 1pt; }
"""


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def job(r):
    end = r.get("end")
    ctx = f'<p class="ctx">{esc(r["ctx"])}</p>' if r.get("ctx") else ""
    items = "".join(f"<li>{esc(b)}</li>" for b in r["bullets"])
    return f"""
<div class="job">
  <div class="logo"><img src="img/logo-{r['logo']}.png" alt=""></div>
  <div class="top"><h3>{esc(r['title'])}</h3><span class="dates">{period(r['start'], end)}</span></div>
  <div class="org">{esc(r['org'])} <span>· {duration(r['start'], end)}</span></div>
  {ctx}<ul>{items}</ul>
</div>"""


def foot(n):
    return (f'<div class="foot"><span>Lance Moore · Curriculum vitae · {TODAY:%B %Y}</span>'
            f"<span>Page {n} of 3</span></div>")


skills_html = "".join(
    f"<h4>{esc(g)}</h4><div class=\"chips\">"
    + "".join(f'<span class="chip">{esc(s)}</span>' for s in items)
    + "</div>"
    for g, items in SKILLS
)

page1 = f"""
<section class="sheet">
  <aside class="side">
    <img class="photo" src="img/headshot.png" alt="Lance Moore">
    <h3 class="first">Contact</h3>
    <div class="contact">
      <div class="k">Email</div><div class="v"><a href="mailto:lance@adminout.net">lance@adminout.net</a></div>
      <div class="k">Location</div><div class="v">Johannesburg, South Africa</div>
      <div class="k">Works with</div><div class="v">UK and US teams, remotely</div>
      <div class="k">Portfolio</div><div class="v"><a href="https://adminout.net/resume/portfolio">adminout.net/resume/portfolio</a></div>
    </div>
    <h3>Skills</h3>
    {skills_html}
  </aside>
  <main class="main">
    <div class="name">Lance Moore</div>
    <div class="headline">Senior software engineer and integration specialist</div>
    <div class="rule"></div>
    <h2><span class="bar"></span>Profile</h2>
    <p class="profile">{esc(PROFILE)}</p>
    <h2><span class="bar"></span>Experience</h2>
    <div class="timeline">{''.join(job(r) for r in ROLES_P1)}</div>
    {foot(1)}
  </main>
</section>"""

earlier_html = "".join(
    f'''<div class="job short"><div class="logo"><img src="img/logo-{lg}.png" alt=""></div>
  <div class="top"><h3>{esc(t)}</h3><span class="dates">{period(s, e)}</span></div>
  <div class="org">{esc(o)} <span>· {duration(s, e)}</span></div></div>'''
    for t, o, s, e, lg in EARLIER
)
edu_html = '''<div class="job short"><div class="logo"><img src="img/logo-wits.png" alt=""></div>
  <div class="top"><h3>Bachelor of Pharmacy</h3><span class="dates">2006</span></div>
  <div class="org">University of the Witwatersrand</div></div>'''
SECTORS = ["Manufacturing (GMP)", "Pharmacy", "Recruitment", "E-commerce", "Contact centres",
           "Business advisory", "Non-profit", "Metal recycling", "Retail"]
sectors_html = "".join(f'<span class="chip">{esc(x)}</span>' for x in SECTORS)

page2 = f"""
<section class="sheet">
  <aside class="side">
    <h3 class="first">At a glance</h3>
    <div class="stat"><div class="n">{YEARS}<span>+</span></div><div class="l">years building and running software</div></div>
    <div class="stat"><div class="n">29</div><div class="l">client integrations delivered through FlowConnect</div></div>
    <div class="stat"><div class="n">451</div><div class="l">of the 565 merged pull requests on the platform I lead</div></div>
    <div class="stat"><div class="n">13<span>+</span></div><div class="l">years in pharmacy and GMP manufacturing</div></div>
    <h3>Industries</h3>
    <div class="chips">{sectors_html}</div>
    <h3>Portfolio</h3>
    <a class="qr" href="https://adminout.net/resume/portfolio"><img src="img/qr-portfolio.svg" alt="">
      <div><b>See the work</b>Project write-ups and screenshots at adminout.net/resume/portfolio</div></a>
  </aside>
  <main class="main">
    <h2><span class="bar"></span>Experience, continued</h2>
    <div class="timeline">{''.join(job(r) for r in ROLES_P2)}</div>
    <h2 class="next"><span class="bar"></span>Earlier career: pharmacy</h2>
    <div class="timeline">{earlier_html}</div>
    <h2 class="next"><span class="bar"></span>Education</h2>
    <div class="timeline">{edu_html}</div>
    {foot(2)}
  </main>
</section>"""

def card(p, cls="card", crop="short"):
    stack = f'<div class="st">{esc(p["stack"])}</div>' if p["stack"] else ""
    return (f'<div class="{cls}"><img src="img/{p["img"]}-{crop}.jpg" alt="{esc(p["title"])}">'
            f'<div class="b"><h3>{esc(p["title"])}</h3><div class="m">{esc(p["meta"])}</div>'
            f"<p>{esc(p['text'])}</p>{stack}</div></div>")


FEATURED = dict(PROJECTS[0], text=PROJECTS[0]["text"] + " Live in production, replacing the "
                "legacy system with no data left behind.")
cards = card(FEATURED, "card feat", "wide") + "".join(card(p) for p in PROJECTS[1:])

page3 = f"""
<section class="sheet work last">
  <div class="band">
    <div><div class="t">Selected work</div><div class="s">Recent projects I designed, built and run</div></div>
    <div class="r">Screenshots show demo data<br><a href="https://adminout.net/resume/portfolio"><b>adminout.net/resume/portfolio</b></a></div>
  </div>
  <div class="cards">{cards}</div>
  {foot(3)}
</section>"""

html = f"""<!DOCTYPE html>
<html lang="en-GB"><head><meta charset="utf-8">
<title>Lance Moore, CV</title>
<meta name="author" content="Lance Moore">
<meta name="description" content="Curriculum vitae of Lance Moore, senior software engineer and integration specialist.">
<meta name="keywords" content="software engineer, integration specialist, Django, Python, TypeScript, HubSpot, iPaaS, AWS, Azure">
<style>{CSS}</style></head>
<body>{page1}{page2}{page3}</body></html>
"""
Path(sys.argv[1]).write_text(html)
