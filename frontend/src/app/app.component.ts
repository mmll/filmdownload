import { Component , OnInit} from '@angular/core';
import {MatTableDataSource, MatInputModule} from '@angular/material';
import {FilmService} from './film.service';
import {Film} from './entity/film';
import {ResultItemComponent} from './result-item/result-item.component';
import {MatProgressSpinnerModule} from '@angular/material/progress-spinner';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = '';
  films: Film[];

  constructor(private filmService:FilmService){
    this.films = [];
    this.loading = false;

  }
  ngOnInit(){

  }
  SearchFilm(value): void{
    this.films = [];
    this.loading = true;
  	this.filmService.getResults(value).subscribe(res=>{
      if(res.result){
        this.films = res.result;
        this.loading = false;
      }
     });
  }
}
