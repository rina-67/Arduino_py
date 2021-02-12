//int data ; //受信データを代入する変数
char d ;
int data ;

void setup() {
    Serial.begin(9600);
    pinMode(LED_BUILTIN, OUTPUT);
    digitalWrite(LED_BUILTIN, LOW);
}

void loop(){
    
    
    if (Serial.available() > 0) {
        //data = Serial.peek(); //peekだとreadのようにデータがきえることはない
        //Serial.print(data);

        d = Serial.read();
        data = d - '0';
        //printf("%d\n",data);
        //ここでpythonから2以上の値を送っても実行されません。
        //dataにはint型の値が入っていない、またはまったく違う数値を受信しているということでしょうか...

        /*
        if (data>2) {
            digitalWrite(LED_BUILTIN, HIGH);
            delay(1000);
            digitalWrite(LED_BUILTIN, LOW);
            delay(100);
        }else{
            digitalWrite(LED_BUILTIN, HIGH);
            delay(2000);
            digitalWrite(LED_BUILTIN, LOW);
            delay(100);
    
        }
        */
        


        
    
    

    
        
    /*}else{
        digitalWrite(LED_BUILTIN, HIGH);
        delay(500);
        digitalWrite(LED_BUILTIN, LOW);
        delay(500);
    */
    }

    digitalWrite(LED_BUILTIN, HIGH);
    delay(data*data);
    digitalWrite(LED_BUILTIN, LOW);
    delay(10);

    
}

/*
今の問題点
pythonからはきちんとint型の値を送っている
なのに、もしかするとarduino側ではint型ではない可能性あり
dataにデータはあるのにそれが別の型になっていて、if文も無意味に？
とりま変数の型がintかどうかしらべたい

2/11 
もしかしたらアスキー型でint 変換されてるかもしれん
１～５の値出力しても、アスキーの５０前後に変換されちゃう
でも、０の４８引いてもうまくいかないし、、
とりあえず一行ずつデバッグする方法を考えないと

2/12
pythonのコードで変数のシリアル通信での渡し方変えたらなんかできた
charで受け取ったデータをintに直すとアスキーコードになるね
(訂正)charでうけとったものはアスキーコードになる！(つまりchar型は数値でもある)
charで受け取るところが問題なのか、そのあとintに直すところが問題なのか、、
まあまた今度調べよう
これはできれば直したいけど、ASCIIで０は４８だから、それをdから引けば問題解決
よかった！
*
今更思ったけどこうゆう問題管理をgithubでやるのかな
もう少し勉強しないとな
*/

