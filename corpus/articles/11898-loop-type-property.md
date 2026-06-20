---
title: "Loop type property"
source_id: 11898
source_url: https://wiki.genexus.com/commwiki/wiki?11898
genexus_version: "18"
---

# Loop type property

Defines the type of loop condition on the number of instances to be created.

### [Values](#Values)

|  |  |
| --- | --- |
| **Multi-Instance** | Specifies the number of times the task will be executed. The condition is evaluated once and returns the number of instances that must be created. Two properties are added to be configured. |
| **None** | No loop condition is defined. The task is executed once and continues the flow. This is the default value. |
| **Standard** | A standard loop activity has an associated Boolean expression that is evaluated after each loop cycle. Three properties are added to be configured. |

### [Scope](#Scope)

**Controls:** [Task](https://wiki.genexus.com/commwiki/wiki?17495)

### [Description](#Description)

You can configure the **Loop type property** for a [Task control](https://wiki.genexus.com/commwiki/wiki?17495) included in a [Business Process Diagram object](https://wiki.genexus.com/commwiki/wiki?16486).

The possible values of this property are described below:

**1) Multi-Instance**

Allows a Task to be executed a certain number of times.

When selecting this value, the following properties are offered to be configured:

1.1) **Expression Type property**

Allows you to choose how to determine the number of times the Task will be repeated. It can be by means of a Rule or a Procedure.

**Values:**

* **Rule:** Once this value is selected, the **Expression rule property** is offered to be completed. Allows you to specify an expression rule that will determine the number of times the Task should be repeated. It accepts characters, attributes, and relevant data (e.g. "Customer registration number"+CustomerId+&relevantData).
* **Procedure:** Once selected, the **Expression procedure property** is offered to be completed. It allows you to specify a Procedure object to determine the number of times the Task should be repeated.

           This Procedure must have the following [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862):

```
parm(in:&WorkflowProcessDefinition,in:&WorkflowProcessInstance,in:&WorkflowWorkitem,out: &numberofinstances);
```

           where the &numberofinstances variable must be Numeric (10).

1.2) **Ordering property**

Allows you to select the order in which the looped Tasks are executed, either all together or one at a time.

**Values:**

* **Sequential:** The instances are executed one at a time.
* **Parallel:** The instances are all executed at the same time.
  + If you select Parallel value, the **Flow condition property** is offered to be configured. It determines how the flow continues: whether after all Tasks are executed or when the first Task is executed, the flow continues.

                     1.2.1) The **Flow condition property** has the following values:

None  
For each completed instance, a parallel path will be followed.

One  
When the first instance is completed, the flow will continue. The other instances will continue running, but they will not create a new path when they are completed.

All  
The flow will only continue when all instances have been completed (synchronization).  
This is the default value.

Complex  
Defines an expression that will be executed when each instance is completed to check whether it should continue.

`[imagen omitida: wiki id 11908]`

If you select Complex value, the following property is offered to be configured:

1.2.2) **Complex flow condition type:** Checks if the flow should continue.

This property has two values: Rule and Procedure.

* **Rule:** If you select Rule value, a new property is offered to be completed, called: **Complex flow condition rule.**Specifies a rule to evaluate the condition. If the condition is met, the flow continues for the instance of that Task.
* **Procedure:** If you select the Procedure value, a new property is offered, called: **Complex flow condition procedure.**Allows you to specify a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) to evaluate the condition. If the condition is met, the flow continues for the instance of that Task.

          This Procedure must have the following [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862):

```
parm(in:&WorkflowProcessDefinition,in:&WorkflowProcessInstance,in:&WorkflowWorkitem,out: &code)
```

Where the &code variable must be Numeric (4.0). If the &code variable returns 1, the flow will continue; otherwise, if it returns 0, the flow will not be continued.

**2) None**

No loop condition is defined. The Task is executed once and continues the flow. This is the default value.

**3) Standard**

With this type of loop, each time a loop Task is executed, a condition is checked to see if the loop should continue.

When selecting this value, the following three properties are offered in the Properties window:

3.1) **Test Time property**

Allows you to select whether the check is before or after the Task is executed.

**Values:**

* Before: The condition is evaluated before executing the Task.
* After: The condition is evaluated after executing the Task.

3.2) **Condition Type property**

Allows you to select the way in which the condition is to be checked, either with a Rule or a Procedure.

**Values:**

* **Rule:** Specifies a rule to evaluate the condition. It accepts characters, attributes, and relevant data (e.g. "Customer registration number"+CustomerId+&relevantData). If you select this value, the **Condition rule property** is offered to be configured.
* **Procedure:** Allows you to specify a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) to evaluate the condition.

           This Procedure must have the following [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862):

```
parm(in:&WorkflowProcessDefinition,in:&WorkflowProcessInstance,in:&WorkflowWorkitem,out: &code);
```

           Where the &code variable must be Numeric (4.0). If the &code variable returns 1, the loop will continue; otherwise, if it  
           returns 0, the Task will be completed, and the flow will continue.  
           If you select this value, the **Condition procedure property** is offered to be configured.

3.3) **Maximum Iterations property**

Allows you to select the maximum number of times the Task can be executed in the loop. This property ignores the condition.

`[imagen omitida: wiki id 11907]`

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [See Also](#See+Also)

[Attribute definition](https://wiki.genexus.com/commwiki/wiki?6802)  
[Relevant Data](https://wiki.genexus.com/commwiki/wiki?11759)  
[HowTo: Implement Loop Tasks in GXflow](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?58366,,)


|  |
| --- |
| **Backlinks** |
| [BPD Subprocesses Embedded Properties](https://wiki.genexus.com/commwiki/wiki?17582) | [BPD Subprocesses Reusable Properties](https://wiki.genexus.com/commwiki/wiki?17580) | [Category:BPD Tasks](https://wiki.genexus.com/commwiki/wiki?17495) |
| [Table of contents:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [HowTo: Creating n instances of a task and automatically assigning them](https://wiki.genexus.com/commwiki/wiki?20635) | [Introduction to BPMN - Activities](https://wiki.genexus.com/commwiki/wiki?24916) |
| [None Task Properties](https://wiki.genexus.com/commwiki/wiki?17497) | [Reusable Properties](https://wiki.genexus.com/commwiki/wiki?12867) | [Script Task Properties](https://wiki.genexus.com/commwiki/wiki?17498) | [User Task Properties](https://wiki.genexus.com/commwiki/wiki?17499) |

---
