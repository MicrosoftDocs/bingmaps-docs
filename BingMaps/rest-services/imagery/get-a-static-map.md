---
title: "Get a Static Map | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: cf1fc5cb-e393-4be6-9c27-13cc3e60ff4b
caps.latest.revision: 121
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Get a Static Map
Use the following URL templates to get a static map. You can also display a route on a static map, and you can request static map metadata. Static map metadata includes the absolute (latitude and longitude) and relative (with respect to the map) coordinates and size of pushpins as well as the map area and center point.  
  
## Supported HTTP Methods

GET, POST

POST requests require all parameters to be passed into the body of the request as a JSON object. This API is [CORs enabled](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing).

## URL Templates  
 The default map size is 350 pixels by 350 pixels.  
  
> [!Note]
> These templates support both HTTP and HTTPS protocols. To use this API, you must have a [Bing Maps key](../getting-started/getting-a-bing-maps-key.md). 
  
 **Static map metadata**: To get the size and center point of the image and the locations and size of the pushpins on the map, set the mapMetadata parameter to 1 (true). When you request static map metadata, the metadata is returned instead of the map image.  
  
 **Get a map that is centered at a specified point.**  
  
 When you specify a center point, you must also specify a zoom level.  
  
```  
https://dev.virtualearth.net/REST/v1/Imagery/Map/{imagerySet}/{centerPoint}/{zoomLevel}?mapSize={mapSize}&pushpin={pushpin_1}&pushpin={pushpin_2}&mapLayer={mapLayer}&format={format}&mapMetadata={mapMetadata}&key={BingMapsKey}  
```  
  
 **Get a map that shows a specified map area.**  
  
```  
https://dev.virtualearth.net/REST/v1/Imagery/Map/{imagerySet}?pushpin={pushpin_1}&pushpin={pushpin_2}&pushpin={pushpin_n}&mapArea={mapArea}&mapSize={mapSize}&mapLayer={mapLayer}&format={format}&mapMetadata={mapMetadata}&key={BingMapsKey} 
```  
  
 **Get a map with pushpins that does not specify a center point or map area.**  
  
 If you do not specify a center point or map area, the map area is chosen to optimize the display of the pusphins.  
  
```  
https://dev.virtualearth.net/REST/v1/Imagery/Map/{imagerySet}?pushpin={pushpin_1}&pushpin={pushpin_2}&pushpin={pushpin_n}&mapSize={mapSize}&mapLayer={mapLayer}&format={format}&mapMetadata={mapMetadata}&key={BingMapsKey}  
```  
  
 **Get a map that is centered at the specified point and that displays a route.**  
  
 You can display a route on a map by specifying a set of waypoints.  
  
```  
https://dev.virtualearth.net/REST/v1/Imagery/Map/{imagerySet}/{centerPoint}/{zoomLevel}/Routes/{travelMode}?waypoint.1={waypoint1}&waypoint.2={waypoint2}&waypoint.n={wWaypointN}&mapSize={mapSize}&avoid={avoidOptions}&pushpin={pushpin_1}&pushpin={pushpin_2}&pushpin={pushpin_n}&timeType={timeType}&dateTime={dateTime}&maxSolutions={maxSolutions}&distanceBeforeFirstTurn={distanceBeforeFirstTurn}&mapLayer={mapLayer}&format={format}&mapMetadata={mapMetadata}&key={BingMapsKey}   
```  
  
 **Get a map that displays a route without specifying a center point. You can choose to specify the map area or you can accept the default.**  
  
 You can display a route on a map by specifying a set of waypoints. When a map area or a center point and a zoom level are not specified, a map area is chosen to optimize the display of the route.  
  
```  
https://dev.virtualearth.net/REST/v1/Imagery/Map/{imagerySet}/Routes/{travelMode}?waypoint.1={waypoint1}&waypoint.2={waypoint2}&waypoint.n={wWaypointN}&mapSize={mapSize}&mapArea={mapArea}&avoid={avoidOptions}&pushpin={pushpin_1}&pushpin={pushpin_2}&pushpin={pushpin_n}&timeType={timeType}&dateTime={dateTime}&maxSolutions={maxSolutions}&distanceBeforeFirstTurn={distanceBeforeFirstTurn}&mapLayer={mapLayer}&format={format}&mapMetadata={mapMetadata}&key={BingMapsKey}  
```  
  
 **Get a map that is based on a query.**  
  
