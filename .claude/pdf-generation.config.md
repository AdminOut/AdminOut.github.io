# PDF generation config

Read by the pdf-generation skill's `build_doc.py`. The CV is a flat document built from `.claude/pdf-generation.flat-template.cv.html` and gated with `--client default --check-only`.

- **Provider name:** Lance Moore
- **Provider wordmark:** Lance Moore
- **Provider tagline:** Senior software engineer and integration specialist
- **Prepared by:** Lance Moore
- **Output dir:** .artifacts

The CV names the technologies a software buyer screens for, so the jargon tier's framework names are allowed for the default tenant.

### [client:default]

```
Client name: Prospective client
Wordmark: Lance Moore
Strapline: Curriculum vitae
Allow: celery, postgres, redis, docker, webhook
Forbidden: Cobalt, Pennington, Purpose Factory International, Pergolux, Forward Products,
  Kekst, Frameless, Hunter Bond, Talkdesk, Glenvista
```
