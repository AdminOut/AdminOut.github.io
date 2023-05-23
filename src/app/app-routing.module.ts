import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {HomePageComponent} from './pages/home-page/home-page.component';
import {ResumeComponent} from "./layouts/resume/resume.component";
import {MainComponent} from "./layouts/main/main.component";
import {CvPageComponent} from "./pages/cv-page/cv-page.component";
import {PortfolioPageComponent} from "./pages/portfolio-page/portfolio-page.component";

const routes: Routes = [
  {
    path: '', component: MainComponent, children: [
      {path: '', component: HomePageComponent},
    ]
  },
  {
    path: 'resume', component: ResumeComponent, children: [
      {path: 'cv', component: CvPageComponent},
      {path: 'portfolio', component: PortfolioPageComponent},
      {path: '',   redirectTo: '/resume/cv', pathMatch: 'full' },
    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {
}
