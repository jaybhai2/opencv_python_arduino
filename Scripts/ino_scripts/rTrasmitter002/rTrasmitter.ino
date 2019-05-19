
#include <RH_ASK.h>
#include <SPI.h> 

#define myCycle 5000;

boolean firstOccurance = true;

unsigned long DeltaTime2 = 0;

unsigned long freq = 0 ;
unsigned long lastDeltaTime = 0;
unsigned long deltaTime = 0;



RH_ASK driver(2000,"",3,10); // use D3 as input 

SIGNAL(TIMER1_COMPA_vect)
{
  unsigned long currentTime = micros();  //return arduino running time
  
  deltaTime =  currentTime - lastDeltaTime; //  
  lastDeltaTime = currentTime; //store currentTime for next interrupt

  if (firstOccurance)                      //make the first interupt invalid
  {
    firstOccurance = false;
  }
  else if (DeltaTime2 == 0)      //sampling storedDeltaTime as base delta time
  {
    DeltaTime2 = deltaTime;      
  }
  // Reset OCR1A
  OCR1A += myCycle;         //OCR1A = OCR1A + 5000
  //Serial.println(deltaTime);
}

void setup()
{
    
  pinMode(13,OUTPUT);
  Serial.begin(9600);    
	if (!driver.init())
         Serial.println("init failed");
  TCCR1A = 0b00000000;
  
  TCCR1B = 0b00000111;

  // Enable timer compare interrupt A 
  TIMSK1 |= (1 << OCIE1A);

  // Set OCR1A (timer A counter) to trigger interrupt on next cycle
  OCR1A = myCycle;
 
  //pinMode(13, OUTPUT);
}

void loop()
{
   String pStr = String(deltaTime);
    
   char pChar[sizeof(pStr)+1];
   pStr.toCharArray(pChar, sizeof(pChar));
   
   delay(100);
   Serial.println(pChar); 
    
   driver.send((uint8_t *)pChar, strlen(pChar));
   driver.waitPacketSent();
    
}




