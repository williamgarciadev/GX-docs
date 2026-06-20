---
title: "GeneXus SDK for SAP Leonardo: Retraining a model to use in a ML service"
source_id: 41860
source_url: https://wiki.genexus.com/commwiki/wiki?41860
genexus_version: "18"
---

# GeneXus SDK for SAP Leonardo: Retraining a model to use in a ML service

Genexus has a module that allows you to retrain SAP Leonardos ML services, which you can obtain from [here](https://wiki.genexus.com/commwiki/wiki?41886,,).

**Consideration: Before including the module into your Knowledge Base you need to have the pattern Fiori Initialized first.**

First of all, it should be clarified that in the case of retraining services, services are no longer accessed through APIKey, but OAuth2.0 is used here.

This is because now, the service we will use (eg Image Classification) will no longer be the one published in the SAP API Business Hub (public sandbox) but will be our instance of that service that we will create.

**1 - Creating our own instance of the Service in SCP**

This process must be done outside of GeneXus.

First, we access [SCP](https://account.hanatrial.ondemand.com/cockpit#/home/trialhome) with our trial account (Cloud Foundry Trial/trial).

We see in Cloud Foundry 1 Space, the tile "dev" is the one assigned to my Space.  
Here you can see if you have any application available.  
  
What we must do next, is to create an instance of the service and a service key for the ML Foundation.  
Go to Service Marketplace, choose ml-foundation-trial-beta and in the Instance option select New Instance.

If you cannot find the ml-foundation-trial-beta in the marketplace, check that in your accounts Entitlements, ML Foundation Trial has a plan assigned.`[imagen omitida: wiki id 43747]`

Then, go to Service Instance and select the newly created instance.

Choose Service Keys and Create Service Key.

You will obtain a file (in json format) which contains all the information and URLs necessary to invoke both the retraining and inference services of this instance.

`[imagen omitida: wiki id 41872]`

Copy this json that you will use later.

**2 - Retraining**

The GeneXus retraining module uses the Rest API that SAP Leonardo makes available for this purpose, this module is a wizard that will guide you through the necessary steps to retrain.

Additionally, it has a transaction for the purpose of storing all the information referring to the different instances of the services (Trn: SCPLeoSrvInst).

You must create a record here for each service instance and enter all the information of the service key information obtained when creating it (you can enter it manually or copy and paste the json in the option for such purposes).

Access through Service Instance Setup tile:

`[imagen omitida: wiki id 41877]`

From the Service Instance Setup option you can:

- Work with instance service key data

`[imagen omitida: wiki id 41878]`

- View service token validation status (green valid/red expired) and renew it

`[imagen omitida: wiki id 41879]`

- Retrain the service

`[imagen omitida: wiki id 41880]`

With this option, you access the retraining wizard

`[imagen omitida: wiki id 41881]`

This module uses the following SAP Leonardo ML services:

 . GET /storage: Returns the storage endpoint for the given tenant.  
 . POST /storage: Initiate the creation of a storage endpoint for the tenant id defined by the zoneId from the JWT token.

 . GET /jobs: Get information about retraining jobs.  
 . POST /jobs: Submit a retraining job.  
 . GET /jobs/{id}: Get status of retraining job with the specified ID.

 . GET /models: List models.  
 . GET /deployments: Get a list of deployed models.  
 . DELETE /deployments/{id}: Undeploy a deployed model.  
 . POST /deployments: Deploy a retrained model.

The wizard will guide you through the different stages of the retraining process.

**Stage: Storage Endpoint**

In this example we are going to retrain a model for image classification, for this we must upload a set of training images to the cloud where SAP Leonardo will take them.  
For this purpose, the first step is Initialize the cloud filesystem, that means the creation of a storage endpoint for the tenant id defined, this is done automatically in this step.

When this step is started, the first thing to do is check the status of the 'Storage Endpoint', if it is not initialized, a 'Status: Pending' or 'Status: Error' message will be issued and the same can be initialized (Create button).

When you have a 'Status: Ready' message you can go to the next step (Next button).

`[imagen omitida: wiki id 41889]`

**Stage: Upload Data**

As you know, the first thing you must to do in a Retraining Model process is the Data Preparation. It's referred to obtain the data set to use in the training process, debug it and split into three groups, Training/Test/Validation (80%/10%/10%).

Once you have de data (images) simply put it in a data structure (a directory structure) that represent the different categories which you want to obtain, and the different groups, Training/Test/Validation.

In this sample we will retrain the model to differentiate images of the Superhero Flash from other Superheroes, therefore the categories will be "Flash" and "NoFlash".

`[imagen omitida: wiki id 41926]`

This structure of directories with the images is the one that must be uploaded to the cloud storage from where SAP Leonardo will take them to retrain the model. Therefore, in this step, you have to zip the root directory that contains the images, upload it by selecting the Add Files button and pressing the Start Upload Button. Once uploaded, click the button Send to send the data to the AWS S3 bucket associated to your user, the data will be sent on the background.

When the data starts being sent, the Send button will change for a Status button that when you press it, it shows information about the status of the process.

The status of the process can be Finished, Pending or Error. An error can happen when you are trying to send a large quantity of data and the connection is cut, causing the upload to interrupt.

If the process is interrupted a new Resume button will appear allowing you to resume the process of sending data.

**Note: The SDK has set a Maximum File Size of 262144000 bytes (250 MB) if you want to change this restriction, you have to change the [File Upload User Control Max File Size Property](https://wiki.genexus.com/commwiki/wiki?30574).**

`[imagen omitida: wiki id 41890]`

**Stage: Retrain**

Once you have the data is uploaded and sent to the AWS S3 bucket you can start the retraining process. In this stage, you can manage the existing retraining jobs for this service instance or start new ones.

`[imagen omitida: wiki id 41934]`

In order to start a new retraining job, you must click on the + button and then select some parameters for the job definition (For more information on some of the parameters used here see the following [link](https://towardsdatascience.com/epoch-vs-iterations-vs-batch-size-4dfb9c7ce9c9))

`[imagen omitida: wiki id 41932]`

When the job ends with status SUCCEEDED, you can proceed to the next step.

`[imagen omitida: wiki id 41936]`

**Stage: Deploy Model**

The last step is to Deploy the version of the model retrained by you. You can work with the different version of all the models in your Service Instance. You can undeploy an active version and Deploy the one you want.

`[imagen omitida: wiki id 41955]`

The model version with Deployment status SUCCEEDED is the one that will be used for Inference.

**3 - Using a retrained model for Inference**

Using a retrained model for inference allows you to redefine the behavior of a Machine Learning Service in order to best fit your needs.

In the case of retraining a model for image classification service, you redefine the categories to be shown as results along with the classification score the image gets for each category.

Run your application pressing F5 or clicking the Run icon `[imagen omitida: wiki id 41940]`

Click on the Image Classification Tile to open the List Report.

`[imagen omitida: wiki id 41941]`

Now select the Insert icon `[imagen omitida: wiki id 41942]` to add a new image.

`[imagen omitida: wiki id 41943]`

Set the image Description as 'Flash'

Select 'Change' option to upload a local file.

`[imagen omitida: wiki id 41944]`

`[imagen omitida: wiki id 41945]`

Once you have selected the image, click confirm to create the new registry.

`[imagen omitida: wiki id 41946]`

Now click on Classify to process the image using SAP Leonardo Machine Learning Services

`[imagen omitida: wiki id 41947]`

By clicking Confirm you can process the service with the pre-trained model available in the public SAP API Hub service instance.

`[imagen omitida: wiki id 41951]`

This is the result of processing the image with the pre-trained model available in the public SAP API Hub service instance.

Notice how the image classification results are shown, displaying the highest scored categories defined in the pre-trained model.

`[imagen omitida: wiki id 41952]`

In the Service Instance dropbox, you can select any service instance defined.

Select the custom service instance previously created 'mlflash'

`[imagen omitida: wiki id 41948]`

In the custom service instance, you can select from different models you have retrained, including the default pre-trained model available in the public SAP API Hub service instance

Select the 'mlflash' Service Instance and  then select the Model Version 'sapflash-01'

Click Confirm to process the image using the retrained model of your own service instance.

`[imagen omitida: wiki id 41953]`

You can observe how the categories and the score in the classification service have been redefined as a result of the retraining process.

`[imagen omitida: wiki id 41956]`


|  |
| --- |
| **Backlinks** |
| [GeneXus SDK for SAP Leonardo: End User Documentation](https://wiki.genexus.com/commwiki/wiki?41183) | [GeneXus SDK for SAP Leonardo: FAQ](https://wiki.genexus.com/commwiki/wiki?41185) | [HowTo: Build a custom model for GeneXusAI](https://wiki.genexus.com/commwiki/wiki?43665) |

---
