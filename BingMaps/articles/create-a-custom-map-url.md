---
title: "Create a Custom Map URL | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 74b4554d-7db5-43b3-a9bb-f4b097009f5c
caps.latest.revision: 10
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Create a Custom Map URL
If you want to email someone a map URL or embed a map into your website, you can get the map you need in most cases by clicking **Share** at http://bing.com/maps. From the **Share** dialog box, you can click **Customize and Preview** to further customize your map URL. However, there may be times when you want more control or options such as search results and items in your places list.  In this case, you can use the information in this article to build your own Bing Maps URL. `  
  
## Getting Started  
 To create your map link, start with the base URL for Bing Maps shown below, and then add parameters to customize the map. Parameters specify things like the map center point, zoom level, map view (area that you want your map to display), search results and more. Available parameters and examples are provided in the sections below.  
  
1.  To build your own URL, start with the base map URL:  
  
     `http://bing.com/maps/default.aspx`  
  
2.  Add a question mark (?):  
  
     `http://bing.com/maps/default.aspx?`  
  
3.  Add the first parameter that you want to use, and then set the value of the parameter by using an equal sign (=):  
  
     This example sets the centerpoint of the map.  
  
     `http://bing.com/maps/default.aspx?cp=47.677797~-122.122013`  
  
## General parameters  
 The following are some common parameters that customize your map.  
  

