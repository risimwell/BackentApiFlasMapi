import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PanelDocenteComponent } from './panel-docente.component';

describe('PanelDocenteComponent', () => {
  let component: PanelDocenteComponent;
  let fixture: ComponentFixture<PanelDocenteComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PanelDocenteComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PanelDocenteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
