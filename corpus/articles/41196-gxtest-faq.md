---
title: "GXtest - FAQ"
source_id: 41196
source_url: https://wiki.genexus.com/commwiki/wiki?41196
genexus_version: "18"
---

# GXtest - FAQ

In this article, you can find some frequently asked questions (FAQ) about [GXtest](https://wiki.genexus.com/commwiki/wiki?24193,,).

### [General](#General)

#### [**1. Can a test be debugged?**](#1.+Can+a+test+be+debugged%3F)

Yes. You can use [GeneXus debugger](https://wiki.genexus.com/commwiki/wiki?9307) and run tests in a "step by step" mode.

#### [**2. Is the "Build" process affected when using or running tests?**](#2.+Is+the+%22Build%22+process+affected+when+using+or+running+tests%3F+)

Yes. Test objects are part of the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836), which means that running a [Build All or Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691) process in your [KB](https://wiki.genexus.com/commwiki/wiki?2428) will include tests.

#### [**3. Can batch processes be tested?**](#3.+Can+batch+processes+be+tested%3F)

Yes. Unit testing capabilities enable batch processes to be tested.

#### [**4. Where can GXtest be found?**](#4.+Where+can+GXtest+be+found%3F)

GXtest 4 has officially been released inside GeneXus 16 upgrades.  
If you want to install the latest version of GXtest in a custom GeneXus version, you can download and install it on top.

#### [**5. How can the GXtest version build number be known in advance?**](#5.+How+can+the+GXtest+version+build+number+be+known+in+advance%3F)

GXtest channel is released over AWS S3 with a "key" version.  
You can get the version number by using:  https://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectGETtagging.html

### [Building Process](#Building+Process)

#### [**1. Why is a build process triggered before running Unit tests?**](#1.+Why+is+a+build+process+triggered+before+running+Unit+tests%3F)

Unit Tests are special GeneXus Procedures that need to be generated, so each time you run a test, GeneXus checks if there are modifications.

Only if the test itself or one of its dependencies (generated test [Structured Data Type](https://wiki.genexus.com/commwiki/wiki?10021), test [Data Provider](https://wiki.genexus.com/commwiki/wiki?4417), and objects) has changed, then it forces building the test case object. This means that objects in the KB will not be generated unless they are referenced by tests that have references pending to be built.

#### [**2. Does the unit test objects modify the original object spec/generation in any way?**](#2.+Does+the+unit+test+objects+modify+the+original+object+spec%2Fgeneration+in+any+way%3F)

No. They are isolated objects that don't change other object behavior.

### [UI Automation](#UI+Automation)

#### [**1. How are tests run using different browsers?**](#1.+How+are+tests+run+using+different+browsers%3F)

You can change the default browser on your [Knowledge Base Properties](https://wiki.genexus.com/commwiki/wiki?33001) or just do it explicitly on your test using the Browsers' domain. I.e.:

```
&driver.SetBrowser(Browsers.Firefox)
```

#### [**2. How is a test run in a remote browser?**](#2.+How+is+a+test+run+in+a+remote+browser%3F)

GXtest 4 supports Selenium / WebDriver architecture. You will need to have a Selenium node listening for running tests over some IP/port. Then, just use it on your test:

```
&driver.SetRemoteWebDriver(url)
```

#### [**3. How is the same test run against different environments / URLs? (ie. dev, staging, pre-prod)**](#3.+How+is+the+same+test+run+against+different+environments+%2F+URLs%3F+%28ie.+dev%2C+staging%2C+pre-prod%29)

There are 2 ways to do this since the UI test will start running after the Go command:

1- Using the Go command to navigate to different environments:

```
 &driver.Go("http://stagingenv:port/App/home.aspx")
```

2- Or using the "Base URL" property on your KB/Environment in [GeneXus IDE](https://wiki.genexus.com/commwiki/wiki?5272), plus using the Go() command with relative paths, like:

```
&driver.Go(Home.Link())
&driver.Go("home.aspx") // If the object is not in the same KB as the test
```

#### [**4. How are the right targets (HTML elements) used in a Command?**](#4.+How+are+the+right+targets+%28HTML+elements%29+used+in+a+Command%3F)

When simulating user actions over HTML controls, commands need the right target to run against.  
Use GXtest Recorder and after recording a test case, you will be able to use command locators in the Target section:

`[imagen omitida: wiki id 41200]`

#### [**5. Does GXtest4 support Custom Commands (like GXtest v3)?**](#5.+Does+GXtest4+support+Custom+Commands+%28like+GXtest+v3%29%3F)

In older versions of GXtest, there were special commands used to interact with custom HTML elements and JS when it was not possible to use native commands.

This is no longer needed since GXtest 4 can interact with any HTML element on a webpage, even if they are not GeneXus native web controls.

#### [**6. How are validations added over a webPage?**](#6.+How+are+validations+added+over+a+webPage%3F)

Use Assertions: when recording a test, by right-clicking over an HTML control:

`[imagen omitida: wiki id 41201]`

#### [**7. How are test iterations added to use different data inputs and outputs?**](#7.+How+are+test+iterations+added+to+use+different+data+inputs+and+outputs%3F)

You can use a For in the test over a Data Provider or other Data sources to add different interactions.

#### [**8. Can tests using Safari be run, even when the "Browsers" domain's Enum values don't have that option?**](#8.+Can+tests+using+Safari+be+run%2C+even+when+the+%22Browsers%22+domain%27s+Enum+values+don%27t+have+that+option%3F)

Yes. You can run on any browser supported by WebDriver technology.   
To do so, use the SetRemoteWebDriver function to launch your test using a remote browser.


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) |

---
