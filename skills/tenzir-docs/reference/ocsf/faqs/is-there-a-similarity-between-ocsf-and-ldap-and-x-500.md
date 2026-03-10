# Is there a similarity between OCSF and LDAP (and X.500)?

> OCSF FAQ: Is there a similarity between OCSF and LDAP (and X.500)?


Yes there is, although OCSF is considerably simpler. At a fundamental level LDAP consists of attributes and object classes, while OCSF consists of attributes and event classes. Attributes in LDAP have syntaxes and in OCSF have data types (OCSF objects are complex data types). An event class is similar to an LDAP structural object class; it defines the basic structure of an event, as the LDAP object class defines the structure of an entry. Like LDAP, an OCSF event class can be constructed via extending a super class to inherit attributes. And an OCSF profile is similar to an LDAP auxiliary class which can be applied to a structural object class so that an entry can mix in additional attributes, independent of structural hierarchy of the entry.