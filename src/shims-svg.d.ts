// src/shims-svg.d.ts
declare module '*.svg?component' {
    import { DefineComponent } from 'vue';
    const component: DefineComponent;
    export default component;
}