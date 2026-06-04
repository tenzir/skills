# Action

Enum representing different possible actions taken by the product that created the event. Google SecOps classifies: - ALLOW and ALLOW_WITH_MODIFICATION actions as "successful". - BLOCK, QUARANTINE, FAIL, and CHALLENGE actions as "failed". This includes all corresponding metrics (for example, AUTH_ATTEMPTS_FAIL, FILE_EXECUTIONS_FAIL, RESOURCE_READ_FAIL, and so on). - UNKNOWN_ACTION actions as neither "successful" nor "failed", because, for example, logs might not provide information whether a login event occurred but some kind of "unknown" error was issued nonetheless.

## Values

- `UNKNOWN_ACTION` (0): The default action.
- `ALLOW` (1): Allowed.
- `BLOCK` (2): Blocked.
- `ALLOW_WITH_MODIFICATION` (3): Strip, modify something (e.g. File or email was disinfected or rewritten and still forwarded).
- `QUARANTINE` (4): Put somewhere for later analysis (does NOT imply block).
- `FAIL` (5): Failed (e.g. the event was allowed but failed).
- `CHALLENGE` (6): Challenged (e.g. the user was challenged by a Captcha, 2FA).
