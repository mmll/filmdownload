import { Injectable } from '@angular/core';
import {Observable, of} from 'rxjs'
import {ResultItemComponent} from './result-item/result-item.component'
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class FilmService {
 
  configUrl = 'http://www.zimuzu.tv/search?keyword=%E8%A5%BF%E9%83%A8%E4%B8%96%E7%95%8C';
  //document.domain = 's.ygdy8.com';
  constructor(private http: HttpClient) { }

  getResults(value){
  	return this.http.get(this.configUrl,{
        withCredentials: false
    }).subscribe(data => {
      console.log(data); // using the HttpClient instance, http to call the API then subscribe to the data and display to console
    });
  }
}
