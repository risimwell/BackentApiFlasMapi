import { NgModule, Component, ModuleWithProviders } from '@angular/core';
import {Routes, RouterModule} from '@angular/router';
import { CommonModule } from '@angular/common';
import {ReactiveFormsModule,FormsModule} from '@angular/forms';

import { AppComponent } from './app.component';

//Usuarios
import { InicioComponent } from './Componentes/inicio/inicio.component';
import { LoginComponent } from './Componentes/login/login.component';
import { SalirComponent } from './Componentes/salir/salir.component';
import { RegistrarComponent } from './Componentes/registrar/registrar.component';


//Docente
import { PanelDocenteComponent } from './Componentes/docente/panel-docente/panel-docente.component';
import { SalonesComponent } from './Componentes/docente/salones/salones.component';
import { AnunciosComponent } from './Componentes/docente/anuncios/anuncios.component';

//Acudiente
import { PanelAcudienteComponent } from './Componentes/acudiente/panel-acudiente/panel-acudiente.component';
import { NinosComponent } from './Componentes/acudiente/ninos/ninos.component';

const appRoutes:Routes=[
  //Ruta principal
  {path:'', component:InicioComponent},
  //Rutas acudiente
  {path:'panelacudiente',component:PanelAcudienteComponent},
  {path:'ninos',component:NinosComponent},
  //Rutas docente
  {path:'paneldocente',component:PanelDocenteComponent},
  {path:'salones',component:SalonesComponent},
  {path:'anuncios',component:AnunciosComponent},
  //Rutas generales
  {path:'login', component:LoginComponent},
  {path:'registrar', component:RegistrarComponent},
  {path:'salir', component:SalirComponent},
];
export const appRoutingProvider:any[]=[];

export const routing:ModuleWithProviders<any>=RouterModule.forRoot(appRoutes);

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    FormsModule
  ]
})
export class AppRoutingModule { }
