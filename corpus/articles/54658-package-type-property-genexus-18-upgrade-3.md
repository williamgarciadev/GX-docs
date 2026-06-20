---
title: "Package Type property (GeneXus 18 Upgrade 3)"
source_id: 54658
source_url: https://wiki.genexus.com/commwiki/wiki?54658
genexus_version: "18"
---

# Package Type property (GeneXus 18 Upgrade 3)

Specifies the contents of the package being created so that the application can be deployed.

### [Values](#Values)

|  |  |
| --- | --- |
| **Binaries** | The package that is created contains the compiled and executable code of the application, along with any necessary dependencies or libraries. |
| **Sources** | The package being created contains the source code for the application, along with any necessary configuration files or static files, etc. |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604)  
**Level:** Deploy Target Options

### [Description](#Description)

The Package Type property is typically used in software development and deployment processes to distinguish between packages containing source code and those containing compiled code. It helps to determine how the package can be used and what steps may be required to use it.

If you simply want to run the application, a package containing the binaries will suffice. Thus, you should configure the property with the Binaries value.

If you need to modify the application code or upload the generated code to a version control system, you will need a package containing the source code. Then you must configure the property with the Sources value.

When you choose the Sources value, the deployment creates a structure with two directories:

* **src:** Contains the generated sources and C-Sharp projects to assemble the binaries.
* **web:**Root directory of the web application. It contains configuration files, images, JavaScripts, styles, and resources in general that the application needs to run.

In the src\build directory, there is a solution file named: <DeploymentUnitName>.sln.

When compiling <DeploymentUnitName>.sln, all the binaries needed to run the application are created in the web\bin directory.

To build those binaries, you just need to execute the command:

```
dotnet publish src\build\<NameDeploymentUnit>.sln --output web\bin
```

**Note**: For [.NET Generator](https://wiki.genexus.com/commwiki/wiki?38604) is supported when the Target is Local or Microsoft Azure Serverless (backend services).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

#### [Uploading the source code of an application to a source code management system such as GitHub.](#Uploading+the+source+code+of+an+application+to+a+source+code+management+system+such+as+GitHub.)

In this case, a package containing the source code of the application is usually created. This package is uploaded to GitHub, where other developers can access the code. In this scenario, the Package Type property would be set to 'Sources'. This is because the package contains the source code for the application, which can be used to build the application later. It can then be built for a specific platform, such as Linux or Windows. More information in [SAC #52557](https://www.genexus.com/developers/websac?en,,,52557).

#### [Integrating the build process into an organization's existing pipeline with certain quality rules.](#Integrating+the+build+process+into+an+organization%27s+existing+pipeline+with+certain+quality+rules.)

When an organization wants to integrate the build process of a software application into its existing deployment pipeline, it usually creates a package containing the source code of the application along with the necessary build scripts or configuration files. This package is then integrated into the organization's build process, where it can be compiled, tested, and deployed. In addition, the organization may have certain quality standards and static code analysis as part of its build process that the application must meet before being deployed. In this case, the Package Type property would be set to 'Sources'.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?53853).
