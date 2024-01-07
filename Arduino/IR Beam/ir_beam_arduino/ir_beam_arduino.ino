void setup() {
  
  Serial.begin(9600);
  pinMode(5, INPUT_PULLUP);
  pinMode(13, OUTPUT);

}

void loop() {

  int val = digitalRead(5);

  if (val == 0) //Beam is broken
  {
    digitalWrite(13, LOW);
  }
  else
  {
    digitalWrite(13, HIGH);
  }

  Serial.print("The value of pin 5 is: ");
  Serial.println(val);

  delay(100);


}
