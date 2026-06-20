---
title: "Angular application - Troubleshooting"
source_id: 46352
source_url: https://wiki.genexus.com/commwiki/wiki?46352
genexus_version: "18"
---

# Angular application - Troubleshooting

This is a list of issues that could happen when you develop Angular applications with GeneXus, and instructions to solve them.

#### [**1. When running the Angular application from GeneXus IDE, it opens a cmd window and closes it, but the app won't start.**](#1.+When+running+the+Angular+application+from+GeneXus+IDE%2C+it+opens+a+cmd+window+and+closes+it%2C+but+the+app+won%27t+start.)

**Cause:**The reason could be an error in the compile or start stage.

**Solution:**

1. Open a node.js command line window.
2. In the KB directory, CD to <target environment>\mobile\angular\<main>
3. Run command "npm start"

#### [**2. When running the Angular application from GeneXus IDE, during compile stage the following error appears:**](#2.+When+running+the+Angular+application+from+GeneXus+IDE%2C+during+compile+stage+the+following+error+appears%3A)

```
Failed to compile entry-point ........ (`es2015` as esm2015) due to compilation errors:
node_modules/@angular/common/common.d.ts:114:22 - error NG6002: .......
```

**Cause:**There was a problem in the install/compile stage.

**Solution:**

1. Stop the command window serving the Angular app
2. Delete *node\_modules* folder, *package-lock.json, run,build, run.install*files from the Angular KB directory: <target environment>\mobile\angular\<main>
3. Open a node.js command line window.
4. Run the command "npm install"
5. Run the command "npm start"

#### **3. When running the Angular application, the compile/start stage runs smoothly, but when it starts the browser the page is empty.**

**Cause:**Start the browser debugger and read the console output to look for an error. If the error states: .......Could not find "emod" .....  
So, there was a problem in the install/compile stage.

**Solution:**

1. Stop the command window serving the Angular app
2. Delete *node\_modules* folder *package-lock.json, run,build, run.install*files from the Angular KB directory: <target environment>\mobile\angular\<main>
3. Open a node.js command line window.
4. Run the command "npm install"
5. Run the command "npm start"

#### **4. Error "'npm' ERR! Unexpected end of JSON input while parsing near"**

**Cause:**When running the Angular application from the GeneXus IDE or running an 'npm install' command,this error may occur.

The following JSON file consists of a random example of the failure. The important part of the error is as follows:

**"Unexpected end of JSON input while parsing near... "**

Full trace:

```
C:\Models\TravelAgency_videosGX17_FrontEnd\Data084\mobile\Angular\Attractions_CFPanel>npm install
npm WARN deprecated core-js@2.6.11: core-js@<3 is no longer maintained and not recommended for usage due to the number of issues. Please, upgrade your dependencies to the actual version of core-js@3.
npm WARN deprecated joi@9.2.0: This version has been deprecated in accordance with the hapi support policy ([http://hapi.im/support|hapi.im/support]). Please upgrade to the latest version to get the best features, bug fixes, and security patches. If you are unable to upgrade at this time, paid support is available for older versions ([http://hapi.im/commercial|hapi.im/commercial]).
npm WARN deprecated request@2.88.2: request has been deprecated, see [https://github.com/request/request/issues/3142]
npm WARN deprecated popper.js@1.16.1: You can find the new Popper v2 at @popperjs/core, this package is dedicated to the legacy v1
npm WARN deprecated fsevents@1.2.13: fsevents 1 will break on node v14+ and could be using insecure binaries. Upgrade to fsevents 2.
npm WARN deprecated hoek@4.2.1: This version has been deprecated in accordance with the hapi support policy ([http://hapi.im/support|hapi.im/support]). Please upgrade to the latest version to get the best features, bug fixes, and security patches. If you are unable to upgrade at this time, paid support is available for older versions ([http://hapi.im/commercial|hapi.im/commercial]).
npm WARN deprecated items@2.1.2: This module has been deprecated in accordance with the hapi support policy ([http://hapi.im/support|hapi.im/support]). Please upgrade to the latest version of hapi to get the best features, bug fixes, and security patches. If you are unable to upgrade at this time, paid support is available for older versions ([http://hapi.im/commercial|hapi.im/commercial]).
npm WARN deprecated topo@2.0.2: This version has been deprecated in accordance with the hapi support policy ([http://hapi.im/support|hapi.im/support]). Please upgrade to the latest version to get the best features, bug fixes, and security patches. If you are unable to upgrade at this time, paid support is available for older versions ([http://hapi.im/commercial|hapi.im/commercial]).
npm WARN deprecated har-validator@5.1.5: this library is no longer supported
npm WARN deprecated mkdirp@0.5.1: Legacy versions of mkdirp are no longer supported. Please update to mkdirp 1.x. (Note that the API surface has changed to use Promises in 1.x.)
npm WARN deprecated request-promise-native@1.0.9: request-promise-native has been deprecated because it extends the now deprecated request package, see [https://github.com/request/request/issues/3142]
npm WARN deprecated resolve-url@0.2.1: [https://github.com/lydell/resolve-url#deprecated]
npm WARN deprecated urix@0.1.0: Please see [https://github.com/lydell/urix#deprecated]
npm ERR! Unexpected end of JSON input while parsing near '...ies":{"typescript":">'
```

