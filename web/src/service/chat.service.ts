import { useCallback, useEffect, useState } from 'react';
import { Signal } from 'signal-polyfill';
import { effect } from './signal/effect';
import { EventStreamContentType, fetchEventSource } from '@microsoft/fetch-event-source';

interface DataFormat {
  type: string;
  title: string;
  id: string;
}
export class ChatService {
  #value = new Signal.State<DataFormat[]>([]);
  mockList: DataFormat[] = [
    { type: 'db', title: '伪数据测试123456', id: '1' },
    { type: 'db', title: '伪数据测试123456', id: '2' },
    { type: 'db', title: '伪数据测试123456', id: '3' },
    { type: 'db', title: '伪数据测试123456', id: '4' },
    { type: 'db', title: '伪数据测试123456', id: '5' },
    { type: 'db', title: '伪数据测试123456', id: '6' },
  ];
  initList() {
    useEffect(() => {
      // 模拟
      setTimeout(() => {
        this.#value.set(this.mockList);
      }, 1000);
    }, []);
  }
  getList() {
    let [value, setValue] = useState(this.#value.get());
    useEffect(() => {
      effect(() => {
        setValue(this.#value.get());
      });
    }, []);
    return value;
  }
  requestHistory(options:any) {
    let [message, setMessage] = useState<any[]>([
      { role: 'user', context: '你好吗' },
      { role: 'system', context: '# 我很好' },
    ]);

    return message;
  }
  requestChat(options:any) {
    let [message, setMessage] = useState<any>(undefined);
    // todo
    return useEffect(() => {
      // fetchEventSource('', {
      //   onmessage: (e) => {
      //     console.log(e);
      //     setMessage(e.data);
      //   },
      // });
      // setMessage()
    }, []);
    return message;
  }

  getModelList() {
    // todo 接口
    let [value, setValue] = useState<any[]>([{ label: 'chatglm3' }]);
    return value;
  }
  getDatabaseList() {
    // todo 接口
    let [value, setValue] = useState<any[]>([{ label: 'postgresql' }]);
    return value;
  }
}
