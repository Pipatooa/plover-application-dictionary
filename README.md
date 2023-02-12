# Plover Application Dictionary
Plover dictionary entries based on the current focussed application.

This plugin has two dictionary types `.ad` and `.mad`, for defining single or multiple application dictionaries 
respectively. The first is not readonly, allowing for entries to be added through Plover, but `.mad` dictionaries are
readonly. Both have to be edited to change which applications the entries within the dictionary 

## Installation:

Navigate to the installation directory for Plover and open a terminal / command prompt.

> Run: `<exe_name> -s plover_plugins install -e plover-application-dictionary`

Restart Plover.

## Dictionaries:

Dictionaries can match applications using three properties, `app`, `class` and `title`. `title` *should* be consistent
between platforms, whereas `class` and `app` will depend across platforms and specific user installations. To find an
application's `app` or `class`, see [meta actions](#meta-actions). `class` is only available on some Linux systems.

Matching supports full Regex. An empty string will match anything.

> **Note:** The plugin only checks the currently focussed window every 0.25 seconds, so translations made quickly after
> switching windows may be inaccurate.

The following is an example dictionary which only activates when Discord or Firefox is active. Implementation from
system to system may vary.

#### Example.ad:
```json
{
  "app": "",
  "class": "discord|Navigator",
  "title": "",
  "entries": {
    ...
  }
}
```

The following is an example dictionary which defines separate entries depending on the user being messaged on Discord.

#### Example.mad:
```json
[
  {
    "app": "",
    "class": "discord",
    "title": "@User1 - Discord",
    "entries": {
      ...
    }
  },
  {
    "app": "",
    "class": "discord",
    "title": "@User2 - Discord",
    "entries": {
      ...
    }
  }
]
```

## Meta Actions:

The `{:application_name}` meta outputs information about the currently active window. Argument can be `app`, `class` or 
`title`, or a combination of them with `:` as a separator. When a property is unknown `UNKNOWN` will be output.

The following example will output `UNKNOWN:Navigator:Mozilla Firefox` (output will vary between platforms and installations). 

#### Example:
```json
{
  "W*EUPB": "{:application_name:app:class:title}"
}
```
