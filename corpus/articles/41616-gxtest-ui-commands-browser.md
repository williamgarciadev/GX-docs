---
title: "GXtest UI Commands - Browser"
source_id: 41616
source_url: https://wiki.genexus.com/commwiki/wiki?41616
genexus_version: "18"
---

# GXtest UI Commands - Browser

## [GetSource](#GetSource)

`[imagen omitida: wiki id 41620]`

Gets the source HTML code of the current webpage.

Returns: The webpage source-code as a string

Example of use:

```
&wp_source = &driver.GetSource()
```

## [GetTitle](#GetTitle)

`[imagen omitida: wiki id 41621]`

Gets the current webpage title.

Returns: The webpage title as a string

Example of use:

```
&wp_title = &driver.GetTitle()
// Validate current page is the expected
AssertStringEquals("MySite | Home", &driver.GetTitle(), "Current page is Home")
```

## [Maximize](#Maximize)

`[imagen omitida: wiki id 41622]`

Maximizes the browser window.

Example of use:

```
&driver.Maximize()
```

## [SetWindowSize](#SetWindowSize)

`[imagen omitida: wiki id 46661]`

Sets the browser's exact window size.

Parameters:

* Width: window width in pixels
* Height: window height in pixels

Example of use:

```
&driver.SetWindowSize(720, 480)
```

## [Go](#Go)

`[imagen omitida: wiki id 48469]`

Navigates to the given URL.

Parameters:

* url: target URL to navigate to, it can be full or partial. In case it is partial it will be combined with the [Base URL property](https://wiki.genexus.com/commwiki/wiki?45420).

Example of use:

```
&driver.Go(WebPanelX.Link())

&driver.Go("https://abstracta.us/why-us/company")
```

## [SetBaseURL](#SetBaseURL)

`[imagen omitida: wiki id 48470]`

Sets a base URL to be used when relative paths are given to Go commands. This is automatically set if you have configured [the BaseURL property](https://wiki.genexus.com/commwiki/wiki?45420) on your environment.

Parameters:

* url: the base URL to be set. It will be combined with the url parameter of Go commands.

Example of use:

```
&driver.SetBaseURL("https://serverName/applicationName/")
```

## [Refresh](#Refresh)

`[imagen omitida: wiki id 41623]`

Refreshes (reloads) the browser webpage.

Example of use:

```
&driver.Refresh()
```

## [GoBack](#GoBack)

`[imagen omitida: wiki id 46662]`

Goes to the previous page

Example of use:

```
&driver.GoBack()
```

## [GoForward](#GoForward)

`[imagen omitida: wiki id 46663]`

Goes to the next page. Note that it is required to perform a GoBack command in order for this command could be used.

Example of use:

```
&driver.GoForward()
```

## [ScriptEval](#ScriptEval)

`[imagen omitida: wiki id 41624]`

Runs JavaScript code.

Parameters:

* Script: a string containing the JavaScript code to run.

Returns:

* Script's returned value.

Example of use:

```
//Change Title to "New Title" using Javascript
&driver.ScriptEval("document.title = 'New Title';")

// Get last status code
&statusCode = &driver.ScriptEval("return window.gx.http.lastStatus")
```

Notes: JS functions are intended for some specific automation that (for some reason) is it not possible to achieve using traditional UI commands, so this is intended to be used only by experienced users.


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Example to not overwrite the screenshots](https://wiki.genexus.com/commwiki/wiki?47209) |
| [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) | [GXtest UI Commands - Assertions](https://wiki.genexus.com/commwiki/wiki?41682) | [GXtest UI Commands - Custom Commands](https://wiki.genexus.com/commwiki/wiki?47402) | [GXtest UI Commands - Property Setters](https://wiki.genexus.com/commwiki/wiki?48468) |
| [GXtest UI Test for Web - Supported Commands](https://wiki.genexus.com/commwiki/wiki?40281) |

---
