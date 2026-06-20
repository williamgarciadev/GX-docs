---
title: "Docker Environment variables property"
source_id: 40607
source_url: https://wiki.genexus.com/commwiki/wiki?40607
genexus_version: "18"
---

# Docker Environment variables property

Set the environment variables you want the Dockerfile to include

### [Description](#Description)

What's written in the property gets added to the result dockerfile in a line starting with the [ENV instruction](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#env). You can either set one variable (VAR=VALUE) or as many as you want to separate them with a space (VAR1=VALUE1 VAR2=VALUE2). Also, make sure you single quote the values that may contain spaces (VAR='THE VALUE').

After the image is created you can check its environment variables executing the following command.

```
docker inspect <image name> --format {{.ContainerConfig.Env}}
```

At runtime, you can check every environment variable with the [Configuration Manager](https://wiki.genexus.com/commwiki/wiki?40085)

### [See Also](#See+Also)

* [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092)
* [HowTo: Deploy an Application to Docker](https://wiki.genexus.com/commwiki/wiki?36951)
* [Application Configuration using Environment Variables](https://wiki.genexus.com/commwiki/wiki?39459)
* [Configuration Manager](https://wiki.genexus.com/commwiki/wiki?40085)


|  |
| --- |
| **Backlinks** |
| [HowTo: Deploy an Application to Docker](https://wiki.genexus.com/commwiki/wiki?36951) | [HowTo: Deploy an Application to Docker (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54337) |

---
