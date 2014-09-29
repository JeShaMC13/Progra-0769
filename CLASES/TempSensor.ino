#include "inc/hw_memmap.h"
#include "inc/hw_types.h"
#include "driverlib/debug.h"
#include "driverlib/sysctl.h"
#include "driverlib/adc.h"
#include "Energia.h"

unsigned long ulADC0Value[4];
volatile unsigned long ulTempAvg;
volatile unsigned long ulTempValueC;
volatile unsigned long ulTempValueDec;
volatile unsigned long ulTempValueF;

void  setup(){
  Serial.begin(115200);
  
  pinMode(PUSH1, INPUT_PULLUP);
  pinMode(GREEN_LED, OUTPUT);
  pinMode(BLUE_LED, OUTPUT);
  pinMode(RED_LED, OUTPUT);
  
  digitalWrite(RED_LED, 0);
  
  SysCtlPeripheralEnable(SYSCTL_PERIPH_ADC0);
  SysCtlADCSpeedSet(SYSCTL_ADCSPEED_125KSPS); // 250
  ADCSequenceDisable(ADC0_BASE, 1);
  ADCSequenceConfigure(ADC0_BASE, 1, ADC_TRIGGER_PROCESSOR, 0);
  ADCSequenceStepConfigure(ADC0_BASE, 1, 0, ADC_CTL_TS);
  ADCSequenceStepConfigure(ADC0_BASE, 1, 1, ADC_CTL_TS);
  ADCSequenceStepConfigure(ADC0_BASE, 1, 2, ADC_CTL_TS);
  ADCSequenceStepConfigure(ADC0_BASE, 1, 3, ADC_CTL_TS | ADC_CTL_IE | ADC_CTL_END);
  ADCSequenceEnable(ADC0_BASE, 1);
  
  byte ledStatus = 1;
  
  while(digitalRead(PUSH1)){
    digitalWrite(BLUE_LED, ledStatus);
    delay(100);
    ledStatus ^= 0x01;
  }
  digitalWrite(BLUE_LED, 0);
  digitalWrite(GREEN_LED, 1);
}

void readSensor(){
  digitalWrite(GREEN_LED, 1);
  ADCIntClear(ADC0_BASE, 1);
  ADCProcessorTrigger(ADC0_BASE, 1);
  
  while(!ADCIntStatus(ADC0_BASE, 1, false))
  {    
  }
  
  ADCSequenceDataGet(ADC0_BASE, 1, ulADC0Value);
  ulTempAvg = (ulADC0Value[0] + ulADC0Value[1] + ulADC0Value[2] + ulADC0Value[3] + 2)/4;
  ulTempValueC = (1475 - ((2475 * ulTempAvg)) / 4096);
  ulTempValueDec = ulTempValueC / 10;
  ulTempValueDec *= 10;
  ulTempValueDec = ulTempValueC - ulTempValueDec;
  ulTempValueC /= 10;
  //ulTempValueF = ((ulTempValueC * 9) + 160) / 5;
  delay(5);
  digitalWrite(GREEN_LED, 0);
  Serial.print(ulTempValueC);
  Serial.print(".");
  Serial.println(ulTempValueDec);
}

void die(){
  digitalWrite(RED_LED, 1);
  delay(2000);
  while(digitalRead(PUSH1)){; }
  digitalWrite(RED_LED, 0);
}

void loop()
{  
  while(Serial.available() > 0){
   if(Serial.read()=='a'){
     readSensor();
   }else{
     die();
   }
  }
}
