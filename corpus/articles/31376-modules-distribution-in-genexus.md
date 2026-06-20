---
title: "Modules Distribution in GeneXus"
source_id: 31376
source_url: https://wiki.genexus.com/commwiki/wiki?31376
genexus_version: "18"
---

# Modules Distribution in GeneXus

GeneXus allows distribution of the API and binaries of a [Module](https://wiki.genexus.com/commwiki/wiki?22441,,) and installation of it in other [Knowledge Bases](https://wiki.genexus.com/commwiki/wiki?1836).

A Module installed using this mechanism, provided by another KB, has the following characteristics:

* Just the API of the module is visible
* The API is read-only
* It consists of a specific version of the API and also its implementation (the corresponding binaries in possibly several platforms or languages)

That provides the following benefits:

* It allows preserving the privacy of the code
* It is very clear that the module is maintained by the provider, under a certain license, and unwanted changes are avoided.
* It improves build performance (Code is built just once, in the origin)
* Modules can be easily distributed in the company or publicly through a repository manager

GeneXus itself uses this mechanism to provide the [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268) and others, like [GeneXus Cognitive API](https://wiki.genexus.com/commwiki/wiki?40167).

## [Understanding the modules lifecycle, step by step](#Understanding+the+modules+lifecycle%2C+step+by+step)

Through the following steps, you can create a module, distribute it, install it in another KB, and use it there.

### [1) Create a module with a specific functionality](#1%29+Create+a+module+with+a+specific+functionality)

First, you create a module with specific functionality and test it thoroughly in the platforms you want to provide it.

For this, read [HowTo: Create a Module Object](https://wiki.genexus.com/commwiki/wiki?25541), [HowTo: Add an object to a Module](https://wiki.genexus.com/commwiki/wiki?25548), and [Modules - Defining an interface](https://wiki.genexus.com/commwiki/wiki?22584).

### [2) Package and Publish a module](#2%29+Package+and+Publish+a+module)

Then, you package and publish the module, adding a description of the functionality, link to documentation, and other relevant information.

For this, read [Package and Publish Modules](https://wiki.genexus.com/commwiki/wiki?46751).

Now, you are done: You shared your module on a [Modules Server](https://wiki.genexus.com/commwiki/wiki?45933).

### [3) Create or open another KB, and install the module](#3%29+Create+or+open+another+KB%2C+and+install+the+module)

Open the [Manage Module References](https://wiki.genexus.com/commwiki/wiki?40172) tool window and install it.

### [4) Now you are ready to use it.](#4%29+Now+you+are+ready+to+use+it.+)

`[imagen omitida: wiki id 31389]`

**Note**: The binaries of the referenced modules will be copied to your target environment directory during build time.

### 

## [Objects that are packaged](#Objects+that+are+packaged)

This is a list of objects that could belong to the module's API and implementation.

* Services
  + [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270)
  + [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293)
  + [External object](https://wiki.genexus.com/commwiki/wiki?5669)
* Data
  + [Domain object](https://wiki.genexus.com/commwiki/wiki?7221)
  + [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021)
* Structure
  + [Folder object](https://wiki.genexus.com/commwiki/wiki?9757)
  + [Module object](https://wiki.genexus.com/commwiki/wiki?22411)
* User Interface (Design System)
  + [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375)
  + [Stencil object](https://wiki.genexus.com/commwiki/wiki?38418)
  + [Image object](https://wiki.genexus.com/commwiki/wiki?23387)
  + [File object](https://wiki.genexus.com/commwiki/wiki?5852)
  + [User Control object](https://wiki.genexus.com/commwiki/wiki?39356)

Note: Implementation of Business Components referenced by the implementation of the module's API is also packaged.

#### [Considerations](#Considerations)

The REST service and the corresponding implementation resulting from Procedures that have the [REST Protocol property](https://wiki.genexus.com/commwiki/wiki?37254) set as True are packaged even when those Procedures are not public ([Object Visibility property](https://wiki.genexus.com/commwiki/wiki?22473) set as Internal or Private). This allows packaging REST services to be deployed wherever the module is used.

#### [Sample](#Sample)

There is a KB with the following structure:

```
Root Module
|_ MyModule
   |_ ProcedureA (inherit)
   |_ InternalModule
       |_ ProcedureB (internal, online, REsT)
```

And these details:

* ProcedureA calls ProcedureB.
* The Object Visibility property is set for ProcedureA as Public (exposed) and for ProcedureB as Intenal/Private (not exposed).
* The [Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?20911)  is set for ProcedureA as inherit, and for ProcedureB as online.
* ProcedureB has the properties [Expose as Web Service](https://wiki.genexus.com/commwiki/wiki?36480) and REST Protocol set as True.

When installing MyModule on another KB, if an offline Panel (Connectivity Support = Offline) for Native Mobile (Apple, Android) calls MyModule.ProcedureA, it is executed on the device (that is, offline) and it is able to call the service layer of the same app via REST.

## [MSBuild Tasks for Continuous Integration](#MSBuild+Tasks+for+Continuous+Integration)

There are several MSBuild tasks that help automate tasks or installation, publishing, etc. : More information at [Modules MSBuild Tasks](https://wiki.genexus.com/commwiki/wiki?46830)

## [General Restrictions](#General+Restrictions)

* When Packaging
  + Only submodules of the Root Module can be packaged (i.e. A module with a parent that is not the Root cannot be packaged)
  + Circular dependencies between modules are not allowed
  + Business Components must not be referenced in the module interface's [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862) or [Output property](https://wiki.genexus.com/commwiki/wiki?41037)
  + [Translation type property](https://wiki.genexus.com/commwiki/wiki?9126) must be set to 'No Translation' (default)
  + If you package a module with database access, read: [Package Module with database access for Solutions extensibility scenarios](https://wiki.genexus.com/commwiki/wiki?42900)
* On the Target KB
  + The distributed module must be generated with the same GeneXus version as the one that references the module.
  + Downgrade (installing a lower version of an already installed module) is not fully supported.

FAQ

**Q**: What if the following situation happens: In KB "Provider" is Object A and that object is exported to KB "Client". Then, in KB "Provider", Object A is put into a module M and then that Module is packaged and installed in KB "Client"?   
**A**: Since the internal GUID of object A remains unchanged, GeneXus resolves all; that means: References to object A will now point to M.A. A is not anymore in its folder, it is in the module M under References in KB Explorer; it is read-only and only its interface is available.

**Q**: Not every Procedure in my module got packaged. What happened?  
**A**: In order to be packaged, your objects in the module must be in some main object call tree. So if you have [unreachable objects](https://wiki.genexus.com/commwiki/wiki?40919,,), these will not be packaged. Make sure you add the needed objects to some main object call tree. It could be just a dummy Procedure outside of your Module just for that purpose.


|  |
| --- |
| **Backlinks** |
|
| [GeneXus 18 hardware and software requirements](https://wiki.genexus.com/commwiki/wiki?30900) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54300) |
| [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?54649) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55768) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 6)](https://wiki.genexus.com/commwiki/wiki?56187) | [GeneXus 18 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?54242) |
| [Knowledge-driven with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51573) | [Manage Module References](https://wiki.genexus.com/commwiki/wiki?40172) |
| [Manage Module References (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55064) | [Migrate to Unanimo](https://wiki.genexus.com/commwiki/wiki?52177) | [Module Author property](https://wiki.genexus.com/commwiki/wiki?46757) | [Module Description property](https://wiki.genexus.com/commwiki/wiki?46756) |
| [Module License URL property](https://wiki.genexus.com/commwiki/wiki?46633) | [Module Owner property](https://wiki.genexus.com/commwiki/wiki?46754) | [Module Project URL property](https://wiki.genexus.com/commwiki/wiki?46634) | [Module Resources property](https://wiki.genexus.com/commwiki/wiki?45010) |
| [Module Server URL property](https://wiki.genexus.com/commwiki/wiki?46635) | [Module Tags property](https://wiki.genexus.com/commwiki/wiki?46636) | [Module Version property](https://wiki.genexus.com/commwiki/wiki?46755) | [Toc:Modules](https://wiki.genexus.com/commwiki/wiki?22414) |
| [Modules Server](https://wiki.genexus.com/commwiki/wiki?45933) | [Modules Server (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55061) | [MSBuild Tasks](https://wiki.genexus.com/commwiki/wiki?3908) | [MSBuild Tasks (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53867) |
| [MSBuild Tasks (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54112) | [Object Visibility property](https://wiki.genexus.com/commwiki/wiki?22473) | [Package Module with database access for Solutions extensibility scenarios](https://wiki.genexus.com/commwiki/wiki?42900) | [Package Name property](https://wiki.genexus.com/commwiki/wiki?46759) |
| [Packaged Module Management Error Codes and messages](https://wiki.genexus.com/commwiki/wiki?46761) | [Updating Unanimo](https://wiki.genexus.com/commwiki/wiki?52180) |

---
