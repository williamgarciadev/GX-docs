---
title: "Running tests on remote browsers"
source_id: 43877
source_url: https://wiki.genexus.com/commwiki/wiki?43877
genexus_version: "18"
---

# Running tests on remote browsers

GXtest 4 supports Selenium-Grid to run your UI tests.

The first step that we must follow is to have a Selenium node listening for running tests over some IP/port. There are several ways to set up a Selenium node, you can use [NPM](https://www.npmjs.com/package/selenium-webdriver), [Docker](https://github.com/SeleniumHQ/docker-selenium), [Homebrew](https://stackoverflow.com/questions/18868743/how-to-install-selenium-webdriver-on-mac-os) and others, or you can just [download](https://www.seleniumhq.org/download/) the .war and [launch it using Java](https://github.com/SeleniumHQ/selenium/wiki/Grid2). Note that is possible that you need administrator rights to launch the selenium standalone server.

For example,

Suppose that you are working on machine A(local) and you want to run a UI test in a remote browser in machine B (real or virtual). Firstly, you must to [start the hub and the Selenium node](https://www.seleniumhq.org/docs/07_selenium_grid.jsp) in machine B.  After that, you just have to use the following commands at the beginning of your UI test:

```
      SetRemoteWebDriver("http://<IP_machineB>:<hubPort>/wd/hub")
      AddCapability("capabilityName","capabilityValue")
```

Note, the <IP\_machineB> value will depend on what kind of machine B is. If machine B is part of your local area network (LAN), the <IP\_machineB> will be the IPv4. If machine B is not part of your local area network, the <IP\_machineB> will be the public IP.

It is important to check the correct hub port status, the <hubPort> value should be open to access from machine A. When you launch the hub in machine B, the <hubPort> value by default is 4444.

A simple UItest example,

```
&driver.SetRemoteWebDriver("http://sampleServer.com:4444/wd/hub")
&driver.AddCapability("browser","Chrome")
&driver.Start()
&driver.Go("homeURL")
// Do actions and validations
&driver.End()
```


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) |

---
