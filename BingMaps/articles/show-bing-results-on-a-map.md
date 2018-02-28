---
title: "Show Bing Results on a  Map | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: e0cf1327-1d5c-4633-b0ef-87310f6320b8
caps.latest.revision: 5
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Show Bing Results on a  Map
This article shows how to build a web page that uses the [Bing API, Version 2](http://msdn.microsoft.com/en-us/library/dd251056.aspx) to search for Phonebook entries near a location and then displays the results on a map by using the [Bing Maps AJAX Control, Version 7.0](../Topic/Bing%20Maps%20AJAX%20Control,%20Version%207.0.md) (interactive map) or the [Bing Maps REST Services](../rest-services/bing-maps-rest-services.md) (static map). The [!INCLUDE[bm_rest_product_name](../articles/includes/bm-rest-product-name-md.md)] is used to geocode the specified location.  
  
 The complete web page is listed at the end of the article.  
  
## Setup  
  
### Get a Bing Maps Key and a Bing Application ID  
 You need a [!INCLUDE[maps_ticket](../articles/includes/maps-ticket-md.md)] to use the [Bing Maps APIs](http://msdn.microsoft.com/en-us/library/dd877180.aspx) and a Bing Application ID to access the [Bing API, Version 2](http://msdn.microsoft.com/en-us/library/dd251056.aspx). If you do not have a [!INCLUDE[maps_ticket](../articles/includes/maps-ticket-md.md)], see [Getting a Bing Maps Key](../getting-started/getting-a-bing-maps-key.md). If you do not have a Bing Application ID, see [Getting Started with Bing API, Version 2](http://msdn.microsoft.com/en-us/library/dd251020.aspx).  
  
### Create a basic web page  
  
1.  Copy the following basic HTML content and save it as a file with an .htm extension.  
  
    ```  
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"   
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">  
    <html>  
    <head>  
        <title>Search and Map</title>  
    </head>  
    <body>  
    </body>  
    </html>  
  
    ```  
  
2.  Add the following elements to the header section of your HTML page. These elements set the content type to UTF-8 which is recommended. The script elements setup the reference to the map control, your Bing Application ID and your Bing Maps Key.  
  
    > [!IMPORTANT]
    >  Make sure you replace the placeholder text below with your Bing Application ID and Bing Maps Key.  
  
    ```  
  
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />  
    <script type="text/javascript" src="http://ecn.dev.virtualearth.net/mapcontrol/mapcontrol.ashx?v=7.0"></script>  
    <script type="text/javascript">  
  
        // Replace the following string with the Bing Maps Key you received from the  
        // Bing Maps Account Center http://www.bingmapsportal.com  
        var BingMapsKey = "INSERT_BING_MAPS_KEY";  
  
        // Replace the following string with the Application ID you received from the  
        // Bing Developer Center.  
        var AppId = "INSERT_BING_APPLICATION_ID";   
  
        // Initialize the AJAX 7 map  
        var map = null;  
    </script>  
  
    ```  
  
### Add a function to submit REST Services and Bing API requests  
 The [!INCLUDE[bm_rest_product_name](../articles/includes/bm-rest-product-name-md.md)] and Bing API, Version 2.0 use a Representational State Transfer (REST) interface that makes HTTP requests. Insert the following function within the second set of script tags in your HTML page. This function executes REST URL requests dynamically.  
  
```  
//Makes a service request for the Bing Map REST Services and Bing 2.0 Search Service  
function MakeServiceRequest(request) {  
    var script = document.createElement("script");  
    script.setAttribute("type", "text/javascript");  
    script.setAttribute("src", request);  
    document.body.appendChild(script);  
}  
  
```  
  
### Add body text and user input  
 Insert the following HTML in the body section of your HTML page. This HTML code includes input fields for the user to specify a location and select a distance to use as “find nearby” search parameters. There are also DIV elements that will hold the search results and map.  
  
```  
<div style="color:#330000;font-size:larger;font-family:Arial,Sans-Serif">  
    <p> Search and Map Entities Near a Location </p>  
</div>  
<div style="color:#003366;font-size:large;margin-bottom:10px"><span>Search for&nbsp;</span>  
    <input id="queryTerm" type="text" value="Insert search term" size="30" />    
</div>  
<div style="color:#003366;font-size:large"><span>Search within&nbsp;</span>  
    <select id="distance">  
        <option value="1">1</option>  
        <option value="5">5</option>  
        <option value="10" selected="selected">10</option>  
        <option value="25">25</option>  
        <option value="50">50</option>  
        <option value="100">100</option>  
        <option value="200">200</option>    
        <option value="400">400</option>  
    </select><span>&nbsp;kilometers of&nbsp;</span>  
    <input id="address" type="text" value="Insert Location/Address" size="30" />    
    <input type="button" value="Search" onclick="Geocode()" />  
</div>   
<div>  
    <div id="mapDiv" style="padding-left:10px;"></div>  
    <div id="output" style="float:left;" ></div>  
</div>  
  
```  
  
## Geocode the location using the REST Services  
 Insert the following functions within the second set of script tags. When the user inputs a location, the Geocode function builds a REST URL request that geocodes the location data and returns a JSON response. The [!INCLUDE[bm_rest_product_name](../articles/includes/bm-rest-product-name-md.md)][Find a Location by Address](../rest-services/find-a-location-by-address.md) API is used to geocode the location information. The response is provided to the GetLocationCoordinates  JSON callback function to retrieve the geocoded latitude and longitude from the response. These coordinates are then passed to the Search function defined in the next section.  
  
```  
//Geocode the location specified by the user  
function Geocode() {  
    //Create Bing Maps REST Services request to geocode the address provided by the user  
    var geocodeRequest = "http://dev.virtualearth.net/REST/v1/Locations/"  
       + document.getElementById('address').value  
       + "?output=json"  
       //Set the callback function  
       + "&jsonp=GetLocationCoordinates"  
       + "&key=" + BingMapsKey;  
    //Submit the request  
    MakeServiceRequest(geocodeRequest);  
}  
  
//Get the geocoded latitude and longitude from the response  
function GetLocationCoordinates(geocodeResponse) {  
    if (geocodeResponse &&  
           geocodeResponse.resourceSets &&  
           geocodeResponse.resourceSets.length > 0 &&  
           geocodeResponse.resourceSets[0].resources &&  
           geocodeResponse.resourceSets[0].resources.length > 0) {  
  
        Search(geocodeResponse.resourceSets[0].resources[0].point.coordinates[0], geocodeResponse.resourceSets[0].resources[0].point.coordinates[1]);  
  
    }  
    else {//The location could not be geocoded  
        document.getElementById("output").innerHTML = "";  
        var output = document.getElementById("output");  
        var resultsHeader = document.createElement("h4");  
        output.appendChild(resultsHeader);  
        resultsHeader.innerHTML = "The location could not be geocoded";  
    }  
}  
  
```  
  
## Search for Phonebook entries using the specified query string  
 Insert the following Search function with the second set of script tags. The Search function creates a Bing, Version 2.0 request for Phonebook results that match the query string provided by the user.  
  
```  
// Search for Phonebook results using the Bing, Version 2.0 API  
// and the query string provided by the user  
function Search(lat, long) {  
    //Get the distance to search selected by the user  
    var distance = document.getElementById('distance').value;  
  
    queryString = document.getElementById('queryTerm').value;  
    if ((queryString != null)&&(queryString !="Insert search term")){  
        var requestStr = "http://api.bing.net/json.aspx?"                  
        // Common request fields (required)  
        + "AppId=" + AppId  
        + "&Query=" + queryString  
        + "&Sources=Phonebook"  
  
        // Common request fields   
        + "&Version=2.0"  
        + "&Market=en-us"  
        + "&UILanguage=en"  
        + "&Latitude=" + lat  
        + "&Longitude=" + long  
        + "&Radius=" + distance  
        + "&Options=EnableHighlighting"  
  
        // Phonebook-specific request fields (optional)  
        + "&Phonebook.Count=10"  
        + "&Phonebook.Offset=0"  
        + "&Phonebook.FileType=YP"  
        + "&Phonebook.SortBy=Distance"  
  
        // Set the JSON callback function  
        + "&JsonType=callback"  
        + "&JsonCallback=MapResults";  
  
        var output = document.getElementById("output");  
        //Make URL service request  
        MakeServiceRequest(requestStr);  
        }  
     else {//The query string is undefined.  
        document.getElementById("output").innerHTML = "";  
        var output = document.getElementById("output");  
        var resultsHeader = document.createElement("h4");  
        output.appendChild(resultsHeader);  
        resultsHeader.innerHTML = "Please enter a query string.";  
  
    }  
}  
  
```  
  
## Show results on an interactive map  
 Insert the following functions within the second set of script tags. The MapResults function displays the address information for the search results and shows the locations on an [!INCLUDE[bmmc_product_name](../articles/includes/bmmc-product-name-md.md)] interactive map. The ReplaceHighlightingCharacters function replaces encoded characters in the location information with HTML \<strong> characters.  
  
```  
//Show search results and display the corresponding locations  
// on an interactive (AJAX 7) map  
function MapResults(response) {  
    //Create list of results  
    document.getElementById("output").innerHTML = "";  
    var output = document.getElementById("output");  
    var resultsHeader = document.createElement("h4");  
    var resultsList = document.createElement("ol");  
    output.appendChild(resultsHeader);  
    output.appendChild(resultsList);  
  
    if (response.SearchResponse.Phonebook != null) {  
        //Get phonebook results  
        var results = response.SearchResponse.Phonebook.Results;  
  
        //Create pushpin collection  
        var pushpins = new Microsoft.Maps.EntityCollection();  
  
        //initialize bounds for map area  
        var minLatitude = results[0].Latitude; var maxLatitude = results[0].Latitude;  
        var minLongitude = results[0].Longitude; var maxLongitude = results[0].Longitude;  
  
        // Display the results header.  
        resultsHeader.innerHTML = "Phonebook results for "  
             + response.SearchResponse.Query.SearchTerms;  
  
        // Display the Phonebook results.  
        var resultsListItem = null;  
        var resultStr = "";  
  
        for (var i = 0; i < results.length; ++i) {  
            resultsListItem = document.createElement("li");  
            resultsList.appendChild(resultsListItem);  
            resultStr = results[i].Business  
                + "<br />"  
                + results[i].Address  
                + "<br />"  
                + results[i].City  
                + ", "  
                + results[i].StateOrProvince  
                + "<br />"  
                + results[i].PhoneNumber  
                + "<br />Average Rating: "  
                + results[i].UserRating  
                + "<br /><br />";  
  
            // Replace highlighting characters with strong tags.  
            resultsListItem.innerHTML = ReplaceHighlightingCharacters(  
                    resultStr,  
                    "<strong>",  
                    "</strong>");  
  
            // Add pushpin to map collection  
            var pushpinVal = (i + 1).toString();  
             pushpins.push(new Microsoft.Maps.Pushpin(new Microsoft.Maps.Location(results[i].Latitude, results[i].Longitude), { text: pushpinVal }));  
  
            //Determine bounds that display all pushpins  
            if (results[i].Latitude > maxLatitude)  
            { maxLatitude = results[i].Latitude; }  
            else if (results[i].Latitude < minLatitude)  
            { minLatitude = results[i].Latitude; }  
  
            if (results[i].Longitude > maxLongitude)  
            { maxLongitude = results[i].Longitude; }  
            else if (results[i].Longitude < minLongitude)  
            { minLongitude = results[i].Longitude; }  
        }  
  
        //Create map  
  
        mapDiv.style.visibility = "visible";  
        if (map != null) { map.dispose() };  
        map = new Microsoft.Maps.Map(document.getElementById("mapDiv"), { credentials: BingMapsKey, height: 400, width: 400, mapTypeId: "r" });  
  
        //Add pushpins to the map  
        map.entities.push(pushpins);  
  
        //Add padding to map area so that pushpins are not on the edge  
        minLatitude -= 0.0001;  
        maxLatitude += 0.0001;  
        minLongitude -= 0.0001;  
        maxLongitude += 0.0001;  
        var mapArea = Microsoft.Maps.LocationRect.fromLocations(new Microsoft.Maps.Location(minLatitude, minLongitude), new Microsoft.Maps.Location(maxLatitude, maxLongitude));  
        map.setView({ bounds: mapArea });  
    }  
    else { //No results were returned  
        resultsHeader.innerHTML = "No results were found for &quot;" + response.SearchResponse.Query.SearchTerms  
               + "&quot;. Please try another search term and/or increase the search distance.";  
        resultsHeader.style.color = "DarkRed";  
        resultsHeader.style.fontFamily = "sans-serif";  
        resultsHeader.style.fontWeight = "normal";  
        if (map != null) { map.dispose(); }  
    }  
}  
  
function ReplaceHighlightingCharacters(text, beginStr, endStr) {  
    // Replace all occurrences of U+E000 (begin highlighting) with  
    // beginStr. Replace all occurrences of U+E001 (end highlighting)  
    // with endStr.  
    var regexBegin = new RegExp("\uE000", "g");  
    var regexEnd = new RegExp("\uE001", "g");  
  
    return text.replace(regexBegin, beginStr).replace(regexEnd, endStr);  
}  
  
```  
  
## View in browser  
 You have now created a web application. Save your file and view it in a browser such as Internet Explorer. Some browsers, such as Internet Explorer 9, may require you to allow the use of scripts on the page. Make sure to insert your [!INCLUDE[maps_ticket](../articles/includes/maps-ticket-md.md)] and Bing Application ID before viewing.  
  
## Alternative: Show the results on a static map  
 If you prefer to show the search results on a static map, use the following StaticMapResults function in place of the MapResults function. To do this, insert this function in the second set of script tags and change the JSON Callback function for the [!INCLUDE[bm_spatialapi_product_name](../articles/includes/bm-spatialapi-product-name-md.md)] from MapResults to StaticMapResults. The StaticMapResults function uses a [Get a Static Map](../rest-services/get-a-static-map.md) REST URL that is part of the [!INCLUDE[bm_rest_product_name](../articles/includes/bm-rest-product-name-md.md)][Imagery](../rest-services/imagery-api.md).  
  
 **StaticMapResults function**  
  
```  
     function StaticMapResults(response) {  
        //Create list of results  
        document.getElementById("output").innerHTML = "";  
        var output = document.getElementById("output");  
        var resultsHeader = document.createElement("h4");  
        var resultsList = document.createElement("ol");  
        output.appendChild(resultsHeader);  
        output.appendChild(resultsList);  
  
        //Create REST Static Image URL  
        var mapURL = "http://dev.virtualearth.net/REST/v1/Imagery/Map/Road?mapVersion=v1&key=" + BingMapsKey;  
  
        if (response.SearchResponse.Phonebook != null) {  
            //Get phonebook results  
            var results = response.SearchResponse.Phonebook.Results;  
  
            //initialize bounds for map area  
            var minLatitude = results[0].Latitude; var maxLatitude = results[0].Latitude; ;  
            var minLongitude = results[0].Longitude; var maxLongitude = results[0].Longitude;  
            // Display the results header.  
            resultsHeader.innerHTML = "Phonebook results for "  
                 + response.SearchResponse.Query.SearchTerms;  
  
            // Display the Phonebook results.  
            var resultsListItem = null;  
            var resultStr = "";  
  
            for (var i = 0; i < results.length; ++i) {  
                resultsListItem = document.createElement("li");  
                resultsList.appendChild(resultsListItem);  
                resultStr = results[i].Business  
                    + "<br />"  
                    + results[i].Address  
                    + "<br />"  
                    + results[i].City  
                    + ", "  
                    + results[i].StateOrProvince  
                    + "<br />"  
                    + results[i].PhoneNumber  
                    + "<br /><br />";  
  
                // Replace highlighting characters with strong tags.  
                resultsListItem.innerHTML = ReplaceHighlightingCharacters(  
                        resultStr,  
                        "<strong>",  
                        "</strong>");  
  
                if (results[i].Latitude > maxLatitude)  
                { maxLatitude = results[i].Latitude; }  
                else if (results[i].Latitude < minLatitude)  
                { minLatitude = results[i].Latitude; }  
  
                if (results[i].Longitude > maxLongitude)  
                { maxLongitude = results[i].Longitude; }  
                else if (results[i].Longitude < minLongitude)  
                { minLongitude = results[i].Longitude; }  
  
                mapURL = mapURL + "&pp=" + results[i].Latitude.toString() + "," + results[i].Longitude.toString() + ";;" + (i + 1).toString();  
            }  
  
            minLatitude -= 0.0001;  
            maxLatitude += 0.0001;  
            minLongitude -= 0.0001;  
            maxLongitude += 0.0001;  
  
            mapURL = mapURL + "&mapArea=" + minLatitude.toString() + "," + minLongitude.toString() + ","  
                            + maxLatitude.toString() + "," + maxLongitude.toString()   
                            + "&declutter=1";  
  
            //Create img element to hold static map  
            var map = document.createElement("img");  
            map.setAttribute("alt","Static Map showing Fourth Coffee Shops");  
            map.setAttribute("style", "padding-left: 10px");  
            map.setAttribute("src", mapURL);  
            document.getElementById("mapDiv").appendChild(map);  
            }  
        else { //No results were returned  
            resultsHeader.innerHTML = "No locations were found. Please try another location or increase the search distance."  
            resultsHeader.style.color = "DarkRed";  
            resultsHeader.style.fontFamily = "sans-serif";  
            resultsHeader.style.fontWeight = "normal";  
            map.dispose();  
        }  
  
}  
  
```  
  
 **Search function showing JSON Callback function name change**  
  
```  
// Search for Phonebook results using the Bing, Version 2.0 API  
// and the query string provided by the user  
function Search(lat, long) {  
    //Get the distance to search selected by the user  
    var distance = document.getElementById('distance').value;  
  
    queryString = document.getElementById('queryTerm').value;  
    if ((queryString != null)&&(queryString !="Insert search term")){  
        var requestStr = "http://api.bing.net/json.aspx?"                  
        // Common request fields (required)  
        + "AppId=" + AppId  
        + "&Query=" + queryString  
        + "&Sources=Phonebook"  
  
        // Common request fields   
        + "&Version=2.0"  
        + "&Market=en-us"  
        + "&UILanguage=en"  
        + "&Latitude=" + lat  
        + "&Longitude=" + long  
        + "&Radius=" + distance  
        + "&Options=EnableHighlighting"  
  
        // Phonebook-specific request fields (optional)  
        + "&Phonebook.Count=10"  
        + "&Phonebook.Offset=0"  
        + "&Phonebook.FileType=YP"  
        + "&Phonebook.SortBy=Distance"  
  
        // Set the JSON callback function  
        + "&JsonType=callback"  
        + "&JsonCallback=StaticMapResults";  
  
        var output = document.getElementById("output");  
        //Make URL service request  
        MakeServiceRequest(requestStr);  
        }  
     else {//The query string is undefined.  
        document.getElementById("output").innerHTML = "";  
        var output = document.getElementById("output");  
        var resultsHeader = document.createElement("h4");  
        output.appendChild(resultsHeader);  
        resultsHeader.innerHTML = "Please enter a query string.";  
    }  
}  
  
```  
  
## Complete Sample  
 The following is the complete sample and can display an AJAX 7 interactive map or a REST Services static map. The code to display the alternative static map is in comments. Make sure to insert your [!INCLUDE[maps_ticket](../articles/includes/maps-ticket-md.md)] and Bing Application ID before running the sample.  
  
```  
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"   
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">  
<html>  
<head>  
    <title>Search and Map</title>  
  
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />  
    <script type="text/javascript" src="http://ecn.dev.virtualearth.net/mapcontrol/mapcontrol.ashx?v=7.0"></script>  
    <script type="text/javascript">  
  
        // Replace the following string with the Bing Maps Key you received from the  
        // Bing Maps Account Center http://www.bingmapsportal.com  
        var BingMapsKey = "INSERT_BING_MAPS_KEY";  
  
        // Replace the following string with the AppId you received from the  
        // Bing Developer Center.  
        var AppId = "INSERT_BING_APPLICATION_ID";   
  
        // Initialize the AJAX 7 map  
        var map = null;  
  
        //Makes a service request for the Bing Map REST Services and Bing 2.0 Search Service  
        function MakeServiceRequest(request) {  
            var script = document.createElement("script");  
            script.setAttribute("type", "text/javascript");  
            script.setAttribute("src", request);  
            document.body.appendChild(script);  
        }  
  
        //Geocode the location specified by the user  
        function Geocode() {  
            if (map != null) { map.dispose(); document.getElementById("output").innerHTML = ""; }  
            //Create Bing Maps REST Services request to geocode the address provided by the user  
            var geocodeRequest = "http://dev.virtualearth.net/REST/v1/Locations/"  
               + document.getElementById('address').value  
               + "?output=json"  
               //Set the callback function  
               + "&jsonp=GetLocationCoordinates"  
               + "&key=" + BingMapsKey;  
            //Submit the request  
            MakeServiceRequest(geocodeRequest);  
        }  
  
        //Get the geocoded latitude and longitude from the response  
        function GetLocationCoordinates(geocodeResponse) {  
  
            if (geocodeResponse &&  
                   geocodeResponse.resourceSets &&  
                   geocodeResponse.resourceSets.length > 0 &&  
                   geocodeResponse.resourceSets[0].resources &&  
                   geocodeResponse.resourceSets[0].resources.length > 0) {  
  
                Search(geocodeResponse.resourceSets[0].resources[0].point.coordinates[0], geocodeResponse.resourceSets[0].resources[0].point.coordinates[1]);  
            }  
            else {//The location could not be geocoded.  
                document.getElementById("output").innerHTML = "";  
                var output = document.getElementById("output");  
                var resultsHeader = document.createElement("h4");  
                output.appendChild(resultsHeader);  
                resultsHeader.innerHTML = "The location could not be geocoded";  
            }  
        }  
  
        // Search for Phonebook results using the Bing, Version 2.0 API  
        // and the query string provided by the user  
        function Search(lat, long) {  
            //Get the distance to search selected by the user  
            var distance = document.getElementById('distance').value;  
  
            queryString = document.getElementById('queryTerm').value;  
            if ((queryString != null)&&(queryString !="Insert search term")){  
                var requestStr = "http://api.bing.net/json.aspx?"                  
                // Common request fields (required)  
                + "AppId=" + AppId  
                + "&Query=" + queryString  
                + "&Sources=Phonebook"  
  
                // Common request fields   
                + "&Version=2.0"  
                + "&Market=en-us"  
                + "&UILanguage=en"  
                + "&Latitude=" + lat  
                + "&Longitude=" + long  
                + "&Radius=" + distance  
                + "&Options=EnableHighlighting"  
  
                // Phonebook-specific request fields (optional)  
                + "&Phonebook.Count=10"  
                + "&Phonebook.Offset=0"  
                + "&Phonebook.FileType=YP"  
                + "&Phonebook.SortBy=Distance"  
  
                // Set the JSON callback function  
                + "&JsonType=callback"  
//                + "&JsonCallback=StaticMapResults";  
                + "&JsonCallback=MapResults";  
  
                var output = document.getElementById("output");  
                //Make URL service request  
                MakeServiceRequest(requestStr);  
                }  
             else {//The query string is undefined.  
                document.getElementById("output").innerHTML = "";  
                var output = document.getElementById("output");  
                var resultsHeader = document.createElement("h4");  
                output.appendChild(resultsHeader);  
                resultsHeader.innerHTML = "Please enter a query string.";  
            }  
        }  
  
        //Show search results and display the corresponding locations  
        // on an interactive (AJAX 7) map  
        function MapResults(response) {  
            //Create list of results  
            document.getElementById("output").innerHTML = "";  
            var output = document.getElementById("output");  
            var resultsHeader = document.createElement("h4");  
            var resultsList = document.createElement("ol");  
            output.appendChild(resultsHeader);  
            output.appendChild(resultsList);  
  
            if (response.SearchResponse.Phonebook != null) {  
                //Get phonebook results  
                var results = response.SearchResponse.Phonebook.Results;  
  
                //Create pushpin collection  
                var pushpins = new Microsoft.Maps.EntityCollection();  
  
                //initialize bounds for map area  
                var minLatitude = results[0].Latitude; var maxLatitude = results[0].Latitude;  
                var minLongitude = results[0].Longitude; var maxLongitude = results[0].Longitude;  
  
                // Display the results header.  
                resultsHeader.innerHTML = "Phonebook results for "  
                     + response.SearchResponse.Query.SearchTerms;  
  
                // Display the Phonebook results.  
                var resultsListItem = null;  
                var resultStr = "";  
  
                for (var i = 0; i < results.length; ++i) {  
                    resultsListItem = document.createElement("li");  
                    resultsList.appendChild(resultsListItem);  
                    resultStr = results[i].Business  
                        + "<br />"  
                        + results[i].Address  
                        + "<br />"  
                        + results[i].City  
                        + ", "  
                        + results[i].StateOrProvince  
                        + "<br />"  
                        + results[i].PhoneNumber  
                        + "<br /><br />";  
  
                    // Replace highlighting characters with strong tags.  
                    resultsListItem.innerHTML = ReplaceHighlightingCharacters(  
                            resultStr,  
                            "<strong>",  
                            "</strong>");  
  
                    // Add pushpin to map collection  
                    var pushpinVal = (i + 1).toString();  
                     pushpins.push(new Microsoft.Maps.Pushpin(new Microsoft.Maps.Location(results[i].Latitude, results[i].Longitude), { text: pushpinVal }));  
  
                    //Determine bounds that display all pushpins  
                    if (results[i].Latitude > maxLatitude)  
                    { maxLatitude = results[i].Latitude; }  
                    else if (results[i].Latitude < minLatitude)  
                    { minLatitude = results[i].Latitude; }  
  
                    if (results[i].Longitude > maxLongitude)  
                    { maxLongitude = results[i].Longitude; }  
                    else if (results[i].Longitude < minLongitude)  
                    { minLongitude = results[i].Longitude; }  
                }  
  
                //Create map  
  
                mapDiv.style.visibility = "visible";  
                if (map != null) { map.dispose() };  
                map = new Microsoft.Maps.Map(document.getElementById("mapDiv"), { credentials: BingMapsKey, height: 400, width: 400, mapTypeId: "r" });  
  
                //Add pushpins to the map  
                map.entities.push(pushpins);  
  
                //Add padding to map area so that pushpins are not on the edge  
                minLatitude -= 0.0001;  
                maxLatitude += 0.0001;  
                minLongitude -= 0.0001;  
                maxLongitude += 0.0001;  
                var mapArea = Microsoft.Maps.LocationRect.fromLocations(new Microsoft.Maps.Location(minLatitude, minLongitude), new Microsoft.Maps.Location(maxLatitude, maxLongitude));  
                map.setView({ bounds: mapArea });  
            }  
            else { //No results were returned  
                resultsHeader.innerHTML = "No results were found for &quot;" + response.SearchResponse.Query.SearchTerms  
                       + "&quot;. Please try another search term and/or increase the search distance.";  
                resultsHeader.style.color = "DarkRed";  
                resultsHeader.style.fontFamily = "sans-serif";  
                resultsHeader.style.fontWeight = "normal";  
                if (map != null) { map.dispose(); }  
            }  
        }  
  
        function ReplaceHighlightingCharacters(text, beginStr, endStr) {  
            // Replace all occurrences of U+E000 (begin highlighting) with  
            // beginStr. Replace all occurrences of U+E001 (end highlighting)  
            // with endStr.  
            var regexBegin = new RegExp("\uE000", "g");  
            var regexEnd = new RegExp("\uE001", "g");  
  
            return text.replace(regexBegin, beginStr).replace(regexEnd, endStr);  
        }  
  
//         function StaticMapResults(response) {  
//            //Create list of results  
//            document.getElementById("output").innerHTML = "";  
//            var output = document.getElementById("output");  
//            var resultsHeader = document.createElement("h4");  
//            var resultsList = document.createElement("ol");  
//            output.appendChild(resultsHeader);  
//            output.appendChild(resultsList);  
  
//            //Create REST Static Image URL  
//            var mapURL = "http://dev.virtualearth.net/REST/v1/Imagery/Map/Road?mapVersion=v1&key=" + BingMapsKey;  
  
//            if (response.SearchResponse.Phonebook != null) {  
//                //Get phonebook results  
//                var results = response.SearchResponse.Phonebook.Results;  
  
//                //initialize bounds for map area  
//                var minLatitude = results[0].Latitude; var maxLatitude = results[0].Latitude; ;  
//                var minLongitude = results[0].Longitude; var maxLongitude = results[0].Longitude;  
//                // Display the results header.  
//                resultsHeader.innerHTML = "Phonebook results for "  
//                     + response.SearchResponse.Query.SearchTerms;  
  
//                // Display the Phonebook results.  
//                var resultsListItem = null;  
//                var resultStr = "";  
  
//                for (var i = 0; i < results.length; ++i) {  
//                    resultsListItem = document.createElement("li");  
//                    resultsList.appendChild(resultsListItem);  
//                    resultStr = results[i].Business  
//                        + "<br />"  
//                        + results[i].Address  
//                        + "<br />"  
//                        + results[i].City  
//                        + ", "  
//                        + results[i].StateOrProvince  
//                        + "<br />"  
//                        + results[i].PhoneNumber  
//                        + "<br /><br />";  
  
//                    // Replace highlighting characters with strong tags.  
//                    resultsListItem.innerHTML = ReplaceHighlightingCharacters(  
//                            resultStr,  
//                            "<strong>",  
//                            "</strong>");  
  
//                    if (results[i].Latitude > maxLatitude)  
//                    { maxLatitude = results[i].Latitude; }  
//                    else if (results[i].Latitude < minLatitude)  
//                    { minLatitude = results[i].Latitude; }  
  
//                    if (results[i].Longitude > maxLongitude)  
//                    { maxLongitude = results[i].Longitude; }  
//                    else if (results[i].Longitude < minLongitude)  
//                    { minLongitude = results[i].Longitude; }  
  
//                    mapURL = mapURL + "&pp=" + results[i].Latitude.toString() + "," + results[i].Longitude.toString() + ";;" + (i + 1).toString();  
//                }  
  
//           
//                minLatitude -= 0.0001;  
//                maxLatitude += 0.0001;  
//                minLongitude -= 0.0001;  
//                maxLongitude += 0.0001;  
  
//                mapURL = mapURL + "&mapArea=" + minLatitude.toString() + "," + minLongitude.toString() + ","  
//                                + maxLatitude.toString() + "," + maxLongitude.toString()   
//                                + "&declutter=1";  
  
//                //Create img element to hold static map  
//                var map = document.createElement("img");  
//                map.setAttribute("alt","Static Map showing Fourth Coffee Shops");  
//                map.setAttribute("style", "padding-left: 10px");  
//                map.setAttribute("src", mapURL);  
//                document.getElementById("mapDiv").appendChild(map);  
//                }  
//            else { //No results were returned  
//                resultsHeader.innerHTML = "No locations were found. Please try another location or increase the search distance."  
//                resultsHeader.style.color = "DarkRed";  
//                resultsHeader.style.fontFamily = "sans-serif";  
//                resultsHeader.style.fontWeight = "normal";  
//                map.dispose();  
//            }  
//    }  
  
    </script>  
</head>  
<body>  
<div style="color:#330000;font-size:larger;font-family:Arial,Sans-Serif">  
    <p> Search and Map Entities Near a Location </p>  
</div>  
<div style="color:#003366;font-size:large;margin-bottom:10px"><span>Search for&nbsp;</span>  
    <input id="queryTerm" type="text" value="Insert search term" size="30" />    
</div>  
<div style="color:#003366;font-size:large"><span>Search within&nbsp;</span>  
    <select id="distance">  
        <option value="1">1</option>  
        <option value="5">5</option>  
        <option value="10" selected="selected">10</option>  
        <option value="25">25</option>  
        <option value="50">50</option>  
        <option value="100">100</option>  
        <option value="200">200</option>    
        <option value="400">400</option>  
    </select><span>&nbsp;kilometers of&nbsp;</span>  
    <input id="address" type="text" value="Insert Location/Address" size="30" />    
    <input type="button" value="Search" onclick="Geocode()" />  
</div>   
<div>  
    <div id="mapDiv" style="padding-left:10px;"></div>  
    <div id="output" style="float:left;" ></div>  
</div>  
</body>  
</html>  
  
```