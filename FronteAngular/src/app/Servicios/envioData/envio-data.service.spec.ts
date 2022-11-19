import { TestBed } from '@angular/core/testing';

import { EnvioDataService } from './envio-data.service';

describe('EnvioDataService', () => {
  let service: EnvioDataService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(EnvioDataService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
