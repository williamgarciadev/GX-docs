---
title: "My first BPM Application"
source_id: 11218
source_url: https://wiki.genexus.com/commwiki/wiki?11218
genexus_version: "18"
---

# My first BPM Application

By means of the following example, it is explained that it is a Workflow.

Topic: Booking flight tickets. This process is: Enter the reservation data through an operator; if the customer is not registered, the system automatically does it. Next, an availability check is made and if the result of this check is positive, the process is completed. Otherwise, the control is returned to the first item, where the details can be changed.

This simplified example has only a few steps, but they are well communicated, diagrammed and consistent. Here lies the importance of a Workflow: to automate controls that can be automated, with the least possible intervention from programmers. By following simple steps, you can build robust Workflow applications in [GeneXus](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?35351,,).

In sum, the idea behind a Workflow process is that a tight integration of the available tools ([GeneXus](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?35351,,) tools, in this case) can provide seamless collaboration among all the information systems of a company, thus accelerating management processes and driving the business forward in a dynamic, vertical manner.

Here you have a simple, practical example that illustrates the steps needed to complete it:

* Creating process objects
* Creating the activity diagram that models the process
* Associating objects to the diagram
* Running the process

This is a simple example that shows you how to use GXflow within the IDE. It represents a simplified process for booking airline tickets, which consists of entering the reservation details into the system, with the operator registering any customer that is not registered. If the customer is registered already, the control will go straight to checking availability. If the reservation is available, the process ends, and if it's not available, the flow will return to where the reservation was entered to update the data.

#### [**Step 1: Creating the objects that will be part of the process**](#Step+1%3A+Creating+the+objects+that+will+be+part+of+the+process)

Two Transactions will be needed: Reservation and Customer.

##### [Reservation Transaction](#Reservation+Transaction)

`[imagen omitida: wiki id 43734]`

Notes: Note also that the CustomerId attribute is defined to allow nulls, which is necessary for the example to work properly, also ReservationId is auto number.

*Rules*

Rule to make the ReservationAvailable attribute invisible, as this attribute is used when the reservation is already entered and you want to indicate whether it's available or not.

```
ReservationAvailable.Visible = False If Insert;
```

##### [Customer Transaction](#Customer+Transaction)

`[imagen omitida: wiki id 43735]`

CustomerId is Autonumber

##### [AssignToCustomer Procedure](#AssignToCustomer+Procedure)

Consider a Procedure: Once the reservation and user are entered, it assigns that reservation to that user.

*Rules*

```
Parm(in:&ReservationId, in:&CustomerId);
```

*Variables*

ReservationId (based on the ReservationId attribute)

CustomerId (based on the CustomerId attribute)

*Code*

```
For each Reservation 
     Where ReservationId = &ReservationId
     CustomerId = &CustomerId
Endfor
```

#### [**Step 2: Creating the activity diagram that models the process**](#Step+2%3A+Creating+the+activity+diagram+that+models+the+process)

To add an activity diagram all you have to do is add the [Business Process Diagram object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?16486,,), like it is possible to do with any other object.

`[imagen omitida: wiki id 51988]`

**Step 3: Associating the objects to the diagram**

To mark the beginning of the process, drag a [None Start Event](None Start Event in BPD) symbol.

The first associated object will be the Reservation Transaction. To associate it, drag it from the Folder View to the line that connects the Start and End connectors in the diagram.

