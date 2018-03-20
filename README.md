# CheckSum
## By: LawlietJH

__El PIN WPS Consiste de 2 Partes (Numero + Checksum), Con Un Total de 8 Dígitos. Los Primeros 7 son un Número cualquiera y el Último Dígito es el Checksum.__

### Funciones:

 * ___GetChecksum(Numero):_ str = GetChecksum(str/int Numero)__
   
   * __Recibe Como parametro un Número de 7 Dígitos.__
     * __Puede Ser de Tipo Entero o de Tipo Cadena.__
   * __Devuelve El PIN Completo con su Correcto Checksum.__
   
 * ___IsValidPIN(Numero):_ Bool = IsValidPIN(str/int PIN)__
   
   * __Recibe Como parametro un PIN de 8 Dígitos.__
     * __Puede Ser de Tipo Entero o de Tipo Cadena.__
   * __Devuelve Un Valor Booleano: True si es Valido o False si no lo es.__
   
