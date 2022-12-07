
import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators, FormBuilder, Form } from '@angular/forms';
import { Router } from "@angular/router";

//Objetos y clases
import { Objetonino, Crearnino } from './../../../Modelos/Nino/nino';
//Servicios
import { NinoService } from './../../../Servicios/nino/nino.service';
import { EnvioDataService } from 'src/app/Servicios/envioData/envio-data.service';
import { Objetolistar } from '../../../Modelos/Nino/nino';


@Component({
  selector: 'app-ninos',
  templateUrl: './ninos.component.html',
  styleUrls: ['./ninos.component.css']
})
export class NinosComponent implements OnInit {

  //Capturar datos del formulario
  formulario_nino =new FormGroup({
    identificacion: new FormControl('',Validators.required),
    nombre: new FormControl('',Validators.required),
    apellido: new FormControl('',Validators.required),
    genero: new FormControl('',Validators.required),
    fecha_nacimiento: new FormControl('',Validators.required),
    parentesco_acudiente: new FormControl('',Validators.required),
    grupo: new FormControl('',Validators.required)
  })
  //Objeto
  lista_nino: Objetolistar[]=[];

  constructor(private servicio_nino:NinoService,private obtenerData:EnvioDataService,private formBuilder:FormBuilder,private router:Router) { }

  ngOnInit(): void {
    this.servicio_nino.getAll().subscribe(response=>{
      this.lista_nino=response.ninos;
    })
  }

  Registrar_nino(form:any){
    console.log("Esta entrando a la funcion");
    const nino: Crearnino={
        identificacion:form.identificacion,
        nombre:form.nombre,
        apellido:form.apellido,
        genero:form.genero,
        fecha_nacimiento:form.fecha_nacimiento,
        parentesco_acudiente:form.parentesco_acudiente,
        cedula_acudiente:this.obtenerData.obtenerCedula(),
        codigo_grupo:form.grupo

    }
    console.log(nino)
    console.log("Va a disparar el servicio");
    this.servicio_nino.create(nino).subscribe({
      next: () => {
        //Alert de confirmacion
        alert("Niño registrado correctamente")
        //Redireccion a la pagina
        this.router.navigateByUrl('panelacudiente')

      },
      error: () => {
        // Si hubo un error dentro del registro del usuario
        alert("No se pudo realizar el registro\nVerifique e intente de nuevo")
      }
    }
  );
  console.log(this.obtenerData.obtenerCedula())
  }

}
