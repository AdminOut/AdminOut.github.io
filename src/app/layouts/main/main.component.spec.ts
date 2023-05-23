import { ComponentFixture, TestBed } from '@angular/core/testing';
import { NavbarComponent } from '../../components/navbar/navbar.component';
import { FooterComponent } from '../../components/footer/footer.component';
import { RouterTestingModule } from '@angular/router/testing';

import { MainComponent } from './main.component';
import {BackToTopComponent} from "../../components/back-to-top/back-to-top.component";

describe('MainComponent', () => {
  let component: MainComponent;
  let fixture: ComponentFixture<MainComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [RouterTestingModule],
      declarations: [MainComponent, NavbarComponent, FooterComponent, BackToTopComponent]
    });
    fixture = TestBed.createComponent(MainComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
