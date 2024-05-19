import { Signal } from 'signal-polyfill';
let needsEnqueue = true;

// 这个effect缺少隔离,所以是全局级别的
const w = new Signal.subtle.Watcher(() => {
  if (needsEnqueue) {
    needsEnqueue = false;
    queueMicrotask(processPending);
  }
});

function processPending() {
  needsEnqueue = true;

  for (const s of w.getPending()) {
    s.get();
  }

  w.watch();
}

export function effect(callback: () => (() => any) | any) {
  let cleanup: () => any;

  const computed = new Signal.Computed(() => {
    typeof cleanup === 'function' && cleanup();
    cleanup = callback();
  });

  w.watch(computed);
  computed.get();

  return () => {
    w.unwatch(computed);
    typeof cleanup === 'function' && cleanup();
  };
}
