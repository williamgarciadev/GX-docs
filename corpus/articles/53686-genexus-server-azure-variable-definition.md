---
title: "GeneXus Server Azure Variable Definition"
source_id: 53686
source_url: https://wiki.genexus.com/commwiki/wiki?53686
genexus_version: "18"
---

# GeneXus Server Azure Variable Definition

After performing the [GeneXus Server Azure Configuration](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?52099,,), you must specify each defined variable. To do so, keep in mind the information below.

Once you import your pipeline definition, you need to specify the pipeline variables within the “Variable” section of the .yml script.

Each variable is defined in the pipeline script as a reference to a [UI-defined variable](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops&tabs=classic%2Cbatch#tabpanel_1_classic). You can add each variable with the right-side name through the “variable” interface, or replace the right-side reference with the actual value you wish to assign.

The parameters are as follows:

* MSBUILD: Path to the latest Msbuild installation available in the Windows executor node.
  + Example: "C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\Msbuild\\Current\\Bin\\MSBuild.exe"
* BL\_PATH: Path to the GeneXus installation used in the Windows executor node.
  + Example: “C:\\Program Files (x86)\\GeneXus\\GeneXus17”
* WORKING\_DIR: Path to the directory where the CI/CD files are going to be generated.
  + Example: “C:\\AzureCheckouts”
* KB\_ALIAS: Name of the Knowledge Base you intend to work with.
  + Example: “PlantCare”
* GXSERVER\_URL: URL to the GeneXus Server instance hosting the Knowledge Base.
  + Example: “https://sandform.genexusserver.com/kbs”
* GXSERVER\_ USER: GeneXus Server user to be authenticated with.
  + Example: “gxtechnical\ibianchi”
* GXSERVER\_PASS: GeneXus Server user password. We will be adding this parameter as a [Secret Variable](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/set-secret-variables?view=azure-devops&tabs=yaml%2Cbash).
* KBENVIRONMENT: Specify the Environment for the current Knowledge Base.
  + Example: “NETMySQL”
* KBGENERATOR: Specify the Generator for the current Knowledge Base.
  + Example: “.Net”
* FORCE\_REBUILD: “True” if you wish to empty the build folder and rebuild the Knowledge Base on every pipeline run, “False” to trigger build only on update (no directory cleaning). It is advised to leave “False” as default and enable “Let users override this value when running this pipeline” option. This way, you may call the pipeline modifying the variable value when needed, triggering forced rebuild on demand.
* PUBLISH\_SETTINGS: (for Deploy as WebApp) Path to the Azure publish profile file. See the [HowTo: Deploy as an Azure Web App](https://wiki.genexus.com/commwiki/wiki?31457).
  + Example: "C:\\AzureCheckouts\\GeneXusDeploy.PublishSettings"
* DEPLOYMENT\_UNIT: Name of Deployment Unit object in the Knowledge Base that you wish to deploy.
  + APPLICATION\_KEY: GAM Encryption key used to encrypt sensitive information. See [Application Encryption Key property](https://wiki.genexus.com/commwiki/wiki?36909).

You may also set up your scheduled trigger by modifying the “cron” tag in the “Schedules” section. This parameter follows the [Cron Syntax](https://docs.oracle.com/cd/E12058_01/doc/doc.1014/e12030/cron_expressions.htm) and cannot be specified through variables. The provided example triggers the pipeline once every 10-minute interval.

**Note**: The variables “KB\_PATH” and “DEPLOY\_NAME” need not be defined, as they reference other variables, but they may be modified if you want to. You may need to adjust your pipeline script accordingly.

Once the parameters have been configured, save the .yml changes and this will execute the pipeline automatically.
