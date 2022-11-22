import { Injectable } from '@angular/core';
import { HttpClient,HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

import { Creargrupo,Objetogrupo } from 'src/app/Modelos/Salon/Salon';

const baseUrl = 'http://127.0.0.1:5000';

@Injectable({
  providedIn: 'root'
})
export class GruposService {

  constructor(private http:HttpClient) { }

  getTodo(){
    let header= new HttpHeaders().set('Type-content','aplication/json')
    return this.http.get(baseUrl,{headers:header})
  }

  getAll(): Observable<Objetogrupo[]> {
    return this.http.get<Objetogrupo[]>(baseUrl);
  }

  get(id: any): Observable<any> {
    return this.http.get(`${baseUrl}/${id}`);
  }

  create(data: Creargrupo): Observable<any> {
    console.log(data);
    console.log(this.http.post(`${baseUrl}/registrogrupo`, data))
    return this.http.post(`${baseUrl}/registrogrupo`, data);
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
