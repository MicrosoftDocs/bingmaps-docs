---
title: "Default Autosuggest User Interface Example | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 5ab2c255-5fc7-4d1b-bfc4-d20afd5d097b
caps.latest.revision: 4
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Default Autosuggest User Interface Example
The following code example shows how to add the default autosuggest functionality to a textbox. To do this you first need to define a DIV element where the suggestions will be rendered as well as a textbox where the user will be typing their query. After that, you need to load the autosuggest module, and attach an instance of the AutosuggestManager to the suggestions div and textbox. You will also need to specify a callback handler that will be called when the user selects a suggestion.  When running this sample and typing in the textbox, suggestions will be displayed. If you select a suggestion, the pushpin will be displayed and a map centered over the location.

```
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
    <script type='text/javascript'
            src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap' 
            async defer></script>
    <script type='text/javascript'>
    var map;

    function GetMap() {
        map = new Microsoft.Maps.Map('#myMap', {
            credentials: 'Your Bing Maps Key'
        });

        Microsoft.Maps.loadModule('Microsoft.Maps.AutoSuggest', function () {
            var manager = new Microsoft.Maps.AutosuggestManager({ map: map });
            manager.attachAutosuggest('#searchBox', '#searchBoxContainer', selectedSuggestion);
        });
    }

    function selectedSuggestion(result) {
        //Remove previously selected suggestions from the map.
        map.entities.clear();

        //Show the suggestion as a pushpin and center map over it.
        var pin = new Microsoft.Maps.Pushpin(result.location);
        map.entities.push(pin);
        map.setView({ bounds: result.bestView });
    }
    </script>
</head>
<body>
    <div id='searchBoxContainer'>
        <input type='text' id='searchBox'/>
    </div>

    <div id="myMap" style="position:relative;width:400px;height:300px;"></div>
</body>
</html>
```

Here is what the autosuggest UI looks like when typing in the letters “Se”. If you select a suggestion, you will see it displayed on the map. Note that the suggestions you receive may be different as both the map view and your location are being used to influence the suggestions.
  
![Default Autosuggest Dropdown](../v8-web-control/media/bmv8-autosuggestexample.png)

[Try it now](http://www.bing.com/api/maps/sdk/mapcontrol/isdk#autoSuggestUi+JS)