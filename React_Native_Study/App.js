import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import HomeScreen from "./src/screens/HomeScreen";
import UserLoginScreen from './src/screens/UserLoginScreen';
import WelcomePageScreen from './src/screens/WelcomePageScreen';

const navigator = createStackNavigator(
  {
    Home: HomeScreen,
    UserLogin: UserLoginScreen,
    Welcome: WelcomePageScreen
  },
  {
    initialRouteName: "Home",
    defaultNavigationOptions: {
      title: "App"
    }
  }
);

export default createAppContainer(navigator);
