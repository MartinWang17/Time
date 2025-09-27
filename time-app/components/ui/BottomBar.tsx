import MaterialIcons from '@expo/vector-icons/MaterialIcons';
import React from 'react';
import { Pressable, StyleSheet, View, type StyleProp, type ViewStyle } from 'react-native';
import { FAB } from 'react-native-paper';

import { Colors } from '@/constants/theme';
import { useColorScheme } from '@/hooks/use-color-scheme';
import { useSafeAreaInsets } from 'react-native-safe-area-context';

type BottomBarProps = {
  onLeftPress?: () => void;
  onRightPress?: () => void;
  onFabPress?: () => void;
  leftIconName?: React.ComponentProps<typeof MaterialIcons>['name'];
  rightIconName?: React.ComponentProps<typeof MaterialIcons>['name'];
  style?: StyleProp<ViewStyle>;
};

const BAR_HEIGHT: number = 80;
const FAB_SIZE: number = 56;

export function BottomBar({
  onLeftPress,
  onRightPress,
  onFabPress,
  leftIconName = 'menu',
  rightIconName = 'more-horiz',
  style,
}: BottomBarProps) {
  const insets = useSafeAreaInsets();
  const colorScheme = useColorScheme();
  const theme = Colors[colorScheme ?? 'light'];

  const barPaddingBottom: number = Math.max(insets.bottom, 12);
  const fabBottom: number = barPaddingBottom + BAR_HEIGHT / 2 - FAB_SIZE / 2 + 4;

  return (
    <View pointerEvents="box-none" style={[styles.root, style]}>
      <View
        style={[
          styles.bar,
          {
            backgroundColor: theme.surfaceHighlight,
            borderTopColor: theme.secondary,
            paddingBottom: barPaddingBottom,
          },
        ]}
      >
        <Pressable onPress={onLeftPress} style={styles.sideButton}>
          <MaterialIcons name={leftIconName} size={28} color={theme.icon} />
        </Pressable>

        <View style={styles.fabSpacer} />

        <Pressable onPress={onRightPress} style={styles.sideButton}>
          <MaterialIcons name={rightIconName} size={28} color={theme.icon} />
        </Pressable>
      </View>

      <FAB
        icon="plus"
        onPress={onFabPress}
        color={theme.text}
        style={[
          styles.fab,
          {
            backgroundColor: theme.tint,
            bottom: fabBottom,
            borderWidth: 3,
            borderColor: theme.secondary,
            width: FAB_SIZE + 6,
            height: FAB_SIZE + 6,
            borderRadius: (FAB_SIZE + 6) / 2,
          },
        ]}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  root: {
    position: 'absolute',
    left: 0,
    right: 0,
    bottom: 0,
    zIndex: 100,
  },
  bar: {
    height: BAR_HEIGHT,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    borderTopWidth: 2,
    paddingHorizontal: 20,
  },
  sideButton: {
    padding: 8,
  },
  fabSpacer: {
    width: FAB_SIZE, // keeps space for the center FAB
  },
  fab: {
    position: 'absolute',
    alignSelf: 'center',
    width: FAB_SIZE,
    height: FAB_SIZE,
    borderRadius: FAB_SIZE / 2,
    elevation: 6,
    zIndex: 101,
  },
});