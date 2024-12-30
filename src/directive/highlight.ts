import hljs from "highlight.js";
import "highlight.js/styles/atom-one-dark.css";
import { copy } from '@/utils/copy'

const createLangEl = (language: string) => {
  const span = document.createElement("span");
  span.classList.add("btn", "btn-xs", "no-animation");
  span.innerHTML = language
  span.classList.add("bg-opacity-80");

  return span
}

const createCopyButtonEl = (codeText: string) => {
  const button = document.createElement("button");
  button.classList.add("btn", "btn-xs");
  button.innerHTML = `<svg class="feather feather-copy" fill="none" height="14" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="14" xmlns="http://www.w3.org/2000/svg"><rect height="13" rx="2" ry="2" width="13" x="9" y="9"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>复制代码`;
  button.addEventListener("click", () => {
    copy(codeText).then(() => {
      button.innerHTML = `<svg class="feather feather-check" fill="none" height="14" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="14" xmlns="http://www.w3.org/2000/svg"><polyline points="20 6 9 17 4 12"/></svg>已复制!`;
      setTimeout(() => {
        button.innerHTML = `<svg class="feather feather-copy" fill="none" height="14" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="14" xmlns="http://www.w3.org/2000/svg"><rect height="13" rx="2" ry="2" width="13" x="9" y="9"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>复制代码`;
      }, 2000)
    });
  });
  button.classList.add("bg-opacity-80");
  return button;
}



export default function (el: HTMLElement) {
  // 获取所有 <pre> 标签
  const blocks = el.querySelectorAll("pre");

  blocks.forEach((block: HTMLElement) => {
    const codeEl = block.querySelector("code");
    if (!codeEl) return;
    const language = codeEl.className.replace("language-", "");

    // 使用 highlightAuto 自动检测代码语言并高亮
    const codeText = codeEl.innerText.trim(); // 获取代码文本
    const highlightedCode = hljs.highlightAuto(codeText).value; // 高亮代码
    codeEl.innerHTML = highlightedCode; // 替换为高亮后的内容

    const html = document.createElement("div");
    html.id = `code-${language}`;
    html.classList.add("w-full", "border-base-200", "h-[30px]", "flex", "justify-between", "items-center", "border-b-[1px]", "mb-4", "pb-[10px]")
    block.prepend(html);
  });
}
