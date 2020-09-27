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

const HomeScreen = props => {
  return (
  <View style={{width: screenWidth, flexDirection: 'column', alignItems: 'stretch'}}>
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
    <View>
      {/* 첫 번째 행 */}
      <View style={{display: 'flex', flexDirection: 'row', justifyContent: "center", alignItems: 'center'}}>
        <TouchableOpacity>
          <View style={[styles.menubox, {backgroundColor: colors[1]}]}>
            <MaterialIcons name="eco" size={40} color="#000000" style={{ marginTop: -10}}/>
            <Text style={{textAlign: 'center', marginTop: 10}}>
              {'폐의약품\n환경영향정보'}
            </Text>
          </View>
        </TouchableOpacity>
        <TouchableOpacity onPress = {() => props.navigation.navigate('Info')}>
          <View style={[styles.menubox, {backgroundColor: colors[5]}]}>
            <FontAwesomeIcons name='search' size={35} color="#000000" style={{ marginTop: -10}}/>
            <Text style={{textAlign: 'center', marginTop: 15}}>
              {'폐의약품\n정보 검색'}
            </Text>
          </View>
        </TouchableOpacity>
        <TouchableOpacity onPress = {() => props.navigation.navigate('Noti')}>
          <View style={[styles.menubox, {backgroundColor: colors[3]}]}>
            <MaterialIcons name="access-alarm" size={40} color="#000000" style={{ marginTop: -10}}/>
            <Text style={{textAlign: 'center', marginTop: 10}}>
              {'수거 과정\n알리미'}
            </Text>
          </View>
        </TouchableOpacity>
      </View>
      {/* 두 번째 행 */}
      <View style={{display: 'flex', flexDirection: 'row', justifyContent: "center", alignItems: 'center'}}>
        <TouchableOpacity>
          <View style={[styles.menubox, {backgroundColor: colors[2]}]}>
            <FontistoIcons name="doctor" size={40} color="#000000" style={{ marginTop: -10}}/>
            <Text style={{textAlign: 'center', marginTop: 10}}>
              {'나의\n의사선생님'}
            </Text>
          </View>
        </TouchableOpacity>
        <TouchableOpacity>
          <View style={[styles.menubox, {backgroundColor: colors[4]}]}>
            <MaterialIcons name="control-point" size={40} color="#000000" style={{ marginTop: -10}}/>
            <Text style={{textAlign: 'center', marginTop: 10}}>
              {'폐의약품\n포인트 관리'}
            </Text>
          </View>
        </TouchableOpacity>
        <TouchableOpacity>
          <View style={[styles.menubox, {backgroundColor: colors[5]}]}>
            <EntypoIcons name="bar-graph" size={40} color="#000000" style={{ marginTop: -10}}/>
            <Text style={{textAlign: 'center', marginTop: 10}}>
              {'폐의약품\n수거 통계'}
            </Text>
          </View>
        </TouchableOpacity>
      </View>
      <View style={{display: 'flex', flexDirection: 'row', justifyContent: "center", alignItems: 'center'}}>
        <TouchableOpacity>
          <View style={[styles.menubox, {backgroundColor: colors[3]}]}>
            <FontAwesomeIcons name="newspaper-o" size={40} color="#000000" style={{ marginTop: -10}}/>
            <Text style={{textAlign: 'center', marginTop: 10}}>
              {'폐의약품\n법령/뉴스'}
            </Text>
          </View>
        </TouchableOpacity>
        <TouchableOpacity onPress = {() => props.navigation.navigate('Map')}>
          <View style={[styles.menubox, {backgroundColor: colors[1]}]}>
            <EntypoIcons name="map" size={40} color="#000000" style={{ marginTop: -10}}/>
            <Text style={{textAlign: 'center', marginTop: 10}}>
              {'폐의약품\n수거지 검색'}
            </Text>
          </View>
        </TouchableOpacity>
        <TouchableOpacity>
          <View style={[styles.menubox, {backgroundColor: colors[2]}]}>
            <AntDesign name="notification" size={40} color="#000000" style={{ marginTop: -10}}/>
            <Text style={{textAlign: 'center', marginTop: 10}}>
              {'폐의약품\n수거앱 알리기'}
            </Text>
          </View>
        </TouchableOpacity>
      </View>
    </View>
    <TouchableOpacity onPress = {() => props.navigation.navigate('UserLogin')}>
      <View style={{height: 100, backgroundColor: '#FFFFFF', justifyContent: 'center', alignItems: 'center'}}>
        <Text style={{color: '#000000', fontSize: 16, marginTop: -20, textAlign: 'center'}}>
          {'더욱 자세한 내용은 보건소 홈페이지를 참고하세요\n바로가기 >>'}
        </Text>
      </View>
    </TouchableOpacity>
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

export default HomeScreen;

