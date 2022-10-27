import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RegistroAcudientesComponent } from './registro-acudientes.component';

describe('RegistroAcudientesComponent', () => {
  let component: RegistroAcudientesComponent;
  let fixture: ComponentFixture<RegistroAcudientesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RegistroAcudientesComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RegistroAcudientesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
