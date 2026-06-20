---
title: "Grouping tasks and processes in pools and lanes"
source_id: 24777
source_url: https://wiki.genexus.com/commwiki/wiki?24777
genexus_version: "18"
---

# Grouping tasks and processes in pools and lanes

The BPMN standard provides mechanisms to document the information in a diagram, like the tasks related to each other, if they belong to the same participant or business entity, or if they are associated with a specific function or role in the company.

This is done using Pools and Lanes, which are part of [Swimlanes](https://wiki.genexus.com/commwiki/wiki?24919).

### [Pools](#Pools)

In the [Travel Agency example](https://wiki.genexus.com/commwiki/wiki?24748,,), the only business entity involved is the Travel Agency, which has a single process that it is called: Ticket Reservation.

To indicate this, a Pool symbol is used; in the example, it covers the entire diagram.

`[imagen omitida: wiki id 24783]`

If the diagram had another business entity with its own process, you would group the tasks of this process in another pool.

### [Lanes](#Lanes)

Another thing you could do to add better documentation to our diagram is to group tasks associated with a specific role or function in the company.

In the example, you want to make a group with all the tasks related to customer care and another group with all the other tasks.

To indicate this, the Lane symbols are used. A pool can include one or more lanes.

`[imagen omitida: wiki id 24784]`

### [External entities](#External+entities)

It's worth pointing out that even though several process tasks interact with the customer, it isn’t part of the process; it is an external entity.

This can be modeled using dotted lines to show interaction between the process and the customer.

`[imagen omitida: wiki id 24798]`


|  |
| --- |
| **Backlinks** |
| [Hide value property](https://wiki.genexus.com/commwiki/wiki?40163) |

---
