import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  LOGIN: string = 'http://127.0.0.1:5000/login'

  constructor(private clientHtpp: HttpClient) { }

  inicioSesion(datoslogin:any):Observable<any>{
    return this.clientHtpp.post(this.LOGIN, datoslogin, { headers: { 'Content-Type': 'application/json' }})
  }

}
