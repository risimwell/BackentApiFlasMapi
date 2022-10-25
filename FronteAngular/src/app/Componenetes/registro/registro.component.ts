import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Form } from '@angular/forms';
import { Router } from "@angular/router";
import { RegistrarService } from '../../Servicios/registro/registrar.service';

@Component({
  selector: 'app-registro',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.css']
})
export class RegistroComponent implements OnInit {

  formularioRegistro:FormGroup;

  constructor(public formulario:FormBuilder,
    private registrar:RegistrarService, private router: Router) { 

    this.formularioRegistro=this.formulario.group({
      nombres:[''],
      apellidos:[''],
      cedula: [''],
      clave:[''],
      telefono:[''],
      

      
    });
  }

  ngOnInit(): void {
  }
    enviarDatos():any {
      console.log("Me Presionaste");
      console.log(this.formularioRegistro.value)
      this.registrar.agregarUsuario(this.formularioRegistro.value).subscribe(
        {
          next: () => {
            // Si el usuario se registra con éxito
            // Redirigir el usuario a la página inicio
            this.router.navigateByUrl('')
          },
          error: () => {
            // Si hubo un error dentro del registro del usuario
            alert("Hubo un error con el registro del usuario")
          }
        }
      );
      
    }

  

}
