import React, { Component } from "react";
import { 
  Text, 
  StyleSheet, 
  View, 
  Button, 
  TouchableOpacity,
  Dimensions,
  ProgressViewIOSComponent
} from "react-native";
import Header from '../Components/Header';
import MapView, { Marker } from 'react-native-maps';

const screenWidth = Dimensions.get('window').width
const DrugStoreLocation = {
  1: [37.564436, 127.083531],
  2: [37.564112, 127.079948],
  3: [37.563670, 127.082824]
}

export default class MapScreen extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return(
      <View style={{width: screenWidth, flexDirection: 'column', alignItems: 'stretch'}}>
        <Header />
        <MapView
          style={{width: screenWidth, height: 700}}
          initialRegion={{
            latitude: 37.563615,
            longitude: 127.085089,
            latitudeDelta: 0.02,
            longitudeDelta: 0.02
          }}
        >
          <Marker coordinate={{ latitude: DrugStoreLocation[1][0], longitude: DrugStoreLocation[1][1] }} />
          <Marker coordinate={{ latitude: DrugStoreLocation[2][0], longitude: DrugStoreLocation[2][1] }} />
          <Marker coordinate={{ latitude: DrugStoreLocation[3][0], longitude: DrugStoreLocation[3][1] }} />
        </MapView>
      </View>
    )
  }
}