# Best practices Guidelines for LEEF events

LEEF is flexible and can create custom key value pairs for events, but you must follow some best practices to avoid potential parsing issues.

Items that are marked `Allowed` can be included in a key or value, and is not in violation of LEEF but these items are not good practice when you create custom event keys.

The following list contains custom key and value general guidelines:

- Use alphanumeric (A-Z, a-z, and 0-9) characters, but avoid tab, pipe, or caret delimiters in your event payload keys and values (key=value).
  - `Correct` - usrName=Joe.Smith
  - `Incorrect` - usrName=Joe\<tab>Smith

- Contain a single word for the key attribute (key=value).
  - `Correct` - file name=pic07720.gif
  - `Allowed` - file name=pic07720.gif
  - `Allowed` - file name =pic07720.gif

- A user-defined key cannot use the same name as a LEEF predefined key. For more information, see [Predefined LEEF event attributes](../attributes.yaml).
- Key values must be human readable, if possible, to help you to investigate event payloads.
  - `Correct` - deviceProcessHash=value
  - `Correct` - malwarename=value
  - `Allowed` - EBFDFBE14D4=value
