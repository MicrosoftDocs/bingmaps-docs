---
title: "Implementing Driving Directions in Bing Maps | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: b2091c84-ccb5-4594-bfb2-47bedb249c22
caps.latest.revision: 16
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Implementing Driving Directions in Bing Maps
> [!CAUTION]
>  The content in this article may still be applicable to the current version of the [!INCLUDE[vemc_product_name](../articles/includes/vemc-product-name-md.md)], but it uses a previous version of the [!INCLUDE[vemc_product_name](../articles/includes/vemc-product-name-md.md)] which is no longer supported. More information about the current version of the [!INCLUDE[vemc_product_name](../articles/includes/vemc-product-name-md.md)] is found in the [Bing Map Control SDK](http://msdn.microsoft.com/en-us/library/bb429619.aspx).  
  
 In this article we will create a popup context menu to set the start and end points for a journey. We will then discover how to build the code to allow us to retrieve the directions for the journey. Finally we will plot out the route on the map.  
  
 In order to get started, we need a basic HTML page showing a [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] map.  
  
```  
<html>  
<head>  
  <title>Driving Directions in Bing Maps</title>  
  <script src="http://dev.virtualearth.net/mapcontrol/v4/mapcontrol.js"></script>  
  <script>  
    var map = null;  
    function OnPageLoad()  
    {  
      map = new VEMap('myMap');  
      map.LoadMap(new VELatLong(-33.7939, 151.1093), 10, 'r', false);  
      map.SetScaleBarDistanceUnit(VEDistanceUnit.Kilometers);  
    }  
  </script>  
</head>  
<body onload="OnPageLoad();">  
    <div id="myMap" style="position:relative;width:600px;height:400px;"></div>  
</body>  
</html>  
```  
  
 *Listing 1 The starter page (Driving.html)*  
  
 If you open this page in a browser, you will see a map of Sydney, Australia.  Note that the scale bar is in Kilometers.  
  
## The Menu  
 The first thing we need is a way for our user to define a starting point, ending point and ask for directions.  Although we could build a form, a floating context menu seems more appropriate.  
  
### The Menu HTML  
 The first step is to build an HTML menu and add it to the body:  
  
```  
<div id="menu">  
  <ul id="popupmenu" class="pmenu">  
    <li><a href="#" onclick='SetStart()'>Set Start</a></li>  
    <li><a href="#" onclick='SetEnd()'>Set End</a></li>  
    <li><a href="#" onclick='GetDirections()'>Get Directions</a></li>  
  </ul>  
</div>  
```  
  
 *Listing 2 The Menu*  
  
### Menu StyleSheet  
 Next, we need to add the styles that will define the menu.  Put this block of style code in the \<head> section of Listing 1:  
  
```  
<style type="text/css" media="screen">  
  ul, li {margin:0;padding:0;}  
  
  ul.pmenu  
  {  
      position:absolute;  
      margin: 0;  
      padding: 1px;  
      list-style: none;  
      width: 150px; /* Width of Menu Items */  
      border: 1px solid #ccc;  
      background:white;  
      display:none;  
      z-index:10;  
  }  
  
  ul.pmenu li { position: relative; }  
  
  /* Styles for Menu Items */  
  ul.pmenu li a  
  {  
      display: block;  
      text-decoration: none;  
      color: black;  
      padding: 2px 5px 2px 20px;  
  }  
  
  ul.pmenu li a:hover  
  {  
      background:#335EA8;  
      color:white;  
  }  
</style>  
```  
  
 *Listing 3 The Menu CSS*  
  
### Grabbing the ContextMenu Event  
 Last, we need to figure out a way to make our menu appear and disappear.  Since we only want the menu to appear when the user right-clicks on the map area, we can create a JavaScript method to show the map and attach it to the 'onconextmenu' event of our map.  Add the following line to the end of the OnPageLoad() method:  
  
```  
map.AttachEvent("oncontextmenu", ShowPopupMenu);  
```  
  
 *Listing 4 Listening for the context menu event.*  
  
 Now we need to write the JavaScript to show the menu:  
  
```  
function ShowPopupMenu(e)  
{  
  popuplat = e.view.LatLong.Latitude;  
  popuplon = e.view.LatLong.Longitude;  
  var latlong = map.LatLongToPixel(new VELatLong(popuplat,popuplon));  
  
  var x = map.GetLeft();  
  var y = map.GetTop();  
  
  var menu = document.getElementById('popupmenu');  
  menu.style.display='block'; //Showing the menu  
  menu.style.left = latlong.x + x; //Positioning the menu  
  menu.style.top = latlong.y + y;  
}  
```  
  
 *Listing 5 Showing the Menu*  
  
 Note that we actually are going to need two global variables (popuplat, popuplon), so add two definition lines at the beginning of the script block:  
  
```  
var popuplat;  
var popuplon;  
```  
  
 *Listing 6 Global variables*  
  
 These variables are going to define the cursor position for when we add our start and end points.  
  
 If you try your code now, you should see a popup menu when you right click anywhere on the map.  Of course, none of the functions work and you can't close the menu.  Our next task will be to create shells for all three methods and figure out how to close the menu.  
  
### Shell Methods for Start, End and Directions  
 Unfortunately, as soon as the menu opens, the VEMap control has no way of knowing when additional mouse events occur.  That is, we can't simply capture a "click" event and close the map.  Instead, we have to perform some "bad programming" and manually close the menu at the end of each of our functions.  Add the following hollow implementations to your code:  
  
```  
function RemovePopupMenu()  
{  
  var menu = document.getElementById('popupmenu').style.display='none';  
}  
  
function SetStart()  
{  
  RemovePopupMenu();  
}  
  
function SetEnd()  
{  
  RemovePopupMenu();  
}  
  
function GetDirections()  
{  
  RemovePopupMenu();  
}  
```  
  
 *Listing 7 Shell functions*  
  
 Note that every one of our menu functions has to call the RemovePopupMenu() function in order to close the menu.  
  
 At this point, you should have a [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] map, with a popup menu that will close if you select any option.  
  
### Setting the Start and End  
 Now, before we can actually request driving directions, we need to set our start point and end point.  Our sequence of events will be:  
  
1.  Remove the existing start or end pin (if there is one).  
  
2.  Create a pushpin for the start (or end).  
  
3.  Store the latitude and longitude in a VELatLong object.  
  
4.  Close the popup menu.  
  
 First, we want to add two more global variables:  
  
```  
var startpt = null;  
var endpt = null;  
```  
  
 *Listing 8 More global variables*  
  
 Next, we want to create the pushpin in our SetStart method:  
  
```  
function SetStart()  
{  
  try {  
    map.DeletePushpin('start');  
  } catch(err) {}  
  
  startpt = new VELatLong(popuplat, popuplon);  
  var pin = new VEPushpin('start', startpt, null, 'Start Here', 'Starting point');  
  map.AddPushpin(pin);  
  
  RemovePopupMenu();  
}  
```  
  
 *Listing 9 The SetStart method*  
  
 Note that the DeletePushpin() method throws an exception if the pushpin doesn't exist.  Since we also get an exception if we try to add a new pushpin with the same ID as an existing pushpin, we have to perform a workaround.  Basically, we try to delete the pushpin.  If it doesn't exist, we catch the exception, but continue anyway since the exception doesn't break our functionality.  Also, if we wanted to use a custom pushpin, we could replace the null third parameter with a URL to an image.  
  
 Our SetEnd method is almost identical:  
  
```  
function SetEnd()  
{  
  try {  
    map.DeletePushpin('end');  
  } catch(err) {}  
  
  endpt = new VELatLong(popuplat, popuplon);  
  var pin = new VEPushpin('end', endpt, null, 'pin', 'end');  
  map.AddPushpin(pin);  
  
  RemovePopupMenu();  
}  
```  
  
 *Listing 10 The SetEnd method*  
  
 Our application should now show our popup menu and allow us to create pushpins for the starting and ending points of our route.  
  
### Driving Directions  
 The real magic of driving directions consists of a single call to the VEMap object.  All we have to do is pass our start point, end point, and a few other parameters into the GetRoute method, and we will have a nice route automatically drawn on our map.  
  
```  
function GetDirections()  
{  
  map.GetRoute(startpt, endpt, VEDistanceUnit.Kilometers, VERouteType.Quickest);  
  RemovePopupMenu();  
}  
```  
  
 *Listing 11 Getting Directions*  
  
 Note that we are reusing the endpoints created by the start and end methods.  We're also setting all of our directions so that they will display with Kilometers (remember, we're looking at a map of Sydney!), and we are going to use the quickest route rather than the shortest route.  
  
 Of course, we may want to display the text directions for our users.  Although we would most likely want to create a custom panel, in this example, we will simply print the directions to an alert popup message.  All we have to do is slightly modify our GetRoute() call to pass in a callback function:  
  
