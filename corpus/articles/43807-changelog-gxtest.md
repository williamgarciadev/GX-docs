---
title: "Changelog GXtest"
source_id: 43807
source_url: https://wiki.genexus.com/commwiki/wiki?43807
genexus_version: "18"
---

# Changelog GXtest

The table below describes the main changes made to GXtest for GeneXus 18 upgrades. The beta version includes all the changes in stable and preview channels.


### [**GXtest Beta**](#GXtest+Beta)

**Date**: By night-build.  
**Version**: 4.18.13.X  
**Release**: GeneXus 18 - Beta Channel  
`[imagen omitida: wiki id 40856]` [Download](https://gxtest-downloads.s3.amazonaws.com/develop/GXtest_Beta.zip)

What's new?

* [Create Rest Tests from API object](https://wiki.genexus.com/commwiki/wiki?59799)

Bugfixes:

* CUTFO when there is only one input parameter does not generate all test cases if the algorithm is Pair Wise

### [**GXtest for GeneXus 18 Preview**](#GXtest+for+GeneXus+18+Preview)

**Date**: By night-build.  
**Version**: 4.18.10.X  
**Release**: GeneXus 18 - Preview Channel  
`[imagen omitida: wiki id 40856]` [Download](https://gxtest-downloads.s3.amazonaws.com/staging/GXtest_Stable.zip)

What's new: -

Bugfixes: -

### [**GXtest for GeneXus 18 upgrade 10, 11 and 12**](#GXtest+for+GeneXus+18+upgrade+10%2C+11+and+12)

**Date**: June 26th, 2024.  
**Version**: 4.18.10.29126  
**Release**: GeneXus 18 Upgrade 10

What's new.

* Open the test with the cursor positioned in the selected step from the Tests Results window
* [Create Web UI Test command](https://wiki.genexus.com/commwiki/wiki?48103) from Web Panels and Transactions

Bugfixes:

* Compatibility changes

### [**GXtest for GeneXus 18 upgrade 9**](#GXtest+for+GeneXus+18+upgrade+9)

**Date**: April 23rd, 2024.  
**Version**: 4.18.9.27634  
**Release**: GeneXus 18 Upgrade 9

What's new.

* [Tests Coverage window](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?57475,,) and [Measure Tests Coverage MSBuild task](https://wiki.genexus.com/commwiki/wiki?40738)
* Added support for browser preferences by using *pref::* prefix in AddCapability command

Bugfixes:

* ClickByLinkText when the link is not in the viewport
* Improvements in Set As Expected feature

### [**GXtest for GeneXus 18 upgrade 8**](#GXtest+for+GeneXus+18+upgrade+8)

**Date**: February 20th, 2024.  
**Version**: 4.18.8.26106  
**Release**: GeneXus 18 upgrade 8

What's new.

* Procedures mock for unit testing: [Objects Mock](https://wiki.genexus.com/commwiki/wiki?55859)
* Added [a property](https://wiki.genexus.com/commwiki/wiki?45420) that enables displaying unit tests in KB Explorer as children of the objects they call to
* Included coverage percentage in the HTML report
* Added context menu option to create a mock from a Procedure

Bugfixes: -

### [**GXtest for GeneXus 18 upgrade 7**](#GXtest+for+GeneXus+18+upgrade+7)

**Date**: December 18th, 2023.  
**Version**: 4.18.7.25280  
**Release**: GeneXus 18 upgrade 7

What's new.

* The first difference in assertions is shown in the JUnit report for texts longer than 20 characters
* Added new HTML report template in Japanese
* Added the Module parameter for [RunTests msbuild task](https://wiki.genexus.com/commwiki/wiki?40738), allowing to execute all the tests contained in the given module

Bugfixes: -

### [**GXtest for GeneXus 18 upgrade 6**](#GXtest+for+GeneXus+18+upgrade+6)

**Date**: November 3rd, 2023.  
**Version**: 4.18.6.24222  
**Release**: GeneXus 18 upgrade 6

Bugfixes:

* Web UI Tests not running for Chrome versions greater than 115.

### [**GXtest for GeneXus 18 upgrade 5**](#GXtest+for+GeneXus+18+upgrade+5)

**Date**: August 29th, 2023.  
**Version**: 4.18.5.23891  
**Release**: GeneXus 18 Upgrade 5

What's new.

* Set As Expected button available in the Assertion comparison tab
* Improved [HTML Report](https://wiki.genexus.com/commwiki/wiki?43925)
* Improved SDT and SDT collections initialization when using the Create Unit Test option
* Enabled filtering by the result of the tests in the Tests Results window
* No license is required to use DB Mocking

Bugfixes:

* Running unit tests only starts the Kestrel server
* Screenshots and HTML can be seen properly in the HTML report

Warning:

* If you use Web UI Tests, due to an external incompatibility issue, tests execution will not work for Chrome versions 115 and higher.

### [**GXtest for GeneXus 18 upgrade 4**](#GXtest+for+GeneXus+18+upgrade+4)

**Date**: July 4th, 2023.  
**Version**: 4.18.4.23542  
**Release**: GeneXus 18 Upgrade 4

What's new.

* Now webdrivers are not delivered by GXtest. Instead, a built-in drivers manager is used.
* Improvements in the [CompareImage command](https://wiki.genexus.com/commwiki/wiki?48889). Added a new parameter to set color similarity tolerance.
* Set modules and folders as generated to prevent conflicts when committing/updating objects from GXserver
* Improved tests' deployment for Java. Check: [Deploying Tests](https://wiki.genexus.com/commwiki/wiki?54122)

Bugfixes:

* Error finishing web UI test execution in Java

 Warning:

* If you use Web UI Tests, due to an external incompatibility issue, tests execution will not work for Chrome versions 115 and higher.

### [**GXtest for GeneXus 18 upgrade 3**](#GXtest+for+GeneXus+18+upgrade+3)

**Date**: April 26th, 2023.  
**Version**: 4.18.3.23228  
**Release**: GeneXus 18 Upgrade 3

What's new.

* Test objects can be included in Deployment Units. Check: [Deploying Tests](https://wiki.genexus.com/commwiki/wiki?54122)
* Tests can be run in parallel via MSBuild. Check: [Running MSbuild using GXtest Target](https://wiki.genexus.com/commwiki/wiki?40739)
* Added option Run All Unit Tests in the Test menu with shortcut Ctrl + Shift + U
* Added a Select All / Unselect All checkbox in the Tests Explorer window. The Run button was moved to the top.

Bugfixes:

* Test Suite's set up and tear down objects throwing errors in runtime when inside modules
* Java interpreter options for environment are used when running tests now too
* SendKeys command not working for combined keys in net

### [**GXtest for GeneXus 18 upgrade 2**](#GXtest+for+GeneXus+18+upgrade+2)

**Date**: February 17th, 2023.  
**Version**: 4.18.2.22604  
**Release**: GeneXus 18 Upgrade 2

What's new.

* -

Bugfixes:

* Running with Java version in a custom path
* Tab name for screenshots was not adjusted for long command names

### [**GXtest for GeneXus 18 upgrade 1**](#GXtest+for+GeneXus+18+upgrade+1)

**Date**: December 21st, 2022.  
**Version**: 4.18.1.22459  
**Release**: GeneXus 18 Upgrade 1

What's new.

* Added support for strong-named assemblies in .Net Framework
* Added a [combo box and property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?52800,,) to choose the type of build performed when running test in GeneXus IDE (Don't Build, Build With These Only, Build, Rebuild)
* The assertion message is shown in the Comparer window
* Execution results are stored in TestResults folder for each environment and can be opened from [Tests Results window](https://wiki.genexus.com/commwiki/wiki?47576)
* Stack trace, exception types, and inner exceptions are logged for .Net environments when a test execution throws an error
* The browser's log is now shown when a Web UI Test command fails
* Added property to enable/disable the use of mock data at environment level: [Use Mock Data property](https://wiki.genexus.com/commwiki/wiki?45420)

Bugfixes:

* Calling the RunTests MSBuild task without parameters was running nothing, now it runs all tests.

### [**GXtest for GeneXus 18**](#GXtest+for+GeneXus+18)

**Date**: November 10th, 2022.  
**Version**: 4.18.0.21956  
**Release**: GeneXus 18

What's new.

* Updated Test objects' icons
* Added [support for shadow DOMs](https://wiki.genexus.com/commwiki/wiki?47719) through >>> selector
* Added boolean Build parameter to RunTests MSBuild task, allowing to choose whether building tests or not before executing them

Bugfixes:

* GXtest output is focused when creating a new KB
* Execution of more than 1000 tests wrongly reporting build failed
* Create Rest Test for objects without parameters does not call via HTTP
* Create Rest Test generates test source commented when parameters are attributes of some specific types
* Start Kestrel server when running web UI Tests in .Net environments

---

---

|  |
| --- |
| **Backlinks** |
| [Table of contents:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) |
| [Table of contents:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) |
| [GXtest 4 Releases - Public Channels](https://wiki.genexus.com/commwiki/wiki?42858) |

---
