import { TestBed } from '@angular/core/testing';

import { DocenteService } from './docente.service';

describe('DocenteService', () => {
  let service: DocenteService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(DocenteService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
