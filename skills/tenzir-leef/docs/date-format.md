# Custom event date format

To create a customized event format, your device must supply the raw date format by using the `devTime` event attribute in the payload of the event.

Use the `devTimeformat` to format the `devTime` event attribute to display the event in IBM® Security QRadar®. The suggested `devTimeFormat` patterns are listed in the following table:

*Table 1. devTimeFormat suggested patterns*

| devTimeFormat Pattern | Result |
| --- | --- |
| devTimeFormat=MMM dd yyyy HH:mm:ss | Jun 06 2015 16:07:36 |
| devTimeFormat=MMM dd yyyy HH:mm:ss.SSS | Jun 06 2015 16:07:36.300 |
| devTimeFormat=MMM dd yyyy HH:mm:ss.SSS z | Jun 06 2015 02:07:36.300 GMT |

For more information about specifying a date format, see the SimpleDateFormat information on the [Java Web Page](http://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html)(http://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html).
