
import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators, FormBuilder, Form } from '@angular/forms';
import { Router } from "@angular/router";

//Objetos y clases
import { Objetonino, Crearnino } from './../../../Modelos/Nino/nino';
//Servicios
import { NinoService } from './../../../Servicios/nino/nino.service';

@Component({
  selector: 'app-ninos',
  templateUrl: './ninos.component.html',
  styleUrls: ['./ninos.component.css']
})
export class NinosComponent implements OnInit {

  //Capturar datos del formulario
  formulario_nino =new FormGroup({
    identificacion: new FormControl('',Validators.required),
    nombre_nino: new FormControl('',Validators.required),
    apellido_nino: new FormControl('',Validators.required),
    genero: new FormControl('',Validators.required),
    fecha_nacimiento: new FormControl('',Validators.required),
    parentesco: new FormControl('',Validators.required)
  })
  //Objeto
  nino: Objetonino[]=[];

  constructor(private servicio_nino:NinoService,private formBuilder:FormBuilder,private router:Router) { }

  ngOnInit(): void {
  }

  Registrar_nino(form:any){
    console.log("Esta entrando aca");
  const nino: Crearnino={
        identificacion:form.identificacion,
        nombre:form.nombre,
        apellido:form.apellido,
        fecha_nacimiento:form.fechanacimiento,
        genero:form.genero,
        parentesco:form.parentesco
    }
    this.servicio_nino.create

    console.log("si manda datos desde el componenete principal")
  }

}
