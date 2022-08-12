---
title: "Filter Example | Microsoft Docs"
description: An example that shows how to use the execute and toString functions of the Filter and FilterGroup classes.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: d495790b-29f9-48ae-b805-cea3b426068b
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Filter Example

This example shows how to use the `execute` and `toString` functions of the [Filter](../../modules/spatial-data-service-module/filter-class.md) and [FilterGroup](../../modules/spatial-data-service-module/filtergroup-class.md) classes by performing a bunch of tests. The output of the `toString` functions are compared against their expected values. The `execute` functions are tested against an arbitrary JSON object that has the following structure. 

```javascript
var myJsonObject = {
    id: 1,
    title: 'My Object',
    properties: {
        updated: Date.Now,
        value: 5.5
    }
};
```

This example loads the Spatial Data Services module on its own as a map isn't required to use this module.


```html
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />

    <script type='text/javascript'
            src='http://www.bing.com/api/maps/mapcontrol?callback=RunTests'
            async defer></script>

    <script type='text/javascript'>
        var sds;

        function RunTests() {
            //Load the Bing Spatial Data Services module.
            Microsoft.Maps.loadModule('Microsoft.Maps.SpatialDataService', function () {
                //Create local variable for Spatial Data Services namespace to reduce the amount of typing needed.
                sds = Microsoft.Maps.SpatialDataService;

                sdsFilterTest();
                testFilters();
            });
        }

        function sdsFilterTest() {
            //This test creates a bunch of filters and verifies that the output of the toString function is a valid SDS filter string.
            
            //Create a filter that checks that the 'Locality' property starts with 'Sea'.
            var f1 = new sds.Filter("Locality", sds.FilterCompareOperator.startsWith, "Sea");

            //Create a filter that checks that the 'HasWifi' property equals true.
            var f2 = new sds.Filter("HasWifi", sds.FilterCompareOperator.equals, true);

            //Create a filter that checks that the 'Created' property greater or equal than Oct 29th, 2015.
            var f3 = new sds.Filter("Created", sds.FilterCompareOperator.greaterThanOrEqual, new Date(Date.parse("Thu, 29 Oct 2015 21:25:09 GMT")));

            //Create a filter that checks that the 'CountryRegion' property equals 'US'.
            var f4 = new sds.Filter("CountryRegion", sds.FilterCompareOperator.equals, "US");

            //Create a filter that checks that the 'entityId' property is in the array ['-22067', '-7891'].
            var f5 = new sds.Filter("entityId", sds.FilterCompareOperator.isIn, ['-22067', '-7891']);

            //Create a filter group where filters 1,2, and 3 all must be met.
            var fg1 = new sds.FilterGroup([f1, f2, f3], sds.FilterLogicalOperator.and);

            //Create a filter group where the first filter group or filters 4 or 5 are met.
            var fg2 = new sds.FilterGroup([fg1, f4, f5], sds.FilterLogicalOperator.or);

            //Create a filter group that checks that the fifth filter is not met.
            var fg3 = new sds.FilterGroup([f5], sds.FilterLogicalOperator.and, true);

            var output = ['toString Tests:<br/>'];

            output.push("Test 1: " + ((f1.toString() == "startsWith(Locality,'Sea')%20eq%20true") ? "Passed" : "Failed"));
            output.push("Test 2: " + ((f2.toString() == "HasWifi%20eq%20true") ? "Passed" : "Failed"));
            output.push("Test 3: " + ((f3.toString() == "Created%20ge%20datetime'2015-10-29T21:25:09Z'") ? "Passed" : "Failed"));
            output.push("Test 4: " + ((f4.toString() == "CountryRegion%20eq%20'US'") ? "Passed" : "Failed"));
            output.push("Test 5: " + ((f5.toString() == "entityId%20in('-22067','-7891')") ? "Passed" : "Failed"));
            output.push("Test 6: " + ((fg1.toString() == "(startsWith(Locality,'Sea')%20eq%20true%20and%20HasWifi%20eq%20true%20and%20Created%20ge%20datetime'2015-10-29T21:25:09Z')") ? "Passed" : "Failed"));
            output.push("Test 7: " + ((fg2.toString() == "((startsWith(Locality,'Sea')%20eq%20true%20and%20HasWifi%20eq%20true%20and%20Created%20ge%20datetime'2015-10-29T21:25:09Z')%20or%20CountryRegion%20eq%20'US'%20or%20entityId%20in('-22067','-7891'))") ? "Passed" : "Failed"));
            output.push("Test 8: " + ((fg3.toString() == "not (entityId%20in('-22067','-7891'))") ? "Passed" : "Failed"));

            document.getElementById('output').innerHTML = output.join('<br/>');
        }

        function testFilters() {
            //This test creates a bunch of filters and runs the execute function against a test JSON object.

            var myJsonObject = {
                id: 1,
                title: 'My Object',
                properties: {
                    value: 5.5
                }
            };

            //Check that the 'id' property of the JSON object is in the array [5, 7, 1].
            var idFilter = new sds.Filter('id', sds.FilterCompareOperator.isIn, [5, 7, 1]);

            //Check that the 'title' property of the JSON object starts with 'My'.
            var startsWithFilter = new sds.Filter('title', sds.FilterCompareOperator.startsWith, 'My');

            //Check that the 'properties.value' propery of the JSON object is greater than 3. 
            var valueFilter = new sds.Filter('properties.value', sds.FilterCompareOperator.greaterThan, 3);

            //Check that the JSON object passes all of the other filter tests.
            var filterGroup = new sds.FilterGroup([idFilter, startsWithFilter, valueFilter], sds.FilterLogicalOperator.and);

            var output = ['<br/><br/>execute Tests:<br/>'];

            output.push("Id Filter Test: " + idFilter.execute(myJsonObject));
            output.push("StartsWith Filter Test: " + startsWithFilter.execute(myJsonObject));
            output.push("Value Filter Test: " + valueFilter.execute(myJsonObject));

            output.push("Filter Group Test: " + filterGroup.execute(myJsonObject));

            document.getElementById('output').innerHTML += output.join('<br/>');
        }
    </script>
</head>
<body>
    <div id="output"></div>
</body>
</html>
```

Running this code will display a line of text for each test and either the word “passed” or “true” if the filter logic performed as expected.

![BMV8_FilterExample](../../media/bmv8-filterexample.PNG)