---
title: "Smart Devices Semantic Domains"
source_id: 18242
source_url: https://wiki.genexus.com/commwiki/wiki?18242
genexus_version: "18"
---

# Smart Devices Semantic Domains

Semantic Domanis are one of the ways, provided by GeneXus, to enable the applications running on our devices to interact closely with our device's resources. Using them is as easy as setting a variable or attribute based on a certain domain or data type, and by doing this our variable or attribute will start behaving according to the domain selected. When we refer to behavior there are three major things you can notice:

1. The way you enter the information of the att/var depending on the device limitations.

2. The way the var or att behaves in view mode.

3. The behavior of in-screen-keyboards.

Let's see how they will behave and look at the different domains depending on the device and mode (view/edit).

### [Numeric](#Numeric)

Numeric is one of the default data types supported by GeneXus; it can handle numeric with and without floating point.

Smart Devices behavior:

To help the user enter numeric data the in-screen-keyboard adapts itself to the numeric keyboard automatically.

|  |  |
| --- | --- |
|  |  |

(Iphone)

### [Character](#Character)

Also a default data type which can store and handle different characters

Smart Device behavior:

The in-screen keyboard will be the default text keyboard

|  |  |
| --- | --- |
|  |  |

(iphone)

### [Email](#Email)

The atts/vars based on this domain can handle an email address.

Smart Devices behavior:

Edit mode:

The input keyboard will adapt to the email needs:

|  |
| --- |
|  |

Also, when trying to save a wrongly formatted e-mail address a message will be displayed and the operation will be canceled.

|  |  |
| --- | --- |
|  |  |

View:

In view mode with just one tap over the email address (iOS) or the envelope icon of the email att/var (Android, BB) the email client will be automatically invoked with this email address in the To field.

|  |  |
| --- | --- |
|  |  |

### [Phone](#Phone)

Atts/vars based on this domain can store and handle phone numbers.

Smart Device behavior:

Edit mode:

The in-screen-keyboard will adapt to the default phone input keyboard.

|  |  |
| --- | --- |
|  |  |

View mode:

If there is a field based on this domain by tapping on the number (iOS) or the phone icon (Android, BB) a call o SMS text will be prompted to the number stored on the att/var.

|  |  |
| --- | --- |
|  |  |

### [URL](#URL)

A web URL can be stored or handled in atts/vars based on this domain.

Smart Device behavior:

Edit mode:

The format and syntax of the URL will be checked to validate the URL the user just inserted. Also the keyboard will adapt in the case of email input.

View mode:

Tapping on the URL (iOS) or the symbol icon (Android, BlackBerry) will open the page of that URL in the default web browser of the device.

|  |  |
| --- | --- |
|  |  |

### [Component](#Component)

A domain that can also handle and store web page URLs, but this domain will load the page and show it on the smart device inside the application.

Smart Device behavior:

It will show a Webview, that is, the web page of the URL specified on the field based on this domain. The web page will occupy the space given for the variable.

(Component)

`[imagen omitida: wiki id 18335]`

### [HTML](#HTML)

An att/var based on this domain can store HTML code.

Smart device behavior:

View Mode:

The HTML code stored in this field will be rendered by the device.

`[imagen omitida: wiki id 18336]`

More information at [Component domain](https://wiki.genexus.com/commwiki/wiki?16186).

### [Image](#Image)

The first of three multimedia domains. This domain can store and manipulate any image inserted via server side or smart device.

Smart Device behavior:

Edit mode:

If the user wants to insert a var or att based on the image semantic domain, and he is using a device with a camera, an option similar to the one shown below will be displayed.

|  |  |
| --- | --- |
|  |  |

If the device doesn't have a built-in camera, only the Choose from library option will be available.

### [Video](#Video)

Like the image domain this multimedia domain can handle and store video sequences.

Smart device behavior:

Edit mode:

A message will be displayed for the user when trying to insert an att/var based on this domain. Also the application will know the limitations of the device it is on. If there is no camera the Record Video option will not be shown.

|  |  |
| --- | --- |
|  |  |

Choosing a video will upload it:

|  |
| --- |
|  |

View Mode:

The default platform player will be displayed:

`[imagen omitida: wiki id 18346]`

### [Audio](#Audio)

The last multimedia domain can store audio content.

Smart Device behavior:

Edit mode:

In iOS a screen like the one shown below will be desplayed to start recording. On Android and BlackBerry you can record now or choose an audio file on your device.

|  |  |
| --- | --- |
|  |  |

### [Date, Time, Date Time:](#Date%2C+Time%2C+Date+Time%3A)

These domains are familiar to GeneXus developers for win and web applications, so their default and expected behavior should be known.

Smart Device behavior:

Edit mode:

The most relevant behavior of these domains is that when inserting this field the platform default date picker will be invoked. This is a way to help the user insert dates on smart devices:

|  |  |
| --- | --- |
|  |  |

Time example:

`[imagen omitida: wiki id 18337]`

### [Geolocation](#Geolocation)

Atts/Vars based on this domain can handle specific latitude-longitude coordinates.

Smart Device behavior:

Edit mode:

Coordinates can be entered with the default numeric keyboard or selected from a map, just by tapping over the icon next to the Geolocation field.

|  |
| --- |
|  |

View mode:

A Geoloaction value can be shown over the map just by tapping over the coordinates (iOS) or the pin icon (Android, BlackBerry).

|  |
| --- |
|  |

### [Address](#Address)

This domain's behavior is similar to the Geolocation domain.

Smart Device behavior:

Edit mode:

When inserting an address-based att/var it will behave as an ordinary character-based field.

View mode:

When viewing it, by tapping over the text (iOS) or icon (Android, BlackBerry) the map will be invoked to show the specified address.

|  |  |
| --- | --- |
|  |  |


|  |
| --- |
| **Backlinks** |
| [Allow Webview execute javascript property](https://wiki.genexus.com/commwiki/wiki?37299) | [Allow Webview execute local files property](https://wiki.genexus.com/commwiki/wiki?37300) | [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268) |

---
