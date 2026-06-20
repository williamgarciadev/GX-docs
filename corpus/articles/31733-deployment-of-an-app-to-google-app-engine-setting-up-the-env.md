---
title: "Deployment of an app to Google App Engine: setting up the environment"
source_id: 31733
source_url: https://wiki.genexus.com/commwiki/wiki?31733
genexus_version: "18"
---

# Deployment of an app to Google App Engine: setting up the environment

Below are the steps required to deploy a JAVA application to [Google App Engine](https://cloud.google.com/appengine/) (a product of [Google Cloud Platform](https://cloud.google.com/)).

## [Setting up the environment](#Setting+up+the+environment)

The following steps are done using the [console](http://console.cloud.google.com).

### [1. Creating the project](#1.+Creating+the+project)

First, select or create a Cloud Platform Console project. To deploy your app to App Engine, you will need to register a project to create your project ID, which will determine the URL for the app.

### [2. Installing the client tools to deploy the app](#2.+Installing+the+client+tools+to+deploy+the+app)

Download & install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/install).

Important: consider the following notes:

1. After the installation is complete, **make sure you leave the options to start the shell and configure your installation selected. The installer starts a terminal window and runs the gcloud init command.**
2. The default installation doesn't include the App Engine extensions required to deploy an application using gcloud commands.   
   So, you have to execute from a cmd:   
     
   **gcloud components install app-engine-java**

### [3. Setting Permissions](#3.+Setting+Permissions+)

The Owner of the Cloud project must create the App Engine application.

`[imagen omitida: wiki id 49598]`

So, in the machine where you execute the deployment, you have to be logged in as the project owner.  
You can log in executing the following at the command line:

**gcloud auth login**

A web browser opens where Google Clouds SDK asks you for access to the Google account:

`[imagen omitida: wiki id 49597]`  
  
In addition, give **Cloud Build** permission to deploy apps in your project.

Check [this](https://cloud.google.com/appengine/docs/standard/java/tools/uploadinganapp#before_you_begin) document from Google for more information.

### [Ready](#Ready)

Now you are ready to deploy the app to Google App Engine. See [HowTo: Deploy an application to Google App Engine](https://wiki.genexus.com/commwiki/wiki?32211).


|  |
| --- |
| **Backlinks** |
| [HowTo: Deploy an application to Google App Engine](https://wiki.genexus.com/commwiki/wiki?32211) |

---
