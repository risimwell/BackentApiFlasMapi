import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RegistroPadresComponent } from './registro-padres.component';

describe('RegistroPadresComponent', () => {
  let component: RegistroPadresComponent;
  let fixture: ComponentFixture<RegistroPadresComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RegistroPadresComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RegistroPadresComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
