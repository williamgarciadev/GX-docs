---
title: "Submit method"
source_id: 24382
source_url: https://wiki.genexus.com/commwiki/wiki?24382
genexus_version: "18"
---

# Submit method

Executes a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) asynchronously; the main program flow will continue processing immediately.

**Note**: The Client WebSession is not available in the submit procedure.

### [Syntax](#Syntax)

*ObjectName***.Submit(***submit-parms* , [*parm1*, .... , *parN*]**)**

**Where:**  
*ObjectName*  
      Is the name of the Procedure we want to submit.

*submit-parms*  
      This parameter is only used in [iSeries applications](https://wiki.genexus.com/commwiki/wiki?24383), all other generators will ignore the parameter.

*par1, …, parN*  
      Optional parameters that can be sent to the submitted object with some purpose (and they must be received in the called object by declaring them with the [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862)).

### [Samples](#Samples)

Suppose you have a [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) in your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?2428) that only has a button included in its form. Its objective is to submit a Procedure which will do some calculations; so, when the user presses that button, the event associated to it is executed. In order to achieve this, the following code inside the event associated to the button has to be defined:

```
Event 'Calculate Payroll Tax'
    CalculatePayrollTax.Submit("", &startDate, &endDate)
EndEvent
```

The Procedure *CalculatePayrollTax* will be submitted and the program execution will return immediately to the called object.

### [See Also](#See+Also)

[Submit rule](https://wiki.genexus.com/commwiki/wiki?15405,,)  
[iSeries Submit considerations](https://wiki.genexus.com/commwiki/wiki?24383)  
[VB Submit considerations](https://wiki.genexus.com/commwiki/wiki?24384,,)


|  |
| --- |
| **Backlinks** |
| [Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947) | [iSeries Submit considerations](https://wiki.genexus.com/commwiki/wiki?24383) | [Specification Codes from spc0000 to spc0049](https://wiki.genexus.com/commwiki/wiki?6431) |
| [Submit command](https://wiki.genexus.com/commwiki/wiki?15386) |

---
