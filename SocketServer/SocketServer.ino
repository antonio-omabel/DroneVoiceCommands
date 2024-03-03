#include <WiFi.h>
#include <WiFiClient.h>
#include <WiFiAP.h>

const char* ssid = "";      //Set your Wifi ssid
const char* password = "";  //Set your Wifi password

const int listeningLedPin = 26;
const int buttonPin = 25;
bool startConnection = false;

WiFiServer server(10000);  //Set desired PORT

void setup() {
  Serial.begin(115200);
  pinMode(listeningLedPin, OUTPUT);
  pinMode(buttonPin, INPUT);
  TCPCommunicationSetup();
}

void loop() {
  if(startConnection){
    TCPCommunication();}
  if(digitalRead(buttonPin) == HIGH){
    startConnection=!startConnection;
  }
}

void TCPCommunicationSetup(){
  WiFi.begin(ssid, password);  //ESP32 WiFi Connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Wifi connection...");
  }
  Serial.println("Wifi connected.");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  server.begin(); //TCP server starting
  Serial.println("TCP server started.");
}

void TCPCommunication(){
  WiFiClient client = server.available(); //Connected client check
  if (client) {
    String receivedText = client.readStringUntil('\r');     //Read client string
    if(receivedText.equals("HIGH")) {
      digitalWrite(listeningLedPin, HIGH); 
    }
    else if(receivedText == "LOW"){
      digitalWrite(listeningLedPin, LOW); 
    }
    else if(receivedText!=NULL){
      Serial.print("Received text: ");
      Serial.println(receivedText);
      client.stop();  //Close connection
      Serial.println("TCP connection closed");
    }
  }
}
