---
title: "About GeneXus Upgrades Adoption"
source_id: 28016
source_url: https://wiki.genexus.com/commwiki/wiki?28016
genexus_version: "18"
---

# About GeneXus Upgrades Adoption

This article is intended to clarify the steps you need to follow to adopt a GeneXus Upgrade.   
  
Each GeneXus Upgrade contains features, improvements, and bug fixes and some of them may include compatibility issues, breaking changes that require special steps.  Each released upgrade contains Release Notes that contain details of the content, including a Compatibility Section that contain all those issues that may need your special attention.

Supposing you have already systems in production generated with Upgrade N of some GeneXus version and you want to update them generating with Upgrade M, M>N; you need to follow at least these steps:

1. Backup your GeneXus installation, Knowledge Base and also your Prototyping Environment (Programs and Databases)
2. Read the Compatibility section of the Release Notes of each upgrade Y, N  < Y<=M, playing special attention to issues related to changes in Hardware and Software Requirements
3. Install Upgrade M, M>N. Check out [About GeneXus Upgrades Installation](https://wiki.genexus.com/commwiki/wiki?14443)
4. Make sure you have a baseline of your regression Tests
5. If the different Release Notes require you to change some configuration or coding due to breaking changes, apply that changes to your Knowledge Base
6. Rebuild All
7. Run your Regression Tests
8. Verify that your prototyping environment generated with upgrade M works equal to or better than the previous upgrade N
9. Adopt new features
10. Test & validate again
11. Read the Release Notes again in order to know if some special steps are needed to take your system to the Production Environment
12. Publish your system

Disclaimer: If your GeneXus Installation contains some User Controls, Patterns, and other third-party Extensions and they are updated, also read their Release Notes in order to know what else needs to be taken into account.
