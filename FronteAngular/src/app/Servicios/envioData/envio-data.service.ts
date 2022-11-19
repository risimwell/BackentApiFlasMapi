import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class EnvioDataService {
  cedula_acudiente:String="";
  constructor() {
  this.cedula_acudiente
  }

  envioCedula(cedula:String){
    this.cedula_acudiente=cedula
    console.log(this.cedula_acudiente);

  }

  obtenerCedula(){
    console.log(this.cedula_acudiente);
    return this.cedula_acudiente
  }
}
