---
title: "WebExtension Toolkit"
source_id: 37807
source_url: https://wiki.genexus.com/commwiki/wiki?37807
genexus_version: "18"
---

# WebExtension Toolkit

**WebExtension Toolkit** is a set of [External Objects](https://wiki.genexus.com/commwiki/wiki?5669) to solve typical problems in Web Applications.

It can be used by installing the **WebExtension Toolkit**module available in the Global Matrix when selecting the **Knowledge Manager > Manage** **Module References** option.

For example, you can do the following:

* Geolocation: Get user location
* Close Popups programmatically
* Open a new window/browser tab
* Manage the address bar of the browser (change, back, forward, etc.)
* Execute JS code
* Send error messages and warnings to the browser console
* Subscribe to events of:
  + Popup closure
  + On Ready of web apps
  + onUnLoad (when closing a web page)
* Display native Web dialogs for:
  + Confirmation
  + Alerts
* Display UI Browser Alerts
* Use of WebSocket API (management of the WebSocket low-level API)
* Timer:
  + Fire User Events after elapsed time.

## [**Samples**](#Samples)

### [**Sample 1: Open in new Window**](#Sample+1%3A+Open+in+new+Window)

```
Event 'OpenNewWindow'
    if (&UseAdvancedOptions)
        Extensions.Web.Window.OpenNewWindow(&Url, "",&WindowOptions)
    else if (&OpenMultipleWindows)
        Extensions.Web.Window.OpenNewWindow(&Url,  'myNewWindow-1')
        Extensions.Web.Window.OpenNewWindow(&Url2, 'myNewWindow-2')
    else
        Extensions.Web.Window.OpenNewWindow(&Url)
    endif
Endevent

Event 'Close Window'
    Extensions.Web.Window.Close('')
EndEvent

Event Extensions.Web.Window.OnClose(&windowName)
    msg(&windowName + "has beed closed!")
EndEvent
```

**WindowOptions:**

`[imagen omitida: wiki id 37808]`

**Note:** To open in a new Tab, use the method with only the URL parameter as follows:

```
Extensions.Web.Window.OpenNewWindow(&Url)
```

### [**Sample 2: Close Popup programmatically**](#Sample+2%3A+Close+Popup+programmatically)

```
Event Enter
    Popup1.Popup()
Endevent

Event 'Close'
    Extensions.Web.Popup.Close()
Endevent

Event Extensions.Web.Popup.OnPopupClosed(&PopupName)
    msg("popup has been closed: " + &PopupName)        
EndEvent
```

### [**Sample 3: Run JS code, show alert, and confirm dialogs**](#Sample+3%3A+Run+JS+code%2C+show+alert%2C+and+confirm+dialogs)

```
Event 'RunJS'
    Extensions.Web.WebInterop.RunJS(!"console.log('hello world');alert('hello world');")
Endevent

Event 'LogError'
    Extensions.Web.WebInterop.LogError(&logMessage)
Endevent

Event Extensions.Web.WebInterop.OnReady()
    msg("Onready!")
EndEvent

Event Extensions.Web.WebInterop.OnUnload()
    Extensions.Web.WebInterop.LogError(!"Exiting Page!")
EndEvent
```

**Note for OnUnload Event:**

* The HTML specification states that calls to window.alert(), window.confirm(), and window.prompt() methods may be ignored during this event. See the HTML specification for more details.

https://developer.mozilla.org/en-US/docs/Web/API/Window/beforeunload\_event

### [**Sample 3.1: Alert Dialog**](#Sample+3.1%3A+Alert+Dialog)

`[imagen omitida: wiki id 42102]`

```
Event 'ShowAlert'
    Extensions.Web.Dialog.Alert(&logMessage) //&LogMessage: Message that will be display within Alert Dialog
Endevent
```

### [**Sample 3.2: Confirm Dialog**](#Sample+3.2%3A+Confirm+Dialog)

`[imagen omitida: wiki id 42104]`

```
Event 'ShowConfirm'
    Extensions.Web.Dialog.Confirm(&logMessage) //&LogMessage: Message that will be display within Confirm Dialog
Endevent

Event Extensions.Web.Dialog.OnConfirmClosed(&UserResponse)   //&UserResponse: MUST be a Boolean Variable. 
    Extensions.Web.Dialog.Alert("User Confirm Response: " + &UserResponse.ToString())
EndEvent
```

### [**Sample 4: Get User Geolocation**](#Sample+4%3A+Get+User+Geolocation)

```
Event 'GetMyLocation'
    Extensions.Web.Geolocation.requestLocation()
Endevent

Event Extensions.Web.Geolocation.OnError(&ErrCode, &errMessage)    
    msg("Geolocation Error: " + &errMessage)    
EndEvent

Event Extensions.Web.Geolocation.OnLocationChanged(&GeolocationInfo)    
    msg(&geolocationinfo.ToJson())    
EndEvent

Event 'GetLocationWithOptions'    
    Extensions.Web.Geolocation.requestLocation(&LocationRequestOptions)
Endevent
```

### [**Sample 5: Show UI Alert Messages with Web Notification API**](#Sample+5%3A+Show+UI+Alert+Messages+with+Web+Notification+API)

`[imagen omitida: wiki id 58365]`

```
Event 'Show Notification'
    UINotification.show(&UINotificationMessage.Id, &UINotificationMessage)
Endevent

Event 'Hide Notification'
    UINotification.hide(&DeleteNotificationId)
Endevent

Event 'ShowSimple'
    UINotification.show(&NotificationId, &NotificationTitle, &NotificationBody, '')
Endevent

Event UINotification.onRequestPermission(&permission)  //'granted', 'denied'
    msg("UINotification.requestPermission: " + &permission)    
EndEvent
```

### [**Sample 6: Manage Browser History API:**](#Sample+6%3A+Manage+Browser+History+API%3A)

```
Event 'PushState'
    Extensions.Web.History.PushState(&ResourceName)
Endevent

Event 'Replacestate'
    Extensions.Web.History.ReplaceState(&ResourceName)
Endevent

Event 'GoBack'
    Extensions.Web.History.GoBack()
Endevent

Event 'GoForward'
    Extensions.Web.History.GoForward()
Endevent
```

## **Installation instructions**

**GeneXus 17 Upgrade 5 onwards:**

1. In the GeneXus main menu, select: **Knowledge Manager > Manage Module References**
2. Select Global Matrix and Install "WebExtensionToolkit". (Requires [Maven](https://mkyong.com/maven/how-to-install-maven-in-windows/). Installation will fail if not installed)

It is ready to use!

**GeneXus 17 Upgrade 4 or prior versions:**

1. [Download .OPC file from Marketplace](https://marketplace.genexus.com/viewproduct.aspx?758)
2. In the GeneXus main menu, select: **Knowledge Manager > Manage Module References**
3. In the left dialog, right-click "Upload from file". Select the .opc file
4. Install
5. Copy the file ["gx-web-extensions.js" (download it here)](https://raw.githubusercontent.com/ggallotti/genexusweblibrary/master/src/gx-web-extensions.js) to the WEB folder.
6. Copy the file ["gx-grid-freeze.js" (download it here)](https://raw.githubusercontent.com/ggallotti/genexusweblibrary/master/src/gx-grid-freeze.js) to the WEB folder. (If using Grid.FreezeColumns)

**Additionally, for GeneXus 15 Upgrade 8 or prior (ONLY)**

Add the following code:

* **.NET:**Form.HeaderRawHTML += !'<script type="text/javascript" src="gx-web-extensions.js" data-gx-external-script=""></script>'
* **.JAVA:**Form.HeaderRawHTML += !'<script type="text/javascript" src="../static/gx-web-extensions.js" data-gx-external-script=""></script>'

### [**Troubleshooting**](#Troubleshooting)

```
javax.servlet.ServletException: java.lang.NoClassDefFoundError: com/webinterop/extensions/web/SdtWindowOptions
```

* Check if "Web\modules\Extensions.jar" has been copied to "WEB-INF\Lib" directory

```
js error: cannot read 'web' of undefined  or 404 not found
```

* Check if the file "gx-web-extensions.js" (<https://raw.githubusercontent.com/ggallotti/genexusweblibrary/master/src/gx-web-extensions.js>) has been copied to the Deploy static directory.

#### [[**Symptom:** When Installing, "Object reference not set to an instance of an object"](https://wiki.genexus.com/commwiki/wiki?40172)](#com.gxwiki.wiki%3F40172%2CManage%2BModule%2BReferences%23Troubleshooting+Symptom%3A+When+Installing%2C+%22Object+reference+not+set+to+an+instance+of+an+object%22)

```
error: Error downloading module 'WebExtensionToolkit' from 'GeneXusMatrix' (internal error: 'Object reference not set to an instance of an object.').
```

In gxlogging.log you can see the following error:

**PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested**

**Reason:** GeneXus requires Maven 3.6.1 or higher for installing modules from a Nexus [Modules Server](https://wiki.genexus.com/commwiki/wiki?45933).  
**Solution:**Install/update [Maven](https://mkyong.com/maven/how-to-install-maven-in-windows/), which has to be added to the System Path. Also, it is necessary to update the JDK or manually update the certificate in the Java version of the development machine, so that the new certificate used by the Matrix server is recognized. This will allow you to establish a secure connection and resolve the error. More information is available at [SAC #52914](https://www.genexus.com/developers/websac?es,,,52914).
