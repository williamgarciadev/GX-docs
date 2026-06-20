---
title: "GXtest"
source_id: 38327
source_url: https://wiki.genexus.com/commwiki/wiki?38327
genexus_version: "18"
---

# GXtest

## [What is GXtest?](#What+is+GXtest%3F)

GXtest is the test automation solution for GeneXus-based applications. Each component adds different automation layers to GeneXus' development lifecycle, such as Unit Testing and UI Test Automation.

All tests are designed to run under CI / CD servers such as Jenkins, by spinning dockerized containers harnessing DevOps culture. This means that tests can easily run on the developer's IDE, over on-premises / PaaS solutions or even in the cloud.

## [Where can you get it?](#Where+can+you+get+it%3F)

GXtest is currently included inside GeneXus IDE.

GXtest is published continuously over [Beta and Preview GeneXus channels](https://wiki.genexus.com/commwiki/wiki?43829). You can look at the [mapping between every GeneXus and GXtest versions](https://wiki.genexus.com/commwiki/wiki?42858).

## [Requirements](#Requirements)

* [GeneXus requirements](https://wiki.genexus.com/commwiki/wiki?30900)
* [GXserver](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?26438,,) to use licensed features
* [Google Chrome](https://www.google.com/intl/es/chrome/) to use GXtest Recorder
* [Selenium](https://www.seleniumhq.org/) to run tests from remote browsers.

## [GXtest License](#GXtest+License)

GXtest has both free and licensed features. See the [details about the licensing model](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?41571,,).

GXtest is built by GeneXus and [Abstracta](https://abstracta.us).


## [Contents](#Contents)

* [Installation](https://wiki.genexus.com/commwiki/wiki?41446)
* [Methodology](https://wiki.genexus.com/commwiki/wiki?38367)
  + [Agile Development](https://wiki.genexus.com/commwiki/wiki?39195)
  + [Typical GeneXus development cycle for Agile](https://wiki.genexus.com/commwiki/wiki?38329)
  + [Testing Automation Pyramid](https://wiki.genexus.com/commwiki/wiki?38333)
  + [Strategies for Data Setup in Test Automation](https://wiki.genexus.com/commwiki/wiki?56320)
* [Unit Testing](https://wiki.genexus.com/commwiki/wiki?38334)
  + [Creating Unit tests](https://wiki.genexus.com/commwiki/wiki?38337)
  + [Assertions](https://wiki.genexus.com/commwiki/wiki?38336)
  + [Running Unit tests](https://wiki.genexus.com/commwiki/wiki?38345)
  + [Database Mocking](https://wiki.genexus.com/commwiki/wiki?38349)
  + [Objects Mock](https://wiki.genexus.com/commwiki/wiki?55859)
  + [Execution time validation](https://wiki.genexus.com/commwiki/wiki?53786)
  + [CI / CD integration](https://wiki.genexus.com/commwiki/wiki?38332)
* Service Testing
  + [Rest Test](https://wiki.genexus.com/commwiki/wiki?50074)
* [UI Test for Web Automation](https://wiki.genexus.com/commwiki/wiki?38353)
  + [Introduction](https://wiki.genexus.com/commwiki/wiki?40280)
  + [Locating controls](https://wiki.genexus.com/commwiki/wiki?47719)
  + [Recording tests](https://wiki.genexus.com/commwiki/wiki?40310)
  + [Running tests on different browsers](https://wiki.genexus.com/commwiki/wiki?41128)
  + [Running tests on remote browsers](https://wiki.genexus.com/commwiki/wiki?43877)
  + [Running tests with a proxy](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?58668,,)
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
* [Test Suite object](https://wiki.genexus.com/commwiki/wiki?47819)
* [Test Preferences](https://wiki.genexus.com/commwiki/wiki?45420)
* Interface
  + [Tests Explorer window](https://wiki.genexus.com/commwiki/wiki?47575)
  + [Test Results window](https://wiki.genexus.com/commwiki/wiki?47576)
  + [Tests Coverage window](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?57475,,)
  + [Menu Commands](https://wiki.genexus.com/commwiki/wiki?48103)
  + [Test Execution Results Report](https://wiki.genexus.com/commwiki/wiki?43925)
* Coverage
  + [Code Coverage and Profiling](https://wiki.genexus.com/commwiki/wiki?44369)
  + [Test Coverage](https://wiki.genexus.com/commwiki/wiki?44954)
* CI / CD
  + [MSbuild Tasks](https://wiki.genexus.com/commwiki/wiki?40738)
  + [Using MSbuild Example](https://wiki.genexus.com/commwiki/wiki?40739)
  + [GXtest-Docker-Selenium](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?41202,,)
* [Deploying Tests](https://wiki.genexus.com/commwiki/wiki?54122)
* Other Integrations
  + [Test case sets from JSON](https://wiki.genexus.com/commwiki/wiki?47773)
  + [Read test data from CSV](https://wiki.genexus.com/commwiki/wiki?49717)
  + [How to create a unit test and add a task using the GeneXus Jenkins Plugin](https://wiki.genexus.com/commwiki/wiki?38359)
  + [Allure test reports for Jenkins](https://wiki.genexus.com/commwiki/wiki?47611)
  + [JUnit test reports for Jenkins](https://wiki.genexus.com/commwiki/wiki?41320)
  + [Saucelabs - Running test on the cloud](https://wiki.genexus.com/commwiki/wiki?41131)
* [Testing Best Practices](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?45031,,)
* [FAQ](https://wiki.genexus.com/commwiki/wiki?41196)
* [Troubleshooting](https://wiki.genexus.com/commwiki/wiki?46828)
* [Released Versions](https://wiki.genexus.com/commwiki/wiki?43829)
* [Changelog](https://wiki.genexus.com/commwiki/wiki?43807)
* [Reporting an incident](https://wiki.genexus.com/commwiki/wiki?44961)

---
