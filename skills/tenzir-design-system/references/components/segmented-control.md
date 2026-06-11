# Segmented Control

A toggle component for switching between mutually exclusive options, available in icon and text variants.

## Props

| Prop     | Values                              |
| -------- | ----------------------------------- |
| `type`   | `icon`, `text`                      |
| `amount` | `two`, `three`, `four`              |
| `size`   | `xs` (24px), `s` (28px), `m` (32px) |
| `active` | `1`, `2`, `3`, `4`                  |

## Container Specifications

| Property      | Value                       |
| ------------- | --------------------------- |
| Background    | `neutral-100` (#f7f8fa)     |
| Border        | 1px `neutral-200` (#f0f1f5) |
| Border radius | 5px                         |
| Padding       | 2px                         |
| Gap           | 2px (between buttons)       |

## Size Specifications

### Icon Type

| Size     | Container Height | Button Height | Button Width | Icon Size |
| -------- | ---------------- | ------------- | ------------ | --------- |
| M (32px) | 32px             | 28px          | 32px         | 24px      |

### Text Type

| Size      | Container Height | Button Height | Padding X | Font Size | Line Height |
| --------- | ---------------- | ------------- | --------- | --------- | ----------- |
| XS (24px) | 24px             | 20px          | 6px       | 12px      | 18px        |
| S (28px)  | 28px             | 24px          | 8px       | 14px      | 20px        |

## Button States

**Note:** Unlike other interactive components, segmented controls have only two states: Active and Inactive. There are no hover, pressed, or focus states.

### Active Button

| Property      | Value                                   |
| ------------- | --------------------------------------- |
| Background    | `neutral-50` (#fdfdfe)                  |
| Border radius | 3px                                     |
| Shadow        | `0px 1px 4px 0px rgba(14, 16, 23, 0.2)` |
| Text color    | `neutral-800` (#0e1017)                 |
| Icon color    | `neutral-800` (#0e1017)                 |

### Inactive Button

| Property      | Value                   |
| ------------- | ----------------------- |
| Background    | transparent             |
| Border radius | 4px                     |
| Shadow        | none                    |
| Text color    | `neutral-500` (#68738d) |
| Icon color    | `neutral-600` (#414b62) |

## Typography

- Font family: Inter
- Font weight: Medium (500)
- Text alignment: center
- Min width: 20px

## CSS Implementation

```css
/* Container */
.segmented-control {
  display: flex;
  align-items: center;
  gap: 0;
  padding: 2px;
  background: var(--tnz-neutral-100);
  border: 1px solid var(--tnz-neutral-200);
  border-radius: 5px;
}

/* Buttons wrapper */
.segmented-control__buttons {
  display: flex;
  align-items: center;
  gap: 2px;
}

/* Base button */
.segmented-control__button {
  display: flex;
  align-items: center;
  justify-content: center;
  background: transparent;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition:
    background var(--tnz-duration-fast) var(--tnz-ease-standard),
    box-shadow var(--tnz-duration-fast) var(--tnz-ease-standard);
}

/* Active button */
.segmented-control__button--active {
  background: var(--tnz-neutral-50);
  border-radius: 3px;
  box-shadow: 0px 1px 4px 0px rgba(14, 16, 23, 0.2);
}

/* Icon button - M size */
.segmented-control__button--icon-m {
  width: 32px;
  height: 28px;
}

.segmented-control__button--icon-m svg {
  width: 24px;
  height: 24px;
}

/* Text button - XS size */
.segmented-control__button--text-xs {
  height: 20px;
  padding: 0 6px;
  min-width: 20px;
  font-family: "Inter", sans-serif;
  font-size: 12px;
  font-weight: 500;
  line-height: 18px;
}

/* Text button - S size */
.segmented-control__button--text-s {
  height: 24px;
  padding: 0 8px;
  min-width: 20px;
  font-family: "Inter", sans-serif;
  font-size: 14px;
  font-weight: 500;
  line-height: 20px;
}

/* Inactive text color */
.segmented-control__button:not(.segmented-control__button--active) {
  color: var(--tnz-neutral-500);
}

/* Inactive icon color */
.segmented-control__button:not(.segmented-control__button--active) svg {
  color: var(--tnz-neutral-600);
}

/* Active text/icon color */
.segmented-control__button--active {
  color: var(--tnz-neutral-800);
}

.segmented-control__button--active svg {
  color: var(--tnz-neutral-800);
}
```

## CSS Custom Properties

```css
:root {
  /* Segmented control container */
  --segmented-control-bg: var(--tnz-neutral-100);
  --segmented-control-border: var(--tnz-neutral-200);
  --segmented-control-radius: 5px;
  --segmented-control-padding: 2px;
  --segmented-control-gap: 2px;

  /* Active button */
  --segmented-control-active-bg: var(--tnz-neutral-50);
  --segmented-control-active-radius: 3px;
  --segmented-control-active-shadow: 0px 1px 4px 0px rgba(14, 16, 23, 0.2);
  --segmented-control-active-color: var(--tnz-neutral-800);

  /* Inactive button */
  --segmented-control-inactive-radius: 4px;
  --segmented-control-inactive-color: var(--tnz-neutral-500);
  --segmented-control-inactive-icon-color: var(--tnz-neutral-600);

  /* Sizes - Icon M */
  --segmented-control-icon-m-width: 32px;
  --segmented-control-icon-m-height: 28px;
  --segmented-control-icon-m-icon: 24px;

  /* Sizes - Text XS */
  --segmented-control-text-xs-height: 20px;
  --segmented-control-text-xs-px: 6px;
  --segmented-control-text-xs-font: 12px;
  --segmented-control-text-xs-lh: 18px;

  /* Sizes - Text S */
  --segmented-control-text-s-height: 24px;
  --segmented-control-text-s-px: 8px;
  --segmented-control-text-s-font: 14px;
  --segmented-control-text-s-lh: 20px;
}
```

## Usage Guidelines

1. **Type selection**:
   - **Icon** - Use for switching between view modes (e.g., grid/list, table/chart)
   - **Text** - Use for time ranges, categories, or labeled options

2. **Common patterns**:
   - View switchers: Grid | List | Table
   - Time filters: 1D | 1W | 1M | 1Y
   - Data views: Chart | Table | Raw
