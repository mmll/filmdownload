import { Component , OnInit} from '@angular/core';
import {MatTableDataSource, MatInputModule} from '@angular/material';
import {FilmService} from './film.service';
import {Film} from './entity/film';
import {ResultItemComponent} from './result-item/result-item.component';
import {MatProgressBarModule} from '@angular/material/progress-bar';
import {MessageService} from './message.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = '';
  films: Film[];

  constructor(private loading:Boolean , private filmService:FilmService, private messageService: MessageService){
    this.films = [];
    this.loading = false;

  }
  ngOnInit(){

  }
  SearchFilm(value,event): void{
    if(event && event.keyCode !=13){
      return;
    }
    this.films = [];
    this.loading = true;
  	this.filmService.getResults(value).subscribe(
      res=>{
        this.films = (<any>res).result;
        this.loading = false;
     },
     res=>{
       this.messageService.add("Some Error");
       this.loading = false;
     })
  }
}
