/**
 * Everything the resume pages say about roles and projects. The CV, the
 * portfolio and the print page all render from here, so edit content in
 * this file rather than in the page templates.
 *
 * Months are "YYYY-MM". Leave `end` out for a current role; its duration
 * is calculated from the render date.
 */
import adminoutLogo from "~/assets/img/logo-mini.webp";
import accruviaLogo from "~/assets/img/resume/accruvia.jpg";
import g2gLogo from "~/assets/img/resume/g2g.webp";
import flowconnectLogo from "~/assets/img/resume/flowconnect.webp";
import pfpLogo from "~/assets/img/resume/purpose-factory-partners.webp";
import wlastLogo from "~/assets/img/resume/wlast.webp";
import opsPlatformShot from "~/assets/img/portfolio/ops-platform.webp";
import messagingShot from "~/assets/img/portfolio/messaging-console.webp";
import inspectionShot from "~/assets/img/portfolio/virtual-inspection.webp";
import wlastDashboard from "~/assets/img/portfolio/wlast-dashboard.webp";
import wlastBatch from "~/assets/img/portfolio/wlast-batch.webp";
import wlastStock from "~/assets/img/portfolio/wlast-stock.webp";
import flowconnectArt from "~/assets/img/portfolio/flowconnect.webp";
import contactCentreArt from "~/assets/img/portfolio/contact-centre.webp";

export interface Role {
  organisation: string;
  title: string;
  start: string;
  end?: string;
  /** Logo image; when absent the card shows the `initials` badge. */
  logo?: string;
  initials?: string;
  summary: string;
  highlights: string[];
}

export interface BriefRole {
  organisation: string;
  title: string;
  start: string;
  end: string;
  line: string;
}

export interface Screenshot {
  src: string;
  alt: string;
}

export interface Project {
  title: string;
  client: string;
  role: string;
  summary: string;
  features: string[];
  outcome?: string;
  stack: string[];
  /** Real screenshots, shown in a browser frame. */
  screenshots?: Screenshot[];
  /** Generated illustration; when absent and no screenshots, a placeholder. */
  illustration?: Screenshot;
  featured?: boolean;
}

export interface BriefProject {
  title: string;
  stack?: string;
  line: string;
}

export interface SkillGroup {
  name: string;
  items: string[];
}

export const profile = {
  name: "Lance Moore",
  headline: "Senior software engineer and integration specialist",
  softwareSince: "2015-02",
  /**
   * The contact email, reversed then base64-encoded so it never appears as
   * plain text in the HTML or the JavaScript bundle. Decoded in the browser
   * only when a visitor asks for it (components/resume/ProtectedEmail.vue).
   * To change it: btoa([...address].reverse().join("")).
   */
  emailEncoded: "dGVuLnR1b25pbWRhQGVjbmFs",
  location: "Johannesburg, South Africa · remote with UK and US teams",
  /** `{years}` is replaced with completed years since `softwareSince`. */
  bio: [
    "I design, build and run the systems businesses depend on: integration platforms, ERPs, multi-tenant SaaS and the cloud infrastructure behind them. I have {years}+ years of software delivery, as an independent consultant, a technical co-founder and the lead engineer on client platforms in the UK, US and South Africa.",
    "Before software I spent over a decade as a pharmacist, which still shapes how I build for regulated, compliance-heavy businesses.",
  ],
};

export const skills: SkillGroup[] = [
  {
    name: "Engineering",
    items: [
      "Python, Django and Django REST Framework, Celery",
      "TypeScript, Next.js, Nuxt and Vue",
      "PostgreSQL, Redis, RabbitMQ",
    ],
  },
  {
    name: "Integrations",
    items: [
      "HubSpot, Shopify, NetSuite, Bullhorn",
      "Microsoft 365 (Graph), Dynamics 365 and Business Central",
      "Sage 100 Contractor, QuickBooks, REST APIs and webhooks",
    ],
  },
  {
    name: "Cloud and DevOps",
    items: [
      "AWS (ECS/Fargate), Azure, Cloudflare Workers",
      "Terraform, Docker, GitHub Actions",
      "Sentry and Grafana monitoring",
    ],
  },
  {
    name: "AI",
    items: [
      "LLM agents (pydantic-ai) on business data",
      "MCP servers that give AI agents controlled access",
      "AI-assisted engineering workflows, from ticket to pull request",
    ],
  },
  {
    name: "Delivery",
    items: [
      "Technical leadership and code review",
      "Architecture decision records",
      "Client-facing delivery, SLAs and security policy",
    ],
  },
];

