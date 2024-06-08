// Sensor de temperatura y humedad DHT12 + ESP32

// Librerias utilizadas
#include <Arduino.h>
#include <DHT12.h>
#include <WiFi.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>

// Pin al cual estara conectado el sensor dentro del ESP32
#define DHTPIN 5    //(D5 dentro del ESP32)

// La comunicacion entre sensor y ESP32 se realiza utilizando el protocolo I cuadrado C (I2C)
// Establecemos que el objeto dht12 es de tipo DHT12 (sus propiedades se encuentran dentro de la libreria)
// Mediante el primer parametro indicamos que va a funcionar en el pin que escogimos (D5)
// Mediante el segundo parametro indicamos que la comunicacion mediante I2C utiliza un solo cable (puede utilizar dos tambien)
DHT12 dht12(DHTPIN, true);

// WiFi
const char *ssid = "Labredes"; // Nombre de la red Wi-Fi
const char *password = "Wireshark";  // Enter Wi-Fi password

// MQTT Broker
const char *mqtt_broker = "192.168.5.105";   //IP del Host
const char *topic = "Server/DHT12";   //Topic
const char *mqtt_username = "emqx";   //User
const char *mqtt_password = "public";   //Password
const int mqtt_port = 1883;   //Puerto

// Definicion de objetos para utilizar dentro del codigo
WiFiClient espClient;
PubSubClient client(espClient);

// Creacion de un String vacio de 400 caracteres para guardar el JSON llamado data
JsonDocument data;

void setup()
{
  // Inicializacion de la comunicacion serial, para mostrar los datos en alguna terminar serial de ser necesario
	Serial.begin(115200);     // 115200 Baudios para la comunicacion

  // Inicializacion del sensor mediante su metodo begin()
	dht12.begin();

  // Conexion a la red WiFi
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.println("Iniciando conexion WiFi..");
    }
    Serial.println("Conectado a la red Wi-Fi");
    //Conexion al broker
    client.setServer(mqtt_broker, mqtt_port);
    while (!client.connected()) {
        String client_id = "esp32-DHT12-";   //ID de Cliente
        client_id += String(WiFi.macAddress());
        if (client.connect(client_id.c_str(), mqtt_username, mqtt_password)) {
            Serial.println("Conectado al Broker");
        } else {
            Serial.println("Error al conectar al Broker ");
            Serial.print(client.state());
            delay(2000);
        }
    }
}

// Variable utilizada para contar el tiempo entre mediciones
int timeSinceLastRead = 0;

void loop()
{
	// Se esperan 5000 milisegundos y luego se mide
	if(timeSinceLastRead > 5000) {
		// Lectura de datos en grados Celsius
		float t12 = dht12.readTemperature();

		// Lectura de datos en grados Farenheit (se lee pero no se utiliza en el JSON)
		float f12 = dht12.readTemperature(true);

		// Lectura de la humedad en el ambiente (%)
		float h12 = dht12.readHumidity();

    // Mediante true indicamos que ya terminamos de leer datos, para luego procesarlos
		bool dht12Read = true;

		// Verificamos que los datos leidos sean numericos, en caso de no serlo, se imprime un error y no se muestran los resultados
		if (isnan(h12) || isnan(t12) || isnan(f12)) {
		  Serial.println("Error en la lectura!");

		  dht12Read = false;
		}

		if (dht12Read){
			//Indice de Calor en Farenheit
			float hif12 = dht12.computeHeatIndex(f12, h12);
			//Indice de Calor en Celsius
			float hic12 = dht12.computeHeatIndex(t12, h12, false);
			//Calculo de rocio en el ambiente en Farenheit
			float dpf12 = dht12.dewPoint(f12, h12);
			//Calculo de rocio en el ambiente en Celsius
			float dpc12 = dht12.dewPoint(t12, h12, false);


      // Imprimimos los resultados en la terminar serial
			Serial.print("DHT12 => Humedad: ");
			Serial.print(h12);
			Serial.print(" %\t");
			Serial.print("Temperatura: ");
			Serial.print(t12);
			Serial.print(" *C ");
			//Serial.print(f12);
			//Serial.print(" *F\t");
			Serial.print("  Indice de calor: ");
			Serial.print(hic12);
			Serial.print(" *C ");
			//Serial.print(hif12);
			//Serial.print(" *F");
			Serial.print("  Punto de Rocio: ");
			Serial.print(dpc12);
			Serial.print(" *C ");
			//Serial.print(dpf12);
			//Serial.println(" *F");

      //String de JSON para enviar
      //Guardo en data la clave ["clave"] con el valor correspondiente
      data["device_id"] = "DHT12";
      data["temp"] = t12;
      data["hum"] = h12;
      data["h_index"] = hic12;
      data["dew"] = dpc12;

    //Convierto el json en cadena de caracteres en C
    String jsonString;
    serializeJson(data, jsonString);
    Serial.println(jsonString);

    //Una vez armado el JSON, lo publico en el topic
    client.publish(topic, jsonString.c_str());
    client.loop();
		}
    // Reiniciamos el contador entre mediciones
		timeSinceLastRead = 0;
	}
  // Aumentamos el contador de mediciones
	delay(100);
	timeSinceLastRead += 100;
}