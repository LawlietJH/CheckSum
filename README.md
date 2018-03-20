# CheckSum
## Algoritmo Checksum (Suma de Verificación) para PINs WPS de Routers Wi-Fi.
## By: LawlietJH

__El PIN WPS Consiste de 2 Partes (Número + Checksum), Con Un Total de 8 Dígitos. Los Primeros 7 son un Número cualquiera y el Último Dígito es el Checksum.__

### Funciones:

 * ___GetChecksum(Número):_ str x = GetChecksum(str/int Número)__
   
   * __Recibe Como parametro un Número de 7 Dígitos.__
     * __Puede Ser de Tipo Entero o de Tipo Cadena.__
     * __Si son Menos de 7 Dígitos, se agregaran ceros por la izquierda.__
     * __Si son Mas de 8 Dígitos, devolvera 'Error'.__
   * __Devuelve Un Valor de Tipo Cadena: Devuelve El PIN Completo con su Correcto Checksum.__
   
 * ___IsValidPIN(PIN):_ bool x = IsValidPIN(str/int PIN)__
   
   * __Recibe Como parametro un PIN de 8 Dígitos.__
     * __Puede Ser de Tipo Entero o de Tipo Cadena.__
     * __Si son Menos de 8 Dígitos, se agregaran ceros por la izquierda.__
     * __Si son Mas de 8 Dígitos, devolvera False.__
   * __Devuelve Un Valor de Tipo Booleano: True si es Valido o False si no lo es.__
   
