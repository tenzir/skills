# Authentication.Mechanism

Mechanism(s) used to authenticate.

## Values

0. `MECHANISM_UNSPECIFIED`: The default mechanism.
1. `USERNAME_PASSWORD`: Username + password authentication.
2. `OTP`: OTP authentication.
3. `HARDWARE_KEY`: Hardware key authentication.
4. `LOCAL`: Local authentication.
5. `REMOTE`: Remote authentication.
6. `REMOTE_INTERACTIVE`: RDP, Terminal Services, or VNC.
7. `MECHANISM_OTHER`: Some other mechanism that is not defined here.
8. `BADGE_READER`: Badge reader authentication
9. `NETWORK`: Network authentication.
10. `BATCH`: Batch authentication.
11. `SERVICE`: Service authentication
12. `UNLOCK`: Direct human-interactive unlock authentication.
13. `NETWORK_CLEAR_TEXT`: Network clear text authentication.
14. `NEW_CREDENTIALS`: Authentication with new credentials.
15. `INTERACTIVE`: Interactive authentication.
16. `CACHED_INTERACTIVE`: Interactive authentication using cached credentials.
17. `CACHED_REMOTE_INTERACTIVE`: Cached Remote Interactive authentication using cached credentials.
18. `CACHED_UNLOCK`: Cached Remote Interactive authentication using cached credentials.
19. `BIOMETRIC`: Biometric device such as a fingerprint reader.
20. `WEARABLE`: Wearable such as an Apple Watch.
