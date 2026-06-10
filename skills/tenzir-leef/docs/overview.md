# LEEF overview

The Log Event Extended Format (LEEF) is a customized event format for IBM® Security QRadar®.

Any vendor can use this documentation to generate LEEF events.

QRadar can integrate, identify, and process LEEF events. LEEF events must use UTF-8 character encoding.

You can send events in LEEF output to QRadar by using the following protocols:

- Syslog
- File import with the Log File Protocol

> **Important:** Before QRadar can use LEEF events, you must complete Universal LEEF configuration tasks. For more information about configuring the log file protocol to collect Universal LEEF events, see the *DSM Configuration Guide*.

The method that you select to provide LEEF events determines whether the events can be automatically discovered in QRadar. When events are automatically discovered the level of manual configuration that is needed in QRadar is reduced.

As LEEF events are received, QRadar analyzes the event traffic in an attempt to identify the device or appliance. This process is referred to as *traffic analysis*. It typically takes at least 25 LEEF events to identify and create a new log source in QRadar. Until traffic analysis identifies the event source, the initial 25 events are categorized as *SIM Generic Log DSM* events and the event name is set as *Unknown Log Event*. After the event traffic is identified, QRadar creates a log source to properly categorize and label any events that are forwarded from your appliance or software. Events that are sent from your device are viewable in QRadar on the Log Activity tab.

> **Important:** When a log source cannot be identified after 1,000 events, QRadar creates a system notification and removes the log source from the traffic analysis queue. QRadar is still capable of collecting the events, but a user must intervene and create a log source manually to identify the event type.
