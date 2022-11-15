import { TestBed } from '@angular/core/testing';

import { NinoService } from './nino.service';

describe('NinoService', () => {
  let service: NinoService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(NinoService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
