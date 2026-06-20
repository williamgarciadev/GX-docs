---
title: "UITestSD external object"
source_id: 44873
source_url: https://wiki.genexus.com/commwiki/wiki?44873
genexus_version: "18"
---

# UITestSD external object

The **UITestSD external object** allows for the development of User Interface (U.I.) automated tests such as, for example, of [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)s.

`[imagen omitida: wiki id 44874]`

This external object is loaded in your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) when you create the first [UI Test object](https://wiki.genexus.com/commwiki/wiki?46009).

## [Properties](#Properties)

None

## [Methods](#Methods)

### [Parameters received by most methods](#Parameters+received+by+most+methods)

Several of the methods described below (and used in [UI Test object](https://wiki.genexus.com/commwiki/wiki?46009)s) receive parameters to indicate a **text on a screen,** a **control name,** or other details. Below are general aspects of the parameters received by most of the methods.

#### [**controlName**](#controlName)

It's the name of a control (as shown in the Control Name property) in the GeneXus object where it is defined.  
**Examples:** "&numeric" (for a variable), "CustomerName" (for an attribute), "Save" (for a button).  
**Note:** The casing is not important because GeneXus ignores it.

#### [**context**](#context)

It allows indicating the container in which the control is located.  
In some cases, it is necessary to disambiguate the name of the control. For example, if there is a Component on the screen, there may be two controls with the same control name.

For example, if you want to tap on a button called "Button1" located in the second row of the "Grid1" grid, you must write:

```
&app.Tap("Button1", "Grid1.item(2)")   //&app is a variable based on the UITestSD external object
```

**Notes:**  
- The **context** defines a route where controls should be found, though it is not necessary for the route to be complete. For example, in the above case, the "button1" button could also be inside a "Grid1Table" table, which will not have to be indicated.  
- For controls representing collections (Grid, Horizontal Grid, Tab Control, etc.), the "item" allows indicating an element within the collection.  
- **Predefined contexts:**In many cases, the context depends on the names of the controls –for example, "Grid1"– but there are also cases in which the context may be predefined. This happens with the controls in the Application Bar. To this end, an [Enumerated Domain](https://wiki.genexus.com/commwiki/wiki?2207) called **UITestingContext** is defined.

##### [**UITestingContext Enumerated Domain features**](#UITestingContext+Enumerated+Domain+features)

- It is based on the same data type as the **context** in the method parameters, i.e. VarChar(40).  
- It has only one value: ApplicationBar (value: "applicationbar") that represents the context of the Application Bar. When this **context** is indicated, only elements found there will be searched.

- If the ApplicationBar context is indicated, in addition to searching for the elements that are visible there, the elements that were placed in the Application Bar at design time should also be searched. Because there is not enough space, they were grouped by the flexible client and it is necessary to press an additional button to find them.

#### **target**

"Target" or "Action Target" refers to an action that may be done on:

* A **controlName**, or
* Any **Text shown on the screen.**

**Notes:**  
- When searching for elements on the screen, the search is done first by controlName and if none is found, then the search is done by text.  
- If there is more than one control fulfilling the conditions, then you use the first one found (non-deterministic).

#### **expected**

This boolean parameter indicates if you expect a text on the screen:

* If you indicate True, you are expecting the text on the screen. If it isn't on the screen the test fails.
* On the other hand, if you indicate False, the test will fail if the text is on the screen.

## [Methods for Actions](#Methods+for+Actions)

### [Back](#Back)

Simulates the action of the *back* button in the device in the case of Android, and it is a *tap* on the button for that purpose in the case of iOS.

```
Back()
```


### [Tap](#Tap)

It performs a *tap* on a given point on the screen (<target>).

```
Tap(<target> [, <context>])
```

View [Parameters received by most of the methods](https://wiki.genexus.com/commwiki/wiki?44873)

---

### [LongTap](#LongTap)

It performs a *long tap* on a given point on the screen (<target>).

```
LongTap(<target> [, <context>])
```

View [Parameters received by most of the methods](https://wiki.genexus.com/commwiki/wiki?44873)

---

### [DoubleTap](#DoubleTap)

It performs a *double tap* on a given point on the screen (<target>).

```
DoubleTap(<target> [, <context>])
```

View [Parameters received by most of the methods](https://wiki.genexus.com/commwiki/wiki?44873)

---

### [TapSystemAlertIfShown](#TapSystemAlertIfShown)

When you run an application on a device, you might see non-application dialogs during execution; they are system dialogs. These dialogs are displayed by the system, for example, so that the user can grant or deny certain permissions. With this method, you can control those actions in the [UI Test object](https://wiki.genexus.com/commwiki/wiki?46009).

```
TapSystemAlertIfShown(<button> [, <alertType>])
```

where

* <button> - Indicates the button on which to tap in case the dialog is displayed. It is based on the **SystemAlertButton** [Enumerated Domain](https://wiki.genexus.com/commwiki/wiki?2207) that defines which button the TapSystemAlertIfShown function should tap on.
* <alertType> - Indicates the type of alert to interact with. This parameter is optional. If you are not prompted for the type of alert, then any system dialog that is presented is considered.

Possible values offered by the **SystemAlertButton** Enumerated Domain:

* DoNotAllow
* Ok
* AllowOnce
* AllowWhenInUse
* AllowAlways

**SystemAlertType** is the enumerated domain that indicates the different types of dialog that the TapSystemAlertIfShown method can handle. The possible values are as follows:

* Bluetooth
* Calendar
* Camera
* Contacts
* Location
* Microphone
* Photos
* Storage
* Any

**Sample**

```
//&app is a variable based on the UITestSD external object

&app.Tap("GetLocation")           
&app.TapSystemAlertIfShown(SystemAlertButton.AllowOnce,SystemAlertType.Location)
&app.Wait(3000)
&app.verifyMsg("Done")
&app.Tap("OK")
```

---

### [Fill](#Fill)

It enters a value in a given control of the Edit type.

```
fill(<controlName>, <value> [, <context>])
```

View [Parameters received by most of the methods](https://wiki.genexus.com/commwiki/wiki?44873)

---

### [PickDate](#PickDate)

It enters a value in a field of the Date type using the corresponding *picker*.

```
pickDate(<controlName>, <year>, <month>, <day>, [, <context>])
```

View [Parameters received by most of the methods](https://wiki.genexus.com/commwiki/wiki?44873)

---

### [PickDateTime](#PickDateTime)

It enters a value in a field of the DateTime type using the corresponding *picker*.

```
pickDateTime(<controlName>, <year>, <month>, <day>, <hour>, <minutes>, [, <context>])
```

View [Parameters received by most of the methods](https://wiki.genexus.com/commwiki/wiki?44873)

---

### [PickTime](#PickTime)

It enters a value in a field of the Time type (a.k.a. DateTime without the Date part) using the corresponding *picker*.

```
pickTime(<controlName>, <hour>, <minutes>, [, <context>])
```

View [Parameters received by most of the methods](https://wiki.genexus.com/commwiki/wiki?44873)

---

### [SelectValue](#SelectValue)

It enables the selection of a value from a list of values of a Combo Box or Radio Button, given by its Control Name. The value to be selected is indicated in the "value" parameter.

```
selectValue(<controlName>, <value> [, <context>])
```

View [Parameters received by most of the methods](https://wiki.genexus.com/commwiki/wiki?44873)

---

### [Swipe](#Swipe)

It performs a *swipe* over the screen in the direction indicated by the parameter. The starting point of the *swipe* depends on the parameter. There is also the option to indicate the control where it should start. In the absence of an indication, the *swipe* will start at a fixed point on the screen (the fixed point will depend on the direction).

```
Swipe(<direction> [, <controlName>] [, <context>])
```

where <direction> may be "Up", "Down", "Left", or "Right".

* Up - does a *swipe* upwards from the center of the lower margin on the device (some pixels above the border) or from the control if it is indicated.
* Down - does a *swipe* downwards from the center of the upper margin on the device (some pixels under the border) or from the control if it is indicated.
* Left - does a *swipe* to the left from the center of the right margin on the device (some pixels to the left of the border) or from the control if it is indicated.
* Right - does a *swipe* to the right from the center of the left margin on the device (some pixels to the right of the border) or from the control if it is indicated.

View [Parameters received by most of the methods](https://wiki.genexus.com/commwiki/wiki?44873)

**Note:** In iOS, it is not possible to indicate from which position the *swipe* should start. It is always done (apparently) from the center of the control.

---

### [Wait](#Wait)

Waits for a given number of milliseconds.

```
wait(<milliseconds>)
```

## [Methods for Verifications](#Methods+for+Verifications)

Verifications will cause the test case to fail in case of non-compliance. When conditions are fulfilled, they do not cause the test to fail.

### [VerifyText](#VerifyText)

Verifies whether a text is on screen, anywhere, unless a *context* has been indicated.

```
verifyText(<string> [, <expected>] [, <context>])
```

View [Parameters received by most of the methods](https://wiki.genexus.com/commwiki/wiki?44873)

---

### [VerifyGridRowsCount](#VerifyGridRowsCount)

Verifies whether the number of rows on a grid equals the given value.

```
verifyGridRowsCount(<grid control name>, <value> [, <expected>] [, <context>])
```

View [Parameters received by most of the methods](https://wiki.genexus.com/commwiki/wiki?44873)

---

### [VerifyCheckbox](#VerifyCheckbox)

Verifies whether a control of the checkbox type has been checked or not, according to the (Boolean) "value" indicated.

```
verifyCheckbox(<controlName>, <value> [, <expected>] [, <context>])
```

View [Parameters received by most of the methods](https://wiki.genexus.com/commwiki/wiki?44873)

---

### [verifyControlValue](#verifyControlValue)

Verifies whether a control has the value indicated or not.

```
verifyControlValue(<controlName>, <value> [, <expected>] [, <context>])
```

View [Parameters received by most of the methods](https://wiki.genexus.com/commwiki/wiki?44873)

---

### [verifyControlEnabled](#verifyControlEnabled)

Verifies whether a control is enabled to edit or not (read-only).

```
verifyControlEnabled(<controlName> [, <expected>] [, <context>])
```

In iOS, this verification is always successful. In theory, in the API of Xcode you have an **isEnabled** property, but in the cases tested, it returns **true** every time.

View [Parameters received by most of the methods](https://wiki.genexus.com/commwiki/wiki?44873)

---

### [verifyMsg](#verifyMsg)

Verifies whether an alert with a specific message sent with the **msg** command of GeneXus is presented.

This verification must be done both in the title and in the text of the alert.

```
verifyMsg(<string> [, <expected>])
```

View [Parameters received by most of the methods](https://wiki.genexus.com/commwiki/wiki?44873)

---

### [verifyControlVisible](#verifyControlVisible)

Verifies whether the control is visible on the screen or not.

```
verifyControlVisible(<controlName> [, <expected>] [, <context>])
```

View [Parameters received by most of the methods](https://wiki.genexus.com/commwiki/wiki?44873)

---

### [verifyScreenshot](#verifyScreenshot)

Takes a screenshot of a control or the entire screen and compares it to a reference image. If the comparison fails, the test fails.

```
verifyScreenshot(<reference> [, <controlName> [, <context>]])
```

View [Parameters received by most of the methods](https://wiki.genexus.com/commwiki/wiki?44873)

The reference parameter is of string type and identifies the reference image within the current test.

**Note:** Using this function requires some additional setup. You can find more information in [Visual testing in Native Mobile applications](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49568,,).

The verifyScreenshot method is available as of [GeneXus 17 upgrade 7](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49301,,).

---

### [IsControlEnabled](#IsControlEnabled)

Similar to [VerifyControlEnabled](https://wiki.genexus.com/commwiki/wiki?44873) but returns a boolean instead of failing the test.

If the control is not found, the command fails with an assert.

```
IsControlEnabled(<controlName> [, <context>]): Boolean
```

View [Parameters received by most of the methods](https://wiki.genexus.com/commwiki/wiki?44873)

---

### [IsControlVisible](#IsControlVisible)

Similar to [VerifyControlVisible](https://wiki.genexus.com/commwiki/wiki?44873) but returns a boolean instead of failing the test.

If the control is not found, the function returns False.

```
IsControlVisible(<controlName> [, <context>]): Boolean
```

View [Parameters received by most of the methods](https://wiki.genexus.com/commwiki/wiki?44873)

---

### [IsShowingMessage](#IsShowingMessage)

Returns True if an alert is being displayed on the screen.

**Note:** It does not take into account system alerts, for example, if it is asking for permission to receive notifications. 

```
IsShowingMessage(): Boolean
```

---

### [GetControlValue](#GetControlValue)

Gets the value of the control and returns a string.

If the control is not found, the command fails with an assert.

```
GetControlValue(<controlName> [, <context>]): VarChar
```

View [Parameters received by most of the methods](https://wiki.genexus.com/commwiki/wiki?44873)

---

### [GetCheckboxValue](#GetCheckboxValue)

Similar to [VerifyCheckbox](https://wiki.genexus.com/commwiki/wiki?44873), returns a boolean with the value of the checkbox.

If the control is not found, the command fails with an assert.

```
GetCheckboxValue(<controlName> [, <context>]): Boolean
```

View [Parameters received by most of the methods](https://wiki.genexus.com/commwiki/wiki?44873)

---

### [GetGridRowsCount](#GetGridRowsCount)

Similar to [VerifyGridRowsCount](https://wiki.genexus.com/commwiki/wiki?44873), returns an integer with the number of rows in the Grid.

If the Grid is not found, the test fails with an assert.

```
GetGridRowsCount(<controlName> [, <context>]): Numeric(8)
```

View [Parameters received by most of the methods](https://wiki.genexus.com/commwiki/wiki?44873)

---

### [GetMessageText](#GetMessageText)

If there is an alert on the screen, it gets the text of the alert. Similar to [VerifyMsg](https://wiki.genexus.com/commwiki/wiki?44873).

If the alert is not found, the command fails with an assert.

```
GetMessageText(): VarChar
```

---

### [VerifyCondition](#VerifyCondition)

Receives a boolean and optionally a message, if the boolean is False then it fails the test and uses the message as the reason for the failure.

```
VerifyCondition(<boolean value> [, <message>])
```

**Note:**  
Starting from iOS 17, performing a Swipe Right anywhere on the screen (not only from the left edge) triggers the system Back navigation by default.  
When running UI Tests that use SwipeRight() on controls without slide actions (e.g., TextBlock, Table), the test may unintentionally navigate back.  
To avoid this during testing, add an empty Back event in the Panel to override the system behavior:

```
Event Back 

```
EndEvent
```
```

---

---

|  |
| --- |
| **Backlinks** |
| [UI Test for Native Mobile Automation](https://wiki.genexus.com/commwiki/wiki?44571) | [UITestSD external object](https://wiki.genexus.com/commwiki/wiki?44873) |
| [Visual Testing Repository URL property](https://wiki.genexus.com/commwiki/wiki?49551) | [KB:VisualTestingStore](https://wiki.genexus.com/commwiki/wiki?49571) |

---
