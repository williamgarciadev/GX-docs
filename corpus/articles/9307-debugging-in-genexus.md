---
title: "Debugging in GeneXus"
source_id: 9307
source_url: https://wiki.genexus.com/commwiki/wiki?9307
genexus_version: "18"
---

# Debugging in GeneXus

In the [GeneXus IDE](https://wiki.genexus.com/commwiki/wiki?5272) you can debug GeneXus code, such as with other development environments (Visual Studio, NetBeans, etc.).

To debug the application, you have to add a breakpoint and run the application. When the breakpoint is found, GeneXus gets the focus, and you can check attribute and variable values using the "Watch" tool window. In addition, the "Call Stack" window shows you the objects executed from the beginning of the execution.

Follow the basic steps to debug your code:

1. Go to the Toolbar and select the Debug configuration, as shown in the image:  
   `[imagen omitida: wiki id 53560]`  
   Once you have to select Debug, a pop-up window opens with the following options:
   1. Watch: Allows to visualize the values of variables and attributes at each step of the running process.  
      `[imagen omitida: wiki id 56254]`
   2. Call Stack: Shows the object and the execution lines.  
      `[imagen omitida: wiki id 56255]`
   3. Breakpoints: Displays the objects and lines of code where breakpoints have been added. It also allows you to activate, deactivate, delete, and navigate to where they are defined.  
      `[imagen omitida: wiki id 56256]`In addition, the debug tool window (DebuGx) will open.
2. Add objects you want to debug to the debug tool window by clicking on Add and selecting the objects to debug in the pop-up window:  
   `[imagen omitida: wiki id 53561]`
3. Open an object added to the debug tool window and set a breakpoint on the line of code you need to review. To do this, you can right-click on the line and select Toggle Breakpoint.  
   `[imagen omitida: wiki id 53563]`  
   **Note:** Step 2 is not mandatory. You can add the breakpoint in the object's line you want, and it automatically added this object to the debug tool window.
4. Go to the Watch Window and use the Add button to add the variables and attributes for which you want to know the value.
5. Run the application by pressing F5.  
   During execution, upon encountering a breakpoint, GeneXus will stop its execution and take the focus.  
   `[imagen omitida: wiki id 53564]`
6. Use the Debug toolbar to run, step by step. To do this, right-click anywhere on the Toolbar and select Debug.  
   `[imagen omitida: wiki id 53565]`

In the following video, you can see the example of the execution time.

`[imagen omitida: wiki id 56303]`

**Notes:**

* Objects added to the debug tool window are generated again with debug information.
* Objects generated with Debug information execute slower. In case of extreme performance degradation, see [SAC #39137](https://www.genexus.com/es/developers/websac?data=39137).
* Notice that the release code will be generated after rebuilding using the '*Release*' configuration option.
* The debugger works with Server Side Code.
* Please review [GeneXus Debugger and Profiling common issues](https://wiki.genexus.com/commwiki/wiki?11013), for troubleshooting.

### [Scope](#Scope)

**Object:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generator:** [Java](https://wiki.genexus.com/commwiki/wiki?12258), [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892)  
**Level:** Back end

### [See Also](#See+Also)

[Code Coverage and Profiling](https://wiki.genexus.com/commwiki/wiki?44369)  
[Live Editing in Web Applications](https://wiki.genexus.com/commwiki/wiki?27771)  
[HowTo: Enable logging for Native Mobile](https://wiki.genexus.com/commwiki/wiki?37846)


|  |
| --- |
| **Backlinks** |
| [Configuration options](https://wiki.genexus.com/commwiki/wiki?11087) | [GeneXus Debugger and Profiling common issues](https://wiki.genexus.com/commwiki/wiki?11013) | [GXtest - FAQ](https://wiki.genexus.com/commwiki/wiki?41196) |
|

---
