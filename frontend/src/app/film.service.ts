import { Injectable } from '@angular/core';
import {Observable, of} from 'rxjs';
import {ResultItemComponent} from './result-item/result-item.component';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Film } from './entity/film'

@Injectable({
  providedIn: 'root'
})
export class FilmService {
 
  configUrl = 'http://localhost:5000/search/';
  constructor(private http: HttpClient) { }

  getResults(value): Observable<Object>{
   var url = this.configUrl + value;
  	return this.http.get(url);
  }
}
