---
title: "User Context Parameters | Microsoft Docs"
ms.date: "02/28/2018"
ms.topic: "reference"
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# User Context Parameters

Use user context parameters to specify information about the user. You can increase the accuracy of a location result when you specify a user context parameter in your request URL.  
  
 When an alias is provided, you can use the alias to shorten the length of the query parameter.  
  
|Parameter|Alias|Description|Values|  
|---------------|-----------|-----------------|------------|  
|`userMapView`|`umv`|**Optional.** The geographic region that corresponds to the current viewport.|A rectangular area on the earth defined as a bounding box object. The sides of the rectangles are defined by latitude and longitude values. For more information, see [Location and Area Types](../location-and-area-types.md). When you specify this parameter, the geographical area is taken into account when computing the results of a location query.<br /><br />Example: `40.879052728414536,-122.51596324145794,49.77062925696373,-105.74403114616871`|  
|`userLocation`|`ul`|**Optional**. The user’s current position.|A point on the earth specified as a latitude and longitude. When you specify this parameter, the user’s location is taken into account and the results returned may be more relevant to the user.<br /><br />Example: `userLocation=51.504360719046616,-0.12600176611298197`|  
|`userIp`|`uip`|**Optional**. An Internet Protocol version 4 (IPv4) address.|The default address is the IPv4 address of the request. When you specify this parameter, the location associated with the IP address is taken into account in computing the results of a location query.<br /><br />Example: `userIp=111.111.11.11`|  
|`userRegion`|`ur`|**Optional.** The region the user is in.|A string that an [ISO 3166-1 Alpha-2 region/country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). This will alter Geopolitical disputed borders and labels to align with the specified user region.<br /><br />Example: `userRegion=SA`|