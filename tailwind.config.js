/** Tailwind config for compiling a static, production CSS file.
 *  Theme mirrors the previous inline (CDN) config in build.py.
 *  Run:  npx tailwindcss -c tailwind.config.js -i css/tailwind-src.css -o css/tailwind.min.css --minify
 */
module.exports = {
  darkMode: "class",
  content: ["./*.html"],
  theme: { extend: {
    colors: {
      "primary-container": "#facc15", "on-primary-container": "#6c5700",
      "surface": "#131316", "surface-dim": "#131316",
      "surface-container-lowest": "#0e0e11", "surface-container-low": "#1b1b1e",
      "surface-container": "#1f1f22", "surface-container-high": "#2a2a2d",
      "surface-container-highest": "#353438", "surface-bright": "#39393c",
      "surface-tint": "#eec200", "on-surface": "#e5e1e6", "on-surface-variant": "#cac4d0",
      "primary": "#ffecb9", "on-primary": "#3c2f00", "primary-fixed": "#ffe083",
      "primary-fixed-dim": "#eec200", "inverse-primary": "#735c00",
      "secondary": "#c7c5d0", "secondary-container": "#46464f", "on-secondary-container": "#b6b4bf",
      "outline": "#9a9078", "outline-variant": "#4d4632",
      "inverse-surface": "#e5e1e6", "inverse-on-surface": "#303033",
      "background": "#131316", "on-background": "#e5e1e6", "surface-variant": "#353438",
      "white": "#ffffff", "gray-50": "#f8f9fa", "gray-100": "#f1f5f9", "gray-200": "#e2e8f0",
      "gray-600": "#4b5563", "gray-700": "#374151", "gray-900": "#111827"
    },
    borderRadius: { "DEFAULT": "0.125rem", "lg": "0.25rem", "xl": "0.5rem", "full": "0.75rem" },
    spacing: { "gutter": "1.5rem", "margin": "2rem", "space-xs": "0.25rem", "space-sm": "0.5rem",
      "space-md": "1rem", "space-lg": "1.5rem", "space-xl": "2.5rem" },
    fontFamily: {
      "headline": ["Barlow Condensed", "Barlow Condensed Fallback", "Arial Narrow", "sans-serif"],
      "body": ["Montserrat", "Montserrat Fallback", "Arial", "sans-serif"],
      "mono": ["JetBrains Mono", "JetBrains Mono Fallback", "ui-monospace", "monospace"]
    },
    fontSize: {
      "display-hero": ["72px", { lineHeight: "80px", letterSpacing: "-0.03em", fontWeight: "700" }],
      "display-hero-mobile": ["40px", { lineHeight: "46px", letterSpacing: "-0.02em", fontWeight: "700" }],
      "headline-xl": ["48px", { lineHeight: "56px", letterSpacing: "-0.02em", fontWeight: "700" }],
      "headline-xl-mobile": ["32px", { lineHeight: "38px", letterSpacing: "-0.01em", fontWeight: "700" }],
      "headline-lg": ["36px", { lineHeight: "44px", letterSpacing: "-0.015em", fontWeight: "600" }],
      "headline-md": ["24px", { lineHeight: "32px", fontWeight: "600" }],
      "headline-sm": ["20px", { lineHeight: "28px", fontWeight: "600" }],
      "body-lg": ["18px", { lineHeight: "28px", fontWeight: "400" }],
      "body-md": ["15px", { lineHeight: "24px", fontWeight: "400" }],
      "body-sm": ["13px", { lineHeight: "20px", fontWeight: "400" }],
      "label-data": ["13px", { lineHeight: "18px", letterSpacing: "0.04em", fontWeight: "500" }],
      "label-caps": ["11px", { lineHeight: "14px", letterSpacing: "0.12em", fontWeight: "700" }]
    }
  } }
};
