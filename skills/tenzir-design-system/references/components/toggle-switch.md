# Toggle Switch

Binary switch control for on/off states.

## Props

| Prop     | Values                                  |
| -------- | --------------------------------------- |
| `state`  | `default`, `hover`, `focus`, `disabled` |
| `active` | `true`, `false`                         |

## Size Specifications

| Property      | Value |
| ------------- | ----- |
| Width         | 32px  |
| Height        | 20px  |
| Border radius | pill (9999px) |
| Knob size     | 16px  |
| Knob inset    | 2px   |

## Inactive State Specifications

| State    | Background              | Ring                        |
| -------- | ----------------------- | --------------------------- |
| Default  | `neutral-300` (#ced3de) | none                        |
| Hover    | `neutral-400` (#959db1) | none                        |
| Focus    | `neutral-300` (#ced3de) | 2px `primary-200` (#e0eaff) |
| Disabled | `neutral-200` (#f0f1f5) | none                        |

## Active State Specifications

| State    | Background              | Border                      | Ring |
| -------- | ----------------------- | --------------------------- | ---- |
| Default  | `primary-500` (#0a54ff) | none                        | none |
| Hover    | `primary-600` (#0043e0) | none                        | none |
| Focus    | `primary-500` (#0a54ff) | 2px `primary-300` (#adc6ff) | none |
| Disabled | `neutral-300` (#ced3de) | none                        | none |

## Knob Specifications

| Property | Value                  |
| -------- | ---------------------- |
| Size     | 16px                   |
| Color    | `neutral-50` (#fdfdfe) |
| Shape    | Circle                 |
| Position | 2px from edge          |

## Knob Position

| State    | Left Position |
| -------- | ------------- |
| Inactive | 2px           |
| Active   | 14px (right)  |

## CSS Implementation

```css
/* Toggle Switch Base */
.toggle {
  position: relative;
  width: 32px;
  height: 20px;
  border-radius: var(--tnz-radius-pill);
  cursor: pointer;
  transition: background var(--tnz-duration-base) var(--tnz-ease-standard);
}

/* Inactive - Default */
.toggle--inactive {
  background: var(--tnz-neutral-300);
}

/* Inactive - Hover */
.toggle--inactive:hover {
  background: var(--tnz-neutral-400);
}

/* Inactive - Focus */
.toggle--inactive:focus-visible {
  background: var(--tnz-neutral-300);
  box-shadow: 0 0 0 2px var(--tnz-primary-200);
  outline: none;
}

/* Inactive - Disabled */
.toggle--inactive:disabled {
  background: var(--tnz-neutral-200);
  cursor: not-allowed;
}

/* Active - Default */
.toggle--active {
  background: var(--tnz-primary-500);
}

/* Active - Hover */
.toggle--active:hover {
  background: var(--tnz-primary-600);
}

/* Active - Focus */
.toggle--active:focus-visible {
  background: var(--tnz-primary-500);
  border: 2px solid var(--tnz-primary-300);
  outline: none;
}

/* Active - Disabled */
.toggle--active:disabled {
  background: var(--tnz-neutral-300);
  cursor: not-allowed;
}

/* Knob */
.toggle__knob {
  position: absolute;
  top: 2px;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: var(--tnz-neutral-50);
  transition: left var(--tnz-duration-base) var(--tnz-ease-standard);
}

/* Knob positions */
.toggle--inactive .toggle__knob {
  left: 2px;
}

.toggle--active .toggle__knob {
  left: 14px;
}
```

## CSS Custom Properties

```css
:root {
  /* Toggle switch */
  --toggle-width: 32px;
  --toggle-height: 20px;
  --toggle-radius: var(--tnz-radius-pill);
  --toggle-knob-size: 16px;
  --toggle-knob-inset: 2px;

  /* Toggle inactive */
  --toggle-inactive-bg: var(--tnz-neutral-300);
  --toggle-inactive-bg-hover: var(--tnz-neutral-400);
  --toggle-inactive-bg-disabled: var(--tnz-neutral-200);

  /* Toggle active */
  --toggle-active-bg: var(--tnz-primary-500);
  --toggle-active-bg-hover: var(--tnz-primary-600);
  --toggle-active-bg-disabled: var(--tnz-neutral-300);
  --toggle-active-focus-border: var(--tnz-primary-300);

  /* Knob */
  --toggle-knob-color: var(--tnz-neutral-50);

  /* Focus ring */
  --toggle-focus-ring: var(--tnz-primary-200);
}
```

## Usage Guidelines

1. **Behavior**:
   - Animate the knob transition with the base duration (200ms)
