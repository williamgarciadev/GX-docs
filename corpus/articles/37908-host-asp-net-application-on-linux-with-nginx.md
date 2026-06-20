---
title: "Host ASP.NET application on Linux with Nginx"
source_id: 37908
source_url: https://wiki.genexus.com/commwiki/wiki?37908
genexus_version: "18"
---

# Host ASP.NET application on Linux with Nginx

This guide explains setting up a production-ready ASP.NET application generated with [GeneXus .NET generator](https://wiki.genexus.com/commwiki/wiki?38604) on Linux (Ubuntu 14.04) with Nginx as a reverse proxy.

## [Prerequisites for .NET on Linux](#Prerequisites+for+.NET+on+Linux)

See [Linux prerequisites](https://docs.microsoft.com/es-es/dotnet/core/install/dependencies?pivots=os-linux&tabs=netcore31) for other Linux versions.

### [Install .NET for Ubuntu 14.04](#Install+.NET+for+Ubuntu+14.04)

1. Register the Microsoft Product key as trusted.

```
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg
```

2. Set up the desired version host package feed.

```
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-ubuntu-trusty-prod trusty main" > /etc/apt/sources.list.d/dotnetdev.list' 
sudo apt-get update
```

3. Install .NET

```
sudo apt-get install dotnet-sdk-5.0
```

5.Run the dotnet --version command to prove the installation succeeded.

```
dotnet --version
```

## [Copy over the app](#Copy+over+the+app)

Deploy your application using Build -> Deploy Application and then and copy it to the target linux.

From command line **positioned in web directory** (or equivalent) run:

```
dotnet bin/GxNetCoreStartup.dll
```

Your application can be tested at for example: http://localhost:5000/Webpanel1.aspx (see dotnet command output to check port)

## [Configure Nginx as a reverse proxy server](#Configure+Nginx+as+a+reverse+proxy+server)

1.Install Nginx

```
sudo apt-get install nginx
```

2. Start it by running:

```
sudo service nginx start
```

3.Configure Nginx

To configure Nginx as a reverse proxy to forward requests to our ASP.NET app, modify `/etc/nginx/sites-available/default`. Open it in a text editor, and replace the contents with the following:

```
server {
    listen 80;
    location / {
        proxy_pass http://localhost:5000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection keep-alive;
        proxy_set_header Host $http_host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

This Nginx configuration file forwards incoming public traffic from port `80` to port `5000`.

Once the Nginx configuration is established, run `sudo nginx -t` to verify the syntax of the configuration files. If the configuration file test is successful, force Nginx to pick up the changes by running `sudo nginx -s reload`

## [Enable websockets](#Enable+websockets)

In order to enable websockets in Nginx the following configuration is needed:

```
location /gxwebsocket.svc {
         proxy_pass http://localhost:5000/gxwebsocket.svc;
         proxy_http_version 1.1;
         proxy_set_header Upgrade $http_upgrade;
         proxy_set_header Connection "upgrade";
      }
```

## [Multiple applications on one domain with Nginx](#Multiple+applications+on+one+domain+with+Nginx)

Let's suppose you have two applications SmallDemo0 and SmallDemo1 (\*) and want to host both on the same server and access at: http://localhost/SmallDemo0/WebPanel1.aspx and http://localhost/SmallDemo1/WebPanel1.aspx.

(\*) For example /home/deploy/dev/dotnet/SmallDemo0 and /home/deploy/dev/dotnet/SmallDemo1

1. Configure nginx to handle boths ports. Open /etc/nginx/sites-available/default in a text editor and replace the contents with the following:

```
server {
    listen 80;
    # Make site accessible from http://localhost/
    server_name localhost;
     location /SmallDemo0/ {
           proxy_pass http://localhost:5000/;
           proxy_http_version 1.1;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection keep-alive;
           proxy_set_header Host $host;
           proxy_cache_bypass $http_upgrade;
    }
    location /SmallDemo1/ {
           proxy_pass http://localhost:5001/;
           proxy_http_version 1.1;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection keep-alive;
           proxy_set_header Host $host;
           proxy_cache_bypass $http_upgrade;
    } 
}
```

Once the Nginx configuration is established, run `sudo nginx -t` to verify the syntax of the configuration files. If the configuration file test is successful, force Nginx to pick up the changes by running `sudo nginx -s reload`

Or start it with:

```
sudo service nginx start
```

2. Run your apps with the following commands:

```
/home/deploy/dev/dotnet/SmallDemo1$ dotnet bin/GxNetCoreStartup.dll "" /home/deploy/dev/dotnet/SmallDemo1 5001

/home/deploy/dev/dotnet/SmallDemo0$ dotnet bin/GxNetCoreStartup.dll "" /home/deploy/dev/dotnet/SmallDemo0 5000
```

Test your sites at http://localhost/SmallDemo0/WebPanel1.aspx  and http://localhost/SmallDemo1/WebPanel1.aspx

### [Another valid configuration using a different BaseURL (but getting the same final urls) could be:](#Another+valid+configuration+using+a+different+BaseURL+%28but+getting+the+same+final+urls%29+could+be%3A)

1. Configuration por nginx

```
server {
    listen 80;
    # Make site accessible from http://localhost/
    server_name localhost;
     location /SmallDemo0/ {
           proxy_pass http://localhost:5000/SmallDemo0/;
           proxy_http_version 1.1;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection keep-alive;
           proxy_set_header Host $host;
           proxy_cache_bypass $http_upgrade;
    }
    location /SmallDemo1/ {
           proxy_pass http://localhost:5001/SmallDemo1/;
           proxy_http_version 1.1;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection keep-alive;
           proxy_set_header Host $host;
           proxy_cache_bypass $http_upgrade;
    } 
}
```

2. Run commands:

```
/home/deploy/dev/dotnet/SmallDemo1$ dotnet bin/GxNetCoreStartup.dll "SmallDemo1" /home/deploy/dev/dotnet/SmallDemo1 5001

/home/deploy/dev/dotnet/SmallDemo0$ dotnet bin/GxNetCoreStartup.dll "SmallDemo0" /home/deploy/dev/dotnet/SmallDemo0 5000
```

3. Test your sites at http://localhost/SmallDemo0/WebPanel1.aspx  and http://localhost/SmallDemo1/WebPanel1.aspx

GxNetCoreStartup.dll has 3 parameters:

1. Virtual Dir (or BaseURL)

2. Physical application path

3. Port

default values are:

1. Empty

2. Current Directory where dotnet command is executed

3. 80


|  |
| --- |
| **Backlinks** |
| [Toc:.NET Applications Development](https://wiki.genexus.com/commwiki/wiki?53971) | [GeneXus 18 hardware and software requirements](https://wiki.genexus.com/commwiki/wiki?30900) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54300) |
| [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?54649) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55768) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 6)](https://wiki.genexus.com/commwiki/wiki?56187) |

---