/** Newest start date first. */
export const roles: Role[] = [
  {
    organisation: "Purpose Factory Partners",
    title: "Lead Software Engineer",
    start: "2026-06",
    logo: pfpLogo,
    summary:
      "A US leadership-coaching and business-advisory group, building an AI and data platform for its member companies.",
    highlights: [
      "Lead engineer on a multi-tenant operations platform serving the group and its member companies. Wrote most of the code (451 of 565 merged pull requests) and own the architecture through 40+ recorded design decisions.",
      "Own the Azure infrastructure end to end: Terraform, a self-hosted CI runner and 18 GitHub Actions pipelines, deploying a Django/Celery API and Next.js front ends on Cloudflare Workers.",
      "Built Microsoft 365 and Google Workspace integrations (Outlook, Teams, SharePoint, Planner) behind a Microsoft-verified app, plus an MCP server that lets AI agents use the platform's data.",
      "Delivered a read-only Sage 100 Contractor integration across seven companies, with a locked-down tunnel, pinned TLS and a login that is blocked from personal data.",
      "Lead and review a small distributed team, and built its AI-assisted ticket-to-PR engineering workflow.",
      "Shipped a second product on the same infrastructure: an omnichannel messaging console for a non-profit.",
    ],
  },
  {
    organisation: "FlowConnect",
    title: "Co-founder",
    start: "2023-09",
    logo: flowconnectLogo,
    summary:
      "An integration platform (iPaaS) that keeps a company's CRM, e-commerce, ERP, recruiting and phone systems in step. Spun out of Six & Flow, a UK HubSpot agency, where I am Development Lead.",
    highlights: [
      "Co-founded the company, and designed and built its integration engine (Django, Celery, Postgres, RabbitMQ) from the first commit.",
      "Delivered and support 29 client integrations across about 38 connectors, linking HubSpot with Shopify, OrderWise, NetSuite, Dynamics / Business Central, Bullhorn, Workday and others.",
      "Designed and run the AWS infrastructure (ECS/Fargate, Terraform), with gated GitHub Actions deploys, rollback, and Sentry and Grafana monitoring.",
      "Built the multi-tenant client dashboard (Next.js on Cloudflare) and an on-site agent that pulls data from clients' on-premises systems.",
      "Lead the engineering team: hiring, code review, and building connectors alongside contractors.",
      "Act as the technical contact for clients. Wrote the SLA, security policy, product documentation and support agreements.",
    ],
  },
  {
    organisation: "Accruvia | ROI Developers",
    title: "Senior Software Engineering Lead",
    start: "2018-04",
    end: "2023-05",
    logo: accruviaLogo,
    summary:
      "A custom software development house specialising in API integrations.",
    highlights: [
      "Responsible for the planning, implementation, deployment and maintenance of custom software solutions for the company's clients.",
      "Designed and introduced agile workflows and standard operating procedures that increased development velocity and improved estimation.",
      "Introduced and enforced code quality standards that significantly reduced end-user downtime.",
      "Introduced automated CI/CD pipelines that made daily releases routine.",
      "Introduced hiring processes that significantly reduced developer churn.",
    ],
  },
  {
    organisation: "AdminOut (Pty) Ltd",
    title: "Director",
    start: "2017-01",
    logo: adminoutLogo,
    summary:
      "My software consultancy, through which I deliver independent client work.",
    highlights: [
      "Designed and built the batch manufacturing ERP for W.Last, a GMP complementary-medicine manufacturer, and in 2026 rebuilt it on Django and Next.js with a full migration from the legacy system.",
      "Designed and built the Virtual Inspection system for the Metal Recyclers Association of South Africa, approved by the South African Police Service and in production since 2021.",
      "Built long-running client relationships, with nearly every client returning for follow-up work.",
    ],
  },
  {
    organisation: "Gift2Give",
    title: "Freelance Software Engineer",
    start: "2015-02",
    end: "2018-01",
    logo: g2gLogo,
    summary:
      "Third-party gift voucher issuing and redemption for a chain of malls and retailers.",
    highlights: [
      "Designed and built a gift voucher redemption proxy server and the terminal UI.",
      "Configured and ran the Linux and Apache web servers.",
    ],
  },
  {
    organisation: "W.LAST Manufacturing",
    title: "Acting Responsible Pharmacist",
    start: "2009-09",
    end: "2019-08",
    logo: wlastLogo,
    summary: "A complementary and alternative medicine manufacturing facility.",
    highlights: [
      "Stock procurement and product formulation.",
      "Introduced GMP standards through SOPs to keep the facility compliant.",
      "Responsible for regulatory matters and for maintaining FDA and SAHPRA registrations.",
      "Designed and built the custom ERP that took the factory off paper, which cut operational overhead and is still in daily use.",
    ],
  },
];

