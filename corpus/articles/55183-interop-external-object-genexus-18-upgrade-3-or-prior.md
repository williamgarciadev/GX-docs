---
title: "Interop external object (GeneXus 18 Upgrade 3 or prior)"
source_id: 55183
source_url: https://wiki.genexus.com/commwiki/wiki?55183
genexus_version: "18"
---

# Interop external object (GeneXus 18 Upgrade 3 or prior)

The Interop external object (which can be found in the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210) under the [Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288)) is used for interacting with the device using procedural programming.

|  |  |
| --- | --- |
|  |  |

## [Properties](#Properties)

### [ApplicationState property](#ApplicationState+property)

**Deprecated**: Use [AppLifecycle.ApplicationState](https://wiki.genexus.com/commwiki/wiki?42056) instead.

Indicates the current state of your application. Its values belong to the ApplicationState domain listed and described below:

|  |  |  |
| --- | --- | --- |
| **Key** | **Value** | **Description** |
| 0 | Active | The application is in the foreground or received events. |
| 1 | Inactive | The application is in the foreground but not receiving events. This can happen when an interruption occurs (eg., an incoming call) or while switching from background state. |
| 2 | Background | The application is not in the foreground. |

Knowing the state of the application can be useful in event management scenarios (such as push notifications or event location) and perform different actions depending on the status of implementation.

**Note:** On Android devices, Inactive state behavior does not exist. Therefore, in such devices, the property only acquires Active or Background values.

### ScreenBrightness property

Gets or sets the brightness of the device screen for Android and Apple generators.   
It allows you to assign a brightness value to the device. The range of values ​​is between 0.0 and 1.0.

```
&Brightness = Interop.ScreenBrightness
```

**Return value** Numeric(6.2)

**Notes**  
   -  In Android, the default value is -1. If this value is used, the brightness will return to the device's default.  
   - The brightness value will be modified as long as the screen is not changed. When the current screen is exited, it returns to the device's default brightness value.

#### [**Sample**](#Sample)

With this sample, you can learn how to capture the brightness value of a device and if the value is less than 0.5 you can change it.

```
Event 'SampleBrightness'
   Composite
          &BrightnessVar =  Interop.ScreenBrightness
          If &BrightnessVar < 0.5
                 Interop.ScreenBrightness = 0.5
          EndIf
   EndComposite
Endevent
```

## [Methods](#Methods)

### [SendMessage method](#SendMessage+method)

Sends a message to a contact without specifying the channel (it can be a phone number, an email address, a Facebook account, etc).  
Check [HowTo: Use SendMessage method from Interop external object](https://wiki.genexus.com/commwiki/wiki?15528).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | Message:[VarChar(200)](https://wiki.genexus.com/commwiki/wiki?6778), To:[Character(60)](https://wiki.genexus.com/commwiki/wiki?6777) |

### [PlayVideo method](#PlayVideo+method)

Plays a video from its URI (e.g. by '*http*', '*file*' or '*data*' schemes).  
Check [HowTo: Use PlayVideo method from Interop external object](https://wiki.genexus.com/commwiki/wiki?15986).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | Video:[URL](https://wiki.genexus.com/commwiki/wiki?15668) |

### [PlayAudio method](#PlayAudio+method)

Plays an audio from its URI (e.g. by '*http*', '*file*' or '*data*' schemes).  
Check [HowTo: Use PlayAudio method from Interop external object](https://wiki.genexus.com/commwiki/wiki?17339).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | Audio:[URL](https://wiki.genexus.com/commwiki/wiki?15668) |

### [PlaceCall method](#PlaceCall+method)

Opens the defined app for making calls with the input phone number.  
Check [HowTo: Use PlaceCall method from Interop external object](https://wiki.genexus.com/commwiki/wiki?17309).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | Phone:[Phone](https://wiki.genexus.com/commwiki/wiki?14639) |

### [SendEmail method](#SendEmail+method)

Sends a simple email through the native email client.  
Check [HowTo: Use SendEmail method from Interop external object](https://wiki.genexus.com/commwiki/wiki?17321).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | To:[Email](https://wiki.genexus.com/commwiki/wiki?14650), Subject:[VarChar(200)](https://wiki.genexus.com/commwiki/wiki?6778), Message:[VarChar(200)](https://wiki.genexus.com/commwiki/wiki?6778) |

### [SendEmailAdvanced method](#SendEmailAdvanced+method)

Sends a more complex email through the native email client to multiple targets.  
Check [HowTo: Use SendEmailAdvanced method from Interop external object in Native Mobile apps](https://wiki.genexus.com/commwiki/wiki?18193).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | To:Collection([Email](https://wiki.genexus.com/commwiki/wiki?14650)), CC:Collection([Email](https://wiki.genexus.com/commwiki/wiki?14650)), BCC:Collection([Email](https://wiki.genexus.com/commwiki/wiki?14650)), Subject:[VarChar(200)](https://wiki.genexus.com/commwiki/wiki?6778), Message:[VarChar(200)](https://wiki.genexus.com/commwiki/wiki?6778), Attachment:[BlobFile](https://wiki.genexus.com/commwiki/wiki?40420). |

### [SendSMS method](#SendSMS+method)

Sends an SMS (*Small Message System*) to a target phone number.  
Check [HowTo: Use SendSMS method from Interop external object](https://wiki.genexus.com/commwiki/wiki?17310).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | To:[Phone](https://wiki.genexus.com/commwiki/wiki?14639), Message:[VarChar(200)](https://wiki.genexus.com/commwiki/wiki?6778) |

### [Msg method](#Msg+method)

Displays a message to the end user.  
Check [HowTo: Use Msg method from Interop external object](https://wiki.genexus.com/commwiki/wiki?17328).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | Message:[VarChar(200)](https://wiki.genexus.com/commwiki/wiki?6778), OkButtonText:[VarChar(200))](https://wiki.genexus.com/commwiki/wiki?6778) |

Note: Parameter "OkButtonText" is optional and is only available from v16u9.

### [Confirm method](#Confirm+method)

Displays a message to the end user and returns True if it was confirmed or False otherwise. If the returned value has not been used, the event execution is canceled.  
Check [HowTo: Use Confirm method from Interop external object](https://wiki.genexus.com/commwiki/wiki?17334).

|  |  |
| --- | --- |
| **Return value** | [Boolean](https://wiki.genexus.com/commwiki/wiki?4374) |
| **Parameters** | Message:[VarChar(200)](https://wiki.genexus.com/commwiki/wiki?6778), OkButtonText:[VarChar(200))](https://wiki.genexus.com/commwiki/wiki?6778), CancelButtonText:[VarChar(200)](https://wiki.genexus.com/commwiki/wiki?6778) |

Note: Parameters "OkButtonText" and "CancelButtonText" are optional and are only available from [GeneXus 16 upgrade 9](https://wiki.genexus.com/commwiki/wiki?45275,,).

### [OpenInBrowser method](#OpenInBrowser+method)

Opens a URL in the default web browser of the device.  
Check [HowTo: Open a Web Page in a New Browser Window from a Smart Devices Application](https://wiki.genexus.com/commwiki/wiki?18555).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | Url:[URL](https://wiki.genexus.com/commwiki/wiki?15668) |

### [CanOpen method](#CanOpen+method)

Checks if a URL can be opened (True) or not (False).  
Check [Interop.CanOpen method](https://wiki.genexus.com/commwiki/wiki?23732).

|  |  |
| --- | --- |
| **Return value** | [Boolean](https://wiki.genexus.com/commwiki/wiki?4374) |
| **Parameters** | Url:[URL](https://wiki.genexus.com/commwiki/wiki?15668) |

### [Open method](#Open+method)

Opens a URI content using the appropriate application depending on its scheme.  
For instance, '*http*' scheme can open a [deep link](https://wiki.genexus.com/commwiki/wiki?36163) or web content in a browser, '*mailto*' will open the email client, '*maps*' will open the maps app, etc. Check [URI scheme](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier) definition and [Interop.Open method](https://wiki.genexus.com/commwiki/wiki?23733) article.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | Url:[URL](https://wiki.genexus.com/commwiki/wiki?15668) |

### [ClearCache method](#ClearCache+method)

Enables you to clear the cache on the device.  
Check [HowTo: Using ClearCache Method From Interop in Smart Devices Api](https://wiki.genexus.com/commwiki/wiki?22580).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | None |

### [SetBadgeNumber method](#SetBadgeNumber+method)

Sets a badge number on the application icon.  
Check [HowTo: Use Badge operations in Apple](https://wiki.genexus.com/commwiki/wiki?19356).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | number:[Numeric(8.0)](https://wiki.genexus.com/commwiki/wiki?6793) |

### [IOSSetBadgeTextToTabIndex method](#IOSSetBadgeTextToTabIndex+method)

Sets a badge text on a tab index when using a [Menu object with Control Type = Tabs](https://wiki.genexus.com/commwiki/wiki?16098).  
Check [HowTo: Use Badge operations in Apple](https://wiki.genexus.com/commwiki/wiki?19356).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | text:[Character(255)](https://wiki.genexus.com/commwiki/wiki?6777), tabIndex:[Numeric(8.0)](https://wiki.genexus.com/commwiki/wiki?6793) |

### [IOSSetSelectedTabIndex method](#IOSSetSelectedTabIndex+method)

Selects a tab by a code indicating its index when using a [Menu object with Control Type = Tabs](https://wiki.genexus.com/commwiki/wiki?16098).  
Check [HowTo: Use Badge operations in Apple](https://wiki.genexus.com/commwiki/wiki?19356).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | tabIndex:[Numeric(8.0)](https://wiki.genexus.com/commwiki/wiki?6793) |

### [IOSSetBadgeNumber method](#IOSSetBadgeNumber+method)

**Warning**: Deprecated since [GeneXus X Evolution 3 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?27678,,); use [SetBadgeNumber method](https://wiki.genexus.com/commwiki/wiki?23734) instead.

Check [HowTo: Use Badge operations in Apple](https://wiki.genexus.com/commwiki/wiki?19356).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | number:[Numeric(8.0)](https://wiki.genexus.com/commwiki/wiki?6793) |

### [ShowError method](#ShowError+method+)

Performs the equivalent of what is automatically done to display errors when a [Composite command](https://wiki.genexus.com/commwiki/wiki?17389) fails in a Native Mobile application.  
Check [HowTo: Using the ShowError method from Interop in Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?51446).

|  |  |
| --- | --- |
| **Return value** | number:[Numeric(3.0)](https://wiki.genexus.com/commwiki/wiki?6793) |
| **Parameters** | None |

## Events

It does not have any.

## [Domains](#Domains)

### [ApplicationState domain](#ApplicationState+domain)

List of possible application states.

|  |  |
| --- | --- |
| **Active** | The application is in the foreground or received events. |
| **Inactive** | The application is in the foreground but not receiving events. This can happen when an interruption occurs (for example, an incoming call) or while switching from the background state. |
| **Background** | The application is not in the foreground. |

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917) |
