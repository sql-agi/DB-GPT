import { useCallback, useEffect, useState } from 'react';
import { Signal } from 'signal-polyfill';
import { effect } from './signal/effect';
import { inject } from 'static-injector';
import { URL_PREFIX_TOKEN } from './token';
import axios from 'axios';

interface DataFormat {
  id: number;
  title: string;
  user_id: number;
  user_name: string;
}
interface ChatOptions {
  database_id: number;
  model: string;
  input: string;
  session_id: number;
}
export interface ChatHistory {
  message_content: string;
  message_type: string;
  session_id: number;
}
export class ChatService {
  sessionList = new Signal.State<DataFormat[]>([]);
  sessionHistory = new Signal.State<ChatHistory[]>([]);
  #requestList() {
    axios.get(`${this.#urlPrefix}/chat/sessions`).then((result) => {
      this.sessionList.set(result.data);
    });
  }
  initList() {
    this.#requestList();
  }
  #requestHistory(id: number) {
    axios.get(`${this.#urlPrefix}/chat/history/${id}`).then((result) => {
      this.sessionHistory.set(result.data);
    });
  }
  getHistory(id: number) {
    this.#requestHistory(id);
  }
  async deleteItem(id: number) {
    await axios.delete(`${this.#urlPrefix}/chat/sessions/${id}`);
    this.#requestList();
  }

  getModelList() {
    // todo 接口
    let [value, setValue] = useState([{ label: 'gpt-4', value: 'gpt-4' }]);
    return value;
  }

  readonly #urlPrefix = inject(URL_PREFIX_TOKEN);

  async chat(options: ChatOptions) {
    return axios.post(`${this.#urlPrefix}/chat/db`, options);
  }
  saveSession(title: string) {
    return axios.post(`${this.#urlPrefix}/chat/save-session`, { input: title });
  }
  getSessionList() {
    return axios.post(`${this.#urlPrefix}/chat/sessions`);
  }
}
