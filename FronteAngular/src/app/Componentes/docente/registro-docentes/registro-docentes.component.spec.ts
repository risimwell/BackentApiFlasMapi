import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RegistroDocentesComponent } from './registro-docentes.component';

describe('RegistroDocentesComponent', () => {
  let component: RegistroDocentesComponent;
  let fixture: ComponentFixture<RegistroDocentesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RegistroDocentesComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RegistroDocentesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
