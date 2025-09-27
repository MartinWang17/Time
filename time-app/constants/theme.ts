import { Platform } from 'react-native';

const BRAND = {
  bgDark: '#000000',   // hsl(0 0% 0%)
  bg: '#0D0D0D',       // hsl(0 0% 5%)
  bgLight: '#1A1A1A',  // hsl(0 0% 10%)
  textPrimary: '#F2F2F2', // hsl(0 0% 95%)
  textMuted: '#B3B3B3',   // hsl(0 0% 70%)
  border: '#4D4D4D',      // hsl(0 0% 30%)
  primary: '#638a7e',
  secondary: '#e7d192',
};

// Keep both schemes aligned to the brand dark palette
export const Colors = {
  light: {
    // Core tokens used app‑wide
    text: BRAND.textPrimary,
    background: BRAND.bgDark,
    tint: BRAND.primary,
    icon: BRAND.textMuted,
    tabIconDefault: BRAND.textMuted,
    tabIconSelected: BRAND.primary,

    // Extras for convenience
    surface: BRAND.bg,
    surfaceHighlight: BRAND.bgLight,
    border: BRAND.border,
    primary: BRAND.primary,
    secondary: BRAND.secondary,

    // Gradients (use with expo-linear-gradient)
    gradient: [BRAND.bg, BRAND.bgLight],
    gradientHover: [BRAND.bgDark, BRAND.bgLight],
  },
  dark: {
    text: BRAND.textPrimary,
    background: BRAND.bgDark,
    tint: BRAND.primary,
    icon: BRAND.textMuted,
    tabIconDefault: BRAND.textMuted,
    tabIconSelected: BRAND.primary,

    surface: BRAND.bg,
    surfaceHighlight: BRAND.bgLight,
    border: BRAND.border,
    primary: BRAND.primary,
    secondary: BRAND.secondary,

    gradient: [BRAND.bg, BRAND.bgLight],
    gradientHover: [BRAND.bgDark, BRAND.bgLight],
  },
};

export const Fonts = Platform.select({
  ios: {
    sans: 'system-ui',
    serif: 'ui-serif',
    rounded: 'ui-rounded',
    mono: 'ui-monospace',
  },
  default: {
    sans: 'normal',
    serif: 'serif',
    rounded: 'normal',
    mono: 'monospace',
  },
  web: {
    sans: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif",
    serif: "Georgia, 'Times New Roman', serif",
    rounded: "'SF Pro Rounded', 'Hiragino Maru Gothic ProN', Meiryo, 'MS PGothic', sans-serif",
    mono: "SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace",
  },
});