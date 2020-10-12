import React from "react";
import { Text, StyleSheet, View, Button, TouchableOpacity } from "react-native";


const WelcomePageScreen = props => {
  return (
    <View>
   <Text style={styles.text}>WelcomePage Screen</Text>
   <Button 
   // onPress = {() => props.navigation.navigate('WeekPlan')}
    title= "Enter to welcome page"
    />
   </View>
  );
};

const styles = StyleSheet.create({
  text: {
    fontSize: 40
  }
});

export default WelcomePageScreen;