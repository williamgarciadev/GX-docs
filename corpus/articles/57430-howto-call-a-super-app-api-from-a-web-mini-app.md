---
title: "HowTo: Call a Super App API from a Web Mini App"
source_id: 57430
source_url: https://wiki.genexus.com/commwiki/wiki?57430
genexus_version: "18"
---

# HowTo: Call a Super App API from a Web Mini App

Below you can see some completed samples of how a [Web Mini App](https://wiki.genexus.com/commwiki/wiki?57422) can call a [Super App API](https://wiki.genexus.com/commwiki/wiki?58207).

In these samples, it is assumed that you have a Super App that exposes the following methods in its API:

```
Payment {
    PayWithUI(in:&Amount,out:&Reference)
        => PayPanel(&Amount,&Reference);

    PayWithoutUI(in:&Amount,out:&Reference)
        => PayProc(&Amount,&Reference);
}
```

Web Mini App metadata will be as follows:

```
{
   "EntryPointURL": "https://your_miniapp_services_url",
   "SuperAppObjectName": "GxSuperAppApi",
   "MiniAppObjectName": "MiniAppAPI"
}
```

For more details on how to create a [Super App object](https://wiki.genexus.com/commwiki/wiki?53457), you can read: [Super App API](https://wiki.genexus.com/commwiki/wiki?58207).

For more information on how to define a metadata in a Web Mini App, read: [HowTo: Define the metadata of a Web Mini App](https://wiki.genexus.com/commwiki/wiki?57429).

### [Samples](#Samples)

### [Case 1 - HTML + JavaScript](#Case+1+-+HTML+%2B+JavaScript)

In the first case, a JavaScript code is provided to interact with a Super App.

Here, you can find an example of how to call a Super App API from a Web Mini App built with HTML and JavaScript.

```
<html>
    <head>
    <script>
    function payWithUI() {
       try {
          var parm = 500;
          window.GxSuperAppApi.call("PayWithUI", [parm]).then(
             function (value) {
                document.getElementById("response").innerHTML = "Success: " +value;
             },
             function (error) {
                console.log(error);
             });
       } catch (error) {
          console.log(error);
       }
    }

    function payWithoutUI() {
       try {
          var parm = 200;
          window.GxSuperAppApi.call("PayWithoutUI", [parm]).then(
             function (value) {
                document.getElementById("response").innerHTML = "Success: " +value;
             },
             function (error) {
                console.log(error);
             });
       } catch (error) {
          console.log(error);
       }
    }

    function exitFromMiniApp() {
       window.MiniAppAPI.Exit();
    }
    </script>
    <style>
        Div{
            font-size: 20px;
        }
        Button{
            font-size: 20px;
        }
        table {
            border-collapse:separate; 
            border-spacing: 20px;
        }
    </style>
    </head>
    <body>
        <table>
            <tr>
                <td>
                    <button type="button"
                        onclick="payWithUI()">Pay With UI</button>
                </td>            
            </tr>
            <tr>
                <td>
                    <button type="button"
                        onclick="payWithoutUI()">Pay Without UI</button>
                </td>
            </tr>
            <tr>
                <td>
                    <button type="button"
                        onclick="exitFromMiniApp()">EXIT FROM MINI-APP</button>
                </td>            
            </tr>
            <tr>
                <td>
                    <div id="response"/>
                </td>            
            </tr>
        </table>    
    </body>
</html>
```

### [Case 2 - GeneXus Web](#Case+2+-+GeneXus+Web)

In this example, you can find a complete integration flow between a Web Mini App and a Super App through an [External Object](https://wiki.genexus.com/commwiki/wiki?5669) called PaymentsApi. At the bottom of this page, there is a link to download the KB sample.

The following file is loaded as paymentsApi.Js

```
var paymentsApi = {
   
   internal_errorCode: 0,
    
   errorCode: function() { 
    return this.internal_errorCode;
   },
    
   internal_errorDesc: "",
    
   errorDesc: function() { 
       return this.internal_errorDesc;
   },

   payWithUI: function (params) {

      var parmsArray = [];
      parmsArray.push(params);
      let reference = "";
      try {
         reference = window.GxSuperAppApi.call("PayWithUI", parmsArray).then(
            function (value) {
                return value; 
            },
            function (error) {
    this.internal_errorCode = 1;
            this.internal_errorDesc = error;
            });
      } catch (error) {
          this.internal_errorCode = 999;
        this.internal_errorDesc = error.message;

      }
      return reference;
   },

   payWithoutUI: function (params) {
      var parmsArray = [];
      parmsArray.push(params);
      let reference = "";
      try {
         reference = window.GxSuperAppApi.call("PayWithoutUI", parmsArray).then(
            function (value) {
                return value;
            },
            function (error) {
                this.internal_errorCode = 1;
            this.internal_errorDesc = error;
            });
      } catch (error) {
         this.internal_errorCode = 999;
       this.internal_errorDesc = error.message;
      }
      return reference;
   },

   exit: function () {
      window.MiniAppAPI.Exit();
   },
}
```

You need to create an External Object for communication with the following Structure:

`[imagen omitida: wiki id 57431]`

It is important to configure the API methods by setting the [Should Await For Completion property](https://wiki.genexus.com/commwiki/wiki?56479) to True.

The following events are programmed from a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) to make the call:

```
Event 'Pay With UI'
    &Reference = PaymentsApi.PayWithUI(&Amount)
    If PaymentsApi.ErrorCode = 0
        msg(&Reference.ToString().Trim())
    Else
        msg(str(PaymentsApi.ErrorCode)+!' - '+PaymentsApi.ErrorDesc)
    Endif
Endevent

Event 'Pay Without UI'
    &Reference = PaymentsApi.PayWithoutUI(&Amount)
    If PaymentsApi.ErrorCode = 0
        msg(&Reference.ToString().Trim())
    Else
        msg(str(PaymentsApi.ErrorCode)+!' - '+PaymentsApi.ErrorDesc)
    Endif
Endevent

Event 'Close'
   PaymentsApi.Exit()
Endevent
```

This sample allows you to call methods in PaymentsApi from your Web Mini App.

### [Download](#Download)

Download the KB sample from [Web Mini App API handling sample](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?56692,,).

### [Case 3 - GeneXus Web Previous Version](#Case+3+-+GeneXus+Web+Previous+Version)

Consider this sample as a workaround if you are working on versions prior to GeneXus 18 Upgrade 9.

The following file is loaded as File: paymentsPreviousVersionApi.Js

```
var paymentsPreviousVersionApi = {

   payWithUI: function (params) {

      var parmsArray = [];
      parmsArray.push(params);
      try {
         window.GxSuperAppApi.call("PayWithUI", parmsArray).then(
            function (value) {
               gx.fx.obs.notify("PaymentsPreviousVersionApi.PayWithUI_onResolve", [value]);
            },
            function (error) {
               gx.fx.obs.notify("PaymentsPreviousVersionApi.onError", [1, error]);
            });
      } catch (error) {
         gx.fx.obs.notify("PaymentsPreviousVersionApi.onError", [999, error]);
      }
   },

   payWithoutUI: function (params) {
      var parmsArray = [];
      parmsArray.push(params);
      try {
         window.GxSuperAppApi.call("PayWithoutUI", parmsArray).then(
            function (value) {
               gx.fx.obs.notify("PaymentsPreviousVersionApi.PayWithoutUI_onResolve", [value]);
            },
            function (error) {
               gx.fx.obs.notify("PaymentApi.onError", [1, error]);
            });
      } catch (error) {
         gx.fx.obs.notify("PaymentsPreviousVersionApi.onError", [999, error]);
      }
   },

   exit: function () {
      window.MiniAppAPI.Exit();
   },
}
```

You need to create an [External Object](https://wiki.genexus.com/commwiki/wiki?5669) for communication with the following Structure:

`[imagen omitida: wiki id 57441]`

The following events are programmed from a Web Panel object to make the call:

```
Event 'Pay With UI'
      PaymentsPreviousVersionApi.PayWithUI(&Amount)
Endevent

Event 'Pay Without UI'
    PaymentsPreviousVersionApi.PayWithoutUI(&Amount)
Endevent

Event 'Close'
   PaymentsPreviousVersionApi.Exit()
Endevent
```

And the following to obtain the answer:

```
Event PaymentsPreviousVersionApi.PayWithUI_onResolve(&Reference)
    msg(Format(!"OK - Reference: %1", &Reference))
EndEvent

Event PaymentsPreviousVersionApi.PayWithoutUI_onResolve(&Reference)
    msg(Format(!"OK - Reference: %1", &Reference))
EndEvent

Event PaymentsPreviousVersionApi.onError(&ErrorCode,&ErrorDesc)
   msg(Format(!"Error %1 - %2", &ErrorCode.ToString().Trim(),&ErrorDesc))
EndEvent
```

This sample allows you to call methods in PaymentsPreviousVersionApi from your Web Mini App and receive success or error events from the Super App. Events can be handled in the Web Panel object to perform additional actions or display messages to the user.

### [Download](#Download)

Download the KB sample from [Web Mini App API handling sample](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?56692,,).

### [Case 4 - GeneXus Angular Web Mini App](#Case+4+-+GeneXus+Angular+Web+Mini+App)

In this example, you can find a complete integration flow between an Angular Web Mini App and a Super App through an External Object called PaymentsApi.

Create a library in npm with the following Structure:

```
class PaymentsApi {

   static internal_errorCode = 0;

   static ErrorCode = function () {
      return PaymentsApi.internal_errorCode;
   };

   static internal_errorDesc = "";

   static ErrorDesc = function () {
      return PaymentsApi.internal_errorDesc;
   };

   static async payWithUI(params) {
      var parmsArray = [];
      parmsArray.push(params);
      let reference = "";
      try {
         reference = window.GxSuperAppApi.call("PayWithUI", parmsArray).then(
            function (value) {
               return value;
            },
            function (error) {
               PaymentsApi.internal_errorCode = 1;
               PaymentsApi.internal_errorDesc = error;
               return "";
            }
         );
      } catch (error) {
         PaymentsApi.internal_errorCode = 999;
         PaymentsApi.internal_errorDesc = error.message;
      }
      return reference;
   };

   static async payWithoutUI(params) {
      var parmsArray = [];
      parmsArray.push(params);
      let reference = "";
      try {
         reference = window.GxSuperAppApi.call("PayWithoutUI", parmsArray).then(
            function (value) {
               return value;
            },
            function (error) {
               PaymentsApi.internal_errorCode = 1;
               PaymentsApi.internal_errorDesc = error;
               return "";
            }
         );
      } catch (error) {
         PaymentsApi.internal_errorCode = 999;
         PaymentsApi.internal_errorDesc = error.message;
      }
      return reference;
   };

   static exit() {
      window.MiniAppAPI.Exit();
   }
}

module.exports = {
   PaymentsApi,
};
```

You need to create an [External Object](https://wiki.genexus.com/commwiki/wiki?5669) for communication with the following Structure:

`[imagen omitida: wiki id 57442]`

It is important to set the API methods with the Should Await for Completion property set to True.

The following events are programmed from a Web Panel object to make the call:

```
Event 'Pay With UI'
    &Reference = PaymentsApi.payWithUI(&Amount)
    If PaymentsApi.errorCode = 0
        msg(&Reference.ToString().Trim())
    Else
        msg(str(PaymentsApi.ErrorCode)+!' - '+PaymentsApi.ErrorDesc)
    Endif
Endevent

Event 'Pay Without UI'
    &Reference = PaymentsApi.payWithoutUI(&Amount)
    If PaymentsApi.errorCode = 0
        msg(&Reference.ToString().Trim())
    Else
        msg(str(PaymentsApi.ErrorCode)+!' - '+PaymentsApi.ErrorDesc)
    Endif
Endevent

Event 'Close'
   PaymentApi.exit()
Endevent
```

This sample allows you to call methods in PaymentsApi from your Angular Web Mini App.

### [Download](#Download)

Download the KB sample from [Angular Web Mini App API handling sample](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?56675,,).


|  |
| --- |
| **Backlinks** |
| [Table of contents:GeneXus Super Apps and Mini Apps](https://wiki.genexus.com/commwiki/wiki?50899) | [HowTo: Call a Super App API from a Native Mobile Mini App](https://wiki.genexus.com/commwiki/wiki?58185) | [Super App API](https://wiki.genexus.com/commwiki/wiki?58207) |

---
