# Tailwind CSS

Tenzir theme configuration for Tailwind. All values derive from
[data/brand.yml](../../data/brand.yml) and
[data/tokens.yml](../../data/tokens.yml); if anything here disagrees with
the YAML, the YAML wins.

Spacing and breakpoints intentionally match Tailwind's defaults, so only
colors, fonts, radius, shadows, and z-index need configuration.

## Tailwind v4 (`@theme`)

```css
@import "tailwindcss";

@theme {
  /* Fonts */
  --font-sans: "Inter Variable", "Inter", system-ui, sans-serif;
  --font-mono: "JetBrains Mono Variable", "JetBrains Mono", monospace;

  /* Type scale (size + line height; tracking applied via utilities) */
  --text-xxs: 0.625rem;
  --text-xxs--line-height: 0.875rem;
  --text-xs: 0.75rem;
  --text-xs--line-height: 1.125rem;
  --text-sm: 0.875rem;
  --text-sm--line-height: 1.25rem;
  --text-base: 1rem;
  --text-base--line-height: 1.5rem;
  --text-lg: 1.125rem;
  --text-lg--line-height: 1.75rem;
  --text-xl: 1.25rem;
  --text-xl--line-height: 1.75rem;
  --text-2xl: 1.5rem;
  --text-2xl--line-height: 2rem;
  --text-2xl--letter-spacing: -0.005em;
  --text-3xl: 1.875rem;
  --text-3xl--line-height: 2.25rem;
  --text-3xl--letter-spacing: -0.01em;
  --text-4xl: 2.25rem;
  --text-4xl--line-height: 2.5rem;
  --text-4xl--letter-spacing: -0.015em;
  --text-5xl: 3rem;
  --text-5xl--line-height: 3.5rem;
  --text-5xl--letter-spacing: -0.02em;

  /* Neutrals */
  --color-neutral-800: #0e1017;
  --color-neutral-700: #262e40;
  --color-neutral-600: #414b62;
  --color-neutral-500: #68738d;
  --color-neutral-400: #959db1;
  --color-neutral-300: #ced3de;
  --color-neutral-250: #e3e6ed;
  --color-neutral-200: #f0f1f5;
  --color-neutral-100: #f7f8fa;
  --color-neutral-50: #fdfdfe;

  /* Brand hues */
  --color-blue-600: #0043e0;
  --color-blue-500: #0a54ff;
  --color-blue-400: #477eff;
  --color-blue-300: #adc6ff;
  --color-blue-200: #e0eaff;
  --color-blue-100: #f0f4ff;
  --color-blue-50: #f8f9fc;
  --color-green-600: #1ab252;
  --color-green-500: #29e06c;
  --color-green-400: #5ee891;
  --color-green-300: #b8f5ce;
  --color-green-200: #e4fbec;
  --color-green-100: #f2fdf6;
  --color-lightblue-600: #0096e0;
  --color-lightblue-500: #0aadff;
  --color-lightblue-400: #47c2ff;
  --color-lightblue-300: #ade4ff;
  --color-lightblue-200: #e0f5ff;
  --color-lightblue-100: #f0faff;
  --color-purple-600: #b400e0;
  --color-purple-500: #cf0aff;
  --color-purple-400: #db47ff;
  --color-purple-300: #efadff;
  --color-purple-200: #f9e0ff;
  --color-purple-100: #fcf0ff;
  --color-pink-600: #e0008e;
  --color-pink-500: #ff0aa5;
  --color-pink-400: #ff47bc;
  --color-pink-300: #ffade1;
  --color-pink-200: #ffe0f4;
  --color-pink-100: #fff0f9;
  --color-orange-600: #e04b00;
  --color-orange-500: #ff5c0a;
  --color-orange-400: #ff8547;
  --color-orange-300: #ffc9ad;
  --color-orange-200: #ffebe0;
  --color-orange-100: #fff5f0;
  --color-yellow-600: #d09611;
  --color-yellow-500: #edae1d;
  --color-yellow-400: #f1c255;
  --color-yellow-300: #f9e4b4;
  --color-yellow-200: #fef6e1;
  --color-yellow-100: #fff9f0;
  --color-red-600: #e00025;
  --color-red-500: #ff0a33;
  --color-red-400: #ff4766;
  --color-red-300: #ffadbb;
  --color-red-200: #ffe0e5;
  --color-red-100: #fff0f2;

  /* Semantic aliases */
  --color-primary: var(--color-blue-500);
  --color-success: var(--color-green-600);
  --color-info: var(--color-lightblue-600);
  --color-warning: var(--color-yellow-600);
  --color-error: var(--color-red-500);

  /* Border radius */
  --radius-DEFAULT: 5px;
  --radius-tight: 3px;
  --radius-pill: 35px;

  /* Shadows (two layers each — both required) */
  --shadow-l: 0px 20px 40px -16px #0e101733, 0px 8px 16px -8px #0e101733;
  --shadow-m: 0px 10px 20px -8px #0e101733, 0px 4px 8px -6px #0e101733;
  --shadow-s: 0px 8px 16px -8px #0e101733, 0px 3px 6px -3px #0e101733;
  --shadow-xs: 0px 8px 16px -8px #0e10171a, 0px 3px 6px -3px #0e10171a;

  /* Motion */
  --ease-standard: cubic-bezier(0.4, 0, 0.2, 1);
  --ease-decelerate: cubic-bezier(0, 0, 0.2, 1);
  --ease-accelerate: cubic-bezier(0.4, 0, 1, 1);
}
```

