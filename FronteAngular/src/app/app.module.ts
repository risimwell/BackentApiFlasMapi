import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { routing, appRoutingProvider } from "./app.routing"
import { RouterModule } from "@angular/router"

import { AppRoutingModule } from './app.routing';
import { AppComponent } from './app.component';
import { UsuariosComponent } from './Componenetes/usuarios/usuarios.component';
import {HttpClientModule} from '@angular/common/http';
import { RegistroComponent } from './Componenetes/registro/registro.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { InicioComponent } from './Componenetes/inicio/inicio.component';
import { LoginComponent } from './Componenetes/login/login.component';
import { MuroComponent } from './Componenetes/muro/muro.component';
import { SalirComponent } from './Componenetes/salir/salir.component';
import { RegistroPadresComponent } from './Componenetes/registro-padres/registro-padres.component';


@NgModule({
  declarations: [
    AppComponent,
    UsuariosComponent,
    RegistroComponent,
    InicioComponent,
    LoginComponent,
    MuroComponent,
    SalirComponent,
    RegistroPadresComponent
    
    
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
