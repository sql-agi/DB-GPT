import { useEffect, useState } from 'react';
import { Signal } from 'signal-polyfill';
import { effect } from './effect';

export function useSignal<T>(value: Signal.State<T>) {
  let [value1, setValue] = useState(value.get());
  useEffect(() => {
    effect(() => {
      setValue(value.get());
    });
  }, []);
  return value1;
}