```  
https://dev.virtualearth.net/REST/v1/Imagery/Map/{imagerySet}/{query}?mapSize={mapSize}&mapLayer={mapLayer}&format={format}&mapMetadata={mapMetadata}&key={BingMapsKey}   
```  
  
 **Pushpin limits**: If you use HTTP GET method with the following URL templates, you can specify up to 18 pushpins in the URL. If you want to specify more than 18 pushpins, use the HTTP POST method and specify up to 100 pushpins in the body of the HTTP POST request. If you use the HTTP POST method, all pushpins must be in the body of the request and not in the URL, and you must set the Content-Type to “text/plain” and the charset to “UTF-8” in the HTTP header. For a sample request, see the **Examples** section.  
  
### Template Parameters  
  
> [!NOTE]
>  See the [Common Parameters and Types](../rest-services/common-parameters-and-types.md) section for additional common parameters to use with these URLs.  
>   
>  Common parameters include:  
>   
>  -   [Output Parameters](../rest-services/output-parameters.md): Includes response output types and the JSON callback parameters.  
> -   [Culture Parameter](../rest-services/culture-parameter.md): Includes a list of the supported cultures.  
> -   [User Context Parameters](../rest-services/user-context-parameters.md): Includes parameters that set user location and viewport values to help determine locations. For example, these values may help prioritize a set of possible locations when you get a map based on a location query.  
>   
>  Parameter values are not case-sensitive.  
>   
>  When an alias is provided, you can use the alias to shorten the length of the query parameter. For example, pushpin=47.610,-122.107 can be shortened to pp=47.610,-122.107.  
  
 **Map Parameters**  
  
