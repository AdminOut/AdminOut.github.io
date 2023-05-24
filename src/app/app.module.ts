import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { HomePageComponent } from './pages/home-page/home-page.component';
import { NgOptimizedImage } from "@angular/common";
import { FooterComponent } from './components/footer/footer.component';
import { ResumeComponent } from './layouts/resume/resume.component';
import { MainComponent } from './layouts/main/main.component';
import { PortfolioPageComponent } from './pages/portfolio-page/portfolio-page.component';
import { CvPageComponent } from './pages/cv-page/cv-page.component';
import { BackToTopComponent } from './components/back-to-top/back-to-top.component';

@NgModule({
  declarations: [AppComponent, NavbarComponent, HomePageComponent, FooterComponent, ResumeComponent, MainComponent, PortfolioPageComponent, CvPageComponent, BackToTopComponent],
  imports: [BrowserModule, AppRoutingModule, NgOptimizedImage],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
