---
title: "Creating Custom Modules | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 2abfbb67-4a51-4f13-b62d-fa5c7b60307b
caps.latest.revision: 4
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# Creating Custom Modules

The Bing Maps Modular framework allows you to create reusable blocks of code that tie into Bing Maps. This saves on development time and is a great way to improve code quality by re-using proven and tested modules.  

The basic overview of how to create a module:

1.	Create a single JavaScript file that contains all the code for your module. 
2.	Add a call to the Bing Maps `moduleLoaded` event to the end of the JavaScript file containing the code for your module, passing in the name of your module. For example:

`Microsoft.Maps.moduleLoaded('MyModule');`

3.	Register your module by adding a reference to where your modular plugin JavaScript file is located. This is often done right after the map is loaded. For example:

`Microsoft.Maps.registerModule('MyModule', 'http://example.com/MyModule.js');`

4.	Load your module by calling the `loadModule` method in Bing Maps and passing in a callback method that will be fired when the module has been loaded. For example:

`Microsoft.Maps.loadModule('MyModule', myModuleLoaded);`

## Example

The following example shows a common way of structuring a custom module. 

```javascript
var MyModule = function (map) {
    var localVariable = "";

    //Constructor
    function init() {

    }

    //Private Method
    function _doSomething() {
    }

    //Public method
    this.DoSomething = function () {
    };

    init();
};

//Call the Module Loaded method.
Microsoft.Maps.moduleLoaded('MyModule');
```

If this module was stored saved in a folder called js and a file called MyModule.js, the following code can register and load it.

```html
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
	<script type="text/javascript">
        var map;

        function GetMap() {
            map = new Microsoft.Maps.Map('#myMap', {
                credentials: ‘Your Bing Maps Key’
            });
            
            //Register code to our Custom Module
            Microsoft.Maps.registerModule('MyModule', 'js/MyModule.js');

            //Load the arrow module
            Microsoft.Maps.loadModule('MyModule', function(){
                //MyModule is loaded. Do post load tasks here.
            });
        }
    </script>
    <script type='text/javascript' src='http://www.bing.com/api/maps/mapcontrol?callback=GetMap' async defer></script>
</head>
<body>
    <div id="myMap" style="position:relative;width:600px;height:400px;"></div>
</body>
</html>
```

**_Tip_**: The Bing Maps V7 SDK also supported custom modules. Several developers created useful modules and made them available through the [Bing Maps V7 Module project](https://bingmapsv7modules.codeplex.com/) on CodePlex. This is a great place to see how other custom modules have been created.  
