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
import { PanelDocenteComponent } from './Componentes/docente/panel-docente/panel-docente.component';
import { SalonesComponent } from './Componentes/docente/salones/salones.component';
import { AnunciosComponent } from './Componentes/docente/anuncios/anuncios.component';

//Acudiente
import { PanelAcudienteComponent } from './Componentes/acudiente/panel-acudiente/panel-acudiente.component';
import { NinosComponent } from './Componentes/acudiente/ninos/ninos.component';
import { RegistrarComponent } from './Componentes/registrar/registrar.component';


@NgModule({
  declarations: [
    AppComponent,
    InicioComponent,
    LoginComponent,
    SalirComponent,
    PanelDocenteComponent,
    SalonesComponent,
    AnunciosComponent,
    PanelAcudienteComponent,
    NinosComponent,
    RegistrarComponent,
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
