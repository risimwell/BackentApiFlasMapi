import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Form } from '@angular/forms';
import { Router } from "@angular/router";


import { LoginService } from 'src/app/Servicios/login/login.service';
import { EnvioDataService } from 'src/app/Servicios/envioData/envio-data.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],

})

export class LoginComponent implements OnInit  {
  formulario:FormGroup;
  usuario:any=""
  nombre:any=""
  constructor(public formularios:FormBuilder,private loginService:LoginService,private envioData:EnvioDataService, private router:Router) {
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
          this.nombre=data.nombre
          if(this.usuario=="acudiente"){
            this.router.navigateByUrl('panelacudiente')
            console.log(data.cedula)
            this.envioData.envioCedula(data.cedula)
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

}
