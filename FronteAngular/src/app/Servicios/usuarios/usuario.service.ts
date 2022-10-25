import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

import { UsuariosComponent } from '../../Componenetes/usuarios/usuarios.component'; 
import { Usuario } from '../../Componenetes/usuarios/usuario'; 

const baseUrl = 'http://localhost:4000/api/usuarios';

@Injectable({
  providedIn: 'root'
})
export class UsuarioService {

  constructor(private http:HttpClient) { }
  getTodo(){
    let header= new HttpHeaders().set('Type-content','aplication/json')
    return this.http.get(baseUrl,{headers:header})
  }
  getAll(): Observable<Usuario[]> {
    return this.http.get<Usuario[]>(baseUrl);
  }
  get(id: any): Observable<Usuario> {
    return this.http.get(`${baseUrl}/${1}`);
  }

  create(data: any): Observable<any> {
    return this.http.post(baseUrl, data);
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
