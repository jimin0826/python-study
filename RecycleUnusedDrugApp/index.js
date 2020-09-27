import {AppRegistry} from 'react-native';
import App from './App';
import {name as appName} from './app.json';

AppRegistry.registerComponent(appName, () => App);

// 앱이 가장 처음 참조하는 코드 : App을 참조하라고 명령