import React from "react";
import { 
  Text, 
  StyleSheet, 
  View, 
  Button, 
  TouchableOpacity,
  Dimensions
} from "react-native";
import Header from '../Components/Header';

import MaterialIcons from 'react-native-vector-icons/MaterialIcons'
import FontAwesomeIcons from 'react-native-vector-icons/FontAwesome'
import FontistoIcons from 'react-native-vector-icons/Fontisto'
import EntypoIcons from 'react-native-vector-icons/Entypo'
import AntDesign from 'react-native-vector-icons/AntDesign'

const screenWidth = Dimensions.get('window').width
const colors = {
  0: '#6088f8',
  1: '#e3e5ff',
  2: '#d1f3c8',
  3: '#d2f0ff',
  4: '#ffdfd8',
  5: '#ffffaa'
}

const StatisticsScreen = props => {
  return (
  <View style={{width: screenWidth, flexDirection: 'column', alignItems: 'center'}}>
    <Header />
    <View style={{width: screenWidth, height: 100, flexDirection: 'column', backgroundColor: colors[0],
        justifyContent: 'space-around', paddingLeft: 15}}>
      <TouchableOpacity>
        <Text style={{color: 'white'}}>
          ⍟ 폐의약품을 분리수거 해야하는 이유  >>
        </Text>
      </TouchableOpacity>
      <TouchableOpacity>
        <Text style={{color: 'white'}}>
          ⍟ 폐의약품 수거의 경제 효과  >>
        </Text>
      </TouchableOpacity>
      <TouchableOpacity>
        <Text style={{color: 'white'}}>
          ⍟ 폐의약품이 환경에 미치는 영향  >>
        </Text>
      </TouchableOpacity>
    </View>
    <View style={{height: 30}} />
    <View style={{width: screenWidth - 60, shadowColor: '#000000', shadowOffset: { width: 2, height: 10 }, 
        shadowOpacity: 0.23, shadowRadius: 2.62, elevation: 4, backgroundColor: '#FFFFFF', padding: 10, borderRadius: 10}}>
        <View>
          <Text style={{fontSize: 16, fontWeight: 'bold', alignSelf: 'center'}}>
            저번주 수거 통계
          </Text>
        </View>
        <View style={{height: 10}} />
        <View style={{flexDirection: 'row', justifyContent: 'center'}}>
          <View style={{width: 100, height: 40,  alignItems: 'center'}}>
            <Text style={{fontSize: 16, fontWeight: 'bold'}}>
              수거 인원
            </Text>
            <Text>
              54 명
            </Text>
          </View>
          <View style={{width: 50}} />
          <View>
            <Text>
              수거 개수
            </Text>
          </View>
        </View>
    </View>
  </View>
  );
};

const styles = StyleSheet.create({
  text: {
    fontSize: 40
  },
  menubox: {
    width: screenWidth/3 -1 ,
    height: screenWidth/3 + 20,
    borderColor: 'white',
    borderWidth: 1,
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center'
  }
});

export default StatisticsScreen;

