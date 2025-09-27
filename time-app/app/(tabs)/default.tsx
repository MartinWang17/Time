import { Image } from 'expo-image';
import { Platform, StyleSheet, Text, View } from 'react-native';
import { Button, Card, Chip, Paragraph, Title } from 'react-native-paper';

import { HelloWave } from '@/components/hello-wave';
import ParallaxScrollView from '@/components/parallax-scroll-view';
import { ThemedText } from '@/components/themed-text';
import { ThemedView } from '@/components/themed-view';
import { Link } from 'expo-router';

export default function HomeScreen() {
  return (
    <ParallaxScrollView
      headerBackgroundColor={{ light: '#A1CEDC', dark: '#1D3D47' }}
      headerImage={
        <Image
          source={require('@/assets/images/partial-react-logo.png')}
          style={styles.reactLogo}
        />
      }>
      <ThemedView style={styles.titleContainer}>
        <ThemedText type="title">Welcome!</ThemedText>
        <HelloWave />
      </ThemedView>
      <View className="bg-blue-500 p-4 rounded-lg mx-4 my-2">
        <Text className="text-white font-bold text-center">
          🎉 Tailwind CSS is working! This is styled with NativeWind.
        </Text>
      </View>
      
      {/* React Native Paper Demo Components */}
      <ThemedView style={styles.paperContainer}>
        <ThemedText type="subtitle">📱 React Native Paper Components</ThemedText>
        
        <Card style={styles.card}>
          <Card.Content>
            <Title>Material Design Card</Title>
            <Paragraph>React Native Paper is now set up and working! This card component follows Material Design guidelines.</Paragraph>
          </Card.Content>
          <Card.Actions>
            <Button onPress={() => alert('Paper Button Pressed!')}>Got it</Button>
            <Button onPress={() => alert('Another action!')}>Action</Button>
          </Card.Actions>
        </Card>
        
        <View style={styles.buttonsContainer}>
          <Button 
            mode="contained" 
            onPress={() => alert('Contained button pressed!')}
            style={styles.button}
          >
            Contained Button
          </Button>
          <Button 
            mode="outlined" 
            onPress={() => alert('Outlined button pressed!')}
            style={styles.button}
          >
            Outlined Button
          </Button>
        </View>
        
        <View style={styles.chipsContainer}>
          <Chip icon="information" onPress={() => alert('Chip pressed!')}>Info Chip</Chip>
          <Chip mode="outlined" onPress={() => alert('Outlined chip pressed!')}>Outlined Chip</Chip>
        </View>
      </ThemedView>
      <ThemedView style={styles.stepContainer}>
        <ThemedText type="subtitle">Step 1: Try it</ThemedText>
        <ThemedText>
          Edit <ThemedText type="defaultSemiBold">app/(tabs)/index.tsx</ThemedText> to see changes.
          Press{' '}
          <ThemedText type="defaultSemiBold">
            {Platform.select({
              ios: 'cmd + d',
              android: 'cmd + m',
              web: 'F12',
            })}
          </ThemedText>{' '}
          to open developer tools.
        </ThemedText>
      </ThemedView>
      <ThemedView style={styles.stepContainer}>
        <Link href="/modal">
          <Link.Trigger>
            <ThemedText type="subtitle">Step 2: Explore</ThemedText>
          </Link.Trigger>
          <Link.Preview />
          <Link.Menu>
            <Link.MenuAction title="Action" icon="cube" onPress={() => alert('Action pressed')} />
            <Link.MenuAction
              title="Share"
              icon="square.and.arrow.up"
              onPress={() => alert('Share pressed')}
            />
            <Link.Menu title="More" icon="ellipsis">
              <Link.MenuAction
                title="Delete"
                icon="trash"
                destructive
                onPress={() => alert('Delete pressed')}
              />
            </Link.Menu>
          </Link.Menu>
        </Link>

        <ThemedText>
          {`Tap the Explore tab to learn more about what's included in this starter app.`}
        </ThemedText>
      </ThemedView>
      <ThemedView style={styles.stepContainer}>
        <ThemedText type="subtitle">Step 3: Get a fresh start</ThemedText>
        <ThemedText>
          {`When you're ready, run `}
          <ThemedText type="defaultSemiBold">npm run reset-project</ThemedText> to get a fresh{' '}
          <ThemedText type="defaultSemiBold">app</ThemedText> directory. This will move the current{' '}
          <ThemedText type="defaultSemiBold">app</ThemedText> to{' '}
          <ThemedText type="defaultSemiBold">app-example</ThemedText>.
        </ThemedText>
      </ThemedView>
    </ParallaxScrollView>
  );
}

const styles = StyleSheet.create({
  titleContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  stepContainer: {
    gap: 8,
    marginBottom: 8,
  },
  reactLogo: {
    height: 178,
    width: 290,
    bottom: 0,
    left: 0,
    position: 'absolute',
  },
  paperContainer: {
    gap: 12,
    marginBottom: 16,
    paddingHorizontal: 16,
  },
  card: {
    marginVertical: 8,
  },
  buttonsContainer: {
    flexDirection: 'row',
    gap: 12,
    marginVertical: 8,
  },
  button: {
    flex: 1,
  },
  chipsContainer: {
    flexDirection: 'row',
    gap: 8,
    marginVertical: 8,
  },
});
