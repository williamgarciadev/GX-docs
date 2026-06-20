---
title: "Http Error Handlers property"
source_id: 45949
source_url: https://wiki.genexus.com/commwiki/wiki?45949
genexus_version: "18"
---

# Http Error Handlers property

Enables HTTP error code handlers to control how to respond when an application error or exception occurs.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** Environment

### [Description](#Description)

When errors occur, the user shouldn't have to read technical error details that they cannot understand; instead, a friendly page that tells them what happened should be displayed. Also, proper handling of errors is recommended to hide sensitive technical information that can be exploited.

#### [How to specify default errors](#How+to+specify+default+errors)

To configure the property, go to Preferences > Environment.

`[imagen omitida: wiki id 58070]`

To enable this property, associate an HTTP Error Code to a File previously uploaded to the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) as a File object (it is recommended to use a plain HTML file). Typically, you can configure the following error types:

* 401: Unauthorized.
* 404: Page not found.
* 405: Method not allowed. A request was made of a page using a request method not supported by that page.
* 408: Timeout. Server timed out.
* 500: Internal Server Error.

### [Considerations](#Considerations)

When using the [.NET Framework Generator](https://wiki.genexus.com/commwiki/wiki?2892), valid values are between 400 and 999 inclusive; otherwise, the following error will be displayed:

```
The 'statusCode' attribute is invalid. Integer value must be between 400 and 999 inclusive.
```

In general, Java Application servers such as Tomcat will directly handle the 400 (Bad Request) error and it will not be delegated to the web application.

Also, be sure to always use the "Extract File" option in the uploaded file, when setting the Http Error Handlers property.

When using [Spring Boot](https://wiki.genexus.com/commwiki/wiki?55782), you need to name the error pages according to the error code you want to handle. For example, if you want to customize the page for error 404, you should name the file 404.html and for error 500, the file should be 500.html.

For more details, you can refer to the official Spring Boot documentation on [Custom error pages](https://docs.spring.io/spring-boot/docs/1.4.3.RELEASE/reference/html/boot-features-developing-web-applications.html#boot-features-error-handling-custom-error-pages).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Create a 404.html file with the following content and upload it to the Knowledge Base; set the extraction location path for your generators.

```
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>404 Error - Page Not Found</title>
  </head>
  <body>
    <div class="container">
      <main>
        <h1>Sorry, the page you requested was not found.</h1>
      </main>
    </div>
  </body>
</html>
```

Configure this property to bind the 404 HTTP error code to the 404.html file.

`[imagen omitida: wiki id 45953]`

With this declaration, if any 404 error occurs, your own error page is displayed to the end user.

`[imagen omitida: wiki id 45954]`

Note that your custom error page is relative to the web application’s context root.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build All](https://wiki.genexus.com/commwiki/wiki?5691).


|  |
| --- |
| **Backlinks** |
| [Configuration for secure deployment using GAM](https://wiki.genexus.com/commwiki/wiki?47243) | [Spring Boot in Java Application Development](https://wiki.genexus.com/commwiki/wiki?55782) |

---