export const earlierCareer: BriefRole[] = [
  {
    organisation: "Fezile Dabi District Municipality",
    title: "Pharmacy Manager (community service)",
    start: "2008-06",
    end: "2009-06",
    line: "Ran district pharmacy procurement and satellite clinics, and maintained the district's stock management software.",
  },
  {
    organisation: "Springbok Pharmacy",
    title: "Locum Retail Pharmacist",
    start: "2005-10",
    end: "2017-08",
    line: "Dispensing, compounding and patient counselling at one of South Africa's largest single-store pharmacies.",
  },
];

export const education = {
  qualification: "Bachelor of Pharmacy",
  institution: "University of the Witwatersrand",
  year: 2006,
};

export const projects: Project[] = [
  {
    featured: true,
    title: "Batch manufacturing ERP, rebuilt",
    client: "W.Last, a GMP complementary-medicine manufacturer",
    role: "Sole developer",
    summary:
      "A modern rebuild of the batch manufacturing ERP I first built for W.Last in PHP, which took the factory off paper. Every material, product, supplier and batch record moved across from the legacy system, and the new ERP now runs the factory day to day.",
    features: [
      "Live dashboard with low-stock and expiry alerts",
      "Batch records tracked from sales order through production to release",
      "Stock levels and expiry tracking per material batch",
      "Role-based access",
      "PDF and CSV exports",
    ],
    outcome:
      "Live in production, replacing the legacy system with no data left behind.",
    stack: [
      "Django",
      "Django REST Framework",
      "Next.js",
      "shadcn/ui",
      "Azure",
      "Cloudflare",
    ],
    screenshots: [
      {
        src: wlastDashboard,
        alt: "W.Last ERP dashboard with stock and expiry alerts (demo data)",
      },
      { src: wlastBatch, alt: "W.Last ERP batch records list (demo data)" },
      {
        src: wlastStock,
        alt: "W.Last ERP stock on hand per material (demo data)",
      },
    ],
  },
  {
    title: "Multi-company operations platform",
    client: "A US business-advisory group and its member companies",
    role: "Lead engineer",
    summary:
      "One platform that gives an advisory group and its member companies a single place for communications, documents, recruiting, estimating and accounting data, with AI agents working on top of it.",
    features: [
      "Tenant-scoped data with per-company modules and roles",
      "Microsoft 365 and Google Workspace ingest",
      "Read-only Sage 100 Contractor data, blocked from personal data",
      "MCP server and AI agents over the platform's data",
      "Recruiting pipeline with scorecards",
    ],
    stack: [
      "Django",
      "Celery",
      "PostgreSQL",
      "Next.js",
      "Azure",
      "Terraform",
      "Microsoft Graph",
      "pydantic-ai",
      "MCP",
    ],
    screenshots: [
      { src: opsPlatformShot, alt: "Recruiting pipeline board (demo data)" },
    ],
  },
  {
    title: "FlowConnect integration platform",
    client: "FlowConnect, co-founded; clients across the UK",
    role: "Co-founder and lead architect",
    summary:
      "An integration platform that keeps clients' CRM, e-commerce, ERP, recruiting and phone systems in step automatically, with alerts when something breaks.",
    features: [
      "29 client integrations across about 38 connectors",
      "HubSpot, Shopify, OrderWise, NetSuite, Dynamics, Bullhorn, Workday",
      "On-site agent for clients' on-premises systems",
      "Multi-tenant client dashboard",
      "Gated deploys with rollback and full monitoring",
    ],
    stack: [
      "Django",
      "Celery",
      "PostgreSQL",
      "RabbitMQ",
      "AWS ECS",
      "Terraform",
      "Next.js",
      "Cloudflare",
    ],
    illustration: {
      src: flowconnectArt,
      alt: "Illustration of a hub keeping connected business systems in sync",
    },
  },
  {
    title: "Omnichannel messaging console",
    client: "A non-profit outreach organisation",
    role: "Lead developer",
    summary:
      "An operator console that brings conversations from eight channels into one inbox per contact, with a pipeline and analytics behind it. Rebuilt from a contractor's prototype.",
    features: [
      "Unified inbox: WhatsApp, Telegram, Instagram, TikTok, Messenger, web form, email and SMS",
      "Contact merge and CSV import and export",
      "Engagement pipeline board, tasks and reminders",
      "Meta ad-campaign spend analytics",
      "Role and data-scope permissions enforced by the API",
    ],
    stack: ["Django", "Next.js", "Cloudflare Workers", "Docker"],
    screenshots: [
      {
        src: messagingShot,
        alt: "Conversations per channel dashboard (demo data)",
      },
    ],
  },
  {
    title: "Virtual Inspection system",
    client: "Metal Recyclers Association of South Africa",
    role: "Designer and developer",
    summary:
      "Replaces the physical annual inspections of scrap-metal dealers with a virtual process approved by the South African Police Service (SAPS).",
    features: [
      "Annual inspections generated automatically for every member",
      "Member, staff and SAPS logins",
      "Encrypted uploads of member documentation",
      "Automated reminders and compliance reports",
      "PDF inspection reports and compliance certificates",
    ],
    outcome: "In production since 2021.",
    stack: ["Django", "Vue"],
    screenshots: [
      {
        src: inspectionShot,
        alt: "Regulatory declaration step of an inspection",
      },
    ],
  },
  {
    title: "HubSpot calling and SMS",
    client: "A major contact-centre SaaS vendor",
    role: "Integration engineer (through Six & Flow)",
    summary:
      "Added embedded calling inside HubSpot and SMS message logging to the vendor's official HubSpot integration, working in the vendor's own engineering repositories.",
    features: [
      "Click-to-call from HubSpot records using the embedded dialer",
      "SMS conversations logged to the HubSpot timeline",
    ],
    stack: ["JavaScript", "HubSpot Calling Extensions SDK", "Ruby"],
    illustration: {
      src: contactCentreArt,
      alt: "Illustration of calls and messages flowing into a CRM timeline",
    },
  },
];

export const earlierProjects: BriefProject[] = [
  {
    title: "Invoicing and payment collection",
    stack: "Django, Vue",
    line: "Multi-tenant, white-labelled invoicing with QuickBooks Desktop and Online integration. Contributor, then team lead.",
  },
  {
    title: "Electronic procurement and ERP",
    line: "Ordering, commission calculations and payment collection for a pharmaceutical supplier, with logins for clinics, practitioners and sales staff.",
  },
  {
    title: "National cryptocurrency rollout",
    line: "Assembled and led a contractor team to resolve severe issues during a national rollout of crypto as legal tender.",
  },
  {
    title: "Crypto arbitrage feed",
    stack: "Python, Celery",
    line: "Personal project aggregating order books from local and international exchanges into a realtime arbitrage feed with alerts.",
  },
];
