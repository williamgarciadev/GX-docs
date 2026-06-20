---
title: "Application Deployment tool (GeneXus 18 Upgrade 2 or prior)"
source_id: 54334
source_url: https://wiki.genexus.com/commwiki/wiki?54334
genexus_version: "18"
---

# Application Deployment tool (GeneXus 18 Upgrade 2 or prior)

By selecting **Build > Deploy Application** in the GeneXus main menu, you can access the **Application Deployment tool** which provides the following features:

* Local Deployment; it lets you package web applications. That is to say, you package Web objects and Services and get a .zip, .war, .ear, etc. with the corresponding classes, libraries, and resources to be installed in Tomcat, Websphere, JBOSS, IIS, or any Web Server of your favorite Infrastructure as a Service or Hosting providers.
* Docker Containers Deployment; it lets you build Docker images with your application.
* Cloud Deployment; it lets you deploy those packages to the most popular Platform as a Service ([PaaS](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?32096,,)) Cloud Providers (i.e., AWS Elastic Beanstalk, Google App Engine, IBM Bluemix, Microsoft Azure, SAP Cloud Platform) or to Serverless Platforms (i.e., AWS Lambda & API Gateway).
* Package batch processes. That is to say, you package command line Procedures and get .zip or .jar files with the corresponding classes, libraries, and resources. Command line procedures can also be deployed to Serverless Platforms (as AWS Lambda Functions).

