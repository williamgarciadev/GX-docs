---
title: "Android UITest Log"
source_id: 55471
source_url: https://wiki.genexus.com/commwiki/wiki?55471
genexus_version: "18"
---

# Android UITest Log

## [How to generate it?](#How+to+generate+it%3F)

To generate this log, change the value of the [Default Log Level property](https://wiki.genexus.com/commwiki/wiki?33333) of the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770) being tested (the one set in the [Test Target property](https://wiki.genexus.com/commwiki/wiki?42595) of the [UI Test object](https://wiki.genexus.com/commwiki/wiki?46009)) to Debug.

`[imagen omitida: wiki id 55472]`

As a result, when the execution of the UITest is completed, there is a log and screenshots from the steps where the test failed.

## [Where are the log and screenshots saved?](#Where+are+the+log+and+screenshots+saved%3F)

The log and screenshots are saved in the testResults directory below the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) directory.

The name of the log is <TestTargetName>UITests.log

For example, if the main object is called MainSD, the log will be called MainSDUITests.log.

`[imagen omitida: wiki id 55473]`

## [How to read it?](#How+to+read+it%3F)

Start and meaning of parts of the lines

`[imagen omitida: wiki id 55474]`

Date, time:minutes:seconds:milliseconds, process id, logtype (D, I, W, E), and tag.

The logType depends on what is set in the logLevel property, which is D for debug.

This means it will add Error (E), Information (I), and Warning (W) lines.

If you want a shorter log that includes only errors, for example, change the main object property from Debug to Error.

### [Tag examples](#Tag+examples+)

#### [GeneXusApplication](#GeneXusApplication)

When the "GeneXusApplication" label is found in the log, the following records will provide information related to the metadata read from the application, including details about database tables, [procedures](https://wiki.genexus.com/commwiki/wiki?6293), validation rules, events, and other elements of the logic and user interface.

`[imagen omitida: wiki id 55475]`

#### [GeneXus HTTP - Request](#GeneXus+HTTP+-+Request)

`[imagen omitida: wiki id 55476]`

#### [GeneXus HTTP - Response](#GeneXus+HTTP+-+Response)

This section of the log shows the server's response. In this case, there is a 500 error on the server.

`[imagen omitida: wiki id 55477]`

#### [GeneXusApplication: Loading...](#GeneXusApplication%3A+Loading...+)

Several Loading lines may be displayed. They are all the panels in the main object call tree.

`[imagen omitida: wiki id 55478]`

It loads all the panels at the start.

#### [Device Information](#Device+Information)

Shows information about the emulator or device. If it is shown, you can be sure that the application metadata is being loaded.

`[imagen omitida: wiki id 55479]`

#### [Starting test](#Starting+test)

This line indicates the start of the test execution and shows the name of the executed test object.

`[imagen omitida: wiki id 55480]`

#### [[UITestingLibLogger] starting command / ending command after](#NoWiki+1+starting+command+%2F+ending+command+after)

This tag shows the commands that are executed, the start and end of the commands, and how long they took.

`[imagen omitida: wiki id 55481]`


|  |
| --- |
| **Backlinks** |
| [UI Test for Native Mobile Automation](https://wiki.genexus.com/commwiki/wiki?44571) |

---
