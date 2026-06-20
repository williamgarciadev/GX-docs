---
title: "Run Target property"
source_id: 49730
source_url: https://wiki.genexus.com/commwiki/wiki?49730
genexus_version: "18"
---

# Run Target property

Sets the target server that will be used to serve an Angular application.

### [Values](#Values)

|  |  |
| --- | --- |
| **Default** | This value implies that, by default, it runs on the 'Angular Dev Server' for fast prototyping. However, if the 'Deploy to cloud' property of the backend generator is set to Yes, the application will be deployed to the GeneXus cloud automatically. |
| **Angular Dev Server** | It runs on a Local Development Server for fast prototyping. Angular HTTP Server of the Angular Platform. It is a Server that runs local to the machine on a random Port. |
| **Local WebServer** | The application is copied to the local Web Server of the GeneXus Environment (Java, .Net) below a subfolder called "ng". It is executed directly in the URL of the Web backend. |

### [Scope](#Scope)

**Generators:** [Angular](https://wiki.genexus.com/commwiki/wiki?42550)  
**Level:** Generator

### [Description](#Description)

All these options are for prototyping purposes.

The 'Angular Dev Server' option makes the Angular application run on the development machine, from its own prototyping web server. This has the advantage that it automatically detects changes in the sources and compiles instantly. It is not necessary to Run again to see the changes after generating, because immediately after generating the Angular program is compiled and updated in the prototyping server. This option may require a manual configuration of the [CORS](https://wiki.genexus.com/commwiki/wiki?52092,,) in the local server.

When selecting the 'Local WebServer' value, the application is copied to a subdirectory (named "ng") of the backend server and runs from the same web server that runs the backend.

For deploying to production, read [Frontend applications deployment](https://wiki.genexus.com/commwiki/wiki?51105).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Availability](#Availability)

This property is available since [GeneXus 17 upgrade 7](https://wiki.genexus.com/commwiki/wiki?49301,,).

### [See Also](#See+Also)

[Deploy to cloud property](https://wiki.genexus.com/commwiki/wiki?15041)


|  |
| --- |
| **Backlinks** |
| [Deploy to cloud property](https://wiki.genexus.com/commwiki/wiki?15041) | [Frontend applications deployment](https://wiki.genexus.com/commwiki/wiki?51105) |

---
