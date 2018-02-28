---
title: "Creating a Basic Map Control | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 97fbc75e-1e2c-4181-87a8-59fb249c41a3
caps.latest.revision: 9
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Creating a Basic Map Control



## Create a Bing Maps Account and Get a Key

Before you begin developing your application, you need to create a developer account on the Bing Maps Account Center. A Bing Maps Developer Account allows you to create a Bing Maps Key to use in your map application. Getting a key is described in the [Getting a Bing Maps Key](https://msdn.microsoft.com/library/ff428642.aspx) topic.

## Loading a map

Displaying the default map, which includes all of the navigation functionality, consists of the following steps:

1.	At the top of the HTML page, add the following DOCTYPE declaration.

```
<!DOCTYPE html>
```

2.	In the header section of an HTML page, add a META element with the charset attribute set to "utf-8", as follows:

```
<meta charset="utf-8" />
```

Alternatively, you can also use the older HTML4 method of specifying that UTF8 character sets are used:

```
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
```

**Note:** It is recommended that you use UTF-8 encoding in your application as it is capable of encoding all possible characters in Unicode. It is also widely supported by browsers and will ensure that your application renders correctly across the most browsers and devices. 

3. In the header section or the body of the page add a reference to the map control script. You specify your Bing Maps key as part of the map script URL.  The map control can be loaded asynchronously by specifying a callback function in the script URL and by adding "async defer" to the script tag as follows:

```
<script type='text/javascript' src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap&key=[YOUR_BING_MAPS_KEY]' async defer></script>
```

To use SSL, change http to https:

```
<script type='text/javascript' src='https://www.bing.com/api/maps/mapcontrol?callback=GetMap&key=[YOUR_BING_MAPS_KEY]' async defer></script>
```

This will result in the browser inheriting the protocol from the website and automatically selecting HTTP or HTTPS as needed.

**Tip**: If you refresh the page when using an async script reference to the map control, it will trigger the callback instantly as all the script is already loaded, however, the callback function or the map div may not yet be loaded on the page and would result in an error. To prevent this from happening, It is recommended that you add the map script tag to the bottom of the body of the page after the map div and all other script references. 

4.	In the body of the page, add a DIV element to the page to contain the map. The size of the map is defined by the height and width of the DIV element. The position of the map is set by using the "position", "top", and "left" properties. You can set these values either inline or by defining the values in a style class and then referencing that class, as follows.

```
<div id="myMap" style='position:relative;width:600px;height:400px;'></div>
```

or CSS Style:

```
#myMap {
    position: relative;
    width: 600px;
    height: 400px;
}
```

HTML
```
<div id="myMap"></div>
```


5.	Next, within a new script tag, create a function that can be called when your application loads.

```
<script type="text/javascript">
   function GetMap()
   {
   }
</script>
```

If loading the map synchronously, you can trigger the GetMap function by adding it to the onload event of the body tag.
 
```
<body onload="GetMap();">

var map = new Microsoft.Maps.Map('#myMap');
```

6.	Finally, you can create an instance of the Map Class in the GetMap function. There are two different ways to do this in the Bing Maps V8 SDK. The recommended way to load the map is to use the asynchronous method which loads all the required resources needed by the map in the background and then triggers a callback function when the map has been loaded.  When loading the map, you need to add a reference to the DIV element where you want the map to load. Here is how to load the map asynchronously:


The following is the full code required for loading a map asynchronously.

```
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />

    <!-- Reference to the Bing Maps SDK -->
    <script type='text/javascript'
            src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap&key=[YOUR_BING_MAPS_KEY]' 
            async defer></script>
    
    <script type='text/javascript'>
    function GetMap()
    {
        var map = new Microsoft.Maps.Map('#myMap');

        //Add your post map load code here.
    }
    </script>
</head>
<body>
    <div id="myMap" style="position:relative;width:600px;height:400px;"></div>
</body>
</html>
```