```  
function GetDirections()  
{  
  map.GetRoute(startpt, endpt, VEDistanceUnit.Kilometers, VERouteType.Quickest,   
    OnGotRoute);  
  RemovePopupMenu();  
}  
```  
  
 *Listing 12 Modified GetDirections method*  
  
 Now we need to create our OnGotRoute function, which will process the array of driving directions returned by the GetRoute() call.  
  
```  
function OnGotRoute(route)  
{  
  var routeinfo="Route info:\n\n";  
  routeinfo+="Total distance: ";  
  routeinfo+=   route.Itinerary.Distance+" ";  
  routeinfo+=   route.Itinerary.DistanceUnit+"\n";  
  var steps="";  
  var len = route.Itinerary.Segments.length;  
  for(var i = 0; i < len ;i++)  
  {  
    steps+=route.Itinerary.Segments[i].Instruction+" -- (";  
    steps+=route.Itinerary.Segments[i].Distance+") ";  
    steps+=route.Itinerary.DistanceUnit+"\n";  
  }  
  routeinfo+="Steps:\n"+steps;  
  alert(routeinfo);  
}  
```  
  
 *Listing 13 The OnGotRoute callback*  
  
 Now, whenever our users click on Get Directions (after setting a start and end), they will not only see the directions overlaid on the map, but they will also see the written directions in a popup window.  
  