The Application Deployment tool is extensible and customizable. You can access the scripts [here](https://github.com/genexuslabs/deployment-targets).  
The options available through the UI are just a part of all those available through [Application Deployment MSBuild tasks](https://wiki.genexus.com/commwiki/wiki?42073).

Below you will find a guide through the basic concepts. There may be additional considerations, specific to the platforms and clouds which may be covered in the related documents.

* [Select what you want to deploy](#Select+what+you+want+to+deploy)
* [Security](#Security)

+ [GAM](#GAM)

* [Deployment of a Java application to Tomcat, Websphere, JBoss, etc.](#Deployment+of+a+Java+application+to+Tomcat%2C+Websphere%2C+JBoss%2C+etc.)
* [Deployment of a .NET application to IIS](#Deployment+of+a+.NET+application+to+IIS)
* [Deployment of applications to Docker Containers](#Deployment+of+applications+to+Docker+Containers)
* [Deployment of applications to the Cloud ([PaaS](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?32096,,))](#Deployment+of+applications+to+the+Cloud+%2832096%29)
* [Deployment of Batch processes](#Deployment+of+Batch+processes)
* [EAR Deployment](#EAR+Deployment)
* [Deployment of additional files and directories](#Deployment+of+additional+files+and+directories)
* [How to exclude objects from the Deployment unit](#How+to+exclude+objects+from+the+Deployment+unit)
* [FAQ](#FAQ)

+ [1. Where are the packages created?](#1.+Where+are+the+packages+created%3F)
+ [2. How intelligent is it? I mean, will it package every file or directory set in the classpath property?](#2.+How+intelligent+is+it%3F+I+mean%2C+will+it+package+every+file+or+directory+set+in+the+classpath+property%3F)
+ [3. My app uses Query Viewer, doesn't it?](#3.+My+app+uses+Query+Viewer%2C+doesn%27t+it%3F)
+ [4. What about GAM?](#4.+What+about+GAM%3F)
+ [5. Does it deploy the GeneXus Flow Inbox and its API?](#5.+Does+it+deploy+the+GeneXus+Flow+Inbox+and+its+API%3F)
+ [6. How do I deploy the objects referenced by my business processes?](#6.+How+do+I+deploy+the+objects+referenced+by+my+business+processes%3F)
+ [7. How do I create a deployment package for the Reorganization?](#7.+How+do+I+create+a+deployment+package+for+the+Reorganization%3F)
+ [8. Does GeneXus provide some spaces in the Cloud for prototyping?](#8.+Does+GeneXus+provide+some+spaces+in+the+Cloud+for+prototyping%3F)

### [Select what you want to deploy](#Select+what+you+want+to+deploy)

This is the first step.   
The 'Add' / 'Clear' buttons let you add or remove objects.  
By just selecting the main object, all the called ones will be included automatically (those that don't appear in the list).  
Only the objects available for selection in a [Deployment Unit object](https://wiki.genexus.com/commwiki/wiki?38886) can be selected.

`[imagen omitida: wiki id 36798]`

In case of selecting one or more Native Mobile main objects to be deployed, the deployment will include all the server-side components that the application requires, including all the necessary REST services and also the application metadata files as indicated in the [App Update](https://wiki.genexus.com/commwiki/wiki?46540) and [Enable KBN](https://wiki.genexus.com/commwiki/wiki?46541) properties. It doesn't deploy the Android or Apple application binaries (.apk or .ipa files), and there is no connection with the application stores.

**Notes**:

* This only deploys the Web or Application Server components; it doesn't deploy the Database. See [Export Reorganization](https://wiki.genexus.com/commwiki/wiki?34476) or the FAQ below for more information and other options.
* If you want to deploy the GXflow Inbox and its API the [Include GXflow backoffice property](https://wiki.genexus.com/commwiki/wiki?49569) must be True and a Business Process Diagram must be included in the deployment. See [HowTo: Deploy a Workflow-based Application](https://wiki.genexus.com/commwiki/wiki?19848) for more information.

### [Security](#Security)

For additional security, you may change the [Application Encryption Key property](https://wiki.genexus.com/commwiki/wiki?36909).

#### [GAM](#GAM)

When the [Enable Integrated Security property](https://wiki.genexus.com/commwiki/wiki?14706) is set to TRUE, the [Include GAM Backend property](https://wiki.genexus.com/commwiki/wiki?44996) will be shown. If the Include GAM Backend property is set to TRUE, the GAM Backend files will be included in the package. Otherwise, they will not be included.

You can save your selection into a [Deployment Unit object](https://wiki.genexus.com/commwiki/wiki?38886) or select an existing one. If you don't choose any Deployment Unit, a default one will be created containing the objects you chose to deploy.

### [Deployment of a Java application to Tomcat, Websphere, JBoss, etc.](#Deployment+of+a+Java+application+to+Tomcat%2C+Websphere%2C+JBoss%2C+etc.)

Provided you selected Web or Smart Devices objects to deploy, the Deploy button creates a .war package with the required binaries and resources configuring it, so that you can deploy it to the Web Application Servers that support the following:

* Generic Servlets 3.0 (i.e. Apache Tomcat 7, WAS 8.x)
* Generic Servlets 3.1
* Generic Servlets 5.0 (i.e. Tomcat 10)
* JBOSS (Enterprise Java Beans)
* Tomcat 8.x
* Tomcat 10.x (it adds support to [URL Rewrite](https://wiki.genexus.com/commwiki/wiki?46523) rules)
* WebSphere (Enterprise Java Beans)

**Notes:**

* Tomcat 8.x uses Generic servlets Specification 3.1. Choose Tomcat 8.x target when your application supports file download. Ref.: [SAC 41714](https://www.genexus.com/developers/websac?,,,41714), [Apache Tomcat Versions](https://tomcat.apache.org/whichversion.html)
* In Jboss, when restarting it, it will delete and redeploy the war files, so if there were some changes made in the files of the deployed application they will be lost (unless updating the .war file with the new changes or reconfiguring Jboss to not redeploy the war files).

Select Target Local and choose one of the available application servers of the list, then click on 'Deploy.'

### [Deployment of a .NET application to IIS](#Deployment+of+a+.NET+application+to+IIS)

Provided you selected Web or Smart Devices objects to deploy, the Deploy button creates a .zip package with the required binaries and resources configuring it so that you can deploy it to the following Web Application Servers:

* IIS 7
* IIS8 (or higher)

Select Target Local and choose one of the available application servers of the list, then click on 'Deploy.'

### [Deployment of applications to Docker Containers](#Deployment+of+applications+to+Docker+Containers)

When you select the Target 'Docker Image,' GeneXus creates a Docker image with your application so that you can deploy it. More information in [HowTo: Deploy an Application to Docker](https://wiki.genexus.com/commwiki/wiki?36951).

### [Deployment of applications to the Cloud ([PaaS](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?32096,,))](#Deployment+of+applications+to+the+Cloud+%28com.gxwiki.wiki%3F32096%2CPaaS+PaaS%29)

Provided you selected Web or Smart Devices objects to deploy, and Target other than 'Local' or 'Docker Image,' the 'Deploy' button creates a package with the required binaries and resources so that it can be deployed to the Cloud. Finally, it deploys the package to the cloud with the credentials and options you set in the Deployment Properties.

`[imagen omitida: wiki id 32099]`

**Warning**: To just create the package, select the 'Only package' checkbox.

Available Cloud Targets for .NET: AWS Elastic Beanstalk, Microsoft Azure WebApp

Available Cloud Targets for Java: AWS Elastic Beanstalk, Google App Engine, IBM Bluemix, SAP Cloud Platform, AWS Serverless, AWS Lambda Function, Microsoft Azure WebApp

Available Cloud Targets for .Net Core: Microsoft Azure WebApp

### [Deployment of Batch processes](#Deployment+of+Batch+processes)

Provided you select only one or multiple procedures (Main Object = True, Call Protocol = Command Line or Internal, Expose as Web service = False) and Target = Local, the 'Deploy' button creates a package (.zip or .jar) with the required binaries and resources to run it.

### [EAR Deployment](#EAR+Deployment)

If some selected object (or a called one) is an [EJB](https://wiki.genexus.com/commwiki/wiki?1818), the Deployment tool creates an .ear (Enterprise Archive Resource) file.  
The generated EAR has one web application with all the servlets and static contents, one EJB application with all the EJB defined, and all the JAR files required by the application.

### [Deployment of additional files and directories](#Deployment+of+additional+files+and+directories)

To include extra files in the deployment package, you can

* Select a [File object](https://wiki.genexus.com/commwiki/wiki?5852). Note that [Extract property](https://wiki.genexus.com/commwiki/wiki?13280) has to be set for that File so that the deployment tool can take it from the path set in the 'Extract to path' property and include it in the deployment package.
* Create or Change the <KB Directory>\<Environment Target path>\web\<Deployment Unit Object Name>\_user.gxdproj setting the Files or Directories to include. (\*). See [Customize GeneXus Deployment capabilities](https://wiki.genexus.com/commwiki/wiki?45672) for more information.

If you need to modify the configuration files of the deploying packages (web.xml in Java and web.config in .Net) but you do not want to create a new configuration file, you can modify the templates in the Genexus directory under ApplicationServers\Template (JavaWeb\Generic\_Servlet\_Base.stg for Java and \CsharpWeb\IIS\_base.stg for .Net).

(\*) The name of the file user.gxdproj changed to <Deployment Unit Object Name>\_user.gxdproj in [GeneXus 16 upgrade 8](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?44913,,) in order to be able to deploy different files and directories to each Deployment Unit.

### [How to exclude objects from the Deployment unit](#How+to+exclude+objects+from+the+Deployment+unit)

Create or Change the <KB Directory>\<Environment Target path>\web\<Deployment Unit Object Name>\_user.gxdproj setting the Files or Directories to exclude. See [Customize GeneXus Deployment capabilities](https://wiki.genexus.com/commwiki/wiki?45672) for more information.

### [FAQ](#FAQ)

#### [1. Where are the packages created?](#1.+Where+are+the+packages+created%3F)

Look at the details in the output window. The packages are typically created under the following path: '<KB Directory>\<Environment Directory>\Deploy\<Target>\<Deployment Unit Name>\<TimeStamp>\'.Use Tools / Explore Target Environment Directory and go to the parent folder, you will see the Deploy folder there.

#### [2. How intelligent is it? I mean, will it package every file or directory set in the classpath property?](#2.+How+intelligent+is+it%3F+I+mean%2C+will+it+package+every+file+or+directory+set+in+the+classpath+property%3F)

No, GeneXus + [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) make up a smart team ;-). It only takes the drivers corresponding to your Environment and the libraries that your application uses (i.e. if it doesn't create Excel files, it doesn't include the POI library, etc.). That said, if you have additional files (like jars) that need to be deployed with your app, you'll have to add them as [files](https://wiki.genexus.com/commwiki/wiki?5852) in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) and add those files to the Deploy Dialog, just as you would with a regular main object. For more information about this, read [Adding additional files to an application package](https://wiki.genexus.com/commwiki/wiki?35361)

#### [3. My app uses Query Viewer, doesn't it?](#3.+My+app+uses+Query+Viewer%2C+doesn%27t+it%3F)

Yes, if the selected objects use the Query Viewer Control, it takes the corresponding binaries and resources for the Query Viewer User Control and the referenced Query objects.

#### [4. What about GAM?](#4.+What+about+GAM%3F)

If the [Enable Integrated Security property](https://wiki.genexus.com/commwiki/wiki?14706) is set to True, it takes the corresponding binaries and resources for the GAM API. If you need to package the GAM Example Web Objects, add the GAMHome to your list. It doesn't initialize or populate GAM's tables with the required permissions, roles, etc. Read [GAM - Applications deployment](https://wiki.genexus.com/commwiki/wiki?21219) for information about that.

#### [5. Does it deploy the GeneXus Flow Inbox and its API?](#5.+Does+it+deploy+the+GeneXus+Flow+Inbox+and+its+API%3F)

Yes. If the KB Version has a BPM Diagram and at least one BPM Diagram is included in the deployment, it takes the corresponding binaries and resources.

#### [6. How do I deploy the objects referenced by my business processes?](#6.+How+do+I+deploy+the+objects+referenced+by+my+business+processes%3F)

Select a Business Diagram and the objects it uses will be deployed! Note: It doesn't impact workflow tables! Read [HowTo: Deploy a Workflow-based Application](https://wiki.genexus.com/commwiki/wiki?19848) to do that.

#### [7. How do I create a deployment package for the Reorganization?](#7.+How+do+I+create+a+deployment+package+for+the+Reorganization%3F)

This option is available in Build / Export Reorganization. More Information at [Export Reorganization](https://wiki.genexus.com/commwiki/wiki?34476).

#### [8. Does GeneXus provide some spaces in the Cloud for prototyping?](#8.+Does+GeneXus+provide+some+spaces+in+the+Cloud+for+prototyping%3F)

Oh, you didn't know? Yes, since 2012 there are [Servers available for Cloud prototyping](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?26157,,)! Use [Deploy to cloud property](https://wiki.genexus.com/commwiki/wiki?15041), press F5 and you're prototyping on the cloud for free.


* [Deploy Application Targets](https://wiki.genexus.com/commwiki/wiki?42079)
* Deploy to PaaS
  + [IBM Cloud](https://wiki.genexus.com/commwiki/wiki?32150)
  + [Azure Web App](https://wiki.genexus.com/commwiki/wiki?31457)
  + [SAP Cloud Platform](https://wiki.genexus.com/commwiki/wiki?32059)
  + [AWS Elastic Beanstalk](https://wiki.genexus.com/commwiki/wiki?32104)
  + [Google App Engine](https://wiki.genexus.com/commwiki/wiki?32211)
* Deploy Serverless
  + Serverless Functions
    - [AWS Lambda Functions](https://wiki.genexus.com/commwiki/wiki?51514)
      * [HowTo: Deploy to AWS Lambda Function](https://wiki.genexus.com/commwiki/wiki?51533)
      * [AWS Queue triggered functions](https://wiki.genexus.com/commwiki/wiki?51541)
      * [AWS EventBridge triggered functions](https://wiki.genexus.com/commwiki/wiki?51547)
      * [Lambda Timer-triggered functions](https://wiki.genexus.com/commwiki/wiki?51550)
      * [Lambda HTTP-triggered functions](https://wiki.genexus.com/commwiki/wiki?51552)
    - [Azure Functions](https://wiki.genexus.com/commwiki/wiki?47430)
      * [HowTo: Deploy as Azure Functions](https://wiki.genexus.com/commwiki/wiki?49351)
      * [Azure timer triggered functions](https://wiki.genexus.com/commwiki/wiki?49264)
      * [Azure Http-triggered functions](https://wiki.genexus.com/commwiki/wiki?49266)
      * [Service Bus and Queue Storage triggered Azure functions](https://wiki.genexus.com/commwiki/wiki?49355)
      * [Create a GX procedure as a serverless function](https://wiki.genexus.com/commwiki/wiki?47729)
      * [HowTo: Monitor Azure Functions](https://wiki.genexus.com/commwiki/wiki?49260)
  + Serverless Service Backend
    - [HowTo: Deploy Angular Frontend applications using serverless backend](https://wiki.genexus.com/commwiki/wiki?49963)
    - AWS Serveless
      * [Deploy mobile services to AWS Serverless using AWS Lambda and AWS API Gateway](https://wiki.genexus.com/commwiki/wiki?35355)
    - Azure Serveless
      * [Deploy to Azure Serverless using API Management](https://wiki.genexus.com/commwiki/wiki?49107)
      * [HowTo: MSBuild tasks for Azure serverless deployment](https://wiki.genexus.com/commwiki/wiki?51440)
      * [HowTo: Deploy static files to Azure Storage in Serverless deploy](https://wiki.genexus.com/commwiki/wiki?50142)
      * [HowTo: Use GAM in Azure serverless architecture](https://wiki.genexus.com/commwiki/wiki?53363)
* Containerization
  + [Deploy to Docker](https://wiki.genexus.com/commwiki/wiki?36951)
    - [Deploy to Docker MSBuild task](https://wiki.genexus.com/commwiki/wiki?47839)
    - [Deploy a command-line procedure to Docker containers](https://wiki.genexus.com/commwiki/wiki?51121)
    - [Deploy docker image to Openshift](https://wiki.genexus.com/commwiki/wiki?51124)
    - [Deploy to docker containers: taking properties from configuration file](https://wiki.genexus.com/commwiki/wiki?51122)
  + [Deploy to a Kubernetes cluster](https://wiki.genexus.com/commwiki/wiki?45416)
    - [Deploy to AKS](https://wiki.genexus.com/commwiki/wiki?46730)
* Deploy Front end applications
  + [Frontend applications deployment](https://wiki.genexus.com/commwiki/wiki?51105)
    - [HowTo: Deploy Frontend applications to Docker containers](https://wiki.genexus.com/commwiki/wiki?51104)
      * [HowTo: Deploy Static Front end to Docker using MSBuild Tasks](https://wiki.genexus.com/commwiki/wiki?51115)
    - [Deploy to Cloud Provider Object Storage](https://wiki.genexus.com/commwiki/wiki?49877)
      * [HowTo: Deploy Frontend applications to Azure Blob Storage](https://wiki.genexus.com/commwiki/wiki?49878)
* MSBuild tasks
  + [Application Deployment MSBuild tasks](https://wiki.genexus.com/commwiki/wiki?42073)
* Application Configuration
  + [Application Configuration using Environment Variables](https://wiki.genexus.com/commwiki/wiki?39459)
    - [Application Configuration using Environment Variables in .NET and Java](https://wiki.genexus.com/commwiki/wiki?53336)
    - [Application Configuration using Environment Variables in Cloud Services](https://wiki.genexus.com/commwiki/wiki?53339)
    - [Log settings with environment variables](https://wiki.genexus.com/commwiki/wiki?53361)
  + [Runtime external object](https://wiki.genexus.com/commwiki/wiki?33076)
  + [Tips for deploying an application that references External Objects](https://wiki.genexus.com/commwiki/wiki?50961)
  + [CORS settings with environment variables](https://wiki.genexus.com/commwiki/wiki?52127)

---
