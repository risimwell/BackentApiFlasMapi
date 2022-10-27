import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NinosComponent } from './ninos.component';

describe('NinosComponent', () => {
  let component: NinosComponent;
  let fixture: ComponentFixture<NinosComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NinosComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NinosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
