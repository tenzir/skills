# Appendix A: Date Formats

CEF supports several variations on time and date formats to accurately identify the time an event occurred. These formats are as follows:

- Milliseconds since January 1, 1970 (integer).
  This time format supplies an integer with the count in milliseconds from January 1, 1970 to the time the event occurred.
- MMM dd HH:mm:ss.SSS zzz
- MMM dd HH:mm:sss.SSS
- MMM dd HH:mm:ss zzz
- MMM dd HH:mm:ss
- MMM dd yyyy HH:mm:ss.SSS zzz
- MMM dd yyyy HH:mm:ss.SSS
- MMM dd yyyy HH:mm:ss zzz
- MMM dd yyyy HH:mm:ss

For a key to the date formats shown above, refer to the [SimpleDateFormat](http://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html) page from the API specification for the Java™ Platform, Standard Edition document.
