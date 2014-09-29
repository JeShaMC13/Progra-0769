void setup(){
  Serial2.begin(115200);
  Serial.begin(115200);
  pinMode(RED_LED, OUTPUT);
  pinMode(GREEN_LED, OUTPUT);
  pinMode(BLUE_LED, OUTPUT); 
  digitalWrite(RED_LED, 0);
  digitalWrite(GREEN_LED, 0);
  digitalWrite(BLUE_LED, 0);
}



unsigned int readPWMvalue(void){
  unsigned int cntVal = 0;
  unsigned int val[3]={0,0,0};
  while (cntVal < 3){
      if(Serial2.available()>0){
        val[cntVal] = Serial2.read()-48;
        cntVal++; 
      }
    }
    return val[0]*100+val[1]*10+val[2];
}

void activar(byte ch){
  char pwm[3] = {0, 0, 0};
  if (ch=='R'){ //Red
    Serial.print("RED_LED ");
    pwm[0] = readPWMvalue();
    Serial.println(pwm[0],DEC);
    analogWrite(RED_LED, pwm[0]);
  
  }else if(ch=='G'){ //Green
    Serial.print("GREEN_LED ");
    pwm[1] = readPWMvalue();
    Serial.println(pwm[1],DEC);
    analogWrite(GREEN_LED, pwm[1]);

  }else if(ch=='B'){ //Blue
    Serial.print("BLUE_LED ");  
    pwm[2] = readPWMvalue();
    Serial.println(pwm[2],DEC);
    analogWrite(BLUE_LED, pwm[2]);
  }
}

void loop(){
  byte data;
  
  if (Serial2.available()>0){
    data = Serial2.read();
    activar(data);
  } 
  
}
