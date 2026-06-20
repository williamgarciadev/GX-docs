---
title: "A06:2021 - Vulnerable and outdated components"
source_id: 50186
source_url: https://wiki.genexus.com/commwiki/wiki?50186
genexus_version: "18"
---

# A06:2021 - Vulnerable and outdated components

Vulnerable Components are a known issue concerning the security of applications. Below you can find a guideline of the actions to solve these vulnerabilities.

Read more at: [Vulnerable and Outdated Components - OWASP Documentation](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/)

#### [Actions by GeneXus](#Actions+by+GeneXus)

* GeneXus uses a set of public standard classes. You can find them here: [GeneXus Standard Classes](https://wiki.genexus.com/commwiki/wiki?18859).
* GeneXus updates its dependencies on every release.
* GeneXus fixes known vulnerabilities on its releases.

#### [Actions by Developers](#Actions+by+Developers)

* Upgrade to the latest GeneXus version.
* Verify third-party components used against known vulnerabilities in databases, mailing lists, etc.
* Check for [User Controls](https://wiki.genexus.com/commwiki/wiki?5273), [Extensions](https://wiki.genexus.com/commwiki/wiki?3243), [Patterns](https://wiki.genexus.com/commwiki/wiki?2814) and [External object](https://wiki.genexus.com/commwiki/wiki?5669) dependencies.

  + Security Scanner helps to detect this scenario with case codes #120 & #121.
* Change the database driver to the latest on deployment.
* Verify the server software is up to date.
* Implement security policies.

### [Availability](#Availability)

Since [GeneXus 18 upgrade 1](https://wiki.genexus.com/commwiki/wiki?51081).


|  |
| --- |
| **Backlinks** |
| [Toc:Managing OWASP Top 10 2021 in GeneXus Applications](https://wiki.genexus.com/commwiki/wiki?50180) |

---
