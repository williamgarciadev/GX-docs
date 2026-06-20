---
title: "Http Connections Log Level property"
source_id: 33332
source_url: https://wiki.genexus.com/commwiki/wiki?33332
genexus_version: "18"
---

# Http Connections Log Level property

Sets the desired log level related to the HTTP connections between the device and the server side.

### [Values](#Values)

|  |  |
| --- | --- |
| **Debug** | Info level plus useful information for the developer is saved. |
| **Error** | Only errors are saved. |
| **Info** | Errors, warnings, and any other relevant information is saved. |
| **Off** | Default value. No log is saved. |
| **Warning** | Errors and warnings are saved. |

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

The order in terms of verbosity, from the least to the most verbose is Off, Error, Warning, Info, Debug.

Debug logs are compiled but stripped at runtime. Error, warning, and info, logs are always kept.

### [Samples](#Samples)

#### [Android](#Android)

**Debug**

```
D/Genexus-HTTP(2953): {
  "request": {
    "url": "http:\/\/apps5.genexus.com\/Id51f76c6843610d8c3116b4bee8828376\/gxmetadata\/gxversion.json",
    "method": "GET",
    "headers": {
      "DeviceId": "someID",
      "GeneXus-Language": "English",
      "GeneXus-Theme": "SimpleAndroid",
      "DeviceType": "1",
      "DeviceOSName": "Android",
      "DevicePlatform": "Android Phone",
      "DeviceOSVersion": "7.0",
      "GxTZOffset": "America\/Montevideo",
      "DeviceName": "generic_x86-unknown",
      "GXAppVersionName": "1.0",
      "GXAppVersionCode": "1.0",
      "Accept-Language": "en-US,en",
      "GeneXus-Agent": "SmartDevice Application"
    }
  }
}
D/Genexus-HTTP(2953): {
  "response": {
    "url": "http:\/\/apps5.genexus.com\/Id51f76c6843610d8c3116b4bee8828376\/gxmetadata\/gxversion.json",
    "statusCode": 200,
    "headers": {
      "Content-Type": "application\/json",
      "Last-Modified": "some date in GMT format",
      "Accept-Ranges": "bytes",
      "ETag": "\"028a62cad65d21:0\"",
      "Server": "Microsoft-IIS\/8.0",
      "X-Powered-By": "ASP.NET",
      "Access-Control-Allow-Origin": "http:\/\/editor.swagger.io",
      "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept",
      "Date": "some date GMT",
      "Content-Length": "24"
    },
    "bytes": 24,
    "data": "{ \"version\":\"1036181\"}\r\n"
  }
}
D/Genexus-HTTP(2953): {
  "request": {
    "url": "http:\/\/serverName\/AppName\/gxmetadata\/MainSD.android.json",
    "method": "GET",
    "headers": {
      "DeviceId": "ID",
      "GeneXus-Language": "English",
      "GeneXus-Theme": "SimpleAndroid",
      "DeviceType": "1",
      "DeviceOSName": "Android",
      "DevicePlatform": "Android Phone",
      "DeviceOSVersion": "7.0",
      "GxTZOffset": "America\/Montevideo",
      "DeviceName": "generic_x86-unknown",
      "GXAppVersionName": "1.0",
      "GXAppVersionCode": "1.0",
      "Accept-Language": "en-US,en",
      "GeneXus-Agent": "SmartDevice Application"
    }
  }
}

D/Genexus-HTTP(2953): {
  "response": {
    "url": "http:\/\/serverName\/AppName\/gxmetadata\/MainSD.android.json",
    "statusCode": 200,
    "headers": {
      "Content-Type": "application\/json",
      "Last-Modified": "Tue, 03 Jan 2017 09:43:44 GMT",
      "Accept-Ranges": "bytes",
      "ETag": "\"08872dfa565d21:0\"",
      "Server": "Microsoft-IIS\/8.0",
      "X-Powered-By": "ASP.NET",
      "Access-Control-Allow-Origin": "http:\/\/editor.swagger.io",
      "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept",
      "Date": "Tue, 03 Jan 2017 13:36:47 GMT",
      "Content-Length": "34"
    },
    "bytes": 34,
    "data": "{\"minor\":\"0\",\"major\":\"1\",\"uri\":\"\"}"
  }
}
D/Genexus-HTTP(2953): {
  "request": {
    "url": "http:\/\/serverName\/AppName\/rest\/Offdb?fmt=json",
    "method": "POST",
    "headers": {
      "GXSynchronizerVersion": "kG5bwpHrClQzlXMSMRwAhw==",
      "DeviceId": "ID",
      "GeneXus-Language": "English",
      "GeneXus-Theme": "SimpleAndroid",
      "DeviceType": "1",
      "DeviceOSName": "Android",
      "DevicePlatform": "Android Phone",
      "DeviceOSVersion": "7.0",
      "GxTZOffset": "America\/Montevideo",
      "DeviceName": "generic_x86-unknown",
      "GXAppVersionName": "1.0",
      "GXAppVersionCode": "1.0",
      "Accept-Language": "en-US,en",
      "GeneXus-Agent": "SmartDevice Application"
    },
    "body": "[]"
  }
}
D/Genexus-HTTP(2953): {
  "response": {
    "url": "http:\/\/serverName\/AppName\/rest\/Offdb?fmt=json",
    "statusCode": 200,
    "headers": {
      "Cache-Control": "private",
      "Content-Type": "application\/json; charset=utf-8",
      "Content-Encoding": "gzip",
      "Last-Modified": "Tue, 03 Jan 2017 13:36:47 GMT",
      "Server": "Microsoft-IIS\/8.0",
      "X-AspNet-Version": "4.0.30319",
      "Set-Cookie": "ASP.NET_SessionId=xay5td1ab2lzgvqvm0yu5zfz; path=\/; HttpOnly",
      "X-Powered-By": "ASP.NET",
      "Access-Control-Allow-Origin": "http:\/\/editor.swagger.io",
      "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept",
      "Date": "Tue, 03 Jan 2017 13:36:48 GMT",
      "Content-Length": "536"
    },
    "bytes": 2372,
    "data": "[...data...]"
  }
}
D/Genexus-HTTP(2953): {
  "request": {
    "url": "http:\/\/serverName\/AppName\/rest\/Offdb?fmt=json&event=gxconfirmsync",
    "method": "POST",
    "headers": {
      "GXSynchronizerVersion": "kG5bwpHrClQzlXMSMRwAhw==",
      "DeviceId": "ID",
      "GeneXus-Language": "English",
      "GeneXus-Theme": "SimpleAndroid",
      "DeviceType": "1",
      "DeviceOSName": "Android",
      "DevicePlatform": "Android Phone",
      "DeviceOSVersion": "7.0",
      "GxTZOffset": "America\/Montevideo",
      "DeviceName": "generic_x86-unknown",
      "GXAppVersionName": "1.0",
      "GXAppVersionCode": "1.0",
      "Accept-Language": "en-US,en",
      "GeneXus-Agent": "SmartDevice Application"
    },
    "body": "[[...data...]]"
  }
}
D/Genexus-HTTP(2953): {
  "response": {
    "url": "http:\/\/serverName\/AppName\/rest\/Offdb?fmt=json&event=gxconfirmsync",
    "statusCode": 200,
    "headers": {
      "Cache-Control": "private",
      "Content-Type": "application\/json; charset=utf-8",
      "Content-Encoding": "gzip",
      "Last-Modified": "Tue, 03 Jan 2017 13:36:47 GMT",
      "Server": "Microsoft-IIS\/8.0",
      "X-AspNet-Version": "4.0.30319",
      "X-Powered-By": "ASP.NET",
      "Access-Control-Allow-Origin": "http:\/\/editor.swagger.io",
      "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept",
      "Date": "Tue, 03 Jan 2017 13:36:53 GMT",
      "Content-Length": "22"
    },
    "bytes": 2,
    "data": "[]"
  }
}
```

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770). |


|  |
| --- |
| **Backlinks** |
| [Default Log Level property](https://wiki.genexus.com/commwiki/wiki?33333) | [Enable Logging property](https://wiki.genexus.com/commwiki/wiki?37876) | [HowTo: Enable logging for Native Mobile](https://wiki.genexus.com/commwiki/wiki?37846) |
| [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817) |

---