**Solution:**

1. Open a node js command prompt (as Administrator) and run the following command:

```
npm cache clean --force
```

2. Delete *node\_modules* folder and *package-lock.json* file from the Knowledge Base directory.

3. On the node js command prompt, run this command:

```
npm install
```

You should now be able to execute your Angular application.

#### [**5. Error "'npm' is not recognized as an internal or external command"**](#5.+Error+%22%27npm%27+is+not+recognized+as+an+internal+or+external+command%22)

#### [When trying to run the application, an error similar to the following appears:](#When+trying+to+run+the+application%2C+an+error+similar+to+the+following+appears%3A)

```
Command: cmd /c npm install
'npm' is not recognized as an internal or external command,
operable program or batch file.
Failed: Angular Execution
Failed: Run MyMain
```

**Cause:**NodeJS is not correctly installed.

**Solution:**Check [Angular Generator requirements](https://wiki.genexus.com/commwiki/wiki?42541) or try closing GeneXus and opening it again.

#### [**6.****When trying to make an HTTP request to a target domain different than the source domain, CORS (Cross-Origin Resource Sharing) errors can occur.**](#6.+When+trying+to+make+an+HTTP+request+to+a+target+domain+different+than+the+source+domain%2C+CORS+%28Cross-Origin+Resource+Sharing%29+errors+can+occur.)

**Cause:**Browsers block requests that are not from the same domain as a security mechanism. So, when trying to make an HTTP request (an image, video, file, etc. is requested) to a target domain that is different from the source domain, CORS (Cross-Origin Resource Sharing) errors can be displayed in the browser.

Samples

1)  The following code tries to apply the [AddFile method](https://wiki.genexus.com/commwiki/wiki?7046) to a variable based on the [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932):

```
&httpclient.AddFile('UserImage', "https://www.imagedomain.com/media/images/img.svg")
```

The following error may be displayed in the browser:

```
Access to fetch at 'https://www.imagedomain.com/media/images/img.svg' from origin 'http://localhost:60808' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource. If an opaque response serves your needs, set the request's mode to 'no-cors' to fetch the resource with CORS disabled.
```

2) The following code tries to obtain an image and use the [Image manipulation API](https://wiki.genexus.com/commwiki/wiki?39415)

```
&image.FromURL('https://www.imagedomain.com/media/images/img.jpg')
&image.Rotate(90)
```

The following error may be displayed in the browser:

```
ERROR Error: Uncaught (in promise): SecurityError: Failed to execute 'toDataURL' on 'HTMLCanvasElement': Tainted canvases may not be exported.
```

**Solution:**It is recommended to have the files, images, or videos uploaded to the source domain. There are other ways to avoid CORS errors (for example, if you have access to the server corresponding to the target domain, you can specify which domains are authorized to make requests (by adding the Access-Control-Allow-Origin header)), but to avoid security problems, the recommended solution is to have the files, images, or videos uploaded to the source domain.


|  |
| --- |
| **Backlinks** |
| [Toc:Angular Application Development](https://wiki.genexus.com/commwiki/wiki?42539) |

---
