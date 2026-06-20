---
title: "Testing Automation Pyramid"
source_id: 38333
source_url: https://wiki.genexus.com/commwiki/wiki?38333
genexus_version: "18"
---

# Testing Automation Pyramid

Modern software engineering, agile development, and DevOps practices are based on the pipeline approach, where any idea (feature or change request) is built through pipes strongly based on different automation layers. The test Automation process is an (if not the most) important key to deliver valuable software systematically.

There are several layers of test automation that adds value to the pipeline, depending on factors like cost of automation, how often and how fast tests are running, where (in which environment) the test runs, and how valuable/effective checks are.

The following image represents the ideal test automation layers, being Unit tests the fastest and the cheapest. On the other hand, UI (end-to-end) tests are quite slow and more expensive.

`[imagen omitida: wiki id 42826]`

Of course, the exact mix of tests will depend on each team, but the efforts invested on each specific test approach should respect this pyramid, especially in GeneXus.

## [Why?](#Why%3F)

[Unit Tests](https://wiki.genexus.com/commwiki/wiki?38334) are the **most important layer of testing** on GeneXus apps, basically because of these 3 main reasons:

* They are **reliable and fast**: Unit test run in order of ms, depending on how many business logic is running in your procedures (usually depends on SQL / DB times).
* Easy to create and debug: It is very easy to create and debug tests inside GeneXus IDE, and their results **isolate failures**.
* Provides **immediate feedback** to Developers: Each time a procedure change and is built, Genexus can run these tests automatically in a dev environment and provide immediate feedback to the user if that test is now broken.

Additionally, all GeneXus developers need to run/debug their procedures in some way after writing down some procedures. Traditionally they test input/ output using self-made Web Panels or UI to run it using different input and evaluating outputs. All this effort can be reduced (and automated) by using the new Test feature inside GeneXus, and by letting those tests as an important asset to your Knowledge Base.

Unit test has a major disadvantage, which is that even in an isolated way, some function works as expected, the system as a whole (integrated with different components) can be buggy. GeneXus apps often designed to expose services through SOAP or REST APIs, providing an important entry point to test business logic together. That’s why it is recommended to automate as-much-as-you-can API / Service test.   
In that case, API automation brings an excellent opportunity since they:

* run quite fast.
* test core-functionality (without UI).
* Are easy to integrate into a CI/CD pipeline

When your core business logic is encapsulated inside GeneXus procedures and Data Providers, then you will take advantage of unit testing with the best ROI. On the other hand, when the logic that you want to test is not in Procedures but encapsulated on panels (i.e. WebPanels or SD Panels which is also a very bad programming practice in GeneXus), then you will need to test your features using a different approach.

So, UI tests are the last layer (traditionally the preferred approach in GeneXus). UI test automation can be flaky, and very dependant on your test infrastructure, data, frameworks used and browser versions, but still the only way to simulate real user interactions.

To get the best of UI test automation it is recommended to start building test from:  
The app: by recording a new test case using your application.  
The Knowledge Base: by auto-generating UI test skeleton based on your WebPanel definition.


## [Recommended references](#Recommended+references)

* [Google Testing Blog](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html)
* [Abstracta Blog](https://abstracta.us/blog/test-automation/best-testing-practices-agile-teams-automation-pyramid)
* [Martin Fowler](https://martinfowler.com/bliki/TestPyramid.html)

---

|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) | [Methodology](https://wiki.genexus.com/commwiki/wiki?38367) |
| [UI Test for Web Automation](https://wiki.genexus.com/commwiki/wiki?38353) |

---
