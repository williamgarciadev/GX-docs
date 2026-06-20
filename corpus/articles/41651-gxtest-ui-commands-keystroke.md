---
title: "GXtest UI Commands - Keystroke"
source_id: 41651
source_url: https://wiki.genexus.com/commwiki/wiki?41651
genexus_version: "18"
---

# GXtest UI Commands - Keystroke

Keystroke commands are used to send single Keys to some UI control, typically to force running some JS events on the webpage after pressing a special key.

See the [list of special characters to use](https://wiki.genexus.com/commwiki/wiki?41678).

**Note:**  
While sending a key {Tab} is a common practice for some automated tests we recommend to use it only when there is no other alternative (like clicking or typing somewhere else to lost focus, etc), since browser implementation of this could lead to flaky results. Also, while this function enables us to send characters to the UI, it is not intended to be used for typing. For typing over text fields use [type commands](https://wiki.genexus.com/commwiki/wiki?41649) instead.

## [SendKeys](#SendKeys)

This command allows you to send keys to the browser and controls.

There are 3 implementations of this command:

Sends keys to a specific control  
`[imagen omitida: wiki id 46799]`

Sends keys to a specific control inside a grid

`[imagen omitida: wiki id 47318]`

Sends keys to the currently focused element or the page itself if there is none.  
`[imagen omitida: wiki id 46800]`

**Parameters:**

* ControlName: name of the control to send the Keys
* Row: row number to locate the element to send the keys to.
* Keys: keys to send. It's recommended to use the "Keys" domain to send special keys like *ENTER, TAB, ESC*, etc.. They can be combined using the character | as keys separator.

Can be used to confirm a form (Keys.Enter), to move over combo box options (Keys.DOWN and Keys.UP), navigate web elements (Keys.TAB), etc.

**Examples:**

```
&driver.SendKeys("optionsCtrl", Keys.DOWN)

&driver.SendKeys(Keys.Enter) 

&driver.SendKeys("someControl", 1, Keys.Enter)

&driver.SendKeys(Keys.CONTROL + "|a") // This will send the command Ctrl + A to the currently focused element or the whole webpage if none is focused

&driver.SendKeys(Keys.TAB)
```

## [KeysByID](#KeysByID)

`[imagen omitida: wiki id 41674]`

Sends keys using the ID attribute.

Parameters:

* ID: the HTML element ID to send the key.
* Text: Character(s) to send.

Example of use:

```
&driver.KeysByID("vSUG1", "{BACKSPACE}")
```

## [KeysByName](#KeysByName)

`[imagen omitida: wiki id 41675]`

Sends keys using the 'name' attribute.

Parameters:

* Name: the name attribute of the element to send the key.
* Text: Character(s) to send.

Example of use:

```
&driver.KeysByName("vSUG1", "{TAB}")
```

## [KeysByCSS](#KeysByCSS)

`[imagen omitida: wiki id 41676]`

Sends keys using a CSS selector.

Parameters:

* CSS: the CSS locator of the element to send the key.
* Text: Character(s) to send.

Example of use:

```
&driver.KeysByCss("#vSUG1", "u")
```

## [KeysByXPath](#KeysByXPath)

`[imagen omitida: wiki id 41677]`

Sends keys using an XPath selector.

Parameters:

* XPath: the XPath of the element to send the key.
* Text: Character(s) to send.

Example of use:

```
&driver.KeysByXpath("//input[@id='vSUG2']", "{RETURN}")
```


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) | [GXtest UI Test for Web - Supported Commands](https://wiki.genexus.com/commwiki/wiki?40281) |

---
