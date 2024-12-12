#include <DHT.h>

#define DHTPIN 2  // Pin conectado al sensor
#define DHTTYPE DHT11  // Modelo del sensor

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Error al leer el sensor");
    return;
  }

  Serial.print("Temperatura: ");
  Serial.print(temperature);
  Serial.print(" °C, Humedad: ");
  Serial.print(humidity);
  Serial.println(" %");

  delay(2000); // Espera 2 segundos entre lecturas
}
