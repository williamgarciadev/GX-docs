---
title: "URL Rewrite object"
source_id: 46523
source_url: https://wiki.genexus.com/commwiki/wiki?46523
genexus_version: "18"
---

# URL Rewrite object

The URL Rewrite object defines friendly URLs, intended to improve the usability and accessibility of a website.

It lets you define URLs and the corresponding mapping to objects with their parameters.

Defining friendly URLs lets you separate the interface from the implementation:

* It helps you to make it SEO friendly
* The defined URLs are independent of the object names and their modularization in the KB
* The defined URLs are independent of the chosen generator, a feature that adds flexibility and reduces lock-in to a specific generator (.NET, .NET Framework, or Java).

The object has the following parts:

* Rewrite Rules
* Variables
* Help
* Documentation

### [Rewrite Rules](#Rewrite+Rules)

This is the main part of a URL Rewrite Object, as it lets you define the mappings (also called rewrite rules).

Each mapping consists of a part on the left where the URL (or part of it) is specified, and on the right side, the object and its parameters are referenced. Mappings are separated by a semicolon.

```
home                                 => Home; 

core/clients                        => Core.WWClient;
core/clients/{&ClientId}/{&Mode}    => Core.Client(&Mode,&ClientId);
core/clients/{&ClientId}            => Core.ViewClient(&ClientId);
```

The above mappings result in URLs like the following:

* http://www.example.com/home
* http://www.example.com/core/clients
* http://www.example.com/core/clients/1/UPD
* http://www.example.com/core/client/1

### [Considerations](#Considerations)

* You do not need to reference all the parameters
* Creating a URL Rewrite object changes the behavior of the [Link Function](https://wiki.genexus.com/commwiki/wiki?8444). Instead of returning document-relative URLs, it returns server-relative URLs when a URL Rewrite object exists. This can introduce breaking changes in your code; for example, if you concatenate the resulting string with another to create an absolute URL.
* [API object](https://wiki.genexus.com/commwiki/wiki?46151) is not supported.

### [Restrictions](#Restrictions)

To use this feature, some restrictions apply

* Parameters can only be mapped on objects where the [Encrypt URL parameters property](https://wiki.genexus.com/commwiki/wiki?8068) is set to 'No' and if the [Parameters Style property for Environments](https://wiki.genexus.com/commwiki/wiki?46404) is set to 'Named'.
* The [Web User Experience property](https://wiki.genexus.com/commwiki/wiki?22449) must be set to 'Smooth' in objects affected by these rules.

## [Samples](#Samples)

#### [1) Partial parameter references](#1%29+Partial+parameter+references)

Missing parameters will be added to the query string:

```
core/clients/{&ClientId}    => Core.Client(&Mode,&ClientId);
```

This result is:

http://www.example.com/core/clients/1?Mode=UPD

when the object is called as follows:

```
Core.Client('UPD',1)
```

#### [2) Object mapping without parameter mapping](#2%29+Object+mapping+without+parameter+mapping)

You can write

core/client => Core.Client;

even if the object Core.Client has a

```
parm(in:&Mode,in:&ClientId)
```

In this sample, when the parameter style is positional, the resulting URL would be as follows:

http://www.example.com/core/client?UPD,1

when the object is called as follows:

```
Core.Client('UPD',1)
```

## [Deployment](#Deployment)

GeneXus automatically deploys all the rules defined in the URL Rewrite objects of the KB when deploying a [Deployment Unit object](https://wiki.genexus.com/commwiki/wiki?38886). This implies that there must be no conflict among rules defined in different objects.

### [Java-specific](#Java-specific)

When deploying to Tomcat 8 or higher, rewrite rules work automatically; however, when you deploy to another Servlet Server, you may need to make extra configurations. For that, take the rules from the urlrewrite.config file to configure the server.

## [Scope](#Scope)

**Generators**: [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)