|Parameter|Alias|Description|Values|  
|---------------|-----------|-----------------|------------|  
|centerPoint||**Required.** A point on the Earth where the map is centered.|A Point value (latitude and longitude). For more information about Point values, see [Location and Area Types](../rest-services/location-and-area-types.md).<br /><br /> **Example**: centerPoint=47.610,-122.107|  
|declutterPins|dcl|**Optional.** Specifies whether to change the display of overlapping pushpins so that they display separately on a map.|One of the following values:<br /><br /> -   1: Declutter pusphpin icons.<br />-   0 **[default]**: Do not declutter pushpin icons.<br /><br /> **Note**: This feature is only supported when using the default pushpin style.<br /><br /> **Examples**:<br /><br /> declutter=1<br /><br /> dcl =1|  
|dpi||**Optional.** Specifies the resolution of the labels on the image to retrieve.|One of the following values:<br /><br /> -   Large: High resolution labels.<br />-   null **[default]**: Default image resolution.<br /><br /> **Example**: dpi=Large|  
|format|fmt|**Optional.** The image format to use for the static map.|One of the following image format values:<br /><br /> -   gif: Use GIF image format.<br />-   jpeg: Use JPEG image format. JPEG format is the default for Road, Aerial and AerialWithLabels imagery.<br />-   png: Use PNG image format. PNG is the default format for CollinsBart and OrdnanceSurvey imagery.<br /><br /> **Examples:**<br /><br /> format=jpeg<br /><br /> fmt=gif|  
|imagerySet||**Required.** The type of imagery.|One of the following values:<br /><br /> - Aerial – Aerial imagery.<br />- AerialWithLabels –Aerial imagery with a road overlay.<br />-AerialWithLabelsOnDemand - Aerial imagery with on-demand road overlay.<br />- CanvasDark - A dark version of the road maps.<br />- CanvasLight - A lighter version of the road maps which also has some of the details such as hill shading disabled.<br />- CanvasGray - A grayscale version of the road maps.<br />- Road – Roads without additional imagery.<br />- RoadOnDemand - Roads without additional imagery. Uses the dynamic tile service.|  
|mapArea|ma|**Required when a center point or set of route points are not specified.** The geographic area to display on the map.|A rectangular area specified as a bounding box. For more information, see [Location and Area Types](../rest-services/location-and-area-types.md).<br /><br /> **Example**: 45.219,-122.325,47.610,-122.107|  
|mapLayer|ml|**Optional.** A display layer that renders on top of the imagery set.|-   OrdnanceSurvey - Ordnance Survey imagery. This imagery is visible only in the UK.<br />-   TrafficFlow<br /><br /> **Example**: mapLayer=TrafficFlow|  
|mapSize|ms|**Optional.** The width and height in pixels of the static map output.|A string that contains a width and a height separated by a comma. The width must be between 80 and 2000 pixels and the height must be between 80 and 1500 pixels. The default map size for static maps is 350 pixels by 350 pixels. If the width or height dimension exceeds the limits, the default dimensions will be used.<br /><br /> **Example**: mapSize=100,600|  
|pushpin|pp|**Optional**. One or more pushpin locations to display on the map.|A series of values that include a Point value (latitude and longitude) with options to add a label of up to three (3) characters and to specify an icon style. For more information about specifying pushpins, see [Pushpin Syntax and Icon Styles](../rest-services/pushpin-syntax-and-icon-styles.md). You can specify up to 18 pushpins within a URL and 100 if you use the HTTP POST method and specify the pushpins in the body of the request. See the **Examples** section for examples.<br /><br /> **Example**: pushpin=47.610,-122.107;5;P10|  
|mapMetadata|mmd|**Optional**. Specifies whether to return metadata for the static map instead of the image.<br /><br /> The static map metadata includes the size of the static map and the placement and size of the pushpins on the static map.|One of the following values:<br /><br /> -   1: Return metadata for the specific image. An image is not returned.<br />-   0: Do not return metadata. **[default]**<br />     When you request metadata, the response returns metadata for the map instead of the map image. For more information about the static map metadata, see [Static Map Data](../rest-services/static-map-data.md).<br /><br /> **Example:** mmd=1|  
|query||**Required.** A query string that is used to determine the map location to display.|A string that contains query terms for the location of the static map.<br /><br /> **Example:** Seattle%20Center|  
|zoomLevel||**Required.** The level of zoom to display.|An integer between 0 and 21. **Note:**  Some imagery may not be available at all zoom levels for all locations. If imagery is not available at a location, a message is returned in the `ErrorDetails` collection that is part of the common response fields. See [Common Response Description](../rest-services/common-response-description.md) for a list of common response fields. <br /><br /> **Example**: 10|  
|highlightEntity|he|Highlights a polygon for an entity.|1 = Highlight polygon is on|  
|entityType||**Optional.** Indicates the type of entity that should be highlighted. The entity of this type that contains the centerPoint will be highlighted.|CountryRegion, AdminDivision1, or PopulatedPlace. For more information, see [Location and Area Types](https://msdn.microsoft.com/en-us/library/ff701726.aspx)<br /><br /> Also, please see the [Examples](../rest-services/get-a-static-map.md#BKMK_GetAStaticMapExamples) section below for demonstrations of this parameter.|  
|style|st|**Optional.** Specifies a custom map style to apply to the road maps.|See [Custom Map Styles in Bing Maps V8 and REST Services](../articles/custom-map-styles-in-bing-maps.md).|  
  
 **Route Parameters**  
  
|Parameter|Alias|Description|Values|  
|---------------|-----------|-----------------|------------|  
|avoid||**Optional.** Specifies the road types to minimize or avoid when the route is created for the driving travel mode.|A comma-separated list of values that limit the use of highways and toll roads in the route. In the definitions below, “highway” also refers to a “limited-access highway”.<br /><br /> If no values are specified, highways and tolls are allowed in the route.<br /><br /> -   highways: Avoids the use of highways  in the route.<br />-   tolls: Avoids the use of toll roads in the route.<br />-   minimizeHighways: Minimizes (tries to avoid) the use of highways in the route.<br />-   minimizeTolls: Minimizes (tries to avoid) the use of toll roads in the route. **Note:**  If you specify more than one option for a road type, then the most restrictive option is used. For example, if you set the avoid parameter to both highways and minimizeHighways, the highways option is used and all highways are avoided. <br /><br /> **Examples**:<br /><br /> avoid=highways<br /><br /> avoid=highways,tolls|  
|distanceBeforeFirstTurn|dbft|**Optional.** Specifies the distance before the first turn is allowed in the route. This option only applies to the driving travel mode.|An integer distance specified in meters. Use this parameter to make sure that the moving vehicle has enough distance to make the first turn.<br /><br /> **Examples**:<br /><br /> distanceBeforeFirstTurn=500<br /><br /> dbft=500|  
|dateTime|dt|**Required when the travel mode is Transit.** The timeType parameter identifies the desired transit time, such as arrival time or departure time. The transit time type is specified by the timeType parameter.|A string that contains the date and time formatted as a [DateTime](http://msdn.microsoft.com/en-us/library/03ybds8y.aspx) value. For information about the string representation options for DateTime values, see [DateTime.Parse Method (String)](http://msdn.microsoft.com/en-us/library/1k1skd40.aspx).<br /><br /> **Examples**:<br /><br /> -   dateTime=03/01/2011 05:42:00<br />-   dateTime=05:42:00 [assumes the current day]<br />-   dateTime=03/01/2011 [assumes the current time]|  
|maxSolutions|maxSolns|**Optional**. Specifies the maximum number of transit routes to return.|A string that contains an integer value. The default value is 1.<br /><br /> **Example**: maxSolns=3 **Note:**  This parameter is only supported for the Transit travel mode.|  
|optimize|optmz|**Optional.** Specifies what parameters to use to optimize the route on the map.|One of the following values:<br /><br /> -   distance: The route is calculated to minimize the distance. Traffic information is not used.<br />-   time **[default]**: The route is calculated to minimize the time. Traffic information is not used.<br />-   timeWithTraffic: The route is calculated to minimize the time and uses current traffic information.<br /><br /> **Example**: optimize=time|  
|timeType|tt|**Required when the travel mode is Transit**. Specifies how to interpret the date and transit time value that is specified by the dateTime parameter.|One of the following values:<br /><br /> -   Arrival: The dateTime parameter contains the desired arrival time for a transit request.<br />-   Departure: The dateTime parameter contains the desired departure time for a transit request.<br />-   LastAvailable: The dateTime parameter contains the latest departure time available for a transit request.|  
|travelMode||**Optional.** The mode of travel for the route.|One of the following values:<br /><br /> -   Driving **[default]**<br />-   Walking<br />-   Transit|  
|waypoint.n|wp.n|**Required.** Specifies two or more locations that define the route and that are in sequential order.|A waypoint location can be specified as a point, a landmark, or an address. You can optionally specify an icon style and add a label of up to three (3) characters for each waypoint. For a list of icon styles, see [Pushpin Syntax and Icon Styles](../rest-services/pushpin-syntax-and-icon-styles.md). For more information about Point values, see [Location and Area Types](../rest-services/location-and-area-types.md).<br /><br /> Specify waypoints using the following format: `wp.n;iconID;label`. The index (n value) for the set of waypoints in an integer starting with 0 or 1. The waypoint index values must be sequential and must always increment by 1.<br /><br /> You can have a maximum of 25 waypoints.<br /><br /> **Examples**:<br /><br /> waypoint.1=47.610,-122.107 [Point]<br /><br /> wp.1=Seattle,WA  [landmark]<br /><br /> wp.1=Seattle,WA;66;SEA  [icon and label]<br /><br /> waypoint.1=1 Microsoft%20Way%20Redmond WA [address]<br /><br /> **Incorrect set of waypoints.** The following set of values is not valid because there is no waypoint.2.<br /><br /> &waypoint.1=San%20Francisco&waypoint.3=Seattle|  
  
## Response  
 Static images are returned in one of the following formats. You can specify the image format by setting the `format` parameter. Default image formats and the corresponding content-type values returned in the response (such as image/png) are defined below.  
  
-   PNG (image/png): Default image format for Collins Bart and Ordnance Survey imagery.  
  
-   JPEG (image/jpeg): Default image format for road, aerial and aerial-with-labels imagery.  
  
-   GIF (image/gif)  
  
 These URLs support JSON (application/json) and XML (application/xml) response formats. A JSON response is provided by default unless you request XML output by setting the output (o) parameter.  For more information, see [Output Parameters](../rest-services/output-parameters.md).  
  
<a name="BKMK_GetAStaticMapExamples"></a>   
## Examples  
 **Get a map with Road imagery and traffic flow based on a query.**  
  
 This example gets a map with road imagery based on a query result Bellevue, Washington. Traffic flow is also included on the map.  
  
```  
https://dev.virtualearth.net/REST/V1/Imagery/Map/Road/Bellevue%20Washington?mapLayer=TrafficFlow&key=BingMapsKey  
```  
  
 This example returns the following image.  
  
 ![Seattle Center Static Map Example](../rest-services/media/seattlecenterstaticmap.jpg "Seattle Center Static Map Example")  
  
 **Get a map with Aerial imagery based on a query.**  
  
 This example gets a map with aerial imagery and labels based on a query result for the Eiffel Tower in Paris. The map has a width of 500 pixels and height of 400 pixels.  
  
```  
https://dev.virtualearth.net/REST/v1/Imagery/Map/AerialWithLabels/eiffel%20tower?mapSize=500,400&key=BingMapsKey  
```  
  
 This example returns the following image.  
  
 ![Static Map Image of the Eiffel Tower](../rest-services/media/rest-eiffeltowerstaticmap.PNG "Static Map Image of the Eiffel Tower")  
  
 **Get a map with Road imagery and pushpins that is centered at a specified point.**  
  
 This example creates a map with road imagery and places pushpins on the Space Needle, the Pacific Science Center, and the Olympic Sculpture Park in Seattle. The centerPoint of the map is set to 47.619048 degrees latitude and -122.35384 degrees longitude. The zoomLevel is set to 15.  
  
```  
https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/47.619048,-122.35384/15?mapSize=500,500&pp=47.620495,-122.34931;21;AA&pp=47.619385,-122.351485;;AB&pp=47.616295,-122.3556;22&key=BingMapsKey  
```  
  
 This example returns the following image.  
  
 ![CenterPoint and ZoomLevel Static Map Example](../rest-services/media/centerpointzoomlevelstaticmap.jpg "CenterPoint and ZoomLevel Static Map Example")  
  
 **Get the static map metadata for a map with Road imagery and pushpins that is centered at a specified point.**  
  
 This example specifies the same map parameters as the previous example and adds the mapMetadata parameter to get the map metadata. Map metadata includes the map size, area and center point and the position and size of the pushpins. To see the XML and JSON responses for this request and for descriptions of the metadata information, see [Static Map Data](../rest-services/static-map-data.md).  
  
```  
https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/47.619048,-122.35384/15?mapSize=500,500&pp=47.620495,-122.34931;21;AA&pp=47.619385,-122.351485;;AB&pp=47.616295,-122.3556;22&mapMetadata=1&o=xml&key=BingMapsKey  
```  
  
 **Get a map with Road imagery and declutter overlapping pushpins.**  
  
 This example creates a map with road imagery and specifies two pushpins that are located very close together. The declutterPins (dcl) parameter is set so that the pushpins both appear separately. If the declutterPins parameter were not set, the pushpins would overlap. Maps for both cases are shown below.  
  
```  
https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/47.6156352,-122.2043549/12?pp=47.6156352,-122.2043549;;1&pp=47.612441,-122.204533;;2&dcl=1&key=BingMapsKey  
```  
  
 This example returns the following image.  
  
 ![Static Map showing decluttered pushpins](../rest-services/media/rest-staticmap-declutteredpins.png "Static Map showing decluttered pushpins")  
  
 If the declutter parameter was not set in this example, the pushpins would overlap as shown in the following image.  
  
 ![Static Map showing overlapping pushpins](../rest-services/media/rest-staticmap-clutteredpins.png "Static Map showing overlapping pushpins")  
  
 **Get a map with Aerial imagery and pushpins without specifying a map area or center point. The map is optimized to fit the pushpins.**  
  
 This example creates a map with aerial imagery with labels and specifies 5 pushpins. Because a map area or center point is not specified, a map area is chosen that best shows all of the pushpins.  
  
```  
https://dev.virtualearth.net/REST/v1/Imagery/Map/AerialWithLabels?pp=40.804000,-74.464460;;1&pp=40.815180,-74.219250;;2&pp=40.881210,-74.168020;;3&pp=40.810830,-74.260250;;4&pp=40.851800,-74.299900;;5&key=BingMapsKey  
```  
  
 This example returns the following image.  
  
 ![Static map with pushpins and Aerial imagery](../rest-services/media/rest-ppwithnomapareaorcp.png "Static map with pushpins and Aerial imagery")  
  
 **Get a map with Road imagery for a specified map area.**  
  
 This example gets a map of the specified area that shows road imagery with traffic flow. The map shows the San Francisco metropolitan area and pushpins identify the location of Stanford University and the University of California at Berkeley.  
  
```  
https://dev.virtualearth.net/REST/V1/Imagery/Map/road?mapArea=37.317227,-122.318439,37.939081,-122.194565&ms=500,600&pp=37.869505,-122.2705;35;BK&pp=37.428175,-122.169680;;ST&ml=TrafficFlow&key=BingMapsKey  
```  
  
 This example returns the following image.  
  
 ![Map Area Static Map](../rest-services/media/rest-mapareastaticmap.jpg "Map Area Static Map")  
  
 **Get a map with Road imagery that displays a route.**  
  
 This example gets a map with road imagery that displays a driving route between the cities of Seattle and Redmond in Washington State.  Custom icons 64 and 66 are chosen to display the endpoints which are identified as “1” and “2”.  
  
```  
https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes?wp.0=Seattle,WA;64;1&wp.1=Redmond,WA;66;2&key=BingMapsKey   
```  
  
 This example returns the following image.  
  
 ![Static map with route overlay](../rest-services/media/rest-routeonmapsimplesea2red.jpg "Static map with route overlay")  
  
 **Get a map with Road imagery centered at a point with a specified zoom level.**  
  
 This example uses a center point and zoom level to get a map that shows the end of the route between Seattle and Redmond from the previous example. The center point is the latitude and longitude coordinates of Redmond. You can use the [Find a Location by Address](../rest-services/find-a-location-by-address.md) API to get the latitude and longitude coordinates of a location.  
  
```  
https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/47.678559869527817,-122.13099449872971/14/Routes? wp.0=Seattle,WA;64;1&wp.1=Redmond,WA;66;2&key=BingMapsKey  
```  
  
 This example returns the following image.  
  
 ![Static map with route overlay](../rest-services/media/rest-routeonmapcpzl-simpleendpoint.jpg "Static map with route overlay")  
  
 **Get maps with Road imagery that displays a transit route and zoomed views of the start and end points.**  
  
 The following examples show how to get a map with road imagery that displays a transit route from the Space Needle in Seattle, Washington to Bellevue Downtown Park in Bellevue, Washington at 3 PM of the current day. The three URL examples display the entire route and zoomed views of the start and end points of the route. Note that the walking segments of the route are displayed as dotted lines.  
  
 View of the complete transit route.  
  
```  
https://dev.virtualearth.net/REST/V1/Imagery/Map/Road/Routes/Transit?wp.0=Space%20Needle&wp.1=Bellevue%20Downtown%20Park&timeType=Departure&dateTime=3:00:00PM&output=xml&key=BingMapsKey  
```  
  
 ![Shows a transit route on a static map](../rest-services/media/rest-transitcompleteroute.PNG "Shows a transit route on a static map")  
  
 View the start of the transit route by specifying a center point and zoom level. The center point for this map is the coordinates for the Space Needle that are returned in the response when you request a transit route by using the [Calculate a Route](../rest-services/calculate-a-route.md) API. This map includes a walking route that is shown by a dotted line.  
  
```  
https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/47.620495,-122.34931/15/Routes/Transit?timeType=Departure&dateTime=3:00:00PM&wp.0=Space%20Needle&wp.1=Bellevue%20Downtown%20Park&key=BingMapsKey  
```  
  
 ![Zoomed&#45;in view of transit route start](../rest-services/media/rest-transitroutestart.PNG "Zoomed-in view of transit route start")  
  
 View the end of the transit route by specifying a center point and zoom level. The center point for this map is the coordinates of the Bellevue Downtown Park in that is returned in the response when you request a transit route by using the [Calculate a Route](../rest-services/calculate-a-route.md) API. This map includes a walking route that is shown by a dotted line.  
  
```  
https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/47.615635,-122.20435/15/Routes/Transit?timeType=Departure&dateTime=3:00:00PM&wp.0=Space%20Needle&wp.1=Bellevue%20Downtown%20Park&key=BingMapsKey  
```  
  
 ![Zoomed&#45;in view of transit route end](../rest-services/media/rest-transitrouteend.PNG "Zoomed-in view of transit route end")  
  
 **Get a map that displays pushpins by using the HTTP POST Method**  
  
 The following example shows how to request a static map by using the HTTP POST method. When you use this method, you can specify up to 100 pushpins. All pushpins must be in the body of the request. Because the request does not specify a map area or center point and zoom level, the map area is optimized to show all of the pushpins.  
  
 **HTTP POST URL**  
  
```  
https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/?key=BingMapsKey  
```  
  
 **HTTP POST Header**  
  
 You must include the following settings in the HTTP POST Header.  
  
```  
Content-Length: insertLengthOfHTTPBody  
Content-Type: text/plain; charset=utf-8  
```  
  
 **HTTP POST Body**  
  
 When specifying pushpins in the request body, you can use a carriage return (\r\n) or an ampersand (&) as a delimiter. The following two examples show these options.  
  
 **Example 1**  
  
```  
pp=38.889586530732335,-77.05010175704956;23;LM\r\n  
pp=38.88772364638439,-77.0472639799118;7;KM\r\n  
pp=38.890479451480054,-77.04744637012482;1;VM\r\n  
pp=38.8896854931628,-77.03519403934479;45;WM  
  
```  
  
 **Example 2**  
  
```  
pp=38.889586530732335,-77.05010175704956;23;LM&pp=38.88772364638439,-77.0472639799118;7;KM\r\n  
pp=38.890479451480054,-77.04744637012482;1;VM&pp=38.8896854931628,-77.03519403934479;45;WM  
  
```  
  
 This example returns the following image.  
  
 ![Static map of Washington monuments with pushpins](../rest-services/media/rest-washingtonmonumentswithpushpins.png "Static map of Washington monuments with pushpins")  
  
 **Get a map with Ordnance Survey imagery that is provided in JPEG format.**  
  
 This example shows a map of Trafalgar Square in Great Britain using Ordnance Survey imagery. The static map is returned in JPEG format. If this image format were not specified in the URL, the static map would be returned in the default PNG format.  
  
```  
https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/51.506666,-0.129436/15?ml=OrdnanceSurvey&format=jpeg&key=BingMapsKeyBingMapsKey  
```  
  
 This example returns the following image.  
  
 ![Image showing Ordnance Survey imagery](../rest-services/media/rest-ordnacesurveyimage.PNG "Image showing Ordnance Survey imagery")  
  
 **Get a map that will highlight the polygon for an entity.**  
  
 This example shows a map using the `HighlightEntity` (he=1) parameter with a value of `admindivision1` to show a map with a polygon for Washington State. The latitude and longitude is a point that is within the entity that you want to highlight.  
  
```  
https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/47.677006,-122.125526/admindivision1?ms=500,270&key=bing maps key&c=en-US&he=1     
```  
  
 This example returns the following image.  
  
 ![BingRestWS&#95;PolyState](../rest-services/media/bingrestws-polystate.png "BingRestWS_PolyState")  
  
 This example shows a map using the `HighlightEntity` (he=1) parameter with a value of `PopulatedPlace` to show a map with a polygon for the city of Redmond. The latitude and longitude is a point that is within the entity that you want to highlight.  
  
```  
https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/47.677006,-122.125526/PopulatedPlace?ms=500,270&zl=12&key=bing maps key &c=en-US&he=1  
```  
  
 This example returns the following image.  
  
 ![BingRestWS&#95;PolyCity](../rest-services/media/bingrestws-polycity.png "BingRestWS_PolyCity")  
  
## HTTP Status Codes  
  
> [!NOTE]
>  For more details about these HTTP status codes, see [Status Codes and Error Handling](../rest-services/status-codes-and-error-handling.md).  
  
 When the request is successful, the following HTTP status code is returned.  
  
* 200

When the request is not successful, the response returns one of the following errors.

* 400
* 401
* 404
* 429
* 500
* 503 
  
## See Also  
 [Using the REST Services with .NET](../rest-services/using-the-rest-services-with-net.md)   
 [JSON Data Contracts](../rest-services/json-data-contracts.md)