---
title: "GeneXus behind corporate proxy"
source_id: 55898
source_url: https://wiki.genexus.com/commwiki/wiki?55898
genexus_version: "18"
---

# GeneXus behind corporate proxy

One common challenge developers face is developing with GeneXus on a computer that is behind a corporate proxy.

This can be particularly problematic when it comes to building and deploying applications that rely on external dependencies, such as Java and Android apps that need to connect to Maven, or Angular apps that require a connection to NPM. This article explores the challenges and provides solutions for configuring NPM and Gradle to work seamlessly behind a corporate proxy.

## [Challenges faced behind a corporate proxy](#Challenges+faced+behind+a+corporate+proxy)

### [1. Gradle and Maven dependencies](#1.+Gradle+and+Maven+dependencies)

When working on Java and Android applications with GeneXus, Gradle is commonly used as the build tool. Gradle relies on Maven repositories to download dependencies, plugins, and libraries required for the project. However, when a Windows computer is behind a corporate proxy, Gradle may struggle to connect to external Maven repositories, leading to build failures.

### [2. Angular and NPM](#2.+Angular+and+NPM)

Angular applications developed in GeneXus often rely on NPM (Node Package Manager) to manage JavaScript libraries and packages. NPM requires internet access to download and update packages, which can be problematic when operating behind a corporate proxy that restricts internet access.

## [Configuring Gradle for a corporate proxy](#Configuring+Gradle+for+a+corporate+proxy)

To address the issues related to Gradle and Maven dependencies behind a corporate proxy, follow these steps:

1. **Configure Gradle Properties:**

   This configuration sets Gradle to use the corporate proxy for both HTTP and HTTPS requests.

   * Configure the proxy settings in the `gradle-wrapper.properties` file, which is located in the `/web/gradle/wrapper` directory.
   * Add the following lines to the file, replacing the placeholders with your corporate proxy details:

```
systemProp.http.proxyHost=your.proxy.host 
systemProp.http.proxyPort=your.proxy.port
systemProp.http.proxyUser=your.proxy.username 
systemProp.http.proxyPassword=your.proxy.password 
systemProp.https.proxyHost=your.proxy.host 
systemProp.https.proxyPort=your.proxy.port 
systemProp.https.proxyUser=your.proxy.username 
systemProp.https.proxyPassword=your.proxy.password
```

After making these changes, sync your Gradle project in GeneXus and try to build your Java or Android application. Gradle should now be able to connect to the Maven repositories through the corporate proxy.

## [Configuring NPM for a corporate proxy](#Configuring+NPM+for+a+corporate+proxy)

To enable NPM to work smoothly behind a corporate proxy for Angular applications, follow these steps:

1. **Create a `.npmrc` File:**

   * In your project's root directory (mobile/angular/%AppName), create a file named `.npmrc`.
2. **Edit `.npmrc`:**

   * Open the `.npmrc` file and add the following lines, replacing the placeholders with your corporate proxy details:

```
proxy=http://your.proxy.host:your.proxy.port 
https-proxy=http://your.proxy.host:your.proxy.port
(These configurations tell npm to route its requests through the corporate proxy for both HTTP and HTTPS connections.)
```

1. **Set Strict SSL to False (if necessary):**

   This setting allows NPM to work with self-signed certificates. Use it with caution, as it may expose you to security risks.

   * Some corporate proxies have self-signed SSL certificates. To avoid SSL certificate verification errors, you can add the following line to your `.npmrc` file: `strict-ssl=false`
2. **Install or Update Packages:**

   * After configuring NPM, run `npm install` or `npm update` to ensure that your Angular application's dependencies are installed or updated through the corporate proxy.

### [Environment variables for Mac proxy configuration](#Environment+variables+for+Mac+proxy+configuration)

To define a proxy for compiling iOS applications, you should define the following environment variables for the terminal or user that uses the Mac:  http\_proxy and https\_proxy

### [Environment variables for Windows proxy configuration](#Environment+variables+for+Windows+proxy+configuration)

Additionally, to ensure that your Windows system is configured correctly for proxy usage, set the following environment variables:

* **HTTP\_PROXY** and **HTTPS\_PROXY**: These environment variables should be set to the URL of your corporate proxy, including the protocol (for example, `http://proxy.example.com:8080`).
* **NO\_PROXY**: To skip the proxy for specific hosts like `localhost` and `127.0.0.1`, add these hosts to the `NO_PROXY` environment variable, separated by commas (for example, `localhost,127.0.0.1`).
* [Windows Proxy configuration](https://superuser.com/questions/1508302/how-to-set-network-proxy-to-ignore-localhost-on-windows-10)

By following these steps, you can configure Gradle and NPM to operate smoothly behind a corporate proxy when working with GeneXus. This allows you to develop and build Java, Android, and Angular applications without being hindered by proxy-related connectivity issues.

## [Configuring Maven for a corporate proxy](#Configuring+Maven+for+a+corporate+proxy)

Please read <https://maven.apache.org/guides/mini/guide-proxies.html>


|  |
| --- |
| **Backlinks** |
| [Manage Module References](https://wiki.genexus.com/commwiki/wiki?40172) |

---
