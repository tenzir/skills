# Authentication.Mechanism

Mechanism(s) used to authenticate.

## Values

- `MECHANISM_UNSPECIFIED` (0): The default mechanism.
- `USERNAME_PASSWORD` (1): Username + password authentication.
- `OTP` (2): OTP authentication.
- `HARDWARE_KEY` (3): Hardware key authentication.
- `LOCAL` (4): Local authentication.
- `REMOTE` (5): Remote authentication.
- `REMOTE_INTERACTIVE` (6): RDP, Terminal Services, or VNC.
- `MECHANISM_OTHER` (7): Some other mechanism that is not defined here.
- `BADGE_READER` (8): Badge reader authentication
- `NETWORK` (9): Network authentication.
- `BATCH` (10): Batch authentication.
- `SERVICE` (11): Service authentication
- `UNLOCK` (12): Direct human-interactive unlock authentication.
- `NETWORK_CLEAR_TEXT` (13): Network clear text authentication.
- `NEW_CREDENTIALS` (14): Authentication with new credentials.
- `INTERACTIVE` (15): Interactive authentication.
- `CACHED_INTERACTIVE` (16): Interactive authentication using cached credentials.
- `CACHED_REMOTE_INTERACTIVE` (17): Cached Remote Interactive authentication using cached credentials.
- `CACHED_UNLOCK` (18): Cached Remote Interactive authentication using cached credentials.
- `BIOMETRIC` (19): Biometric device such as a fingerprint reader.
- `WEARABLE` (20): Wearable such as an Apple Watch.
