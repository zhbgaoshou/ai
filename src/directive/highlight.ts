import hljs from "highlight.js";
import "highlight.js/styles/atom-one-dark.css";
import { copy } from "@/utils/copy";

export default function (el: HTMLElement) {
  // 获取所有 <pre> 标签
  const blocks = el.querySelectorAll("pre");

  blocks.forEach((block: HTMLElement) => {
    const codeEl = block.querySelector("code");
    // 为代码块添加高亮
    hljs.highlightElement(block);

    // 创建一个复制按钮
    const copyButton = document.createElement("button");
    copyButton.innerText = "复制";
    copyButton.className = "copy-btn";

    // 设置按钮样式
    copyButton.style.position = "absolute";
    copyButton.style.right = "10px";
    copyButton.style.top = "10px";
    copyButton.style.padding = "5px 10px";
    copyButton.style.fontSize = "12px";
    copyButton.style.cursor = "pointer";

    // 为 <pre> 设置相对定位，以便按钮能够正确定位
    block.style.position = "relative";

    // 点击复制功能
    copyButton.addEventListener("click", function () {
      const code = codeEl?.innerText.trim() || ""; // 获取代码内容
      copy(code).then(() => {
        console.log("复制成功");
      });
    });
    // 将复制按钮添加到代码块中
    block.appendChild(copyButton);
  });
}
