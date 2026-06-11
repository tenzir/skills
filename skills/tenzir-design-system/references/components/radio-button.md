# Radio Button

Circular selection control for single choice from multiple options.

## Props

| Prop      | Values                                  |
| --------- | --------------------------------------- |
| `state`   | `default`, `hover`, `focus`, `disabled` |
| `checked` | `true`, `false`                         |

## Size Specifications

| Property      | Value              |
| ------------- | ------------------ |
| Size          | 16px               |
| Border radius | 10px (full circle) |
| Border width  | 1px                |

## Unchecked State Specifications

| State    | Background              | Border                  | Ring                        |
| -------- | ----------------------- | ----------------------- | --------------------------- |
| Default  | `neutral-50` (#fdfdfe)  | `neutral-300` (#ced3de) | none                        |
| Hover    | `neutral-100` (#f7f8fa) | `neutral-300` (#ced3de) | none                        |
| Focus    | `neutral-50` (#fdfdfe)  | `neutral-300` (#ced3de) | 2px `primary-200` (#e0eaff) |
| Disabled | `neutral-100` (#f7f8fa) | `neutral-250` (#e3e6ed) | none                        |

## Checked State Specifications

| State    | Background              | Border                      | Ring | Indicator              |
| -------- | ----------------------- | --------------------------- | ---- | ---------------------- |
| Default  | `primary-500` (#0a54ff) | none                        | none | `neutral-50` (#fdfdfe) |
| Hover    | `primary-600` (#0043e0) | none                        | none | `neutral-50` (#fdfdfe) |
| Focus    | `primary-500` (#0a54ff) | 2px `primary-300` (#adc6ff) | none | `neutral-50` (#fdfdfe) |
| Disabled | `neutral-300` (#ced3de) | none                        | none | `neutral-50` (#fdfdfe) |

## CSS Implementation

```css
/* Radio Button Base */
.radio {
  position: relative;
  width: 16px;
  height: 16px;
  border-radius: 10px;
  cursor: pointer;
}

/* Unchecked - Default */
.radio--unchecked {
  background: var(--tnz-neutral-50);
  border: 1px solid var(--tnz-neutral-300);
}

/* Unchecked - Hover */
.radio--unchecked:hover {
  background: var(--tnz-neutral-100);
}

/* Unchecked - Focus */
.radio--unchecked:focus-visible {
  background: var(--tnz-neutral-50);
  box-shadow: 0 0 0 2px var(--tnz-primary-200);
  outline: none;
}

/* Unchecked - Disabled */
.radio--unchecked:disabled {
  background: var(--tnz-neutral-100);
  border-color: var(--tnz-neutral-250);
  cursor: not-allowed;
}

/* Checked - Default */
.radio--checked {
  background: var(--tnz-primary-500);
  border: none;
}

/* Checked - Hover */
.radio--checked:hover {
  background: var(--tnz-primary-600);
}

/* Checked - Focus */
.radio--checked:focus-visible {
  background: var(--tnz-primary-500);
  border: 2px solid var(--tnz-primary-300);
  outline: none;
}

/* Checked - Disabled */
.radio--checked:disabled {
  background: var(--tnz-neutral-300);
  cursor: not-allowed;
}

/* Check indicator (inner dot/checkmark) */
.radio__indicator {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--tnz-neutral-50);
}

.radio__indicator svg {
  width: 100%;
  height: 100%;
}
```

## CSS Custom Properties

```css
:root {
  /* Radio button */
  --radio-size: 16px;
  --radio-radius: 10px;

  /* Radio unchecked */
  --radio-unchecked-bg: var(--tnz-neutral-50);
  --radio-unchecked-bg-hover: var(--tnz-neutral-100);
  --radio-unchecked-border: var(--tnz-neutral-300);
  --radio-unchecked-border-disabled: var(--tnz-neutral-250);

  /* Radio checked */
  --radio-checked-bg: var(--tnz-primary-500);
  --radio-checked-bg-hover: var(--tnz-primary-600);
  --radio-checked-bg-disabled: var(--tnz-neutral-300);
  --radio-checked-focus-border: var(--tnz-primary-300);
  --radio-indicator: var(--tnz-neutral-50);

  /* Focus ring */
  --radio-focus-ring: var(--tnz-primary-200);
}
```
