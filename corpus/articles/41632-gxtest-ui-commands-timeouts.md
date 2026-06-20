---
title: "GXtest UI Commands - Timeouts"
source_id: 41632
source_url: https://wiki.genexus.com/commwiki/wiki?41632
genexus_version: "18"
---

# GXtest UI Commands - Timeouts

Waiters and syncs are one of the biggest headaches in test automation. To avoid that, each time an action is executed against an HTML element GXtest waits (**implicitly**) for that element to be present on the webpage (until a certain amount of seconds) otherwise it will fail and cancel test execution. Moreover, GXtest takes care of several Ajax and JS events to make test automation robust while providing an interface to set timeouts using the following functions:

## [SetImplicitWaitTimeout](#SetImplicitWaitTimeout)

`[imagen omitida: wiki id 41635]`

Sets maximum wait time (in seconds) that GXtest will wait for an element, on every interaction with the webpage. It must be used **before** the Start command.

Default value: 2s

Parameters:

* seconds: the number of seconds to wait for.

Example of use:

```
&driver.SetImplicitWaitTimeout(30)
...
&driver.Start()
```

## [SetPageLoadTimeout](#SetPageLoadTimeout)

`[imagen omitida: wiki id 42505]`

Sets maximum wait time (in seconds) that GXtest will wait for the webpage to load. It must be used **before** the Start command.

Default value: 60s

Parameters:

* seconds: the number of seconds to wait for.

Example of use:

```
&driver.SetPageLoadWaitTimeout(10) 
...
&driver.Start()
```

## [SetExplicitWaitTimeout](#SetExplicitWaitTimeout)

`[imagen omitida: wiki id 41637]`

Sets maximum wait time (in seconds) for the elements used to be present/visible on the webpage when using [Waiter](https://wiki.genexus.com/commwiki/wiki?41633) functions.

Default value: 10s

Parameters:

* seconds: the number of seconds to wait for.

Example of use:

```
&driver.SetExplicitWaitTimeout(20)
```


|  |
| --- |
| **Backlinks** |
| [Table of contents:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Table of contents:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) | [GXtest UI Test for Web - Supported Commands](https://wiki.genexus.com/commwiki/wiki?40281) |

---
