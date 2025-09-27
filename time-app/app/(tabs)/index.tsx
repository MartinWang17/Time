import AllCaughtUp from '@/assets/svg/all-caught-up.svg';
import { ThemedText } from '@/components/themed-text';
import { ThemedView } from '@/components/themed-view';
import { Colors } from '@/constants/theme';
import { useColorScheme } from '@/hooks/use-color-scheme';
import React from 'react';
import { Pressable, StyleSheet, View } from 'react-native';
import { SafeAreaView, useSafeAreaInsets } from 'react-native-safe-area-context';

const TABS = ['ALL', 'Nearest Upcoming', 'Today', "Archived"] as const;

// Define consistent spacing
const SPACING = {
  xs: 4,
  sm: 8,
  md: 16,
  lg: 24,
  xl: 32,
};

export default function TasksScreen() {
  const colorScheme = useColorScheme();
  const theme = Colors[colorScheme ?? 'light'];
  const insets = useSafeAreaInsets();

  // Presentational only; keep ALL highlighted by default.
  // const activeTab: (typeof TABS)[number] = 'ALL';
  const [activeTab, setActiveTab] = React.useState<typeof TABS[number]>('ALL');

  const bottomBarSpace = 80 + 28; // BAR_HEIGHT + bottomOffset from BottomBar

  return (
    <SafeAreaView style={[styles.safeArea, { paddingTop: Math.max(insets.top - SPACING.xl, 0), paddingBottom: insets.bottom + bottomBarSpace }]}>
      <ThemedView style={styles.container}>
        {/* Header */}
        <View style={styles.header}>
          <ThemedText type="title" style={{ textAlign: 'center'}}>Tasks</ThemedText>
        </View>

        {/* Tabs */}
        <View style={styles.tabsRow}>
          {TABS.map((label) => {
            const isActive = label === activeTab;
            return (
              <Pressable
                key={label}
                style={[styles.tabItem, isActive && { borderBottomColor: theme.tint }]}
                onPress={() => {
                  setActiveTab(label);
                }}
                android_ripple={{ color: String(theme.icon) }}
              >
                <ThemedText
                  style={[
                    styles.tabText,
                    { color: isActive ? theme.tint : theme.icon },
                  ]}
                >
                  {label}
                </ThemedText>
              </Pressable>
            );
          })}
        </View>

        {/* Body */}
        <View style={styles.body}>
          {/* <View
            style={[
              styles.circle,
              { borderColor: theme.tint },
            ]}
          >
            <ThemedText style={styles.checkmark}>✓</ThemedText>
          </View> */}
          <AllCaughtUp 
            width={260}
            height={260}
            color={theme.tint}
            style={{ marginBottom: SPACING.lg }}
          />
          <ThemedText style={styles.caughtUp}>ALL CAUGHT UP!</ThemedText>
          <ThemedText style={[styles.subtext, { color: theme.icon }]}>
            Record it and forget it. 
          </ThemedText>
          <ThemedText style={[styles.subtext, { color: theme.icon }]}>
            Never let a task slip again!
          </ThemedText>
        </View>

      </ThemedView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
  },
  container: {
    flex: 1,
    paddingHorizontal: SPACING.md,
  },
  header: {
    marginBottom: SPACING.xs,
  },
  tabsRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    gap: SPACING.sm,
    marginBottom: SPACING.md,
  },
  tabItem: {
    alignItems: 'center',
    paddingVertical: SPACING.sm,
    paddingHorizontal: SPACING.lg,
    borderBottomWidth: 3,
    borderBottomColor: 'transparent',
  },
  tabText: {
    fontSize: 16,
    fontWeight: '600',
  },
  body: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    paddingHorizontal: SPACING.md,
  },
  circle: {
    width: 260,
    height: 260,
    borderRadius: 130,
    borderWidth: 6,
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: SPACING.lg,
  },
  checkmark: {
    fontSize: 120,
    fontWeight: 'bold',
  },
  caughtUp: {
    fontSize: 28,
    fontWeight: '800',
    textAlign: 'center',
    marginBottom: SPACING.sm,
    lineHeight: 34,
  },
  subtext: {
    fontSize: 16,
    textAlign: 'center',
  },
});