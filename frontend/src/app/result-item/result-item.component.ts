import { Component, OnInit, Input } from '@angular/core';
import { MatCard } from '@angular/material/card';
import {Film} from '../entity/film';

@Component({
  selector: 'app-result-item',
  templateUrl: './result-item.component.html',
  styleUrls: ['./result-item.component.css']
})
export class ResultItemComponent implements OnInit {
  @Input('item') item: Film;
  constructor() { 

  }
  ngOnInit(){

  }
  downloadFilm(){
  	window.open(this.item.link)
  }
}
