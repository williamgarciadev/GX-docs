---
title: "Object Mock Testing"
source_id: 55859
source_url: https://wiki.genexus.com/commwiki/wiki?55859
genexus_version: "18"
---

# Object Mock Testing

This feature allows you to pre-set some replacements for invocations to internal objects to not depend on them, just testing the code you need to test and nothing else. Supported objects are Procedures and Data Providers.

The mechanism uses an external object inside the GXtest module. This external object called MockManager provides 2 basic functions: Skip, and SetMock.

### [SetMock(in:&objectName, in:&mockObject)](#SetMock%28in%3A%26objectName%2C+in%3A%26mockObject%29)

Receives two varchar values, the name of the object to be mocked and the name of the object to execute instead. This means that when running the test, instead of calling the objectName, the mock object is executed.

The mock object must have the same number and type of parameters as the object being replaced (they must be interchangeable). It is required that in the usage of this function, the parameterization of MockObject is done using the syntax ObjectName.Type, otherwise ObjectName will not be generated and execution will fail.

```
&MockManager.SetMock(ObjectX.Type, ObjectXMock.Type)
```

### [Skip(in:&objectName)](#Skip%28in%3A%26objectName%29)

If you want a call to an object to be avoided, then you don't necessarily need to create an object to replace it. Using this function you can skip the execution and output parameters (if any) will be set with default values for each type.

### [Notes](#Notes)

* The usage of MockManager external object is local to the test where it is declared, it does not affect the invocation of other objects calling the mocked objects from other contexts.
* Mockable objects must be enabled through an environment-level property and require rebuilding the objects. The property is [Generate Mockable Objects property](https://wiki.genexus.com/commwiki/wiki?56903).
* Any code can be mocked by placing it inside a Procedure object, this is very useful when you have a call to an external service that you don’t want to depend on

### [Example](#Example)

If you have a Procedure called ProcA that calls to ProcB and you are interested in testing ProcA’s code only, the first step is to define a variable of type MockManager in the unit test.

So in the test source code, you can do the following:

```
&Mock.Skip(ProcB.Type) // or &Mock.SetMock(ProcB.Type, ProcBMock.Type)

ProcA(...)

Assert...(...)
```

This code will cause the object ProcB is not executed in the context of the execution of the current test. In the case of using the SetMock method, the ProcBMock procedure will be executed instead.

## [Creating a mock](#Creating+a+mock)

The easiest way to create a mock is by using the contextual menu option Create Mock, which creates a copy of the selected procedure except for the Source part. The source includes comments with the [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862) of the Procedure and sample code. This option is enabled only when the [Generate Mockable Objects property](https://wiki.genexus.com/commwiki/wiki?56903) is set to Yes.

### [Availability](#Availability)

This feature is available since [GeneXus 18 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?54242).


|  |
| --- |
| **Backlinks** |
| [Changelog GXtest](https://wiki.genexus.com/commwiki/wiki?43807) | [Generate Mockable Objects property](https://wiki.genexus.com/commwiki/wiki?56903) | [GeneXus 18 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?54242) |
| [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) |

---
