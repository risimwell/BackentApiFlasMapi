import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators, FormBuilder, Form } from '@angular/forms';
import { Router } from "@angular/router";
 
@Component({
  selector: 'app-ninos',
  templateUrl: './ninos.component.html',
  styleUrls: ['./ninos.component.css']
})
export class NinosComponent implements OnInit {

  //Capturar datos del formulario
  formulario_nino =new FormGroup({
    identificacion: new FormControl('',Validators.required)
  })

  constructor(private formBuilder:FormBuilder,private router:Router) { }

  ngOnInit(): void {
  }

  Registrar_nino(form:any){
    console.log("si manda datos desde el componenete principal")
  }

}
