# SecurityResult.Action

Enum representing different possible actions taken by the product that created the event. Google SecOps classifies: - ALLOW and ALLOW_WITH_MODIFICATION actions as "successful". - BLOCK, QUARANTINE, FAIL, and CHALLENGE actions as "failed". This includes all corresponding metrics (for example, AUTH_ATTEMPTS_FAIL, FILE_EXECUTIONS_FAIL, RESOURCE_READ_FAIL, and so on). - UNKNOWN_ACTION actions as neither "successful" nor "failed", because, for example, logs might not provide information whether a login event occurred but some kind of "unknown" error was issued nonetheless.

- **Full name**: `google.backstory.SecurityResult.Action`
- **Values**: `7`

## Values

### `UNKNOWN_ACTION`

- **Number**: `0`

The default action.

### `ALLOW`

- **Number**: `1`

Allowed.

### `BLOCK`

- **Number**: `2`

Blocked.

### `ALLOW_WITH_MODIFICATION`

- **Number**: `3`

Strip, modify something (e.g. File or email was disinfected or rewritten and still forwarded).

### `QUARANTINE`

- **Number**: `4`

Put somewhere for later analysis (does NOT imply block).

### `FAIL`

- **Number**: `5`

Failed (e.g. the event was allowed but failed).

### `CHALLENGE`

- **Number**: `6`

Challenged (e.g. the user was challenged by a Captcha, 2FA).
