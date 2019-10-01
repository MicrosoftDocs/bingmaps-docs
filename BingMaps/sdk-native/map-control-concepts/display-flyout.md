
# Display flyout of pushpin

A Flyout is a simple panel that displays information over a map, often when an associated [MapIcon](../map-control-api/MapIcon-class.md) is tapped.

## Examples

### Assigning flyout to pushpin

The following example shows how to set the flyout of a pushpin with a title.

**Java**
>```java
> MapFlyout flyout = new MapFlyout();
> flyout.setTitle("Flyout");
> flyout.setDescription("Sample description");
> icon.setFlyout(flyout);
>```

**Swift**
> ```swift
> let flyout = MSMapFlyout.flyout()
>flyout.title = "Flyout"
>flyout.description = "Sample description"
> icon.flyout = flyout
> ```

**Objective-C**
> ```objectivec
>MSMapFlyout *flyout = [MSMapFlyout flyout];
>flyout.title = @"Flyout";
>flyout.description = @"Sample description";
>icon.flyout = flyout;
> ```
