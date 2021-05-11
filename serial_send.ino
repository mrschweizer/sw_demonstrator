
int val = 0;
int analogPin = A0;

void setup() {
  Serial.begin(56700);
}

void loop() {
  val = analogRead(analogPin);
  Serial.println(val);
  delay(10);
}
