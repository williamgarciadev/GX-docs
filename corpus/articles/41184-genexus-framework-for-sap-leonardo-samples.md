---
title: "GeneXus Framework for SAP Leonardo: Samples"
source_id: 41184
source_url: https://wiki.genexus.com/commwiki/wiki?41184
genexus_version: "18"
---

# GeneXus Framework for SAP Leonardo: Samples

Welcome to the GeneXus for SAP Systems sample walkthrough using SAP Leonardo Machine Learning Services!

In this walkthrough, you will be covering all the required steps to successfully use a SAP Leonardo ML service in a Fiori-like web application created using GeneXus for SAP Systems.

The sample implemented will use SAP Leonardo ML Image Classification service.

GeneXus and GeneXus for SAP Systems design architecture focuses on [Knowledge Bases](https://wiki.genexus.com/commwiki/wiki?1836) (how projects are named in GeneXus terminology)

Links for further information about GeneXus Objects will be provided along the walkthrough.

Start by launching GeneXus for SAP Systems.

After the program loads, GeneXus for SAP Systems IDE will be displayed, an intuitive IDE that provides engaging user experience.

`[imagen omitida: wiki id 41451]`

For more information on how the IDE is organized please access [this article](https://wiki.genexus.com/commwiki/wiki?5272).

For this walkthrough, you will use an existing Knowledge Base, downloaded from [GeneXus Server](https://wiki.genexus.com/commwiki/wiki?31337,,).

This Knowledge Base serves as a framework accessible to every GeneXus developer, providing the essential know-how to include and use SAP Leonardo ML Services in GeneXus applications.

Additionally, the Knowledge Base contains samples of practical uses of the SAP Leonardo ML services to empower the application development.

Once the IDE is launched, in the menu bar go to File->New->Knowledge Base from GeneXus Server.

`[imagen omitida: wiki id 41452]`

Clicking on the ‘New Knowledge Base from GeneXus Server’ option will prompt a form to create the new Knowledge Base based in a server hosted Knowledge Base.

To simplify this step you can browse the server to find the KB. To do so, click on ‘Select Server KB’

`[imagen omitida: wiki id 41453]`

A login form will prompt to connect to GeneXus Server. The GeneXus account credentials must be provided in order to log in.

`[imagen omitida: wiki id 41454]`

After the validation process of the account credentials is successful, the developer is able to browse the different Knowledge Bases in the Server.

For this walkthrough, you will work on the Knowledge Base called ‘GXSAPLeonardo15v4’. This Knowledge Base can be found under the server ‘Samples’ in the left tab.

`[imagen omitida: wiki id 41455]`

Once the Knowledge Base is selected from the browser view, the Server KB URL is set, allowing the developer to configure local properties such as name and path.

After setting local values, select ‘Create’ to start the Knowledge Base creation process.

`[imagen omitida: wiki id 41456]`

`[imagen omitida: wiki id 41457]`

`[imagen omitida: wiki id 41458]`

`[imagen omitida: wiki id 41459]`

Now the local Knowledge Base was created successfully!

Let’s explore the Knowledge Base.

`[imagen omitida: wiki id 41460]`

First is important to know that GeneXus for SAP Systems IDE has side tabs that can be expanded and rearranged according to the developer needs.

`[imagen omitida: wiki id 41461]`

1. KB Explorer: Shows the structure of the Knowledge Base, modules, folders, and objects.
2. Preferences: Allows configuration of development environments, including code generators and data stores.
3. Test Results: Shows unit tests results and allows to view the execution details.
4. Test Explorer: Displays all unit tests defined and allows to run selected tests.
5. Toolbox: Contains design elements that can be added to enhance the application.
6. Properties: Displays properties of the selected object.
7. Output: Displays the output of the application specification process and of the application generation process.

As a first step, some key modules for this walkthrough in the KB Explorer will be reviewed in detail, therefore you should expand and pin `[imagen omitida: wiki id 41381]` the KB Explorer panel.

`[imagen omitida: wiki id 41462]`

This Knowledge Base contains a Root Module that includes defined modules, folders and objects allowing improved file organization.

`[imagen omitida: wiki id 41463]`

Inside the Root Module you can observe two Fiori related modules, **FioriBaseObjects** and **FioriMobileBaseObjects**.

GeneXus for SAP Systems Fiori Pattern feature was applied to his Knowledge Base to enable Fiori UX design of the application according to Fiori design guidelines.

Once the Fiori Pattern is applied to web applications, GeneXus automatically generates all the objects required to design the web application considering Fiori design guidelines under the **FioriBaseObjects** module.

Fiori Pattern was also applied to Smart Devices (SD) application, allowing the design based on Fiori UX to be implemented in smart devices, generating automatically the **FioriMobileBaseObjects** module.

Another key module in this Knowledge Base is **GXSAPLeonardo.**

**GXSAPLeonardo** module contains modules automatically generated according to each SAP Leonardo ML service imported to this Knowledge Base.

This AI framework includes the following services:

`[imagen omitida: wiki id 41464]`

This framework is updated frequently, but if the developer wants to use a SAP Leonardo ML service that is not in this framework version, the developer may [import the Open API](https://wiki.genexus.com/commwiki/wiki?31864).

Each service module, for example, Image Classification, contains automatically generated objects to implement the API call, procedures and structured data types defined to model the required information to be sent to the service.

`[imagen omitida: wiki id 41465]`

Each service module in **GXSAPLeonardo** module works as the backend for the framework, calling SAP Leonardo Machine Learning Service APIs.

The module that works as the frontend for the Machine Learning services framework is the **GXSAPLeonardoSamples**.

**`[imagen omitida: wiki id 41466]`**

Here you can see different ML services grouped in folders which contain GeneXus objects to establish the functionality, presentation, and accessibility as the frontend elements in the framework.

Now Run the application, to so click on the run button `[imagen omitida: wiki id 41387]` or press F5.

If the Hana DB connection settings are not set, GeneXus will prompt a panel which allows to specify the settings.

(Take into account that if you are using a trial version of SAP Cloud Platform a tunnel connection must be opened to establish a connection to the cloud Schema)

Access [this link](https://wiki.genexus.com/commwiki/wiki?34179) for more information.

GeneXus will start the specification to create the objects described in the database.

After this step is completed the ide will show the tables that will be created and will ask for confirmation to continue.

GeneXus will proceed to generate automatically the Java code based on the objects defined in the Knowledge Base.

Once the code generation process is finished the application will launch.

This is the framework main menu, displaying a Fiori Launchpad including, as tiles, all the machine learning services samples. This menu style is generated automatically after Fiori Pattern is applied.

`[imagen omitida: wiki id 41467]`

Upon selecting the Image Classification Tile, image records are displayed in a Fiori List Report since Fiori Pattern was applied to this object.

Some image records were loaded during runtime for this example.

The ‘Classify’ link calls SAP Leonardo Image Classification pre-trained service to process the image selected.

`[imagen omitida: wiki id 41468]`

If you click Classify for the image Brandenburg Gate (id 8), the framework requests the image Classification service to be run for this image.

`[imagen omitida: wiki id 41469]`

SAP Leonardo Image Classification service classifies the landmark and displays the matching percentage to the predefined categories.

In this walkthrough, you are going to create a frontend interface similar to the one shown previously to consume SAP Leonardo Machine Learning Services.

Now, start by creating a new folder for the sample, named ‘ImageClassificationSample’

Right click the module **GXSAPLeonardoSamples**-> New -> Folder

`[imagen omitida: wiki id 41470]`

Once the folder is created, add your first GeneXus object, a [transaction](https://wiki.genexus.com/commwiki/wiki?1908).

Transactions allow the developer to describe key aspects in order to model the reality, fulfilling the requirements of the application.

To create a transaction, right click in the newly created folder named ‘ImageClassificationSample’ and select New->Object

`[imagen omitida: wiki id 41471]`

A panel showing all available GeneXus objects will be displayed.

In the category ‘Common’ select ‘Transaction’ object in the right side of the panel.

As the transaction represents the ImageClassificationSample you will name the object the same in the lower side of the panel.

Once this is done, click on ‘Create’.

`[imagen omitida: wiki id 41472]`

This is the [transaction object](https://wiki.genexus.com/commwiki/wiki?1908).

In the Structure selector, the attributes for the transaction are defined, indicating attribute name, type, description, etc.

`[imagen omitida: wiki id 41473]`

Since in this particular case you are storing images to classify, you are going to describe three main attributes.

**Id** – A unique key to identify a record, set as a numeric type. By default, the type Numeric(4) is assigned.

**Name**- A name to assign to the image, set as a variable character field.

**Img**- The image itself. For this type of data, GeneXus has the Image Type.

You can observe that GeneXus in most cases infers the data type according to the name of the attribute.

If the developer presses the dot character (.) while having the prompt in an attribute name line, GeneXus will add the name of the transaction, therefore, the developer will only need to enter the rest of the attribute name.

(Naming attributes in a unique way throughout the Knowledge Base is a **highly recommended** practice since GeneXus infers through the attribute name, valuable information that saves a lot of development time)

After describing the attributes the transaction should look like this.

`[imagen omitida: wiki id 41474]`

Once the structure is defined, you will have to apply Fiori Pattern to visualize this transaction as a Fiori List Report.

To do so, click on the ‘Patterns’ selectors.

`[imagen omitida: wiki id 41475]`

Notice that in the transaction tab there is an asterisk character after the name of the transaction.  `[imagen omitida: wiki id 41397]`

The asterisk shows that the object has unsaved changes. Once the transaction changes are saved the asterisk character at the end will disappear.

To apply Fiori Pattern for web, you have to save the transaction created, click OK.

`[imagen omitida: wiki id 41476]`

After saving, a panel will display the available Fiori floorplans applicable to the transaction object showing on the right side of the panel a preview of the selected floorplan.

Select ListReport floorplan.

This is the List Report floorplan view, to access the Fiori floorplan view set to a transaction, select the Transaction->Patterns Selectors-> Fiori for Web->ListReport.

The last tab may vary depending on the Fiori floorplan selected, in this case, you selected List Report, so the floorplan view tab reads List Report.  
`[imagen omitida: wiki id 41477]`

When the ListReport floorplan view is selected, two panels are displayed.

The left panel indicates the objects created automatically by GeneXus Fiori Pattern. This objects may be modified by the developer according to the desired visualization of the information. GeneXus automatically generates objects for all the attributes defined in the transaction structure.

The right panel shows the interface preview of all the objects defined according to the selected floorplan. Please check that the preview size is set to ‘Medium’ since if it is set to ‘Automatic’ depending on the panel size in the IDE some attributes may not be displayed.

(This is because each attribute has properties allowing whether to show the attribute or hide it depending on the different sizes the web form may take).

Next, you want to have a button to run the Image Classification service for each image record in the List Report view.

To do this, right click on the Grid control and select New->User Action

(The User Action control works as a button)  
`[imagen omitida: wiki id 41478]`

Next, naming the User Action is required, that can be done in the properties panel at the right side of the IDE, the properties panel will be shown after clicking the User Action control.  
`[imagen omitida: wiki id 41479]`

The ‘Name’ property is mandatory (asterisk indicates mandatory value required) and determines a unique control name to be referenced by GeneXus.

Enter ‘Classify’ on this field.

The ‘GXObject’ property determines which GeneXus object will be called after the User Action is clicked. For now, this field will be left blank.

The ‘Caption’ property determines the text shown to the user. Enter ‘Classify’ on this field.

This is how the ListReport panel will look after the User Action is added.

`[imagen omitida: wiki id 41480]`

If the ‘Classify’ User Action is clicked the application should call the Image Classification service to process the image.

Once the image is processed you need to design the user interface to show the results of the service.

Let’s create a [web panel](https://wiki.genexus.com/commwiki/wiki?6916) to show this results.

This web panel will receive as input parameter the attribute ‘ImageClassificationSampleId’ to determine which image has to be processed and call the ML service.

The service will automatically load its defined structures (generated on the import) with the data output.

In this web panel, you will design how to display the information and how to obtain it after the ML service was called.

First, start by creating a web panel. Right click on the ‘ImageClassificationSample’ folder and select New->Object.`[imagen omitida: wiki id 41481]`

Now under ‘Web’ Category select ‘Web Panel’ and name it ‘ViewClassificationSample’

`[imagen omitida: wiki id 41482]`

After creating the Web Panel the object will show this way.

`[imagen omitida: wiki id 41483]`

To design the interface you will start using the toolbox panel at the right so you might want to pin it.

The toolbox panel contains all the design controls required to create a suitable interface for the application.

There are four main elements that you want to show in this web form.

1. The image selected to process.
2. A Grid object to list elements 3 & 4
3. The categories in which the service has classified the image.
4. The matching percentage for each category.

1. Considering that the image to be displayed will change according to the selected image to process, the image must be a variable value, therefore you have to add an Attribute/Variable control to the web form.  
   To do so, simply drag the Attribute/Variable to the web form.  
   Upon dragging the control you can observe that a window panel will display showing all attributes and variables defined in the Knowledge base.  
   In this case, you will need to create a new variable, so click New Variable.  
   `[imagen omitida: wiki id 41484]`  
   In this window, you have to assign a name and a type to the variable.  
   This variable will be of type Image and you will name it ‘ProcessedImage’.  
   `[imagen omitida: wiki id 41485]`  
   GeneXus will automatically infer the variable type due to the variable name ending in 'Image’.  
   Once the variable is defined the web form will look like this.`[imagen omitida: wiki id 41486]`  
   Make sure that the Label Position property is set to ‘None’.  
   Also, set the AutoResize property to ‘False’ so the image has a fixed size.  
   Set Width property to ‘450px’.  
   `[imagen omitida: wiki id 41487]`
2. Now you will insert another common GeneXus object: the [Grid control](https://wiki.genexus.com/commwiki/wiki?24817).  
   To add a Grid control drag the item from the toolbox to the Web Form.  
   The control may be placed on either of the edges of the present elements in the web form, thus is possible to place controls in different places allowing multiple design approaches.`[imagen omitida: wiki id 41488]`  
   Upon dragging the control you can observe that a window panel will display showing all attributes and variables defined in the Knowledge Base.
3. You need to display in the grid a variable describing the categories assigned to the image processing, so click New Variable.  
   `[imagen omitida: wiki id 41489]`  
   To specify the Category variable, you need to name the variable as ‘Category’ and select ‘Varchar’ as Data Type, with Maximum length assigned to ‘100’.  
   When completed click Ok.  
   `[imagen omitida: wiki id 41490]`  
   Here is the Web Form including the gird with the variable ‘Category’ defined.  
   `[imagen omitida: wiki id 41491]`
4. Now repeat the procedure of adding a variable, but this time place it inside the grid, by the right border of the ‘Category’ Variable box.  
   `[imagen omitida: wiki id 41492]`  
   Once the control is placed, click on ‘New Variable’ after the windows form appears.  
   `[imagen omitida: wiki id 41493]`  
   Name the variable ‘MatchPercentage’ and assign the Data Type to ‘Numeric’ with Length ’10’ and Decimals ‘5’.  
   Click Ok.  
     
   `[imagen omitida: wiki id 41494]`

Once the four main elements have been set the layout for this form will look like this.

This is a good time to save the work done on this web panel, to do so press Ctrl+S or click the diskette icon

`[imagen omitida: wiki id 41495]`

Now as this panel will work with a variable attribute (ImageClassificationSampleId) it is required to define which the input parameters to call this object.

To do this, you have to select the ‘Rules’ Selector nex to WebForm.

In this Selector, you can specify [rules](https://wiki.genexus.com/commwiki/wiki?8288) to this object.`[imagen omitida: wiki id 41496]`

In the rules editor in order to define the input, you need to specify the following line.

```
parm(in:ImageClassificationSampleId);
```

parm is the rule that defines the input and output parameters, they can be in for input, out for output or inout for input/output.

Now save your web panel pressing Ctrl+S or clicking the diskette icon.

Now, get back to the Transaction object, open the pattern tab and under Fiori for web select the List Report view.

Select the User Action you added before ago, and in the properties of the object go to GXObject … remember you left that property blank?

Here you will assign that when the Classify button is clicked, the Web panel will be called.  
`[imagen omitida: wiki id 41497]`

All GeneXus objects will be displayed, you may want to filter by filling the Pattern text box.

Once you have found the ViewClassificationSample WebPanel, select OK.  
`[imagen omitida: wiki id 41498]`

As the web panel object to be called has the input parameter of ImageClassificationSampleId, you have to assign it to the User Action.

First, you need to define that the User Action sends a set of parameters.

Right click on User Action->Add->Parameters.  
`[imagen omitida: wiki id 41499]`

Okay, now you just the defined that the user action control sends a set of parameters, but you need to specify which are those parameters.

Right Click on Parameters->Add->Parameter.

`[imagen omitida: wiki id 41500]`

After adding the parameter you will have to set the name of the parameter in the properties.

`[imagen omitida: wiki id 41423]``[imagen omitida: wiki id 41501]`

Let’s name it ‘ImageClassificationSampleId’

`[imagen omitida: wiki id 41502]`

It’s a good time to save the work now.

So far you have created a transaction modeling the data you need to store, assigned a Fiori pattern to the object and, you configured a button that will allow us to classify the image.

The button will call a web panel that will load the image selected to process and show its categories and matching percentages.

You also designed the web panel layout and configured the parameters received as inputs.

The final step is to program the SAP ML service call to process the image and work with the results on the web panel.

 Click the Event Selector in the WebPanel ‘ViewClassificationSample’.

`[imagen omitida: wiki id 41503]`

Since the objective is that the image selected is loaded in the web panel with its classification stats, you need to display the information as soon as possible. In this case, you have to use the [Load Event](https://wiki.genexus.com/commwiki/wiki?8188).

Once you selected Events, select ‘Load’ from the dropdown list.

`[imagen omitida: wiki id 41504]`

After selecting the following code will appear denoting the beginning and the end of the event block.

```
Event Load     

Endevent
```

Inside of the event block, we will write this code.

```
for each           

             &ProcessedImage = ImageClassificationSampleImg

             &ImageClassificationBlob = ImageClassificationSampleImg

       endfor

&ImageClassificationFile.Source = &ImageClassificationBlob

//Call SAP Leonardo API for Image Classification

&ResultOK = GXSAPLeonardo.ImageClassification.POSTInferenceSync(&ImageClassificationFile, '', '', &ResponseOkOUT, &ResponseErrorOUT, &ErrorOUT, &Message)

if &ResultOK

       for &ClassificationResults in &ResponseOkOUT.predictions

             for &Classification in &ClassificationResults.results

                   

                    &Category = &Classification.label                         

                    &MatchPercentage = Round(&Classification.score * 100, 2 ) 

                    load

                   

             endfor

       endfor

endif
```

Don’t worry! The code is going to be reviewed line by line.

Before reviewing the code, define the variables and its types.

|  |  |
| --- | --- |
| **Variable Name** | **Data Type** |
| ImageClassificationBlob | Blob |
| ImageClassificationFile | File |
| ResultOK | Boolean |
| ResponseOkOUT | ResponseOk, GXSAPLeonardo.ImageClassification |
| ResponseErrorOUT | ResponseError, GXSAPLeonardo.ImageClassification |
| ErrorOUT | Error, GXSAPLeonardo.ImageClassification |
| Message | Messages.Message, GeneXus.Common |
| ClassificationResults | ClassificationResult, GXSAPLeonardo.ImageClassification |
| Classification | Classification, GXSAPLeonardo.ImageClassification |

It is important that the data type of a variable refers to the appropriate module, in this case as you are using the Image Classification service, the module is GXSAPLeonardo.ImageClassification.

Take a look at what this code does.

```
for each

             &ProcessedImage = ImageClassificationSampleImg

             &ImageClassificationBlob = ImageClassificationSampleImg

Endfor
```

The for each command (for each wiki)

performs a database query filtering registers where the register id (defined in the Transaction object) is the same as the parameter provided id, once the Id matches, the register image data will be assigned to the image variable.

The register image data will also be assigned to a blob variable (blob wiki), this will be of use for the next line.

```
&ImageClassificationFile.Source = &ImageClassificationBlob
```

The image retrieved from the database is assigned as the source of the file to be processed by the Image Classification service.

Now you have all the required data to call the service.

&ResultOK = GXSAPLeonardo.ImageClassification.POSTInferenceSync(&ImageClassificationFile, '', '', &ResponseOkOUT, &ResponseErrorOUT, &ErrorOUT, &Message)

The service call returns a Boolean indicating whether the service executed successfully or not.

The POSTInferenceSync method is included in GXSAPLeonardo.ImageClassification module and has the following parameters.

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter** | **In/ Out** | **Data Type** | **Value passed** |
| &file | In | File | &ImageClassificationFile |
| &options | In | Varchar(256) | ‘ ’ |
| &Oauth2\_ClientCredentials | In | Character(20) | ‘ ‘ |
| &ResponseOkOUT | Out | ResponseOk, GXSAPLeonardo.ImageClassification | &ResponseOkOUT |
| &ResponseErrorOUT | Out | ResponseError, GXSAPLeonardo.ImageClassification | &ResponseErrorOUT |
| &ErrorOUT | Out | Error, GXSAPLeonardo.ImageClassification | &ErrorOUT |
| &HttpMessage | Out | Messages.Message, GeneXus.Common | &Message |
| &IsSuccess | Out | Boolean | &ResultOK |

The service call will load the elements in the structure of the ImageClassification Service objects.

In order to display the results we have to read the information loaded in those objects as result of the service call.

```
if &ResultOK

       for &ClassificationResults in &ResponseOkOUT.predictions

             for &Classification in &ClassificationResults.results

                   

                    &Category = &Classification.label                                      

                    &MatchPercentage = Round(&Classification.score * 100, 2 )              

                    load

                   

             endfor

       endfor

endif
```

If the procedure executed without errors you iterate through every Classification results in in the response (In this case, since you called the service for one image, there will be only one item, but the service can process more than one image in one call, this is due that the call allows .zip files to be passed as the file parameter)

For each classification in the Classification Result, you load in the grid (using the load command), the name of the category in which the object was classified and its matching score to that category.

Now Run the application, to so click on the run button `[imagen omitida: wiki id 41430]` or press F5.

If the Hana DB connection settings are not set, GeneXus will prompt a panel which allows to specify the settings.

(Take into account that if you are using a trial version of SAP Cloud Platform a tunnel connection must be opened to establish a connection to the cloud Schema)

Access [this link](https://wiki.genexus.com/commwiki/wiki?34179) for more information.

`[imagen omitida: wiki id 41505]`

`[imagen omitida: wiki id 41506]`

GeneXus will start the specification to create the objects described in the database.

After this step is completed the ide will show the tables that will be created and will ask for confirmation to continue.  
`[imagen omitida: wiki id 41507]`

Select Create.

GeneXus will proceed to generate automatically the Java code based on the objects defined in the Knowledge Base.

Once the code generation process is finished the application will launch.

This is the Launchpad view, here you can observe all the GXSAP Leonardo Samples as tiles.

There is also the transaction created in the walkthrough.

Click on the ‘Image Classification Sample’ Tile.

`[imagen omitida: wiki id 41508]`

You are now viewing the List report for the Image Classification Sample records, since it is empty click on the Add icon to add a new image.

`[imagen omitida: wiki id 41509]`

To create a new record you must assign a unique Id, a Sample Name and select an image.

After filling the fields select ‘Change’ in the image icon.

`[imagen omitida: wiki id 41510]`

Now upload a local file browsing in your computer files.`[imagen omitida: wiki id 41511]`

Click ‘Confirm’ to create the Image Classification Sample record.

`[imagen omitida: wiki id 41512]`

Once you created the image record you are ready to select ‘Classify’ to call the SAP ML Image Classification Service.

Click on Classify for the new image record created.

`[imagen omitida: wiki id 41513]`

After selecting ‘Classify’ the image was processed by SAP ML image classification service and the categories and matching percentages are shown as you designed in the web form.

`[imagen omitida: wiki id 41514]`

Well done! You have successfully created a web example that stores data in HANA DB schema in SAP Cloud Platform, using GeneXus for SAP Systems Fiori Pattern to develop with a style guideline similar to SAP applications.

This example is using a SAP Leonardo Machine Learning pre-trained service to classify a given image into categories with the respective match percentage for each category.

If you are interested in working with more ML services you can browse the GXSAPLeonardoSamples Module to see how the other ML services samples were made.

If you are interested in creating a sample for  ML services that are not in this framework you can import the Open API from Tools-> Application Integration -> Open API.

You have reached the end of the walkthrough, now you have the know-how to start developing applications in GeneXus for SAP, calling SAP ML services and storing data in a HANA schema.
