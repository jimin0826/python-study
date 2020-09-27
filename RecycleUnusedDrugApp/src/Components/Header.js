import React, { Component } from 'react'
import { 
  Text, 
  StyleSheet, 
  View, 
  Dimensions,
  Button, 
  TouchableOpacity 
} from "react-native";
import Icon from 'react-native-vector-icons/AntDesign';

const screenWidth = Dimensions.get('window').width

export default class Header extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return(
      <View style={styles.headerContainer}>
        <Text style={[styles.headerText]}>
          폐의약품 수거 앱
        </Text>
        <Icon name="bars" size={30} color="#000000" 
          style={{position: 'absolute', right: 10}}/>
      </View>
    )
  }
}

const styles = StyleSheet.create({
  headerContainer: {
    width: screenWidth,
    height: 50,
    backgroundColor: '#FFFFFF',
    alignItems: 'center',
    shadowOffset: {
      width: 2, height: 10
    },
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center'
  },
  headerText: {
    fontSize: 24,
    fontFamily: 'AppleSDGothicNeo',
    fontWeight: 'bold'
  }
});