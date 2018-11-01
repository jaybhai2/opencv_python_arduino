
int data = 0;



void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}
void loop() {
  // put your main code here, t
  data = analogRead(3);
  Serial.println(data);
  delay(500);
}
