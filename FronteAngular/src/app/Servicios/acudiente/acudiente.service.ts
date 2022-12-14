import { Crearacudiente,Objetoacudiente } from './../../Modelos/Acudiente/Acudiente';
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';


const baseUrl = 'http://127.0.0.1:5000'; 

@Injectable({
  providedIn: 'root'
})
export class AcudienteService {

  //Iniciamos en el constructor los metodos del HTTP
  constructor(private http:HttpClient) { }

  //Declaramos la funcion para realizar consultas al api
  getTodo(){
    let header= new HttpHeaders().set('Type-content','aplication/json')
    return this.http.get(baseUrl,{headers:header})
  }

  getAll(): Observable<Objetoacudiente[]> {
    return this.http.get<Objetoacudiente[]>(baseUrl);
  }

  get(id: any): Observable<any> {
    return this.http.get(`${baseUrl}/${id}`);
  }

  create(data: Crearacudiente): Observable<any> {
    console.log(data);
    console.log(this.http.post(`${baseUrl}/registroacudiente`, data))
    return this.http.post(`${baseUrl}/registroacudiente`, data);
  }

  update(id: any, data: any): Observable<any> {
    return this.http.put(`${baseUrl}/${id}`, data);
  }

  delete(id: any): Observable<any> {
    return this.http.delete(`${baseUrl}/${id}`);
  }

  deleteAll(): Observable<any> {
    return this.http.delete(baseUrl);
  }
}
