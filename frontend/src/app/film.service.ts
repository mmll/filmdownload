import { Injectable } from '@angular/core';
import {Observable, of} from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';
import {ResultItemComponent} from './result-item/result-item.component';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Film } from './entity/film';
import {MessageService} from './message.service';

@Injectable({
  providedIn: 'root'
})
export class FilmService {
 
  configUrl = 'http://localhost:5000/search/';
  constructor(
  	private http: HttpClient,
  	private messageService: MessageService) {
  }

  getResults(value): Observable<Object>{
   var url = this.configUrl + value;
  	return this.http.get(url).pipe(
  		tap(value=>this.log('fetched films')),
  		catchError(this.handleError("get films",[])));
  }

  private handleError<T>(operation = 'operation',result?: T){
  	return (error: any): Observable<T> =>{
  		console.error(error);
  		this.log('${operation} failed: ${error.message}');
  		return of(result as T);
  	}
  }

  private log(message: string){
  	this.messageService.add('HeroService:'+message);
  }
}
