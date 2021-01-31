char data;

void setup() {
    Serial.begin(9600);
    pinMode(LED_BUILTIN, OUTPUT);
    digitalWrite(LED_BUILTIN, LOW);
}

void loop(){
    if (Serial.available() > 0) {
        data = Serial.read();
        if(data=='0'){
            digitalWrite(LED_BUILTIN, LOW);

        }else{
            digitalWrite(LED_BUILTIN, HIGH);
        }
    }
}