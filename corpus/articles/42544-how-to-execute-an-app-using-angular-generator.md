---
title: "How to execute an app using Angular Generator"
source_id: 42544
source_url: https://wiki.genexus.com/commwiki/wiki?42544
genexus_version: "18"
---

# How to execute an app using Angular Generator

With [GeneXus Angular Generator](https://wiki.genexus.com/commwiki/wiki?42550), when you [Run](https://wiki.genexus.com/commwiki/wiki?5692) your main object, a window console is opened, the application is automatically installed on a server (that is launched for development purposes).

If this fails, you can execute it manually by following these steps:

Open a command-line prompt, change directory to <KB Model Directory>\mobile\Angular\<main> (e.g.:LightCRM\CSharpModel\mobile\Angular\LightCRM) and run:

* npm install

The npm install command installs all the necessary libraries to run the application under the  <KB Model Directory>\mobile\Angular\LightCRM\node\_modules folder. This folder contains all the libraries needed to execute the application, such as Angular, the library of GeneXus controls, etc., and is handled by npm from packages.json file. The packages.json file contains the list of libraries that must be installed, which are necessary to run the application, and is created by the generator.

You only need to execute it once after installing a new GeneXus build.

* npm start

The npm start will complete setup launch the server, watch the files, and rebuild the app as GeneXus makes changes to those files.

Once these commands are executed and the application is running, you should keep the cmd console open so the changes generated in GeneXus are automatically compiled and updated in the browser.


|  |
| --- |
| **Backlinks** |
| [Toc:Angular Application Development](https://wiki.genexus.com/commwiki/wiki?42539) | [Angular Generator requirements](https://wiki.genexus.com/commwiki/wiki?42541) | [My first Angular application](https://wiki.genexus.com/commwiki/wiki?42551) |
| [My first Angular application (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?57319) |

---
