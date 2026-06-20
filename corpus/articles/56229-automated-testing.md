---
title: "Automated Testing"
source_id: 56229
source_url: https://wiki.genexus.com/commwiki/wiki?56229
genexus_version: "18"
---

# Automated Testing

Testing is one of the main stages in software development, and most of the times it is the bottleneck of it. The approach to overcome this problem is to delve into testing automation.

In this table of contents are presented all the objects, practices, and tools that GeneXus offers to achieve high-quality software through the usage of GXtest, the tool for testing automation built-in the IDE.

In the following video, the basics of testing in GeneXus is presented.

And the new features regards testing in GeneXus 18 are presented in the following video


## [Contents](#Contents)

* [Testing Automation Pyramid](https://wiki.genexus.com/commwiki/wiki?38333)
* Requirements
  + [GXtest 4 Installation](https://wiki.genexus.com/commwiki/wiki?41446)
* [Unit Testing](https://wiki.genexus.com/commwiki/wiki?38334)
  + [Creating Unit tests](https://wiki.genexus.com/commwiki/wiki?38337)
  + [Assertions](https://wiki.genexus.com/commwiki/wiki?38336)
  + [Running Unit tests](https://wiki.genexus.com/commwiki/wiki?38345)
  + [Database Mocking](https://wiki.genexus.com/commwiki/wiki?38349)
  + [How to validate object execution time](https://wiki.genexus.com/commwiki/wiki?53786)
  + [CI / CD integration](https://wiki.genexus.com/commwiki/wiki?38332)
* Service Testing
  + [Rest Test](https://wiki.genexus.com/commwiki/wiki?50074)
* [UI Test for Web Automation](https://wiki.genexus.com/commwiki/wiki?38353)
  + [Introduction](https://wiki.genexus.com/commwiki/wiki?40280)
  + [Locating controls](https://wiki.genexus.com/commwiki/wiki?47719)
  + [Recording tests](https://wiki.genexus.com/commwiki/wiki?40310)
  + [Running tests on different browsers](https://wiki.genexus.com/commwiki/wiki?41128)
  + [Running tests on remote browsers](https://wiki.genexus.com/commwiki/wiki?43877)
  + [Supported commands](https://wiki.genexus.com/commwiki/wiki?40281)
    - [WebDriver](https://wiki.genexus.com/commwiki/wiki?41690)
    - [Browser](https://wiki.genexus.com/commwiki/wiki?41616)
    - [Taking screenshots](https://wiki.genexus.com/commwiki/wiki?49711)
    - [Get Text from PDF](https://wiki.genexus.com/commwiki/wiki?49951)
    - [Click](https://wiki.genexus.com/commwiki/wiki?41647)
    - [Select](https://wiki.genexus.com/commwiki/wiki?41650)
    - [Type](https://wiki.genexus.com/commwiki/wiki?41649)
    - [Send Keys](https://wiki.genexus.com/commwiki/wiki?41651)
    - [Drag and Drop](https://wiki.genexus.com/commwiki/wiki?47574)
    - [File Upload](https://wiki.genexus.com/commwiki/wiki?45868)
    - [Get Text](https://wiki.genexus.com/commwiki/wiki?41680)
    - [Get Messages](https://wiki.genexus.com/commwiki/wiki?47281)
    - [Get Value](https://wiki.genexus.com/commwiki/wiki?41681)
    - [Grids](https://wiki.genexus.com/commwiki/wiki?47283)
    - [Control Presence](https://wiki.genexus.com/commwiki/wiki?45802)
    - [Control Visibility](https://wiki.genexus.com/commwiki/wiki?45804)
    - [Control Enabling](https://wiki.genexus.com/commwiki/wiki?45803)
    - [Control Focus](https://wiki.genexus.com/commwiki/wiki?45805)
    - [Verify](https://wiki.genexus.com/commwiki/wiki?45806)
    - [Image Comparison](https://wiki.genexus.com/commwiki/wiki?48889)
    - [Assertions](https://wiki.genexus.com/commwiki/wiki?41682)
    - [Timeouts](https://wiki.genexus.com/commwiki/wiki?41632)
    - [Waiters](https://wiki.genexus.com/commwiki/wiki?41633)
    - [Alerts](https://wiki.genexus.com/commwiki/wiki?41686)
    - [Mouse Move](https://wiki.genexus.com/commwiki/wiki?41653)
    - [Edit Content](https://wiki.genexus.com/commwiki/wiki?41652)
    - [Submit](https://wiki.genexus.com/commwiki/wiki?41684)
    - [Frames](https://wiki.genexus.com/commwiki/wiki?41685)
    - [Windows and tabs](https://wiki.genexus.com/commwiki/wiki?41683)
    - [Get / Set Attribute](https://wiki.genexus.com/commwiki/wiki?43904)
    - [Property setters](https://wiki.genexus.com/commwiki/wiki?48468)
    - [Custom Commands](https://wiki.genexus.com/commwiki/wiki?47402)
  + [Running UI tests under CI](https://wiki.genexus.com/commwiki/wiki?40737)
* [UI Test for Native Mobile Automation](https://wiki.genexus.com/commwiki/wiki?44571)
* [Test Suite object](https://wiki.genexus.com/commwiki/wiki?47819)
* [Test Preferences](https://wiki.genexus.com/commwiki/wiki?45420)
* Interface
  + [Tests Explorer window](https://wiki.genexus.com/commwiki/wiki?47575)
  + [Test Results window](https://wiki.genexus.com/commwiki/wiki?47576)
  + [Menu Commands](https://wiki.genexus.com/commwiki/wiki?48103)
  + [Test Execution Results Report](https://wiki.genexus.com/commwiki/wiki?43925)
* Coverage
  + [Code Coverage and Profiling](https://wiki.genexus.com/commwiki/wiki?44369)
  + [Test Coverage](https://wiki.genexus.com/commwiki/wiki?44954)
* CI / CD
  + [MSbuild Tasks for Running Tests](https://wiki.genexus.com/commwiki/wiki?40738,,)
  + [Using MSbuild Example](https://wiki.genexus.com/commwiki/wiki?40739)
  + [GXtest-Docker-Selenium](https://wiki.genexus.com/commwiki/wiki?41202,,)
* [Deploying Tests](https://wiki.genexus.com/commwiki/wiki?54122)
* Other Integrations
  + [Test case sets from JSON](https://wiki.genexus.com/commwiki/wiki?47773)
  + [Read test data from CSV](https://wiki.genexus.com/commwiki/wiki?49717)
  + [How to create a unit test and add a task using the GeneXus Jenkins Plugin](https://wiki.genexus.com/commwiki/wiki?38359)
  + [Allure test reports for Jenkins](https://wiki.genexus.com/commwiki/wiki?47611)
  + [JUnit test reports for Jenkins](https://wiki.genexus.com/commwiki/wiki?41320)
  + [Saucelabs - Running test on the cloud](https://wiki.genexus.com/commwiki/wiki?41131)
* [Testing Best Practices](https://wiki.genexus.com/commwiki/wiki?45031,,)
* [FAQ](https://wiki.genexus.com/commwiki/wiki?41196)
* [Troubleshooting](https://wiki.genexus.com/commwiki/wiki?46828)
* [Released Versions](https://wiki.genexus.com/commwiki/wiki?43829)
* [Changelog](https://wiki.genexus.com/commwiki/wiki?43807)
* [Reporting an incident](https://wiki.genexus.com/commwiki/wiki?44961)

---
