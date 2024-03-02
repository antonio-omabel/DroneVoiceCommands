#include <WiFi.h>
#include <WiFiClient.h>
#include <WiFiAP.h>

const char* ssid = "TIM-24364625";
const char* password = "tRK27u27beDF9TX6u4uYTK6H";

WiFiServer server(10000);  //Set desired PORT

void setup() {
  Serial.begin(115200);
  TCPCommunicationSetup();
}

void loop() {
  TCPCommunication();
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
    Serial.println("New TCP connection");
    
    String receivedText = client.readStringUntil('\r');     //Read client string
    Serial.print("Received text: ");
    Serial.println(receivedText);
    client.stop();  //Close connection
    Serial.println("TCP connection closed");
    }
}