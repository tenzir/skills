# CSS Custom Properties

The canonical `--tnz-*` custom-property block for plain-CSS consumers. All
values derive from [data/brand.yml](../../data/brand.yml) and
[data/tokens.yml](../../data/tokens.yml); if anything here disagrees with
the YAML, the YAML wins.

## Naming Convention

`--tnz-<category>-<name>`: palette colors keep their palette name
(`--tnz-blue-500`), semantic roles use `--tnz-color-*`, and other categories
use their token name (`--tnz-space-4`, `--tnz-shadow-m`,
`--tnz-duration-base`, `--tnz-z-modal`).

## Root Block

```css
:root {
  /* Neutrals */
  --tnz-neutral-800: #0e1017;
  --tnz-neutral-700: #262e40;
  --tnz-neutral-600: #414b62;
  --tnz-neutral-500: #68738d;
  --tnz-neutral-400: #959db1;
  --tnz-neutral-300: #ced3de;
  --tnz-neutral-250: #e3e6ed;
  --tnz-neutral-200: #f0f1f5;
  --tnz-neutral-100: #f7f8fa;
  --tnz-neutral-50: #fdfdfe;

  /* Blue (primary brand color) */
  --tnz-blue-600: #0043e0;
  --tnz-blue-500: #0a54ff;
  --tnz-blue-400: #477eff;
  --tnz-blue-300: #adc6ff;
  --tnz-blue-200: #e0eaff;
  --tnz-blue-100: #f0f4ff;
  --tnz-blue-50: #f8f9fc;

  /* Green (secondary brand color) */
  --tnz-green-600: #1ab252;
  --tnz-green-500: #29e06c;
  --tnz-green-400: #5ee891;
  --tnz-green-300: #b8f5ce;
  --tnz-green-200: #e4fbec;
  --tnz-green-100: #f2fdf6;

  /* Lightblue */
  --tnz-lightblue-600: #0096e0;
  --tnz-lightblue-500: #0aadff;
  --tnz-lightblue-400: #47c2ff;
  --tnz-lightblue-300: #ade4ff;
  --tnz-lightblue-200: #e0f5ff;
  --tnz-lightblue-100: #f0faff;

  /* Purple */
  --tnz-purple-600: #b400e0;
  --tnz-purple-500: #cf0aff;
  --tnz-purple-400: #db47ff;
  --tnz-purple-300: #efadff;
  --tnz-purple-200: #f9e0ff;
  --tnz-purple-100: #fcf0ff;

  /* Pink */
  --tnz-pink-600: #e0008e;
  --tnz-pink-500: #ff0aa5;
  --tnz-pink-400: #ff47bc;
  --tnz-pink-300: #ffade1;
  --tnz-pink-200: #ffe0f4;
  --tnz-pink-100: #fff0f9;

  /* Orange */
  --tnz-orange-600: #e04b00;
  --tnz-orange-500: #ff5c0a;
  --tnz-orange-400: #ff8547;
  --tnz-orange-300: #ffc9ad;
  --tnz-orange-200: #ffebe0;
  --tnz-orange-100: #fff5f0;

  /* Yellow */
  --tnz-yellow-600: #d09611;
  --tnz-yellow-500: #edae1d;
  --tnz-yellow-400: #f1c255;
  --tnz-yellow-300: #f9e4b4;
  --tnz-yellow-200: #fef6e1;
  --tnz-yellow-100: #fff9f0;

  /* Red */
  --tnz-red-600: #e00025;
  --tnz-red-500: #ff0a33;
  --tnz-red-400: #ff4766;
  --tnz-red-300: #ffadbb;
  --tnz-red-200: #ffe0e5;
  --tnz-red-100: #fff0f2;

  /* Primary/secondary aliases */
  --tnz-primary-600: var(--tnz-blue-600);
  --tnz-primary-500: var(--tnz-blue-500);
  --tnz-primary-400: var(--tnz-blue-400);
  --tnz-primary-300: var(--tnz-blue-300);
  --tnz-primary-200: var(--tnz-blue-200);
  --tnz-primary-100: var(--tnz-blue-100);
  --tnz-primary-50: var(--tnz-blue-50);
  --tnz-secondary-600: var(--tnz-green-600);
  --tnz-secondary-500: var(--tnz-green-500);
  --tnz-secondary-400: var(--tnz-green-400);
  --tnz-secondary-300: var(--tnz-green-300);
  --tnz-secondary-200: var(--tnz-green-200);
  --tnz-secondary-100: var(--tnz-green-100);

  /* Semantic aliases */
  --tnz-color-primary: var(--tnz-blue-500);
  --tnz-color-success: var(--tnz-green-600);
  --tnz-color-info: var(--tnz-lightblue-600);
  --tnz-color-warning: var(--tnz-yellow-600);
  --tnz-color-error: var(--tnz-red-500);
  --tnz-color-text: var(--tnz-neutral-800);
  --tnz-color-text-secondary: var(--tnz-neutral-600);
  --tnz-color-text-tertiary: var(--tnz-neutral-500);
  --tnz-color-background: var(--tnz-neutral-50);
  --tnz-color-surface: var(--tnz-neutral-50);
  --tnz-color-muted: var(--tnz-neutral-100);
  --tnz-color-border: var(--tnz-neutral-200);

  /* Opacities: overlays and the outline-fill tint */
  --tnz-dim-50: 0.5;
  --tnz-dim-20: 0.2;
  --tnz-dim-8: 0.08;
  --tnz-lighten-20: 0.2;
  --tnz-lighten-8: 0.08;
  --tnz-tint-12: 0.12;

  /* Font families */
  --tnz-font-sans: "Inter Variable", "Inter", system-ui, sans-serif;
  --tnz-font-mono: "JetBrains Mono Variable", "JetBrains Mono", monospace;

  /* Font sizes */
  --tnz-text-xxs: 0.625rem; /* 10px */
  --tnz-text-xs: 0.75rem; /* 12px */
  --tnz-text-sm: 0.875rem; /* 14px */
  --tnz-text-base: 1rem; /* 16px */
  --tnz-text-lg: 1.125rem; /* 18px */
  --tnz-text-xl: 1.25rem; /* 20px */
  --tnz-text-2xl: 1.5rem; /* 24px */
  --tnz-text-3xl: 1.875rem; /* 30px */
  --tnz-text-4xl: 2.25rem; /* 36px */
  --tnz-text-5xl: 3rem; /* 48px */

  /* Line heights */
  --tnz-leading-xxs: 0.875rem; /* 14px */
  --tnz-leading-xs: 1.125rem; /* 18px */
  --tnz-leading-sm: 1.25rem; /* 20px */
  --tnz-leading-base: 1.5rem; /* 24px */
  --tnz-leading-lg: 1.75rem; /* 28px */
  --tnz-leading-xl: 1.75rem; /* 28px */
  --tnz-leading-2xl: 2rem; /* 32px */
  --tnz-leading-3xl: 2.25rem; /* 36px */
  --tnz-leading-4xl: 2.5rem; /* 40px */
  --tnz-leading-5xl: 3.5rem; /* 56px */

  /* Font weights */
  --tnz-font-regular: 400;
  --tnz-font-medium: 500;
  --tnz-font-semibold: 600;

  /* Spacing */
  --tnz-space-0: 0;
  --tnz-space-0-5: 0.125rem; /* 2px */
  --tnz-space-1: 0.25rem; /* 4px */
  --tnz-space-1-5: 0.375rem; /* 6px */
  --tnz-space-2: 0.5rem; /* 8px */
  --tnz-space-3: 0.75rem; /* 12px */
  --tnz-space-4: 1rem; /* 16px */
  --tnz-space-5: 1.25rem; /* 20px */
  --tnz-space-6: 1.5rem; /* 24px */
  --tnz-space-7: 1.75rem; /* 28px */
  --tnz-space-8: 2rem; /* 32px */
  --tnz-space-10: 2.5rem; /* 40px */
  --tnz-space-16: 4rem; /* 64px */
  --tnz-space-20: 5rem; /* 80px */

  /* Border radius */
  --tnz-radius: 5px;
  --tnz-radius-tight: 3px;
  --tnz-radius-pill: 9999px;

  /* Shadows (two layers each — both required) */
  --tnz-shadow-l: 0px 20px 40px -16px #0e101733, 0px 8px 16px -8px #0e101733;
  --tnz-shadow-m: 0px 10px 20px -8px #0e101733, 0px 4px 8px -6px #0e101733;
  --tnz-shadow-s: 0px 8px 16px -8px #0e101733, 0px 3px 6px -3px #0e101733;
  --tnz-shadow-xs: 0px 8px 16px -8px #0e10171a, 0px 3px 6px -3px #0e10171a;

  /* Motion */
  --tnz-duration-instant: 0ms;
  --tnz-duration-fast: 150ms;
  --tnz-duration-base: 200ms;
  --tnz-duration-slow: 300ms;
  --tnz-duration-slower: 500ms;
  --tnz-ease-standard: cubic-bezier(0.4, 0, 0.2, 1);
  --tnz-ease-decelerate: cubic-bezier(0, 0, 0.2, 1);
  --tnz-ease-accelerate: cubic-bezier(0.4, 0, 1, 1);

  /* Z-index */
  --tnz-z-base: 0;
  --tnz-z-sticky: 100;
  --tnz-z-dropdown: 200;
  --tnz-z-overlay: 300;
  --tnz-z-sidepanel: 400;
  --tnz-z-modal: 500;
  --tnz-z-popover: 600;
  --tnz-z-toast: 700;
  --tnz-z-tooltip: 800;
}
```

