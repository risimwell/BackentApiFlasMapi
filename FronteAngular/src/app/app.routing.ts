import { NgModule, Component, ModuleWithProviders } from '@angular/core';
import {Routes, RouterModule} from '@angular/router';
import { CommonModule } from '@angular/common';
import {ReactiveFormsModule,FormsModule} from '@angular/forms';


import { AppComponent } from './app.component';



import { RegistroComponent } from './Componenetes/registro/registro.component';
import { InicioComponent } from './Componenetes/inicio/inicio.component';
import { LoginComponent } from './Componenetes/login/login.component';
import { MuroComponent } from './Componenetes/muro/muro.component';
import { SalirComponent } from './Componenetes/salir/salir.component';
import { RegistroPadresComponent } from './Componenetes/registro-padres/registro-padres.component';

const appRoutes:Routes=[
  {path:'', component: InicioComponent},//Ruta principal
  {path:'muro',component:MuroComponent}, //ruta muro
  {path:'registro',component:RegistroComponent},
  {path:'login', component:LoginComponent}, //ruta login
  {path:'salir', component:SalirComponent},// ruta salir
  {path:'registroPadres', component:RegistroPadresComponent}//ruta Registro Padres

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