Or, drag a [User Task](https://wiki.genexus.com/commwiki/wiki?59395) from the [Toolbox](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?16487,,), to the properties windows and press the button in the [Application property](https://wiki.genexus.com/commwiki/wiki?11884).

`[imagen omitida: wiki id 11219]`

Relevant data with the same name and data type as the Transaction's primary key is created right after the project is added. This data, just like the rest of the relevant information, will be known throughout the flow.

The second step consists of adding the conditional that defines whether or not the customer is registered and associated with the Reservation Transaction. To do so, add the exclusive gateway symbol from the diagram toolbar (by default it is located on the right-hand side of the screen), as shown in the figure below.

`[imagen omitida: wiki id 43738]`

Once the gateway has been inserted, you have to define the condition that will make the flow follow the usual course or follow the alternative course to register a customer. First, you need to add the Customer Transaction to the diagram and connect it with the conditional's alternative route, as follows:

`[imagen omitida: wiki id 11221]`

Note: To connect the gateway with the 'Customer' task, click the right-hand side of the conditional and drag the arrow to the left-hand side of the task. Its type is defined in the route properties.

To complete the conditional, you have to define the condition that will make the flow follow one route or the other. To this end, the IDE offers a condition editor that allows you to express conditions based on attributes and relevant data. Double-click the edge that connects the customer record and enters the following expression:

`[imagen omitida: wiki id 7559]`

By defining this condition, non-registered customers (customerId = 0) are registered.

Next, following the usual flow, the Reservation Transaction is added again. This task evaluates whether the reservation is available to be issued; change its name by pressing F2 button.

`[imagen omitida: wiki id 11222]`

Now select the connector that goes to ReservationAvailability, go to properties and in Condition type select "Default"

`[imagen omitida: wiki id 43776]`

Netx, Double-clicking the gateway symbol displays a summary of the conditions, as shown in the figure below:

`[imagen omitida: wiki id 43778]`

Once the reservation availability has been determined, another gateway must be defined as follows to evaluate the condition:

`[imagen omitida: wiki id 43766]`

If the reservation is available, the process is finished. If it's not available, the flow goes back to the initial task in order to change the reservation details.

To complete the flow, you have to define the alternative course to be followed when the customer is not registered. So, after registering the customer, you have to assign him or her to the reservation and check availability. To do so, you need to add the Procedure previously created (AssignToCustomer) and the connection routes as follows:

`[imagen omitida: wiki id 43777]`

Once the Procedure is added to the diagram, the parameter rule (parm) is automatically evaluated. If attributes or variables with the same name and type as the relevant data are found, they will be instantiated with their values. In this case, the **&ReservationId** and **&CustomerId** variables will be associated with the values of the corresponding relevant data.

#### [**Step 4: Running the process**](#Step+4%3A+Running+the+process)

Lastly, the process is run. Before running the process for the first time, do a **Build All** (Build command menu option). Right-click the diagram listed in the Folder View and press the 'RUN'.

`[imagen omitida: wiki id 51989]`

Next, GeneXus performs the necessary actions to run this diagram and show the changes made. The steps that follow are:

* Update workflow objects
* Specify objects
* Generate objects
* Compile workflow objects
* Impact the diagram on the database

Whether or not all these steps are performed will depend on the changes made; that is to say, a change in the diagram will cause all its objects to be specified, generated and compiled, impacting the diagram.

A browser will be automatically opened with the application as shown in the figure below:

`[imagen omitida: wiki id 51990]`

When the prototyper is executed, a new instance of the process to be prototyped is generated. It allows you to perform all the steps without defining roles or assigning them to the user that is prototyping.

Below is the process flow for both cases: the first case corresponds to a customer that has to be registered, and the second case corresponds to a customer that is already registered in the system.

#### [**Case 1: When the user needs to be registered**](#Case+1%3A+When+the+user+needs+to+be+registered)

The reservation details are entered and the CustomerId field is left blank (the customer is not registered yet).

`[imagen omitida: wiki id 51991]`

Next, you have to register the customer.

`[imagen omitida: wiki id 51992]`

Once the reservation and customer are registered, the Procedure that assigns the customer to the reservation is automatically executed.

To end the process, you have to define whether the reservation is available or not.

`[imagen omitida: wiki id 51993]`

#### [**Case 2: When the customer is already registered**](#Case+2%3A+When+the+customer+is+already+registered)

Create a new task as shown in the figure below and enter the reservation details including the customer, who in this case is registered in the system.

`[imagen omitida: wiki id 51994]`

Next, the reservation is set to 'not available' and the flow returns to the beginning, where the reservation data can be changed.

### [See Also](#See+Also)

[Structure Editor](https://wiki.genexus.com/commwiki/wiki?3913)


|  |
| --- |
| **Backlinks** |
| [Beginners in GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?20955) | [Table of contents:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |
| [HowTo: Configure GXflow Client for Native Mobile from xpz](https://wiki.genexus.com/commwiki/wiki?50551) | [HowTo: Set up an independent Data Store for Workflow tables](https://wiki.genexus.com/commwiki/wiki?25683) | [Looking for help in GeneXus BPM Suite and GXflow?](https://wiki.genexus.com/commwiki/wiki?20951) |
| [Model Automation](https://wiki.genexus.com/commwiki/wiki?25115) | [Modeling with GeneXus](https://wiki.genexus.com/commwiki/wiki?25071) | [My first BPM Native Mobile application](https://wiki.genexus.com/commwiki/wiki?50516) |

---
