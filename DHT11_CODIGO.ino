#include <DHT.h>

#define DHTPIN 2  // Pin conectado al sensor
#define DHTTYPE DHT11  // Modelo del sensor
#define BUZZER_PIN 3  // Pin conectado al buzzer

DHT dht(DHTPIN, DHTTYPE);

float temperaturaAnterior = 0;  // Variable para almacenar la temperatura anterior

void setup() {
  Serial.begin(9600);
  dht.begin();
  pinMode(BUZZER_PIN, OUTPUT);  // Configura el pin del buzzer como salida
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


  // Si la temperatura supera el umbral crítico (ejemplo: 35°C), activa la alarma
  if (temperature >= 30.0) {  // Ajusta el umbral de temperatura crítica
    for (int i = 0; i < 10; i++) {  // Repite 10 veces el sonido rápido de alarma
      tone(BUZZER_PIN, 1000);  // Tono alto (1000Hz) para el "ruido de alarma"
      delay(100);  // Activa el buzzer por 100ms
      noTone(BUZZER_PIN);  // Apaga el buzzer
      delay(100);  // Pausa de 100ms
    }
  }

  // Si la temperatura ha cambiado significativamente (más de 2°C de diferencia), aumenta la alerta
  if (abs(temperature - temperaturaAnterior) > 2) {  // Cambios mayores a 2°C
    tone(BUZZER_PIN, 1000, 500);  // Tono rápido para alertar sobre el cambio importante
  }

  // Al final del ciclo, guardamos la temperatura para la próxima comparación
  temperaturaAnterior = temperature;

  delay(2000); // Espera 2 segundos entre lecturas
}