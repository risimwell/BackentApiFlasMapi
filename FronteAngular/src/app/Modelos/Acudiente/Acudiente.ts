export interface Objetoacudiente{
  cedula_acudiente:String;
  nombre:String;
  apellido:String;
  telefono:String;
  telefono_2:String;
  acudiente_alternativo:String;
  telefono_alternativo:String;
  clave:String;
}

export interface Crearacudiente{
  cedula_acudiente:String;
  nombre:String;
  apellido:String;
  telefono:String;
  clave:String;
}

export interface Validarusuario{
  email:String;
  password:String;
}
