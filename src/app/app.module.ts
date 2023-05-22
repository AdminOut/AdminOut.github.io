import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { HomePageComponent } from './home-page/home-page.component';
import { NgOptimizedImage } from "@angular/common";
import { FooterComponent } from './footer/footer.component';

@NgModule({
  declarations: [AppComponent, NavbarComponent, HomePageComponent, FooterComponent],
  imports: [BrowserModule, AppRoutingModule, NgOptimizedImage],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
