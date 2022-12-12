import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class CerrarService {
  CERRAR: string = 'http://127.0.0.1:5000/cerrar'

  constructor(private clientHtpp: HttpClient) { }
  
  cerrarsesion():Observable<any>{
    return this.clientHtpp.get(this.CERRAR)
  }
}
