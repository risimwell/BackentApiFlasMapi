import { Data } from "@angular/router";


export interface Objetogrupo{
  nombre_grupo:String;
  codigo_grupo:String;
  nombre_institucion:String;
  fecha_creacion:Data;
  cedula_docente:String;



}

export interface Creargrupo{
  nombre_grupo:String;
  codigo_grupo:String;
  nombre_institucion:String;
  fecha_creacion:String;
  cedula_docente:String;


}

export interface Objetolistar{
  nombre_grupo:String;
  codigo_grupo:String;
  fecha_creacion:String;


}
export interface Respuestagrupo{
  cursos:Objetolistar[];

}