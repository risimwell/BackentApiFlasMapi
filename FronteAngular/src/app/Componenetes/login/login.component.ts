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

  formularioLogin:FormGroup;

  constructor(public formulario:FormBuilder,
    private loginService:LoginService, private router:Router) {

      this.formularioLogin=this.formulario.group({
       
        cedula:[''],
        clave:[''],
      });


     }

  ngOnInit(): void {
  }

    enviarLogin():any {
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
  }

}
