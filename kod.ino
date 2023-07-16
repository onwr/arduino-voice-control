const int ledPin = 13;
char incomingData;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  digitalWrite(ledPin, LOW);
}

void loop() {
  if (Serial.available() > 0) {
    incomingData = Serial.read();
    
    if (incomingData == '1') {
      digitalWrite(ledPin, HIGH);
    } else if (incomingData == '0') {
      digitalWrite(ledPin, LOW);
    }
  }
}
