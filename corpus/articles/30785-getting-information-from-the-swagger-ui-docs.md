---
title: "Getting information from the Swagger UI docs"
source_id: 30785
source_url: https://wiki.genexus.com/commwiki/wiki?30785
genexus_version: "18"
---

# Getting information from the Swagger UI docs

Below is a use case of a RESTful service (in fact, it's a [Business Component exposed as a Rest service](https://wiki.genexus.com/commwiki/wiki?28214)).

Suppose that you want to build a consumer for that service.

To do so, you activate the [Generate OpenAPI interface property](https://wiki.genexus.com/commwiki/wiki?31859) so that the default.yaml file is available.

As you need to implement a consumer, the documentation will help you for that purpose.

The information of the OpenAPI (Swagger) docs can be easily read using the [OpenAPI import tool](https://wiki.genexus.com/commwiki/wiki?31864). However, here it is explained how the same process could be done (with a rational analysis effort) using the Swagger UI tool.

Consider the Product [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) structure defined as follows:

```
Product
{
  ProductId*
  ProductName
  ProductPrice
  ProductStock
}
```

Its properties are set as follows:

* Business Component property = True
* Expose as Web Service property = True
* Web Service Protocol property= Rest Protocol

Let's focus on the HTTP POST method. For this HTTP method in particular, the default.yaml file includes the following lines:

```
/Product/{ProductId}:
post:
      tags:
        - Product
      summary: "Inserts a Product"
      parameters:
        - name: "ProductId"
          in: "path"
          description: "Product Id"
          required: true
          type: "integer"
          format: "int32"
        - name: "Product"
          in: "body"
          description: "SDT of Product"
          required: false
          schema:
            $ref: "#/definitions/Product"
       
      responses:
        200:
          description: "Successful operation"
          schema:
            $ref: "#/definitions/Product_z"
        404:
          description: "Not found"
```

Graphically, it is represented by the [Swagger UI](http://swagger.io/swagger-ui/) as shown below:

`[imagen omitida: wiki id 30787]`

You can click on "Try this operation" and complete the request form that appears, which looks as shown in this example:

`[imagen omitida: wiki id 30788]`

After completing the form, you will have the following summary of the HTTP Request where you can get information about the HTTP headers used to execute the HTTP POST verb, and the JSON body format.

`[imagen omitida: wiki id 30789]`

The JSON Body can be imported in GeneXus using the JSON Import tool (Tools > Application integration), and the correct SDT for that JSON format will be automatically created in the KB.


|  |
| --- |
| **Backlinks** |
| [OpenAPI import tool](https://wiki.genexus.com/commwiki/wiki?31864) | [OpenAPI import tool (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54370) |

---
