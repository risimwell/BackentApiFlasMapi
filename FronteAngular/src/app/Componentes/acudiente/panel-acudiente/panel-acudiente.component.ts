import { Component, OnInit, Input } from '@angular/core';
import { LoginComponent } from '../../login/login.component';
import { Router } from "@angular/router";
import Swal from 'sweetalert2';

import { CerrarService} from 'src/app/Servicios/cerrar_sesion/cerrar.service';

@Component({
  selector: 'app-panel-acudiente',
  templateUrl: './panel-acudiente.component.html',
  styleUrls: ['./panel-acudiente.component.css']
})
export class PanelAcudienteComponent implements OnInit {

  constructor(private cerrar:CerrarService,private router:Router) {
    
  }

  ngOnInit(): void {
  }
  Cerrar(){
    this.cerrar.cerrarsesion().subscribe((data)=>{
      if (data.exito) {
        Swal.fire(
          'Sesion cerrada'
        )
        this.router.navigateByUrl('login')
      }else{
        Swal.fire(
          'No se cerro'
        )
      }
    })
  }

}
