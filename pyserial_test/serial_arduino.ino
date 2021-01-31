char data;

void setup() {
    Serial.begin(9600);
    pinMode(LED_BUILTIN, OUTPUT);
    digitalWrite(LED_BUILTIN, LOW);
}

void loop(){
    if (Serial.available() > 0) {
        data = Serial.read();
        if(data == '1'){
            digitalWrite(LED_BUILTIN, HIGH);
            delay(500);
            digitalWrite(LED_BUILTIN, LOW);
            delay(500);

        }else{
            digitalWrite(LED_BUILTIN, HIGH);
            delay(2000);
            digitalWrite(LED_BUILTIN, LOW);
            delay(500);
        }
    }
}


