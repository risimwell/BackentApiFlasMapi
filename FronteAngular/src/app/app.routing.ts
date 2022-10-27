import { NgModule, Component, ModuleWithProviders } from '@angular/core';
import {Routes, RouterModule} from '@angular/router';
import { CommonModule } from '@angular/common';
import {ReactiveFormsModule,FormsModule} from '@angular/forms';

import { AppComponent } from './app.component';

//Usuarios
import { InicioComponent } from './Componentes/inicio/inicio.component';
import { LoginComponent } from './Componentes/login/login.component';
import { SalirComponent } from './Componentes/salir/salir.component';

//Docente
import { RegistroDocentesComponent } from './Componentes/docente/registro-docentes/registro-docentes.component';
import { PanelDocenteComponent } from './Componentes/docente/panel-docente/panel-docente.component';
import { SalonesComponent } from './Componentes/docente/salones/salones.component';
import { AnunciosComponent } from './Componentes/docente/anuncios/anuncios.component';

//Acudiente
import { RegistroAcudientesComponent } from './Componentes/acudiente/registro-acudientes/registro-acudientes.component';
import { PanelAcudienteComponent } from './Componentes/acudiente/panel-acudiente/panel-acudiente.component';
import { NinosComponent } from './Componentes/acudiente/ninos/ninos.component';
const appRoutes:Routes=[
  //Ruta principal
  {path:'', component: InicioComponent},
  //Rutas acudiente
  {path:'registroacudiente',component:RegistroAcudientesComponent},
  {path:'panelacudiente',component:PanelAcudienteComponent},
  {path:'ninos',component:NinosComponent},
  //Rutas docente
  {path:'registroDocente',component:RegistroDocentesComponent},
  {path:'panelDocente',component:PanelDocenteComponent},
  {path:'salones',component:SalonesComponent},
  {path:'anuncios',component:AnunciosComponent},
  //Rutas generales
  {path:'login', component:LoginComponent},
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
