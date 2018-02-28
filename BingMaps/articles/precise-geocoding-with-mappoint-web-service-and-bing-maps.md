---
title: "Precise Geocoding with MapPoint Web Service and Bing Maps | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 9992d643-ffef-4c26-8393-525a33af877a
caps.latest.revision: 11
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Precise Geocoding with MapPoint Web Service and Bing Maps
> [!CAUTION]
>  The content in this article may still be applicable to the current version of the [!INCLUDE[vemc_product_name](../articles/includes/vemc-product-name-md.md)], but it uses a previous version of the [!INCLUDE[vemc_product_name](../articles/includes/vemc-product-name-md.md)] which is no longer supported. More information about the current version of the [!INCLUDE[vemc_product_name](../articles/includes/vemc-product-name-md.md)] is found in the [Bing Map Control SDK](http://msdn.microsoft.com/en-us/library/bb429619.aspx).  
  
 The [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)]`Find` method provides a quick and easy way to obtain the latitude and longitude of a particular location.  However, the geocoding engine uses one of the many common interpolation schemes to determine a street address.  That is, the geocoding engine knows that the 1300 block of Main street starts at position (X1, Y1), and runs to position (X2, Y2).  Finding house 1325 is therefore a matter of taking one quarter of the distance.  Although this mechanism often produces "good enough" results, it can also fail when houses aren't spaced evenly.  
  
 Fortunately, by leveraging the Find service of the [!INCLUDE[mws_product_name](../articles/includes/mws-product-name-md.md)], you can take advantage of a new type of more precise geocoding known as "rooftop geocoding".  The rooftop geocoding engine uses the underlying imagery and much more complex algorithms to precisely locate a street address or a particular building.  With rooftop geocoding, you get a very precise latitude and longitude value from a street address.  
  
 In this article, we will look at the mechanics necessary to leverage rooftop geocoding through [!INCLUDE[mws_product_name](../articles/includes/mws-product-name-md.md)] and [!INCLUDE[vemc_product_name](../articles/includes/vemc-product-name-md.md)].  This article also shows you a fairly standard approach for leveraging any external data source from inside [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)].  
  
 Note: In order to use the code described in this article, you must have an active [!INCLUDE[ve_platform_name](../articles/includes/ve-platform-name-md.md)] account.  To request a developer account, please go to the [Bing Maps Developer Account Request](https://mappoint-css.live.com/MwsSignUp/Default.aspx) page.  
  
## Architecture  
 Since the basic `VEMap.Find` method doesn't leverage the same geocoding engine as [!INCLUDE[mws_product_name](../articles/includes/mws-product-name-md.md)], we have to build three separate components:  
  
1.  Geocoding Application - A mechanism for leveraging the [!INCLUDE[mws_product_name](../articles/includes/mws-product-name-md.md)] to perform rooftop geocoding.  This mechanism should be a single method that accepts an address field and returns a latitude and longitude.  
  
2.  AJAX - A mechanism for calling the geocoding application from a [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] application.  
  
3.  [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] Client – A mechanism for using the geocoding information inside our [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] application.  
  
 The second and third components are both client side JavaScript running on our user's browser.  The first component is an ASP.NET web application running on our servers.  
  
### Component Communication  
 In order to get the three components to talk to each other (and Microsoft's [!INCLUDE[mws_product_name](../articles/includes/mws-product-name-md.md)] farm), we need to use two different communications strategies as shown in Figure 1.  
  
 ![9552b78f&#45;b811&#45;4f47&#45;84cc&#45;a0b908689a62](../articles/media/9552b78f-b811-4f47-84cc-a0b908689a62.gif "9552b78f-b811-4f47-84cc-a0b908689a62")  
  
 *Figure 1: System Architecture*  
  
 The [!INCLUDE[mws_product_name](../articles/includes/mws-product-name-md.md)] component (our Geocoding Application) uses HTTP and SOAP to communicate with Microsoft's [!INCLUDE[mws_product_abbr](../articles/includes/mws-product-abbr-md.md)] servers.  
  
## The Server Side  
 On the server side, we need to build two components:  
  
-   A geocoding class that uses [!INCLUDE[mws_product_name](../articles/includes/mws-product-name-md.md)] to perform the rooftop geocoding.  
  
-   An HttpHandler to listen for requests from and return appropriate responses to the [!INCLUDE[vemc_product_name](../articles/includes/vemc-product-name-md.md)] Application.  
  
 It is easiest to put both components in a new ASP.NET web application.  
  
 Although the code in this article uses C#, you can perform very similar tasks using Visual Basic .NET.  Also, you can use any other language you like for this service.  You could, for example, write a Java web application that leverages AXIS or another Java Web Service API for the geocoding component.  The `HttpHandler` component would be replaced by a `Servlet`.  
  
### The Geocoder  
 Assuming you have started a new ASP.NET 2.0 web application, then you will want to do the following to create the geocoder class:  
  
1.  Add a web reference to the [!INCLUDE[mws_product_name](../articles/includes/mws-product-name-md.md)].  For this article, we will use the staging services at [http://staging.mappoint.net/standard-30/mappoint.wsdl](http://staging.mappoint.net/standard-30/mappoint.wsdl).  For a production system, you would use [http://service.mappoint.net/standard-30/mappoint.wsdl](http://service.mappoint.net/standard-30/mappoint.wsdl).  Name the reference "MapPointService".  
  
2.  Create a new class called RooftopGeocoder.  In an ASP.NET 2.0 application, this class should automatically be placed in the App_Code directory.  
  
3.  In the constructor, create an instance of the FindServiceSoap class and set your [!INCLUDE[mws_product_name](../articles/includes/mws-product-name-md.md)] Credentials:  
  
    ```  
    private MapPointService.FindServiceSoap findService;  
    public RooftopGeocoder()  
      {  
        findService = new MapPointService.FindServiceSoap();  
        findService.Credentials = new System.Net.NetworkCredential("username", "password");  
        findService.PreAuthenticate = true;  
      }  
    ```  
  
     *Listing 1: Initializing the Web Service*  
  
 4.Next, we need to create a method to use rooftop geocoding on an address line.  The method should look something like this:  
  
```  
public string GeocodePoint(string streetAddress)  
{  
    string latlong = "Unavailable";  
  
    //Define the address specification for MWS  
    MapPointService.Address myAddress = new MapPointService.Address();  
    myAddress.FormattedAddress = streetAddress;  
  
    //Set the search options  
    MapPointService.FindOptions myFindOptions = new MapPointService.FindOptions();  
  
    MapPointService.FindAddressSpecification findAddressSpec =   
     new MapPointService.FindAddressSpecification();  
    findAddressSpec.InputAddress = myAddress;  
    findAddressSpec.Options = myFindOptions;  
    findAddressSpec.DataSourceName = "MapPoint.NA";  
  
    //Set the ResultMask to include the rooftop geocoding values  
    findAddressSpec.Options.ResultMask =  
        MapPointService.FindResultMask.RooftopFlag |  
        MapPointService.FindResultMask.LatLongFlag |  
        MapPointService.FindResultMask.EntityFlag |   
        MapPointService.FindResultMask.MatchDetailsFlag |  
        MapPointService.FindResultMask.AddressFlag;  
  
    //Call the MWS FindAddress method  
    MapPointService.FindResults myFindResults = findService.FindAddress(findAddressSpec);  
  
    //Parse the Results  
    MapPointService.FindResult bestResult = myFindResults.Results[0];  
    int matchcode = 0;  
  
    MapPointService.EntityPropertyValue[] props =   
      bestResult.BestViewableLocation.Entity.Properties;  
    //Find MatchedMethod property which tells you whether rooftop was used   
    for (int i =0; i< props.Length; i++)  
    {  
        if (props[i].Name == "MatchedMethod")  
        {  
            matchcode = System.Convert.ToInt32(props[i].Value);  
        }  
    }  
    //Prepare result   
    if (matchcode == 7)  
    {  
        latlong = "new VELatLong(" + bestResult.BestViewableLocation.LatLong.Latitude   
            + ", " + bestResult.BestViewableLocation.LatLong.Longitude + ")";  
    }  
  
    return latlong;  
}  
```  
  
 *Listing 2: Rooftop Geocoding*  
  
 Our function uses the [!INCLUDE[mws_product_name](../articles/includes/mws-product-name-md.md)]`FindAddress` method to find a geocode for the address.  If the `MatchedMethod` property equals "7" then the resulting latitude and longitude are from the rooftop geocoder.  If we have a rooftop geocode, the method returns a string defining a `VELatLong` object containing the geocoded point.  
  
### The HttpHandler  
 The next step on the server side is to create an HttpHandler that will leverage the `RooftopGeocoder` class.  In your ASP.NET application, add a new Generic Handler named "GeocodingHandler".  This handler should expect one parameter (the address).  
  
```  
public void ProcessRequest(HttpContext context)  
{  
    RooftopGeocoder rg = new RooftopGeocoder();  
    context.Response.ContentType = "text/plain";  
    string result = rg.GeocodePoint(context.Request.QueryString["addr"]);  
    context.Response.Write("CreatePin('Rooftop', "+result+ ")");  
}  
```  
  
 *Listing 3: The HttpHandler*  
  
 Notice that we pass the "addr" querystring parameter to an instance of RooftopGeocoder.  We take the returned `VELatLong` object and pass it back to a JavaScript method called "CreatePin".  We'll write that method in the next section.  
  
## The Client Side  
 On the client side, we need a basic HTML page with a [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] map.  We also need to perform two tasks:  
  
-   Write a mechanism for connecting to the geocoder HttpHandler  
  
-   Write a mechanism for users to enter and address and see the resulting geocode location.  
  
 We will also add another method for displaying a regular geocoded point in order to see the difference.  
  
### The Basic Page  
 Since you already have an ASP.NET web project, create a simple HTML page called Rooftop.html.  Replace the contents of the page with the following:  
  
```  
<html>  
<head>  
<title>Rooftop Geocoding</title>  
<script type="text/javascript"   
  src="http://dev.virtualearth.net/mapcontrol/mapcontrol.ashx?v=5"></script>  
<script type="text/javascript">  
  var map;  
  function OnPageLoad()  
  {  
    map = new VEMap('myMap');  
    map.LoadMap();  
  }  
  //Add Additional Code Here  
</script>  
</head>  
<body onload="OnPageLoad();">  
  <div id="myMap" style="position:relative;width:600px;height:400px;"></div>  
</body>  
</html>  
```  
  
 *Listing 4: Rooftop.html basic page*  
  
 This basic page will display a map.  In addition to the map, we need a field for the user to input an address and several other functions to help display the pushpins.  
  
### Adding Controls  
 Adding a text input box to our map will give the user a place to enter an address.  Add the following \<div> tag to Listing 4:  
  
```  
<div id="SearchPanel">  
  <table border=0 width='100%'>  
    <tr><td bgcolor='#C0C0CF'><p align='center'>Search</p></td></tr>  
    <tr><td><p align='left'>  
      Address  
      <INPUT id="txtWhere" type="text" value="" name="txtWhere" style="width: 225px">  
    </td></tr>  
    <tr><td bgcolor='#E0E0E0'><p align='center'>  
      <input type="button" value="Geocode" onclick="Geocode();"   
        id="Geocode" name="Geocode" />  
    </td></tr>  
  <table>  
</div>  
```  
  
 *Listing 5: Adding the controls*  
  
 Next, we need to add a CSS style section to make the control easier to see:  
  
```  
<style type="text/css" media="screen">  
  #SearchPanel  
  {  
    width: 300px;  
    border-style: solid;  
    border-width: 1px;  
    border-color: lightgray;  
    background: white;  
  }  
</style>  
```  
  
 *Listing 6: CSS Styling for Find Control*  
  
 Finally, we need to change the `OnPageLoad` method in Listing 4 to register the SearchPanel div and position it properly.  Add the following lines to the end of `OnPageLoad`:  
  
```  
var geocode = document.getElementById('SearchPanel');  
map.AddControl(geocode);  
geocode.style.left = "300px";  
geocode.style.top = "5px";  
```  
  
 *Listing 7: Registering the control*  
  
 If we load up the HTML page, it should look like this:  
  
 ![f02f9aae&#45;eb20&#45;4de0&#45;a09b&#45;b1b2bd66d222](../articles/media/f02f9aae-eb20-4de0-a09b-b1b2bd66d222.jpg "f02f9aae-eb20-4de0-a09b-b1b2bd66d222")  
  
 *Figure 2: The Basic Page with the Find Control*  
  
### Working with Pushpins  
 When a user enters an address and presses the Geocode button, we want to create two pushpins.  One pin will be generated using rooftop geocoding.  The other will be generated using the default [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] geocoding.  We can start by creating a method to draw custom HTML pins for each of our pushpins.  Our method will accept a string indicating the geocode method and a `VELatLong` indicating the point.  
  
```  
function CreatePin(type, point)  
{  
  if (point != 'Unavailable')  
  {  
    var icon = "<div style='font-size:12px;font-weight:bold;   
      border:solid 2px Black;background-color:Aqua;width:200px;'>"  
    icon += type + ":" + point.Latitude + " : " + point.Longitude;  
    icon += "<div>";  
    var spec = new VECustomIconSpecification();  
    spec.CustomHTML = icon;  
  
    var pin = new VEShape(VEShapeType.Pushpin, point);  
    pin.SetCustomIcon(spec);  
    map.AddShape(pin);  
  }  
}  
```  
  
 *Listing 8: Pin Generation*  
  
 The next step is to add the methods for creating the default [!INCLUDE[ve_product_abbr](../articles/includes/ve-product-abbr-md.md)] geocoded pin:  
  
```  
function AddRegularGeocode(address)  
{  
  map.Find(null, address, null, null, 0, 10, false, false, false, true, ProcessResults)  
}  
  
function ProcessResults(layer, results, places, hasmore)  
{  
  CreatePin("Default", places[0].LatLong);  
}  
```  
  
 *Listing 9: Adding a default geocoded pushpin*  
  
 We need one last method to link our text box to the geocoding methods.  Add the following function to respond to when the user pushes the "geocode" button:  
  
```  
function Geocode()  
{  
  var where = document.getElementById('txtWhere').value;  
  AddRegularGeocode(where);  
  AddRooftopGeocode(where);  
}  
```  
  
 *Listing 10: The Geocode method*  
  
 We now only need to figure out the `AddRooftopGeocode` method, which will be our link between the server side HttpHandler and the client side [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] map.  
  
### The AJAX plumbing  
 In order to connect our client side JavaScript to our server side call to the [!INCLUDE[mws_product_name](../articles/includes/mws-product-name-md.md)] geocoder, we need to add three more methods:  
  
1.  A mechanism for creating an XMLHttp Object to allow us to make HTTP calls.  
  
2.  A callback method to handle the response from the HTTP request  
  
3.  The `AddRooftopGeocode` method to make the HTTP request.  
  
#### Creating an XMLHTTP object  
 Given that we want our application to run in several different types of browser, we can use a standard method for creating our XMLHttp object:  
  
```  
var xmlhttp=false;  
function InitXmlHttp() {  
  // Attempt to initialize xmlhttp object  
  try  
  {  
    xmlhttp = new ActiveXObject("Msxml2.XMLHTTP");  
  }  
  catch (e)  
  {  
    // Try to use different activex object  
    try  
    {  
      xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");  
    }  
    catch (E)  
    {  
      xmlhttp = false;  
    }  
  }  
  // If not initialized, create XMLHttpRequest object  
  if (!xmlhttp && typeof XMLHttpRequest!='undefined')  
  {  
    xmlhttp = new XMLHttpRequest();  
  }  
  // Define function call for when Request obj state has changed  
  xmlhttp.onreadystatechange=SearchHandler;  
}  
```  
  
 *Listing 11: Creating an XMLHttp Object*  
  
 This object will allow us to submit HTTP requests from the client side.  When the response comes back, it will be processed by the `SearchHandler` function.  
  
#### The SearchHandler function  
 The `SearchHandler` function is fairly simple. All we need to do is ensure that we've received the full response and then simply evaluate the response:  
  
```  
function SearchHandler()  
{  
  if (xmlhttp.readyState==4)  
  {  
    eval(xmlhttp.responseText);  
  }  
}  
```  
  
 *Listing 12: The SearchHandler*  
  
#### The AddRoofTopGeocode Method  
 The last step is to use the XMLHttp object to call the GeocodingHandler in our server part of the application.  
  
```  
function AddRooftopGeocode(address)  
{         
  InitXmlHttp();        
  var msg = "GeoCodingHandler.ashx?addr="+escape(address);  
  xmlhttp.open("GET", msg, true);  
  xmlhttp.send(null);  
}  
```  
  
 *Listing 13: Calling the HTTPHandler*  
  
 The handler will return a result containing a call to the CreatePin method we defined in Listing 8.  
  
## Using the Results  
 The next step in this application is to try it out with a few addresses.  Currently, the [!INCLUDE[mws_product_abbr](../articles/includes/mws-product-abbr-md.md)] system provides rooftop geocodes for approximately 40% of all United States addresses, spread all across the country.  The number of addresses is increased regularly as new data becomes available.  
  
 We can see the benefits of Rooftop geocoding with a couple of different examples:  
  
 ![568805b6&#45;6594&#45;4293&#45;9022&#45;43464f78ea9a](../articles/media/568805b6-6594-4293-9022-43464f78ea9a.jpg "568805b6-6594-4293-9022-43464f78ea9a")  
  
 *Figure 3: Geocoding Results*  
  
 In this first example (10880 Wilshire Blvd Ste 1101, Los Angeles, CA 90024-4112) we see a typical commercial scenario where several buildings share the same street address.  In this case, the rooftop geocoding tells us that we want the second building rather than the first big building.  
  
 In another example (1300 Saratoga Ave Unit 701, Ventura, CA 93003-6407), we can see the results in a typical apartment complex:  
  
 ![5d918508&#45;65af&#45;49e1&#45;9658&#45;29445ab28a88](../articles/media/5d918508-65af-49e1-9658-29445ab28a88.jpg "5d918508-65af-49e1-9658-29445ab28a88")  
  
 *Figure 4: Another Geocoding Example*  
  
 A regular geocode may show us the address of the office, or the street entrance to the complex.  The rooftop geocode shows us the exact location.  Delivering a pizza to Unit 701 would be much easier with rooftop geocoding.  
  
## Conclusion  
 The sample code in this article illustrates two key points.  First, you can use the AJAX framework illustrated here to connect your [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] system to any data source.  Whether you are connecting indirectly to [!INCLUDE[mws_product_name](../articles/includes/mws-product-name-md.md)], or connect to your own database, or even a third party data service, you can display the data on your [!INCLUDE[ve_product_name](../articles/includes/ve-product-name-md.md)] map.  
  
 Second, you can leverage the [!INCLUDE[mws_product_name](../articles/includes/mws-product-name-md.md)] advanced rooftop geocoding.  All you need to do is:  
  
1.  Set up a [!INCLUDE[mws_product_name](../articles/includes/mws-product-name-md.md)] account  
  
2.  Create a class to perform the geocoding  
  
3.  Write the AJAX plumbing for both the server side (HttpHandler) and client side.  
  
 Following these simple steps, you could also leverage other components of [!INCLUDE[mws_product_name](../articles/includes/mws-product-name-md.md)], including alternate map views, "line drive" driving directions, and the extended points of interest data sets.