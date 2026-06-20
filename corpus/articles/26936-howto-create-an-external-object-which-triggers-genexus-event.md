---
title: "HowTo: create an External Object which triggers GeneXus events in iOS"
source_id: 26936
source_url: https://wiki.genexus.com/commwiki/wiki?26936
genexus_version: "18"
---

# HowTo: create an External Object which triggers GeneXus events in iOS

## [Introduction](#Introduction)

This guide explains how to create an External Object that can be called from offline and online code and can trigger a GeneXus Event.

## [Getting started](#Getting+started)

If you haven't already done so, please read [this](https://wiki.genexus.com/commwiki/wiki?18072) document first, explaining the basics on how to create an external object for iOS.

You must provide the user-event-callable implementation allong with the offline implementation, so start there first. Then check how to [create an extension library](https://wiki.genexus.com/commwiki/wiki?36340) as this sample uses it.

## [Example](#Example)

You will implement a timer in Swift, that is, an external object with a method that receives a number of seconds, a message, and calls a GeneXus event when the time has elapsed, passing the message to the event.

We need:

* A definiiton in GeneXus (External Object)
* an offline implementation to be called from the generated code
* a handler to be called from the online code.

## [External Object definition](#External+Object+definition)

This is the external object definition:

`[imagen omitida: wiki id 26937]`

Make sure you mark the *Start* method and the *Completed* event as "static".

## [Offline](#Offline)

Before starting with the implementation, you need to provide some information in the EO definition.

`[imagen omitida: wiki id 38518]`

And the Start method:

`[imagen omitida: wiki id 38519]`

### [Implementation](#Implementation)

Now that everything is in place, you can provide the actual implementation.

First of all, create the TimerEO class as follows:

#### [TimerEO.swift](#TimerEO.swift)

```
import Foundation
import GXStandardClasses

class TimerEO: GXExternalObjectBase {

    private static let gxServerSideEvent = "Completed"

    private var message: String = ""
    
    init(message: String) {
        self.message = message
        super.init()
    }

    static func startTimerWithSeconds( _ seconds: Int, _ message: String) {
        TimerEO(message: message).startTimer(seconds: seconds)
    }
        
    func startTimer(seconds: Int) {
        gx_dispatch_sync_on_main_queue({() -> Void in
            Timer.scheduledTimer(timeInterval: TimeInterval(seconds), target: self, selector: #selector(self.timerDidFinish), userInfo: nil, repeats: false)
        })
    }

    open override var externalObjectName: String {
        return "TimerEO"
    }
    
    // MARK - GeneXus event

    @objc func timerDidFinish(timer: Timer) {
        self.dispatchExteralObjectEvent(TimerEO.gxServerSideEvent, withParameters: [self.message])
    }
}
```

#### [A few things to note:](#A+few+things+to+note%3A)

1. To simplify the code, there is no error handling. The type of the parameters is not checked in *startTimer* method, and there is no way to know if the timer was scheduled correctly. You should add error cheching in your EO's actual implementation.
2. The *startTimer(seconds:)* method creates the timer in the main thread. This is beacuse it may be called on a background thread that finishes before the time has been elapsed, and in that case the event won't be triggered.  
   When implementing your own external object, you may need to do some things on the main thread, but avoid doing this if it is not required.
3. The *externalObjectName* is required if the external object will trigger some GeneXus events, and should return the name of the EO as defined in GeneXus
4. To trigger the *Completed* GeneXus event, use the method *dispatchExteralObjectEvent* defined in the base class.

You are done, when using the Start method from the TimerEO from an offline application, the generated code will directly call the static function *startTimerWithSeconds*.

## [Online section](#Online+section)

By "online", we mean an external object that can be called from a user event, whether the object that calls it is online or offline.

As described in [External Object for iOS Devices](https://wiki.genexus.com/commwiki/wiki?18072), you need to provide a "mapper" class (TimerEOLibrary.swift) and the implementation for the handler (TimerEOActionHandler.swift).

### [Implementation](#Implementation)

Here's the code:

#### [TimerEOLibrary.swift](#TimerEOLibrary.swift)

```
import GXCoreBL

@objc(TimerEOLibrary)
public class TimerEOLibrary: NSObject, GXExtensionLibraryProtocol {

    public func initializeExtensionLibrary(withContext context: GXExtensionLibraryContext) {

        GXActionExternalObjectHandler.register(TimerEOActionHandler.self, forExternalObjectName:TimerEOActionHandler.classIdentifier)

    }
}
```

#### [TimerEOActionHandler.swift](#TimerEOActionHandler.swift)

```
import Foundation
import GXCoreBL

@objc(TimerEOActionHandler)
public class TimerEOActionHandler: GXActionExternalObjectHandler {

    public static let classIdentifier = "TimerEO"

    override public class func handleActionExecutionUsingMethodHandlerSelectorNamePrefix() -> Bool {
        return true
    }
    
    // MARK - External object methods
    
    @objc public func gxActionExObjMethodHandler_Start() {
        let (secs, msg) = self.readParameters()
        if (secs == nil) {
            let error = NSError.wrongNumberOfParametersDeveloperError(forMethod: self.actionExObjDesc.actionExternalObjectMethod)
            self.onFinishedExecutingWithError(error)
            return
        }
        self.handleStartTimerAction(seconds: secs!, message: msg!)
        self.onFinishedExecutingWithSuccess()
    }

    //MARK: - Private
    
    private func readParameters() -> (Int?, String?) {
        guard let actionParameterArray = self.actionExObjDesc.actionParametersDescriptor??.actionParametersDescriptors,
            actionParameterArray.count == 2 else {
            return (nil, nil)
        }
        let seconds = self.readStringParameter(actionParameterArray[0], from: self.contextEntityData())
        let msg = self.readStringParameter(actionParameterArray[1], from: self.contextEntityData())
        return (GXUtilities.integerNumber(fromValue: seconds) as? Int, GXUtilities.nonEmptyString(from: msg))
    }
        
    private func handleStartTimerAction(seconds: Int, message: String) {
        // Start the timer and trigger the user event
        TimerEO.startTimerWithSeconds(seconds, message)
        self.onFinishedExecutingWithSuccess()
    }
}
```

The online code uses the *gxActionExObjMethodHandler\_Start* function; gets the parameters and then calls the *handleStartTimerAction* function which uses the TimerEO implementation already discussed.

## [GeneXus test objects](#GeneXus+test+objects)

To test the implementation, we created the following objects:

### [MainTimer (Dashboard)](#MainTimer+%28Dashboard%29)

#### [Properties](#Properties)

Main program: True

Connectivity Support: Offline

#### [Events](#Events)

```
Event TimerEO.Completed(&message)
    msg(&message)
EndEvent

Event 'StartTimer'
    TimerEO.Start(5, "TimerEO from user code")    
Endevent

Event 'StartTimerProc'
    StartTimerProc()
EndEvent
```

### [StartTimerProc (Procedure)](#StartTimerProc+%28Procedure%29)

#### [Source](#Source)

```
TimerEO.Start(5, "TimerEO from offline code")
```

### [Source Code](#Source+Code)

You can download the source code from this sample [here](http://svn.assembla.com/svn/gxusercontrols/SmartDevices/iOS/TimerEOv15).

Note: you'll need a [SVN](https://wiki.genexus.com/commwiki/wiki?27438,,) client to donwload the source code, or you can browse it online in the link above.

### [Installation](#Installation)

You need [GeneXus 15 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?37491,,) or higher and copy the TimerEO folder to "GeneXusInstallDir\Libraries\".


|  |
| --- |
| **Backlinks** |
| [External Object for iOS Devices](https://wiki.genexus.com/commwiki/wiki?18072) | [Global Events](https://wiki.genexus.com/commwiki/wiki?31164) |

---
