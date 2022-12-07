import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators, FormBuilder, Form } from '@angular/forms';
import { Router } from "@angular/router";



//Objetos y clases
import { Objetodocente, Creardocente } from '../../Modelos/Docente/Docente';
import { Objetoacudiente, Crearacudiente } from '../../Modelos/Acudiente/Acudiente';
//Servicios
import { DocenteService } from '../../Servicios/docente/docente.service';
import {AcudienteService} from '../../Servicios/acudiente/acudiente.service'
import Swal from 'sweetalert2';


@Component({
  selector: 'app-registrar',
  templateUrl: './registrar.component.html',
  styleUrls: ['./registrar.component.css']
})
export class RegistrarComponent implements OnInit {


  //Declaracion de formularios
  formulario_acudiente =new FormGroup({
    cedula_acudiente: new FormControl('',Validators.required),
    nombre_acudiente: new FormControl('',Validators.required),
    apellido_acudiente: new FormControl('',Validators.required),
    telefono_acudiente: new FormControl('',Validators.required),
    clave_acudiente: new FormControl('',Validators.required),
  })

  formulario_docente=new FormGroup ({
      cedula_docente: new FormControl('',Validators.required),
      nombre_docente: new FormControl('',Validators.required),
      apellido_docente: new FormControl('',Validators.required),
      telefono_docente: new FormControl('',Validators.required),
      institucion_docente: new FormControl('',Validators.required),
      clave_docente: new FormControl('',Validators.required)
    })
  //Objetos
  docente: Objetodocente[]=[];
  acudiente: Objetoacudiente[]=[];

  constructor(private servicio_Acudiente:AcudienteService,private servicio_Docente:DocenteService, private formBuilder:FormBuilder,private router:Router) { }

  ngOnInit(): void {

  }

  //Funciones para registrar
  Registrar_acudiente(form:any){
    console.log("Esta entrando aca");
    const acudiente: Crearacudiente={
        cedula_acudiente:form.cedula_acudiente,
        nombre:form.nombre_acudiente,
        apellido:form.apellido_acudiente,
        telefono:form.telefono_acudiente,
        clave:form.clave_acudiente
    }
    //Envio de datos al servicio
    this.servicio_Acudiente.create(acudiente).subscribe({
        next: () => {
          //Alert de confirmacion
          Swal.fire(
            'Acudiente registrado con exito'
          )

          //Redireccion a la pagina
          this.router.navigateByUrl('login')

        },
        error: () => {
          // Si hubo un error dentro del registro del usuario
          Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: "No se pudo realizar el registro\nVerifique e intente de nuevo",
          })
          //alert("No se pudo realizar el registro\nVerifique e intente de nuevo")
        }
      }
    );

  }

  Registrar_docente(form:any){
    console.log("Esta entrando aca");
    const docente: Creardocente={
        cedula_docente:form.cedula_docente,
        nombre:form.nombre_docente,
        apellido:form.apellido_docente,
        telefono:form.telefono_docente,
        institucion:form.institucion_docente,
        clave:form.clave_docente
    }
    //Envio de datos al servicio
    this.servicio_Docente.create(docente).subscribe({
        next: () => {
          //Alert de confirmacion
          Swal.fire(
            'Docente registrado con exito'
          )
          //alert("Docente registrado con exito")
          //Redireccion a la pagina
          this.router.navigateByUrl('login')
        },
        error: () => {
          // Si hubo un error dentro del registro del usuario
          Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: "No se pudo realizar el registro\nVerifique e intente de nuevo",
          })
          //alert("No se pudo realizar el registro\nVerifique e intente de nuevo")
        }
      }
    );

  }

}
