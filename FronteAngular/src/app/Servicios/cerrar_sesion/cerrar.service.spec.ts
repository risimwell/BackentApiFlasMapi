import { TestBed } from '@angular/core/testing';

import { CerrarService } from './cerrar.service';

describe('CerrarService', () => {
  let service: CerrarService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CerrarService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
