---
title: "GXtest Menu Commands"
source_id: 48103
source_url: https://wiki.genexus.com/commwiki/wiki?48103
genexus_version: "18"
---

# GXtest Menu Commands

GXtest provides some commands that allow creating and running tests in a [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836). Among them, you can distinguish two types of commands: global commands and contextual commands.

## [Global commands or operations](#Global+commands+or+operations)

### [Run All Tests](#Run+All+Tests)

Builds and runs all enabled tests present in the KB, i.e. unit tests, web UI tests, Rest tests, and UI tests.

Shortcut: Ctrl + Shift + R

`[imagen omitida: wiki id 50210]`

Run All Unit Tests

Build and runs all enabled unit tests present in the KB.

Shortcut: Ctrl + Shift + U

### [Rebuild All Tests](#Rebuild+All+Tests)

Rebuild all enabled tests and, therefore, the objects called by them.

`[imagen omitida: wiki id 50211]`

### [Run Current Test](#Run+Current+Test)

Run the current test being edited or the object unit tests if the object being edited is a testable object.

Shortcut: Ctrl + R

### [Record Web UI Test](#Record+Web+UI+Test)

Creates, records and saves a new web UI test using GXtest Recorder extension: see more information about this feature in the [Recorder-IDE integration](https://wiki.genexus.com/commwiki/wiki?48448) article.

`[imagen omitida: wiki id 50212]`

### [Stop Tests Execution](#Stop+Tests+Execution)

Stops the current tests execution in progress, or the build process, if any.

`[imagen omitida: wiki id 50213]`

### [Tests Build Type](#Tests+Build+Type)

Allows choosing the type of build performed (if any) when a test execution is done. The options are the following:

* Build: a build operation is performed with the selected tests. Default value.
* Rebuild: a rebuild operation is performed with the selected tests
* These Only: a build with these only is performed with the selected tests
* No Build: no build operation is performed whatsoever. Therefore tests are immediately run.

This setting is saved as a local KB property, this means it is stored locally and remembered each time you open the KB, but it is not committed to GXServer. Additionally, a shortcut is displayed in the toolbar so it is easier to modify it.

`[imagen omitida: wiki id 52984]`

## [Contextual menu options](#Contextual+menu+options)

These options are available when specific objects are selected, typically tests or unit-testable objects (procedures, data providers, and business components).

### [Run Test(s)](#Run+Test%28s%29)

* Target objects: tests or suites. It becomes available for a selection from one to any number of test objects exclusively. Disabled when there is a test execution in progress.
* Action: Run the selected test objects.
* Shortcut: Ctrl + R

`[imagen omitida: wiki id 50216]`

### [Run Unit Tests](#Run+Unit+Tests)

* Target objects: unit-testable objects: procedures, data providers, and business components. It becomes available for a single unit-testable object. Disabled if there is a test execution in progress.
* Action: Run the unit tests that call the selected object.
* Shortcut: Ctrl + R

`[imagen omitida: wiki id 50214]`

### [Create Unit Test](#Create+Unit+Test)

* Target objects: unit-testable objects: procedures, data providers, and business components. It becomes available for a single unit-testable object.
* Action: Creates a unit test for the selected object according to Test Generation properties set for the current KB.

`[imagen omitida: wiki id 50215]`

### [Create Rest Test](#Create+Rest+Test)

* Target objects: objects exposable as Rest services. It becomes available for a single object.
* Action: Creates a Rest test for the selected object according to Test Generation properties set for the current KB.

`[imagen omitida: wiki id 52985]`

### [Record Mocking Data](#Record+Mocking+Data)

* Target objects: unit tests. It becomes available for a single unit test selection. Disabled if there is a test execution in progress.
* Action: Run the selected unit test, recording all queries to the database during its execution. See [Database Mocking](https://wiki.genexus.com/commwiki/wiki?38349) for more information about this feature.

`[imagen omitida: wiki id 50217]`


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) |
| [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) | [GXtest Menu Commands (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54365) | [GXtest Menu Commands (GeneXus 18)](https://wiki.genexus.com/commwiki/wiki?52983) |

---
