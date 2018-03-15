---
title: "Map Control Branches | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 80ff1089-3610-4868-b37c-22071b4aaf96
caps.latest.revision: 7
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms:service: "bing-maps"
---
# Map Control Branches
There are two branches of the Bing Maps V8 SDK that can be accessed. This provides the option to access new features as soon as they are available, even if those features have not been thoroughly tested or completed.

Branch	     | Description
------------ | --------------------
`release`	     | The main branch of the SDK that is used in most applications. New features have been fully tested and known bugs found while in the experimental branch have been fixed. 
`experimental` | New features are made available as soon as they have been developed. These features are still being tested and may have bugs in them. This branch is recommended for developers who want to try out the latest and greatest features as soon as they are available. 

<!--`frozen`	     | New features are added only after they have been in the release branch for a period of time and all known bugs have been fixed. This branch is recommended for mission critical apps that are willing to wait longer for new features in exchange for the extra stability.-->

To point your application to a specific branch simply add `&branch=[branch_version]` to the map script URL. If a branch is not specified, the release branch is automatically loaded. For example, the following URL can be used to load the experimental branch.

```
<script type='text/javascript' src='http//www.bing.com/api/maps/mapcontrol?callback=GetMap&branch=experimental&key=[YOUR_BING_MAPS_KEY]' async defer></script>

<script>
    function GetMap() {
        //Load the map.
    }
</script>
```
