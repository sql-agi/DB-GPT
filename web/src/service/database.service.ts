import { useEffect, useState } from 'react';
import { Injectable, inject } from 'static-injector';
import { URL_PREFIX_TOKEN } from './token';
import { Signal } from 'signal-polyfill';
import { effect } from './signal/effect';
import axios from 'axios';

export class DatabaseService {
  readonly #urlPrefix = inject(URL_PREFIX_TOKEN);
  databaseList = new Signal.State<any[]>([]);
  #requestList() {
    fetch(`${this.#urlPrefix}database/list`, { method: 'get' })
      .then((res) => res.json())
      .then((value) => {
        this.databaseList.set(value);
      });
  }
  /** 请求数据库连接列表 */
  requestList() {
    useEffect(() => {
      this.#requestList();
    }, []);
  }

  getItem(id: number) {
    return axios.get(`${this.#urlPrefix}database/${id}`).then((item) => {
      return item.data;
    });
  }
  saveData(data: any) {
    if (typeof data.id !== 'undefined') {
      return axios.put(`${this.#urlPrefix}database/update/${data.id}`, data).then((value) => {
        this.#requestList();
      });
    }
    return axios.post(`${this.#urlPrefix}database/save`, data).then((value) => {
      this.#requestList();
    });
  }
  deleteItem(id: number) {
    return axios.delete(`${this.#urlPrefix}database/delete/${id}`).then((value) => {
      this.#requestList();
    });
  }
}
