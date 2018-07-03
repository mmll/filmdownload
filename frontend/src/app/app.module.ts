import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { MatGridListModule, MatToolbarModule, MatInputModule, MatCardModule, MatButtonModule } from '@angular/material';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ResultItemComponent } from './result-item/result-item.component';
import { HttpClientModule }  from '@angular/common/http';
import { FilmService } from './film.service';
import { Film } from './entity/film';

@NgModule({
  declarations: [
    AppComponent,
    ResultItemComponent
  ],
  imports: [
    BrowserModule,
    MatToolbarModule, 
    MatInputModule,
    MatCardModule,
    BrowserAnimationsModule,
    MatButtonModule,
    HttpClientModule,
    MatGridListModule
  ],
  exports: [
    AppComponent,
    ResultItemComponent
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
