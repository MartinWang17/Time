import React from 'react';

import { BottomBar } from '@/components/ui/BottomBar';
import { useColorScheme } from '@/hooks/use-color-scheme';
import { Stack } from 'expo-router';

export default function TabLayout() {
  const colorScheme = useColorScheme();

  return (
    <>
      <Stack>
        <Stack.Screen name="index" options={{ headerShown: false }} />
      </Stack>
      <BottomBar
          onLeftPress={() => { /* TODO: open menu */ }}
          onFabPress={() => { /* TODO: new task */ }}
          onRightPress={() => { /* TODO: show more */ }}
        />
    </>
  );
}