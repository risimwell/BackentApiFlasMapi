import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators, FormBuilder, Form } from '@angular/forms';
import { Router } from "@angular/router";
import { Objetoacudiente, Crearacudiente } from '../../../Modelos/Acudiente/Acudiente';
//Servicio
import {AcudienteService} from '../../../Servicios/acudiente/acudiente.service'
@Component({
  selector: 'app-registro-acudientes',
  templateUrl: './registro-acudientes.component.html',
  styleUrls: ['./registro-acudientes.component.css']
})
export class RegistroAcudientesComponent implements OnInit {
  //Capturamos los datos del formulario de los acudientes
  formulario =new FormGroup({
      cedula_acudiente: new FormControl('',Validators.required),
      nombre: new FormControl('',Validators.required),
      apellido: new FormControl('',Validators.required),
      telefono: new FormControl('',Validators.required),
      clave: new FormControl('',Validators.required),
  })
  acudiente: Objetoacudiente[]=[];

  constructor(private servicio_Acudiente:AcudienteService, private formBuilder:FormBuilder,private router:Router) { }

  ngOnInit(): void {
  }
  Registrar(form:any){
    console.log("Esta entrando aca");
    const acudiente: Crearacudiente={
        cedula_acudiente:form.cedula_acudiente,
        nombre:form.nombre,
        apellido:form.apellido,
        telefono:form.telefono,
        clave:form.clave
    }

    //Envio de datos al servicio
    this.servicio_Acudiente.create(acudiente).subscribe({
        next: () => {
          //Alert de confirmacion
          alert("Usuario registrado con exito")
          //Redireccion a la pagina
          this.router.navigateByUrl('panelacudiente')
        },
        error: () => {
          // Si hubo un error dentro del registro del usuario
          alert("No se pudo realizar el registro\nVerifique e intente de nuevo")
        }
      }
    );

  }
}
