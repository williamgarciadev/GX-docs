---
title: "HowTo: Deployment of a Command Line Procedure in Java"
source_id: 55200
source_url: https://wiki.genexus.com/commwiki/wiki?55200
genexus_version: "18"
---

# HowTo: Deployment of a Command Line Procedure in Java

This article shows the steps you must follow to execute a deployment from the Command Line [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) for the [GeneXus Java Generator](https://wiki.genexus.com/commwiki/wiki?12258).

### [Step 1: Command Line Procedure Configuration](#Step+1%3A+Command+Line+Procedure+Configuration)

* Select the Procedure you want to deploy from the command line.
* In the [Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947) of the Procedure, set the "Command Line" option.
* Set the [Main program property](https://wiki.genexus.com/commwiki/wiki?7407) to True.

### [Step 2: Deployment generation](#Step+2%3A+Deployment+generation)

* From the GeneXus Toolbar, go to Build>Deploy Application.
* Choose the "Local" Target to perform a deployment in the local environment.  
  Choose [Package Type](https://wiki.genexus.com/commwiki/wiki?53373) = Binaries.
* Then click on the Deploy button.   
    
  GeneXus will generate the necessary files for deployment, including the .jar file containing your application and its dependencies.  
    
  In the output, you will see the path to the generated .jar file with your application classes:  
    
  `[imagen omitida: wiki id 55236]`  
    
  Therefore, the resulting structure will be as follows:  
    
  `[imagen omitida: wiki id 55237]`  
    
  The .jar file named <DeploymentUnit\_Name>\_<ProjectName>.jar contains the classes and configuration files needed to execute the procedure.  
    
  In a child directory of the deployment folder (in the example "DeploymentUnit2"), you will find all the .jar files that represent your application's dependencies.  
    
  `[imagen omitida: wiki id 55238]`

**Note**: The loose .class files that you find in the classes folder are only intermediary and are used to build the final .jar file, but they are not needed to run the application.

### [Step 3: Running the Deployed Application](#Step+3%3A+Running+the+Deployed+Application)

To run your application, you only need the main .jar file and all the dependencies specified in the classpath entry. Be sure to include all necessary dependencies according to your application requirements.

java -cp <classpath> package.<classfile>

To set the classpath using the Deploy files:

java -cp "<deployfolderpath>\<numberfolder>\\*;<deployfolderpath>\<FileName.jar>" package.<classfile>

Sample:

java -cp "DeploymentUnit2\_20230706104002.jar;DeploymentUnit2\20230706104002\\*" mypackage.test.sample

In addition, when the deployment unit contains only one command line procedure, the deployment process generates a manifest file that contains information about the main class of your application and the classpath required for its execution.  
This simplifies the execution process, as you can have the generated .jar file along with the other .jar files indicated in the classpath entry, and easily execute it using the following command:

java -jar <FileName.jar>


|  |
| --- |
| **Backlinks** |
| [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) |

---
