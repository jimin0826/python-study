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

const InfoScreen = props => {
  return (
    <View style={{flexDirection: 'column', alignItems: 'center', backgroundColor: 'white', minHeight: screenHeight }}>
      <Header />
      <View style={{marginTop: 10, flexDirection: 'row', justifyContent: 'center', height: 40, alignItems: 'center'}}>
        <FontistoIcons name="pills" size={30} />
        <Text style={{paddingLeft: 15, fontSize: 22, fontWeight: 'bold'}}>
          폐의약품 정보 알아보기
        </Text>
      </View>
      <View style={{height: 20}} />
      <View style={{width: screenWidth - 60, shadowColor: '#000000', shadowOffset: { width: 2, height: 10 }, 
        shadowOpacity: 0.23, shadowRadius: 2.62, elevation: 4, backgroundColor: '#FFFFFF', padding: 10, borderRadius: 10}}>
        <View style={{flexDirection: 'row', alignItems: 'center'}}>
          <MaterialCommunityIcons name="pill" size={30} color="orange" />
          <Text style={{marginLeft: 5, fontSize: 17, color: 'orange', fontWeight: 'bold'}}>
            폐의약품이란?
          </Text>
        </View>
        <View height={5} />
        <Text>
          폐의약품은 가정이나 그 밖의 장소에서 복용(사용)기한 경과나 변질, 부패 등으로 인해 복용(사용)할 수 없는 의약품을 말한다.
        </Text>
      </View>
      <View height={20} />
      <View style={{width: screenWidth - 60, shadowColor: '#000000', shadowOffset: { width: 2, height: 10 }, 
        shadowOpacity: 0.23, shadowRadius: 2.62, elevation: 4, backgroundColor: '#FFFFFF', padding: 10, borderRadius: 10}}>
        <View style={{flexDirection: 'row', alignItems: 'center'}}>
          <EntypoIcons name="tree" size={30} color="green" />
          <Text style={{marginLeft: 7, fontSize: 17, color: 'green', fontWeight: 'bold'}}>
            폐의약품의 환경오염
          </Text>
        </View>
        <View height={5} />
        <Text>
        싱크대 하수구나 생활쓰레기로 무심코 버린 폐의약품은 분해되지 않은 채로 하천
        이나 토양에 잔류하여 생태계 교란, 토양오염, 수질오염의 원인이 된다. 특히 항생
        제와 같은 의약품의 경우 물에 쉽게 분해되지 않아 사람이 오염된 물을 계속 마시
        게 되면 균주들에게 항생제 내성이 생겨 차후 세균 및 바이러스 감염 또는 수술 치
        료 및 회복을 방해하는 2차적인 피해를 발생시키게 된다.
        </Text>
      </View>
      <View height={20} />
      <View style={{width: screenWidth - 60, shadowColor: '#000000', shadowOffset: { width: 2, height: 10 }, 
        shadowOpacity: 0.23, shadowRadius: 2.62, elevation: 4, backgroundColor: '#FFFFFF', padding: 10, borderRadius: 10}}>
        <View style={{flexDirection: 'row', alignItems: 'center'}}>
          <MaterialIcons name="star-border" size={30} color="skyblue" />
          <Text style={{marginLeft: 5, fontSize: 17, color: 'skyblue', fontWeight: 'bold'}}>
            폐의약품의 처리방법
          </Text>
        </View>
        <View height={5} />
        <Text>
        약국에서 폐의약품을 수거한 후 약국에서 의약품도매협회를 통하여 보건소에 보낸
        후 보건소에서 보관하다가 자원공사 또는 자치구를 통하여 소각장으로 보내져 소각․ 처리한다. 
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

export default InfoScreen;