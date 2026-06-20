---
title: "GXtest UI Commands - Waiters"
source_id: 41633
source_url: https://wiki.genexus.com/commwiki/wiki?41633
genexus_version: "18"
---

# GXtest UI Commands - Waiters

The following functions are intended to handle timing on test automation.

While it is not recommended to use PauseFor (sleep time) on tests, sometimes it could be handy in troubleshooting.

## [PauseFor](#PauseFor)

`[imagen omitida: wiki id 41639]`

Pauses (sleep) during test execution.

Parameters:

* seconds: the number of seconds to wait for.

Example of use:

```
&driver.PauseFor(3)
```

## [WaitByID](#WaitByID)

`[imagen omitida: wiki id 41640]`

Waits (explicitly) for a ceirtain HTML element to be present (or visible) on the webpage.

Parameters:

* ID: the HTML element ID to wait for.
* Visible: When true, it also checks for an element to be visible.

Example of use:

```
&driver.WaitById("button1", true)
```

## [WaitByLinkText](#WaitByLinkText)

`[imagen omitida: wiki id 41641]`

Waits (explicitly) for a link to be present (or visible) on the webpage.

Parameters:

* LinkText: the link text to wait for.
* Visible: When true, it also checks for an element to be visible.

Example of use:

```
&driver.WaitByLinkText("click here", true)
```

## [WaitByName](#WaitByName)

`[imagen omitida: wiki id 41642]`

Waits (explicitly) for a ceirtain HTML element to be present (or visible) on the webpage using the element Name.

Parameters:

* Name: the HTML element NAME to wait for.
* Visible: When true, it also checks for an element to be visible.

Example of use:

```
&driver.WaitByName("LinksContainer", true)
```

## [WaitByCSS](#WaitByCSS)

`[imagen omitida: wiki id 41643]`

Waits (explicitly) for a ceirtain HTML element to be present (or visible) on the webpage using the CSS selector.

Parameters:

* CSS: the CSS selector to the element that wants to wait for.
* Visible: When true, it also checks for an element to be visible.

Example of use:

```
&driver.WaitByCSS("#button1", true)
```

## [WaitByXPath](#WaitByXPath)

`[imagen omitida: wiki id 41644]`

Waits (explicitly) for a certain HTML element to be present (or visible) on the webpage using the XPath selector.

Parameters:

* XPath: the XPath selector to the element that wants to wait for.
* Visible: When true, it also checks for an element to be visible.

Example of use:

```
&driver.WaitByXPath("//span/input", true)
```


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) | [GXtest UI Commands - Timeouts](https://wiki.genexus.com/commwiki/wiki?41632) |
| [GXtest UI Test for Web - Supported Commands](https://wiki.genexus.com/commwiki/wiki?40281) |

---
