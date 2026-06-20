---
title: "Versioning the application to manage the different stages of Validation or Approval"
source_id: 20938
source_url: https://wiki.genexus.com/commwiki/wiki?20938
genexus_version: "18"
---

# Versioning the application to manage the different stages of Validation or Approval

Versioning the application to manage the different stages of Validation or Approval is one of the [Version Management and Work Methodology with GeneXus Server](https://wiki.genexus.com/commwiki/wiki?20649,,) scenarios.

It is common for companies to subject the versions released to clients or set for production to a validation or testing stage that takes place after the Commit done by developers.

Such validation may be done in a single stage (where the case would be similar to the scenario described in [Defining versions for each application release](https://wiki.genexus.com/commwiki/wiki?20945)). Or, as it often happens, in multiple successive stages, each meant to test or validate a particular aspect of the development.

For instance, in a given project, you could have the following stages:

* Code Review
  + Is the code correctly written?
  + Does it abide by the internal standards of nomenclature, documentation, modularization, security, etc.?
* Integration Test
  + Is the compilation, set up and functioning correctly following the integration with other modules or components in the final product?
* Functional Test
  + Does the system correctly perform the functionalities defined?
* Pre-Production Test
  + Does it function properly in an environment copied from the one used for production (hardware, DBMS, Web Server, configurations, data, etc.?

Each of these stages is completed one after the other, and you can only go on to the next level when the previous one has been approved.

For example, if a particular change does not satisfy the Code Review, then you cannot go ahead with the Integration Test.

For this reason, in this scenario, you need to define versions to manage the different stages of the validation or approval.

### [Version Management](#Version+Management)

You first see a simplified scenario, with a single validation stage. For this simplified scenario, you will have to create a parallel version for the developers to work on based on the main version. Those in charge of carrying out the tests will be the ones who, in the event of the tests proving successful, will pass the changes on to the main version. This development version is created on the KB of GXserver, using the console or from the dialogue of Team Development in GeneXus, Tab Versions.

`[imagen omitida: wiki id 34527]`

Work Methodology with one validation stage

For implementing this method using GeneXus Server, you will first see a simple scenario where you work with one development version and a single validation step, since you can perform additional stages in an analogous manner.

The development and testing work is organized as follows:

* **One development team:** Each developer collaborates with a local Knowledge Base local connected to GeneXus Server, on the development version (Development Branch)
* **One testing team:** Each tester works with a local Knowledge Base attached to the General version and uses [Bring Changes](https://wiki.genexus.com/commwiki/wiki?20912,,) to bring changes from the development version. In case the changes are approved, the [Commit to GeneXus Server](https://wiki.genexus.com/commwiki/wiki?10626) is done in the main version. The development team must be notified of the changes that have not been approved.

Every time that a developer needs to consolidate changes with the Knowledge Base in [GeneXus Server](https://wiki.genexus.com/commwiki/wiki?9911), he must do a [Commit to GeneXus Server](https://wiki.genexus.com/commwiki/wiki?10626).

Likewise, when a developer needs to obtain the changes done by another developer, he must do an [Update From GeneXus Server](https://wiki.genexus.com/commwiki/wiki?10627), to update the objects.

Therefore, the General version keeps the changes that have been validated.

With a Knowledge Base connected to that version it is possible to do [Update From GeneXus Server](https://wiki.genexus.com/commwiki/wiki?10627) and execute the application set up process, to take to the client the corresponding programs and the reorgs files.

`[imagen omitida: wiki id 34545]`

### [Work Methodology with two validation stages](#Work+Methodology+with+two+validation+stages)

As mentioned, you can have a single validation stage or several stages, and for the case of several steps, you work in parallel with several versions, with the requirement of passing changes on from one version to the other every time that changes are approved.

In this case, the work methodology is similar to scenario [Defining versions for each application release](https://wiki.genexus.com/commwiki/wiki?20945). In addition to describing a parallel version for development, you can identify as many parallel versions as there are additional validation stages.

For cases with two validation steps, like for example, Development Version, Integrated Test, and Production, you must define the following versions, all derived from the General version.

`[imagen omitida: wiki id 34548]`

* **Development Branch**: this is the version on which the developers work and do [Commit to GeneXus Server](https://wiki.genexus.com/commwiki/wiki?10626).
* **Integrated Test**: those doing integration tests have Knowledge Bases connected to this version. They do Update to obtain the changes approved by other integrators, [Bring Changes](https://wiki.genexus.com/commwiki/wiki?20912,,) to bring in the changes from the development version, [Commit to GeneXus Server](https://wiki.genexus.com/commwiki/wiki?10626) to approve changes, and Revert for changes that are not to be done.
* **General**: To set up the final version to be released or to roll it out, use a Knowledge Base connected to the main version, from where you do [Update From GeneXus Server](https://wiki.genexus.com/commwiki/wiki?10627) and Build.

`[imagen omitida: wiki id 34550]`

### [More than two validation stages](#More+than+two+validation+stages)

When you have the following stages: Code review, Integration Test, Functional Test, Pre-production Test, you should define the following versions, all derived from the main version and the same base point:

* **Development.** This is the version on which developers work and do [Commit to GeneXus Server](https://wiki.genexus.com/commwiki/wiki?10626).
* **Review.** This is the version on which those responsible for reviewing the code will work. They do Update to obtain the changes approved by other reviewers, Bring Changes to bring the changes from the Development version, [Commit to GeneXus Server](https://wiki.genexus.com/commwiki/wiki?10626) to accept changes, and Revert when changes are not approved (in addition to notifying the developer regarding any errors found).
* **Integrated**. Those who do the integration test have Knowledge Bases connected to this version. They do Update to obtain the changes approved by other integrators, Bring Changes to bring changes of the Reviewed version, [Commit to GeneXus Server](https://wiki.genexus.com/commwiki/wiki?10626) to accept changes, and Revert when changes are not approved.
* **Functional.** This version is used by the functional testing team. As in the other stages, Bring Changes is used here to obtain changes from the previous stage, and [Commit to GeneXus Server](https://wiki.genexus.com/commwiki/wiki?10626) is used to approve the changes.

The last testing stage, called Pre-Production, is done with a Knowledge Base connected to the main version, used to set up an environment equal to the one that will be utilized for production, and trying to make is as similar as possible in what concerns hardware, software installed, configurations, and even operational data. The changes to be tested are obtained with Bring Changes from the Functional version, and only when the changes have been approved in this pre-production test, you can [Commit to GeneXus Server](https://wiki.genexus.com/commwiki/wiki?10626) on the main version.

To set up the final version to be released or to roll it out, use a Knowledge Base connected to the main version, from where you can only do [Update From GeneXus Server](https://wiki.genexus.com/commwiki/wiki?10627) and Build.

You could go on with this scheme, and based on what you have seen, what grows is the middle column, where you can continue adding further validation stages (notice the different profiles with different colors and how the central profile increases).


|  |
| --- |
| **Backlinks** |
|
| [Versioning the application by Modules](https://wiki.genexus.com/commwiki/wiki?20937) |

---
