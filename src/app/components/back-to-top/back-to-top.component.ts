import {Component, HostListener} from '@angular/core';
import {Router} from "@angular/router";

@Component({
  selector: 'app-back-to-top',
  templateUrl: './back-to-top.component.html',
  styleUrls: ['./back-to-top.component.scss']
})
export class BackToTopComponent {
  constructor(private router: Router) { }
  isAtTop = true;
  @HostListener('window:scroll', [])
  onWindowScroll() {
    // Check if the user has scrolled to the top
    this.isAtTop = (document.documentElement.scrollTop || document.body.scrollTop) === 0;
  }

  get navigateTo(){
    return `${window.location.pathname}#top`
  }

}
