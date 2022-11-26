import { FormGroup, Validators, FormBuilder, Form, FormControl } from '@angular/forms';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

//Objetos y clases
import { Objetogrupo, Creargrupo,Objetolistar} from 'src/app/Modelos/Salon/Salon';
import { GruposService } from '../../../Servicios/grupos/grupos.service';
import { EnvioDataService } from '../../../Servicios/envioData/envio-data.service';

@Component({
  selector: 'app-salones',
  templateUrl: './salones.component.html',
  styleUrls: ['./salones.component.css']
})
export class SalonesComponent implements OnInit {

  /* Capturar datos del formulario Grupos */

  formulario_grupos = new FormGroup({

    nombre_grupo: new FormControl ('',Validators.required),
    codigo_grupo: new FormControl('',Validators.required),
    nombre_institucion: new FormControl('',Validators.required),
    fecha_creacion: new FormControl('',Validators.required),
    codigo_anuncio: new FormControl('',Validators.required),
    cedula_docente: new FormControl('',Validators.required),
    grupo: new FormControl('',Validators.required)

  })
  //Objeto grupo
  grupo: Objetogrupo[]=[];

//formulario listar grupo
  formulario_listar= new FormGroup({

    nombre_grupo: new FormControl ('',Validators.required),
    codigo_grupo: new FormControl('',Validators.required),
    fecha_creacion: new FormControl('',Validators.required),
    grupo: new FormControl('',Validators.required)

  })

  //objeto listar
  listar: Objetolistar[]=[];

  constructor(private servicio_grupo: GruposService, private obtenerData:EnvioDataService, private formlarioGrupo:FormBuilder,private formulariolistar:FormBuilder, private router:Router) { }

  ngOnInit(): void {


  }
  Registrar_grupo (form:any){
    console.log("Estoy adentro de regitrar grupo")
    const grupo: Creargrupo={

      nombre_grupo:form.nombre_grupo,
      codigo_grupo:form.codigo_grupo,
      nombre_institucion: form.nombre_institucion,
      fecha_creacion:form.fecha_creacion,
      cedula_docente:form.cedula_docente,


    }

    console.log("Va a disparar el servicio");
    this.servicio_grupo.create(grupo).subscribe({


    })

  }}

   /*  Listar_grupo (form:any){
      console.log("Estoy adentro de listar grupo")
      const listar: Objetolistar={

        nombre_grupo:form.nombre_grupo,
        codigo_grupo:form.codigo_grupo,
        fecha_creacion:form.fecha_creacion,



      }
    }
      console.log("Va a disparar el servicio");
      this.servicio_grupo.getAll(listar).subscribe({


      }) */




