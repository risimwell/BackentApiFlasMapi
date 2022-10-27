import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SalonesComponent } from './salones.component';

describe('SalonesComponent', () => {
  let component: SalonesComponent;
  let fixture: ComponentFixture<SalonesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SalonesComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SalonesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
