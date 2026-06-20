---
title: "ContextPath Rewrite: X-Forwarded Headers Support (App behind Reverse Proxy) (GeneXus 18 Upgrade 10)"
source_id: 59271
source_url: https://wiki.genexus.com/commwiki/wiki?59271
genexus_version: "18"
---

# ContextPath Rewrite: X-Forwarded Headers Support (App behind Reverse Proxy) (GeneXus 18 Upgrade 10)

When your application is behind a Reverse Proxy, the Web Server lacks direct access to the client's original host, protocol, port, and IP address. As a result, properties in [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932) and [HttpRequest data type](https://wiki.genexus.com/commwiki/wiki?6933)  (such as BaseURL, Host, Port, and RemoteAddress) may display inaccurate information, since the client is not directly accessing the WebService.

## [Standard HTTP Headers for Proxy Information](#Standard+HTTP+Headers+for+Proxy+Information)

To provide accurate information to the WebServer, use these standard HTTP headers:

* **X-Forwarded-Port:**gives the port the client connected to on the proxy (e.g. 80 or 443)
* **X-Forwarded-Proto:** gives the protocol the client used to connect to the proxy (http or https)
* **X-Forwarded-Host:** gives the content of the Host header the client sent to the proxy.
* **X-Forwar****ded****-For:**allows a proxy to inform the web application of the source IP from which it is being accessed.

By forwarding these HTTP headers from the Proxy, you can effectively "rewrite" the Host, port, Protocol, and client IP information.

## [Rewriting the ContextPath](#Rewriting+the+ContextPath)

Rewriting the contextPath is not something that is normally seen or recommended.

### [Samples](#Samples)

Application hosted on WebServer app: app1:

* http://websserver/app1

But needs to be accessible via a Reverse Proxy by the following way:

* http://public-host/subfolder/apps/app1

The problem here is that the Working Application does not know that it is being server to the "outside world" by context path: "/subfolder/apps/app1".

So all the Realtive host URLS returned by the App are: "/app1" and not "/subfolder/apps/app1". This can lead to access problems from the "outside world".

This is something known as Rewriting the Context Path.

There is a draft RFC request to standardize a new Http Header for this scenario: "X-Forwarded-Prefix". However, is still not supported by many WebServers.

One solution for this problem is to include a filter that reMaps the requestPath automcatically.

This can be done by the following steps.

## [Implementing Context Path Rewriting](#Implementing+Context+Path+Rewriting)

### [For Java Applications](#For+Java+Applications)

Using this Project: <https://github.com/qaware/x-forwarded-filter>

### [Steps](#Steps)

1. Download [JAR file](https://repo1.maven.org/maven2/de/qaware/xff/x-forwarded-filter/1.0/x-forwarded-filter-1.0.jar)
2. Put JAR file on web server lib
3. Add the following to web.xml\*
4. Configure the Proxy to Forward the Header: <"X-Forwarded-Prefix"> = "/subfolder/apps/app1"

```
<!--ForwardedHeaderFilter MUST be first filter in chain -->
<filter>
    <filter-name>ForwardedHeaderFilter</filter-name>
    <filter-class>de.qaware.xff.filter.ForwardedHeaderFilter</filter-class>
    <init-param>
        <param-name>headerProcessingStrategy</param-name>
        <param-value>EVAL_AND_REMOVE</param-value>
    </init-param>
    <init-param>
        <param-name>xForwardedPrefixStrategy</param-name>
        <param-value>REPLACE</param-value>
    </init-param>
    <!-- 
    <init-param>
        <param-name>enableRelativeRedirects</param-name>
        <param-value>false</param-value>
    </init-param>
    -->
</filter>
<filter-mapping>
    <filter-name>ForwardedHeaderFilter</filter-name>
    <url-pattern>/*</url-pattern>
</filter-mapping>
```

### [For .NET Applications](#For+.NET+Applications)

1. Enable the ForwardedHeaders middleware by setting the environment variable:

```
ASPNETCORE_FORWARDEDHEADERS_ENABLED=true
```

2. Configure your reverse proxy (e.g., Nginx) to set the appropriate headers:

```
server {
    listen 80;
    server_name server.example.com;

    location / {
        proxy_pass http://localhost:8083;
        proxy_http_version 1.1;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-Prefix "/subfolder/apps/app1";
        proxy_cache_bypass $http_upgrade;
    }
}
```

## [Scope](#Scope)

**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258), [.NET](https://wiki.genexus.com/commwiki/wiki?38604)

## [Availability](#Availability)

These 4 Headers are available since [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?45901,,).


|  |
| --- |
| **Backlinks** |
| [RemoteAddr function (GeneXus 18 Upgrade 10 or prior)](https://wiki.genexus.com/commwiki/wiki?59268) |

---
