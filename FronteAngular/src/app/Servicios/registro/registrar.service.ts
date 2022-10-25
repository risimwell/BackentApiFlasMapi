import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import {Registrado} from './personaRegistrada';

@Injectable({
  providedIn: 'root'
})
export class RegistrarService {

  API:string='http://127.0.0.1:5000/registro'


  constructor(private clientHttp:HttpClient) { }

  agregarUsuario(datosUsuarios:Registrado):Observable<any>{
    return this.clientHttp.post(this.API,datosUsuarios,{headers:{'Content-Type':'application/json'}});
  }

 
}
