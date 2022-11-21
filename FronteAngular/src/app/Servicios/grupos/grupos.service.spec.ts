import { TestBed } from '@angular/core/testing';

import { GruposService } from './grupos.service';

describe('GruposService', () => {
  let service: GruposService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(GruposService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
