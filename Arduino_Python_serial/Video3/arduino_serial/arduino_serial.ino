bool serial_connection = false;

void setup() {
  Serial.begin(9600);
}

void loop() {

  if (Serial.available() > 0)
  {
    char inData = Serial.read();

    if (inData == 'i' && serial_connection == false)
    {
      Serial.println("Starting");
      serial_connection = true;
    }
    else if(inData == 'a' && serial_connection == true)
    {
      Serial.println(analogRead(0));
    }
    else if (inData == 'i' && serial_connection == true)
    {
      serial_connection = false;
    }
  }

}
