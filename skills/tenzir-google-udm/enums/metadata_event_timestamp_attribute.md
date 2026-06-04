# Metadata.EventTimestampAttribute

Enum representing the type of timestamp that the event_timestamp field represents.

## Values

0. `EVENT_TIMESTAMP_ATTRIBUTE_UNSPECIFIED`: Default event timestamp attribute.
1. `FILE_LAST_ACCESS_TIME` (deprecated): Deprecated. Use LAST_ACCESSED instead.
2. `FILE_LAST_MODIFIED_TIME` (deprecated): Deprecated. Use LAST_MODIFIED instead.
3. `FILE_METADATA_LAST_CHANGE_TIME` (deprecated): Deprecated. Use METADATA_LAST_CHANGED instead.
4. `FILE_CREATION_TIME` (deprecated): Deprecated. Use CREATED instead.
5. `COLLECTED_TIME` (deprecated): Deprecated. Use COLLECTED instead.
6. `COLLECTED`: The time when the event was collected by the vendor's local collection infrastructure.
7. `ACCESSED`: The time when the file was accessed.
8. `CHANGED`: The time when the file was changed.
9. `CREATED`: The time when the file was first created.
10. `FILE_NAME_ACCESSED`: The time when the file name was accessed.
11. `FILE_NAME_CHANGED`: The time when the file name was changed.
12. `FILE_NAME_CREATED`: The time when the file name was created.
13. `FILE_NAME_LAST_ACCESSED`: The time when the file name was last accessed.
14. `FILE_NAME_LAST_MODIFIED`: The time when the file name was last modified.
15. `FILE_NAME_METADATA_LAST_CHANGED`: The time when the file name metadata was last changed.
16. `FILE_NAME_MODIFIED`: The time when the file name was modified.
17. `LAST_ACCESSED`: The time when the file was last accessed.
18. `LAST_MODIFIED`: The time when the file was last modified.
19. `METADATA_LAST_CHANGED`: The time when the file metadata was last changed.
20. `MODIFIED`: The time when the file was modified.
21. `ADDED`: Added Timestamp.
22. `BACKED_UP`: Backed Up Timestamp.
23. `LAST_CONNECTED`: Last Connected timestamp.
24. `DELETED`: Deleted Timestamp.
25. `ENDED`: Ended Timestamp.
26. `EXITED`: Exited Timestamp.
27. `EXPIRED`: Expired Timestamp.
28. `FIRST_ACCESSED`: First Accessed Timestamp.
29. `APPEARED`: Appeared Timestamp.
30. `INSTALLED`: Installed Timestamp.
31. `LAST_ACTIVE`: Last Active Timestamp.
32. `LAST_LOGGED_IN`: Last Login Timestamp.
33. `LAST_LOGIN_ATTEMPT`: Last Login Attempt Timestamp.
34. `LAST_PASSWORD_SET`: Last Password Set Timestamp.
35. `LAST_PRINTED`: Last Printed Timestamp.
36. `LAST_RESUMED`: Last Resumed Timestamp.
37. `LAST_EXECUTED`: Last Executed Timestamp.
38. `LAST_SEEN`: Last Seen Timestamp.
39. `LAST_SHUTDOWN`: Last Shutdown Timestamp.
40. `LAST_UPDATED`: Last Updated Timestamp.
41. `LAST_USED`: Last Used Timestamp.
42. `LAST_VISITED`: Last Visited Timestamp.
43. `LINKED`: Linked Timestamp.
44. `METADATA_MODIFIED`: Metadata Modified Timestamp.
45. `CONTENT_MODIFIED`: Modified Timestamp.
46. `PURCHASED`: Purchased Timestamp.
47. `RECORDED`: Recorded Timestamp.
48. `REQUEST_RECEIVED`: Request Received Timestamp.
49. `RESPONSE_SENT`: Response Sent Timestamp.
50. `SCHEDULED_TO_END`: Scheduled to End Timestamp.
51. `SCHEDULED_TO_START`: Scheduled to Start Timestamp.
52. `SENT`: Sent Timestamp.
53. `STARTED`: Started Timestamp.
54. `UPDATED`: Updated Timestamp.
55. `VALIDATED`: Validated Timestamp.
56. `MOST_RECENT_RUN`: Most Recent Run Timestamp.
57. `NEXT_RUN`: Next Run Timestamp.
58. `VISITED`: Visited Timestamp.
59. `TARGET_CREATED`: Target Created Timestamp.
60. `VOLUME_CREATED`: Volume Created Timestamp.
61. `POST_CHECKED`: Post Checked Timestamp.
62. `SYNCHRONIZED`: Synchronized Timestamp.
63. `ITEM_CREATED`: Item Created Timestamp.
64. `ITEM_MODIFIED`: Item Modified Timestamp.
65. `DOCUMENT_LAST_SAVED`: Document Last Saved Timestamp.
66. `LAST_REGISTERED`: Last Registered Timestamp.
67. `LAUNCHED`: Launched Timestamp.
68. `FIRST_VISITED`: First Visited Timestamp.
69. `FIRST_SEEN`: First Seen Timestamp.
70. `DOWNLOADED`: Downloaded Timestamp.
