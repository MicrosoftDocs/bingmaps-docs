---
title: "Display flyout of icon | Microsoft Docs"
author: "pablocan"
---

# Display flyout of icon

A Flyout is a simple panel that displays information over a map, often when an associated [MapIcon](../map-control-api/MapIcon-class.md) is tapped.  
Flyouts are represented by [MapFlyout class](../map-control-api/mapflyout-class.md).

## Examples

### Creating and displaying a default flyout

The following example shows how to create a flyout with title and description, and set it to an existing map icon. When
user taps an icon that has a flyout attached, flyout will be shown.  
Flyouts are light-dismissable by default, meaning they can be hidden by tapping elsewhere. This behavior is controlled by
[LightDismissEnabled property](../map-control-api/mapflyout-class.md#lightdismissenabled).

**Java**

>```java
> MapFlyout flyout = new MapFlyout();
> flyout.setTitle("Test");
> flyout.setDescription("Sample description");
> icon.setFlyout(flyout);
>```

**Swift**

>```swift
> let flyout = MSMapFlyout()
> flyout.title = "Test"
> flyout.description = "Sample description"
> icon.flyout = flyout
>```

**Objective-C**

>```objectivec
> MSMapFlyout *flyout = [MSMapFlyout flyout];
> flyout.title = @"Test";
> flyout.description = @"Sample description";
> icon.flyout = flyout;
>```


### Creating and displaying a custom flyout

Flyouts also support custom views through [MapFlyoutCustomViewAdapter interface](../map-control-api/mapflyoutcustomviewadapter-interface.md).

***Important: View will be rendered on canvas, with interactive elements no longer interactive.***

**Java**

>```java
> MapFlyout flyout = new MapFlyout();
> flyout.setCustomViewAdapter(new MapFlyout.CustomViewAdapter() {
>     @Override
>     public View getFlyoutView(MapElement mapElement){
>         if (mapElement instanceof MapIcon)
>         {
>             MapIcon icon = (MapIcon)mapElement;
>             // Retrieve title info and custom info stored in the Tag property.
>             return new MyCustomFlyoutView(icon.getTitle(), icon.getTag());
>         }
>         return null;
>     }
> });
> icon.setFlyout(flyout);
>```

**Swift**

>```swift
> let flyout = MSMapFlyout()
> flyout.customViewAdapter = { (mapElement: MSMapElement) -> UIView? in
>     if mapElement is MSMapIcon {
>         let icon = mapElement as! MSMapIcon
>         // Retrieve title info and custom info stored in the Tag property.
>         return MyCustomFlyoutView(icon.title, icon.tag)
>     }
>     return nil
> }
> icon.flyout = flyout
>```


### Showing and hiding flyouts manually

Let's say you want to disable the default light dismiss behavior for flyouts. The following example shows how to hide all your flyouts at
once, assuming that `pinLayer` variable is the map element layer with your map icons.

**Java**

>```java
> for (MapElement element : pinLayer.getElements()) {
>     if (element instanceof MapIcon) {
>         MapFlyout flyout = ((MapIcon)element).getFlyout();
>         if (flyout != null) {
>             flyout.hide();
>         }
>     }
> }
>```

**Swift**

>```swift
> for element in pinLayer.elements {
>     let icon = element as? MSMapIcon
>     icon?.flyout?.hide()
> }
>```

_Note: to be able to iterate through `Elements` property of `MapElementLayer` in Swift, you will need to add
[Sequence extension for MSMapElementCollection](../map-control-api/MapElementCollection-class.md#sequence-protocol-in-swift)._

**Objective-C**
>```objectivec
> for (MSMapElement *element in pinLayer.elements) {
>     if ([element isKindOfClass:[MSMapIcon class]]) {
>         MSMapIcon *icon = (MSMapIcon *)element;
>         if (icon.flyout != nil) {
>             [icon.flyout hide];
>         }
>     }
> }
>```


## See also:

* [MapFlyout](../map-control-api/mapflyout-class.md)
* [MapFlyoutCustomViewAdapter](../map-control-api/mapflyoutcustomviewadapter-interface.md)
* [Icons](map-icons.md)
* [MapIcon](../map-control-api/mapicon-class.md)
