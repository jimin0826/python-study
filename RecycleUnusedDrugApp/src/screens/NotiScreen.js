import React from "react";
import { 
  Text, 
  View,
  Button,
  Dimensions
} from "react-native";
import Header from '../Components/Header';

import MaterialIcons from 'react-native-vector-icons/MaterialIcons'
import FontistoIcons from 'react-native-vector-icons/Fontisto'
import MaterialCommunityIcons from 'react-native-vector-icons/MaterialCommunityIcons'
import EntypoIcons from 'react-native-vector-icons/Entypo'

const screenWidth = Dimensions.get('window').width
const screenHeight = Dimensions.get('window').height

const NotiScreen = props => {
  // TO-DO : 데이터 베이스에서 수거 정보 받아와서 보여주어야 함
  return (
    <View style={{flexDirection: 'column', alignItems: 'center', backgroundColor: 'white', minHeight: screenHeight }}>
      <Header />
      <View style={{marginTop: 10, flexDirection: 'row', justifyContent: 'center', height: 40, alignItems: 'center'}}>
        <FontistoIcons name="pills" size={30} />
        <Text style={{paddingLeft: 15, fontSize: 22, fontWeight: 'bold'}}>
          나의 폐의약품 수거 정보
        </Text>
      </View>
      <View style={{height: 20}} />
      <View style={{width: screenWidth - 60, shadowColor: '#000000', shadowOffset: { width: 2, height: 10 }, 
        shadowOpacity: 0.23, shadowRadius: 2.62, elevation: 4, backgroundColor: '#FFFFFF', padding: 10, borderRadius: 10}}>
        <View style={{flexDirection: 'row', alignItems: 'center'}}>
          <MaterialCommunityIcons name="pill" size={30} color="orange" />
          <Text style={{marginLeft: 5, fontSize: 17, color: 'orange', fontWeight: 'bold'}}>
            폐의약품 수거 접수
          </Text>
        </View>
        <View height={5} />
        <Text>
          강남구 하나우리약국(GN102-071203)에서 2020년 07월 12일 13:51에 폐의약품 수거를 접수하였습니다.
        </Text>
      </View>
      <View height={20} />
      <View style={{width: screenWidth - 60, shadowColor: '#000000', shadowOffset: { width: 2, height: 10 }, 
        shadowOpacity: 0.23, shadowRadius: 2.62, elevation: 4, backgroundColor: '#FFFFFF', padding: 10, borderRadius: 10}}>
        <View style={{flexDirection: 'row', alignItems: 'center'}}>
          <MaterialCommunityIcons name="pill" size={30} color="orange" />
          <Text style={{marginLeft: 5, fontSize: 17, color: 'orange', fontWeight: 'bold'}}>
            폐의약품 수거 접수
          </Text>
        </View>
        <View height={5} />
        <Text>
          강남구 하나우리약국(GN102-071302)에서 2020년 07월 13일 12:05 에 폐의약품 수거를 접수하였습니다.
        </Text>
      </View>
      <View height={20} />
      <View style={{width: screenWidth - 60, shadowColor: '#000000', shadowOffset: { width: 2, height: 10 }, 
        shadowOpacity: 0.23, shadowRadius: 2.62, elevation: 4, backgroundColor: '#FFFFFF', padding: 10, borderRadius: 10}}>
        <View style={{flexDirection: 'row', alignItems: 'center'}}>
          <MaterialCommunityIcons name="truck-delivery" size={30} color="red" />
          <Text style={{marginLeft: 5, fontSize: 17, color: 'red', fontWeight: 'bold'}}>
            폐의약품 보건소 발송
          </Text>
        </View>
        <View height={5} />
        <Text>
          강남구 하나우리약국에서 보건소로 접수하신 폐의약품이 발송되었습니다. (접수번호 : GN102-071203, GN102-071302)
        </Text>
      </View>
      <View height={20} />
      <View style={{width: screenWidth - 60, shadowColor: '#000000', shadowOffset: { width: 2, height: 10 }, 
        shadowOpacity: 0.23, shadowRadius: 2.62, elevation: 4, backgroundColor: '#FFFFFF', padding: 10, borderRadius: 10}}>
        <View style={{flexDirection: 'row', alignItems: 'center'}}>
          <MaterialIcons name="control-point" size={30} color="blue" />
          <Text style={{marginLeft: 7, fontSize: 17, color: 'blue', fontWeight: 'bold'}}>
            폐의약품 포인트 적립
          </Text>
        </View>
        <View height={5} />
        <Text>
          접수번호 : GN102-071203(5g), GN102-071302(13g)에 대한 폐의약품 수거 포인트 18PG가 적립되었습니다.
        </Text>
      </View>
      <View style={{height: 10}} />
      <View style={{position: 'absolute', bottom: 80}}>
        <Button
          onPress = {() => props.navigation.navigate('Home')}
          title= "홈으로 돌아가기"
        />
      </View>
   </View>
  );
};

export default NotiScreen;