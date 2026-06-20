---
title: "HowTo: Deploy an Application to AWS Elastic Beanstalk"
source_id: 32104
source_url: https://wiki.genexus.com/commwiki/wiki?32104
genexus_version: "18"
---

# HowTo: Deploy an Application to AWS Elastic Beanstalk

It is possible to easily deploy and run
[Java](https://wiki.genexus.com/commwiki/wiki?12258) and
[.NET](https://wiki.genexus.com/commwiki/wiki?38604) generated applications in [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/).

Before deployment, using a new [Environment](https://wiki.genexus.com/commwiki/wiki?7115) in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) is recommended to generate a new deployment version that runs locally in the Tomcat or IIS of the computer used to work with GeneXus connected to the AWS RDS database, or any [Cloud Database](https://wiki.genexus.com/commwiki/wiki?31685). In this way, you can make the configurations that will be used in the production database.

Before starting, make sure that you have [MSDeploy](http://www.iis.net/downloads/microsoft/web-deploy) installed on your machine (only if you use
[.NET](https://wiki.genexus.com/commwiki/wiki?38604)).

### [Prerequisites](#Prerequisites)

1. [Amazon Web Services Account](https://aws.amazon.com).
2. [AWS Access Key creation](https://wiki.genexus.com/commwiki/wiki?32106) for managing AWS Resources from the Command Line Interface.
3. An AWS RDS Database.
4. [MSDeploy](http://www.iis.net/downloads/microsoft/web-deploy) installed on your machine.

\* [See minimal required policy](https://wiki.genexus.com/commwiki/wiki?39355,,) to Deploy to EBS without FullAccess.

### [Steps to deploy to AWS Elastic Beanstalk](#Steps+to+deploy+to+AWS+Elastic+Beanstalk)

**1.** Before making a deployment, you must configure your Data Store to connect to the target Database, which may be an AWS RDS Database. (ref.: [Cloud Database](https://wiki.genexus.com/commwiki/wiki?31685))

**2.** Run a [Build All](https://wiki.genexus.com/commwiki/wiki?5691).

**3.** Go to the Build menu and select the Deploy Application option.

**4.** In the Deployment screen:

**1.** Select the Main objects to be included in the deployment.

**2.** In Target, select the option "AWS Elastic Beanstalk".

**3.** Set the following properties as indicated below:

**1.** AWS Access Key/Secret Access Key: Enter your AWS Access Key generated from:  [AWS Access Key creation](https://wiki.genexus.com/commwiki/wiki?32106).

**2.** AWS Default Region: Select your preferred region (localization) for your Deployment.

**3.** Application Name: It's the name used to display the application. After deployment, it will be visible from [AWS Elastic Beanstalk Portal](https://console.aws.amazon.com/elasticbeanstalk/).

**4.** Application Version: The Application version name. Every deployment must have a different version name (or will fail).

**5.** Application Environment Name: Your environment name. Defaults to "Production", but you can create other environments such as "Test", "Preproduction".

**5.** After selecting the main objects and configuring the necessary properties for the automatic deployment, press the Deploy button. It will build the WAR package (when JAVA) or a Web Deploy ZIP (for .NET), as well as upload and deploy it in AWS Elastic Beanstalk.

**6.** You can check the Application URL, Status and Configuration from [AWS Elastic Beanstalk Portal](https://console.aws.amazon.com/elasticbeanstalk/).

### [Troubleshooting](#Troubleshooting)

> "The instance profile aws-elasticbeanstalk-ec2-role associated with the environment does not exist."

**Solution**: Log in to AWS Console. Create any Elastic Beanstalk Environment through the Console, as it will create automatically the necessary IAM profile 'aws-elasticbeanstalk-ec2-role'.  You can delete the environment after.

### [See Also](#See+Also)

[What is AWS Elastic Beanstalk](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)


|  |
| --- |
| **Backlinks** |
| [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Toc:Application Deployment tool (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54334) | [Deploy Application Targets](https://wiki.genexus.com/commwiki/wiki?42079) |

---
