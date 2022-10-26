import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder} from '@angular/forms';
import { RegistrarService } from 'src/app/Servicios/registro/registrar.service';
import { Router } from '@angular/router';


@Component({
  selector: 'app-registro-padres',
  templateUrl: './registro-padres.component.html',
  styleUrls: ['./registro-padres.component.css']
})
export class RegistroPadresComponent implements OnInit {

  formularioRegistroPadres:FormGroup;

  constructor(public formulario:FormBuilder,
    private registrar:RegistrarService, private router: Router) { 

    this.formularioRegistroPadres=this.formulario.group({
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
      console.log(this.formularioRegistroPadres.value)
      this.registrar.agregarUsuario(this.formularioRegistroPadres.value).subscribe(
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

