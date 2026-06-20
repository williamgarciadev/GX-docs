---
title: "HowTo: Deploy an application to IBM Cloud"
source_id: 32150
source_url: https://wiki.genexus.com/commwiki/wiki?32150
genexus_version: "18"
---

# HowTo: Deploy an application to IBM Cloud

The purpose of this article is to explain the necessary steps to deploy an application to IBM Cloud. By using the [Deploy Applications tool](https://wiki.genexus.com/commwiki/wiki?32092), it is possible to run Java applications on [IBM Cloud](https://www.ibm.com/cloud).

### [Prerequisites:](#Prerequisites%3A)

A Cloud Foundry app using the IBM Cloud console needs to be defined. See [Deploying to IBM Cloud prerequisites](https://wiki.genexus.com/commwiki/wiki?26766,,) for detailed information on this topic.

### [Steps to deploy to IBM Cloud](#Steps+to+deploy+to+IBM+Cloud)

**1.** Before making a deployment, you must configure your Data Store to connect to the database. See [Configuring a GeneXus environment to be deployed on IBM Cloud](https://wiki.genexus.com/commwiki/wiki?28043,,).

**2.** Run a Build All.

**3.** Go to the Build menu and select the Deploy Application option.  
`[imagen omitida: wiki id 32151]`

**4.** On the Deployment screen:

**1.** Select the Main objects to be included in the deployment.  
`[imagen omitida: wiki id 32152]`

**2.** In Target, select the option "IBM Cloud (Cloud Foundry)" (\*).

**3.** Set the following properties as indicated below:

* User: Enter your IBM Cloud account.
* Password: Enter your password.
* Organization: Associated to the Cloud account.
* Space: Defined for the IBM Cloud organization.
* Application: The Cloud Foundry application previously defined (step 1)

After selecting the main objects and configuring the necessary properties for the automatic deployment, press the Deploy button. It will build the WAR package, as well as upload and deploy it in IBM Cloud.

You'll see an output similar to the following:

```
API endpoint:   https://api.ng.bluemix.net (API version: 2.54.0)
  User:           sjuarez@genexus.com
  Org:            genexus.com
  Space:        GENEXUS-INVESTIGACION
Deploy:
  cf push SummerReading -b liberty-for-java -p C:\Models\SummerReading2\SummerReading2\Deploy\JavaMySQL013\Bluemix\20160826102928\..\SummerReading2_20160826102928.war
  Updating app SummerReading in org genexus.com / space GENEXUS-INVESTIGACION as sjuarez@genexus.com...
  OK
  
  Uploading SummerReading...

  Done uploading
  
  Stopping app SummerReading in org genexus.com / space GENEXUS-INVESTIGACION as sjuarez@genexus.com...
  OK
  
  Starting app SummerReading in org genexus.com / space GENEXUS-INVESTIGACION as sjuarez@genexus.com...
  -----> Downloaded app package (21M)
  -----> Downloaded app buildpack cache (336K)
```

You can check the Application URL, Status and Configuration from the IBM Cloud console.

For example, the URL could be: https://summerreading.mybluemix.net/servlet/com.summerreading2.patternconsole.mainconsolepanel.

`[imagen omitida: wiki id 32153]`

If you've selected the "Only Package" checkbox, the WAR package is copied to the local file system, from where you can [deploy it manually to IBM Cloud](https://wiki.genexus.com/commwiki/wiki?28044,,).

### [See Also](#See+Also)

[here](https://developer.ibm.com/bluemix/2014/07/10/monitoring-liberty-bluemix-jconsole/#) for monitoring a java application on IBM Cloud, with [JMX](https://wiki.genexus.com/commwiki/wiki?18873,,).

(\*) IBM Cloud was formerly known as IBM Bluemix


|  |
| --- |
| **Backlinks** |
| [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Toc:Application Deployment tool (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54334) | [Application property](https://wiki.genexus.com/commwiki/wiki?45922) |
| [Deploy Application Targets](https://wiki.genexus.com/commwiki/wiki?42079) | [IBM Password property](https://wiki.genexus.com/commwiki/wiki?45931) | [IBM User property](https://wiki.genexus.com/commwiki/wiki?45930) |
| [Organization property](https://wiki.genexus.com/commwiki/wiki?45920) | [Space property](https://wiki.genexus.com/commwiki/wiki?45921) |

---
