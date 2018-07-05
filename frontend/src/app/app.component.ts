import { Component , OnInit} from '@angular/core';
import {MatTableDataSource, MatInputModule} from '@angular/material';
import {FilmService} from './film.service';
import {Film} from './entity/film';
import {ResultItemComponent} from './result-item/result-item.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = '';
  films: Film[];

  constructor(private filmService:FilmService){

  }
  ngOnInit(){

  }
  SearchFilm(value): void{
  	this.filmService.getResults(value).subscribe(res=>{(res.result)this.films = res.result});
  }
}