|**Parameter**|**Definition**|**Example**|**Details**| 
|-|-|-|-| 
|cp|center point|cp=47.677797~-122.122013|Defines where the center of the map should be. Use the following format for the cp parameter:<br /><br /> `Latitude~Longitude`<br /><br /> Both values must be expressed in [decimal degrees](http://en.wikipedia.org/wiki/Decimal_degrees). Latitude and longitude are commonly presented in decimal degrees as two numbers, such as -47.677797 (latitude) and -122.122013 (longitude).|  
|lvl|zoom level|lvl=5|Defines the zoom level of the map view. Valid values are 1-20. This parameter is ignored when a search parameter, such as **ss** or **where1**, is specified. A table of search parameters is provided below.|  
|style|map view|style=r|Defines the map view. Valid values for this parameter include:<br /><br /> -   **a**: Display an aerial view of the map.<br /><br /> -   **r**: Display a road view of the map.<br /><br /> -   **h**: Display an aerial view of the map with labels.<br /><br /> -   **o**: Use this value to display a bird's eye (oblique) view of the map.<br /><br /> -   **b**: Display a bird's eye (oblique) with labels view of the map.|  
|scene|scene ID reference|scene=3715328|Specifies the ID of the bird's eye (oblique) image tile to display. You can use this parameter with a **lvl** value of 1 or 2 and a **dir** value to view different formats of the map image.|  
|dir|direction|dir=180|Specifies the direction that the camera is pointing in degrees. Valid values are 0 for North, 90 for East, 180 for South, and 270 for West.|  
|trfc|traffic|trfc=1|Specifies whether traffic information is included on the map. Omitting the trfc parameter produces the same results as trfc=0|  
  
### Examples  
 To open Bing Maps with the map centered on a specific location with a zoom level of 12, and the map view set to the road map view:  
  
 `http://bing.com/maps/default.aspx?cp=43.901683~-69.522416&lvl=12&style=r`  
  
 To open Bing Maps with the map centered on a specific location, the map view set to bird's eye (oblique) image, and a specified zoom level and scene:  
  
 `http://bing.com/maps/default.aspx?cp=37.814692~-122.477339&style=o&lvl=1&dir=0&scene=1140291`  
  
 To open Bing Maps with the map centered on a specific location, the map view set to bird’s eye (oblique), and with a traffic overlay displayed:  
  
 `http://bing.com/maps/default.aspx?cp=47.621065~-122.352534&style=o&lvl=14&trfc=1`  
  
## Search parameters  
 To create a map that displays specific search results, use the following parameters.  
  
|**Parameter**|**Definition**|**Example**|**Details**|  
|-|-|-|-|  
|where1|location|where1=1 Microsoft Way, Redmond, WA|Defines a location to center the map based on a specific address or a place name. The text is the same text that you type in the upper search box in Bing Maps to search for a specific address or place name.|  
|ss|search type search|ss=coffee|Defines the searches that you want to display. Use this parameter to display search results for a business.|  
  
 **Search Parameter Modifiers**  
  
 Use the following search parameter modifiers with the **ss** parameter to specify how results are displayed.  
  
|**Modifier**|**Definition**|**Example**|**Details**|  
|-|-|-|-|  
|sst|search parameter modifier|sst.1|You can append the **sst** parameter to a search string using a tilde (~) to specify how the search results are sorted. Use the following values with the sst parameter to specify the sort option.<br /><br /> **0**: Relevance<br /><br /> **1**: Distance<br /><br /> **2**: Rating|  
|pg|search  parameter modifier|pg.2|You can append the **pg** parameter to a search string using a tilde (~) to specify which page of results to display.|  
  
### Example  
  
-   To open Bing Maps to a specific address:  
  
     `http://bing.com/maps/default.aspx?rtp=adr.One%20Microsoft%20Way,%20Redmond,%20WA%2098052~pos.45.23423_-122.1232_MyPlace&rtop=0~1~0`  
  
-   To open Bing Maps with a business search:  
  
     `http://bing.com/maps/default.aspx?ss=yp.Pizza~sst.1~pg.2`  
  
## Driving directions parameters  
 To create a map that displays directions from a specific start and end point, use the following parameters.  
  
|**Parameter**|**Definition**|**Example**|**Details**|  
|-|-|-|-|  
|rtp|route|Rtp=adr.Seattle,WA~adr.One%20Microsoft%20Way,Redmond,WA|Defines the start and end of a route to draw on the map, each separated by a tilde (~). Each of the waypoints is defined by either a pos (position) or adr (address) identifier. These identifiers are described in the table below.<br /><br /> A complete route contains at least two waypoints. For example, a route with two waypoints is defined by the following:<br /><br /> `rtp="A"~"B"`<br /><br /> You can also specify an incomplete route. For example, you can define only the start of a route: `rtp="A"~`<br /><br /> Or, you can enter only the end of a route: `rtp=~"B"`<br /><br /> If you provide only one waypoint, the driving directions panel is displayed with the provided waypoint, but no route is drawn.|  
|rtop|route options|rtop=0~1~0|Defines options for the route. There are three sets of options, each separated by a tilde (~) The first option specifies how the route is chosen.  The second option specifies whether traffic is displayed.  The third option must be set to 0 if specified You can choose to not specify a value and get the default value of 0, but you must preserve the order of the values with the tilde (~) separators. For example, the follow examples are all valid values: 0~1~, ~1~0, 1~~0, and 1~~.<br /><br /> The default value of 0~0~0 (quickest without traffic) will be used if this parameter is not specified.<br /><br /> Options for how the route is chosen (first option):<br /><br /> **0**: Quickest time [default]<br /><br /> **1**: Shortest distance<br /><br /> Options for displaying traffic (second option):<br /><br /> **0**: Traffic is not displayed [default]<br /><br /> **1**: Traffic is displayed|  
|mode|mode|mode=D|Defines the mode of transportation. Use the following values:<br /><br /> -   **D**: Driving<br /><br /> -   **T**: Transit<br /><br /> -   **W**: Walking|  
|limit|limit|limit=D|Defines whether the route is limited by the arrival or departure time or chooses the last possible train that day. Use the following values:<br /><br /> -   **D**: Depart at<br /><br /> -   **A**: Arrive by<br /><br /> -   **LT**: Last train (Japanese market only)|  
|time|time|time=201009302015|Defines the time for which the Depart or Arrive limit is based upon and based on the 24-hour timekeeping system. Example represents Sept 30, 2010 at 8:15pm. Use the following format: `YYYYMMDDhhmm`|  
  
 **Rtp Parameter Identifiers**  
  
 Use the following identifiers with the **rtp** parameter to specify the endpoints of a route.  
  

|**Identifier for rtp**|**Definition**|**Example**|**Details**| 
|-|-|-|-|  
|pos|position|rtp=pos.42.2_-122.3~pos.55.2_-127.0|Defines a waypoint as a specific position on the map. Use the following format: `rtp=pos.latitude_longitude_name`|  
|adr|address|rtp=adr.Seattle,WA~adr.One%20Microsoft%20Way,Redmond,WA|Defines a waypoint as an address. Use the following format: `rtp=adr.address`<br /><br /> Make sure your replace blank spaces in the address with the encoded string %20.|  
  
 You can use any of the parameters listed in the previous tables to specify your waypoints.  
  
 The destination is specified using the **rtp** and **pos** parameters described above. Make sure that you specify only the end location, for example rtp=~pos.45.21_-123.2.  
  
### Example  
  
-   To open Bing Maps and show a route from a specific address to a specific point:  
  
     `http://bing.com/maps/default.aspx?rtp=adr.One%20Microsoft%20Way,Redmond,WA%2098052~pos.45.23423_-122.1232_MyPlace&rtop=0~1~0`  
  
-   To open Bing Maps and show the driving directions panel with a start address only:  
  
     `http://bing.com/maps/default.aspx?rtp=adr.Seattle,WA`  
  
-   To open Bing Maps and show driving directions to a fictitious pizza restaurant in Redmond, WA:  
  
     `http://bing.com/maps/default.aspx?rtp=~pos.rycz2z4tpkxm_555%20NE%2055th%20St,Redmond,WA_Pizza%20Parlor_425-555-5555`  
  
## Collections editor and collections parameters  
 To create a map that displays information from the collections editor or a specific collection, use the following parameters.  

|**Parameter**|**Definition**|**Example**|**Details**|  
|-|-|-|-|  
|sp|collections editor|sp=adr.One%20Microsoft%20Way,Redmond,WA|Defines a specific entity, address, or pin to add to the map.<br /><br /> Collections editor items are defined as a category and value, separated by a period. There are five categories: **adr**, **point**, **polyline**, **polygon**, and **yp**. These are described in the next table.<br /><br /> Separate multiple items with a tilde (~). If an item contains a tilde, make sure the tilde is encoded as %7E.|  
|cid|collection ID|cid=15A41C376|Specifies the collection that you want to display by using the ID assigned to that collection. For the collection ID parameter, use the following format:<br /><br /> `cid=collection ID`|  
  
 **Collections Categories**  
  
 Use the following formats to add values to a collection.  
  
|**Category**|**Definition**|**Details**|  
|-|-|-|  
|adr|address|Specifies an address to add to the collections editor. For the address, the value can be the address string, the address string and title, or the address string, title, and description.<br /><br /> sp=adr.addressStringsp=adr.addressString_titlesp=adr.addressString_title_description<br /><br /> Make sure that the addresses you provide are as specific as possible.|  
|point|point|Specifies a point to display on the map. For points, the value includes the latitude, longitude, title, notes, a reference URL, and a photo URL, each separated by an underscore (_).<br /><br /> sp=point.latitude_longitude_titleString_notesString_linkURL_photoURL|  
|polyline|polyline|Specifies a polyline on the map by specifying a set of points. For polylines, the value includes a set of latitude and longitude points, a title, notes, a reference  URL, a photo URL, line color, fill color, line weight, line style, dash style, and the latitude and longitude of the label, each separated by an underscore (_).<br /><br /> sp=polyline.lat1_long1_lat2_long2\_..._titleString_notesString_linkURL_photoURL_strokeColor_fillColor_strokeWeight\_ strokeStyle_strokeDashStyle_labelLatitude_labelLongitude<br /><br /> Fill color and stroke color are each specified as hexadecimal RGB values, such as #00ff00.<br /><br /> Stroke weight is specified as a pixel value, such as 4px.<br /><br /> Stroke style includes the following values: Single, ThinThin, ThickThin, ThinThick, ThickBetweenThin.<br /><br /> Stroke dash style includes the following values: Solid, ShortDash, ShortDot, ShortDashDot, ShortDashDotDot, Dot, Dash, LongDash, DashDot, LongDashDot, and LongDashDotDot.|  
|polygon|polygon|Specifies a polygon to draw on the map by using the lat/long positions of its vertices. For polygons, the value includes pairs of latitude and longitude vertex positions, title, notes, link URL, photo URL, line color, fill color, line weight, line style, dash style, and lat/long position of the lable, each separated by an underscore (_).<br /><br /> sp=polyline.lat1_long1_lat2_long2_lat3_long3\_..._titleString_notesString_linkURL_photoURL_strokeColor_fillColor_strokeWeight_strokeStyle_strokeDashStyle_labelLatitude_labelLongitude<br /><br /> Fill color and stroke color are each specified as hexadecimal RGB values, such as #00ff00.<br /><br /> Stroke weight is specified as a pixel value, such as 4px.<br /><br /> Stroke style includes the following values: Single, ThinThin, ThickThin, ThinThick, ThickBetweenThin.<br /><br /> Stroke dash style includes the following values: Solid, ShortDash, ShortDot, ShortDashDot, ShortDashDotDot, Dot, Dash, LongDash, DashDot, LongDashDot, and LongDashDotDot.|  
  
### Examples  
  
-   To open Bing Maps and add the address "1 Microsoft Way, Redmond, WA 98052" to the collections editor:  
  
     `http://bing.com/maps/default.aspx?sp=adr.1%20Microsoft%20Way%2C%20Redmond%2C%20WA%2098052`  
  
-   To open Bing Maps and add a polyline to the collections editor:  
  
     `http://bing.com/maps/default.aspx?sp=Polyline.47.68_-122.12_48.68_-123.12_49.68_-122.12_LINE_some%20notes_http://bing.com__%2300ff00__4px_Single_Solid`  
  
> [!NOTE]
>  The parameters described in this topic are subject to change.