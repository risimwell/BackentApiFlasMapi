//Angular
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { routing, appRoutingProvider } from "./app.routing"
import { RouterModule } from "@angular/router"
import { AppRoutingModule } from './app.routing';
import { AppComponent } from './app.component';
import {HttpClientModule} from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

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


@NgModule({
  declarations: [
    AppComponent,
    InicioComponent,
    LoginComponent,
    SalirComponent,
    RegistroDocentesComponent,
    PanelDocenteComponent,
    SalonesComponent,
    AnunciosComponent,
    RegistroAcudientesComponent,
    PanelAcudienteComponent,
    NinosComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    routing,
    RouterModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