Breakpoints cannot be expressed as custom properties (media queries don't
resolve `var()`); use the values from `tenzir.breakpoint` directly:
`640px`, `768px`, `1024px`, `1280px`, `1536px`.

Outline-style fills tint any palette color at 12% alpha:

```css
.tag--outline {
  background: rgb(from var(--tnz-blue-500) r g b / var(--tnz-tint-12));
  color: var(--tnz-blue-500);
}
```

## Dark Mode

Dark mode remaps only the semantic aliases — component CSS that uses
`--tnz-color-*` adapts automatically (mapping from `tenzir.dark` in
tokens.yml):

```css
[data-theme="dark"] {
  --tnz-color-text: var(--tnz-neutral-50);
  --tnz-color-text-secondary: var(--tnz-neutral-300);
  --tnz-color-text-tertiary: var(--tnz-neutral-400);
  --tnz-color-background: var(--tnz-neutral-800);
  --tnz-color-surface: var(--tnz-neutral-800);
  --tnz-color-muted: var(--tnz-neutral-700);
  --tnz-color-border: var(--tnz-neutral-700);
  --tnz-color-primary: var(--tnz-blue-400);
  --tnz-color-success: var(--tnz-green-400);
  --tnz-color-info: var(--tnz-lightblue-400);
  --tnz-color-warning: var(--tnz-yellow-400);
  --tnz-color-error: var(--tnz-red-400);
}
```

## Usage Example

```css
.panel {
  background: var(--tnz-color-surface);
  border: 1px solid var(--tnz-color-border);
  border-radius: var(--tnz-radius);
  box-shadow: var(--tnz-shadow-xs);
  padding: var(--tnz-space-4);
  font-family: var(--tnz-font-sans);
  font-size: var(--tnz-text-sm);
  line-height: var(--tnz-leading-sm);
  color: var(--tnz-color-text);
}
```
