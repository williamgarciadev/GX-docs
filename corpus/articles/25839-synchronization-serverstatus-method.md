---
title: "Synchronization.ServerStatus method"
source_id: 25839
source_url: https://wiki.genexus.com/commwiki/wiki?25839
genexus_version: "18"
---

# Synchronization.ServerStatus method

### [Syntax](#Syntax)

```
&ServerStatus = Synchronization.ServerStatus()
```

**Where:**

&ServerStatus is a Numeric variable.

### [Description](#Description)

This method determines if there were any changes in the server side since last synchronization, which allows the developer to know whether is convenient or not to call the [Synchronization.Receive method](https://wiki.genexus.com/commwiki/wiki?23603).

This process is executed in the server side, which means it might take some time to be finished. In addition, this process requires the server to calculate the hashes of all involved tables in order to determine if changes has been made since last synchornization. Please read the [Advanced Concepts of Offline Applications architecture](https://wiki.genexus.com/commwiki/wiki?25536) document for more information.

### [Type returned](#Type+returned)

Returns one of the following values:

| Value | Meaning |
| --- | --- |
| 0 | There is no pending data to be received from the server side, which means both systems, the device and the server, are synchronized. |
| 1 | There has been changes in the server side since last synchronization. Note that if no [data reception process](https://wiki.genexus.com/commwiki/wiki?23603) has been done yet, this is the returned value. |

### [Example](#Example)

An example of calling the ServerStatus method when pressing a button and asking for confirmation to receive data:

```
Event "MyAction"
    Composite        
        &ServerStatus = Synchronization.ServerStatus()
        If &ServerStatus = 1
            &HasConfirmed = Interop.Confirm("Server has changed since last synchronization, synchronize?")
            If &HasConfirmed
                Synchronization.Receive()
            EndIf
        EndIf
    EndComposite
EndEvent
```

**Tip:** Server status is checked automatically before synchronization, so It's not necessary to check again in your code. However Synchronization.ServerStatus could be useful to ask for user confirmation or other scenarios

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects** | [Objects for Native Mobile applications development](https://wiki.genexus.com/commwiki/wiki?20087) |
| **Platforms** | [Android platform](https://wiki.genexus.com/commwiki/wiki?14453), [Apple platform](https://wiki.genexus.com/commwiki/wiki?14917) |

### [Availability](#Availability)

As from [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,)

### [See also](#See+also)

* [Synchronization.Receive method](https://wiki.genexus.com/commwiki/wiki?23603)
* [Synchronization.Send method](https://wiki.genexus.com/commwiki/wiki?23604)
* [Synchronization API](https://wiki.genexus.com/commwiki/wiki?23602)


|  |
| --- |
| **Backlinks** |
| [Toc:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) | [Synchronization API](https://wiki.genexus.com/commwiki/wiki?23602) | [Synchronization.Receive method](https://wiki.genexus.com/commwiki/wiki?23603) |
| [Synchronization.Send method](https://wiki.genexus.com/commwiki/wiki?23604) |

---
