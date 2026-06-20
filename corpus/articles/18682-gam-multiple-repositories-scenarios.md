---
title: "GAM - Multiple Repositories Scenarios"
source_id: 18682
source_url: https://wiki.genexus.com/commwiki/wiki?18682
genexus_version: "18"
---

# GAM - Multiple Repositories Scenarios

There are cases where only one [GAM](https://wiki.genexus.com/commwiki/wiki?14960) Repository is not enough to model the reality of our application or company.

Remember that when [Enable Integrated Security Property](https://wiki.genexus.com/commwiki/wiki?14706) is set to True in the application, it connects to an external data store (named "GAM") where many [Repositories](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?18463,,) can reside. See [GAM Repository](https://wiki.genexus.com/commwiki/wiki?17568) for details.

The model design of GAM enables to connect to multiple Repositories to solve many scenarios where only one Repository wouldn't be enough. The security module of Multi-tenant applications can be implemented based on this feature, as well as other types of applications, which are detailed below.

In this document you will find some typical applications and scenarios which can be designed using GAM as their Security Module and it is also explained how to manage multiple Repositories in each case.

### [Scenario 1. The same application installation is shared by many companies (Multi-Tenant application)](#Scenario+1.+The+same+application+installation+is+shared+by+many+companies+%28Multi-Tenant+application%29)

See [Multiple Repository Scenario: The same application installation is shared by many companies](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?18710,,)

### [Scenario 2. A company with different branches](#Scenario+2.+A+company+with+different+branches)

Users have different [Security Policies](https://wiki.genexus.com/commwiki/wiki?18521), [Roles](https://wiki.genexus.com/commwiki/wiki?17569) and [Permissions](https://wiki.genexus.com/commwiki/wiki?15912) in each branch.

In this scenario of use, the company has different branches, and users have different security policies, roles and permissions depending on the branch where the application runs.  
There is no need to define one GAM Database for each branch, because users would need to be redundant in each GAM Database. By defining a Repository for each branch, users are the same (and defined only once) in GAM Database.

See [Multiple Repositories Scenario: A company with different branches](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?18709,,)

### [See Also](#See+Also)

[HowTo: Create New Repositories using GAM](https://wiki.genexus.com/commwiki/wiki?18642)  
[Managing GAM Repositories and GAM Applications in GX development time](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?18685,,)


|  |
| --- |
| **Backlinks** |
| [GAM - Authentication Scenarios](https://wiki.genexus.com/commwiki/wiki?15937) | [GAM - Repository](https://wiki.genexus.com/commwiki/wiki?17568) | [GAM - Users](https://wiki.genexus.com/commwiki/wiki?22082) |
| [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [HowTo: Manage repositories using gamadmin user](https://wiki.genexus.com/commwiki/wiki?44904) |
|

---
