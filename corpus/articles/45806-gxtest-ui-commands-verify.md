---
title: "GXtest UI Commands - Verify"
source_id: 45806
source_url: https://wiki.genexus.com/commwiki/wiki?45806
genexus_version: "18"
---

# GXtest UI Commands - Verify

This command is useful to validate if a boolean value is True, setting optionally if test execution must be stopped when validation fails and a message identifying the validation.

`[imagen omitida: wiki id 47476]`

`[imagen omitida: wiki id 47477]`

`[imagen omitida: wiki id 47478]`

Works like an assertion but if the value is not True, then a screenshot of the web page is taken. If it's called with only one parameter, then the StopExecution value will be set to the [*Verify Stops Execution* property](https://wiki.genexus.com/commwiki/wiki?45420)'s value on the current environment.

#### [Parameters:](#Parameters%3A)

* Value: the boolean value to check.
* StopExecution: optional parameter indicating if the received parameter is not True then execution must be stopped or not. The default value is True.
* Message: optional parameter to identify the validation done. Useful when seeing a test execution result.

#### [Returns:](#Returns%3A+)

This method doesn't return any value

#### [Examples of use:](#Examples+of+use%3A)

This command can be combined with several commands.

```
&driver.Verify(&driver.IsElementPresentByID("controlID"))

&driver.Verify(not &driver.AppearText("Not found"), false) 

&driver.Verify(not &driver.AppearText("Not found"), false, "Text 'Not found' was found") 

&driver.Verify(not &driver.AppearText("Not found"))

&driver.Verify(&driver.GetValueByName("controlName") = "Customer Name", false) 

&driver.Verify(&driver.GetValueByName("controlName") = "Customer Name", false, '&driver.GetValueByName("controlName") = "Customer Name"')
```

### [Availability](#Availability)

This set of commands is available since [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/wiki?45624,,).

## [SetVerifyStopsExecution](#SetVerifyStopsExecution)

`[imagen omitida: wiki id 48500]`

Allows setting the default behavior for the Verify commands that only receives one parameter to ease a refactor on all the tests in case it is needed. Take into account that as a good practice this command should never be used explicitly inside a test because it implies that the test will not respect the global testing property designed for setting the Verify behavior, which also can be parameterized by MSBuild.

Parameters:

* Value: the boolean value to set. When True, the tests are stopped at the moment a Verify command fails (if it has only one parameter).

Example of use:

```
&driver.SetVerifyStopsExecution(true)

&driver.SetVerifyStopsExecution(false)
```

### [Availability](#Availability)

This command  is available since [GeneXus 17 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?48247,,).


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [FileUpload command examples](https://wiki.genexus.com/commwiki/wiki?47224) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) |
| [GXtest UI Commands - Property Setters](https://wiki.genexus.com/commwiki/wiki?48468) | [GXtest UI Test for Web - Supported Commands](https://wiki.genexus.com/commwiki/wiki?40281) |

---
