# SecurityResult.Action

Enum representing different possible actions taken by the product that created the event. Google SecOps classifies: - ALLOW and ALLOW_WITH_MODIFICATION actions as "successful". - BLOCK, QUARANTINE, FAIL, and CHALLENGE actions as "failed". This includes all corresponding metrics (for example, AUTH_ATTEMPTS_FAIL, FILE_EXECUTIONS_FAIL, RESOURCE_READ_FAIL, and so on). - UNKNOWN_ACTION actions as neither "successful" nor "failed", because, for example, logs might not provide information whether a login event occurred but some kind of "unknown" error was issued nonetheless.

## Values

0. `UNKNOWN_ACTION`: The default action.
1. `ALLOW`: Allowed.
2. `BLOCK`: Blocked.
3. `ALLOW_WITH_MODIFICATION`: Strip, modify something (e.g. File or email was disinfected or rewritten and still forwarded).
4. `QUARANTINE`: Put somewhere for later analysis (does NOT imply block).
5. `FAIL`: Failed (e.g. the event was allowed but failed).
6. `CHALLENGE`: Challenged (e.g. the user was challenged by a Captcha, 2FA).
