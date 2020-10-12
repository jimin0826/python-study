import React from "react";
import { Text, StyleSheet, View, Button, TouchableOpacity } from "react-native";


const UserLoginScreen = props => {
  return (
    <View>
   <Text style={styles.text}>UserLogIn Page</Text>
   <Button 
    onPress = {() => props.navigation.navigate('Info')}
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

export default UserLoginScreen;