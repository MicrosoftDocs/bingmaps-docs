---
title: "Getting Started with Bing Maps | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 7459dd1b-80a6-4c03-9ed0-d3cbde8253ff
caps.latest.revision: 61
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Getting Started with Bing Maps
To start developing with Bing Maps, choose the API(s) that is most appropriate for your platform and needs.  
  
## Developer APIs  
 The Bing Maps Platform offers a suite of controls and service APIs that you can use to add Bing Maps or geospatial services to your application.  
  
 **Choose Your API**: For a breakdown of the API by feature and platform, see [Choose Your API](http://www.microsoft.com/maps/choose-your-bing-maps-API.aspx) on the Bing Maps Platform website.  
  
 **Bing Maps Keys**: All APIs require a Bing Maps Key. For information about the different types of keys, see [Create a Bing Maps Key](http://www.microsoft.com/maps/create-a-bing-maps-key.aspx).  
  
 **Licensing**: If you have a licensing question or want to request a quote, contact the Bing Maps licensing team [here](http://www.microsoft.com/maps/licensing/licensing.aspx).  
  
 **Additional Resources**: For developer guides, blogs and other resources, check out [Bing Maps Resources](http://www.microsoft.com/maps/developer-resources.aspx).  
  
### Bing Maps APIs  
  
|||  
|-|-|  
|[Bing Maps V8 Web Control](../v8-web-control/index.md)|The Bing Maps V8 Web Control is the latest Bing Maps JavaScript API. Combine the AJAX map control with the [Bing Maps REST Services](../rest-services/index.md) and the [Bing Spatial Data Services](../spatial-data-services/index.md) to create powerful Web sites and mobile applications with the latest imagery and location functionality. An interactive SDK for Bing Maps V8 is at [http://www.bing.com/api/maps/sdk/mapcontrol/isdk](http://www.bing.com/api/maps/sdk/mapcontrol/isdk).|  
|[Bing Maps in Windows UWP](https://docs.microsoft.com/windows/uwp/maps-and-location/)|Bing Maps is built into the Windows UWP developer APIs. See the [Windows documentation](https://docs.microsoft.com/windows/uwp/maps-and-location/) for more information|  
|[Bing Maps REST Services](../rest-services/index.md)|The Bing Maps REST Services uses REST URLs to perform tasks such as creating a map with pushpins, geocoding an address, retrieving imagery metadata or calculating a route.|  
|[Bing Spatial Data Services](../spatial-data-services/index.md)|The Bing Spatial Data Services uses REST URLs to geocode and reverse-geocode large sets of spatial data and to create and query data sources. A data source contains sets of data for a user-defined entity type that has a spatial component. For example you can create a data source for a set of stores and then query this data source to find stores near a location.|  
|[Bing Maps WPF Control](http://www.microsoft.com/download/en/details.aspx?id=27165)|The Bing Maps WPF Control SDK lets developers integrate Bing Maps into rich [Windows Presentation Foundation](http://msdn.microsoft.com/en-us/library/ms754130.aspx) (WPF) applications. Using a software + services approach, the Bing Maps WPF Control retrieves the latest Bing Maps imagery for your WPF application using Bing’s cloud-based architecture. The Bing Maps WPF Control SDK also supports [Microsoft Surface](http://www.microsoft.com/surface/en/us/default.aspx) touch interface for creating rich touch-enabled applications.<br /><br /> To start using the Bing Maps WPF Control, download the [Bing Maps Windows Presentation Foundation Control SDK](http://www.microsoft.com/download/en/details.aspx?id=27165).|  
  
 Using a version of Bing Maps not listed here? Check the [Discontinued Control Migration Guidelines](https://www.microsoft.com/maps/discon-control-migrat-guide.aspx) to see if the version of Bing Maps you are using is nearing end of life, and if so, find out how to migrate to a newer version of Bing Maps.  
  
<a name="simpleNonAPIOptions"></a>   
## Simple non-API Bing Maps options  
 If you simply want to embed a map (static or interactive) on a web page or open the Map app in Windows 8 or Windows 10 from your Windows app, and do not require continuous control of the mapping experience, you may be interested in the following options.  
  
|||  
|-|-|  
|Embed a map in your web page (static or interactive)|Option 1: Go to [http://www.bing.com/maps](http://www.bing.com/maps), create the map you want, and then click **Share**. If you want control over basic parameters like size and imagery, click **Customize and preview**. This option will provide you with HTML that you can embed into your web page.<br /><br /> Option 2: [Create a Custom Map URL](../articles/create-a-custom-map-url.md). You can create a URL that opens Bing Maps with customizations provided by you. In addition to normal map features, you can also display search results. You do not need a Bing Maps Key for this option.<br /><br /> Option 3: [Get a Static Map](../rest-services/get-a-static-map.md). With this option, you can create a URL that displays a static map. You can specify parameters that specify the imagery, define pushpins, display a route and control other map features. You will need a [Bing Maps Key](http://www.microsoft.com/maps/create-a-bing-maps-key.aspx) to use this option.|  
|Open the Windows 8 or 10 Map app from your Windows app|Create a URL using the schema defined in [URI Schema for maps application](http://msdn.microsoft.com/en-us/library/windows/apps/jj635237.aspx). You do not need a Bing Maps Key to use this schema.|  
  
## News and Resources  
 To keep up to date with the latest  Bing Maps news, read the [Bing Dev Center Blog](http://blogs.bing.com/maps/). For help from the Bing Maps community, use the [Bing Maps Forums](http://social.msdn.microsoft.com/Forums/en-US/category/bingmaps).