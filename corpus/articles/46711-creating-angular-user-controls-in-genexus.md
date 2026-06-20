---
title: "Creating Angular User Controls in GeneXus"
source_id: 46711
source_url: https://wiki.genexus.com/commwiki/wiki?46711
genexus_version: "18"
---

# Creating Angular User Controls in GeneXus

This document is intended for developers who are already familiar with the [User Control object](https://wiki.genexus.com/commwiki/wiki?39356) and its basic concepts and want to create User Controls for [Angular](https://wiki.genexus.com/commwiki/wiki?42539).

In addition to the GeneXus [Java](https://wiki.genexus.com/commwiki/wiki?12258), [.NET](https://wiki.genexus.com/commwiki/wiki?38604), and [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892) generators that generate not only the applications' front end but also their back end, the [Angular generator](https://wiki.genexus.com/commwiki/wiki?42550) is exclusively for front-end generation.

Due to the current diversity of structural frameworks (React, Vue, etc.), and to extend the power of GeneXus for generating user interfaces, it is necessary to use User Control objects to integrate third-party controls in the applications generated with this generator.

## [Types of possible integrations](#Types+of+possible+integrations)

The User Control in Angular allows integrating a wide range of third-party controls, which can be divided into two types:

* Native components of the framework (for example, [Angular Material](https://material.angular.io/guide/getting-started) or [Material-UI](https://material-ui.com/))
* Vanilla HTML+CSS+JavaScript (for example, a Bootstrap control)

## [Compatibility with Java, .NET, or .NET Framework front ends](#Compatibility+with+Java%2C+.NET%2C+or+.NET+Framework+front+ends)

To indicate that a UC Object is built for a particular framework, the “target” attribute in the “Definition” tag must be used. This same attribute is used in Java, .NET, or .NET Framework front ends to declare that the UC Object is for [SAPUI5](https://wiki.genexus.com/commwiki/wiki?45691).  
For example:

```
<Definition target="Angular">
...
</Definition>
```

If the attribute is not specified, it will be assumed that the UC Object can be consumed in web layouts (e.g.: [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)) in Java, .NET, or .NET Framework generators.

## [Mustache vs Angular substitution markers](#Mustache+vs+Angular+substitution+markers)

When developing a User Control in Angular, you need to include the following code in the screen template if you are going to use substitution markup in the HTML:

```
{{=<% %>=}}
```

The screen templates are written in Mustache markup. The issue with this is that the substitution markers for Mustache and Angular elements are the same.  
What this instruction does is replace the Mustache markers so that instead of being like this: {{ }}, they become like this: <% %>.

## [References to external resources](#References+to+external+resources)

Front-end generators such as Angular add more advanced ways to include external resources, using the JavaScript import statement. This statement can be used both to include JavaScript modules and to include, through a bundler such as webpack, other types of resources such as images, SVG files, or style sheets.

To include native components, the syntax supports these methods to import resources:

* `import { Component } from "package-name";`
* `import Component from "package-name";`
* `import "package-name";`

They are indicated through a `<script>` block, where through the `"When='import'"` attribute, it can be indicated that the code contained there must be inserted at the beginning of the JavaScript module of the component to be generated, or, specifically in the case of the Angular generator, in the `app.module.ts` and `main.ts` files.

The import options available are as follows:

|  |  |
| --- | --- |
| ``` <script When="import">    import { ViewChild } from "@angular/core";           import { UIChart } from "primeng/chart"; </script> ``` | The import code is placed at the beginning of the JavaScript module of the generated User Control. |
| ``` <script When="import" ng-location="Module">    import "chart.js"; </script> ``` | Since the <script> tag has the ng-location attribute set to Module, the import code is placed in the Angular module that contains the component. Currently, two modules are generated (app.module.ts and shared.module.ts), so the code is placed in both locations. |
| ``` <script When="import" ng-location="Module" ng-module-imports="ChartModule">    import {ChartModule} from 'primeng/chart';    import "chart.js"; </script> ``` | Since the <script> tag has the ng-location attribute set to Module, the import code is placed in the Angular module that contains the component. Currently, two modules are generated (app.module.ts and shared.module.ts), so the code is placed in both locations.  Also, since the ng-module-imports attribute was specified, ChartModule is added to the imports list of the module. The ng-module-imports attribute supports a list of modules to be imported, separated by commas. |

In turn, it is possible to declare which packages should be installed as dependencies. This is achieved by adding the <dependency> block in the control definition.  
For example:

```
  <Dependency name="primeng" version="^9.1.0"/>
  <Dependency name="primeicons" version="^4.0.0" />
  <Dependency name="chart.js" version="^2.7.0" />
```

Both the package name and version must be specified, using the name and version attributes, respectively. The value of the version attribute must be compatible with [node-semver](https://github.com/npm/node-semver).

This package reference will be added to the generated file "package.json" on your Angular project.  
To install that dependency, go to the root of your Angular-generated project and via command line do this:

```
C:\Models\<GeneXusProject>\<Environment>\mobile\Angular\<main_panel> npm install
```

### [Angular Schematics](#Angular+Schematics)

In the case of the Angular generator, some packages require the execution of schematics to be correctly included (the ng add command must be used to add them).  
To specify that Angular Schematics should be used to import the dependency, the ng-schematics attribute should be set to true:

```
<dependency name="@angular/material" ng-schematics="true">
```

### [Style sheets](#Style+sheets)

It is possible to declare style sheets to be included using the <style> tag and the path attribute:

```
  <style path="node_modules/primeicons/primeicons.css" />
  <style path="node_modules/primeng/resources/themes/nova-light/theme.css" />
  <style path="node_modules/primeng/resources/primeng.min.css" />
```

The Angular generator incorporates these styles in [the style property of the angular.json file](https://angular.io/guide/workspace-config#style-script-config).

## [Screen Template](#Screen+Template)

In the Angular generator, a new concept has been added in the language of screen templates that allows you to specify whether to use [Angular Interpolation](https://angular.io/guide/template-syntax#interpolation-) or not. When you assign a value to an attribute or to the content of a tag, you can use the classic syntax of User Control Objects, with double curly brackets. However, when you want to set an Angular binding with a property (using square brackets in the property name) you cannot use Interpolation. To instruct the template not to use Interpolation, square brackets should be added to the double curly brackets.

For example:

|  |  |
| --- | --- |
| ``` <ion-button color="{{Color}}" {{OnClick}}>{{Caption}}</ion-button> ``` | The value of the Color attribute is made using Interpolation. This is possible because the attribute value is not strongly typed. The same applies to the content, using the Caption property. |
| ``` <p-breadcrumb [model]="{{[Items]}}"></p-breadcrumb> ``` | The value of the model property is strongly typed (it is a JavaScript object). For this reason, it is necessary to use square brackets around the property name (model). Otherwise, Angular will serialize the value of the property to a string. Since the model property has square brackets, the value cannot use Interpolation (it gives a syntax error).  For that reason, to pass the value of the Items property, instead of using only double curly brackets ( {{Items}} ), square brackets are added ( {{[Items]}} ). |

## [Events](#Events)

The declaration of events of UC Objects is fully supported. Now it is also possible to declare parameters, using the Parameters attribute in the Event tag:

```
<Event Name="OnActiveIndexChange" Parameters="Numeric" />
```

The value of the Parameters attribute must be a comma-separated list with the list of data types of the parameters received by the event.

## [Scripts and methods](#Scripts+and+methods)

The inclusion of scripts and methods is also fully supported, and an additional attribute called ng-location has also been included. When you want a script to be incorporated into the body of the class generated for the User Control component, it is assigned the ClassBody value. For example, to add a member to the component class you can do the following:

```
<script Name="ViewChild" When="BeforeShow" ng-location="ClassBody">
   @ViewChild("chart", { static: false }) chart: UIChart;
</script>
```

## [See Also](#See+Also)

[HowTo: Create Angular User Controls in GeneXus](https://wiki.genexus.com/commwiki/wiki?57330)


|  |
| --- |
| **Backlinks** |
| [Toc:Angular Application Development](https://wiki.genexus.com/commwiki/wiki?42539) | [Category:User Control object](https://wiki.genexus.com/commwiki/wiki?39356) |

---
