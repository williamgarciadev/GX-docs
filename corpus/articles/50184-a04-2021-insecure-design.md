---
title: "A04:2021 - Insecure design"
source_id: 50184
source_url: https://wiki.genexus.com/commwiki/wiki?50184
genexus_version: "18"
---

# A04:2021 - Insecure design

This article describes the OWASP 2021 architectural flaws that can result in the insecure design of your applications.

Insecure design is a broad category that represents various weaknesses described as "missing or ineffective control design." For example, when some code should encrypt sensitive data but there is no method to do so.

Read more at: [Insecure Design - OWASP Documentation](https://owasp.org/Top10/A04_2021-Insecure_Design/)

#### [Actions by GeneXus](#Actions+by+GeneXus)

* GeneXus does not take any specific actions.

#### [Actions by Developers](#Actions+by+Developers)

A secure design approach involves the whole application team and not only developers. It requires applying secure design patterns, [threat modeling](https://owasp.org/www-community/Threat_Modeling) analysis, and a [secure development life cycle](https://owasp.org/www-project-integration-standards/writeups/owasp_in_sdlc/). Even so, developers can take the actions below:

* [GeneXus application security training](https://training.genexus.com/en/learning/courses/security/course-security-in-web-applications).
* Dependency control (manual or in continuous integration pipelines, if any). [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/) may come in handy for this.
* Use of known libraries for security controls.
* Documentation of reusable controls for future developments.
* Active use of Security Scanner.

### [Availability](#Availability)

Since [GeneXus 18 upgrade 1](https://wiki.genexus.com/commwiki/wiki?51081).


|  |
| --- |
| **Backlinks** |
| [Toc:Managing OWASP Top 10 2021 in GeneXus Applications](https://wiki.genexus.com/commwiki/wiki?50180) |

---
