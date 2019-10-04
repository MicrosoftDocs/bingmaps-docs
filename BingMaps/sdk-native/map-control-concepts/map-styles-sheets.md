# Style Sheets

The Bing Maps SDK supports both default and custom Map Style Sheets.
A **Map Style Sheet** represents a set of rules that define the style of the map in a map view.

Via the [MapStyleSheet](../map-control-api/MapStyleSheet-class.md) static methods you can
create and combine multiple style sheets, where later sheets override settings set by earlier sheets.

## Default Map Style Sheets

The pre-built Style Sheets establish the fundamental mode that a map view will render in.
Available options are specified in [MapStyleSheets](../map-control-api/MapStyleSheets-class.md):

| Style Sheet                 | Description |
| ----------------------------| ----------- |
| Empty                       | A map style with an empty canvas. Useful if you want to display a custom set of tiles with no underlying map data. |
| Aerial                      | A photorealistic map style with no markup. |
| AerialWithOverlay           | A photorealistic map style with labels, roads, and borders. |
| RoadDark                    | A road map style with a dark theme. |
| RoadLight                   | A road map style with a light theme. |
| RoadCanvasLight             | A road map style with a low-contrast light theme (some details such as hill shading disabled). |
| RoadHighContrastDark        | A road map style with a high-contrast dark theme. |
| RoadHighContrastLight       | A road map style with a high-contrast light theme. |

## Custom Map Style Sheets

You can create your own **Map Style Sheet** by writing custom JSON that overrides the default settings.
Usually a default base map style is combined with custom JSON to change the appearance of the map.

The style sheet JSON API is described [here](https://docs.microsoft.com/windows/uwp/maps-and-location/elements-of-map-style-sheet).
The style sheet JSON can also be created interactively using the [Map Style Sheet Editor](https://www.microsoft.com/p/map-style-sheet-editor/9nbhtcjt72ft).

# Changing the appearance of the map

See some examples for [How to change the appearance of the map](change-map-appearance.md).

_See also_:
* [MapStyleSheet](../map-control-api/MapStyleSheet-class.md)
* [Map Style Sheet JSON API](https://docs.microsoft.com/windows/uwp/maps-and-location/elements-of-map-style-sheet)
* [Map Style Sheet Editor](https://www.microsoft.com/p/map-style-sheet-editor/9nbhtcjt72ft)
