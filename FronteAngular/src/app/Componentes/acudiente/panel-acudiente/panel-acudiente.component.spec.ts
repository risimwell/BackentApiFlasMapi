import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PanelAcudienteComponent } from './panel-acudiente.component';

describe('PanelAcudienteComponent', () => {
  let component: PanelAcudienteComponent;
  let fixture: ComponentFixture<PanelAcudienteComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PanelAcudienteComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PanelAcudienteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
