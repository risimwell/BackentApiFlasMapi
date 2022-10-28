import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators,  FormBuilder } from '@angular/forms';
import { Objetodocente, Creardocente } from '../../../Modelos/Docente/Docente';
import { DocenteService } from '../../../Servicios/docente/docente.service';
import { Router } from '@angular/router';


@Component({
  selector: 'app-registro-docentes',
  templateUrl: './registro-docentes.component.html',
  styleUrls: ['./registro-docentes.component.css']
})
export class RegistroDocentesComponent implements OnInit {
  //Capturamos los datos del formulario del docente

  formulario=new FormGroup (
    {
      cedula_docente: new FormControl('',Validators.required),
      nombre: new FormControl('',Validators.required),
      apellido: new FormControl('',Validators.required),
      telefono: new FormControl('',Validators.required),
      institucion: new FormControl('',Validators.required),
      clave: new FormControl('',Validators.required)


    }
  )
  docente: Objetodocente[]=[];

  constructor(private servicio_Docente:DocenteService, private formBuilder:FormBuilder, private router:Router ) { }


  ngOnInit(): void {
  }

Registrar(form:any){
    console.log("Esta entrando aca");
    const docente: Creardocente={
        cedula_docente:form.cedula_docente,
        nombre:form.nombre,
        apellido:form.apellido,
        telefono:form.telefono,
        institucion:form.instituacion,
        clave:form.clave
    }

    //Envio de datos al servicio
    this.servicio_Docente.create(docente).subscribe({
        next: () => {
          //Alert de confirmacion
          alert("Usuario registrado con exito")
          //Redireccion a la pagina
          this.router.navigateByUrl('paneldocente')
        },
        error: () => {
          // Si hubo un error dentro del registro del usuario
          alert("No se pudo realizar el registro\nVerifique e intente de nuevo")
        }
      }
    );

  }
}
