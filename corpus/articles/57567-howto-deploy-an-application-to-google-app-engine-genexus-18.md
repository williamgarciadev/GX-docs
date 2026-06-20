---
title: "HowTo: Deploy an application to Google App Engine (GeneXus 18 Upgrade 8)"
source_id: 57567
source_url: https://wiki.genexus.com/commwiki/wiki?57567
genexus_version: "18"
---

# HowTo: Deploy an application to Google App Engine (GeneXus 18 Upgrade 8)

With the [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092), you can run Java applications on [Google App Engine](https://cloud.google.com/appengine/?utm_source=google&utm_medium=cpc&utm_campaign=2015-q2-cloud-na-gcp-bkws-freetrial-en).

**Summary**

* [Prerequisites](#Prerequisites)
* [Steps to deploy to Google App Engine](#Steps+to+deploy+to+Google+App+Engine)
* [Testing the deployment](#Testing+the+deployment)
* [See also](#See+also)

### [Prerequisites](#Prerequisites)

First, you need to [set the Google environment](https://wiki.genexus.com/commwiki/wiki?31733) using the Google management console.

**Important Note**  
  Google no longer supports Google App Engine Java 8 Runtime. For more information, see [Google documentation](https://cloud.google.com/appengine/migration-center/standard/migrate-to-second-gen/java-differences#key-differences).  
  Therefore, applications have to be upgraded to Java 11+ runtimes.

Below are the options available to deploy your app after upgrading to Java 11+.

There are two main options and the recommended one is the second choice, mostly for new applications.

1. Compile your app using Java 11 or Java 17.  
   In this case, as the Jetty version that will be used is 9 (see Google reference [here](https://cloud.google.com/appengine/docs/standard/java-gen2/upgrade-java-runtime)), and it does not support Jakarta, you have to set [Java platform support property](https://wiki.genexus.com/commwiki/wiki?48353) to Java EE.
2. Compile your app using Java 21.  
   In this case, use [Java platform support property](https://wiki.genexus.com/commwiki/wiki?48353) = Jakarta (default value). Jetty version is 12 in this case so it guarantees Jakarta support.

Before deploying your app, you must edit the file *DeploymentTargets\GoogleAppEngine\Templates\appengine-web.xml* under the GeneXus distribution, and make changes according to the Java version you used to compile your app and the Java runtime you will be using.

In the following example, Java 21 was used. In general, you have to replace the runtime for the one you will be using and set the app-engine-apis to TRUE.

```
<?xml version="1.0" encoding="utf-8"?>
<appengine-web-app xmlns="http://appengine.google.com/ns/1.0">
    <runtime>java21</runtime>
    <threadsafe>true</threadsafe>
    <use-google-connector-j>true</use-google-connector-j>
    <sessions-enabled>true</sessions-enabled>
    <app-engine-apis>true</app-engine-apis>
</appengine-web-app>
```

When using Java 21, you must edit the file *DeploymentTargets\GoogleAppEngine\Definition.target* under the GeneXus distribution, and change the Application Server specification version, as shown below.

```
<ApplicationServer>Generic Servlet 6.0</ApplicationServer>
```

### [Steps to deploy to Google App Engine](#Steps+to+deploy+to+Google+App+Engine)

**1.** Select the Main objects to be included in the [Deployment Unit object](https://wiki.genexus.com/commwiki/wiki?38886). Then go through the contextual option "Deploy Application" of the deployment unit just created.

**2.** In Target, select the option "Google App Engine".

**3.** In the Deployment screen, complete the following:

* *Project Id*  
    
  Enter the Project ID as obtained using the Google management console.  
    
  `[imagen omitida: wiki id 49592]`
* *Application version*  
    
  The app version that will be created or replaced by this deployment. If you don't specify a version, one will be generated for you.  
    
  App Engine uses this version identifier to determine whether to create a new version of the app with the given identifier (or replace the version of the app with the given identifier if one already exists). You can test new versions of your app with a URL using "-dot-" as a subdomain separator in the URL; for example, https://VERSION\_ID-dot-default-dot-PROJECT\_ID.REGION\_ID.r.appspot.com. Using the Google Cloud Console, you can select the default version of your app. The default version is loaded when no version, or an invalid version, is specified.

`[imagen omitida: wiki id 49594]`

After selecting the main objects and configuring the necessary properties for the automatic deployment, press the Deploy button.  
It will build the WAR package, as well as upload and deploy it on Google App Engine.

You'll see an output similar to the following:

```
Services to deploy:
descriptor:                  [C:\models\TestDeployGoogle\TestDeployGoogle\Java8\Deploy\GAE\DeploymentUnit1\20211113123339\WEB-INF\appengine-web.xml]
source:                      [C:\models\TestDeployGoogle\TestDeployGoogle\Java8\Deploy\GAE\DeploymentUnit1\20211113123339]
target project:              [deploy-test-331515]
target service:              [default]
target version:              [v2]
target url:                  [https://deploy-test-331515.uc.r.appspot.com]
target service account:      [App Engine default service account]
Beginning deployment of service [default]...
#============================================================#
#= Uploading 4 files to Google Cloud Storage                =#
#============================================================#
File upload done.
Updating service [default]...
.............................................................................................................................done.
Setting traffic split for service [default]...
.....................................done.
Deployed service [default] to [https://deploy-test-331515.uc.r.appspot.com]
You can stream logs from the command line by running:
$ gcloud app logs tail -s default
To view your application in the web browser run:
$ gcloud app browse
Deploying to Google App Engine finished successfully.
```

**Note**: The Application Server used is Generic Servlet 3.1.

### [Testing the deployment](#Testing+the+deployment)

Once deployed, your application runs on the URL **https://<YOUR\_PROJECT\_ID>.appspot.com**.  
Execute the Google console and go through the App Engine panel (Versions option on the left). On the right, you have the list of all the versions deployed and their URL.

`[imagen omitida: wiki id 49593]`

For example: [https://20211113t091926-dot-deploy-test-331515.uc.r.appspot.com/com.testdeploygoogle.webpanel1]

Number **20211113t091926** is the version, deploy-test-331515 is the project ID, and **com.testdeploygoogle** is the [Java package name property](https://wiki.genexus.com/commwiki/wiki?24941) set in the Knowledge Base.

### [See also](#See+also)

[Deploy to Google App Engine - Datastore configuration](https://wiki.genexus.com/commwiki/wiki?49595)
