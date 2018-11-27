---
title: "Configuration Driven Maps framework | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: c872f526-9f6f-415a-8ddd-37c91d9caabc
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Configuration Driven Maps framework
Configuration driven maps allow you to quickly and easily create a map with your data with little to no coding required. Instead create a JSON configuration fill that species the data sets you want to render along with some map options and then easily generate a map from this. Besides providing a minimal coding option for creating map apps, configuration driven maps are great for creating reusable map apps which are data driven. Take for example SharePoint, every user has different permissions and access to different data sets. This can easily be programmatically defined as a configuration file which can then be used to provide all users with a similar map application, but with only the data sets they have access to.

Map configuration files can be loaded in one of two ways:

* In code using the [ConfigurableMap class](../../map-control-api/configurablemap-class.md) in Bing Maps V8. This class will create a map instance based on the specified configuration file. Your code can then add additional functionality to the map using the Bing Maps V8 API. See the [Load a Configurable Map with Code example](load-a-configurable-map-with-code-example.md).
* As a URL parameter of the Bing Maps configurable map page which can then be viewed in a browser as-is or embedded into a web app using an iframe. See the [IFrameable Configuration Map example](iframeable-configuration-map-example.md).

## Configuration file format

A map configuration file defines the options to use when loading the map as well as the modules and datasets to load. The root JSON object is a [ConfigurableMapOptions object](../../map-control-api/configurablemapoptions-object.md). Here is an example JSON configuration file which loads the map at a specified location and zoom, with three data layers which are loaded via the GeoXml module.

```
{
  "mapOptions": {
    "credentials": "YOUR_BING_MAPS_KEY",
    "center": "47.606209,-122.332071",
    "zoom": 4
  },
  "modules": [
    {
      "moduleName": "Microsoft.Maps.GeoXml",
      "moduleOptions": [
        {
          "addLayerFromUrl": "https://bingmapsisdk.blob.core.windows.net/isdksamples/Countries.xml"
        },
        {
          "addLayerFromUrl": "https://bingmapsv8samples.azurewebsites.net/Common/data/kml/SampleKml.kml"
        },
        {
          "addLayerFromUrl": "https://earthquake.usgs.gov/fdsnws/event/1/query?minmagnitude=3&format=geojson",
          "geoXmlOption": {
            "layerName": "geoxml layer loading geojson data"
          }
        }
      ]
    }
  ]
}
```

A version of this file is hosted by the Bing Maps team here:

`https://bingmapsisdk.blob.core.windows.net/isdksamples/configmap2.json`

This can be loaded using the [ConfigurableMap class](../../map-control-api/configurablemap-class.md) in a web app, or into the Bing Maps configurable maps page using the following URL:

`https://www.bing.com/maps/configurable?config=https%3A%2F%2Fbingmapsisdk.blob.core.windows.net%2Fisdksamples%2Fconfigmap2.json`

Here is a screenshot of the map that is rendered when loading this configuration file.

![BMV8_ConfigMap](..//media/bmv8-configmap.PNG)

[Try it now](http://bingmapsv8samples.azurewebsites.net/#Load%20a%20Configurable%20Map%20with%20Code)

## Examples

* [IFrameable Configuration Map example](iframeable-configuration-map-example.md)
* [Load a Configurable Map with Code example](load-a-configurable-map-with-code-example.md)

## Related Topics

* [ConfigurableMap class](../../map-control-api/configurablemap-class.md)
* [ConfigurableMapModule Object](../../map-control-api/configurablemapmodule-object.md)
* [ConfigurableMapOptions object](../../map-control-api/configurablemapoptions-object.md)
* [PostModuleAction Object](../../map-control-api/postmoduleaction-object.md)
