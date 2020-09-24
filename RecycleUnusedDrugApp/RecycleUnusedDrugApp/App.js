import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
// import { createBottomTabNavigator } from 'react-navigation-tabs'
import HomeScreen from "./src/screens/HomeScreen.js";
import InfoScreen from './src/screens/InfoScreen';
import MapScreen from './src/screens/MapScreen';
import StatisticsScreen from './src/screens/StatisticsScreen';
import NotiScreen from './src/screens/NotiScreen';

const navigator = createStackNavigator(
  {
    Home: HomeScreen,
    Info: InfoScreen,
    Map: MapScreen,
    Stat: StatisticsScreen,
    Noti: NotiScreen
  },
  {
    initialRouteName: "Home",
    defaultNavigationOptions: {
      title: "Jimin's Recycling Unused-Medication App"
    }
  }
);


export default createAppContainer(navigator);
