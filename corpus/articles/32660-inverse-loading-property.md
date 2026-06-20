---
title: "Inverse Loading property"
source_id: 32660
source_url: https://wiki.genexus.com/commwiki/wiki?32660
genexus_version: "18"
---

# Inverse Loading property

Allows reversing the direction of data loading in a Grid within web objects.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Objects:** [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Work With](https://wiki.genexus.com/commwiki/wiki?15974)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Angular](https://wiki.genexus.com/commwiki/wiki?42550), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817)

### [Description](#Description)

Default value: *False*

When you set the value "True", it loads the grid data from bottom to top (in a common grid) and from right to left (in a horizontal grid).

Chat messaging systems are a relevant use case of Inverse loading. Its distinguishing features include:

* Bottom-to-Top Loading Order: messages are loaded in reverse direction; that is, from bottom to top in the conversation. The most recent messages are displayed at the bottom of the screen, which allows for quick viewing of the latest interactions.
* Swipe Down Pagination: Pagination is performed with a swipe down gesture, providing a smoother and uninterrupted user experience.
* Show First Page in Bottom Section on Refresh: When the end user refreshes the conversation, the first page is displayed in the bottom section. This ensures that new messages appear in the end user's field of view, allowing them to keep up with the conversation without the need to manually scroll up to see the most recent messages.

### [How to use](#How+to+use)

To create a simple chat user interface with GeneXus, follow the three steps below:

1. Drag a [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) from the [GeneXus IDE Toolbox](https://wiki.genexus.com/commwiki/wiki?10000) to the abstract layout (with the appropriate attributes/variables for your business logic).
2. Drag a string variable to the bottom section of the layout. The purpose of this variable is to allow the end user to type new text and send it.
3. On the right side of the text field, insert a button to send the messages.  
     
   The most important action to achieve this design is to set the Inverse Loading property at the grid level to *True*. Lastly, the final result looks as shown below:  
     
   `[imagen omitida: wiki id 32665]`

You can customize the appearance of the controls (sizes, positions, and colors) and, finally, achieve a user interface similar to the one shown below:

`[imagen omitida: wiki id 32666]`

### [Notes:](#Notes%3A)

* In the Smart Devices generator, the following table describes the conditions that the grid must satisfy in order to achieve the inverse loading effect.

  |  |  |  |
  | --- | --- | --- |
  |  | **Android** | **iOS** |
  | [Pull To Refresh property](https://wiki.genexus.com/commwiki/wiki?29993,,) | Disable | Disable |
  | [Search](https://wiki.genexus.com/commwiki/wiki?24805) | No | No |
  | [Break by](https://wiki.genexus.com/commwiki/wiki?24805)(\*) | No | No |

See [SAC# 50169.](https://www.genexus.com/en/developers/websac?data=50169;;)

* When there are not enough grid items to fill the screen, the*starting position* of the loaded items is different in Android and iOS, to match the most common usage on each platform:
  + In Android, grid items are shown at the bottom of the screen with empty spaces above them (like *Hangouts*, *Allo*, *Messenger,*or *Telegram*on Android);
  + In iOS, grid items are shown at the top of the screen with empty spaces below them (like *iMessage*, *WhatsApp,*or *Facebook Messenger*on iOS).
* In web environments, for the Inverse Loading property to appear the grid must have infinite scrolling.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build any object.


|  |
| --- |
| **Backlinks** |
| [AudioRecorder external object](https://wiki.genexus.com/commwiki/wiki?34096) |
|

---