Durations: use Tailwind's arbitrary values or built-ins matching the motion
tokens — `duration-150` (fast), `duration-200` (base), `duration-300`
(slow), `duration-500` (slower).

## Tailwind v3 (`tailwind.config.js`)

```js
module.exports = {
  theme: {
    fontFamily: {
      sans: ['"Inter Variable"', "Inter", "system-ui", "sans-serif"],
      mono: ['"JetBrains Mono Variable"', '"JetBrains Mono"', "monospace"],
    },
    fontSize: {
      xxs: ["0.625rem", { lineHeight: "0.875rem" }],
      xs: ["0.75rem", { lineHeight: "1.125rem" }],
      sm: ["0.875rem", { lineHeight: "1.25rem" }],
      base: ["1rem", { lineHeight: "1.5rem" }],
      lg: ["1.125rem", { lineHeight: "1.75rem" }],
      xl: ["1.25rem", { lineHeight: "1.75rem" }],
      "2xl": ["1.5rem", { lineHeight: "2rem", letterSpacing: "-0.005em" }],
      "3xl": ["1.875rem", { lineHeight: "2.25rem", letterSpacing: "-0.01em" }],
      "4xl": ["2.25rem", { lineHeight: "2.5rem", letterSpacing: "-0.015em" }],
      "5xl": ["3rem", { lineHeight: "3.5rem", letterSpacing: "-0.02em" }],
    },
    fontWeight: {
      normal: "400",
      medium: "500",
      semibold: "600",
    },
    borderRadius: {
      none: "0",
      tight: "3px",
      DEFAULT: "5px",
      pill: "35px",
      full: "9999px",
    },
    boxShadow: {
      l: "0px 20px 40px -16px #0E101733, 0px 8px 16px -8px #0E101733",
      m: "0px 10px 20px -8px #0E101733, 0px 4px 8px -6px #0E101733",
      s: "0px 8px 16px -8px #0E101733, 0px 3px 6px -3px #0E101733",
      xs: "0px 8px 16px -8px #0E10171A, 0px 3px 6px -3px #0E10171A",
      none: "none",
    },
    extend: {
      colors: {
        neutral: {
          50: "#FDFDFE", 100: "#F7F8FA", 200: "#F0F1F5", 250: "#E3E6ED",
          300: "#CED3DE", 400: "#959DB1", 500: "#68738D", 600: "#414B62",
          700: "#262E40", 800: "#0E1017",
        },
        blue: {
          50: "#F8F9FC", 100: "#F0F4FF", 200: "#E0EAFF", 300: "#ADC6FF",
          400: "#477EFF", 500: "#0A54FF", 600: "#0043E0",
        },
        green: {
          100: "#F2FDF6", 200: "#E4FBEC", 300: "#B8F5CE", 400: "#5EE891",
          500: "#29E06C", 600: "#1AB252",
        },
        lightblue: {
          100: "#F0FAFF", 200: "#E0F5FF", 300: "#ADE4FF", 400: "#47C2FF",
          500: "#0AADFF", 600: "#0096E0",
        },
        purple: {
          100: "#FCF0FF", 200: "#F9E0FF", 300: "#EFADFF", 400: "#DB47FF",
          500: "#CF0AFF", 600: "#B400E0",
        },
        pink: {
          100: "#FFF0F9", 200: "#FFE0F4", 300: "#FFADE1", 400: "#FF47BC",
          500: "#FF0AA5", 600: "#E0008E",
        },
        orange: {
          100: "#FFF5F0", 200: "#FFEBE0", 300: "#FFC9AD", 400: "#FF8547",
          500: "#FF5C0A", 600: "#E04B00",
        },
        yellow: {
          100: "#FFF9F0", 200: "#FEF6E1", 300: "#F9E4B4", 400: "#F1C255",
          500: "#EDAE1D", 600: "#D09611",
        },
        red: {
          100: "#FFF0F2", 200: "#FFE0E5", 300: "#FFADBB", 400: "#FF4766",
          500: "#FF0A33", 600: "#E00025",
        },
        primary: "#0A54FF",
        success: "#1AB252",
        info: "#0096E0",
        warning: "#D09611",
        error: "#FF0A33",
      },
      transitionTimingFunction: {
        standard: "cubic-bezier(0.4, 0, 0.2, 1)",
        decelerate: "cubic-bezier(0, 0, 0.2, 1)",
        accelerate: "cubic-bezier(0.4, 0, 1, 1)",
      },
      zIndex: {
        sticky: "100", dropdown: "200", overlay: "300", sidepanel: "400",
        modal: "500", popover: "600", toast: "700", tooltip: "800",
      },
    },
  },
};
```

## Notes

- `text-capitalized` (uppercase labels) has no Tailwind slot; compose it:
  `text-xs font-medium uppercase tracking-[0.05em] leading-4`.
- Mono emphasis: `font-mono italic tracking-[-0.04em]`.
- Graph color order for charts: `blue-500`, `lightblue-500`, `purple-500`,
  `pink-500`, `orange-500`, `yellow-500`.
