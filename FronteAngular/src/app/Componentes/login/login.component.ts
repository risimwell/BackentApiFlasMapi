import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Form } from '@angular/forms';
import { Router } from "@angular/router";

import { LoginService } from 'src/app/Servicios/login/login.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  formulario:FormGroup;
  usuario:any=""
  constructor(public formularios:FormBuilder,private loginService:LoginService, private router:Router) {
      this.formulario=this.formularios.group({
        cedula:[''],
        clave:[''],
      });

     }

  ngOnInit(): void {
  }

  ingresar(formulario:any):any{
    console.log(formulario)
    this.loginService.inicioSesion(this.formulario.value).subscribe(
        (data) => {
          this.usuario=data.usuario
          console.log(this.usuario)
          if(this.usuario=="acudiente"){
            this.router.navigateByUrl('panelacudiente')
          }else{
            if(this.usuario=="docente") {
              this.router.navigateByUrl('paneldocente')
            }else {
              alert("Usuario no identificado")
              this.router.navigateByUrl('login')
            }
          }
        },
         (error) => {
          // Si hubo un error dentro del registro del usuario
          alert("Contrasena Incorrecta o Usuario no registrado")

      }
    )
  }
    /* enviarLogin():any {
      console.log("Me Presionaste");
      console.log(this.formularioLogin.value)
      this.loginService.inicioSesion(this.formularioLogin.value).subscribe(
        {
          next: () => {
            alert()
            // Si el usuario se registra con éxito
            // Redirigir el usuario a la página inicio
            this.router.navigateByUrl('')

          },
          error: () => {
            // Si hubo un error dentro del registro del usuario
            alert("Contrasena Incorrecta o Usuario no registrado")
          }
        }
      );
  } */

}
