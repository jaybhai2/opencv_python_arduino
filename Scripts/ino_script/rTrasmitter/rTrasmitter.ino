
#include <RH_ASK.h>
#include <SPI.h> // Not actually used but needed to compile
#include <FreqCounter.h>


RH_ASK driver(2000,"",3,10); // ESP8266: do not use pin 11
long int frqInt;
//String frqStr = "";
int movingSum=0;
int movingAve=0;
int count=0;
//onst char *frqStr ="";
void setup()
{
    
    pinMode(13,OUTPUT);
    Serial.begin(9600);    // Debugging only
    if (!driver.init())
         Serial.println("init failed");
}

void loop()
{
    //Serial.println(FreqCounter::f_freq);
    FreqCounter::f_comp= 12;             // Set compensation to 12
    FreqCounter::start(100);            // Start counting with gatetime of 100ms
    
    while (FreqCounter::f_ready == 0)         // wait until counter ready
    frqInt=FreqCounter::f_freq;            // read result
    Serial.println(FreqCounter::f_freq);
    String frqStr = String(frqInt);
    //frqStr.trim();
   
    if(count < 20){
      count +=1;
      
      if(count > 10){
      movingSum += frqInt;
     
      if(count = 19){
        movingAve = movingSum/9;
      }
      }
    }

    Serial.println(frqInt - 60000);
    if (!driver.init())
         Serial.println("init failed");
    
    char frqChar[sizeof(frqStr)];
    frqStr.toCharArray(frqChar, sizeof(frqChar));
    //const char *frqChar = "efaefafe";
    
    //Serial.println(frqChar);
    driver.send((uint8_t *)frqChar, strlen(frqChar));
    driver.waitPacketSent();
   
    //digitalWrite(13,HIGH);
    delay(2000);
    
    //digitalWrite(13,LOW);

}
