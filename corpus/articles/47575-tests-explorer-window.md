---
title: "Tests Explorer window"
source_id: 47575
source_url: https://wiki.genexus.com/commwiki/wiki?47575
genexus_version: "18"
---

# Tests Explorer window

The Tests Explorer window shows a hierarchy including all the test objects present in the currently open [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836), and its parents' folders.

## [Tests Explorer window structure](#Tests+Explorer+window+structure)

`[imagen omitida: wiki id 47886]`

### [1. Filters](#1.+Filters)

This section has two filters and one information label.

* Searchbox: input field to filter test objects by their name
* Tests count: shows the number of test objects present in the KB and the number of tests currently shown due to applied filters
* Test type filter: allows user to view all tests, only unit tests, only web UI tests, only SD UI tests, or only Test Suites.

### [2. Tests tree](#2.+Tests+tree)

This is the main section and shows a tree structure that contains test objects and their ancestors. Disabled tests will be shown in gray.

### [3. Run button](#3.+Run+button)

Click it to run all the checked test nodes.

## [Contextual menu options](#Contextual+menu+options)

There are three different contextual menu options available on this window: Record Mocking Data, Run, and Enable/Disable.

`[imagen omitida: wiki id 52237]`

### [Record Mocking Data](#Record+Mocking+Data)

Runs the selected test saving mocking data for future executions. See [Database Mocking](https://wiki.genexus.com/commwiki/wiki?38349) for more information about this feature.

### [Run](#Run)

Runs the selected test object.

### [Enable/Disable](#Enable%2FDisable)

Enables/disables the selected test.

## [Drag and drop](#Drag+and+drop)

Relocating tests and other objects present on the tree structure performing drag and drop actions are supported. Take into account that only folders that already contain tests are shown and, if you leave any container object (module. folder, or testable KBObject) empty, it will be removed from this view since it no longer contains a test.


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) |

---
