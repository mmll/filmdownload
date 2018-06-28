import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatInputModule } from '@angular/material/input';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatButtonModule } from '@angular/material/button';
import { ResultItemComponent } from './result-item/result-item.component';
import { HttpClientModule }  from '@angular/common/http';
import { FilmService} from './film.service'
@NgModule({
  declarations: [
    AppComponent,
    ResultItemComponent
  ],
  imports: [
    BrowserModule,
    MatToolbarModule, 
    MatInputModule,
    BrowserAnimationsModule,
    MatButtonModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
