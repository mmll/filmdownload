import { Component } from '@angular/core';
import {MatTableDataSource} from '@angular/material';
import {MatInputModule} from '@angular/material/input';
import {FilmService} from './film.service'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent{
  title = '';

  constructor(private filmService:FilmService){

  }
  ngOnInit(){

  }
  SearchFile(value){
  	
  	let value = this.filmService.getResults(value);
  }
}
