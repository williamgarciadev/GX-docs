---
title: "GXtest Troubleshooting"
source_id: 46828
source_url: https://wiki.genexus.com/commwiki/wiki?46828
genexus_version: "18"
---

# GXtest Troubleshooting

On this page, you can find some common errors related to GXtest objects and how you can fix them quickly.

## [Testing object or related gives build error](#Testing+object+or+related+gives+build+error)

These cases could be a typical error that some objects need to be rebuilt. Test objects are not built in a Rebuild All operation because they are not called by any Main object (except some user change it), so the option Rebuild All Tests forces to rebuild test objects and their references.

**Solutions**: there are two options:

a) Modify the object so is automatically rebuilt by GeneXus in the next execution

b) Run the option Test -> Rebuild All Tests.

## [Running web UI tests on Internet Explorer on Jenkins as a service or similar](#Running+web+UI+tests+on+Internet+Explorer+on+Jenkins+as+a+service+or+similar)

In order for web UI tests to work properly over the Internet Explorer browser, the browser must be opened by the CI server. That is because If you have Jenkins as a service, tests are running under "SYSTEM" which has different security settings than your Administrator account. To solve this Jenkins must be executed from the command line and not as a service. Information regarding this topic [is here](https://github.com/SeleniumHQ/selenium/wiki/InternetExplorerDriver#running-iedriverserverexe-under-a-windows-service).

Note: If you already have it running as a service you can use the *Jenkins.war* file in your Jenkins installation folder as follows:

```
java -jar "C:\Program Files\Jenkins\Jenkins.war" --httpPort=8081
```

## [Error launching browser for web UI tests](#Error+launching+browser+for+web+UI+tests)

If you have some error like "session not created" or "this version is not compatible" check out the [Web UI Tests Compatibility Issues](https://wiki.genexus.com/commwiki/wiki?46393)

In case you get an error like "error sending request for url (https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json): error trying to connect: tcp connect error:" check out [this article](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?58668,,).

## [Download a file automatically on Internet Explorer](#Download+a+file+automatically+on+Internet+Explorer)

When you need to download a file in a user interface test executed on Internet Explorer, you will have to manage a download bar that appears in the browser. See the [workaround to download a file on IE](https://wiki.genexus.com/commwiki/wiki?47272).

## [error: Running tests is supported only when build mode is set to MSBuild. You need to change it in order to be able to execute your tests using this version properly.](#error%3A+Running+tests+is+supported+only+when+build+mode+is+set+to+MSBuild.+You+need+to+change+it+in+order+to+be+able+to+execute+your+tests+using+this+version+properly.)

In .Net Environments, .Generator Property 'Build Mode' must be set to "MSBuild".

## [bash: /usr/local/bin/xcpretty: No such file or directory](#bash%3A+%2Fusr%2Flocal%2Fbin%2Fxcpretty%3A+No+such+file+or+directory)

To be able to run UI tests in iOS you need to install the library xcpretty in addition to [Apple Requirements](https://wiki.genexus.com/commwiki/wiki?19478).


|  |
| --- |
| **Backlinks** |
| [Table of contents:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Table of contents:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) |

---