### Conclusion  
 Although the base VEMap control gives you easy access to driving directions, you may find circumstances where you need greater control, or want to perform more complex routing.  Fortunately, you can leverage [!INCLUDE[mws_product_name](../articles/includes/mws-product-name-md.md)] (the other part of the [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)]) and integrate the returned routes into your [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] display.  If you need more complex routing solutions, please examine [!INCLUDE[mws_product_name](../articles/includes/mws-product-name-md.md)].  
  
 This article is an update of an article originally contributed by [Dr Neil Roodyn](http://www.roodyn.com/). The update was performed by [Robert McGovern MVP (Bing Maps/MapPoint)](https://mvp.support.microsoft.com/profile=A9159573-40DB-4BD1-A079-D57C675E1766).  
  
 The final source for the complete example is as follows:  
  
```  
<html>  
<head>  
  <title>Driving Directions in Bing Maps</title>  
  <style type="text/css" media="screen">  
    ul, li {margin:0;padding:0;}  
  
    ul.pmenu  
    {  
        position:absolute;  
        margin: 0;  
        padding: 1px;  
        list-style: none;  
        width: 150px; /* Width of Menu Items */  
        border: 1px solid #ccc;  
        background:white;  
        display:none;  
        z-index:10;  
    }  
  
    ul.pmenu li { position: relative; }  
  
    /* Styles for Menu Items */  
    ul.pmenu li a  
    {  
        display: block;  
        text-decoration: none;  
        color: black;  
        padding: 2px 5px 2px 20px;  
    }  
  
    ul.pmenu li a:hover  
    {  
        background:#335EA8;  
        color:white;  
    }  
  </style>  
  
  <script src="http://dev.virtualearth.net/mapcontrol/v4/mapcontrol.js"></script>  
  <script>  
    var map = null;  
    var popuplat;  
  var popuplon;  
  var startpt = null;  
  var endpt = null;  
  
  function OnPageLoad()  
  {  
    map = new VEMap('myMap');  
    map.LoadMap(new VELatLong(-33.7939, 151.1093), 10, 'r', false);  
    map.SetScaleBarDistanceUnit(VEDistanceUnit.Kilometers);  
    map.AttachEvent("oncontextmenu", ShowPopupMenu);  
  
  }  
  
  function ShowPopupMenu(e)  
  {  
    popuplat = e.view.LatLong.Latitude;  
    popuplon = e.view.LatLong.Longitude;  
    var latlong = map.LatLongToPixel(new VELatLong(popuplat,popuplon));  
  
    var x = map.GetLeft();  
    var y = map.GetTop();  
  
    var menu = document.getElementById('popupmenu');  
    menu.style.display='block'; //Showing the menu  
    menu.style.left = latlong.x + x; //Positioning the menu  
    menu.style.top = latlong.y + y;  
  }  
  
  function RemovePopupMenu()  
  {  
    var menu = document.getElementById('popupmenu').style.display='none';  
  }  
  
  function SetStart()  
  {  
    try {  
    map.DeletePushpin('start');  
    } catch(err) {}  
  
    startpt = new VELatLong(popuplat, popuplon);  
    var pin = new VEPushpin('start', startpt, null, 'Start Here', 'Starting point');  
    map.AddPushpin(pin);  
  
    RemovePopupMenu();  
  }  
  
  function SetEnd()  
  {  
    try {  
    map.DeletePushpin('end');  
    } catch(err) {  
  
    endpt = new VELatLong(popuplat, popuplon);  
    var pin = new VEPushpin('end', endpt, null, 'pin', 'end');  
    map.AddPushpin(pin);  
  
    RemovePopupMenu();  
  }  
  
  function GetDirections()  
  {  
    map.GetRoute(startpt, endpt, VEDistanceUnit.Kilometers, VERouteType.Quickest, OnGotRoute);  
  
    RemovePopupMenu();  
  }  
  
  function OnGotRoute(route)  
  {  
    var routeinfo="Route info:\n\n";  
    routeinfo+="Total distance: ";  
    routeinfo+=   route.Itinerary.Distance+" ";  
    routeinfo+=   route.Itinerary.DistanceUnit+"\n";  
    var steps="";  
    var len = route.Itinerary.Segments.length;  
    for(var i = 0; i < len ;i++)  
    {  
      steps+=route.Itinerary.Segments[i].Instruction+" -- (";  
      steps+=route.Itinerary.Segments[i].Distance+") ";  
      steps+=route.Itinerary.DistanceUnit+"\n";  
    }  
    routeinfo+="Steps:\n"+steps;  
    alert(routeinfo);  
  }  
  
  </script>  
</head>  
<body onload="OnPageLoad();">  
    <div id="myMap" style="position:relative;width:600px;height:400px;"></div>  
  <div id="menu">  
    <ul id="popupmenu" class="pmenu">  
    <li><a href="#" onclick='SetStart()'>Set Start</a></li>  
    <li><a href="#" onclick='SetEnd()'>Set End</a></li>  
    <li><a href="#" onclick='GetDirections()'>Get Directions</a></li>  
    </ul>  
  </div>  
</body>  
</html>  
```  
  
 *Listing 14 Complete Listing for Driving.html*