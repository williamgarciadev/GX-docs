---
title: "HowTo: Use Postman to access secure REST services defined via API Objects"
source_id: 50055
source_url: https://wiki.genexus.com/commwiki/wiki?50055
genexus_version: "18"
---

# HowTo: Use Postman to access secure REST services defined via API Objects

This article shows you the steps to use Postman to access a REST service if you have defined an [API object](https://wiki.genexus.com/commwiki/wiki?46151) and have configured the appropriate security.

Suppose you have an API object like [ListCustomers](https://wiki.genexus.com/commwiki/wiki?50051). In addition, you have configured the [security for your API object](https://wiki.genexus.com/commwiki/wiki?52840).

In this case, you have a restricted API object, so it is not enough to authenticate the application. In the same way, the user who tries to use the service must have the necessary permissions to be able to do so. Thus, set the Integrated Security Level property to Authorization, and modify the [Permission Prefix property](https://wiki.genexus.com/commwiki/wiki?17571) to easily identify the permission when assigning it to a user. In this example, the suffix "123" was added to the "APICustomers" permission name.

`[imagen omitida: wiki id 50274]`

Select [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691) and accept to create GAM tables.

Execute the GAM web back end and configure a new user, giving it permissions over the "apicustomers123\_Services\_Execute" permission name.

Read these articles to learn [how to create a Registration with GAM](https://wiki.genexus.com/commwiki/wiki?19913,,) and to give [permissions](https://wiki.genexus.com/commwiki/wiki?15912).

Identify Client\_Id from the application and copy its value in memory. It will be useful in the next steps.

Next, try to execute some method again using Postman or any other software tool.

Since security is now activated in the service, you will get this as a response:

```
{ 
      "error":{
           "code":"0",
           "message": "This service needs an Authorization Header"
      }
}
```

Follow the instructions on [HowTo: Develop Secure REST Web Services in GeneXus](https://wiki.genexus.com/commwiki/wiki?15918) to obtain the [Access\_token](https://wiki.genexus.com/commwiki/wiki?45320) using the Client\_Id of the application, the user and password of the registered user and the following header.

```
Content-Type
application/x-www-form-urlencoded
```

This token is the key to getting access to all the services. All you need to do is to set an Authorization header using the value returned by the [Access\_token](https://wiki.genexus.com/commwiki/wiki?45320). 

By using the Authorization method and managing permissions through the GAM backend, the new registered user will be able to execute all the services provided by the [API object](https://wiki.genexus.com/commwiki/wiki?46151).

The following picture shows you all the steps being run:

`[imagen omitida: wiki id 50035]`


|  |
| --- |
| **Backlinks** |
| [Toc:First Steps with API objects](https://wiki.genexus.com/commwiki/wiki?49754) | [HowTo: Access secure REST services defined via API Objects](https://wiki.genexus.com/commwiki/wiki?52864) |

---
