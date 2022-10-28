export interface Objetodocente{
    cedula_acudiente:String;
    nombre:String;
    apellido:String;
    telefono:String;
    telefono_2:String;
    acudiente_alternativo:String;
    telefono_alternativo:String;
    clave:String;
  }
  
  export interface Creardocente{
    cedula_docente:String;
    nombre:String;
    apellido:String;
    telefono:String;
    institucion:String;
    clave:String;
  }
  
  export interface Validarusuario{
    email:String;
    password:String;
  }
  