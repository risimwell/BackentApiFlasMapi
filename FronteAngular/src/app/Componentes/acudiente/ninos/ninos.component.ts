
import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators, FormBuilder, Form } from '@angular/forms';
import { Router } from "@angular/router";

//Objetos y clases
import { Objetonino, Crearnino } from './../../../Modelos/Nino/nino';
//Servicios
import { NinoService } from './../../../Servicios/nino/nino.service';
import { EnvioDataService } from 'src/app/Servicios/envioData/envio-data.service';


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
  nino: Objetonino[]=[];

  constructor(private servicio_nino:NinoService,private obtenerData:EnvioDataService,private formBuilder:FormBuilder,private router:Router) { }

  ngOnInit(): void {
  }

  Registrar_nino(form:any){
    console.log("Esta entrando aca");
  const nino: Crearnino={
        identificacion:form.identificacion,
        nombre:form.nombre,
        apellido:form.apellido,
        genero:form.genero,
        fecha_nacimiento:form.fechanacimiento,
        parentesco_acudiente:form.parentesco,
        cedula_acudiente:this.obtenerData.obtenerCedula(),
        grupo:form.grupo

    }
    console.log(this.obtenerData.obtenerCedula())

    console.log("si manda datos desde el componenete principal")
  }

}
