# Data Fields

Processed events are composed of several attributes, each of which is a data field with its own characteristics. These event schema data fields fall into the groups shown in the following sections.

Each attribute has both a **Label** that you see in the ArcSight Console and a unique **Script Alias** you use to refer to the attribute in filters, rules, or Velocity templates. The **Data Type** lets you know how to handle the attribute, and the **Default Turbo Level** indicates whether an attribute is, by default, classified as **1** (essential, or "fastest") or **2** (optional, or "faster"). Turbo Level 3 ("complete") isn't designated because it applies to additional data not represented here.

The easiest way to view all event fields is on the Event Inspector (Event tab) or Common Conditions Editor (CCE) on the Console.

To display the Event Inspector:

1. Select an event in a grid view like an active channel.
2. Right-click and choose **Show event details**.
   The event's details appear in the Event Inspector. To view *all* event fields, make sure that no field set is selected to limit the set of fields shown. Select **Clear** from the drop-down menu above the list of event fields. With no field set selected, the drop-down shows “Select a Field Set”.

> **Note:** For a list of ArcSight’s Common Event Format (CEF) abbreviations, ask your OpenText ArcSight Support representative for the tech note entitled Implementing ArcSight CEF.
