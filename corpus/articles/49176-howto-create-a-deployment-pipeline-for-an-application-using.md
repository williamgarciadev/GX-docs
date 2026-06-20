---
title: "HowTo: Create a deployment pipeline for an application using GXflow"
source_id: 49176
source_url: https://wiki.genexus.com/commwiki/wiki?49176
genexus_version: "18"
---

# HowTo: Create a deployment pipeline for an application using GXflow

In this article, you will find the steps to create a deployment pipeline when using [GXflow](https://wiki.genexus.com/commwiki/wiki?4179,,) in your application.

First, it describes the scenario where the [Deploy to Cloud](https://wiki.genexus.com/commwiki/wiki?15041) option is used for a development environment. Then, the scenario of a test or production environment where you deploy on your own web and database server.

## [Pipeline with Deploy to Cloud](#Pipeline+with+Deploy+to+Cloud)

Following the steps provided in the article [CI integrated to GeneXus and GXserver](https://wiki.genexus.com/commwiki/wiki?46966), you can create a pipeline with the “Deploy to Cloud” option. In this way, your application will be automatically built and run on a certain URL, including GXflow.

## [Pipeline to deploy on your own web and database server](#Pipeline+to+deploy+on+your+own+web+and+database+server)

Three stages will be described to perform the process in a fully automated way. They are carried out together; for example, using a Jenkins Job:

### [Step 1](#Step+1)

Build the corresponding [KB](https://wiki.genexus.com/commwiki/wiki?2428) using [GXServer](https://wiki.genexus.com/commwiki/wiki?31337,,) as in the previous step, only that now the “Deploy to Cloud” option has to be cleared. Here, you can use your own databases and use only one for the GXflow tables. Below is how to do so:

* Create the pipeline to be used in GXServer with the “Deploy to Cloud” option cleared.
* Open the *jenkings.config* file found in your GXServer installation; for example, it could be: “*C:\GeneXusServer\GeneXusServer17\VDir\BinGenexus\Packages\ContinuousIntegration.*”
* Here you will find several “jobs” nodes, one for each pipeline you have in GXServer.
* Under the “friendlyname” tag, find the node that has the name of your new pipeline and change the tag localsettings=”BuildOnly.settings” customsettings=”false” to localsettings=”MySettings.settings” customsettings=”true” (MySettings is just an example, you can use another file name).
* In the folder you downloaded from Git (when you followed the steps in [How to configure GeneXus Server for Continuous Integration](https://wiki.genexus.com/commwiki/wiki?46996)), find the KBSettings folder; for example, it can be located at “*C:\GXJenkins\CIscripts\KBSettings*”. Initially, you will only find these files: “BuildOnly.setting” and “DeployToCloud.settings.”
* Create a new *.settings* file. According to the previous example, it would be “MySettings.settings.”
* In it, copy the contents of the “BuildOnly.settings” file.
* You will find the following nodes:

```
<DataStoreProperty Include="Database name">
<Datastore>Default</Datastore>
<PropertyName>Database name</PropertyName>
<PropertyValue>EMPTY</PropertyValue>
</DataStoreProperty>
<DataStoreProperty Include="Server name">
<Datastore>Default</Datastore>
<PropertyName>Server name</PropertyName>
<PropertyValue>EMPTY</PropertyValue>
```

* Change the “EMPTY” values to their values (if the database doesn’t exist, it will be created).
* If you are using a database for GXflow only, add the following below the above, also changing the “EMPTY” values.

```
<DataStoreProperty Include="Database name">
<Datastore>GXFLOW</Datastore>
<PropertyName>Database name</PropertyName>
<PropertyValue>EMPTY</PropertyValue>
</DataStoreProperty>
<DataStoreProperty Include="Server name">
<Datastore>GXFLOW</Datastore>
<PropertyName>Server name</PropertyName>
<PropertyValue>EMPTY</PropertyValue>
<Datastore>GXFLOW</Datastore>
</DataStoreProperty>
```

* Finally, in GXServer select the created pipeline for editing and, without doing anything else, select “SAVE.” In this way, the recent changes will be saved.
* In case of an error stating that the jenkins.config file was modified by another program, restart the server.

### [Step 2](#Step+2)

From a deployment unit already created, the *.war* or *.zip* file will be generated depending on your Environment. To deploy your application, you will need to call two MSBuild tasks. They are explained together with their parameters in [Application Deployment MSBuild tasks](https://wiki.genexus.com/commwiki/wiki?42073).

In this article, you will find an example of automation with Jenkins: [How to deploy the application using the GeneXus Jenkins Plugin](https://wiki.genexus.com/commwiki/wiki?44704,,).

### [Step 3](#Step+3)

Finally, the second MSBuild task will create the deployment file in the path you have specified. Run it with the web server you use. For example, Docker or Tomcat, depending on the deployment file you have created.

### See Also

[DevOps in GeneXus](https://wiki.genexus.com/commwiki/wiki?38363)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |

---
